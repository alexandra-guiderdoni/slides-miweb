#!/usr/bin/env node
/**
 * Audit CLI local pour la recette ShipGuard MiWeb.
 *
 * Le plugin ShipGuard installé dans Codex expose les fichiers de recette, mais
 * pas de binaire shell `sg-code-audit`. Ce script fournit donc une commande
 * locale reproductible qui audite le site servi, puis écrit les contrats JSON
 * consommés par le dashboard ShipGuard local.
 */

import { chromium } from 'playwright';
import {
  copyFileSync,
  existsSync,
  mkdirSync,
  readdirSync,
  readFileSync,
  statSync,
  writeFileSync,
} from 'fs';
import { basename, dirname, join, relative, resolve } from 'path';
import { fileURLToPath } from 'url';
import { createHash } from 'crypto';
import { spawn, spawnSync } from 'child_process';

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(SCRIPT_DIR, '..');
const RESULTS_DIR = join(SCRIPT_DIR, '_results');
const HISTORY_DIR = join(RESULTS_DIR, 'history');
const SCREENSHOTS_DIR = join(RESULTS_DIR, 'screenshots');
const PAGES_DIR = join(SCRIPT_DIR, 'pages');
const CONFIG_PATH = join(SCRIPT_DIR, '_config.yaml');
const VISUAL_RESULTS_PATH = join(RESULTS_DIR, 'visual-results.json');
const AUDIT_RESULTS_PATH = join(RESULTS_DIR, 'audit-results.json');
const AUDIT_TOON_PATH = join(RESULTS_DIR, 'audit-results.toon');
const REPORT_PATH = join(RESULTS_DIR, 'report.md');
const SERVER_PID_PATH = join(RESULTS_DIR, 'site-server.pid');

const DEFAULT_SITE = 'http://localhost:8000/miweb-objectifs-2030-v1/#slide-01';
const VALID_CATEGORIES = [
  'security',
  'race-condition',
  'silent-exception',
  'api-guard',
  'resource-leak',
  'type-mismatch',
  'dead-code',
  'infra',
  'ssr-hydration',
  'input-validation',
  'error-handling',
  'performance',
  'accessibility',
  'logic-error',
  'integration',
  'other',
];
const VALID_SEVERITIES = ['critical', 'high', 'medium', 'low'];

function parseArgs(argv) {
  const args = {};
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (!arg.startsWith('--')) {
      args._ = [...(args._ || []), arg];
      continue;
    }
    const [rawKey, rawValue] = arg.slice(2).split('=', 2);
    const key = rawKey.trim();
    if (rawValue !== undefined) {
      args[key] = rawValue;
      continue;
    }
    const next = argv[i + 1];
    if (next && !next.startsWith('--')) {
      args[key] = next;
      i += 1;
    } else {
      args[key] = true;
    }
  }
  return args;
}

function usage() {
  return `Usage: node visual-tests/sg-code-audit-cli.mjs [options]

Options:
  --site <url>                  URL cible avec hash optionnel.
                                Défaut: ${DEFAULT_SITE}
  --base-url <url>              Base URL des manifestes. Défaut: origine de --site.
  --target-only                 Audite seulement le manifeste correspondant à --site.
  --skip-variant-validation     Saute scripts/validate_variant.sh.
  --no-auto-serve               Échoue si le serveur local ne répond pas.
  --timeout-ms <number>         Timeout par page. Défaut: 15000.
  --help                        Affiche cette aide.
`;
}

function nowIso() {
  return new Date().toISOString();
}

function safeTimestamp(iso = nowIso()) {
  return iso.replace(/[:.]/g, '-');
}

function ensureDirs() {
  mkdirSync(RESULTS_DIR, { recursive: true });
  mkdirSync(HISTORY_DIR, { recursive: true });
  mkdirSync(SCREENSHOTS_DIR, { recursive: true });
}

function archiveIfExists(path, prefix, timestamp) {
  if (!existsSync(path)) return null;
  const target = join(HISTORY_DIR, `${prefix}-${safeTimestamp(timestamp)}.json`);
  copyFileSync(path, target);
  return target;
}

function cleanValue(value) {
  const trimmed = String(value ?? '').trim();
  if ((trimmed.startsWith('"') && trimmed.endsWith('"')) || (trimmed.startsWith("'") && trimmed.endsWith("'"))) {
    return trimmed.slice(1, -1);
  }
  if (trimmed === 'true') return true;
  if (trimmed === 'false') return false;
  if (/^-?\d+(\.\d+)?$/.test(trimmed)) return Number(trimmed);
  if (trimmed.startsWith('[') && trimmed.endsWith(']')) {
    return trimmed.slice(1, -1).split(',').map(item => cleanValue(item)).filter(Boolean);
  }
  return trimmed;
}

