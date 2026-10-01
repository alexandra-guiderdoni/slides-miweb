# Rapport de boucle d’accessibilité

## Périmètre

- Jeu : `web-accessible-points-de-controle-rapides`
- Date : 2 octobre 2026
- Pages contrôlées : présentation en mode toutes les slides, alternatives textuelles et déclaration d’accessibilité
- Source : génération locale depuis `slides.json`

## Outils et réglages

- axe-core CLI 4.13.0
- Chrome for Testing et ChromeDriver 154.0.8037.92
- Tags : `wcag2a`, `wcag2aa`, `wcag21aa`, `wcag22aa`
- Chargement différé d’une seconde avant le scan
- Contrôles complémentaires : HTML Validate, Nu HTML Checker et tests de contrat locaux

## Résultat

| Itération | Violations axe-core | Éléments à vérifier manuellement | Corrections | Nouvelles violations |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | 81 éléments rattachés à la règle de contraste | 0 | 0 |

Score automatisé selon la formule de la boucle : **100 sur 100**. Les principes Perceptible, Utilisable, Compréhensible et Robuste ne comportent aucune violation automatisée détectée.

### Contraste à confirmer manuellement

axe-core a classé la règle `color-contrast` comme incomplète sur les liens et composants DSFR dont le fond ou le soulignement est produit par plusieurs couches CSS. Les couleurs calculées dans le navigateur ont été vérifiées manuellement :

- texte `rgb(22, 22, 22)` sur fond `rgb(238, 238, 238)` : **15,60:1** ;
- texte `rgb(58, 58, 58)` sur fond blanc : **11,37:1** ;
- texte `rgb(0, 0, 145)` sur fond `rgb(227, 227, 253)` : **11,83:1** ;
- texte `rgb(22, 22, 22)` sur fond blanc : **18,10:1**.

Ces rapports dépassent le seuil de 4,5:1 applicable au texte courant.

## Contrôles structurels

- 30 slides et 30 images finales ;
- 30 accordéons de transcription et 30 accordéons de discours oral ;
- 7 tableaux rendus avec `caption`, `thead`, `tbody` et `scope="col"` ;
- langue française et titre de page présents ;
- alternatives courtes relues séparément ;
- 16 tests locaux réussis ;
- HTML Validate et Nu HTML Checker sans erreur.

## Limites

Un scan automatisé ne couvre qu’une partie de l’accessibilité. La cohérence éditoriale, la fidélité au PPTX, la pertinence des alternatives, la lecture au clavier et l’aspect visuel ont donc été contrôlés séparément. Aucun changement n’a été publié pendant cette boucle.
