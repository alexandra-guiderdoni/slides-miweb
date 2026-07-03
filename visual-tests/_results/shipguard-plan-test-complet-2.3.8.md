# Plan de test complet ShipGuard 2.3.8

Date : 2026-07-01

Périmètre : plugin ShipGuard 2.3.8 installé proprement dans Codex et Claude,
sur le site statique MiWeb. Le but est de vérifier les fonctionnalités
ShipGuard, pas de corriger le site.

## Critère de fin

La recette est complète quand chaque fonctionnalité ShipGuard a un verdict :

- `OK` : test exécuté, preuve observable, résultat conforme ;
- `KO` : test exécuté, défaut reproductible ;
- `BLOQUÉ` : test non exécutable à cause d'une limite du plugin ou du dépôt
  ShipGuard amont ;
- `HORS PÉRIMÈTRE` : non applicable au site statique MiWeb ou nécessite une
  action volontairement exclue.

Tout blocage doit préciser le composant, la surface tentée, la raison qui
empêche la preuve et la suite attendue côté Loïc.

## Environnement de référence

| Élément | État attendu | Preuve actuelle |
|---|---|---|
| Plugin Codex | `shipguard@shipguard 2.3.8` installé et activé | OK |
| Plugin Claude | `shipguard@shipguard 2.3.8` installé et activé | OK |
| Commit amont | `3bcf382 fix: normalize monitor agent ids` | OK |
| Cache Codex | recréé après purge | OK |
| Cache Claude | recréé après purge | OK |
| Playwright Node local | importable depuis `visual-tests/` | OK |
| Site local | `http://127.0.0.1:8001/` | à relancer selon besoin |
| Review locale | `http://127.0.0.1:23131/` | active pendant recette |

## Matrice de couverture

