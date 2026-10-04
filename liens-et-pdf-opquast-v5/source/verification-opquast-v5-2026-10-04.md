# Vérification Opquast V5 — liens et PDF

Date de consultation : 2026-10-04.

Source officielle consultée : référentiel « Qualité Numérique », Version 5 – 2025-2030, 245 règles, https://checklists.opquast.com/fr/qualite-numerique/

## Résultats utiles au storyboard

- La rubrique **Liens** va de la règle 136 à la règle 152 dans le référentiel V5 actuel.
- La séquence 136–150 donnée dans la source utilisateur correspond au référentiel actuel.
- La règle **151** porte actuellement sur les liens entrants.
- La règle **152** porte actuellement sur la validité des liens internes.
- La règle **153** appartient actuellement à Navigation et ne doit pas être utilisée pour les liens entrants.
- La règle **240** porte sur le texte sélectionnable des PDF internes.
- La règle **241** porte sur la structure de titres des PDF internes.
- La règle **195** porte sur les styles dédiés à l'impression.
- La règle **207** porte sur l'indication du type MIME de chaque ressource.

## Vérification ciblée des règles PDF

La fiche officielle de la règle 240 indique notamment que le texte réel permet la manipulation, l'indexation et une meilleure accessibilité, et recommande de ne pas diffuser un simple scan image lorsqu'un vrai contenu textuel peut être produit.

La fiche officielle de la règle 241 indique que la structure de titres facilite la compréhension et la navigation, et recommande d'utiliser les styles hiérarchiques dans le document source puis un export PDF balisé ou tagué lorsque l'outil le permet.

Le contrôle de la règle 240 vise chaque PDF interne publié dans le site. Le terme « interne » ne se limite donc pas aux documents produits par l’organisme : un PDF hébergé sur le site peut aussi être concerné lorsqu’il vient d’un tiers. La [discussion Opquast sur la règle 241](https://checklists.opquast.com/workshops/assurance-qualite-web/criterion/54452/) explicite ce périmètre. L’annexe A7 a été corrigée dans le visuel, la transcription et le discours oral pour exprimer cette portée.

## Limites documentaires

La préférence « HTML plutôt que PDF lorsque c'est possible » figure dans la synthèse utilisateur comme doctrine attribuée au livre. Elle n'a pas été retrouvée textuellement sur les pages officielles V5 consultées pendant cette étape. Si cette phrase doit devenir un texte visible dans une slide finale, la source primaire devra être revalidée avant verrouillage.
