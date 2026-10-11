# QA finale — Projets et livrables selon Opquast V5

## Résultat

- Statut : `VALIDEE_PRODUCTION` par délégation explicite de la référente Opquast.
- Série exhaustive : 45 slides, dont 23 `ESSENTIEL_60` et 22 slides d’atlas.
- Couverture : 82 unités sur 82 affectées ; 59 livrables ou objets sur 59 nommés.
- Provenance : 100 % des éléments métier publiés rattachés aux deux Markdown obligatoires.
- `SOURCE_MD_ABSENTE` : 0.
- Affirmation Opquast rejetée : 0.
- Contradiction persistante : 0.

## Preuves mesurées

- 45 PNG finaux, tous en 1672 × 941 pixels.
- 45 images uniques dans `slides.json` et neuf champs canoniques par entrée.
- Alternatives : 59 caractères au maximum.
- `factory.py resume` : 45 slides acceptées, aucune en attente, aucun problème.
- Planche finale : 45 images inspectées ; rythme, palette, titres, badges, footers et paginations cohérents.
- Notes orales : 45 slides, 0 erreur, 0 avertissement.
- Tests communs : 9 tests réussis.
- Tests du jeu : 11 tests réussis.
- ShipGuard : 122 fichiers analysés, aucun constat ; analyse statique report-only.
- Catalogue local : titre exact, slug exact et cinq liens de tuile présents.
- Navigateur local sur le port 8001 : diaporama, plein écran, mode toutes les slides, historique, clavier, swipe gauche, alternatives, ZIP et page d’accessibilité inspectés.

Le port 8000 était occupé par un serveur `uvicorn` étranger nommé « MTPLX ». Il a été préservé ; le contrôle local équivalent a été exécuté sur le port 8001.

## Références de contrôle

- API Opquast `qualite-numerique` : règles 234, 77, 69, 85 et 222, vérifiées le 11 octobre 2026.
- Documents actifs de la fabrique et contrats de `slides-miweb`.
- Les références de contrôle n’ont ajouté aucun contenu métier.

## Contrôles `NOT VERIFIED`

- Test humain des trois secondes : `NOT VERIFIED`.
- Contraste instrumenté : `NOT VERIFIED`.
- Relecture croisée par une seconde personne : `NOT VERIFIED`.
- Essai pédagogique réel : `NOT VERIFIED`.

Ces limites n’annulent pas les contrôles techniques et visuels effectivement exécutés ; elles ne sont pas présentées comme vérifiées.
