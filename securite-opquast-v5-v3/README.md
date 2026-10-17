# securite-opquast-v5-v3

Site statique GitHub Pages pour les slides accessibles « Sécurité selon Opquast V5 - version 3 ».

## Accès directs

- [Présentation plein écran](./?projection=1#slide-01)
- [Toutes les slides](./?slides=all#diaporama)

## Génération

Depuis ce répertoire :

```bash
python3 build.py
```

Le script lit `slides.json` et génère `index.html`, `alternatives.html`, `accessibilite.html`, `alternatives.md` et `assets/downloads/securite-opquast-v5-v3-slides.zip`. Chaque slide dispose d’une alternative courte, d’une description détaillée du visuel, d’une transcription descriptive et d’un discours oral distincts. La présentation affiche deux accordéons : description détaillée et discours oral ; la transcription reste disponible dans les alternatives.

## Sources du jeu de slides

- `source/notes-etalons.md` : source conservée pour traçabilité.
- `source/storyboard.md` : storyboard utilisé pour générer la variante.
- `slides.json` : titres, alternatives textuelles, descriptions détaillées, transcriptions descriptives, discours oraux et références associés aux images publiées.

## Vérifications attendues

- les images listées dans `slides.json` sont présentes dans `assets/slides/` ;
- aucun lien `href="#"` n’est généré ;
- la page principale reste lisible sans JavaScript ;
- les alternatives textuelles, descriptions détaillées, transcriptions et discours oraux sont aussi disponibles dans `alternatives.html` et `alternatives.md`.