| Fonctionnalité | Test complet à exécuter | Preuve attendue | Statut actuel | Blocage ou suite |
|---|---|---|---|---|
| Installation Codex | désinstaller, purger cache, réinstaller `shipguard@shipguard` | liste Codex en `2.3.8`, cache recréé | OK | aucun |
| Installation Claude | désinstaller, purger cache, réinstaller `shipguard@shipguard` | liste Claude en `2.3.8`, validation plugin OK | OK | aucun |
| Inventaire plugin | `claude plugin details shipguard@shipguard` | 12 skills listés | OK | aucun |
| CLI reproductible | chercher `shipguard` et les commandes `sg-*` | commandes trouvées | BLOQUÉ | aucune commande shell installée ; demander un entrypoint CLI ou runner officiel |
| `sg-visual-review` build | `node visual-tests/build-review.mjs` | `review.html`, `visual-results.json` conservé | OK | aucun |
| `sg-visual-review` serveur | `node visual-tests/build-review.mjs --serve --port=23131` | HTTP `200` sur `/` et `/visual-results.json` | OK | onglet par défaut confus si pas d'audit |
| `sg-visual-review-stop` | `node visual-tests/build-review.mjs --stop` sur serveur isolé | `.server.pid` retiré, port fermé | OK fixture | serveur utilisateur `23131` laissé actif |
| Onglet Code Audit | fournir `audit-results.json` valide à zéro bug | dashboard affiche `0 bugs found` | OK harnais | pas un vrai `sg-code-audit` ; voir blocage CLI |
| Dashboard sans audit code | retirer `audit-results.json` sur fixture | état par défaut clair | KO UX | onglet actif `Code Audit` malgré résultats visuels |
| Onglet Visual Tests | ouvrir `Visual Tests` | 31 cartes PASS visibles | OK | aucun |
| Onglet Recorded Tests | ajouter un manifest recorder puis rebuild | manifest visible dans l'onglet | À TESTER | nécessite un vrai run recorder humain |
| `review-smoke-test` | `node visual-tests/review-smoke-test.mjs --port=...` | `review smoke test passed` | OK | aucun |
| Monitor smoke | `node visual-tests/monitor-smoke-test.mjs --port=...` | `monitor smoke test passed` | OK | aucun |
| Monitor live réel | POST start/update/status/complete | clés `z1,z2,z3`, pas de `undefined` | OK | aucun |
| Monitor `id` | update `{"id":"z1"}` | HTTP `200`, agent `z1` | OK | aucun |
| Monitor `agent_id` | update `{"agent_id":"z2"}` | HTTP `200`, agent `z2` | OK | aucun |
| Monitor `zone_id` | update `{"zone_id":"r1:z3"}` | HTTP `200`, agent `z3` | OK | aucun |
| Monitor sans identifiant | update sans `id`, `agent_id`, `zone_id` | HTTP `400` | OK | aucun |
| Favicon GET | `curl /favicon.ico` | HTTP `204` | OK | aucun |
| Favicon HEAD | `curl -I /favicon.ico` | HTTP `204` attendu | KO | ShipGuard renvoie encore `404` ; corriger handler HEAD |
| Contrat `visual-results.json` global | run 31 manifests | `run_id`, `scope`, 31 PASS | OK | aucun |
| Rebuild `run_id/scope` | fixture `from-process` puis rebuild | `run_id` et `scope` conservés | OK | aucun |
| Rebuild `/` racine | fixture avec `/` et page secondaire | seul root reste sélectionné | OK au rebuild | production initiale non prouvée sans runner `sg-visual-run` |
| Routes `skipped` | fixture avec ZIP non HTML | route conservée en `skipped` | OK au rebuild | production initiale non prouvée sans runner |
| Routes `uncovered` | fixture avec `/review.html` sans manifest | route conservée en `uncovered` | OK au rebuild | production initiale non prouvée sans runner |
| `sg-visual-discover --all` | lancer la découverte native | `_config.yaml` et manifests `source: discovered` produits | BLOQUÉ | pas d'entrypoint CLI ; manifests actuels générés par harnais |
| `sg-visual-discover --diff/--refresh-existing` | fixture avec diff UI puis découverte native | seuls les manifests impactés sont créés ou régénérés | BLOQUÉ | même blocage runner |
| `sg-visual-run --all` | lancer la commande officielle | `visual-results.json` produit par ShipGuard | BLOQUÉ | pas de commande shell `sg-visual-run` |
| `sg-visual-run --from-audit` | fournir `audit-results.json`, lancer runner officiel | sous-suite des routes impactées | BLOQUÉ | pas de runner officiel exécutable |
| `sg-visual-run --from-process` | fournir `process-results.json`, lancer runner officiel | sous-suite process, `/`, `skipped`, `uncovered` produits | BLOQUÉ | point clé à demander à Loïc |
| `sg-code-audit` | lancer audit ShipGuard report-only | `audit-results.json` ShipGuard natif | BLOQUÉ | pas de commande shell ; audit actuel est un artefact de harnais |
| `sg-process-check` | lancer mode `reason` puis `hybrid` | `process-results.json`, `process-report.md` | BLOQUÉ | pas de commande shell ; skill non mesurable par CLI |
| `process-results.json` dans review | créer marqueur unique puis rebuild | marqueur visible dans review | KO | `PROCESS_MARKER_ABSENT`; intégrer le process dans `build-review.mjs` ou corriger la doc |
| `sg-ship` orchestrateur | lancer workflow complet report-only | audit, process, visual, review enchaînés | BLOQUÉ | pas de commande shell `sg-ship` |
| `sg-change-report` | créer `change-reports/<id>/report.json`, ajouter screenshots, rebuild review | source durable et rapport persona généré | OK fixture | fournir un smoke officiel côté plugin |
| Recorder preflight | `node visual-tests/sg-record.mjs --check` | `PLAYWRIGHT_OK`, `CHROMIUM_OK`, `GUI_LAUNCH_OK` | OK | aucun |
| Recorder YAML | `actions-to-yaml.test.mjs` | 13 pass | OK | aucun |
| Recorder intégration | `integration-test.mjs` | 11 pass | OK | aucun |
| Recorder humain | lancer recorder, utiliser Check, Stop | manifest avec `assert_text`, visible en review | À TESTER | nécessite interaction humaine réelle |
| `sg-visual-fix` dry-run | smoke amont | `visual-fix dry-run smoke test passed` | OK | aucun |
| `sg-visual-fix` réel | correction sur copie isolée | diff contrôlé, screenshot after | HORS PÉRIMÈTRE temporaire | écriture réelle à valider avant exécution |
| `sg-scout` offline | smoke amont | `scout offline dry-run smoke test passed` | OK | aucun |
| `sg-scout` GitHub réel | recherche GitHub sans issue | rapport local, pas d'issue créée | À TESTER | nécessite accord réseau/écriture selon mode |
| `sg-improve` dry-run | smoke amont | `improve dry-run smoke test passed` | OK | aucun |
| `sg-improve` rollback | smoke amont | `improve rollback smoke test passed` | OK | aucun |
| `sg-improve` réel | écrire `.shipguard/` sur fixture | learning + rollback prouvés | HORS PÉRIMÈTRE temporaire | écriture durable à valider |
| Artefacts générés | contrôler fins de ligne et espaces | aucun défaut texte | KO | `visual-results.json` et `audit-monitor.json` sans saut final |

