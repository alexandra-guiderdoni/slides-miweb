# Slide 03 - Entrer sans obstacle

## Références visuelles à joindre

- Image 1, référence de style uniquement : `/Users/alex/Claude/projets-actifs/opquast/Formations-MIWEB/Internationalisation/contact-sheet-internationalisation.png`
- Image 2, référence de style uniquement : `/Users/alex/Claude/projets-actifs/opquast/Formations-MIWEB/newsletter/newsletter-opquast-v5-imagegen-complete/images/jpg/slide-03-savoir-avant-de-s-abonner.jpg`

Ne pas modifier, copier ni réutiliser les textes, logos, numéros ou contenus métier de ces images. Elles servent uniquement à reprendre la sobriété, la hiérarchie, la palette, les cartes arrondies et le style d'illustration.

## Prompt d'édition utilisé pour produire la V2

Image source : `navigation-opquast-v5-essentielle/assets/slides/slide-03.png`, copiée dans la variante avant édition.

```text
Use case: precise-object-edit.
Asset type: final French presentation slide, 1672 x 941 pixels.
Edit target: the supplied slide 03 image.

Primary request: replace only the existing visible sentence "GARANTIE - La navigation commence immédiatement" with the exact sentence "GARANTIE - L'accès au contenu est immédiat".

Text accuracy is mandatory. Render the replacement exactly once, with this exact spelling, capitalization, accents, apostrophe and simple hyphen:
"GARANTIE - L'accès au contenu est immédiat"

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
Use case: productivity-visual.
Asset type: final French presentation slide, ready to publish as a single raster image.

Generate ONE complete landscape slide only. The final canvas must be exactly 1672 x 941 pixels, 16:9. All required typography must be rendered directly in the image by ImageGen. This is the final slide: no later composition, no text overlay, no empty placeholder reserved for post-processing.

Use Image 1 and Image 2 only as visual style references. Match their calm institutional educational style: luminous white background, deep navy typography, rounded pastel cards, flat vector interface mockups, simple colored icons, restrained shadows and generous whitespace. Keep the hierarchy as clear as the Newsletter rule slide and the visual semantics as concise as Internationalisation.

Do not reproduce any logo from the references. Do not create an Opquast logo, leaf mark, emblem, brand lockup, watermark, signature, seal or decorative lettering. The words "Opquast - présentation Miweb" must appear only as small plain text in the bottom-left footer.

Composition:
- Small plain header text at the top-left.
- A compact pale-blue block marker near the title containing the active block text.
- A blue rounded rule badge above or beside the large centered title.
- Main visual in the center: a two-state comparison of the same simplified web page journey.
  - Left, a pale red panel shows a requested content page blocked by an unnecessary intermediate screen, represented only by shapes and a barrier icon. No UI text.
  - Right, a pale green panel shows a direct arrow entering the requested content page immediately. No UI text.
- Place the impact sentence in the red panel and the guarantee sentence in the green panel.
- Place the final sentence in a wide pale-green rounded callout near the bottom.
- Small plain footer text at the bottom-left and exact pagination at the bottom-right.
- Keep the top-right airy, with only a very pale abstract corner shape and no logo.

Typography:
- Modern highly legible sans serif, similar to Marianne or Arial.
- Title very large and bold in deep navy.
- Block marker and rule badge compact but fully readable.
- Impact and guarantee text large enough for projection, never paragraph-sized.
- No decorative font, no tiny copy, no italic text.

Render ONLY the following visible strings, each exactly once, preserving accents, capitalization, punctuation, straight apostrophes and hyphens exactly as written:
1. "QUALITÉ NUMÉRIQUE - OPQUAST V5"
2. "A - SE SITUER"
3. "Entrer sans obstacle"
4. "RÈGLE 153"
5. "IMPACT - L'accès au contenu est retardé"
6. "GARANTIE - L'accès au contenu est immédiat"
7. "Pas de porte inutile."
8. "Opquast - présentation Miweb"
9. "03 / 17"

No other visible letters, words, numbers, pseudo-text, interface labels or typographic marks. Browser mockups must use abstract bars and shapes only. Do not add the word "Entrer", an address, a button label or any decorative number inside the mockups.

Constraints:
- One slide only, never a contact sheet, collage, deck preview or multi-slide layout.
- Exactly one red impact area and one green guarantee area.
- No real logo and no fake logo.
- No photography, no 3D render, no corporate stock characters.
- No popup terminology, no legal notice, no age gate and no cookie banner text.
- No rule number other than 153.
- Keep all text inside safe margins and fully visible.
- Prioritize exact French text and immediate comprehension over decorative detail.
```

## Contrôle avant acceptation

- Vérifier l'image en résolution originale 1672 x 941.
- Comparer caractère par caractère les neuf chaînes de la liste blanche.
- Vérifier que le visuel oppose bien un accès retardé à un accès direct, sans ajouter de scénario.
- Rejeter toute image comportant un logo, du pseudo-texte dans les interfaces ou une règle autre que 153.
