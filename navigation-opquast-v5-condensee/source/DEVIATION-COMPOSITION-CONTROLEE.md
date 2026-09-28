# Déviation documentée - composition contrôlée

## Choix de production

- ImageGen produit une illustration sémantique distincte pour chaque slide narrative.
- Les illustrations sont conservées dans `source/illustrations/`.
- Les titres, numéros de règles, cartes, messages, pied de page et pagination sont ajoutés par `source/render_slides.py`.
- Les PNG finaux ont donc une provenance hybride : illustration ImageGen et composition typographique déterministe.

## Justification

- Les numéros et les formulations Opquast doivent rester exacts.
- La génération d’image ne doit pas inventer, déformer ou omettre une règle.
- Le texte composé séparément garantit la fidélité aux sources et la lisibilité du support.

## Contrôles conservés

- Une illustration ImageGen par slide narrative.
- Inspection individuelle des illustrations en pleine résolution.
- Rendu final en 1672 x 941 pixels.
- Inspection individuelle des PNG finaux.
- Planche finale de contrôle.
- Transcriptions confrontées aux PNG finaux avant publication.

## Limite

- Les PNG finaux ne sont pas déclarés comme des générations ImageGen intégrales.
- ImageGen reste le moteur de la matière visuelle, pas celui de la typographie finale.
