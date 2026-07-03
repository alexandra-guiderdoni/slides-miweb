# Tableau de synthèse ShipGuard 2.3.8 pour Loïc

Date : 2026-07-01

Périmètre : clean install ShipGuard 2.3.8, audit complet MiWeb, points de
blocage liés au plugin ou au dépôt ShipGuard.

## Synthèse courte

| Sujet | Statut | Preuve | À faire côté Loïc |
|---|---:|---|---|
| Clean install Codex | OK | `shipguard@shipguard 2.3.8`, cache recréé | rien |
| Clean install Claude | OK | `shipguard@shipguard 2.3.8`, `Validation passed` | rien |
| Commit testé | OK | `3bcf382 fix: normalize monitor agent ids` | rien |
| Smokes review et monitor | OK | `review smoke test passed`, `monitor smoke test passed` | rien |
| Recorder preflight | OK | `PLAYWRIGHT_OK`, `CHROMIUM_OK`, `GUI_LAUNCH_OK` | rien |
| Recorder tests YAML | OK | `actionsToYaml: 13 pass`, intégration `11 pass` | rien |
| Visual full run | OK | 31 routes HTML, 31 PASS | rien |
| `sg-visual-discover` natif | BLOQUÉ | manifests actuels générés par harnais, pas par runner ShipGuard | fournir un runner ou confirmer le mode interactif comme seul mode officiel |
| Code Audit dashboard | OK harnais | `audit-results.json` à zéro bug affiché | fournir un vrai runner `sg-code-audit` pour preuve native |
| Monitor `id` | OK | update `{"id":"z1"}` -> `200`, agent `z1` | rien |
| Monitor `agent_id` | OK | update `{"agent_id":"z2"}` -> `200`, agent `z2` | rien |
| Monitor `zone_id` | OK | update `{"zone_id":"r1:z3"}` -> `200`, agent `z3` | rien |
| Monitor sans identifiant | OK | update sans identifiant -> `400` | rien |
| `agents.undefined` | OK | clés finales `z1,z2,z3` | rien |
| `r1:z1` / `z1` | OK | alias `r1:z1`, clé canonique `z1` | rien |
| Rebuild `run_id` / `scope` | OK | fixture `from-process`, `run_id` conservé | rien |
| Rebuild `/` racine | OK au rebuild | seule la route racine reste sélectionnée | prouver aussi la production initiale via runner |
| `skipped` / `uncovered` | OK au rebuild | ZIP en `skipped`, `/review.html` en `uncovered` | prouver aussi la production initiale via runner |
| `HEAD /favicon.ico` | KO | `GET` -> `204`, `HEAD` -> `404` | aligner `HEAD` sur `GET` ou documenter |
| JSON générés | KO | `visual-results.json` et `audit-monitor.json` sans saut final | normaliser les écritures texte |
| CLI ShipGuard | BLOQUÉ | `shipguard`, `sg-ship`, `sg-code-audit`, `sg-process-check`, `sg-visual-run` absents | fournir un entrypoint CLI ou runner officiel |
| `sg-change-report` | OK fixture | `report.json` + screenshots -> rapports persona générés | ajouter un smoke officiel ou une fixture de référence |
| `sg-visual-review-stop` | OK fixture | serveur isolé `23143` arrêté, port fermé | rien immédiat |
| Dashboard sans audit code | KO UX | sans `audit-results.json`, onglet actif `Code Audit`, écran peu informatif | basculer vers `Visual Tests` ou afficher un état vide explicite |
| `process-results.json` dans review | KO | marqueur `UNIQUE_PROCESS_MARKER_2_3_8` absent après rebuild | intégrer le process dans la review ou corriger la doc |
| `sg-visual-run --from-process` E2E | BLOQUÉ | pas de commande shell `sg-visual-run` | fournir runner pour tester la production initiale |
| `sg-ship` E2E | BLOQUÉ | pas de commande shell `sg-ship` | fournir runner orchestrateur |

## Blocages prioritaires

