# presentation-opquast-v5

Site statique GitHub Pages pour les slides accessibles « Présentation selon Opquast V5 ».

## Accès directs

- [Présentation plein écran](./?projection=1#slide-01)
- [Toutes les slides](./?slides=all#diaporama)

## Génération

Depuis ce répertoire :

```bash
python3 build.py
```

Le script lit `slides.json` et génère `index.html`, `alternatives.html`, `accessibilite.html`, `alternatives.md` et les archives suivantes : `assets/downloads/presentation-opquast-v5-slides.zip`. Chaque archive contient aussi `alternatives.md` et reste sous 100 Mio pour GitHub Pages. Le découpage éventuel est défini dans `variant.json`. Chaque slide dispose d’une alternative courte, d’une description détaillée du visuel, d’une transcription descriptive et d’un discours oral distincts. La présentation affiche deux accordéons : description détaillée, complétée par les textes affichés dans l’image, et discours oral ; la transcription descriptive reste aussi disponible dans les alternatives.

## Sources du jeu de slides

- `source/planche-serie.png` : source conservée pour traçabilité.
- `source/storyboard.md` : storyboard utilisé pour générer la variante.
- `source/prompts/` : prompts de génération des images, un par slide (40 fichiers).
- `slides.json` : titres, alternatives textuelles, descriptions détaillées, transcriptions descriptives, discours oraux et références associés aux images publiées.

## Vérifications attendues

- les images listées dans `slides.json` sont présentes dans `assets/slides/` ;
- aucun lien `href="#"` n’est généré ;
- la page principale reste lisible sans JavaScript ;
- les alternatives textuelles, descriptions détaillées, transcriptions et discours oraux sont aussi disponibles dans `alternatives.html` et `alternatives.md`.
