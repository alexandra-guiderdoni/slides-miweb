# AGENTS.md - miweb-objectifs-2030

## Règle centrale

Toujours répondre et documenter en français.

Dans les contenus éditoriaux et les notes orales, utiliser uniquement le tiret simple (`-`, dit tiret du 6) ; ne pas utiliser de tiret cadratin.

Ce dépôt publie des variantes web statiques des slides MiWeb « Objectifs 2030 - accessibilité numérique » et des supports thématiques produits avec le même modèle. Le but n’est pas de créer un nouveau site éditorial, mais de rendre comparables des jeux de slides visuels en conservant la traçabilité des sources.

## Pourquoi

Chaque version doit permettre de répondre à quatre questions :

- quelle variante est publiée ;
- quelles images elle contient ;
- quelles alternatives textuelles décrivent ces images ;
- quel storyboard source a guidé la génération.

Toutes les versions publiées doivent rester comparables. Une version publiée ne doit pas être réécrite pour devenir une autre variante.

## Principe Saint-Exupéry

Appliquer le principe de sobriété : enlever ce qui ne sert pas la lecture, l’accessibilité, la comparaison ou la publication.

Concrètement :

- pas de fonctionnalité ajoutée sans usage réel ;
- pas de nouveau framework ;
- pas de composant décoratif ;
- pas de page supplémentaire si le contenu tient dans le README, `slides.json`, `DEMARCHE-VERSIONS.md` ou `GUIDE-REGENERATION-SITES-SLIDES.md` ;
- pas de duplication de texte long entre versions hors alternatives nécessaires.

## Structure à préserver

- `index.html` : accueil des versions publiées.
- `miweb-objectifs-2030-vN/` : une version autonome du diaporama Objectifs 2030.
- `miweb-offre-mutualisee-listes-diffusion-2026-condensee/` : support thématique condensé.
- `miweb-offre-mutualisee-listes-diffusion-2026-longue/` : support thématique long.
- `span-pan/` : support thématique SPAN / PAN.
- `mise-en-gouvernance-du-span/` : support thématique sur la gouvernance du SPAN.
- `checklist-span-operationnel/` : support thématique checklist SPAN opérationnel et dernière version publiée.
- `<dossier-jeu>/assets/slides/` : les images publiées de la variante.
- `<dossier-jeu>/source/` : storyboard et sources utiles de la variante.
- `<dossier-jeu>/slides.json` : source canonique des titres, alternatives, descriptions et messages.
- `<dossier-jeu>/build.py` : générateur autonome de la variante ; il ne doit générer que le dossier du jeu.
- `matrice-slide-ai/` : matrice canonique pour créer et publier séparément les futurs jeux.
- `published-versions.json` : catalogue racine, créé au premier publish ou mis à jour par `publish_variant.py`.
- `DEMARCHE-VERSIONS.md` : procédure de publication des variantes suivantes.
- `GUIDE-REGENERATION-SITES-SLIDES.md` : mode opératoire complet pour créer, vérifier, prévisualiser et publier un jeu.
- `docs/prd/` : cadrages fonctionnels historiques.
- `docs/prompts/` : prompts de génération et de correction conservés pour référence.
- `docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md` : contrat canonique pour les futures séries Opquast.
- `docs/goals/` : objectifs de chantier historiques.
- `scripts/check_notes_orales_opquast.py` : contrôle structurel des notes orales Opquast avant génération.
- `scripts/validate_variant.sh` : vérification standard d’un jeu.
- `scripts/serve-local.sh` : serveur local standard.
- `scripts/push-pages.sh` : push non interactif vers GitHub Pages.

## Hiérarchie documentaire

Pour un agent ou un LLM qui reprend le dépôt :

- `AGENTS.md` fixe les règles de conduite et les interdits.
- `README.md` donne l’entrée courte et le chemin standard.
- `DEMARCHE-VERSIONS.md` détaille la procédure opérationnelle.
- `GUIDE-REGENERATION-SITES-SLIDES.md` sert de mode opératoire complet quand il faut inspecter, prévisualiser ou prouver.
- `docs/prd/`, `docs/prompts/` et `docs/goals/` sont des archives de cadrage ; ne pas les traiter comme procédure active si un document racine plus récent dit autre chose.

