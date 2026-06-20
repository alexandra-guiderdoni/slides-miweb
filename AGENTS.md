# AGENTS.md - miweb-objectifs-2030

## Règle centrale

Toujours répondre et documenter en français.

Ce dépôt publie des variantes web statiques des slides MiWeb « Objectifs 2030 - accessibilité numérique ». Le but n’est pas de créer un nouveau site éditorial, mais de rendre comparables des variantes visuelles en conservant la traçabilité des sources.

## Pourquoi

Chaque version doit permettre de répondre à quatre questions :

- quelle variante est publiée ;
- quelles images elle contient ;
- quelles alternatives textuelles décrivent ces images ;
- quel storyboard source a guidé la génération.

La V1, la V2, puis les futures V3/V4 doivent rester comparables. Une version publiée ne doit pas être réécrite pour devenir une autre variante.

## Principe Saint-Exupéry

Appliquer le principe de sobriété : enlever ce qui ne sert pas la lecture, l’accessibilité, la comparaison ou la publication.

Concrètement :

- pas de fonctionnalité ajoutée sans usage réel ;
- pas de nouveau framework ;
- pas de composant décoratif ;
- pas de page supplémentaire si le contenu tient dans le README, `slides.json` ou `DEMARCHE-VERSIONS.md` ;
- pas de duplication de texte long entre versions hors alternatives nécessaires.

## Structure à préserver

- `index.html` : accueil des versions publiées.
- `miweb-objectifs-2030-vN/` : une version autonome du diaporama.
- `miweb-objectifs-2030-vN/assets/slides/` : les 10 images publiées.
- `miweb-objectifs-2030-vN/source/` : storyboard et sources utiles de la variante.
- `miweb-objectifs-2030-vN/slides.json` : source canonique des titres, alternatives, descriptions et messages.
- `miweb-objectifs-2030-vN/build.py` : générateur de la version.
- `DEMARCHE-VERSIONS.md` : procédure de publication des variantes suivantes.

## Règles de variante

- Créer une nouvelle variante dans un nouveau dossier `miweb-objectifs-2030-vN`.
- Ne pas modifier les images ou alternatives d’une version déjà publiée pour fabriquer la suivante.
- Copier le storyboard source dans `source/`.
- Mettre à jour `slides.json` avant de générer les pages.
- Si `build.py` d’une ancienne version est lancé, relancer ensuite le build de la dernière version pour restaurer l’accueil racine.
- Ne pas publier d’image sans alternative textuelle.
- Ne pas inventer de chiffre, seuil, engagement, audit ou conformité absents de la note source.

## Vérifications attendues

Pour la version modifiée :

```bash
python3 -m unittest discover -s miweb-objectifs-2030-vN/tests
npx --yes html-validate miweb-objectifs-2030-vN/index.html miweb-objectifs-2030-vN/alternatives.html miweb-objectifs-2030-vN/accessibilite.html index.html
npx --yes vnu-jar --errors-only miweb-objectifs-2030-vN/index.html miweb-objectifs-2030-vN/alternatives.html miweb-objectifs-2030-vN/accessibilite.html index.html
```

Pour une modification commune :

```bash
python3 -m unittest discover -s miweb-objectifs-2030-v1/tests
python3 -m unittest discover -s miweb-objectifs-2030-v2/tests
```

Tester aussi en local :

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

## Publication

Avant push :

- vérifier `git status --short` ;
- ne pas ajouter `.DS_Store`, caches, `test-results/` ou artefacts locaux ignorés ;
- vérifier que l’accueil racine pointe bien vers la dernière version publiée ;
- vérifier que le ZIP de la dernière version existe dans `assets/downloads/`.

GitHub Pages publie depuis la branche du dépôt. Après push, vérifier l’URL publique de la version concernée.
