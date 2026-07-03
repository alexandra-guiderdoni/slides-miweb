# Retest complet ShipGuard 2.4.0 - 2026-07-02

Périmètre : plugin `shipguard@shipguard` réinstallé, harnais `visual-tests`
du projet MiWeb, et URL cible
`http://localhost:8000/miweb-objectifs-2030-v1/#slide-01`.

## Résultat

Verdict global : **OK avec deux réserves produit**.

- Plugin Codex : `shipguard@shipguard` installé, activé, version `2.4.0`.
- Plugin Claude : `shipguard@shipguard` listé en version `2.4.0`.
- Smokes plugin `2.4.0` : OK.
- Smokes du harnais local : OK.
- Run visuel frais : `31/31 PASS`.
- URL cible `#slide-01` : `PASS`, HTTP `200`, hash `#slide-01` préservé.
- Review reconstruite : `31 pass`, `0 fail`, `0 error`, `Screenshots matched: 31/31`.
- Validation variante `miweb-objectifs-2030-v1` : `18 tests`, `OK`.

Réserves :

1. `HEAD /favicon.ico` renvoie encore `404` alors que `GET /favicon.ico`
   renvoie `204`, aussi bien avec le builder local qu'avec le builder du
   plugin `2.4.0` en fixture.
2. Les commandes shell natives `shipguard`, `sg-ship`, `sg-code-audit`,
   `sg-process-check`, `sg-visual-run`, `sg-visual-discover` restent absentes
   du `PATH`. La phase visuelle complète a donc été rejouée par un runner
   Playwright compatible avec le contrat ShipGuard, pas par une CLI native
   `sg-visual-run`.

## Preuves exécutées

| Phase | Commande ou preuve | Verdict |
|---|---:|---:|
| Installation Codex | `codex plugin list` | OK, `shipguard@shipguard 2.4.0` |
| Installation Claude | `claude plugin list` | OK, `shipguard@shipguard 2.4.0` |
| Review plugin | `node .../sg-visual-review/review-smoke-test.mjs --port=23101` | OK |
| Monitor plugin | `node .../sg-visual-review/monitor-smoke-test.mjs --port=23102` | OK |
| Recorder YAML plugin | `node --test .../sg-record/lib/actions-to-yaml.test.mjs` | OK, `21 pass` |
| Scout plugin | `node .../sg-scout/offline-dry-run-smoke-test.mjs` | OK |
| Improve plugin | `node .../sg-improve/improve-dry-run-smoke-test.mjs` | OK |
| Improve rollback plugin | `node .../sg-improve/improve-rollback-smoke-test.mjs` | OK |
| Visual fix plugin | `node .../sg-visual-fix/visual-fix-dry-run-smoke-test.mjs` | OK |
| Review locale | `node visual-tests/review-smoke-test.mjs --port=23111` | OK |
| Monitor local | `node visual-tests/monitor-smoke-test.mjs --port=23112` | OK |
| Recorder local | `node visual-tests/sg-record.mjs --check --check-timeout=30000` | OK |
| Recorder YAML local | `node --test visual-tests/lib/actions-to-yaml.test.mjs` | OK, `13 pass` |
| Process tab | fixture temporaire avec `process-results.json` | OK, `Process check results: found` |
| Visual run | runner Playwright compatible sur `localhost:8000` | OK, `31/31 PASS` |
| Review rebuild | `node visual-tests/build-review.mjs` | OK, `31 pass`, `31/31 screenshots` |
| Variante v1 | `scripts/validate_variant.sh miweb-objectifs-2030-v1` | OK, `18 tests` |

## Artefacts produits

- `visual-tests/_results/visual-results.json`
- `visual-tests/_results/report.md`
- `visual-tests/_results/review.html`
- `visual-tests/_results/screenshots/miweb-objectifs-2030-v1-slide-01-url.png`
- `visual-tests/_results/history/visual-results-before-shipguard-2-4-0-*.json`

## Points non vérifiés

- `sg-code-audit` natif : non vérifié, pas d'entrypoint CLI ou outil Codex
  exposé pour lancer la phase comme commande reproductible.
- `sg-process-check` natif : non vérifié pour la même raison ; seule
  l'intégration de sa sortie dans la review a été vérifiée par fixture.
- `sg-ship` natif : non vérifié, car il dépend des entrées CLI ou slash skills
  non exposées dans ce contexte Codex.
- `sg-change-report` dans ce projet : non écrit pour éviter d'ajouter un
  rapport durable artificiel ; la génération persona est couverte par le smoke
  `sg-visual-review`.

## Écarts observés

- Le harnais local n'est pas une copie exacte du plugin `2.4.0` :
  `sg-record.mjs`, `lib/actions-to-yaml.mjs`,
  `lib/actions-to-yaml.test.mjs`, `lib/recorder-toolbar.js`,
  `build-review.mjs` et `_review-template.html` diffèrent du cache plugin.
- Le serveur local externe lancé entre commandes ne restait pas vivant dans ce
  harnais ; le run visuel final a donc utilisé un serveur HTTP intégré au
  runner Node, ouvert sur `localhost:8000` pendant l'exécution puis arrêté.
