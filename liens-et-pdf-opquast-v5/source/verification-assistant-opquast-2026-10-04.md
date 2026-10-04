# Vérification complémentaire — Assistant Opquast — 2026-10-04

## Mode

Le plugin `@Assistant Opquast` a été explicitement invoqué dans cette conversation. Sa consigne et son corpus du livre *Qualité et conformité des services numériques*, 4e édition 2026, ont été consultés. Cette revue est exécutée dans la même conversation et n'est pas présentée comme un audit humain indépendant.

L'action API `getRuleByNumber` recommandée par le plugin n'est pas exposée dans cette surface. Les formulations actuelles ont donc été recontrôlées sur le référentiel officiel public Opquast V5 : https://checklists.opquast.com/fr/qualite-numerique/

## Constats documentaires

- Rubrique Liens actuelle : règles 136 à 152.
- R. 145 : « Les numéros de téléphone sont activables via le protocole approprié. » Son objectif officiel est de faciliter l'utilisation des numéros, notamment sur mobile.
- R. 151 : liens entrants non interdits ni restreints.
- R. 152 : tous les liens internes sont valides.
- R. 240 : texte des PDF internes sélectionnable.
- R. 241 : PDF internes dotés d'une structure de titres.
- Le corpus du livre, dans le passage associé à la règle 240, indique qu'en matière d'accessibilité numérique, le format HTML est toujours préférable au PDF lorsque cela est possible. Cette phrase relève du livre et ne constitue pas une règle autonome supplémentaire.

## Conséquence pour le storyboard

- Recentrer la slide 4 afin de ne pas attribuer à la règle 145 le même objectif d'avertissement que les règles 144 et 146.
- Regrouper 151–152 séparément des règles de téléchargement dans l'annexe A1.
- Lever le statut « source primaire non revalidée » concernant la préférence HTML/PDF, tout en conservant son statut doctrinal.
