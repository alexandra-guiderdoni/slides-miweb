# Slide 10 - Voir où se trouve le focus

## Références visuelles à joindre

- Image 1, référence de style uniquement : `/Users/alex/Claude/projets-actifs/opquast/Formations-MIWEB/Internationalisation/contact-sheet-internationalisation.png`
- Image 2, référence de style uniquement : `/Users/alex/Claude/projets-actifs/opquast/Formations-MIWEB/newsletter/newsletter-opquast-v5-imagegen-complete/images/jpg/slide-17-neuf-regles-en-trois-temps.jpg`

Ne reprendre aucun texte, logo, numéro, contenu métier ou composition précise de ces références. Elles servent uniquement à retrouver la sobriété, la hiérarchie typographique, les cartes pastel et le style éditorial vectoriel des séries Internationalisation et Newsletter.

## Prompt ImageGen

```text
Use case: comparison-infographic.
Asset type: final French presentation slide, ready to publish as one raster image.

Generate ONE complete landscape slide only. The final canvas must be exactly 1672 x 941 pixels, 16:9. Render every required text directly in the image with ImageGen. This is the final slide: no later composition, no text overlay, no empty placeholder and no post-processing.

Use the supplied Internationalisation and Newsletter images only as style references. Create a calm institutional educational slide with a luminous white background, deep navy typography, rounded pastel cards, crisp flat vector illustration, generous whitespace and restrained shadows. Use muted grey and pale red for loss of position, vivid blue and green for visible focus, pale red for impact and pale green for guarantee.

Composition:
- Top-left: the small common header in plain text.
- Near the title: a compact pale-blue block marker and a distinct blue rule badge.
- Large left-aligned navy title.
- Main body: a wide simplified interface card with several abstract interactive controls arranged clearly.
- Show one current control with a thick, highly perceptible double focus ring and a soft outer halo. The neighboring controls remain neutral, making the active position unmistakable.
- Add a small flat vector person using a keyboard, visually connected to the focused control. Do not show the mouse as the required means of interaction.
- A subtle faded trail behind the current control may suggest previous focus positions, but the current focused element must remain dominant.
- Below the illustration: one pale red rounded impact band and one pale green rounded guarantee band.
- Above the footer: one centered pale-blue memo band.
- Bottom-left: small plain footer text. Bottom-right: exact pagination.
- Keep the top-right airy, with at most a very pale abstract corner shape and no emblem.

Typography:
- Modern highly legible sans serif, similar to Marianne or Arial.
- Title very large and bold in deep navy.
- Impact, guarantee and memo large enough for projection.
- No decorative font, no italics and no tiny explanatory copy.

Render ONLY the following visible strings, each exactly once, preserving accents, capitalization, punctuation, straight apostrophes and simple hyphens exactly as written:
1. "QUALITÉ NUMÉRIQUE - OPQUAST V5"
2. "D - AGIR SANS SOURIS"
3. "Voir où se trouve le focus"
4. "RÈGLE 165"
5. "IMPACT - Sans repère visuel, la navigation avance à l'aveugle"
6. "GARANTIE - L'élément actif reste perceptible"
7. "Le focus est le pointeur du clavier."
8. "Opquast - présentation Miweb"
9. "10 / 17"

No other visible letters, words, numbers, pseudo-text, interface labels, annotations or typographic marks. Interface controls and keyboard keys must remain unlabeled abstract shapes.

Constraints:
- One slide only, never a contact sheet, collage, deck preview or slide shown inside another screen.
- The visible focus indicator must be the central visual evidence, not a decorative glow on the whole interface.
- Do not show or state a numerical contrast threshold.
- Do not depict the mouse as the necessary interaction method.
- Do not invent button labels, keyboard key names, CSS code or accessibility annotations.
- Do not add any logo, fake logo, watermark, signature, seal or brand emblem.
- The words "Opquast - présentation Miweb" must remain plain footer text, never a logo.
- No photography, no 3D render and no corporate stock characters.
- No rule number other than 165.
- Keep every text block fully inside safe margins and never crop or repeat text.
- Prioritize exact French text and immediate comprehension over decorative detail.
```

## Contrôle avant acceptation

- Vérifier l'image en résolution originale 1672 x 941.
- Comparer caractère par caractère les neuf chaînes de la liste blanche.
- Vérifier qu'un seul élément actif possède un indicateur de focus net et immédiatement perceptible.
- Rejeter toute image comportant un seuil chiffré, un logo, un libellé d'interface ou un numéro supplémentaire.
