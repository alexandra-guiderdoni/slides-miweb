# Audit pragmatique de ShipGuard

Destinataire : Loïc
Date : 2 juillet 2026
Dépôt audité : `https://github.com/bacoco/ShipGuard`
Révision auditée : `3c8c111` sur `main`
Mode : lecture seule, clone temporaire sous `/tmp/shipguard-audit.1Gtx3i/ShipGuard`

## Verdict

- État global : **prometteur mais fragile**
- Risque principal : ShipGuard expose des workflows ambitieux, parfois mutateurs, mais le harnais de validation, d'installation et de compatibilité runtime n'est pas encore assez solide pour inspirer confiance hors cercle proche.
- Meilleur prochain investissement : rendre le chemin `installation -> smoke tests -> /sg-visual-review -> /sg-ship --report-only` reproductible en une commande, puis corriger les risques dangereux identifiés.

ShipGuard a une vraie direction produit : audits de code, tests visuels, manifests YAML, dashboard de revue et boucle d'apprentissage. Le problème n'est pas l'ambition, mais le décalage entre les promesses "stable / auto-fix / Codex compatible" et la preuve disponible aujourd'hui.

## Cartographie rapide

Surfaces observées :

- Plugin principal : `plugins/shipguard`
- Skills : `sg-code-audit`, `sg-process-check`, `sg-visual-discover`, `sg-visual-run`, `sg-visual-review`, `sg-visual-fix`, `sg-record`, `sg-improve`, `sg-scout`, `sg-ship`, `sg-change-report`, `sg-visual-review-stop`
- Scripts Node : dashboard review, smoke tests, recorder, improve, scout, visual-fix dry-run
- Exemples : manifests YAML sous `examples/` et `visual-tests/`
- Documentation : README racine, README plugin, architecture, roadmap, rapports scout
- CI : absente

Preuves d'inventaire :

- Comptage local hors `.git` : 119 fichiers, dont 49 Markdown, 20 YAML, 11 `.mjs`, 9 JSON et 24 images ; le code exécutable partagé est concentré dans les scripts `.mjs` des skills.
- `find .github` : uniquement templates issue/PR, aucun workflow.
- `find . -name package.json ...` : aucun `package.json`, lockfile ou runner central.
- `git status --short --branch` après audit : `## main...origin/main`.

## Priorités

| Priorité | Sujet | Impact | Preuve | Correction recommandée | Effort |
|---|---|---|---|---|---|
| P0 | `sg-process-check` documente un `reset --hard` non borné | Peut réinitialiser le workspace courant | `sg-process-check/SKILL.md:109,201` | Utiliser `git -C "$baseline" reset --hard "$BASE"` | S |
| P0 | Code audit et `sg-ship` exposés à Codex mais dépendants de l'outil Agent | Exécution Codex trompeuse ou cassée | `README.md:473-484`, `sg-code-audit/SKILL.md:254-266` | Bloquer ou dégrader explicitement hors Agent tool | M |
| P0 | `/sg-code-audit` corrige par défaut | Risque d'éditions et commits inattendus | `sg-code-audit/SKILL.md:16,71`, `agent-prompt.md:186-195` | Faire de `--report-only` le défaut public | S |
| P0 | Pas de CI, pas de `package.json`, pas de runner central | Pas de confiance partageable | `.github` sans workflows ; aucun `package.json`, lockfile, Makefile, Taskfile ou config lint/test centrale | Ajouter scripts smoke + GitHub Action minimale | M |
| P0 | `/sg-visual-review` lance le build avant bootstrap | Premier usage dashboard cassable | `sg-visual-review/SKILL.md:31-37,191-202` | Copier le builder avant la première commande | S |
| P1 | Arrêt serveur par PID/port sans preuve d'identité | Peut tuer un autre service local | `build-review.mjs:145-159,1188-1195`, `sg-visual-review-stop/SKILL.md:21-28` | Vérifier token, cwd ou `/health` avant `kill` | M |
| P1 | Test d'intégration recorder non isolé | Fausse confiance sur macro recorder | Fixture `/tmp` reproduite : `6 pass, 1 fail`, `_config.yaml missing` | Transformer en smoke test `/tmp` complet | S |
| P1 | Exemples non exécutables tels quels | Onboarding fragile | PDF `data-sample/sample-contract.pdf` absent | Ajouter fixture ou rendre les manifests autonomes | S |
| P1 | Versioning public incohérent | Confusion installation / release | Manifests `2.4.0`, tags publics `v3.0.0`, release GitHub `v1.0.0` | Aligner manifests, tags et release notes | S |
| P2 | Docs produit survendent l'auto-fix | Mauvaises attentes utilisateur | `README.md:15,40,51` vs `sg-ship` report-only | Reformuler : fix opt-in seulement | S |
| P2 | Métadonnées marketplace incomplètes | Frein d'adoption | `.codex-plugin/plugin.json:30-38` : privacy/terms pointent vers le dépôt, `screenshots: []` | Ajouter screenshots et liens policy/terms dédiés ou clarifier l'absence | S |

