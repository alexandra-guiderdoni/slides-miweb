# Slide 07 - Accéder directement aux grandes zones

## Références visuelles à joindre

- Image 1, référence de style uniquement : `/Users/alex/Claude/projets-actifs/opquast/Formations-MIWEB/Internationalisation/contact-sheet-internationalisation.png`
- Image 2, référence de style uniquement : `/Users/alex/Claude/projets-actifs/opquast/Formations-MIWEB/newsletter/newsletter-opquast-v5-imagegen-complete/images/jpg/slide-17-neuf-regles-en-trois-temps.jpg`

Ne reprendre aucun texte, logo, numéro, contenu métier ou composition précise de ces références. Elles servent uniquement à retrouver la sobriété, la hiérarchie typographique, les cartes pastel et le style éditorial vectoriel des séries Internationalisation et Newsletter.

## Prompt d'édition utilisé pour produire la V2

Image source : `navigation-opquast-v5-essentielle/assets/slides/slide-07.png`, copiée dans la variante avant édition.

```text
Use case: precise-object-edit.
Asset type: final French presentation slide, 1672 x 941 pixels.
Edit target: the supplied slide 07 image.

Primary request: replace only the existing visible sentence "GARANTIE - Menu, contenu et recherche sont atteints directement" with the exact sentence "GARANTIE - Les zones utiles sont atteintes directement".

Text accuracy is mandatory. Render the replacement exactly once, with this exact spelling, capitalization, accents and simple hyphen:
"GARANTIE - Les zones utiles sont atteintes directement"

Constraints:
- Change only that one guarantee sentence.
- Preserve the complete original composition, illustration, colors, typography, spacing, icons, cards, footer and pagination as closely as possible.
- Preserve every other visible string exactly as it appears in the input image.
- Keep the canvas exactly 1672 x 941 pixels.
- Do not add, remove, repeat or rewrite any other text.
- No logo, watermark, pseudo-text or new visual element.
- Output one complete final slide only.
```

## Prompt ImageGen

```text
Use case: infographic-diagram.
Asset type: final French presentation slide, ready to publish as one raster image.

Generate ONE complete landscape slide only. The final canvas must be exactly 1672 x 941 pixels, 16:9. Render every required text directly in the image with ImageGen. This is the final slide: no later composition, no text overlay, no empty placeholder and no post-processing.

Use the supplied Internationalisation and Newsletter images only as style references. Create a calm institutional educational slide with a luminous white background, deep navy typography, rounded pastel cards, crisp flat vector illustration, generous whitespace and restrained shadows. Use pale blue for structure, warm pale red for impact and pale green for guarantee. Keep the visual language simple, editorial and immediately readable on projection.

Composition:
- Top-left: the small common header in plain text.
- Near the title: a compact pale-blue block marker and a distinct blue rule badge.
- Large left-aligned navy title with the rule caption directly below it.
- Main illustration: a simplified web page with a repeated header and navigation zone. At the very first keyboard stop, show a clearly visible access link as a highlighted control. From that control, three clean colored paths lead directly to three large abstract page zones representing menu, main content and search.
- Represent all interface content with blank geometric shapes only. The three target zones must be distinguishable by position, color and pictograms without any invented labels.
- Below the illustration: one pale red rounded impact band and one pale green rounded guarantee band.
- Above the footer: one centered pale-blue memo band.
- Bottom-left: small plain footer text. Bottom-right: exact pagination.
- Keep the top-right airy, with at most a very pale abstract corner shape and no emblem.

Typography:
- Modern highly legible sans serif, similar to Marianne or Arial.
- Title very large and bold in deep navy.
- Rule badge compact and clearly separated from the title.
- Rule caption, impact, guarantee and memo large enough for projection.
- No decorative font, no italics and no tiny explanatory copy.

Render ONLY the following visible strings, each exactly once, preserving accents, capitalization, punctuation, straight apostrophes and simple hyphens exactly as written:
1. "QUALITÉ NUMÉRIQUE - OPQUAST V5"
2. "B - ACCÉDER"
3. "Accéder directement aux grandes zones"
4. "RÈGLE 164"
5. "Liens d'accès rapide au début du code source"
6. "IMPACT - Les mêmes blocs sont reparcourus à chaque page"
7. "GARANTIE - Les zones utiles sont atteintes directement"
8. "Éviter le répétitif."
9. "Opquast - présentation Miweb"
10. "07 / 17"

No other visible letters, words, numbers, pseudo-text, interface labels, annotations or typographic marks. All browser mockups and page zones must use shapes only.

Constraints:
- One slide only, never a contact sheet, collage, deck preview or slide shown inside another screen.
- Show a direct skip from the beginning of the page to the main zones. Do not turn the visual into a generic map of landmarks.
- Do not invent keyboard keys, code, anchors, URLs or interface labels.
- Do not add any logo, fake logo, watermark, signature, seal or brand emblem.
- The words "Opquast - présentation Miweb" must remain plain footer text, never a logo.
- No photography, no 3D render and no corporate stock characters.
- No rule number other than 164.
- Keep every text block fully inside safe margins and never crop or repeat text.
- Prioritize exact French text and immediate comprehension over decorative detail.
```

## Contrôle avant acceptation

- Vérifier l'image en résolution originale 1672 x 941.
- Comparer caractère par caractère les dix chaînes de la liste blanche.
- Vérifier que le lien d'accès rapide apparaît au début du parcours et mène directement aux trois grandes zones.
- Rejeter toute image comportant un logo, un texte d'interface inventé, du code ou un numéro supplémentaire.