| Priorité | Blocage | Pourquoi c'est bloquant | Preuve | Demande |
|---:|---|---|---|---|
| P0 | Absence de CLI ou runner officiel | Impossible de rejouer toutes les phases en recette Codex reproductible | commandes `shipguard`, `sg-ship`, `sg-code-audit`, `sg-process-check`, `sg-visual-run` absentes | ajouter un entrypoint CLI ou un runner documenté |
| P0 | `process-results.json` non consommé par la review | Le contrat `process -> review` annoncé ne se matérialise pas dans le dashboard | `PROCESS_MARKER_ABSENT` après rebuild | intégrer `process-results.json` dans `build-review.mjs` ou corriger la documentation |
| P1 | `sg-visual-discover` natif non prouvé | Les manifests propres existent, mais leur génération ne vient pas du skill ShipGuard | absence d'entrypoint exécutable pour `/sg-visual-discover` | fournir runner, smoke ou procédure E2E vérifiable |
| P1 | `sg-change-report` sans smoke officiel | Le contrat fonctionne en fixture, mais il n'y a pas de test de référence livré | fixture recette : persona reports générés | fournir une fixture ou un smoke officiel |
| P1 | `HEAD /favicon.ico` en `404` | Incohérence HTTP du serveur review | `GET /favicon.ico -> 204`, `HEAD /favicon.ico -> 404` | traiter `HEAD` comme `GET` |
| P2 | Dashboard sans audit code | L'utilisateur peut croire que le dashboard est vide malgré des visuels disponibles | screenshot `dashboard-no-audit-default.png`, onglet actif `Code Audit` | ouvrir `Visual Tests` par défaut ou afficher un état vide explicite |
| P2 | JSON sans saut final | Artefacts générés moins propres et diffs fragiles | `final newline missing` sur deux JSON | garantir un saut de ligne final unique |

## Couverture explicite des 12 skills

| Skill | Verdict actuel | Remontée Loïc |
|---|---|---|
| `sg-change-report` | OK fixture | ajouter fixture ou smoke officiel |
| `sg-code-audit` | BLOQUÉ natif | runner officiel manquant |
| `sg-improve` | OK dry-run et rollback smoke | rien immédiat |
| `sg-process-check` | BLOQUÉ natif | runner officiel manquant |
| `sg-record` | OK preflight et tests internes, humain à tester | rien immédiat |
| `sg-scout` | OK offline dry-run, GitHub réel à tester | rien immédiat |
| `sg-ship` | BLOQUÉ natif | runner orchestrateur manquant |
| `sg-visual-discover` | BLOQUÉ natif | runner ou procédure E2E vérifiable manquants |
| `sg-visual-fix` | OK dry-run, réel hors périmètre | rien immédiat |
| `sg-visual-review` | OK build et serveur | corriger intégration process et favicon `HEAD` |
| `sg-visual-review-stop` | OK fixture | rien immédiat |
| `sg-visual-run` | OK harnais, BLOQUÉ natif | runner officiel manquant |

## Points déjà réglés par 2.3.8

| Ancien blocage | Verdict 2.3.8 | Preuve |
|---|---|---|
| `agents.undefined` | corrigé | aucune clé `undefined` après updates monitor |
| doublon `r1:z1` / `z1` | corrigé | clé canonique `z1`, alias `r1:z1` |
| update sans identifiant | corrigé | HTTP `400` |
| `id`, `agent_id`, `zone_id` | corrigé | les trois formes renvoient `200` |
| `run_id` et `scope` écrasés au rebuild | corrigé | fixture `from-process` préservée |
| routes non exécutables perdues | corrigé au rebuild | `skipped` et `uncovered` préservés |

## Ce qu'il reste à tester après correction amont

| Test | Dépendance | Critère OK |
|---|---|---|
| `sg-code-audit --report-only` natif | CLI ou runner officiel | `audit-results.json` produit par ShipGuard, pas par le harnais |
| `sg-process-check --mode=reason` natif | CLI ou runner officiel | `process-results.json` et `process-report.md` produits |
| `sg-visual-discover --all` | CLI ou runner officiel | `_config.yaml` et manifests `source: discovered` produits par ShipGuard |
| `sg-visual-discover --diff --refresh-existing` | CLI ou runner officiel | seuls les manifests impactés sont créés ou régénérés |
| `sg-visual-run --from-audit` | CLI ou runner officiel | sous-suite issue de `impacted_ui_routes` |
| `sg-visual-run --from-process` | CLI ou runner officiel | production initiale de `/`, `skipped`, `uncovered` |
| `sg-ship --report-only` | CLI ou runner officiel | audit, process, visual et review enchaînés |
| `sg-change-report` smoke officiel | fixture livrée par le plugin | `change-reports/<id>` source et persona report générés |
| `sg-visual-review-stop` sur serveur utilisateur | fin de recette utilisateur | serveur review arrêté proprement |
| Recorder humain `Check` + `Stop` | action humaine | manifest avec assertion visible dans Recorded Tests |
| `sg-visual-fix` réel | copie isolée | diff contrôlé et capture after |
| `sg-improve` réel | fixture isolée | learning écrit puis rollback prouvé |
