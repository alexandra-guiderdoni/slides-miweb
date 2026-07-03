# Rapport clean install ShipGuard 2.3.8 et audit complet MiWeb

Date : 2026-07-01

Destinataire : Loïc

Périmètre : ShipGuard 2.3.8 dans l'environnement Codex et Claude, puis audit
complet du site statique MiWeb. Les points liés au workflow personnel d'Alex
sont exclus des blocages à remonter.

## Résultat court

La clean install est prouvée et le site passe l'audit complet disponible dans
ce harnais propre.

- ShipGuard réinstallé proprement en `2.3.8`.
- Commit marketplace Codex et Claude : `3bcf382 fix: normalize monitor agent ids`.
- Validation plugin Claude : `Validation passed`.
- Validation statique du site : 10 variantes OK, tests communs OK.
- Run visuel complet : 31 routes HTML, 31 PASS.
- Review dashboard : construit et servi.
- Monitor live : correctif confirmé, pas de `agents.undefined`, pas de doublon
  `r1:z1` / `z1`.

Blocages ShipGuard ou environnement Codex/Claude à traiter :

1. `HEAD /favicon.ico` renvoie encore `404` alors que `GET /favicon.ico`
   renvoie `204`.
2. Les JSON générés par `build-review.mjs` n'ont pas de saut de ligne final
   (`visual-results.json`, `audit-monitor.json`).
3. Les phases `sg-ship`, `sg-code-audit`, `sg-process-check`,
   `sg-visual-run` et `sg-visual-review` sont exposées comme skills, mais pas
   comme commandes shell natives. Dans Codex, cela empêche une recette 100 %
   reproductible par CLI.
4. La documentation `sg-process-check` et `sg-ship` annonce que
   `process-results.json` alimente la review, mais `sg-visual-review` 2.3.8 ne
   contient pas de lecture visible de `process-results.json`.

## Preuves de clean install

Avant réinstallation :

```text
codex plugin remove shipguard@shipguard
Removed plugin `shipguard` from marketplace `shipguard`.

claude plugin uninstall shipguard@shipguard -y
Successfully uninstalled plugin: shipguard

Codex: shipguard@shipguard not installed
Claude: No plugins installed
codex cache absent
claude cache absent
```

Après réinstallation :

```text
codex marketplace: 3bcf382 fix: normalize monitor agent ids
claude marketplace: 3bcf382 fix: normalize monitor agent ids

codex plugin add shipguard@shipguard
Installed plugin root: /Users/alex/.codex/plugins/cache/shipguard/shipguard/2.3.8

claude plugin install shipguard@shipguard
Successfully installed plugin: shipguard@shipguard

claude plugin validate .../plugins/shipguard
Validation passed

Codex: shipguard@shipguard installed, enabled, version 2.3.8
Claude: shipguard@shipguard version 2.3.8, enabled
```

Le cache a bien été recréé côté Codex et Claude sous `shipguard/2.3.8`.

## Reprise propre du harnais

L'ancien dossier de recette a été conservé par renommage :

```text
visual-tests -> visual-tests-old
```

Le nouveau `visual-tests/` ne réutilise pas les anciens `_results/`.

Contenu recréé :

- scripts `build-review.mjs`, `_review-template.html`,
  `review-smoke-test.mjs`, `monitor-smoke-test.mjs` depuis le cache Codex
  ShipGuard 2.3.8 ;
- scripts recorder et `lib/` depuis le même cache ;
- `package.json` propre et `playwright` local ;
- 31 manifests régénérés depuis `published-versions.json` et les fichiers HTML
  publics du site.

## Phase 1 - Smokes ShipGuard

Commandes passées :

```text
node --check visual-tests/build-review.mjs
node --check visual-tests/review-smoke-test.mjs
node --check visual-tests/monitor-smoke-test.mjs
node --check visual-tests/sg-record.mjs
node visual-tests/review-smoke-test.mjs --port=23121
node visual-tests/monitor-smoke-test.mjs --port=23122
node visual-tests/lib/actions-to-yaml.test.mjs
node visual-tests/lib/integration-test.mjs
node visual-tests/sg-record.mjs --check
node <2.3.8>/skills/sg-visual-fix/visual-fix-dry-run-smoke-test.mjs
node <2.3.8>/skills/sg-scout/offline-dry-run-smoke-test.mjs
node <2.3.8>/skills/sg-improve/improve-dry-run-smoke-test.mjs
node <2.3.8>/skills/sg-improve/improve-rollback-smoke-test.mjs
```

Preuves :

