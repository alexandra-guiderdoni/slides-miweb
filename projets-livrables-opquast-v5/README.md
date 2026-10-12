# Projets et livrables selon Opquast V5

Site statique GitHub Pages pour les slides accessibles « Projets et livrables selon Opquast V5 ».

## Accès directs

- [Présentation plein écran](./?projection=1#slide-01)
- [Toutes les slides](./?slides=all#diaporama)

## Parcours essentiel de 60 minutes

Le parcours essentiel suit les slides 01 à 23, dans cet ordre. Les slides 24 à 45 forment l’atlas exhaustif des 12 familles et des 59 livrables ou objets de projet.

## Génération

Depuis ce répertoire :

```bash
python3 build.py
```

Le script lit `slides.json` et génère `index.html`, `alternatives.html`, `accessibilite.html`, `alternatives.md` et `assets/downloads/projets-livrables-opquast-v5-slides.zip`. Chaque slide dispose d’une alternative courte, d’une description détaillée du visuel, d’une transcription descriptive et d’un discours oral distincts.

## Sources du jeu de slides

- `source/opquast_projets_livrables_V010_objectif_19.md` : source conservée pour traçabilité.
- `source/storyboard.md` : storyboard utilisé pour générer la variante.
- source/metier/ : les deux sources métier obligatoires.
- source/run/ : matrice de couverture, prompts, décisions, rapports et manifeste de production.
- `slides.json` : titres, alternatives textuelles, descriptions détaillées, transcriptions descriptives, discours oraux et références associés aux images publiées.

## Vérifications attendues

- les 45 images listées dans `slides.json` sont présentes dans `assets/slides/` ;
- aucun lien `href="#"` n’est généré ;
- la page principale reste lisible sans JavaScript ;
- les alternatives textuelles, descriptions détaillées, transcriptions et discours oraux sont aussi disponibles dans `alternatives.html` et `alternatives.md`.
