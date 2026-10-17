# QA des images intégrant la règle 149

## Périmètre

- Slide 18 : cinq facteurs de décision.
- Slide 20 : règles 147 et 149.
- Slide 23 : cinq questions avant de consommer.
- Slide 24 : dix règles étudiées, dont la règle 149.

## Contrôles effectués

- Génération avec `image_gen` à partir des images de référence de la série.
- Dimensions de chaque candidat : 1672 x 941 pixels.
- Inspection visuelle en pleine définition ou en rendu haute définition.
- Contact sheet créée et inspectée : `outputs/ia-slides/2026-10-17-regle-149/contact-sheet.png`.
- Contrôle caractère par caractère des titres, libellés, numéros de règles et paginations.
- Absence de texte parasite, de règle dupliquée et de pagination erronée.
- Cohérence du masque commun, du header, du footer et de la palette.

## Verdict

- Slide 18 a001 : acceptée.
- Slide 20 a001 : acceptée.
- Slide 23 a001 : acceptée.
- Slide 24 a001 : acceptée.
- Reçu machine : `outputs/ia-slides/2026-10-17-regle-149/imagegen-receipt.tsv`.
- Les prompts complets envoyés à `image_gen` sont conservés dans `source/prompts/`.
- `NOT VERIFIED` : l’export automatique depuis le JSONL n’est pas disponible, car l’intégration embarquée n’a pas exposé d’identifiant `ig_*` dans le reçu ; cette limite ne concerne ni les PNG ni les prompts conservés manuellement.
