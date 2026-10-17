# Audit sourcé des notes orales Opquast - 17 octobre 2026

## Statut

- Périmètre : les 35 champs `notes_orateur` de `performance-opquast-v5/slides.json`.
- Verdict final : `PRETE_POUR_PRESENTATION`.
- Fond métier : contrôlé avec le skill Opquast, l’assistant Opquast et l’API `qualite-numerique`.
- Numéros et libellés : les 20 règles citées sont confirmées.
- Rubrique « Serveur et performances » : couverture exhaustive des 13 règles, de 218 à 230.
- Correction : les 35 notes ont été resserrées, restructurées et attribuées à la bonne source.
- Limite : ce verdict porte sur les notes et les contrôles du jeu ; il ne remplace pas une répétition chronométrée devant le public cible.

## Hiérarchie des sources appliquée

1. L’API Opquast valide les numéros, libellés, objectifs, explications, solutions et limites des règles.
2. Le livre et le guide Opquast valident les notions transversales, notamment VPTCS.
3. La transcription décrit ce qui est réellement affiché.
4. Le storyboard fixe le rôle narratif de chaque slide.
5. Les notes existantes fournissent la matière éditoriale à contrôler.
6. Le corpus d’articles et de newsletters apporte seulement un éclairage éditorial daté. Il ne remplace jamais la règle officielle.

## Outils et sources effectivement contrôlés

### Plugin Assistant Opquast

- Plugin : `gpt-3ee8327fe63c4a275fa1d7d65b405ee6`.
- Nom affiché : Assistant Opquast.
- Version lue : `0.8.2`.
- Release lue : `pluginrel_6ad341055a788191a4e2bf5f8b71abb3`.
- Instructions appliquées : vérifier les règles auprès de l’API, utiliser le livre pour les concepts et distinguer les articles ou newsletters des formulations officielles.
- Corpus présents :
  - `qualite-et-conformite-des-services-numeriques-llm.md` ;
  - `corpus-opquast-articles-newsletters.md` ;
  - glossaires Opquast ;
  - index de connaissances.

### Skill Opquast

- Skill : `opquast-skill`.
- Source lue : `/Users/alex/Claude/.claude/skills/opquast-skill/SKILL.md`.
- Usage : contrôle du référentiel V5, recherche dans le guide, le glossaire et les documents, distinction entre preuve API et source locale.
- Limite : ce skill n’est pas édité par la société Opquast, mais utilise ses contenus et recommandations.

### MCP et API Opquast

- Serveur MCP : `opquast`.
- Version du serveur : `1.2.0`.
- Version du référentiel demandée : `qualite-numerique`.
- API publique : disponible.
- API privée : disponible.
- Provenance reçue pour les règles : `source=api`.
- Règles récupérées individuellement avec détails : 119, 123, 124, 125, 126, 147, 148 et 218 à 230.
- Total de règles distinctes contrôlées : 20.

### Livre et guide Opquast

- Fiche lue : `VPTCS : structurer les exigences qualité`.
- Identifiant MCP : `concept-1-4`.
- Source reçue : `guide`.
- Édition : `2025-09`.
- Citation interne : `sources/guide.txt`, lignes 481 à 513.
- Point confirmé : VPTCS structure les attentes des utilisateurs en cinq dimensions. Le guide ne le présente pas comme une chronologie stricte du parcours.

### Articles et newsletters Opquast

- Article utilisé comme éclairage éditorial : `Performance Web : 1 Méga, c’est beaucoup`, notamment pour les distinctions des slides 1 à 3.
- Corpus disponible : `corpus-opquast-articles-newsletters.md`.
- Newsletter utilisée comme preuve de règle : aucune. Aucune newsletter n’était nécessaire pour valider les libellés ou objectifs, qui relèvent de l’API.
- Limite appliquée : un article ou une newsletter peut éclairer le discours, mais ne remplace jamais la formulation officielle reçue avec `source=api`.

### Sources du dépôt

