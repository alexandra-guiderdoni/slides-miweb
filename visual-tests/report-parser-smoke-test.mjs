#!/usr/bin/env node

import { copyFileSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'fs';
import { tmpdir } from 'os';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { execFileSync } from 'child_process';
import assert from 'node:assert/strict';

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const SOURCE_BUILD = join(SCRIPT_DIR, 'build-review.mjs');
const SOURCE_TEMPLATE = join(SCRIPT_DIR, '_review-template.html');

function writeFile(path, lines) {
  writeFileSync(path, `${lines.join('\n')}\n`, 'utf8');
}

function writeJson(path, value) {
  writeFileSync(path, `${JSON.stringify(value, null, 2)}\n`, 'utf8');
}

function createManifest(root, id, name) {
  writeFile(join(root, `${id}.yaml`), [
    `name: ${name}`,
    `description: ${name}`,
    'priority: medium',
    'requires_auth: false',
    'steps:',
    '  - action: open',
    '    url: /',
  ]);
}

const root = mkdtempSync(join(tmpdir(), 'shipguard-report-parser-'));

try {
  copyFileSync(SOURCE_BUILD, join(root, 'build-review.mjs'));
  copyFileSync(SOURCE_TEMPLATE, join(root, '_review-template.html'));
  mkdirSync(join(root, 'pages'), { recursive: true });
  mkdirSync(join(root, '_results'), { recursive: true });

  writeFile(join(root, '_config.yaml'), ['base_url: http://127.0.0.1:8001']);
  createManifest(root, 'pages/pass-case', 'Pass case');
  createManifest(root, 'pages/fail-case', 'Fail case');
  createManifest(root, 'pages/error-case', 'Error case');
  createManifest(root, 'pages/stale-case', 'Stale case');
  createManifest(root, 'pages/skipped-case', 'Skipped case');

  writeFile(join(root, '_results', 'audit-results.json'), [
    '{"summary":{"total_bugs":0},"bugs":[],"impacted_ui_routes":[],"agents":[]}',
  ]);
  writeFile(join(root, '_results', 'report.md'), [
    '# Rapport visuel ShipGuard - 2026-06-30 20:49:05',
    '',
    '## Synthèse',
    '- Tests : 5 exécutés, 1 réussi, 1 échec, 1 obsolète, 1 erreur, 1 ignoré',
    '- Durée : 35.8s',
    '- Base URL : http://127.0.0.1:8001',
    '',
    '## Tous les résultats',
    '| Test | Statut | Durée | Libellé | Capture |',
    '|---|---:|---:|---|---|',
    '| pages/pass-case | PASS | 1.0s | Pass case | capture disponible |',
    '| pages/fail-case | FAIL | 1.0s | Fail case | capture disponible |',
    '| pages/error-case | ERROR | 1.0s | Error case | capture disponible |',
    '| pages/stale-case | STALE | 1.0s | Stale case | capture disponible |',
    '| pages/skipped-case | SKIPPED | 1.0s | Skipped case | capture disponible |',
  ]);

  execFileSync(process.execPath, ['build-review.mjs'], { cwd: root, stdio: 'pipe' });

  const results = JSON.parse(readFileSync(join(root, '_results', 'visual-results.json'), 'utf8'));
  assert.equal(results.summary.total, 5);
  assert.equal(results.summary.pass, 1);
  assert.equal(results.summary.fail, 1);
  assert.equal(results.summary.error, 1);
  assert.equal(results.summary.stale, 1);
  assert.equal(results.summary.skipped, 1);
  assert.equal(results.summary.duration_ms, 35800);

  const statuses = Object.fromEntries(results.tests.map(test => [test.id, test.status]));
  assert.equal(statuses['pages/pass-case'], 'PASS');
  assert.equal(statuses['pages/fail-case'], 'FAIL');
  assert.equal(statuses['pages/error-case'], 'ERROR');
  assert.equal(statuses['pages/stale-case'], 'STALE');
  assert.equal(statuses['pages/skipped-case'], 'SKIPPED');

  const html = readFileSync(join(root, '_results', 'review.html'), 'utf8');
  assert.ok(html.includes('2026-06-30 20:49:05'), 'review.html must expose the Markdown last run');

} finally {
  rmSync(root, { recursive: true, force: true });
}

const jsonRoot = mkdtempSync(join(tmpdir(), 'shipguard-report-parser-json-priority-'));

try {
  copyFileSync(SOURCE_BUILD, join(jsonRoot, 'build-review.mjs'));
  copyFileSync(SOURCE_TEMPLATE, join(jsonRoot, '_review-template.html'));
  mkdirSync(join(jsonRoot, 'pages'), { recursive: true });
  mkdirSync(join(jsonRoot, '_results'), { recursive: true });

  writeFile(join(jsonRoot, '_config.yaml'), ['base_url: http://127.0.0.1:8001']);
  createManifest(jsonRoot, 'pages/json-case', 'JSON case');

  writeJson(join(jsonRoot, '_results', 'audit-results.json'), {
    summary: { total_bugs: 0 },
    bugs: [],
    impacted_ui_routes: [],
    agents: [],
  });
  writeJson(join(jsonRoot, '_results', 'visual-results.json'), {
    schema_version: '1.0',
    timestamp: '2026-06-30T20:10:25.602Z',
    base_url: 'http://127.0.0.1:8001',
    summary: {
      total: 1,
      pass: 1,
      fail: 0,
      error: 0,
      stale: 0,
      skipped: 0,
      duration_ms: null,
    },
    tests: [
      {
        id: 'pages/json-case',
        manifest: 'pages/json-case.yaml',
        name: 'JSON case',
        url: '/',
        status: 'PASS',
        duration_ms: null,
        screenshot: null,
        failure_reason: null,
      },
    ],
  });
  writeFile(join(jsonRoot, '_results', 'report.md'), [
    '# Rapport visuel ShipGuard - 2026-06-30 20:49:05',
    '',
    '## Synthèse',
    '- Tests : 1 exécuté, 1 réussi, 0 échec, 0 obsolète, 0 erreur, 0 ignoré',
    '- Durée : 35.8s',
    '',
    '## Tous les résultats',
    '| Test | Statut | Durée | Libellé | Capture |',
    '|---|---:|---:|---|---|',
    '| pages/json-case | PASS | 1.0s | JSON case | capture disponible |',
  ]);

  execFileSync(process.execPath, ['build-review.mjs'], { cwd: jsonRoot, stdio: 'pipe' });

  const results = JSON.parse(readFileSync(join(jsonRoot, '_results', 'visual-results.json'), 'utf8'));
  assert.equal(results.summary.total, 1);
  assert.equal(results.summary.pass, 1);
  assert.equal(results.summary.duration_ms, null);
} finally {
  rmSync(jsonRoot, { recursive: true, force: true });
}

console.log('report parser smoke test passed');
