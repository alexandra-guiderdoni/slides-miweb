# Corrections de l’audit e-commerce, sans modification des PNG

Le propriétaire a autorisé la correction du lecteur, des textes associés et des validateurs, en reportant les images PNG. Référence : [audit du 28 octobre](revue-2026-10-28-ecommerce-opquast-v5-f9b3ae1.md). Base de travail : `4a6d757`, branche de correction isolée.

## Traitement des constats

| Constat | Résultat de cette passe |
|---|---|
| M1, équivalent textuel des questions | Les textes visibles sont maintenant dans l’accordéon de description du lecteur, pour les 132 slides. Les deux accordéons sont conservés. |
| M2, alternatives | 120 alternatives révisées, avec passe alt-text et relecture indépendante. Les questions restent des questions ; les descriptions longues portent leur texte intégral. |
| M3, libellés Opquast | Notes de R38, R63 et R66 actualisées et datées. Le libellé imprimé ancien reste dans les PNG et dans leur transcription fidèle. |
| M4, transitions et validateur | 131 transitions et une conclusion. Le validateur autorise ces rubriques en dehors des 2 à 4 titres de contenu ; ce comptage ne vaut pas preuve de qualité éditoriale. |
| M5, notes | 35 notes de question individualisées, métapédagogie retirée, répétitions et attributions corrigées. Relecture croisée puis correction des réserves de cette relecture. |
| M6, diagnostic public | Limite explicitée sur la page et dans le README : les réponses restent publiques. T0 sert d’amorçage ; après consultation du support, T1 - T0 ne mesure pas à lui seul un apprentissage. Aucune confidentialité n’est revendiquée. |
| M7, indices et distracteurs | Reportés avec les énoncés imprimés dans les PNG. Notes 105, 109 et 113 précisent les limites des scénarios SAV, traitement de réclamation et panier/récapitulatif. Cela ne répare pas les distracteurs. |
| M8, indisponibilité en 017 | Note explicite : le seul grisé ne suffit pas à la différenciation visuelle et textuelle. Illustration reportée. |
| M9, slide 070 | Alternative corrigée avec les correspondances A/R39, B/R33, C/R63. Envoi non vérifié explicité ; ambiguïté de la coche reportée. |
| M10, sans JavaScript | CSS de repli sous empreinte CSP : les 132 slides et les 264 panneaux sont visibles dans un navigateur dont JavaScript est désactivé. |
| M11, anciennes revues | Leur portée est rectifiée dans `source/reviews/README.md`. Les décisions historiques restent conservées ; aucune nouvelle réception des PNG n’est prétendue. |
| M12, liens d’évitement | Gestionnaire corrigé dans les 32 générateurs et pages régénérées des 31 jeux. Les ancres conservent la position et leur état d’historique ; retour et avance restaurent aussi le mode toutes les slides. |

Autres corrections : descriptions 026, 029 et 046 ; métadonnées des règles et sources ; focus restauré sur le titre après un changement de slide, navigation clavier limitée au lecteur, pincement autorisé et geste multi-contact annulé ; nom accessible du menu ; date de juin retirée de l’état d’accessibilité du jeu ; lien Accessibilité dans le pied de page du jeu et de l’accueil ; liens Markdown avec paramètres conservés.

La matrice et le jeu vérifient les parties ZIP avant écriture : noms sûrs, noms uniques, bornes entières, partition continue et exhaustive. Les libellés identiques ne suppriment plus de liens. La publication vérifie chaque archive déclarée et ses octets. Une archive trop volumineuse est rejetée avant remplacement des archives existantes et des pages. Les dates impossibles du catalogue et les champs éditoriaux identiques sont rejetés.

## Preuves de vérification

- 132 PNG comparés à la base Git par SHA-256 : identiques. Champs `numero`, `titre`, `image`, `textes_visibles` et `transcription` identiques sur les 132 slides.
- 420 tests Python dans 33 suites : 419 réussis, 1 ignoré par la matrice dépourvue de ZIP exemple. Cela comprend les tests de chacun des 31 jeux, de la matrice et des scripts.
- Tests de régression du vrai gestionnaire JavaScript exécuté dans un contexte Node isolé pour les 32 générateurs : ancres, slide 132, mode toutes les slides, retour vers une ancre mémorisée. Échec observé avant correction, réussite après correction.
- Contrôle des notes : 132 slides, 0 erreur, 0 avertissement. La relecture indépendante reste distincte de ce contrôle structurel.
- `scripts/validate_variant.sh ecommerce-opquast-v5` : tests du jeu, html-validate et vnu réussis sur les trois pages et l’accueil.
- Navigateur agent-browser 0.31.1, session dédiée locale : depuis la slide 60, activation clavier du lien Sommaire conserve `#sommaire` et la seule slide 60 ; passage au mode toutes les slides, retour vers cette ancre puis avance : 1, puis 132 slides visibles.
- Slide 90 : accordéon ouvert, énoncé et A/B/C lus dans le DOM. Flèche droite : slide 91 et focus sur son titre, aucun focus sous un élément masqué. Fin : slide 132.
- Session distincte lancée avec `--blink-settings=scriptEnabled=false` : style `noscript` interprété, 132 slides et 264 panneaux visibles. Pas d’erreur remontée dans cette session ni dans le parcours normal ; plus d’avertissement DSFR sur le nom du menu.
- Génération répétée : 7 sorties du jeu identiques par SHA-256, y compris les deux ZIP. Les deux archives restent sous 100 Mio et couvrent exactement les 132 PNG avec l’export d’alternatives courant.

Commandes principales :

```bash
python3 scripts/check_notes_orales_opquast.py ecommerce-opquast-v5
python3 -m unittest discover -s scripts/tests
python3 -m unittest discover -s matrice-slide-ai/tests
# Puis la suite tests de chacun des 31 jeux.
scripts/validate_variant.sh ecommerce-opquast-v5
python3 matrice-slide-ai/publish_variant.py --slug ecommerce-opquast-v5
```

Les contre-tests reprennent les défauts établis dans l’audit ShipGuard, mais cette passe n’est pas une nouvelle campagne ShipGuard ni un audit RGAA complet. Les essais Node ne sont pas des essais avec lecteur d’écran. Le test navigateur sans JavaScript est distinct de ces tests unitaires.

## Réserves maintenues

Les fautes d’habillage des PNG 028, 049, 117 et 125, leurs autres défauts visuels, les libellés imprimés anciens, les indices/distracteurs et la formule pédagogique imprimée restent visibles. Les transcriptions les accompagnent sans fabriquer une autre version du visuel. La qualification globale demeure donc « utilisable avec réserves », et non « tous les constats clos ».

Les corrections communes sont limitées à la navigation/historique. Les autres améliorations du lecteur et des archives s’appliquent au jeu e-commerce et à la matrice des futurs jeux ; les anciens jeux conservent leurs autres comportements.
