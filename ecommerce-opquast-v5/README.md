# ecommerce-opquast-v5

Site statique GitHub Pages pour les slides accessibles « E-commerce selon Opquast V5 ».

## Accès directs

- [Présentation plein écran](./?projection=1#slide-01)
- [Toutes les slides](./?slides=all#diaporama)

## Génération

Depuis ce répertoire :

```bash
python3 build.py
```

Le script lit `slides.json` et génère `index.html`, `alternatives.html`, `accessibilite.html`, `alternatives.md` et les archives suivantes : `assets/downloads/ecommerce-opquast-v5-slides.zip` (slides 1 à 66); `assets/downloads/ecommerce-opquast-v5-slides-partie-2.zip` (slides 67 à 132). Chaque archive contient aussi `alternatives.md` et reste sous 100 Mio pour GitHub Pages. Le découpage éventuel est défini dans `variant.json`. Chaque slide dispose d’une alternative courte, d’une description détaillée du visuel, d’une transcription descriptive et d’un discours oral distincts. La présentation affiche deux accordéons : description détaillée, complétée par les textes affichés dans l’image, et discours oral ; la transcription descriptive reste aussi disponible dans les alternatives.

## Usage du diagnostic et des corrections

Ce support public contient toutes les questions, les corrections et les notes. Le diagnostic T0 sert d’amorçage ; si le support a été consulté avant la passation, une différence entre T0 et T1 ne mesure pas à elle seule un apprentissage. Les liens, les accordéons et les alternatives ne constituent pas un contrôle d’accès aux réponses. Une évaluation indépendante demande un dispositif séparé, dont les réponses ne sont pas préalablement diffusées.

## Sources du jeu de slides

- `source/storyboard.md` : storyboard utilisé pour générer la variante.
- `slides.json` : titres, alternatives textuelles, descriptions détaillées, transcriptions descriptives, discours oraux et références associés aux images publiées.

## Vérifications attendues

- les images listées dans `slides.json` sont présentes dans `assets/slides/` ;
- aucun lien `href="#"` n’est généré ;
- la page principale reste lisible sans JavaScript ;
- les alternatives textuelles, descriptions détaillées, transcriptions et discours oraux sont aussi disponibles dans `alternatives.html` et `alternatives.md`.