## Findings détaillés

### 1. Commande destructrice ambiguë dans `sg-process-check`

Problème : la recette `git worktree add --detach ... && git reset --hard <BASE>` ne fixe pas le répertoire du `reset`.

Pourquoi c'est important : c'est un risque opérationnel direct. Si la commande est reprise littéralement, le `reset --hard` peut s'exécuter dans le dépôt courant.

Preuve :

- `plugins/shipguard/skills/sg-process-check/SKILL.md:109`
- `plugins/shipguard/skills/sg-process-check/SKILL.md:201`

Correction minimale :

```bash
git worktree add --detach "$baseline" "$BASE"
git -C "$baseline" reset --hard "$BASE"
```

Ne pas faire maintenant : ne pas refondre tout le mode `execute`; corriger d'abord l'invariant dangereux.

### 2. Compatibilité Codex trompeuse pour le code audit

Problème : le README propose une installation Codex, mais le code audit parallèle dépend d'un outil `Agent` avec isolation worktree.

Pourquoi c'est important : `/sg-ship` dépend de `/sg-code-audit`, donc la promesse "Codex compatible" ne tient pas pour le pipeline complet.

Preuve :

- `README.md:117-118` : installation Codex
- `README.md:473-484` : code audit parallèle non supporté sans Agent
- `plugins/shipguard/skills/sg-code-audit/SKILL.md:254-266` : dépendance Agent/worktree
- `plugins/shipguard/skills/sg-ship/agents/openai.yaml:9-19` : dépendances déclarées insuffisantes

Correction minimale : en contexte Codex/OpenAI, détecter l'absence d'Agent tool et afficher un message explicite : code audit sauté, fallback séquentiel non disponible, ou fallback séquentiel expérimental.

Ne pas faire maintenant : ne pas promettre une équivalence Claude/Codex tant que le fallback n'est pas testé.

### 3. `/sg-code-audit` corrige par défaut

Problème : le skill annonce un audit, mais `fix_mode` est `true` par défaut et le prompt agent demande de corriger et committer.

Pourquoi c'est important : pour un outil d'audit partageable, le défaut doit être non mutateur. Les corrections automatiques doivent être opt-in.

Preuve :

- `plugins/shipguard/skills/sg-code-audit/SKILL.md:16`
- `plugins/shipguard/skills/sg-code-audit/SKILL.md:71`
- `plugins/shipguard/skills/sg-code-audit/references/agent-prompt.md:186-195`

Correction minimale : passer `--report-only` en défaut public, et réserver les éditions à `--fix`.

Ne pas faire maintenant : ne pas ajouter plus de logique de merge avant d'avoir clarifié le mode par défaut.

### 4. Absence de CI et de runner central

Problème : les smoke tests existent, mais aucun `package.json`, aucun lockfile, aucune GitHub Action et aucun runner central ne les lance.

Pourquoi c'est important : les claims "stable" ne sont pas étayés par un contrôle reproductible.

Preuve :

- `find .github -maxdepth 3 -type f` : seulement templates issue/PR
- `find .github/workflows ...` : `NO_GITHUB_WORKFLOWS_DIR`
- `find . -name package.json ...` : `NO_NODE_PROJECT_FILES`
- `find . -maxdepth 4 ...` : `NO_TASK_OR_LINT_CONFIG`
- Tests présents : `review-smoke-test.mjs`, `monitor-smoke-test.mjs`, `improve-*`, `scout`, `visual-fix`, `actions-to-yaml.test.mjs`

Correction minimale :

- Ajouter `package.json`
- Ajouter `test:smoke`
- Ajouter `node --check` sur les `.mjs`
- Ajouter validation YAML sans dépendance réseau
- Ajouter GitHub Action qui lance ces commandes

Ne pas faire maintenant : ne pas essayer de faire tourner `agent-browser` en CI tout de suite.

### 5. `/sg-visual-review` peut échouer sur projet frais

Problème : la commande principale suppose `visual-tests/build-review.mjs` déjà présent, puis documente le bootstrap plus bas.

Pourquoi c'est important : la première expérience dashboard est un point d'entrée majeur.

Preuve :

- `plugins/shipguard/skills/sg-visual-review/SKILL.md:31-37`
- `plugins/shipguard/skills/sg-visual-review/SKILL.md:191-202`