- `docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md`.
- `performance-opquast-v5/source/storyboard.md`.
- `performance-opquast-v5/source/sources/metier/conversation-opquast-performance.md`.
- `performance-opquast-v5/source/sources/opquast/verification-regles-2026-10-12.md`.
- `performance-opquast-v5/slides.json`.

## Preuves automatiques

- `python3 scripts/check_notes_orales_opquast.py performance-opquast-v5` : 35 slides, 0 erreur, 0 avertissement.
- Aucun tiret cadratin détecté dans les notes.
- `python3 -m unittest discover -s scripts/tests` : 10 tests réussis.
- `scripts/validate_variant.sh performance-opquast-v5` : 12 tests réussis.
- `git diff --check` : aucune erreur d’espacement.
- Aucun tiret cadratin ou demi-cadratin détecté dans les notes.
- Toutes les notes comptent entre 84 et 110 mots, soit environ 34 à 44 secondes à 150 mots par minute.
- Le contrôle automatique ne prouve pas à lui seul l’exactitude sémantique ; celle-ci a fait l’objet d’une relecture croisée et d’une vérification API règle par règle.

## Couverture de la rubrique « Serveur et performances »

La relecture indépendante confirme une couverture de 13 règles sur 13, sans omission et sans surpromesse sur la compression, le cache ou la minification.

| Règle | Libellé officiel vérifié | Slide principale | Verdict |
|---:|---|---:|---|
| 218 | **L’adresse du site fonctionne avec et sans préfixe www.** | 26 | Conforme |
| 219 | **La racine du site contient des instructions pour les robots d’indexation.** | 27 | Conforme |
| 220 | **Le site propose un fichier sitemap indiquant les contenus à explorer.** | 27 | Conforme |
| 221 | **Le serveur ne force pas la redirection vers la version ou l’application mobile.** | 26 | Conforme |
| 222 | **Le serveur envoie un code HTTP 404 pour les ressources non trouvées.** | 28 | Conforme |
| 223 | **Le serveur envoie une page d’erreur 404 personnalisée.** | 29 | Conforme |
| 224 | **Le serveur envoie une page d’interdiction 403 personnalisée.** | 29 | Conforme |
| 225 | **Le menu principal de navigation figure sur les pages d’erreur personnalisées.** | 29 | Conforme |
| 226 | **Le serveur transmet des contenus compressés aux clients qui les acceptent.** | 11 | Conforme, sans promesse de performance globale |
| 227 | **Le serveur envoie les informations permettant la mise en cache des contenus.** | 13 | Conforme, sans promesse de réutilisation universelle |
| 228 | **Les entêtes envoyés par le serveur contiennent les informations relatives au jeu de caractères employé.** | 29 | Conforme |
| 229 | **Les feuilles de styles internes sont minifiées.** | 9 | Conforme, distinction avec la compression maintenue |
| 230 | **Les scripts internes sont minifiés.** | 10 | Conforme, sans promesse sur l’utilité ou le temps d’exécution |

## Constats initiaux corrigés

Les constats ci-dessous décrivent l’état antérieur à la correction. Ils sont tous résolus dans le jeu courant.

### Priorité haute

1. Slide 16 : le texte entre guillemets attribué à la règle 229 écrit « Les feuilles de style internes sont minifiées. ». L’API confirme « Les feuilles de styles internes sont minifiées. ». Une citation annoncée comme officielle doit être exacte.
2. Slides 1 et 35 : la formule « Performance Opquast = ne pas faire attendre, télécharger ou calculer inutilement » est une synthèse éditoriale de la série, pas une définition officielle du référentiel. Elle doit être présentée comme le fil conducteur de la série.
3. Slide 27 : `robots.txt` transmet des consignes aux robots compatibles. Il ne constitue ni un mécanisme de sécurité ni une interdiction contraignante.
4. Slide 31 : un audit Web Performance mesure des contextes testés. Il ne prouve pas une performance réelle absolue.
5. Slide 35 : les neuf règles ne garantissent pas collectivement une réduction de tous les traitements inutiles. Les règles 123, 147 et 148 informent surtout la décision.

