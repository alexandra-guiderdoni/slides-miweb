## INVARIANTS
- working directory : `/Users/alex/Claude/projets-heberges/slides-miweb`
- branche : `main` ; base et suivi : `origin/main`
- dernier commit produit : `182dde45255c2c482c22a843ee98f3aa66ea1c0c` - `Publie la série Internationalisation Opquast V2`
- tag de retour local et distant : `checkpoint-2026-09-29-0131-CEST`, résolu vers `182dde4`
- état de clôture avant cette sauvegarde : arbre propre, `HEAD`, `origin/main` local et `main` GitHub au même SHA
- branches locales : uniquement `main`
- branches distantes GitHub : uniquement `main`
- worktrees : uniquement le dépôt courant sur `main`
- skill actif à la clôture : `sauvegarde-git` ; aucun chantier d'implémentation actif
- langue de travail et de documentation : français
- contenus éditoriaux et notes orales : uniquement le tiret simple
- séries publiées : immuables ; une évolution devient une variante autonome
- pour toute série Opquast : le skill ou MCP Opquast valide le fond, la transcription décrit le visuel et le discours oral apporte un éclairage distinct
- publication racine : utiliser `matrice-slide-ai/publish_variant.py`, puis vérifier automatiquement l'accueil, le ZIP, la version locale et la version publique
- préférence utilisateur confirmée : ne pas attendre une demande supplémentaire pour rendre une nouvelle variante visible sur l'accueil et effectuer la recette de publication prévue par le workflow

## STATE
### completed
- [x] Internationalisation Opquast V2 publiée dans `internationalisation-opquast-v5-v2/`
- [x] ancienne série `internationalisation-opquast-v5/` retirée après remplacement par la V2
- [x] accueil racine et `published-versions.json` mis à jour avec la date d'origine du 17 septembre 2026 et la mise à jour du 29 septembre 2026
- [x] ordre d'accueil validé : Internationalisation V2 avant Navigation V2 et Contenus V2
- [x] contrôles Internationalisation V2 : 15 slides, 0 erreur, 0 avertissement
- [x] tests communs `scripts/tests` : 8 réussis
- [x] validation de variante : 11 tests réussis
- [x] accueil GitHub Pages et Internationalisation V2 vérifiés en HTTP 200
- [x] revue Claude Fable des issues #11 et #12 terminée en lecture seule avec verdict `VALIDÉ SOUS RÉSERVE`
- [x] réserves Fable vérifiées dans le code puis intégrées aux tickets
- [x] cinq décisions de conception validées par le mainteneur et inscrites dans les tickets
- [x] issue #11 `[Matrice] Durcir la génération et les contrôles des futures variantes` : labels `bug` et `ready-for-agent`
- [x] issue #12 `[Usine Opquast] Bloquer la publication sans revue factuelle et visuelle traçable` : labels `enhancement` et `ready-for-agent`
- [x] aucun commentaire de triage ajouté ; marqueur IA conservé dans les deux corps
- [x] commit `182dde4`, branche `main` et tag `checkpoint-2026-09-29-0131-CEST` poussés
- [x] audit final Git : aucun fichier modifié, indexé ou non suivi ; aucune branche ancienne locale ou distante

### in progress
- [~] aucun travail en cours

### pending
- [ ] implémenter l'issue #11 sans modifier les variantes déjà publiées
- [ ] implémenter l'issue #12 après ou avec l'interface stabilisée par #11, tout en conservant les deux tickets séparés
- [ ] traiter plus tard les issues de séries Opquast #3 à #10 selon les priorités de présentation

### blocked
- [ ] aucun blocage connu

## DECISIONS
1. **Rendu du message canonique** - Le générateur doit rendre `message` séparément dans la présentation, `alternatives.html` et `alternatives.md`. Le build refuse une transcription contenant déjà une section `Message à retenir`. Seul `slides.example.json` est migré ; aucune variante publiée n'est réécrite. Rejeté : détection silencieuse qui masquerait une duplication.
2. **Complétude mécanique des transcriptions** - Chaque slide future porte une liste non vide `donnees_a_transcrire`. Après normalisation documentée de la casse, des espaces et d'Unicode, chaque valeur doit apparaître dans la transcription. Rejeté : imposer la reprise exhaustive de tous les textes visibles.
3. **Dimensions des slides** - `variant.json` porte `slide_dimensions.width` et `slide_dimensions.height`, avec 1672 x 941 par défaut. Le build lit l'en-tête IHDR du PNG avec la bibliothèque standard. Rejeté : nouvelle dépendance externe ou dimensions HTML non vérifiées.
4. **Provenance du générateur** - `variant.json` porte `generator_provenance` avec au minimum `source`, `schema_version` et `build_sha256`. La chaîne `matrice-slide-ai` est tolérée uniquement dans cette métadonnée ; toute dépendance d'exécution reste interdite.
5. **Reçu Opquast canonique** - Le fichier est `source/revue-opquast.json` avec `schema_version: 1`. Il complète `imagegen-receipt.tsv` sans dupliquer son contenu.
6. **Identités de revue** - `producer` et `reviewer` sont des objets déclaratifs. Une personne utilise un identifiant GitHub ; un agent déclare outil, modèle et `run_id`. Leurs identifiants canoniques doivent être distincts. Rejeté : prétendre à une preuve cryptographique non disponible.
7. **Politique de publication Opquast** - `valide` autorise, `bloque` refuse, `valide_avec_reserves` refuse par défaut. Une publication avec réserves exige `maintainer_approval` avec identité GitHub, date, décision `approve` et réserves acceptées. Les réserves et mentions `à vérifier` restent visibles.
8. **Séparation des tickets** - #11 reste générique et corrige la matrice ; #12 reste spécifique au workflow Opquast. Le contrôle manuel traçable de #12 complète la complétude mécanique de #11.
9. **Point de retour Git** - Le tag annoté `checkpoint-2026-09-29-0131-CEST` est le point de retour avant les prochains travaux.

