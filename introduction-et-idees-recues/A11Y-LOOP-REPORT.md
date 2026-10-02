# Rapport de boucle d'accessibilité

## Périmètre

- Jeu : `introduction-et-idees-recues`
- Date : 2 octobre 2026
- Pages contrôlées : présentation en mode toutes les slides, alternatives textuelles et déclaration d'accessibilité
- Source : génération locale depuis `slides.json`

## Outils et réglages

- axe-core CLI 4.12.1
- Google Chrome 154.0.8037.95 et ChromeDriver 150.0.7871.46
- Tags : `wcag2a`, `wcag2aa`, `wcag21aa`, `wcag22aa`
- Contrôles complémentaires : HTML Validate, Nu HTML Checker, tests de contrat locaux et inspection dans Chrome

## Résultat

| Itération | Violations axe-core | Éléments à vérifier manuellement | Corrections | Nouvelles violations |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | 57 éléments rattachés à la règle de contraste | 0 | 0 |

Score automatisé selon la formule de la boucle : **100 sur 100**. Les principes Perceptible, Utilisable, Compréhensible et Robuste ne comportent aucune violation automatisée détectée.

### Contraste à confirmer manuellement

axe-core a classé la règle `color-contrast` comme incomplète sur les liens et composants DSFR dont le fond ou le soulignement est produit par plusieurs couches CSS. Les couleurs calculées dans le navigateur ont été vérifiées manuellement :

- texte `rgb(22, 22, 22)` sur fond blanc : **18,10:1** ;
- texte `rgb(58, 58, 58)` sur fond blanc : **11,37:1** ;
- texte `rgb(0, 0, 145)` sur fond `rgb(227, 227, 253)` : **11,83:1**.

Ces rapports dépassent le seuil de 4,5:1 applicable au texte courant.

## Contrôles structurels

- 14 slides et 14 images finales ;
- 14 accordéons de transcription et 14 accordéons de discours oral ;
- une page d'alternatives qui restitue les 14 transcriptions et les 14 discours oraux ;
- courriels des intervenants présents dans les transcriptions, absents des visuels ;
- langue française, titre de page et liens d'évitement présents ;
- niveaux de titres continus dans les accordéons et dans la page des alternatives ;
- modes diaporama, toutes les slides et projection contrôlés ;
- 11 tests locaux réussis ;
- HTML Validate et Nu HTML Checker sans erreur ;
- aucune erreur ni alerte dans la console du navigateur.

## Limites

Un scan automatisé ne couvre qu'une partie de l'accessibilité. La fidélité au PPTX, la pertinence des alternatives, les QR codes, la lecture au clavier et l'aspect visuel ont donc été contrôlés séparément. Aucun changement n'a été publié pendant cette boucle.