function parseManifest(text) {
  const manifest = {};
  let inSteps = false;
  let currentStep = null;

  for (const rawLine of text.split('\n')) {
    const line = rawLine.replace(/\r$/, '');
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;

    const top = line.match(/^([a-z_][a-z0-9_-]*):\s*(.*)$/i);
    if (top && !line.startsWith(' ') && !line.startsWith('\t')) {
      const [, key, value] = top;
      if (key === 'steps') {
        inSteps = true;
        manifest.steps = [];
      } else {
        inSteps = false;
        manifest[key] = cleanValue(value);
      }
      continue;
    }

    if (!inSteps) continue;

    const item = line.match(/^\s*-\s+([a-z_][a-z0-9_-]*):\s*(.*)$/i);
    if (item) {
      currentStep = { [item[1]]: cleanValue(item[2]) };
      manifest.steps.push(currentStep);
      continue;
    }

    const prop = line.match(/^\s+([a-z_][a-z0-9_-]*):\s*(.*)$/i);
    if (prop && currentStep) {
      currentStep[prop[1]] = cleanValue(prop[2]);
    }
  }

  return manifest;
}

function collectManifests() {
  return readdirSync(PAGES_DIR)
    .filter(name => name.endsWith('.yaml'))
    .sort()
    .map(file => {
      const manifestPath = join(PAGES_DIR, file);
      const manifest = parseManifest(readFileSync(manifestPath, 'utf8'));
      const id = `pages/${basename(file, '.yaml')}`;
      const openStep = (manifest.steps || []).find(step => step.action === 'open' && step.url);
      const checkStep = (manifest.steps || []).find(step => step.action === 'llm-check') || {};
      return {
        id,
        manifest: `${id}.yaml`,
        path: manifestPath,
        file,
        name: manifest.name || basename(file, '.yaml'),
        description: manifest.description || '',
        priority: manifest.priority || 'medium',
        urlTemplate: openStep?.url || '',
        screenshotName: checkStep.screenshot || `${basename(file, '.yaml')}.png`,
        severity: checkStep.severity || 'medium',
      };
    });
}

function targetManifestFilter(manifests, siteUrl, baseUrl) {
  const targetPath = siteUrl.pathname.replace(/\/+$/, '') || '/';
  return manifests.filter(manifest => {
    const url = materializeUrl(manifest.urlTemplate, baseUrl);
    if (!url) return false;
    const path = new URL(url).pathname.replace(/\/+$/, '') || '/';
    return path === targetPath;
  });
}

function materializeUrl(template, baseUrl) {
  if (!template) return '';
  return String(template).replace('{base_url}', baseUrl);
}

function resolveBaseUrl(site, explicitBaseUrl) {
  const siteUrl = new URL(site);
  const baseUrl = explicitBaseUrl || `${siteUrl.protocol}//${siteUrl.host}`;
  return { siteUrl, baseUrl };
}

async function probe(url, timeoutMs = 2500) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(url, {
      method: 'GET',
      redirect: 'follow',
      signal: controller.signal,
    });
    return { ok: response.ok, status: response.status, statusText: response.statusText };
  } catch (error) {
    return { ok: false, status: 0, statusText: error.message };
  } finally {
    clearTimeout(timer);
  }
}

function isLocalHttp(baseUrl) {
  const url = new URL(baseUrl);
  return url.protocol === 'http:' && ['localhost', '127.0.0.1', '::1'].includes(url.hostname);
}

async function ensureServer(baseUrl, noAutoServe) {
  const firstProbe = await probe(baseUrl);
  if (firstProbe.ok) {
    return { status: 'already-running', probe: firstProbe, pid: null };
  }

  if (noAutoServe || !isLocalHttp(baseUrl)) {
    return { status: 'missing', probe: firstProbe, pid: null };
  }

  const url = new URL(baseUrl);
  const port = url.port || '80';
  const bindHost = url.hostname === '::1' ? '::1' : '127.0.0.1';
  const child = spawn('python3', ['-m', 'http.server', port, '--bind', bindHost], {
    cwd: ROOT,
    detached: true,
    stdio: 'ignore',
  });
  child.unref();
  writeFileSync(SERVER_PID_PATH, `${child.pid}\n`, 'utf8');

  const deadline = Date.now() + 7000;
  let lastProbe = firstProbe;
  while (Date.now() < deadline) {
    await new Promise(resolvePromise => setTimeout(resolvePromise, 250));
    lastProbe = await probe(baseUrl, 1500);
    if (lastProbe.ok) {
      return { status: 'started', probe: lastProbe, pid: child.pid };
    }
  }
  return { status: 'start-failed', probe: lastProbe, pid: child.pid };
}

