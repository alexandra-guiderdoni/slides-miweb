# newsletter-opquast-v5

Site statique GitHub Pages pour les slides accessibles « Newsletter et qualité numérique selon Opquast V5 ».

## Accès directs

- [Présentation plein écran](./?projection=1#slide-01)
- [Toutes les slides](./?slides=all#diaporama)

## Génération

Depuis ce répertoire :

```bash
python3 build.py
```

Le script lit `slides.json` et génère `index.html`, `alternatives.html`, `accessibilite.html`, `alternatives.md` et `assets/downloads/newsletter-opquast-v5-slides.zip`.

## Sources du support

- `source/edition.md` : repères éditoriaux, limites et justification des fichiers publiés.
- `source/provenance.json` : correspondances des 18 images et empreintes SHA-256 des JPEG.
- `source/storyboard.md` : storyboard ayant guidé les 18 visuels finaux.
- `slides.json` : titres, alternatives courtes, transcriptions structurées, relevés des textes visibles et discours oral.

## Vérifications attendues

- les images listées dans `slides.json` sont présentes dans `assets/slides/` ;
- aucun lien `href="#"` n’est généré ;
- la page principale reste lisible sans JavaScript ;
- les alternatives textuelles sont aussi disponibles dans `alternatives.html` et `alternatives.md`.