## Règles de variante

Le schéma canonique des slides porte une transcription descriptive et un discours oral, tous deux obligatoires et distincts. Chacun alimente son propre accordéon dans la présentation, dans la page HTML d’alternatives et dans son export Markdown. Les jeux publiés avant cette règle conservent leur générateur d’origine et ne sont pas repris.

Préserver le mode « toutes les slides » lors d’un retour ou d’une avance navigateur vers une URL ?slides=all. Pour la CSP des pages statiques, autoriser les scripts et styles intégrés par empreintes SHA-256 ; ne pas utiliser de nonce fixe.

- Créer une nouvelle variante ou un nouveau support dans un nouveau dossier autonome avec `matrice-slide-ai/create_variant.py`.
- Si les images source sont préfixées, utiliser `--slide-prefix <prefixe>` au lieu de les renommer manuellement.
- Ne pas modifier les images ou alternatives d’une version déjà publiée pour fabriquer la suivante.
- Copier le storyboard source dans `source/`.
- Mettre à jour `slides.json` avant de générer les pages.
- Refaire systématiquement une passe avec le skill `alt-text` sur les alternatives de `slides.json` avant `build.py` : les champs `alt` doivent remplacer l’information utile, rester courts, ne pas commencer par « image de » et ne pas inventer d’information absente du visuel ou du contexte.
- Optimiser les images avec `scripts/optimiser-images.sh <dossier-jeu>` avant `build.py`. Si les images changent ensuite, relancer `build.py` pour reconstruire le ZIP.
- Lancer `python3 <dossier-jeu>/build.py` pour générer seulement le jeu.
- Publier sur l’accueil racine uniquement avec `python3 matrice-slide-ai/publish_variant.py --slug <dossier-jeu>`.
- Ne pas modifier `PUBLISHED_VERSIONS`, `LATEST_VERSION_SLUG` ou `ROOT_CATALOG_BOOTSTRAP` dans un `build.py` de variante pour publier l’accueil.
- Ne pas écrire à la main `date_publication` ni `date_maj` dans `published-versions.json` : `publish_variant.py` les gère. La date de première publication d’un jeu ne se corrige à la main que si elle est fausse, et jamais pour rajeunir un jeu.
- Ne pas faire dépendre un jeu publié de `matrice-slide-ai/` à l’exécution.
- Ne pas publier d’image sans alternative textuelle.
- Ne pas inventer de chiffre, seuil, engagement, audit ou conformité absents de la note source.

## Séries de slides Opquast

Pour toute nouvelle série consacrée au référentiel Opquast, utiliser `docs/prompts/REVISION-NOTES-ORALES-OPQUAST.md` avant de rédiger l’ensemble des notes orales.

Ordre obligatoire :

- établir la hiérarchie des sources ;
- vérifier les numéros, libellés, objectifs, contrôles et limites auprès du skill ou du MCP Opquast ;
- produire quatre slides étalons : ouverture, règle, éclairage et synthèse ;
- obtenir la validation explicite de ces quatre slides avant toute rédaction massive ou délégation parallèle ;
- appliquer ensuite le même patron éditorial à toute la série ;
- organiser une relecture croisée : aucun agent ne valide seul sa propre production ;
- relire toutes les notes comme un seul discours avant génération ;
- lancer `python3 scripts/check_notes_orales_opquast.py <dossier-jeu>` avant `build.py`.

Contrat éditorial des notes orales Opquast :

- parole directement prononçable ;
- titres portant sur le contenu, sans métapédagogie ;
- aucune consigne au présentateur ni gestion du groupe ;
- pas de répétition de la transcription ;
- listes à puces privilégiées pour faciliter le scan ;
- sections `Impact du non-respect` et `Ce que garantit la règle` pour les slides de règles ;
- transition courte entre les slides, conclusion sur la dernière ;
- rapprochements RGAA limités aux points directement utiles ;
- aucune invention à partir de NotebookLM ou d’une autre source secondaire ;
- uniquement le tiret simple `-`.

