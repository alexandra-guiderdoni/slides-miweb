# Postmortem ShipGuard 2.3.8 après retest propre

Date : 2026-07-01, 12:31 +02:00

Destinataire : Loïc, pour suite ShipGuard générique.

Commit testé : `3bcf382 fix: normalize monitor agent ids`

## Résultat court

ShipGuard 2.3.8 corrige bien le blocage principal du monitor live :
`id`, `agent_id` et `zone_id` sont normalisés, `r1:z1` est réconcilié avec
`z1`, et un update sans identifiant est refusé en `400`.

Deux blocages restent à traiter :

1. `HEAD /favicon.ico` renvoie encore `404` alors que `GET /favicon.ico`
   renvoie `204`.
2. Le rebuild du dashboard génère des artefacts qui échouent à
   `git diff --check` : espaces finaux dans les rapports persona et absence de
   saut de ligne final dans certains fichiers générés.

## État de départ propre

Le fichier `visual-tests/_results/audit-results.json` a été supprimé avant le
retest, comme demandé.

Preuve :

```text
audit-results.json absent
```

Les scripts locaux `build-review.mjs`, `review-smoke-test.mjs` et
`monitor-smoke-test.mjs` ont été resynchronisés depuis le cache ShipGuard 2.3.8.

## Installation et validation

| Point | Preuve | Verdict |
|---|---|---|
| Marketplace Codex | `shipguard@shipguard 2.3.8` installé et activé | OK |
| Marketplace Claude | `shipguard@shipguard 2.3.8` installé et activé | OK |
| Commit marketplace Codex | `3bcf382 fix: normalize monitor agent ids` | OK |
| Commit marketplace Claude | `3bcf382 fix: normalize monitor agent ids` | OK |
| Validation Claude | `Validation passed` | OK |

Note locale : la mise à jour Claude a affiché un avertissement de hook
`SessionEnd`, mais l'installation et la validation plugin ont bien abouti.

## Vérifications passées

```text
node --check visual-tests/build-review.mjs
node --check visual-tests/review-smoke-test.mjs
node --check visual-tests/monitor-smoke-test.mjs
node --check visual-tests/sg-record.mjs
node visual-tests/review-smoke-test.mjs --port=23101
node visual-tests/monitor-smoke-test.mjs --port=23102
node visual-tests/lib/actions-to-yaml.test.mjs
node visual-tests/lib/integration-test.mjs
node visual-tests/sg-record.mjs --check
node <2.3.8>/skills/sg-visual-fix/visual-fix-dry-run-smoke-test.mjs
node <2.3.8>/skills/sg-scout/offline-dry-run-smoke-test.mjs
node <2.3.8>/skills/sg-improve/improve-dry-run-smoke-test.mjs
node <2.3.8>/skills/sg-improve/improve-rollback-smoke-test.mjs
parse scripts inline dashboard
claude plugin validate plugins/shipguard
```

Résultats notables :

```text
review smoke test passed
monitor smoke test passed
actionsToYaml : 13 pass, 0 fail
Recorder Integration Test : 11 pass, 0 fail
PLAYWRIGHT_OK / CHROMIUM_OK / GUI_LAUNCH_OK
visual-fix dry-run smoke test passed
scout offline dry-run smoke test passed
improve dry-run smoke test passed
improve rollback smoke test passed
inline dashboard scripts parse: OK
```

## Matrice des anciens blocages

