# Parser rapport visuel francisé Implementation Plan

> PDG-LARGE-FILE-JUSTIFICATION: plan agentique détaillé nécessaire pour cadrer un fallback de parsing, un test de fixture et les preuves de non-régression sans ambiguïté.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** rendre le fallback Markdown de `build-review.mjs` compatible avec le rapport visuel ShipGuard francisé.

**Architecture:** `visual-results.json` reste prioritaire. Le fallback `report.md` est enrichi dans `parseReport()` pour comprendre le format français courant, et un smoke test isolé prouve le comportement sans dépendre des artefacts du dépôt réel.

**Tech Stack:** Node.js ESM, `child_process.execFileSync`, fixtures temporaires, parser Markdown par expressions régulières bornées, dashboard ShipGuard existant.

---

## PDG Pass

Trigger decision: oui, ce plan sera exécuté par un agent et touche un contrat de fallback du dashboard ShipGuard.

Skill invocation pass: `prd`, `superpowers:writing-plans` et `progressive-disclosure-guard` ont été lus. Une réponse légère est insuffisante parce que le bug est masqué en mode normal par `visual-results.json`; le plan doit forcer le mode dégradé.

Artifacts inspected:
- `visual-tests/build-review.mjs`
- `visual-tests/_results/report.md`
- `visual-tests/_results/visual-results.json`
- `visual-tests/review-smoke-test.mjs`
- `visual-tests/_review-template.html`
- `visual-tests/package.json`

Overlap findings: `extend` de `parseReport()` ; `reuse` du style fixture de `review-smoke-test.mjs` ; `avoid` pour une nouvelle dépendance Markdown ou un second pipeline JSON.

| Claim | Source | Verdict | Impact |
|-------|--------|---------|--------|
| Le JSON est prioritaire | `parseVisualResults()` puis `mergeStatusSources()` | Confirmé | La correction ne doit pas changer ce contrat. |
| Le rapport courant est français | `visual-tests/_results/report.md` | Confirmé | Les regex anglaises ne suffisent pas. |
| Les statuts du tableau sont déjà lus | `parseReport()` lignes de tableau et liste | Confirmé | Le test doit cibler aussi date, durée et synthèse. |
| Les smoke tests utilisent des fixtures temporaires | `visual-tests/review-smoke-test.mjs` | Confirmé | Le nouveau test doit suivre ce modèle. |

Known knowns: le rapport français commence par `# Rapport visuel ShipGuard - ...`; la synthèse contient `Tests : ... exécutés, ... réussis, ... échecs, ... obsolète, ... erreurs, ... ignoré`; la durée est exprimée en secondes.

Known unknowns: d'anciens rapports peuvent encore utiliser le format anglais ; le plan garde donc la compatibilité anglaise.

Forbidden shortcuts: ne pas remplacer `visual-results.json` par `report.md` quand le JSON est valide ; ne pas importer de parser Markdown ; ne pas modifier l'UI pour masquer `unknown`.

Regression proof required: test rouge puis vert sur fixture sans `visual-results.json`, smoke dashboard existant, rebuild réel du dashboard.

PDG self-check, not independent review.

## File Structure

- Modify: `visual-tests/build-review.mjs` - fallback `parseReport()` et helpers locaux.
- Create: `visual-tests/report-parser-smoke-test.mjs` - fixture sans `visual-results.json`.
- Modify: `CHANGELOG.MD` - trace courte de l'implémentation quand elle sera faite.
- Do not modify: `visual-tests/_results/report.md` as source fixture réel ; il sert de référence observée.
- Do not modify: `visual-tests/_review-template.html` unless the smoke proves que `lastRun` n'est pas exposé malgré la correction parser.

## Task 1: Ajouter le smoke test rouge

**Files:**
- Create: `visual-tests/report-parser-smoke-test.mjs`

- [ ] **Step 1: Create the fixture test**

Create `visual-tests/report-parser-smoke-test.mjs` with:

```js
#!/usr/bin/env node

import { copyFileSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'fs';
import { tmpdir } from 'os';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { execFileSync } from 'child_process';
import assert from 'node:assert/strict';

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const SOURCE_BUILD = join(SCRIPT_DIR, 'build-review.mjs');
const SOURCE_TEMPLATE = join(SCRIPT_DIR, '_review-template.html');

function writeFile(path, lines) {
  writeFileSync(path, lines.join('\n') + '\n', 'utf8');
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
    '- Tests : 5 exécutés, 1 réussis, 1 échecs, 1 obsolète, 1 erreurs, 1 ignoré',
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

  console.log('report parser smoke test passed');
} finally {
  rmSync(root, { recursive: true, force: true });
}
```

- [ ] **Step 2: Run the test and verify it fails**

Run:

```bash
node visual-tests/report-parser-smoke-test.mjs
```

Expected before implementation:

```text
AssertionError ... duration_ms ... null !== 35800
```

## Task 2: Étendre le parser Markdown

**Files:**
- Modify: `visual-tests/build-review.mjs`

- [ ] **Step 1: Replace the summary/date parsing block**