function updateConfigBaseUrl(baseUrl) {
  const current = existsSync(CONFIG_PATH) ? readFileSync(CONFIG_PATH, 'utf8') : '';
  const next = current.match(/^base_url:/m)
    ? current.replace(/^base_url:\s*.*$/m, `base_url: "${baseUrl}"`)
    : `base_url: "${baseUrl}"\n${current}`;
  if (next !== current) {
    writeFileSync(CONFIG_PATH, next, 'utf8');
    return true;
  }
  return false;
}

function consoleMessageIsActionable(message) {
  const text = message.text();
  if (/favicon\.ico/i.test(text)) return false;
  if (/Failed to load resource/i.test(text) && /status of 404/i.test(text) && /favicon/i.test(text)) return false;
  return true;
}

async function auditPage(browser, manifest, baseUrl, timeoutMs, runId) {
  const url = materializeUrl(manifest.urlTemplate, baseUrl);
  const context = await browser.newContext({
    viewport: { width: 1440, height: 1000 },
    deviceScaleFactor: 1,
  });
  const page = await context.newPage();
  const consoleErrors = [];
  const pageErrors = [];
  const startedAt = Date.now();
  let response = null;

  page.on('console', message => {
    if (message.type() === 'error' && consoleMessageIsActionable(message)) {
      consoleErrors.push(message.text());
    }
  });
  page.on('pageerror', error => {
    pageErrors.push(error.message);
  });

  try {
    response = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: timeoutMs });
    await page.waitForLoadState('networkidle', { timeout: Math.min(timeoutMs, 8000) }).catch(() => {});
    await page.waitForTimeout(250);

    const diagnostics = await page.evaluate(() => {
      const body = document.body;
      const visibleText = (body?.innerText || '').replace(/\s+/g, ' ').trim();
      const bodyBox = body?.getBoundingClientRect();
      const brokenImages = [...document.images]
        .filter(img => img.currentSrc || img.src)
        .filter(img => !img.complete || img.naturalWidth === 0 || img.naturalHeight === 0)
        .map(img => img.currentSrc || img.src)
        .slice(0, 8);
      const visibleImages = [...document.images]
        .filter(img => {
          const rect = img.getBoundingClientRect();
          const style = getComputedStyle(img);
          return rect.width > 1 && rect.height > 1 && style.visibility !== 'hidden' && style.display !== 'none';
        })
        .length;
      return {
        title: document.title,
        href: location.href,
        hash: location.hash,
        textLength: visibleText.length,
        textSample: visibleText.slice(0, 180),
        bodyWidth: Math.round(bodyBox?.width || 0),
        bodyHeight: Math.round(bodyBox?.height || 0),
        scrollWidth: Math.round(document.documentElement.scrollWidth || 0),
        scrollHeight: Math.round(document.documentElement.scrollHeight || 0),
        imageCount: document.images.length,
        visibleImages,
        brokenImages,
      };
    });

    const screenshotPath = join(SCREENSHOTS_DIR, manifest.screenshotName);
    await page.screenshot({ path: screenshotPath, fullPage: true });

    const failures = [];
    const status = response?.status() || 0;
    if (!response) failures.push('aucune réponse HTTP');
    else if (status >= 400) failures.push(`réponse HTTP ${status}`);
    if (diagnostics.textLength < 40) failures.push('contenu texte insuffisant');
    if (diagnostics.bodyWidth < 320 || diagnostics.bodyHeight < 200) failures.push('surface de page insuffisante');
    if (diagnostics.brokenImages.length) failures.push(`${diagnostics.brokenImages.length} image(s) cassée(s)`);
    if (pageErrors.length) failures.push(`${pageErrors.length} erreur(s) JavaScript pageerror`);
    if (consoleErrors.length) failures.push(`${consoleErrors.length} erreur(s) console`);

    return {
      id: manifest.id,
      manifest: manifest.manifest,
      name: manifest.name,
      url,
      status: failures.length ? 'FAIL' : 'PASS',
      duration_ms: Date.now() - startedAt,
      screenshot: `screenshots/${manifest.screenshotName}`,
      failure_reason: failures.length ? failures.join('; ') : null,
      diagnostics,
      console_errors: consoleErrors.slice(0, 5),
      page_errors: pageErrors.slice(0, 5),
      run_id: runId,
    };
  } catch (error) {
    return {
      id: manifest.id,
      manifest: manifest.manifest,
      name: manifest.name,
      url,
      status: 'ERROR',
      duration_ms: Date.now() - startedAt,
      screenshot: null,
      failure_reason: error.message,
      diagnostics: null,
      console_errors: consoleErrors.slice(0, 5),
      page_errors: pageErrors.slice(0, 5),
      run_id: runId,
    };
  } finally {
    await context.close();
  }
}