Correction minimale : déplacer le bootstrap avant la première exécution du builder, comme le fait déjà `sg-change-report`.

Ne pas faire maintenant : ne pas réécrire le builder HTML.

### 6. Arrêt serveur insuffisamment borné

Problème : `--stop` tue le PID stocké sans vérifier qu'il correspond encore à ShipGuard. Le fallback par port peut tuer un service qui n'est pas ShipGuard.

Pourquoi c'est important : c'est un risque local de nuisance, surtout avec le port 8888.

Preuve :

- `plugins/shipguard/skills/sg-visual-review/build-review.mjs:145-159`
- `plugins/shipguard/skills/sg-visual-review/build-review.mjs:1188-1195`
- `plugins/shipguard/skills/sg-visual-review-stop/SKILL.md:21-28`

Correction minimale : stocker un token serveur, le cwd et le port dans le PID file ; avant `kill`, interroger `/health` et vérifier l'identité.

Ne pas faire maintenant : ne pas ajouter un système de daemon complet.

### 7. Macro recorder : test d'intégration fragile

Problème : `integration-test.mjs` écrit dans son répertoire cible et suppose `build-review.mjs` disponible au bon endroit. En fixture temporaire, il échoue.

Pourquoi c'est important : le macro recorder est annoncé stable, mais son test d'intégration n'est pas raccordé au harnais.

Preuve :

- `plugins/shipguard/skills/sg-record/lib/integration-test.mjs:14-50`
- Exécution en fixture temporaire `/tmp` avec `actions-to-yaml.mjs`, `integration-test.mjs`, `build-review.mjs` et `_review-template.html` : `6 pass, 1 fail`
- Cause reproduite : `Error: visual-tests/_config.yaml missing — run /sg-visual-discover first.`

Correction minimale : transformer ce test en smoke test isolé sous `/tmp`, avec `_config.yaml`, builder et template copiés.

Ne pas faire maintenant : ne pas lancer `sg-record --check` en CI, car cela ouvre Chromium GUI.

### 8. Exemples non autonomes

Problème : l'exemple upload référence un PDF absent ; l'exemple chat dépend d'un test précédent.

Pourquoi c'est important : un exemple doit être copiable ou clairement marqué comme squelette.

Preuve :

- `examples/documents/upload-and-process.yaml:9` : `data-sample/sample-contract.pdf`
- Commande `find ... sample-contract.pdf` : aucun fichier trouvé
- `examples/chat/ask-about-document.yaml:1` : prérequis commentaire
- Contrat upload : `sg-visual-run/references/action-reference.md:99-104`

Correction minimale : ajouter un PDF fixture minimal ou remplacer par un chemin existant ; rendre le scénario chat autonome ou le marquer explicitement comme dépendance de fixture.

Ne pas faire maintenant : ne pas créer une application demo lourde.

### 9. Versioning incohérent

Problème : les manifests annoncent `2.4.0`, la roadmap dit que le manifest est canonique, mais les tags publics incluent `v3.0.0` et aucune release récente ne correspond.

Pourquoi c'est important : pour un plugin installé depuis marketplace, la version doit être compréhensible.

Preuve :

- `plugins/shipguard/.claude-plugin/plugin.json:4` : `2.4.0`
- `plugins/shipguard/.codex-plugin/plugin.json:3` : `2.4.0`
- `docs/product-roadmap.md:3`
- `git ls-remote --tags origin` : `v3.0.0`, `v3.0.0-sprint1`, `v2.2.0`, etc.
- GitHub releases : seule release visible `v1.0.0`

Correction minimale : choisir une source canonique et aligner manifests, tags, release notes et roadmap.

Ne pas faire maintenant : ne pas changer le numéro sans clarifier la politique de release.

### 10. Documentation produit trop optimiste

Problème : le README promet "auto-fix" et "fix automatically", alors que `sg-ship` est report-only par défaut et que les fixes sont opt-in.

Pourquoi c'est important : l'utilisateur doit savoir si ShipGuard observe ou applique des modifications.

Preuve :

- `README.md:15`
- `README.md:40`
- `README.md:51`
- `plugins/shipguard/skills/sg-ship/SKILL.md:33,62,127,135`

Correction minimale : reformuler en "peut proposer ou appliquer des fixes en mode opt-in".

Ne pas faire maintenant : ne pas retirer l'ambition produit ; seulement clarifier les conditions.

## Vérifications réalisées

Commandes lancées :