Hiérarchie spécifique : le skill ou le MCP Opquast valide les règles, la transcription décrit l’écran, le storyboard organise la progression, les notes existantes fournissent la matière éditoriale et NotebookLM sert uniquement à challenger. En cas de contradiction non résolue, écrire `à vérifier` au lieu de compléter par inférence.

### Fabrique des séries Opquast essentielles

La série `navigation-opquast-v5-essentielle/` est la référence locale validée pour les futures séries Opquast essentielles. Reproduire son processus et sa grammaire visuelle sans recopier son contenu métier.

Invariants obligatoires :

- verrouiller la thématique et la liste exacte des règles auprès du skill ou du MCP Opquast avant de construire le storyboard ;
- organiser une série courte en blocs d’usage explicites et regrouper plusieurs règles seulement quand elles répondent au même problème utilisateur ;
- citer sur chaque slide les règles réellement concernées ;
- valider les quatre slides étalons avant toute génération massive ou délégation parallèle ;
- produire chaque slide comme une image raster complète avec ImageGen, texte compris, sans composition, surimpression ou ajout de texte après génération ;
- utiliser un canevas 16:9 de 1672 x 941 pixels pour cette famille de séries ;
- inscrire dans le storyboard une liste blanche exacte des textes visibles de chaque slide ;
- conserver dans `source/prompts/` le prompt complet, les références visuelles et les critères de rejet de chaque image ;
- contrôler chaque image en résolution originale, caractère par caractère, et rejeter tout texte parasite, faux logo, mauvais numéro ou écart de pagination ;
- conserver la distinction entre alternative courte, description, transcription, message et discours oral ;
- appliquer `alt-text`, la relecture croisée, les tests du jeu, la validation HTML et la recette navigateur avant publication ;
- traiter un jeu publié comme immuable : les annexes, extensions ou changements de structure deviennent une nouvelle variante autonome.

Le processus détaillé figure dans la section `Série Opquast essentielle générée avec ImageGen` de `GUIDE-REGENERATION-SITES-SLIDES.md`. Les fichiers `navigation-opquast-v5-essentielle/source/storyboard.md` et `navigation-opquast-v5-essentielle/source/prompts/` servent de précédents concrets.

## Vérifications attendues

Pour le jeu modifié :

```bash
scripts/validate_variant.sh <dossier-jeu>
```

Pour une série Opquast, lancer auparavant :

```bash
python3 scripts/check_notes_orales_opquast.py <dossier-jeu>
python3 -m unittest discover -s scripts/tests
```

Le script utilise les validateurs npm verrouillés à la racine. Si les dépendances ne sont pas installées, lancer `npm ci` depuis la racine du dépôt, puis relancer la validation.

Pour une modification commune :

```bash
python3 -m unittest discover -s matrice-slide-ai/tests
python3 -m unittest discover -s miweb-objectifs-2030-v1/tests
python3 -m unittest discover -s miweb-objectifs-2030-v2/tests
python3 -m unittest discover -s miweb-objectifs-2030-v3/tests
python3 -m unittest discover -s miweb-objectifs-2030-v4/tests
python3 -m unittest discover -s miweb-offre-mutualisee-listes-diffusion-2026-condensee/tests
python3 -m unittest discover -s miweb-offre-mutualisee-listes-diffusion-2026-longue/tests
python3 -m unittest discover -s span-pan/tests
python3 -m unittest discover -s mise-en-gouvernance-du-span/tests
python3 -m unittest discover -s checklist-span-operationnel/tests
```

Tester aussi en local :

```bash
scripts/serve-local.sh 8000
```

## Publication

Avant push :

- vérifier `git status --short` ;
- ne pas ajouter `.DS_Store`, caches, `test-results/` ou artefacts locaux ignorés ;
- vérifier le diff des fichiers racine, du catalogue et du dossier de jeu concerné ;
- vérifier que `published-versions.json` et `index.html` racine ne changent qu’après `publish_variant.py` ;
- vérifier que l’accueil racine pointe bien vers la dernière version publiée ;
- vérifier que le ZIP de la dernière version existe dans `assets/downloads/`.
- pousser avec `scripts/push-pages.sh` pour éviter un blocage silencieux sur une invite Git.

GitHub Pages publie depuis la branche du dépôt. Après push, vérifier l’URL publique de la version concernée.
