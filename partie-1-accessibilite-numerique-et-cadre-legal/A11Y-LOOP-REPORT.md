# Rapport de boucle d’accessibilité

## Périmètre

- Jeu : `partie-1-accessibilite-numerique-et-cadre-legal`
- Date : 2 octobre 2026
- Pages contrôlées : présentation en mode toutes les slides, alternatives textuelles et déclaration d’accessibilité
- Source : génération locale depuis `slides.json`

## Outils et réglages

- axe-core CLI 4.13.0
- Chrome Headless 154
- Tags : `wcag2a`, `wcag2aa`, `wcag21aa`, `wcag22aa`
- Chargement différé d’une seconde avant le scan
- Contrôles complémentaires : HTML Validate, Nu HTML Checker, tests de contrat locaux et inspection dans Chrome

## Résultat

| Itération | Violations axe-core | Corrections | Nouvelles violations |
| ---: | ---: | ---: | ---: |
| 1 | 0 | 0 | 0 |

Score automatisé selon la formule de la boucle : **100 sur 100**. Les trois pages ne comportent aucune violation automatisée détectée.

La règle de contraste est restée incomplète sur plusieurs liens et composants DSFR dont le fond ou le soulignement est produit par plusieurs couches CSS. Les couleurs sont celles du même gabarit DSFR déjà contrôlé : les rapports calculés vont de 11,37:1 à 18,10:1 et dépassent le seuil de 4,5:1 applicable au texte courant.

## Contrôles structurels

- 39 slides et 39 images finales ;
- 39 accordéons de transcription et 39 accordéons de discours oral ;
- 9 tableaux rendus avec `caption`, `thead`, `tbody` et `scope="col"` ;
- les 13 thèmes du RGAA rendus comme une liste ordonnée ;
- langue française, titre de page et hiérarchie des titres validés ;
- 19 tests locaux réussis ;
- HTML Validate et Nu HTML Checker sans erreur ;
- première et dernière slides contrôlées visuellement dans Chrome ;
- accordéons de la dernière slide contrôlés dans l’arbre d’accessibilité du navigateur.

## Limites

Un scan automatisé ne couvre qu’une partie de l’accessibilité. La fidélité au PPTX, la pertinence des alternatives, la cohérence des 39 visuels et la lecture au clavier ont donc été contrôlées séparément. Aucun changement n’a été publié pendant cette boucle.
