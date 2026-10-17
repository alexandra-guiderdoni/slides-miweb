# Correction ciblée ImageGen - slide 26

## Défaut observé

- Les libellés `Server:`, `X-Powered-By:` et `X-AspNet-Version:` sont répétés dans la fausse réponse HTTP, en dehors de l'intitulé autorisé de la règle 213.

## Invariants à préserver

- Conserver strictement le format 16:9, le masque clair, la composition en deux panneaux, les couleurs, les icônes, la loupe, le titre, les attendus, la limite, le footer et la pagination.
- Conserver exactement l'intitulé autorisé `213 - Inspecter Server, X-Powered-By et X-AspNet-Version`.
- Conserver tous les autres textes visibles à l'identique.

## Correction demandée

- Remplacer uniquement les trois libellés `Server:`, `X-Powered-By:` et `X-AspNet-Version:` dans la fausse réponse HTTP par trois traits horizontaux abstraits, sans lettres ni ponctuation.
- Conserver les traits abstraits figurant les valeurs, afin que la réponse reste identifiable comme une représentation schématique.

## Interdits

- Ne pas modifier l'intitulé de la règle 213.
- Ne déplacer, reformuler ou ajouter aucun autre texte.
- Ne modifier aucun autre élément visuel.
- Aucun texte parasite, faux logo ni filigrane.