| Point | Preuve observée | Verdict | Impact |
|---|---|---|---|
| Monitor accepte `id` | `POST agent-update {"id":"z1"}` renvoie `200` | Corrigé | Plus de rejet injustifié |
| Monitor accepte `agent_id` | `POST agent-update {"agent_id":"z2"}` renvoie `200` | Corrigé | Contrat historique conservé |
| Monitor accepte `zone_id` | `POST agent-update {"zone_id":"r1:z3"}` renvoie `200` | Corrigé | Alias zone utilisable |
| Update sans identifiant | `POST agent-update {"status":"completed"}` renvoie `400` | Corrigé | Plus de création silencieuse |
| `agents.undefined` | clés finales `z1, z2, z3` | Corrigé | Aucun agent fantôme |
| `r1:z1` / `z1` | clé finale `z1`, alias `r1:z1` conservé | Corrigé | Pas de doublon `pending/completed` |
| Scope rebuild | `review-smoke-test` vérifie `run_id`, `scope`, `full_suite_total`, `uncovered_routes` | Corrigé au smoke | Non prouvé par un vrai run agentique |
| `--from-process` | documentation 2.3.8 présente et source priorisée dans `invocation-modes.md` | Documenté | Pas d'entrypoint CLI natif à mesurer |
| Route `/` | documentation : `/` ne matche que le manifest racine | Documenté | Pas d'exécution réelle sans runner |
| Routes non HTML | documentation : `skipped` pour asset, `uncovered` pour route sans manifest | Documenté | Pas d'exécution réelle sans runner |
| `GET /favicon.ico` | HTTP `204` | OK | Cas GET réglé |
| `HEAD /favicon.ico` | HTTP `404` | Encore KO | Incohérence HTTP résiduelle |
| `git diff --check` après rebuild | espaces finaux et EOF manquant dans artefacts générés | Encore KO | Le dashboard génère un diff non propre |

## Détail monitor réel

Payload de départ :

```json
{
  "mode": "retest-2.3.8-real",
  "zones": [
    {"id": "r1:z1"},
    {"zone_id": "r1:z2"},
    {"zone_id": "z3"}
  ]
}
```

Preuve finale :

```text
/api/monitor/audit-start 200
/api/monitor/agent-update {"id":"z1"} 200
/api/monitor/agent-update {"agent_id":"z2"} 200
/api/monitor/agent-update {"zone_id":"r1:z3"} 200
/api/monitor/agent-update sans identifiant 400
agent keys: z1, z2, z3
monitor canonicalisation real server: OK
audit-complete 200
status: completed
```

Le fichier `audit-monitor.json` persiste maintenant les trois agents sous leurs
clés canoniques et conserve les alias `r1:z1`, `r1:z2`, `r1:z3`.

## Blocage résiduel 1 : `HEAD /favicon.ico`

Preuve :

```text
health:200
favicon_get:204
favicon_head:404
```

Attendu : `HEAD /favicon.ico` devrait suivre le même contrat que `GET`, au
minimum `204`, ou le comportement différent doit être explicite et testé.

## Blocage résiduel 2 : artefacts générés non propres

Après `node visual-tests/build-review.mjs --serve --port=23113`, la commande
suivante échoue :

```text
git diff --check
```

Exemples de lignes décisives :

```text
visual-tests/_results/persona-reports/.../client.html:34: trailing whitespace.
visual-tests/_results/persona-reports/.../product.html:100: trailing whitespace.
visual-tests/_results/persona-reports/.../client-invite-email.md:36: new blank line at EOF.
```

Le diff local montre aussi des fichiers générés sans saut de ligne final,
notamment `visual-results.json`, `review.html` et `audit-monitor.json`.

Cause probable côté générateur : la version 2.3.8 copiée localement a supprimé
la fonction de normalisation de sortie `generatedText(...)` et écrit désormais
certains artefacts avec `render...` ou `JSON.stringify(...)` bruts.

Attendu : restaurer une normalisation unique des artefacts générés :

```text
trim trailing spaces per line
ensure exactly one final newline
avoid extra blank line at EOF
```

À ajouter au smoke review : reconstruire les rapports persona puis exécuter un
équivalent de `git diff --check` sur les artefacts générés.

## Limites non vérifiées

Je n'ai pas exécuté de vrai `/sg-visual-run --from-audit` ni
`/sg-visual-run --from-process` de bout en bout, car la surface disponible ici
est un skill agentique documenté, pas un runner CLI natif. Les contrats sont
vérifiés par lecture des sources 2.3.8 et par `review-smoke-test`, pas par une
navigation agentique complète.

Je n'ai pas relancé `sg-ship` complet, `sg-scout` GitHub réel, `sg-visual-fix`
réel ni `sg-improve` réel sur le dépôt principal, conformément aux interdits du
harness sans validation explicite.