```bash
node plugins/shipguard/skills/sg-visual-review/review-smoke-test.mjs --port=23101
node plugins/shipguard/skills/sg-visual-review/monitor-smoke-test.mjs --port=23102
node plugins/shipguard/skills/sg-scout/offline-dry-run-smoke-test.mjs
node plugins/shipguard/skills/sg-improve/improve-dry-run-smoke-test.mjs
node plugins/shipguard/skills/sg-improve/improve-rollback-smoke-test.mjs
node plugins/shipguard/skills/sg-visual-fix/visual-fix-dry-run-smoke-test.mjs
node --test plugins/shipguard/skills/sg-record/lib/actions-to-yaml.test.mjs
ruby -r psych -e 'ARGV.each { |f| Psych.load_file(f); puts "YAML_OK #{f}" }' examples/**/*.yaml visual-tests/*.yaml
```

Résultats :

- Review smoke test : passé
- Monitor smoke test : passé
- Scout offline dry-run : passé
- Improve dry-run : passé
- Improve rollback : passé
- Visual-fix dry-run : passé
- `actions-to-yaml.test.mjs` : 21 tests, 21 pass, 0 fail
- YAML exemples et config : syntaxe valide

Vérification non destructive du clone :

```bash
git status --short --branch
# ## main...origin/main
```

## Plan d'action proposé

### Lot 1 : corrections immédiates

Objectif : enlever les risques dangereux et les blocages du premier usage.

1. Borner le `reset --hard` de `sg-process-check`.
2. Passer `sg-code-audit` en report-only par défaut.
3. Ajouter un gate clair si Agent/worktree n'est pas disponible.
4. Déplacer le bootstrap de `sg-visual-review` avant l'exécution du builder.
5. Sécuriser `sg-visual-review-stop` : vérifier l'identité avant `kill`.

Définition de fin :

- Aucun chemin documenté ne contient de commande destructive non bornée.
- Un utilisateur Codex sait exactement quelles lanes sont supportées.
- `/sg-visual-review` fonctionne sur projet frais après présence de `visual-tests/_config.yaml`.

### Lot 2 : stabilisation

Objectif : rendre la qualité reproductible.

1. Ajouter un `package.json` avec scripts :
   - `test:syntax`
   - `test:smoke`
   - `test:yaml`
2. Ajouter une GitHub Action minimale sans dépendance réseau.
3. Convertir `sg-record/lib/integration-test.mjs` en fixture `/tmp`.
4. Ajouter ou corriger les fixtures d'exemples.
5. Ajouter un `.gitignore` cible pour les artefacts transitoires, sans bloquer `change-reports/` et `persona-reports/`.

Définition de fin :

- Une commande locale lance tous les checks non réseau.
- La CI lance la même commande.
- Les exemples ne référencent pas de fichiers absents.

### Lot 3 : amélioration produit

Objectif : rendre ShipGuard partageable sans survente.

1. Aligner version manifest, tags, release notes et roadmap.
2. Reformuler README et README plugin autour de :
   - observe/report-only par défaut ;
   - fix opt-in ;
   - compatibilité Claude/Codex réelle.
3. Compléter les métadonnées marketplace Codex.
4. Marquer les docs scout obsolètes comme livré ou archivé.
5. Garder CI/CD E2E agent-browser comme roadmap, pas comme prérequis immédiat.

## Ce qu'il ne faut pas traiter maintenant

- Ne pas construire une CI E2E complète avec navigateur et application demo.
- Ne pas refondre toute l'architecture des skills.
- Ne pas ajouter d'abstraction runtime avant d'avoir un runner central.
- Ne pas promettre le support Codex complet sans fallback testé.
- Ne pas automatiser plus de fixes tant que le mode report-only n'est pas le défaut.

## Limites de l'audit

Non vérifié :

- Installation marketplace réelle Claude ou Codex.
- Exécution d'un vrai `/sg-visual-run` sur application cible.
- `agent-browser` E2E.
- `sg-record --check`, car cela lance Playwright/Chromium GUI.
- Vrais worktrees Agent Claude.
- Schéma officiel `agents/openai.yaml` hors dépôt.

Contraintes respectées :

- Aucun fichier du dépôt modifié.
- Aucun push.
- Aucune branche créée.
- Aucune installation.
- Aucun script générateur lancé dans le clone.
- Aucun audit offensif de sécurité.

## Conclusion

ShipGuard mérite d'être poursuivi. Le produit a une proposition claire et plusieurs briques fonctionnent déjà en smoke tests isolés. Mais avant de corriger des features avancées, il faut sécuriser les commandes mutatrices, rendre le mode non mutateur par défaut, clarifier la compatibilité Codex et installer un harnais de vérification minimal.

La priorité n'est pas d'ajouter plus d'intelligence ; c'est de rendre les promesses actuelles prouvables.
