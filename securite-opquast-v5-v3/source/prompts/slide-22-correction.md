# Correction ciblée ImageGen - slide 22

## Défaut observé

- Le libellé autonome `Content-Security-Policy` apparaît au-dessus de la barrière alors qu'il ne fait pas partie de la liste blanche.

## Invariants à préserver

- Conserver strictement le format 16:9, le masque clair, la composition, les couleurs, les icônes, les flux, le titre, le badge, le footer et la pagination.
- Conserver l'occurrence autorisée de `Content-Security-Policy` dans `CONTRÔLE - Lire la politique Content-Security-Policy`.
- Conserver tous les autres textes visibles à l'identique.

## Correction demandée

- Supprimer uniquement le libellé autonome `Content-Security-Policy` situé au-dessus de la barrière centrale.
- Laisser cette zone sans aucun texte de remplacement.

## Interdits

- Ne pas supprimer ni modifier l'occurrence présente dans le contrôle inférieur.
- Ne déplacer, reformuler ou ajouter aucun autre texte.
- Ne modifier aucun autre élément visuel.
- Aucun texte parasite, faux logo ni filigrane.