## ARTEFACTS
### modified and published
- `/Users/alex/Claude/projets-heberges/slides-miweb/index.html:369` - tuile Internationalisation V2, placée avant Navigation et Contenus
- `/Users/alex/Claude/projets-heberges/slides-miweb/published-versions.json:100` - entrée Internationalisation V2 avec dates d'origine et de mise à jour
- `/Users/alex/Claude/projets-heberges/slides-miweb/internationalisation-opquast-v5-v2/` - série autonome publiée, générateur, sources, 15 rasters, tests et ZIP
- `/Users/alex/Claude/projets-heberges/slides-miweb/internationalisation-opquast-v5/` - ancienne série supprimée
- commit publié : `182dde45255c2c482c22a843ee98f3aa66ea1c0c`
- tag publié : `checkpoint-2026-09-29-0131-CEST`

### external tracker
- issue #11 : https://github.com/alexandra-guiderdoni/slides-miweb/issues/11
- issue #12 : https://github.com/alexandra-guiderdoni/slides-miweb/issues/12
- les deux issues sont ouvertes, sans commentaire, et portent `ready-for-agent`

### public URLs verified
- https://alexandra-guiderdoni.github.io/slides-miweb/
- https://alexandra-guiderdoni.github.io/slides-miweb/internationalisation-opquast-v5-v2/

### created by this closure
- `/Users/alex/Claude/projets-heberges/slides-miweb/.claude/session-context.md` - contexte de reprise vérifié puis commité séparément

## ERRORS FIXED
1. **Attribution trop étroite du rendu de `message`** - Mauvais : présenter Navigation V2 et Contenus V2 comme les seuls précédents. Correct : le modèle `miweb-objectifs-2030-v4/build.py` et quinze autres générateurs rendent déjà ce champ. Cause : première comparaison limitée aux dernières séries.
2. **Provenance incompatible avec le test d'autonomie** - Mauvais : ajouter `matrice-slide-ai` dans `variant.json` sans traiter `assert_generated_files_are_autonomous`. Correct : tolérance limitée au seul objet `generator_provenance`, sans référence d'exécution.
3. **Migration ambiguë des contenus publiés** - Mauvais : laisser entendre que des `slides.json` publiés pourraient être migrés pour dédupliquer le message. Correct : migrer uniquement `slides.example.json` et appliquer la règle aux futures variantes.
4. **Fausse garantie du reçu Opquast** - Mauvais : laisser croire qu'un reçu déclaratif prouve le jugement métier. Correct : il prouve seulement qu'une revue a été déclarée sur les empreintes concernées ; le fond reste humain ou agentique.
5. **Tag demandé alors que l'arbre était sale** - Mauvais : taguer l'ancien `HEAD`, ce qui n'aurait pas capturé Internationalisation V2. Correct : committer l'état validé, créer le tag sur `182dde4`, puis pousser le commit et le tag.
6. **Accès GitHub bloqué dans le bac à sable** - Mauvais : considérer l'échec réseau comme un échec GitHub. Correct : relancer les mises à jour explicitement autorisées avec l'accès réseau requis, puis relire chaque ticket.

## NEXT
1. Reprendre depuis `main` au commit de clôture indiqué dans `INVARIANTS` et vérifier `git status --short --branch`.
2. Ouvrir l'issue #11 et implémenter d'abord le correctif générique par une nouvelle branche seulement si le workflow futur l'exige ; ne modifier aucune variante publiée.
3. Exécuter les tests de matrice et les tests autonomes de variante prévus par l'issue #11.
4. Ouvrir l'issue #12, créer le schéma `source/revue-opquast.json`, le contrôle déterministe et le verrou dans `publish_variant.py`.
5. Conserver les issues #3 à #10 en attente tant que leur correction n'est pas explicitement priorisée.
6. Après toute publication future, vérifier automatiquement l'accueil local, le ZIP, l'URL publique et l'état Git local et distant.
