# QA finale - Sécurité selon Opquast V5 - version 2

## Périmètre livré

- Nouvelle variante autonome : `securite-opquast-v5-v2`.
- 35 images reprises sans modification sémantique de la variante publiée.
- 35 champs `notes_orateur` révisés.
- Quatre étalons validés explicitement par l’utilisateur : slides 1, 5, 30 et 35.
- Relecture croisée indépendante des 31 autres notes.

## Fidélité des sources

- Règles 197 à 217 vérifiées via le MCP Opquast avec `source=api`.
- Règles transversales citées vérifiées via la même source.
- Guide, glossaire et corpus documentaire utilisés seulement pour les éclairages VPTCS, QSE-IP, MIME, intégrité et double authentification.
- Aucun point laissé « à vérifier ».
- Aucun autre champ de `slides.json` ne diffère de la variante source.

## Contrôles exécutés

- `python3 scripts/check_notes_orales_opquast.py securite-opquast-v5-v2` : 35 slides, 0 erreur, 0 avertissement.
- Longueur des notes : 84 à 110 mots.
- `scripts/optimiser-images.sh securite-opquast-v5-v2` : recompression sans perte.
- `python3 securite-opquast-v5-v2/build.py` : génération réussie.
- `scripts/validate_variant.sh securite-opquast-v5-v2` : 13 tests réussis.
- `python3 -m unittest discover -s scripts/tests` : 10 tests réussis.
- Audit des alternatives : aucun champ vide, aucun préfixe redondant, aucune alternative supérieure à 80 caractères.

## Recette navigateur

- Slide 5 accessible directement par fragment.
- Commande « Ouvrir les accordéons » : les deux accordéons sont ouverts.
- URL `?slides=all#diaporama` : 35 slides visibles sur 35.
- Page d’alternatives : 35 messages, transcriptions et discours présents.
- Aucune erreur JavaScript détectée.

## Verdict

- Variante prête localement.
- Version publiée `securite-opquast-v5` inchangée.
- Aucun commit, push ou publication effectué.