async function auditTargetUrl(browser, siteUrl, timeoutMs) {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 1000 },
    deviceScaleFactor: 1,
  });
  const page = await context.newPage();
  const pageErrors = [];
  const consoleErrors = [];
  page.on('console', message => {
    if (message.type() === 'error' && consoleMessageIsActionable(message)) {
      consoleErrors.push(message.text());
    }
  });
  page.on('pageerror', error => pageErrors.push(error.message));

  try {
    const response = await page.goto(siteUrl.href, { waitUntil: 'domcontentloaded', timeout: timeoutMs });
    await page.waitForLoadState('networkidle', { timeout: Math.min(timeoutMs, 8000) }).catch(() => {});
    const diagnostics = await page.evaluate(() => ({
      href: location.href,
      hash: location.hash,
      title: document.title,
      textLength: (document.body?.innerText || '').replace(/\s+/g, ' ').trim().length,
    }));
    await page.screenshot({ path: join(SCREENSHOTS_DIR, 'site-target.png'), fullPage: true });
    const failures = [];
    if (!response || response.status() >= 400) failures.push(`réponse HTTP ${response?.status() || 0}`);
    if (siteUrl.hash && diagnostics.hash !== siteUrl.hash) failures.push(`hash attendu ${siteUrl.hash}, obtenu ${diagnostics.hash || '(vide)'}`);
    if (diagnostics.textLength < 40) failures.push('contenu cible insuffisant');
    if (pageErrors.length) failures.push(`${pageErrors.length} pageerror`);
    if (consoleErrors.length) failures.push(`${consoleErrors.length} erreur(s) console`);
    return {
      status: failures.length ? 'FAIL' : 'PASS',
      url: siteUrl.href,
      http_status: response?.status() || 0,
      screenshot: 'screenshots/site-target.png',
      failure_reason: failures.join('; ') || null,
      diagnostics,
      console_errors: consoleErrors.slice(0, 5),
      page_errors: pageErrors.slice(0, 5),
    };
  } catch (error) {
    return {
      status: 'ERROR',
      url: siteUrl.href,
      http_status: 0,
      screenshot: null,
      failure_reason: error.message,
      diagnostics: null,
      console_errors: consoleErrors.slice(0, 5),
      page_errors: pageErrors.slice(0, 5),
    };
  } finally {
    await context.close();
  }
}

function variantSlugsFromManifests(manifests) {
  const slugs = new Set();
  for (const manifest of manifests) {
    if (!manifest.urlTemplate) continue;
    const urlPath = manifest.urlTemplate.replace('{base_url}', 'http://example.test');
    const pathname = new URL(urlPath).pathname;
    const slug = pathname.split('/').filter(Boolean)[0];
    if (!slug) continue;
    const slugDir = join(ROOT, slug);
    if (
      existsSync(slugDir)
      && existsSync(join(slugDir, 'index.html'))
      && existsSync(join(slugDir, 'alternatives.html'))
      && existsSync(join(slugDir, 'accessibilite.html'))
      && existsSync(join(slugDir, 'tests'))
    ) {
      slugs.add(slug);
    }
  }
  return [...slugs].sort();
}

function tail(text, maxChars = 1600) {
  const value = String(text || '').trim();
  if (value.length <= maxChars) return value;
  return value.slice(value.length - maxChars);
}

function runValidation(slug) {
  const startedAt = Date.now();
  const result = spawnSync('bash', ['scripts/validate_variant.sh', slug], {
    cwd: ROOT,
    encoding: 'utf8',
    maxBuffer: 10 * 1024 * 1024,
  });
  return {
    slug,
    command: `bash scripts/validate_variant.sh ${slug}`,
    status: result.status === 0 ? 'PASS' : 'FAIL',
    exit_code: result.status,
    duration_ms: Date.now() - startedAt,
    stdout_tail: tail(result.stdout),
    stderr_tail: tail(result.stderr),
  };
}

