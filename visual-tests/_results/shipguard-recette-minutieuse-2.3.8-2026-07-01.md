# Recette minutieuse ShipGuard 2.3.8

Date : 2026-07-01

Périmètre : clean install ShipGuard 2.3.8, site statique MiWeb, harnais
`visual-tests/` reconstruit proprement. Objectif : prouver ce qui fonctionne,
nommer ce qui reste non prouvé, et transformer chaque blocage ShipGuard en
amélioration actionnable pour Loïc.

## Verdict court

ShipGuard 2.3.8 corrige bien les blocages monitor et le rebuild ciblé. Le
dashboard, le monitor, le recorder preflight, les smokes embarqués, le run
visuel complet et les contrats de rebuild sont exploitables.

Les limites restantes sont surtout des limites de testabilité ou de contrat
produit : pas de runner CLI `sg-*`, `process-results.json` non intégré à la
review, `HEAD /favicon.ico` en `404`, JSON générés sans saut final, et dashboard
confus quand les résultats visuels existent sans audit code.

## Preuves exécutées

| Phase | Preuve fraîche | Verdict |
|---|---|---|
| Installation Codex | `shipguard@shipguard 2.3.8` listé | OK |
| Installation Claude | `shipguard@shipguard 2.3.8`, `Validation passed` | OK |
| Inventaire plugin | 12 skills dans les caches Codex et Claude | OK |
| CLI shell | `shipguard` et tous les `sg-*` absents | BLOQUÉ natif |
| Syntaxe scripts | `node --check` sur build, review, monitor, recorder | OK |
| Review smoke | `review smoke test passed` | OK |
| Monitor smoke | `monitor smoke test passed` | OK |
| Recorder tests | `actionsToYaml` 13 pass, intégration 11 pass | OK |
| Recorder preflight | `PLAYWRIGHT_OK`, `CHROMIUM_OK`, `GUI_LAUNCH_OK` | OK |
| Scout smoke | `scout offline dry-run smoke test passed` | OK |
| Visual-fix smoke | `visual-fix dry-run smoke test passed` | OK |
| Improve smokes | dry-run et rollback passés | OK |
| Tests MiWeb | 21 tests racine, 1 skipped ; 10 variantes validées | OK |
| Run visuel frais | 31 manifests, 31 PASS, 31 screenshots | OK |
| Dashboard HTTP | `/`, `/health`, `/visual-results.json`, `/audit-results.json` en `200` | OK |
| Dashboard UI | Code Audit `0 bugs`, Visual Tests `31 PASS` visibles | OK |
| Monitor live | `id`, `agent_id`, `zone_id` acceptés ; sans id `400` | OK |
| Monitor canonicalisation | clés `z1,z2,z3`, alias `r1:z*`, pas de `undefined` | OK |
| `from-process` rebuild | `run_id`, `scope`, `/`, `skipped`, `uncovered` préservés | OK |
| `process-results.json` review | marqueur unique absent de `review.html` | KO |
| `sg-change-report` fixture | 5 rapports persona attendus présents | OK fixture |
| `/save-manifest` | POST valide `200`, JSON invalide `400`, fichier écrit | OK fixture |
| `sg-visual-review-stop` | serveur isolé arrêté, port fermé | OK fixture |
| Favicon | `GET /favicon.ico -> 204`, `HEAD -> 404` | KO |
| Hygiène JSON | `visual-results.json`, `audit-monitor.json` sans saut final | KO |
| `git diff --check` | aucune erreur | OK |

Artefacts frais :

- `visual-tests/_results/recipe-20260701T1318/visual-results.json`
- `visual-tests/_results/recipe-20260701T1318/screenshots/`
- `visual-tests/_results/recipe-20260701T1318/dashboard-default.png`
- `visual-tests/_results/recipe-20260701T1318/dashboard-visual-tests.png`
- `visual-tests/_results/recipe-20260701T1318/dashboard-code-audit.png`
- `visual-tests/_results/recipe-20260701T1318/dashboard-no-audit-default.png`

## Couverture des 12 skills

