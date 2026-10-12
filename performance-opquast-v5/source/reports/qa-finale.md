# QA finale - Performance selon Opquast V5

## Résultat

- Statut : `VALIDEE_PRODUCTION` par délégation explicite de la référente Opquast.
- Série exhaustive : 32 slides, dont 28 `ESSENTIEL_60`, 3 `APPROFONDISSEMENT` et 1 `ANNEXE`.
- Parcours essentiel : slides 01 à 06, 08 à 25, 28, 29, 31 et 32.
- Couverture : 64 unités métier sur 64 rattachées à la source obligatoire.
- Provenance : 100 % des éléments métier publiés rattachés à `conversation-opquast-performance.md`.
- `SOURCE_MD_ABSENTE` : 0.
- Affirmation Opquast rejetée : 0.
- Contradiction persistante : 0.

## Preuves mesurées

- 32 PNG finaux, tous en 1672 × 941 pixels, avec 32 identifiants uniques.
- 32 images uniques dans `slides.json` et neuf champs canoniques par entrée.
- Alternatives : 49 caractères au maximum ; aucune ne commence par « image de », « photo de », « illustration de » ou « logo ».
- Deux slogans présents uniquement sur les slides 01 et 32.
- Planche finale et 32 PNG originaux inspectés ; rythme, palette, titres, footers et paginations cohérents.
- Notes orales : 32 slides, 0 erreur, 0 avertissement.
- Tests communs : 9 tests réussis.
- Tests du jeu : 11 tests réussis.
- Validation de variante : 11 tests réussis.
- Tests de matrice : 24 tests réussis et 1 test sauté.
- ShipGuard : 102 fichiers analysés, aucun constat ; analyse statique en lecture seule.
- Catalogue local : titre exact, slug exact, quatre tuiles de la mission et cinq liens de tuile Performance présents.
- Navigateur local sur le port 8002 : diaporama, navigation clavier, historique, projection plein écran, mode toutes les slides, swipe gauche, deux accordéons, alternatives, ZIP et page d’accessibilité inspectés.
- Les 32 sources d’images du mode toutes les slides répondent avec succès ; aucun échec HTTP d’image.

Le premier lancement d’`agent-browser` a rencontré une version Playwright absente. La recette a été exécutée sans installation en réutilisant la session Chrome déjà active et son navigateur système.

## Références de contrôle

- API Opquast `qualite-numerique` : 9 règles récupérées individuellement avec `source=api` le 12 octobre 2026.
- Documents actifs de la fabrique et contrats de `slides-miweb`.
- Les références de contrôle n’ont ajouté aucun contenu métier.

## Contrôles `NOT VERIFIED`

- Test humain des trois secondes : `NOT VERIFIED`.
- Contraste instrumenté : `NOT VERIFIED`.
- Relecture croisée par une seconde personne : `NOT VERIFIED`.
- Essai pédagogique réel : `NOT VERIFIED`.

Ces limites n’annulent pas les contrôles techniques et visuels effectivement exécutés ; elles ne sont pas présentées comme vérifiées.
