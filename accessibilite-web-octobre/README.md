# accessibilite-web-octobre

Site statique GitHub Pages pour les slides accessibles « Octobre, Web et accessibilité ».

## Accès directs

- [Présentation plein écran](./?projection=1#slide-01)
- [Toutes les slides](./?slides=all#diaporama)

## Génération

Depuis ce répertoire :

```bash
python3 build.py
```

Le script lit `slides.json` et génère `index.html`, `alternatives.html`, `accessibilite.html`, `alternatives.md` et `assets/downloads/accessibilite-web-octobre-slides.zip`. Chaque slide dispose d’une transcription descriptive et d’un discours oral distincts.

## Sources du jeu de slides

- `source/manifest-images.tsv` : source conservée pour traçabilité.
- `source/storyboard.md` : storyboard utilisé pour générer la variante.
- `source/w3c-accessibilite-web.md` : source conservée pour traçabilité.
- `slides.json` : titres, alternatives textuelles, transcriptions descriptives, discours oraux et références associés aux images publiées.

## Vérifications attendues

- les images listées dans `slides.json` sont présentes dans `assets/slides/` ;
- aucun lien `href="#"` n’est généré ;
- la page principale reste lisible sans JavaScript ;
- les alternatives textuelles, transcriptions et discours oraux sont aussi disponibles dans `alternatives.html` et `alternatives.md`.