```text
review smoke test passed
monitor smoke test passed
actionsToYaml: 13 pass, 0 fail
Recorder Integration Test: 11 pass, 0 fail
PLAYWRIGHT_OK
CHROMIUM_OK
GUI_LAUNCH_OK
visual-fix dry-run smoke test passed
scout offline dry-run smoke test passed
improve dry-run smoke test passed
improve rollback smoke test passed
```

Verdict : OK.

## Phase 2 - Audit statique du site

Les 10 variantes publiées ont été validées avec le script standard du dépôt :

```text
scripts/validate_variant.sh <slug>
```

Résultat :

```text
VALIDATE_OK miweb-objectifs-2030-v1
VALIDATE_OK miweb-objectifs-2030-v2
VALIDATE_OK miweb-objectifs-2030-v3
VALIDATE_OK miweb-objectifs-2030-v4
VALIDATE_OK miweb-offre-mutualisee-listes-diffusion-2026-condensee
VALIDATE_OK miweb-offre-mutualisee-listes-diffusion-2026-longue
VALIDATE_OK span-pan
VALIDATE_OK mise-en-gouvernance-du-span
VALIDATE_OK checklist-span-operationnel
VALIDATE_OK emojis-accessibles-reseaux-sociaux
UNITTEST_OK matrice-slide-ai
```

Verdict : OK.

## Phase 3 - Run visuel complet

Le site a été servi sur :

```text
http://127.0.0.1:8001/
```

Le run visuel propre a exécuté 31 manifests HTML.

Preuve du contrat `visual-results.json` :

```json
{
  "schema_version": "1.0",
  "run_id": "clean-full-20260701T104054",
  "scope_type": "all",
  "selected_total": 31,
  "full_suite_total": 31,
  "uncovered_routes": 0,
  "total": 31,
  "pass": 31,
  "fail": 0,
  "error": 0,
  "tests": 31
}
```

Verdict : OK.

Limite : le run a été exécuté par un runner Playwright de recette qui écrit le
contrat ShipGuard, car `sg-visual-run` n'est pas disponible comme commande CLI
native dans l'environnement Codex.

## Phase 4 - Review et monitor live

Review :

```text
node visual-tests/build-review.mjs --serve --port=23131
Found 31 test manifests
Status: 31 pass, 0 fail, 0 error, 0 stale, 0 skipped
Screenshots matched: 31/31
Server: http://127.0.0.1:23131
```

Endpoints :

```text
health:200
visual_results:200
favicon_get:204
favicon_head:404
```

Monitor :

```text
/api/monitor/audit-start 200
/api/monitor/agent-update {"id":"z1"} 200
/api/monitor/agent-update {"agent_id":"z2"} 200
/api/monitor/agent-update {"zone_id":"r1:z3"} 200
/api/monitor/agent-update sans identifiant 400
/api/monitor/audit-complete 200
```

État final :

```json
{
  "status": "completed",
  "agentKeys": ["z1", "z2", "z3"],
  "z1Aliases": ["r1:z1"]
}
```

Verdict monitor : OK.

Blocage restant : `HEAD /favicon.ico` encore `404`.

## Phase 5 - Process et orchestration

Le plugin expose bien les skills :

```text
sg-change-report
sg-code-audit
sg-improve
sg-process-check
sg-record
sg-scout
sg-ship
sg-visual-discover
sg-visual-fix
sg-visual-review
sg-visual-review-stop
sg-visual-run
```

Mais les commandes shell suivantes ne sont pas disponibles :

```text
sg-ship
sg-code-audit
sg-process-check
sg-visual-run
sg-visual-review
```

Dette produit/DX : dans Codex, un utilisateur peut installer le plugin, mais ne
peut pas rejouer toutes les phases en CLI reproductible. Les phases existent
comme skills, pas comme entrypoints mesurables.

Dette contrat : `sg-process-check` et `sg-ship` annoncent que
`process-results.json` alimente la review, mais une recherche dans
`sg-visual-review` 2.3.8 ne montre pas de lecture de `process-results.json`.

Test complémentaire isolé :

```text
Fixture temporaire avec process-results.json contenant UNIQUE_PROCESS_MARKER_2_3_8
Rebuild review avec build-review.mjs 2.3.8
Résultat : PROCESS_MARKER_ABSENT
```

Verdict : la review 2.3.8 ne consomme pas visiblement `process-results.json`.

## Phase 5 bis - Contrats ciblés `from-process`

Un fixture temporaire a été construit avec :

- deux manifests : racine `/` et page secondaire ;
- un `visual-results.json` de type `from-process` ;
- `selected_routes: ["/"]` ;
- `selected_manifests: ["visual-tests/pages/root-index.yaml"]` ;
- deux routes non exécutées : `/review.html` en `uncovered` et un ZIP en
  `skipped`.

