# Post-mortem des derniers commits ShipGuard liés à la demande d'Alex

Date : 2 juillet 2026
Référence inspectée : `bacoco/ShipGuard` sur `main`
Commit inspecté : `3c8c111383cae039d282b5c62d3f3cf4b06d40ab`
Clone de vérification : `/tmp/shipguard-upstream-check.c6Q0MD/ShipGuard`
Statut : transmis à Loïc par Alex le 2 juillet 2026.

## Verdict

Les commits récents règlent une partie importante de la demande, mais pas tout.

- Le câblage `process-results.json -> sg-visual-review` est maintenant réel.
- Les deux petites frictions `sg-visual-review` restent ouvertes : `HEAD /favicon.ico` répond encore `404`, et les JSON générés testés n'ont toujours pas de saut de ligne final.
- La question du runner CLI reste une décision produit, pas un bug.
- Trois risques de l'audit indépendant restent pertinents hors prompt du matin : `sg-process-check` documente encore un `reset --hard` ambigu, `/sg-code-audit` corrige encore par défaut, et il n'existe toujours pas de runner/CI central.

Recommandation : faire une PR minimale `sg-visual-review` pour favicon + newline + test Process tab. Ouvrir des issues séparées pour CLI, `sg-code-audit` report-only par défaut, `sg-process-check` baseline et CI.

## Suivi après transmission

État courant :

- Rapport transmis à Loïc.
- Points considérés réglés côté upstream : intégration fonctionnelle de `process-results.json` dans `sg-visual-review`.
- Points encore ouverts à suivre : `HEAD /favicon.ico`, newline final des JSON générés, runner CLI, CI centrale, défaut mutateur de `/sg-code-audit`, formulation `reset --hard` dans `sg-process-check`.

Prochaine action utile :

1. Si Loïc veut une correction courte : PR minimale `sg-visual-review` uniquement.
2. Si Loïc veut une feuille de route : issues séparées pour CLI, CI et modes mutateurs.
3. Si Loïc répond avec de nouveaux commits : relancer la fixture ciblée et mettre à jour la matrice de faits avant toute conclusion.

## Matrice de faits

| Affirmation | Source / commande | Verdict | Impact |
|---|---|---|---|
| Upstream actuel contient des commits après `3bcf382` | `git log --oneline 3bcf382..HEAD` | Observé : 10 commits jusqu'à `3c8c111` | Les corrections de Loïc ont bien été inspectées sur `main` actuel |
| Les smokes review et monitor passent | `node .../review-smoke-test.mjs --port=23141`, `node .../monitor-smoke-test.mjs --port=23142` | Observé : `review smoke test passed`, `monitor smoke test passed` | Le dashboard de base n'est pas cassé globalement |
| `GET /favicon.ico` est traité, pas `HEAD` | Fixture ciblée : `FAVICON_GET=204`, `FAVICON_HEAD=404`; source `build-review.mjs:1329` | Non réglé | Petite régression HTTP upstream, facile à corriger |
| `visual-results.json` et `audit-monitor.json` n'ont pas de newline final | Fixture ciblée : `VISUAL_LAST_BYTE=7d`, `MONITOR_LAST_BYTE=7d`; sources `build-review.mjs:1071`, `build-review.mjs:1224-1225` | Non réglé | Polish reproductibilité/diff, pas bug fonctionnel |
| `process-results.json` est injecté dans la review | Fixture ciblée : `Process check results: found`, `REVIEW_HAS_PROCESS=yes`; sources `build-review.mjs:1116-1145`, `_review-template.html:2509+` | Réglé | La promesse doc -> dashboard est maintenant tenue |
| Le runner CLI natif n'existe pas | `find ... package.json/lockfile/Makefile/Taskfile` sans résultat ; docs centrées slash skills | Non réglé, mais non classé bug | Décision produit à clarifier |
| Il n'y a pas de CI centrale | `.github` contient seulement templates issue/PR ; `NO_GITHUB_WORKFLOWS_DIR` | Toujours vrai | Confiance partageable encore insuffisante |
| `sg-process-check` contient encore `reset --hard` ambigu | `sg-process-check/SKILL.md:109,201` | Toujours vrai | Risque opérationnel séparé |
| `/sg-code-audit` corrige par défaut | `sg-code-audit/SKILL.md:71` | Toujours vrai | Risque d'édition inattendue hors `/sg-ship` |

## Évaluation des quatre points envoyés à Loïc

### 1. `HEAD /favicon.ico`

Verdict : bug upstream non réglé.

Preuve :

```text
FAVICON_GET=204
FAVICON_HEAD=404
```

Source : `plugins/shipguard/skills/sg-visual-review/build-review.mjs:1329` ne traite que `GET /favicon.ico`.

Action minimale :

- Fichier : `plugins/shipguard/skills/sg-visual-review/build-review.mjs`
- Changement attendu : traiter `GET` et `HEAD` sur `/favicon.ico` avec le même statut `204`.
- Vérification : ajouter un assert `HEAD /favicon.ico === 204` dans `review-smoke-test.mjs`.

À ne pas faire maintenant : ne pas refondre le serveur HTTP pour ce point.

### 2. Newline final dans les JSON générés

Verdict : feature request upstream non réglée.

Preuve :

```text
VISUAL_LAST_BYTE=7d
MONITOR_LAST_BYTE=7d
```

`7d` correspond à `}`. Un saut de ligne final serait `0a`.

Sources visibles :

- `build-review.mjs:1071` écrit `visual-results.json` via `JSON.stringify(...)`
- `build-review.mjs:1224-1225` écrit `audit-monitor.json` via `JSON.stringify(...)`