### Priorité moyenne

- Réduire les répétitions des règles 119, 226, 227, 229 et 230 entre les slides 6 à 16, 24, 25, 31, 34 et 35.
- Réduire les répétitions des règles 123, 124, 147 et 148 entre les slides 18 à 23.
- Appliquer le gabarit canonique aux neuf slides dont le storyboard indique le rôle `règle` : 6, 9, 10, 11, 13, 19, 20, 21 et 22.
- Employer exactement les sections `Impact du non-respect` et `Ce que garantit la règle`.
- Distinguer systématiquement une conséquence garantie par la règle d’un bénéfice technique possible.
- Réduire la plupart des notes à environ 80 à 110 mots prononçables.

## Audit slide par slide

### Slides 1 à 5

- Slide 1 - À corriger : fond pertinent, mais la synthèse Performance Opquast doit être identifiée comme éditoriale. Remplacer le titre métapédagogique `Le fil directeur` par un titre de contenu.
- Slide 2 - Ajustement mineur : temps, données et terminal sont pertinents. Présenter les capacités de calcul comme un cadrage de la série, pas comme une règle Opquast.
- Slide 3 - Ajustement mineur : distinction rapide, léger, affiché et utilisable pertinente. Ajouter une transition vers les cinq situations.
- Slide 4 - À corriger : les cinq situations sont cohérentes et déclarées non officielles. Supprimer la métapédagogie et raccourcir.
- Slide 5 - À corriger : articulation ressource, fichier, transport et cache pertinente. Remplacer la promesse absolue du cache par « éviter certains retransferts inutiles ».

### Slides 6 à 12

- Slide 6 - À corriger : règle 119 exacte. Remplacer `Garantie pour l’utilisateur` par `Ce que garantit la règle`.
- Slide 7 - À corriger : exemple exact et seuils correctement présentés comme pédagogiques. Retirer ou sourcer le travail supplémentaire du terminal, puis raccourcir.
- Slide 8 - À corriger : la minification réduit la version servie au navigateur, pas nécessairement le fichier source de travail. Mettre **règles 229 et 230** en gras.
- Slide 9 - À corriger : règle 229 exacte. Appliquer le gabarit de règle et réduire fortement la durée.
- Slide 10 - À corriger : règle 230 exacte. Appliquer le gabarit, raccourcir et remplacer « toutes les fonctions » par « certaines interactions » ou « le service ».
- Slide 11 - À corriger : règle 226 exacte. Appliquer le gabarit, raccourcir et employer la formulation API « impact énergétique lié à la consultation ».
- Slide 12 - À corriger : synthèse exacte. Préciser que le cache permet la réutilisation ou une revalidation sans corps, sans garantir l’absence de tout échange.

### Slides 13 à 18

- Slide 13 - À corriger : règle 227 exacte. Appliquer le gabarit et remplacer « chaîne complète » par « leviers complémentaires ».
- Slide 14 - À corriger : distinctions exactes, mais très répétitives. La règle 119 vise précisément les vignettes et aperçus. Les quatre gestes ne forment pas nécessairement une suite appliquée au même fichier.
- Slide 15 - Globalement pertinente : contexte réseau et terminal cohérent. Raccourcissement léger recommandé.
- Slide 16 - À corriger en priorité : citation 229 inexacte, forte répétition, durée excessive et transition vers la slide 17 absente.
- Slide 17 - À préciser : éclairage WebPerf pertinent. Indiquer qu’il ne s’agit pas d’une règle Opquast et mettre en valeur les trois états visible, traitements en cours et utilisable.
- Slide 18 - À corriger : les quatre règles sont exactes. Leur regroupement n’est pas une catégorie officielle. Remplacer l’affirmation absolue sur le coût évité et supprimer la priorité non sourcée donnée à la taille.

### Slides 19 à 24