Inside `parseReport()`, replace the existing `summaryMatch` and `dateMatch` block with:

```js
  const englishSummaryMatch = md.match(/Tests:\s*(\d+)\s*run,\s*(\d+)\s*pass,\s*(\d+)\s*fail/i);
  const frenchSummaryMatch = md.match(
    /Tests\s*:\s*(\d+)\s+exécutés,\s*(\d+)\s+réussis,\s*(\d+)\s+échecs?,\s*(\d+)\s+obsolètes?,\s*(\d+)\s+erreurs?,\s*(\d+)\s+ignorés?/i,
  );
  const englishDateMatch = md.match(/^#\s+Visual Report\s*[—-]\s*(.+)$/m);
  const frenchDateMatch = md.match(/^#\s+Rapport visuel ShipGuard\s*-\s*(.+)$/m);
  const durationMatch = md.match(/Durée\s*:\s*(\d+(?:[.,]\d+)?)s/i);
  const baseUrlMatch = md.match(/Base URL\s*:\s*(\S+)/i);
  const durationMs = durationMatch
    ? Math.round(Number.parseFloat(durationMatch[1].replace(',', '.')) * 1000)
    : null;
  const summary = frenchSummaryMatch
    ? {
        total: Number.parseInt(frenchSummaryMatch[1], 10),
        pass: Number.parseInt(frenchSummaryMatch[2], 10),
        fail: Number.parseInt(frenchSummaryMatch[3], 10),
        stale: Number.parseInt(frenchSummaryMatch[4], 10),
        error: Number.parseInt(frenchSummaryMatch[5], 10),
        skipped: Number.parseInt(frenchSummaryMatch[6], 10),
      }
    : {
        total: englishSummaryMatch ? Number.parseInt(englishSummaryMatch[1], 10) : 0,
        pass: englishSummaryMatch ? Number.parseInt(englishSummaryMatch[2], 10) : 0,
        fail: englishSummaryMatch ? Number.parseInt(englishSummaryMatch[3], 10) : 0,
        stale: 0,
        error: 0,
        skipped: 0,
      };
```

- [ ] **Step 2: Return the expanded fallback contract**

Return:

```js
  return {
    statusMap,
    ...summary,
    durationMs,
    baseUrl: baseUrlMatch ? baseUrlMatch[1] : null,
    lastRun: (frenchDateMatch || englishDateMatch)?.[1] || 'unknown',
  };
```

## Task 3: Vérifier les preuves locales

**Files:**
- Execute only

- [ ] **Step 1: Run the new smoke test**

Run:

```bash
node visual-tests/report-parser-smoke-test.mjs
```

Expected:

```text
report parser smoke test passed
```

- [ ] **Step 2: Run the existing review smoke test**

Run:

```bash
node visual-tests/review-smoke-test.mjs --debug
```

Expected:

```text
review smoke test passed
```

- [ ] **Step 3: Rebuild the real review dashboard**

Run:

```bash
node visual-tests/build-review.mjs
```

Expected:

```text
Building Visual review page...
  Visual results: visual-tests/_results/visual-results.json
```

- [ ] **Step 4: Verify the real JSON still uses the structured source**

Run:

```bash
node -e "const r=require('./visual-tests/_results/visual-results.json'); console.log(r.summary.total, r.summary.pass, r.summary.fail, r.summary.duration_ms)"
```

Expected current MiWeb shape:

```text
28 28 0 null
```

`duration_ms` may stay `null` in the real run because the valid JSON remains prioritaire and does not currently carry a duration.

## Task 4: Documenter et committer

**Files:**
- Modify: `CHANGELOG.MD`
- Add: `visual-tests/report-parser-smoke-test.mjs`
- Modify: `visual-tests/build-review.mjs`

- [ ] **Step 1: Add the changelog entry**

Add under `## 2026-07-01`:

```markdown
- Implémentation locale de `PRD-008` : fallback Markdown visuel compatible avec le rapport francisé.
```

- [ ] **Step 2: Run Markdown accent check**

Run from `/Users/alex/Claude`:

```bash
bash scripts/check-accents.sh miweb-objectifs-2030/CHANGELOG.MD
```

Expected: no output, exit 0.

- [ ] **Step 3: Inspect and commit**

Run:

```bash
git diff --check
git status --short
git add CHANGELOG.MD visual-tests/build-review.mjs visual-tests/report-parser-smoke-test.mjs
git diff --cached --check
git commit -m "fix: Parse le rapport visuel francisé"
```

Expected:

```text
[main <sha>] fix: Parse le rapport visuel francisé
```

No push without Alex's explicit approval.

## Self-Review

Spec coverage: `SG-Z5-007` is covered by Task 1 and Task 2. JSON priority is covered by Task 3 step 4. Documentation and commit are covered by Task 4.

Placeholder scan: aucun marqueur de remplissage, aucun test différé, aucune commande vague.

Type consistency: `durationMs` matches the existing `buildVisualResultsContract(data, statusSource)` field; `lastRun` matches the existing `data.summary.lastRun` field.
