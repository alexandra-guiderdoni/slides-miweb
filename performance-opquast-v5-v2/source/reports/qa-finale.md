# QA finale - Serveur et Performance selon Opquast - V2

## Périmètre livré

- Nouvelle variante autonome : `performance-opquast-v5-v2`.
- 35 slides du parcours initial et 5 slides d’annexe glossaire, soit 40 slides.
- Règle 149 intégrée au bloc « laisser décider avant de consommer ».
- Annexe consacrée aux 26 termes du glossaire Opquast de la catégorie « Serveur et performances ».
- Définitions exactes placées dans les notes orales, avec les notions importantes en gras.

## Fidélité des sources

- Règle 149 vérifiée via le MCP Opquast avec `source=api`.
- Libellé, objectifs, explication et contrôle consignés dans `reports/regle-149-opquast.md`.
- Glossaire vérifié via le MCP Opquast, édition du 17 juin 2026.
- Comparaison automatisée des 26 définitions après neutralisation du balisage Markdown : aucune différence, aucun terme manquant ou supplémentaire.
- La sélection transversale reste explicitement distincte de la rubrique officielle « Serveur et performances ».

## Contrôles des images

- Neuf PNG générés ou régénérés à 1672 x 941 pixels pour cette variante.
- Inspection des candidats et des planches contact.
- Titres, textes visibles, numéros de règles, comptes et paginations contrôlés.
- Reçus conservés dans `outputs/ia-slides/2026-10-17-regle-149/` et `outputs/ia-slides/2026-10-17-annexe-glossaire/`.
- Prompts complets conservés dans `source/prompts/`.
- Les faux logos, la mention parasite « JS » et le texte parasite « 404 » ont été supprimés des candidats concernés avant intégration.

## Contrôles exécutés

- `python3 scripts/check_notes_orales_opquast.py performance-opquast-v5-v2` : 40 slides, 0 erreur, 0 avertissement.
- `scripts/optimiser-images.sh performance-opquast-v5-v2` : recompression sans perte.
- `python3 performance-opquast-v5-v2/build.py` : génération réussie.
- `scripts/validate_variant.sh performance-opquast-v5-v2` : 13 tests réussis et validation HTML sans erreur.
- `python3 -m unittest discover -s performance-opquast-v5-v2/tests` : 13 tests réussis.
- `python3 -m unittest discover -s scripts/tests` : 10 tests réussis.
- Audit des alternatives : 40 champs renseignés, aucun préfixe redondant, aucune alternative supérieure à 80 caractères.

## Recette locale

- Accueil servi avec le titre « Serveur et Performance selon Opquast - V2 ».
- URL `?slides=all#diaporama` accessible et contenant la slide 40.
- Page d’alternatives accessible et contenant les termes et définitions du glossaire.
- Image de la slide 40 servie en 1672 x 941 pixels.

## Verdict

- Variante prête localement.
- Version publiée `performance-opquast-v5` inchangée.
- Aucun commit, push ou publication effectué.