- Slide 19 - À restructurer : règle 148 exacte, préjudice et limite pertinents. Appliquer le gabarit canonique.
- Slide 20 - À restructurer : règle 147 exacte. Appliquer le gabarit et retirer une répétition.
- Slide 21 - À restructurer : règle 123 exacte. Appliquer le gabarit sans modifier le fond.
- Slide 22 - À restructurer : règle 124 exacte. Appliquer le gabarit et conserver les limites sur le poids et l’accessibilité complète.
- Slide 23 - À corriger : synthèse exacte mais trop répétitive. Garder les quatre questions sans réciter les quatre libellés complets. Employer « contribuent à éviter » plutôt que « préviennent ».
- Slide 24 - À corriger : le compte de 13 règles et l’intersection de quatre règles sont exacts. Remplacer « règle 119 présentée ensuite » par « règle 119 reprise ensuite ».

### Slides 25 à 30

- Slide 25 - À resserrer : règle 119 et rubrique exactes. La slide répète plusieurs développements antérieurs et manque de transition vers les règles serveur.
- Slide 26 - À resserrer : règles 218 et 221 exactes. Réduire la durée et conclure vers les fichiers destinés aux robots.
- Slide 27 - À corriger : règles 219 et 220 exactes. Présenter `robots.txt` comme une consigne non contraignante. Retirer ou sourcer l’exemple des pages peu reliées ou récemment ajoutées.
- Slide 28 - À resserrer : règle 222, code 404 et faux succès 200 exacts. Distinguer plus directement le préjudice et le signal garanti.
- Slide 29 - À corriger légèrement : règles 223, 224, 225 et 228 exactes. Dire que la page aide l’utilisateur à écarter un problème lié à sa propre connexion et confirme la continuité du serveur.
- Slide 30 - À corriger : règles 125 et 126 exactes. Préciser que leur position « en périphérie » est propre à cette présentation, retirer ou sourcer l’exemple précis du lecteur d’écran et réduire fortement la durée.

### Slides 31 à 35

- Slide 31 - À corriger en priorité : cinq règles exactes mais récitées une nouvelle fois. Nuancer le cache selon la validité de la ressource et les directives. Parler de contextes testés pour l’audit Web Performance. Réduire environ de moitié.
- Slide 32 - Ajustement mineur : relations entre performance, accessibilité contextuelle, écoconception, SEO et coûts présentées comme contributions, pas comme équivalences. Raccourcir et renforcer quelques mots importants.
- Slide 33 - À préciser : VPTCS est correctement présenté comme une lecture non officielle des effets de la performance. Le livre le définit comme un modèle de structuration des attentes, pas comme une chronologie stricte du parcours. Remplacer « suit le parcours » par une formulation moins séquentielle.
- Slide 34 - À corriger en priorité : six distinctions pertinentes mais note beaucoup trop longue. Dire que la compression réduit le volume lorsque le contenu est compressible et que le client l’accepte. Ajouter une transition vers les trois gestes finaux.
- Slide 35 - À corriger : bonne structure de synthèse. Présenter la formule finale comme le fil conducteur de la série. Remplacer la garantie sur les traitements par une formulation bornée aux données, à l’attente et à la maîtrise de la décision.

## Verdict de préparation

La présentation est prête selon le contrat éditorial du dépôt :

- les 20 règles citées existent, leurs numéros et libellés sont exacts ;
- les synthèses éditoriales sont annoncées comme telles ;
- la portée de `robots.txt`, du cache et de l’audit Web Performance est bornée ;
- les neuf slides de règle suivent les sections attendues ;
- les répétitions ont été réduites et toutes les notes tiennent dans la cible de 30 à 45 secondes ;
- les règles 218 à 230 sont toutes couvertes et attribuées précisément ;
- toutes les mentions de règles présentes dans les notes sont en gras.

## Limites de cet audit

- Aucun essai oral chronométré par une personne.
- Aucune validation pédagogique devant le public cible.
- Aucun commit, push ou déploiement déclenché par cette passe corrective.