| Skill | Recette | Verdict |
|---|---|---|
| `sg-change-report` | source `report.json` + screenshots, rebuild, persona reports | OK fixture |
| `sg-code-audit` | dashboard avec `audit-results.json` de harnais | BLOQUÉ natif : pas de runner |
| `sg-improve` | dry-run smoke + rollback smoke | OK smoke |
| `sg-process-check` | contrat `process-results.json` vers review | KO review, BLOQUÉ natif |
| `sg-record` | preflight + tests YAML + intégration | OK partiel ; humain non automatisé |
| `sg-scout` | offline dry-run smoke | OK smoke ; GitHub réel non exercé |
| `sg-ship` | orchestration complète | BLOQUÉ natif : pas de runner |
| `sg-visual-discover` | manifests propres présents | BLOQUÉ natif : production non prouvable |
| `sg-visual-fix` | dry-run smoke | OK smoke ; correction réelle non exercée |
| `sg-visual-review` | build, serveur, UI, endpoints, save-manifest | OK avec défauts listés |
| `sg-visual-review-stop` | serveur isolé stoppé | OK fixture |
| `sg-visual-run` | run Playwright de recette 31/31 | OK harnais ; runner natif absent |

## Améliorations à remonter à Loïc

| Priorité | Point | Pourquoi c'est bloquant | Amélioration attendue |
|---:|---|---|---|
| P0 | Pas d'entrypoint CLI ou runner officiel | Impossible de rejouer en E2E natif `sg-code-audit`, `sg-process-check`, `sg-visual-discover`, `sg-visual-run`, `sg-ship` et les modes `--from-*` | fournir un runner documenté ou assumer officiellement le mode skill-only avec une procédure de preuve |
| P0 | `process-results.json` non consommé par la review | `sg-process-check` et `sg-ship` promettent une consolidation process, mais le marqueur unique reste absent du dashboard | intégrer `process-results.json` dans `build-review.mjs` ou corriger la documentation |
| P1 | `HEAD /favicon.ico` en `404` | serveur HTTP incohérent ; des clients peuvent prévoler en `HEAD` | traiter `HEAD` comme `GET` pour `/favicon.ico` |
| P1 | JSON générés sans saut final | diffs moins propres et hygiène texte fragile | écrire les JSON générés avec un saut final unique |
| P1 | `sg-visual-discover` non prouvable nativement | les manifests existent, mais la génération par le skill n'a pas de preuve automatisable | ajouter une fixture ou un smoke officiel de découverte |
| P1 | `sg-code-audit` et `sg-process-check` natifs non prouvables | les sorties actuelles sont des artefacts de harnais, pas des résultats produits par ShipGuard | fournir un mode report-only exécutable hors conversation |
| P1 | `sg-record` humain non automatisé | `Check` + `Stop` restent à valider manuellement | ajouter un smoke headless ou une fixture recorder E2E |
| P1 | `sg-change-report` sans smoke officiel | le contrat fonctionne en fixture, mais le plugin ne fournit pas de test de référence | ajouter un smoke change-report avec screenshots et rapports persona |
| P2 | Dashboard sans audit code | avec `visual-results.json` seul, l'onglet actif reste `Code Audit` et l'écran paraît vide | ouvrir `Visual Tests` par défaut si aucun audit code n'existe, ou afficher un état vide explicite |
| P2 | Contrat `visual-results.json` à clarifier | les champs enrichis sont sous `scope`, ce qui doit être explicite dans la doc | documenter précisément l'emplacement des champs `selected_*` et `uncovered_routes` |

## Ce qui reste volontairement non exercé

- `sg-visual-fix` réel sur le site principal : exclu pour éviter une écriture
  fonctionnelle hors demande.
- `sg-improve` réel durable dans `.shipguard/` : couvert par smoke rollback,
  pas exécuté sur le dépôt MiWeb.
- `sg-scout` GitHub réel : non lancé, car le smoke offline suffit à la recette
  locale et un mode GitHub peut produire des sorties externes.
- Recorder humain complet : préflight et intégration OK, mais pas de parcours
  manuel `Check` + `Stop` pendant cette passe.

## Conclusion

La 2.3.8 est exploitable pour review visuelle, monitor live, recorder preflight,
change-report en fixture, stop serveur et full visual run de harnais. Elle ne
donne pas encore une recette E2E native complète, car les phases principales
restent non rejouables sans entrypoint officiel et la review ne consolide pas
encore le process.
