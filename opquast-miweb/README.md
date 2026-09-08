# opquast-miweb

Site statique GitHub Pages pour les slides accessibles « Opquast — la qualité web qui se vérifie ».

## Accès directs

- [Présentation plein écran](./?projection=1#slide-01)
- [Toutes les slides](./?slides=all#diaporama)

## Génération

Depuis ce répertoire :

```bash
python3 build.py
```

Le script lit `slides.json` et génère `index.html`, `alternatives.html`, `accessibilite.html`, `alternatives.md` et `assets/downloads/opquast-miweb-slides.zip`.

## Sources de la présentation Opquast

- `source/.DS_Store` : source conservée pour traçabilité.
- `source/edition.md` : source conservée pour traçabilité.
- `source/provenance.json` : correspondances avec le PPTX et empreintes des images avant et après optimisation sans perte.
- `source/storyboard.md` : consignes conservées et notes originales du PPTX, dans l’ordre des 44 slides.
- `slides.json` : titres, alternatives textuelles, descriptions et messages associés aux images publiées.

## Vérifications attendues

- les images listées dans `slides.json` sont présentes dans `assets/slides/` ;
- aucun lien `href="#"` n’est généré ;
- la page principale reste lisible sans JavaScript ;
- les alternatives textuelles sont aussi disponibles dans `alternatives.html` et `alternatives.md`.
