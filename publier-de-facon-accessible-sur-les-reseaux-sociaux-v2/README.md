# publier-de-facon-accessible-sur-les-reseaux-sociaux-v2

Site statique GitHub Pages pour les slides accessibles « Réseaux sociaux accessibles - V2 ».

## Accès directs

- [Présentation plein écran](./?projection=1#slide-01)
- [Toutes les slides](./?slides=all#diaporama)

## Génération

Depuis ce répertoire :

```bash
python3 build.py
```

Le script lit `slides.json` et génère `index.html`, `alternatives.html`, `accessibilite.html`, `alternatives.md` et `assets/downloads/publier-de-facon-accessible-sur-les-reseaux-sociaux-v2-slides.zip`.

## Sources du jeu de slides

- `source/contact-sheet-v8.png` : source conservée pour traçabilité.
- `source/imagegen-prompts-v8-prompt-image-refined.txt` : source conservée pour traçabilité.
- `source/imagegen-receipt-v8.tsv` : source conservée pour traçabilité.
- `source/source-emojis-accessibles.md` : source conservée pour traçabilité.
- `source/source.md` : source éditoriale utilisée pour produire les slides.
- `source/storyboard-v2.md` : source conservée pour traçabilité.
- `source/storyboard.md` : storyboard utilisé pour générer la variante.
- `slides.json` : titres, alternatives textuelles, descriptions et messages associés aux images publiées.

## Vérifications attendues

- les images listées dans `slides.json` sont présentes dans `assets/slides/` ;
- aucun lien `href="#"` n’est généré ;
- la page principale reste lisible sans JavaScript ;
- les alternatives textuelles sont aussi disponibles dans `alternatives.html` et `alternatives.md`.