Action minimale :

- Fichier : `plugins/shipguard/skills/sg-visual-review/build-review.mjs`
- Changement attendu : ajouter un helper `writeJson(path, value)` qui écrit `JSON.stringify(value, null, 2) + "\n"`.
- Vérification : test dernier octet `0a` pour `visual-results.json` et `audit-monitor.json`.

À ne pas faire maintenant : ne pas normaliser tout le dépôt dans la même PR.

### 3. `process-results.json` dans la review

Verdict : bug upstream réglé fonctionnellement.

Preuve :

```text
Process check results: found
REVIEW_HAS_PROCESS=yes
```

Sources :

- `build-review.mjs:1116-1145` lit `process-results.json` et l'injecte dans `__PROCESS_DATA__`
- `_review-template.html:2509+` contient le rendu du Process tab
- `sg-visual-review/SKILL.md:46,112` documente cette lecture
- `docs/architecture.md:408,430` documente le Process tab

Action minimale restante :

- Fichier : `plugins/shipguard/skills/sg-visual-review/review-smoke-test.mjs`
- Changement attendu : ajouter une fixture `process-results.json` et vérifier que `review.html` contient un check, une route UI et un endpoint backend.
- Vérification : `node plugins/shipguard/skills/sg-visual-review/review-smoke-test.mjs --port=<port>`.

À ne pas faire maintenant : ne pas demander une nouvelle intégration produit tant que le test de non-régression manque seulement.

### 4. Commandes shell natives / runner CLI

Verdict : feature request produit, pas bug.

Preuve :

- Aucun `package.json`, lockfile, Makefile ou Taskfile trouvé dans le clone inspecté.
- `README.md` et `plugins/shipguard/README.md` documentent surtout les slash skills.
- Les docs clarifient mieux la compatibilité : `Code Audit (parallel)` reste marqué comme dépendant de l'outil `Agent`.

Action minimale :

- Ouvrir une issue de décision produit : ShipGuard veut-il un runner CLI reproductible hors slash skills ?
- Définir seulement un contrat de premier niveau : `shipguard review`, `shipguard smoke`, `shipguard ship --report-only`, ou décider explicitement que ce n'est pas l'objectif.

À ne pas faire maintenant : ne pas mélanger ce runner CLI avec la PR favicon/newline/process smoke.

## Reste à traiter hors prompt du matin

Ces points viennent de l'audit indépendant et restent visibles sur le commit inspecté.

1. `sg-process-check` : remplacer la formulation `git worktree add --detach ... && git reset --hard <BASE>` par une commande bornée au worktree, par exemple `git -C "$baseline" reset --hard "$BASE"`.
2. `/sg-code-audit` : passer le défaut public en report-only ou clarifier beaucoup plus fortement que la commande seule peut corriger et committer.
3. CI minimale : ajouter un runner central qui lance les smokes Node existants et les tests de contrats, sans tenter tout de suite un E2E `agent-browser`.

## PR minimale recommandée

Nom proposé : `fix(sg-visual-review): align favicon HEAD, normalize json output, cover process tab`

Périmètre :

- `plugins/shipguard/skills/sg-visual-review/build-review.mjs`
- `plugins/shipguard/skills/sg-visual-review/review-smoke-test.mjs`
- éventuellement `plugins/shipguard/skills/sg-visual-review/SKILL.md` si le comportement newline est documenté

Critères d'acceptation :

- `GET /favicon.ico` et `HEAD /favicon.ico` retournent `204`.
- `visual-results.json` et `audit-monitor.json` écrits par le builder/serveur finissent par exactement un saut de ligne.
- `review-smoke-test.mjs` couvre une fixture `process-results.json` et échoue si le Process tab n'est plus injecté.
- Les smokes existants restent verts.

Commandes à lancer :

```bash
node plugins/shipguard/skills/sg-visual-review/review-smoke-test.mjs --port=23101
node plugins/shipguard/skills/sg-visual-review/monitor-smoke-test.mjs --port=23102
node --test plugins/shipguard/skills/sg-record/lib/actions-to-yaml.test.mjs
```

## Prompt Fable resserré pour la suite

```text
Contexte :
Tu es dans le dépôt ShipGuard. Alex a signalé quatre frictions après une recette propre : favicon HEAD/GET, newline final des JSON générés, intégration process-results.json dans la review, et question produit sur un runner CLI hors slash skills.

Mission :
Inspecte le commit courant avant de conclure. Classe chaque point en bug upstream, documentation seulement, feature request, local au harnais Alex, ou non pertinent. Pour chaque point upstream, propose l'action minimale : fichiers concernés, changement attendu, test à lancer.

Effort :
high. La tâche est courte mais exige une preuve source et une vérification ciblée.

Autonomie :
Évaluer et s'arrêter. Ne commit rien, n'ouvre pas d'issue, ne crée pas de PR. Ne traite pas le post-mortem complet d'Alex.

Vérification :
Donne le SHA inspecté, les commandes lancées et les sorties décisives. Si un point n'est pas vérifié, écris `non vérifié` et dis pourquoi.

Communication :
Commence par le verdict. Réponse courte, orientée décision, sans historique. Ne reproduis pas ton raisonnement privé.
```

## Limites

- Installation marketplace réelle non relancée.
- Aucun vrai `/sg-visual-run` avec `agent-browser` relancé dans cette passe.
- Pas de validation par navigateur du rendu visuel du Process tab ; la preuve est l'injection HTML et les smokes Node.
- PDD appliqué en mode documentation ciblée : pas de génération `.pdd/`, car la demande porte sur un Markdown unique.

PDG self-check, pas revue indépendante.
