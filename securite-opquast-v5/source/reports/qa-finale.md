# QA finale - Sécurité selon Opquast V5

## Résultat

- Statut : `VALIDEE_PRODUCTION` par délégation explicite de la référente Opquast.
- Série exhaustive : 35 slides, dont 29 `ESSENTIEL_60`, 5 `APPROFONDISSEMENT` et 1 `ANNEXE`.
- Parcours essentiel : slides 01 à 25, puis 32 à 35.
- Couverture : 140 champs métier sur 140 rattachés à la source obligatoire.
- Provenance : 100 % des éléments métier publiés rattachés à `conversation-opquast-securite.md`.
- `SOURCE_MD_ABSENTE` : 0.
- Affirmation Opquast rejetée : 0.
- Contradiction persistante : 0.

## Preuves mesurées

- 35 PNG finaux, tous en 1672 × 941 pixels, avec 35 identifiants uniques.
- 35 images uniques dans `slides.json` et neuf champs canoniques par entrée.
- Alternatives : 59 caractères au maximum ; aucune ne commence par « image de », « photo de », « illustration de » ou « logo ».
- `factory.py resume` : 35 slides acceptées, aucune en attente, aucun problème.
- Planche finale : 35 images inspectées ; rythme, palette, titres, footers et paginations cohérents.
- Notes orales : 35 slides, 0 erreur, 0 avertissement.
- Tests communs : 9 tests réussis.
- Tests du jeu : 11 tests réussis.
- Validation de variante : 11 tests réussis.
- ShipGuard : 110 fichiers analysés, aucun constat ; analyse statique en lecture seule.
- Catalogue local : titre exact, slug exact et cinq liens de tuile présents.
- Navigateur local sur le port 8001 : diaporama, navigation clavier, projection plein écran, mode toutes les slides, retour navigateur, swipe gauche, deux accordéons, alternatives, ZIP et page d’accessibilité inspectés.

Le port 8000 était occupé par un processus étranger. Il a été préservé ; la recette locale équivalente a été exécutée sur le port 8001.

## Références de contrôle

- API Opquast `qualite-numerique` : 39 règles récupérées individuellement avec `source=api` le 12 octobre 2026.
- Documents actifs de la fabrique et contrats de `slides-miweb`.
- Les références de contrôle n’ont ajouté aucun contenu métier.

## Contrôles `NOT VERIFIED`

- Test humain des trois secondes : `NOT VERIFIED`.
- Contraste instrumenté : `NOT VERIFIED`.
- Relecture croisée par une seconde personne : `NOT VERIFIED`.
- Essai pédagogique réel : `NOT VERIFIED`.

Ces limites n’annulent pas les contrôles techniques et visuels effectivement exécutés ; elles ne sont pas présentées comme vérifiées.