Après rebuild par `build-review.mjs` 2.3.8 :

```json
{
  "run_id": "contract-from-process-001",
  "scope_type": "from-process",
  "selected_routes": ["/"],
  "selected_manifests": ["visual-tests/pages/root-index.yaml"],
  "selected_total": 1,
  "full_suite_total": 2,
  "tests_length": 1,
  "test_ids": ["pages/root-index"]
}
```

Les routes suivantes sont aussi préservées :

```json
[
  {"route": "/review.html", "status": "uncovered", "reason": "no_visual_manifest"},
  {"route": "/assets/downloads/file.zip", "status": "skipped", "reason": "non_html_asset"}
]
```

Verdict : le rebuild review préserve correctement `run_id`, `scope`,
`selected_total`, `full_suite_total`, `skipped` et `uncovered`. Le cas `/`
reste bien limité au manifest racine dans ce contrat de rebuild.

Limite : ce test prouve le rebuild d'un JSON déjà produit, pas l'exécution
réelle de `sg-visual-run --from-process`, car aucun runner shell `sg-visual-run`
ou `shipguard visual-run` n'est installé.

## Phase 6 - Hygiène des artefacts générés

Contrôle appliqué aux artefacts texte du nouveau harnais, hors `node_modules`,
screenshots et thumbnails.

Résultat :

```text
visual-tests/_results/audit-monitor.json: final newline missing
visual-tests/_results/visual-results.json: final newline missing
```

Dette produit : normaliser les sorties générées par ShipGuard avec un saut de
ligne final unique. Ce point est distinct des anciens espaces finaux des
rapports persona, car le harnais propre ne contient pas de change-report
persona.

## Blocages à remonter à Loïc

### B1 - `HEAD /favicon.ico` incohérent

`GET /favicon.ico` renvoie `204`, mais `HEAD /favicon.ico` renvoie `404`.

Impact : le serveur de review reste incohérent pour les prévols ou clients qui
testent `HEAD`.

Attendu : `HEAD /favicon.ico` suit le même contrat que `GET`, ou le cas est
explicitement documenté et testé.

### B2 - JSON générés sans saut de ligne final

`build-review.mjs` produit au moins :

```text
visual-results.json: final newline missing
audit-monitor.json: final newline missing
```

Impact : les artefacts générés ne respectent pas une hygiène de dépôt standard
et compliquent les diffs propres.

Attendu : toutes les écritures texte passent par une fonction de normalisation
qui garantit exactement un saut de ligne final.

### B3 - Pas d'entrypoint CLI pour rejouer toutes les phases

Après installation, les skills existent, mais `sg-ship`, `sg-code-audit`,
`sg-process-check`, `sg-visual-run` et `sg-visual-review` ne sont pas des
commandes shell.

Impact : impossible de prouver une recette complète par commandes reproductibles
dans Codex sans réimplémenter une partie des phases dans le harnais.

Point précis pour Loïc : tant qu'il n'y a pas de runner exécutable, on peut
tester `build-review.mjs`, `monitor-smoke-test.mjs`, `review-smoke-test.mjs` et
les scripts dry-run, mais on ne peut pas prouver de bout en bout
`sg-visual-run --from-process`, la sélection par `/`, ou la production initiale
des routes `skipped` / `uncovered`.

Attendu : fournir un entrypoint CLI ou un runner documenté, par exemple :

```text
shipguard ship --all
shipguard code-audit --report-only
shipguard process-check --from-audit
shipguard visual-run --all
shipguard visual-review --serve
```

### B4 - Contrat process annoncé mais non consommé par la review 2.3.8

`sg-process-check` annonce `process-results.json -> sg-visual-review`, et
`sg-ship` annonce trois signaux dans la review : audit, process, visuel.

Dans le code livré de `sg-visual-review` 2.3.8, aucune lecture de
`process-results.json` n'a été trouvée.

Impact : la phase process peut produire un artefact qui n'apparaît pas dans le
dashboard unifié annoncé.

Attendu : soit intégrer `process-results.json` dans `build-review.mjs`, soit
retirer cette promesse de la documentation 2.3.8.

## Points exclus du rapport de blocage

Les éléments suivants ont été observés mais ne sont pas remontés comme blocages
ShipGuard :

- avertissement `SessionEnd hook` lié au script local d'Alex ;
- premier lancement `npx playwright install` depuis le mauvais répertoire,
  corrigé immédiatement en relançant depuis `visual-tests/` ;
- absence de backend applicatif : le site MiWeb est statique, donc il n'y a pas
  de comportement serveur métier à simuler.
