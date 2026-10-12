# Performance selon Opquast V5

Site statique GitHub Pages pour les slides accessibles « Performance selon Opquast V5 ».

## Accès directs

- [Présentation plein écran](./?projection=1#slide-01)
- [Toutes les slides](./?slides=all#diaporama)

## Parcours essentiel de 60 minutes

Le parcours essentiel suit les slides 01 à 06, 08 à 25, 28, 29, 31 et 32, dans cet ordre. Les slides 07, 26 et 30 constituent des approfondissements ; la slide 27 constitue une annexe.

## Génération

Depuis ce répertoire :

```bash
python3 build.py
```

Le script lit `slides.json` et génère `index.html`, `alternatives.html`, `accessibilite.html`, `alternatives.md` et `assets/downloads/performance-opquast-v5-slides.zip`. Chaque slide dispose d’une transcription descriptive et d’un discours oral distincts.

## Sources du jeu de slides

- `source/brief.md` : source conservée pour traçabilité.
- `source/run.json` : source conservée pour traçabilité.
- `source/storyboard.md` : storyboard utilisé pour générer la variante.
- source/sources/ : source métier obligatoire, matrice de couverture et vérifications Opquast.
- source/prompts/, source/qa/ et source/reports/ : prompts, décisions et rapports de production.
- `slides.json` : titres, alternatives textuelles, transcriptions descriptives, discours oraux et références associés aux images publiées.

## Vérifications attendues

- les images listées dans `slides.json` sont présentes dans `assets/slides/` ;
- aucun lien `href="#"` n’est généré ;
- la page principale reste lisible sans JavaScript ;
- les alternatives textuelles, transcriptions et discours oraux sont aussi disponibles dans `alternatives.html` et `alternatives.md`.