function statusCounts(tests) {
  return tests.reduce((acc, test) => {
    const status = test.status || 'ERROR';
    acc[status.toLowerCase()] = (acc[status.toLowerCase()] || 0) + 1;
    return acc;
  }, { pass: 0, fail: 0, error: 0, stale: 0, skipped: 0 });
}

function bugFromVisualTest(test, index) {
  return {
    id: `site-visual-${String(index + 1).padStart(3, '0')}`,
    severity: test.status === 'ERROR' ? 'high' : 'medium',
    category: test.failure_reason?.includes('image') ? 'accessibility' : 'logic-error',
    subcategory: 'site-page-rendering',
    file: test.manifest,
    line: 1,
    title: `Échec de rendu : ${test.name}`,
    description: `${test.url} ne satisfait pas le contrôle de rendu local : ${test.failure_reason}.`,
    fix_applied: false,
    fix_commit: '',
    confidence: 'high',
    verification_score: null,
    verified: null,
    impacted_routes: [new URL(test.url).pathname],
    lifecycle: 'new',
  };
}

function bugFromValidation(validation, index) {
  return {
    id: `site-validation-${String(index + 1).padStart(3, '0')}`,
    severity: 'high',
    category: 'integration',
    subcategory: 'variant-validation',
    file: validation.slug,
    line: 1,
    title: `Validation échouée : ${validation.slug}`,
    description: `La commande ${validation.command} échoue avec le code ${validation.exit_code}. ${validation.stderr_tail || validation.stdout_tail || ''}`.trim(),
    fix_applied: false,
    fix_commit: '',
    confidence: 'high',
    verification_score: null,
    verified: null,
    impacted_routes: [`/${validation.slug}/`],
    lifecycle: 'new',
  };
}

function bugFromTarget(target, index) {
  return {
    id: `site-target-${String(index + 1).padStart(3, '0')}`,
    severity: target.status === 'ERROR' ? 'critical' : 'high',
    category: 'infra',
    subcategory: 'target-url',
    file: 'site local',
    line: 1,
    title: 'URL cible locale non conforme',
    description: `${target.url} échoue au contrôle direct : ${target.failure_reason}.`,
    fix_applied: false,
    fix_commit: '',
    confidence: 'high',
    verification_score: null,
    verified: null,
    impacted_routes: [new URL(target.url).pathname],
    lifecycle: 'new',
  };
}

function summarizeBugs(bugs) {
  const bySeverity = Object.fromEntries(VALID_SEVERITIES.map(severity => [severity, 0]));
  const byCategory = Object.fromEntries(VALID_CATEGORIES.map(category => [category, 0]));
  for (const bug of bugs) {
    if (bySeverity[bug.severity] !== undefined) bySeverity[bug.severity] += 1;
    else bySeverity.low += 1;
    if (byCategory[bug.category] !== undefined) byCategory[bug.category] += 1;
    else byCategory.other += 1;
  }
  return { bySeverity, byCategory };
}

function promptHash(input) {
  return createHash('sha256').update(input).digest('hex');
}

function writeVisualResults({ runId, timestamp, baseUrl, selectedManifests, visualTests, durationMs }) {
  const counts = statusCounts(visualTests);
  const data = {
    schema_version: '1.0',
    run_id: runId,
    timestamp,
    base_url: baseUrl,
    scope: {
      mode: selectedManifests.length === collectManifests().length ? 'full' : 'target-only',
      selected_total: selectedManifests.length,
      full_suite_total: collectManifests().length,
      selected_manifests: selectedManifests.map(item => item.manifest),
    },
    summary: {
      total: visualTests.length,
      pass: counts.pass,
      fail: counts.fail,
      error: counts.error,
      stale: counts.stale,
      skipped: counts.skipped,
      duration_ms: durationMs,
    },
    tests: visualTests.map(test => ({
      id: test.id,
      manifest: test.manifest,
      name: test.name,
      url: test.url,
      status: test.status,
      duration_ms: test.duration_ms,
      screenshot: test.screenshot,
      failure_reason: test.failure_reason,
    })),
  };
  writeFileSync(VISUAL_RESULTS_PATH, JSON.stringify(data, null, 2), 'utf8');
  return data;
}