## Ordre de test recommandé

1. **Socle validé** : installation propre, smokes review/monitor/recorder/scout/improve/visual-fix, audit statique MiWeb, run visuel 31/31.
2. **Interactif restant** : recorder humain `Check` puis `Stop`, review UI.
3. **Bloqué par absence de CLI** : `sg-visual-discover`, `sg-code-audit`, `sg-process-check`, `sg-visual-run`, `sg-ship`.
4. **Copie isolée seulement** : `sg-visual-fix` réel, `sg-improve` réel, `sg-process-check --mode=execute`.

## Blocages à remonter à Loïc maintenant

### B1 - Absence de CLI ou runner officiel

Surface tentée : `shipguard`, `sg-ship`, `sg-code-audit`,
`sg-process-check`, `sg-change-report`, `sg-visual-discover`,
`sg-visual-run`, `sg-visual-review`.

Résultat : aucune commande shell disponible après clean install.

Pourquoi cela bloque : on ne peut pas prouver en E2E reproductible les phases
documentées comme `sg-code-audit`, `sg-process-check`,
`sg-visual-discover`, `sg-visual-run --from-process` ou `sg-ship`. Les tests
actuels prouvent les scripts livrés et les contrats de rebuild, pas l'exécution
complète des skills.

Attendu côté Loïc : fournir un entrypoint CLI ou un runner documenté capable de
rejouer les skills hors conversation interactive.

### B2 - `process-results.json` non consommé par la review

Surface testée : fixture temporaire avec `process-results.json` contenant
`UNIQUE_PROCESS_MARKER_2_3_8`, puis rebuild avec `build-review.mjs`.
Résultat : `PROCESS_MARKER_ABSENT`.

Pourquoi cela bloque : `sg-process-check` et `sg-ship` annoncent que les
résultats process apparaissent dans `sg-visual-review`, mais le dashboard 2.3.8
ne semble pas les intégrer.

Attendu côté Loïc : intégrer `process-results.json` dans la review ou corriger
la documentation.

### B3 - `HEAD /favicon.ico` renvoie encore `404`

Surface testée : `GET /favicon.ico -> 204`, `HEAD /favicon.ico -> 404`.

Pourquoi cela bloque : le serveur review est incohérent selon la méthode HTTP.
Certains clients ou prévols peuvent utiliser `HEAD`.

Attendu côté Loïc : traiter `HEAD /favicon.ico` comme `GET /favicon.ico`, ou
documenter et tester explicitement le comportement.

### B4 - JSON générés sans saut de ligne final

Surface testée : artefacts générés par `build-review.mjs`.
Résultat : `audit-monitor.json` et `visual-results.json` sans saut final.

Pourquoi cela bloque : les sorties générées ne respectent pas une hygiène texte
standard et créent des diffs moins propres.

Attendu côté Loïc : normaliser toutes les écritures texte générées avec un saut
de ligne final unique.

## Points non bloquants mais à surveiller

- Le dashboard ouvre par défaut l'onglet Code Audit. Si aucun
  `audit-results.json` n'existe mais que `visual-results.json` existe,
  l'utilisateur croit que la page est vide.
- Le `sg-record --check` passe, mais le parcours humain `Check` + `Stop` reste
  à valider.
- Les workflows réels `sg-visual-fix` et `sg-improve` doivent être testés sur
  copie isolée pour ne pas modifier le site principal.

## Prochaine passe proposée

1. Tester recorder humain, annotation review et génération de `fix-manifest.json`.
2. Demander à Loïc un runner officiel, puis rejouer `sg-visual-discover --all`, `sg-visual-discover --diff=<ref> --refresh-existing`, `sg-code-audit --report-only`, `sg-process-check --mode=reason`, `sg-visual-run --from-audit`, `sg-visual-run --from-process`, `sg-ship --report-only`.
3. Sur copie isolée, tester `sg-visual-fix` réel et `sg-improve` réel avec rollback.