function renderMarkdownReport({ timestamp, site, baseUrl, targetResult, visualTests, validations, bugs, serverInfo, archived }) {
  const visualCounts = statusCounts(visualTests);
  const validationsTotal = validations.length;
  const validationsPass = validations.filter(item => item.status === 'PASS').length;
  const lines = [];
  lines.push('# Audit ShipGuard CLI local - MiWeb');
  lines.push('');
  lines.push(`Date : ${timestamp}`);
  lines.push(`Site cible : ${site}`);
  lines.push(`Base URL : ${baseUrl}`);
  lines.push(`Serveur local : ${serverInfo.status}${serverInfo.pid ? ` (PID ${serverInfo.pid})` : ''}`);
  lines.push(`Archives créées : ${archived.filter(Boolean).length}`);
  lines.push('');
  lines.push('## Résumé');
  lines.push('');
  lines.push(`- Bugs site détectés : ${bugs.length}`);
  lines.push(`- URL cible : ${targetResult.status}${targetResult.failure_reason ? ` - ${targetResult.failure_reason}` : ''}`);
  lines.push(`- Tests visuels : ${visualCounts.pass}/${visualTests.length} PASS, ${visualCounts.fail} FAIL, ${visualCounts.error} ERROR`);
  lines.push(`- Validations variantes : ${validationsPass}/${validationsTotal} PASS`);
  lines.push('');
  lines.push('## Phases');
  lines.push('');
  lines.push('| Phase | Statut | Preuve |');
  lines.push('| --- | --- | --- |');
  lines.push(`| Prévol serveur | ${serverInfo.probe?.ok ? 'PASS' : 'FAIL'} | ${baseUrl} répond avec HTTP ${serverInfo.probe?.status ?? 0} |`);
  lines.push(`| URL cible | ${targetResult.status} | Capture ${targetResult.screenshot || 'non produite'} |`);
  lines.push(`| Parcours manifestes | ${visualCounts.fail || visualCounts.error ? 'FAIL' : 'PASS'} | ${visualTests.length} page(s) auditée(s) |`);
  lines.push(`| Validations variantes | ${validationsPass === validationsTotal ? 'PASS' : 'FAIL'} | ${validationsTotal} commande(s) validate_variant.sh |`);
  lines.push('');
  lines.push('## Tests visuels');
  lines.push('');
  lines.push('| Manifeste | Statut | URL |');
  lines.push('| --- | --- | --- |');
  for (const test of visualTests) {
    lines.push(`| ${test.manifest} | ${test.status} | ${test.url} |`);
  }
  lines.push('');
  lines.push('## Validations variantes');
  lines.push('');
  lines.push('| Variante | Statut | Durée |');
  lines.push('| --- | --- | --- |');
  for (const validation of validations) {
    lines.push(`| ${validation.slug} | ${validation.status} | ${validation.duration_ms} ms |`);
  }
  if (bugs.length) {
    lines.push('');
    lines.push('## Bugs');
    lines.push('');
    for (const bug of bugs) {
      lines.push(`- ${bug.id} [${bug.severity}] ${bug.title} : ${bug.description}`);
    }
  }
  lines.push('');
  return `${lines.join('\n')}\n`;
}

function renderToon({ timestamp, site, baseUrl, visualTests, validations, bugs }) {
  const visualCounts = statusCounts(visualTests);
  const validationsPass = validations.filter(item => item.status === 'PASS').length;
  return [
    'audit:',
    '  tool: sg-code-audit-cli-local',
    `  timestamp: ${timestamp}`,
    `  site: ${site}`,
    `  base_url: ${baseUrl}`,
    `  bugs: ${bugs.length}`,
    `  visual: ${visualCounts.pass}/${visualTests.length} PASS`,
    `  validations: ${validationsPass}/${validations.length} PASS`,
    'bugs:',
    ...(
      bugs.length
        ? bugs.map(bug => `  - id: ${bug.id}\n    severity: ${bug.severity}\n    category: ${bug.category}\n    title: ${bug.title}`)
        : ['  []']
    ),
    '',
  ].join('\n');
}

function buildAuditResults({
  timestamp,
  runId,
  site,
  baseUrl,
  mode,
  targetResult,
  visualTests,
  validations,
  bugs,
  durationMs,
  archived,
  serverInfo,
  configUpdated,
}) {
  const bugSummary = summarizeBugs(bugs);
  const visualCounts = statusCounts(visualTests);
  const validationsPass = validations.filter(item => item.status === 'PASS').length;
  const prompt = `sg-code-audit local MiWeb\nsite=${site}\nbase=${baseUrl}\nmode=${mode}`;
  const allRoutes = [...new Set(visualTests.map(test => new URL(test.url).pathname))];
  return {
    schema_version: '1.0',
    tool: 'sg-code-audit-cli-local',
    repo: 'miweb-objectifs-2030',
    timestamp,
    mode,
    prompt_hash: promptHash(prompt),
    rounds: 1,
    agent_count: 4,
    agents: [
      {
        id: 'preflight',
        label: 'Serveur local et URL cible',
        status: targetResult.status === 'PASS' && serverInfo.probe?.ok ? 'completed' : 'failed',
        files_audited: 0,
        bugs_found: targetResult.status === 'PASS' ? 0 : 1,
        duration_ms: targetResult.duration_ms || null,
        paths: [site],
      },
      {
        id: 'visual',
        label: 'Parcours visuel Playwright',
        status: visualCounts.fail || visualCounts.error ? 'failed' : 'completed',
        files_audited: visualTests.length,
        bugs_found: visualCounts.fail + visualCounts.error,
        duration_ms: visualTests.reduce((total, test) => total + (test.duration_ms || 0), 0),
        paths: visualTests.map(test => test.manifest),
      },
      {
        id: 'validation',
        label: 'Validation HTML et tests de variantes',
        status: validationsPass === validations.length ? 'completed' : 'failed',
        files_audited: validations.length,
        bugs_found: validations.length - validationsPass,
        duration_ms: validations.reduce((total, item) => total + item.duration_ms, 0),
        paths: validations.map(item => item.slug),
      },
      {
        id: 'report',
        label: 'Contrats dashboard ShipGuard',
        status: 'completed',
        files_audited: 3,
        bugs_found: 0,
        duration_ms: null,
        paths: [
          relative(ROOT, VISUAL_RESULTS_PATH),
          relative(ROOT, AUDIT_RESULTS_PATH),
          relative(ROOT, REPORT_PATH),
        ],
      },
    ],
    scope_info: {
      mode,
      site_url: site,
      base_url: baseUrl,
      report_only: true,
      official_binary_exposed: false,
      note: 'Le plugin ShipGuard local ne fournit pas de binaire shell sg-code-audit dans cette session ; ce wrapper CLI local exécute les phases vérifiables sur le site servi.',
      config_updated: configUpdated,
      server: {
        status: serverInfo.status,
        pid: serverInfo.pid,
        probe_status: serverInfo.probe?.status ?? 0,
      },
      archived_previous_results: archived.filter(Boolean).map(item => relative(ROOT, item)),
      visual_manifests: visualTests.length,
      validations: validations.length,
    },
    summary: {
      total_bugs: bugs.length,
      by_severity: bugSummary.bySeverity,
      by_category: bugSummary.byCategory,
      files_audited: visualTests.length + validations.length,
      files_modified: 0,
      duration_ms: durationMs,
      risk_score: Math.min(10, bugs.reduce((score, bug) => {
        if (bug.severity === 'critical') return score + 4;
        if (bug.severity === 'high') return score + 3;
        if (bug.severity === 'medium') return score + 2;
        return score + 1;
      }, 0)),
      lifecycle: {
        new: bugs.length,
        persistent: 0,
        fixed: 0,
        not_rechecked: 0,
        compared_to: archived.find(Boolean) ? basename(archived.find(Boolean)) : null,
      },
    },
    impacted_ui_routes: bugs.length
      ? bugs.map(bug => ({
        route: bug.impacted_routes?.[0] || '/',
        reason: bug.title,
        severity: bug.severity,
        bug_count: 1,
      }))
      : allRoutes.map(route => ({
        route,
        reason: 'Route auditée sans bug détecté',
        severity: 'none',
        bug_count: 0,
      })),
    impacted_backend: [],
    verification: {
      checked: 1 + visualTests.length + validations.length,
      confirmed: (targetResult.status === 'PASS' ? 1 : 0) + visualCounts.pass + validationsPass,
      uncertain: 0,
      rejected: bugs.length,
      skipped: 0,
    },
    bugs,
    unverified_bugs: [],
    accepted_bugs: [],
    fixed_since_last_run: [],
    evidence: [
      {
        command: `node visual-tests/sg-code-audit-cli.mjs --site ${site}`,
        result: `${bugs.length} bug(s), ${visualCounts.pass}/${visualTests.length} tests visuels PASS, ${validationsPass}/${validations.length} validations PASS`,
      },
      {
        command: 'Playwright chromium page.goto + screenshots',
        result: `${visualTests.length} capture(s) dans visual-tests/_results/screenshots`,
      },
      {
        command: 'bash scripts/validate_variant.sh <slug>',
        result: `${validationsPass}/${validations.length} variantes validées`,
      },
    ],
  };
}

function runBuildReview() {
  const result = spawnSync('node', ['visual-tests/build-review.mjs'], {
    cwd: ROOT,
    encoding: 'utf8',
    maxBuffer: 4 * 1024 * 1024,
  });
  return {
    status: result.status === 0 ? 'PASS' : 'FAIL',
    exit_code: result.status,
    stdout_tail: tail(result.stdout),
    stderr_tail: tail(result.stderr),
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    process.stdout.write(usage());
    return;
  }

  const startedAt = Date.now();
  const timestamp = nowIso();
  const runId = `site-cli-${safeTimestamp(timestamp)}`;
  const site = String(args.site || DEFAULT_SITE);
  const { siteUrl, baseUrl } = resolveBaseUrl(site, args['base-url'] ? String(args['base-url']) : null);
  const timeoutMs = Number(args['timeout-ms'] || 15000);
  const mode = args['target-only'] ? 'target-only' : 'full-site-local-cli';

  ensureDirs();
  const archived = [
    archiveIfExists(AUDIT_RESULTS_PATH, 'audit-results-before-site-cli', timestamp),
    archiveIfExists(VISUAL_RESULTS_PATH, 'visual-results-before-site-cli', timestamp),
  ];
  const configUpdated = updateConfigBaseUrl(baseUrl);
  const manifests = collectManifests();
  const selectedManifests = args['target-only']
    ? targetManifestFilter(manifests, siteUrl, baseUrl)
    : manifests;
  if (!selectedManifests.length) {
    throw new Error('Aucun manifeste sélectionné pour l’audit.');
  }

  const serverInfo = await ensureServer(baseUrl, Boolean(args['no-auto-serve']));
  if (!serverInfo.probe?.ok) {
    throw new Error(`Serveur local indisponible sur ${baseUrl} : ${serverInfo.probe?.statusText || 'probe failed'}`);
  }

  const browser = await chromium.launch();
  const targetResult = await auditTargetUrl(browser, siteUrl, timeoutMs);
  const visualTests = [];
  for (const manifest of selectedManifests) {
    visualTests.push(await auditPage(browser, manifest, baseUrl, timeoutMs, runId));
  }
  await browser.close();

  const validationSlugs = args['skip-variant-validation'] ? [] : variantSlugsFromManifests(selectedManifests);
  const validations = validationSlugs.map(runValidation);

  const targetBug = targetResult.status === 'PASS' ? [] : [bugFromTarget(targetResult, 0)];
  const visualBugs = visualTests
    .filter(test => test.status !== 'PASS')
    .map((test, index) => bugFromVisualTest(test, index));
  const validationBugs = validations
    .filter(validation => validation.status !== 'PASS')
    .map((validation, index) => bugFromValidation(validation, index));
  const bugs = [...targetBug, ...visualBugs, ...validationBugs];

  const durationMs = Date.now() - startedAt;
  writeVisualResults({ runId, timestamp, baseUrl, selectedManifests, visualTests, durationMs });
  writeFileSync(REPORT_PATH, renderMarkdownReport({
    timestamp,
    site,
    baseUrl,
    targetResult,
    visualTests,
    validations,
    bugs,
    serverInfo,
    archived,
  }), 'utf8');
  writeFileSync(AUDIT_TOON_PATH, renderToon({ timestamp, site, baseUrl, visualTests, validations, bugs }), 'utf8');
  writeFileSync(AUDIT_RESULTS_PATH, JSON.stringify(buildAuditResults({
    timestamp,
    runId,
    site,
    baseUrl,
    mode,
    targetResult,
    visualTests,
    validations,
    bugs,
    durationMs,
    archived,
    serverInfo,
    configUpdated,
  }), null, 2), 'utf8');

  const reviewResult = runBuildReview();
  const visualCounts = statusCounts(visualTests);
  const validationsPass = validations.filter(item => item.status === 'PASS').length;
  process.stdout.write([
    `Audit terminé: ${bugs.length} bug(s)`,
    `URL cible: ${targetResult.status}`,
    `Visuel: ${visualCounts.pass}/${visualTests.length} PASS`,
    `Validations: ${validationsPass}/${validations.length} PASS`,
    `Dashboard: ${reviewResult.status}`,
    `Rapport: ${relative(ROOT, AUDIT_RESULTS_PATH)}`,
    '',
  ].join('\n'));

  if (bugs.length || reviewResult.status !== 'PASS') {
    process.exitCode = 1;
  }
}

main().catch(error => {
  console.error(`Erreur audit: ${error.message}`);
  process.exitCode = 1;
});
