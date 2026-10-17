# Correction ciblée ImageGen - slide 28

## Défaut observé

- Les trois cartes séparent les acronymes de leur question par un retour à la ligne, sans le tiret simple exigé.

## Invariants à préserver

- Conserver strictement le format 16:9, le masque clair, la composition, les couleurs, les icônes, les flèches, l'enveloppe, le titre, le badge, le contrôle, la limite, le footer et la pagination.
- Conserver tous les autres textes visibles à l'identique.

## Correction demandée

- Former exactement `SPF - Qui peut envoyer ?` dans la carte de gauche.
- Former exactement `DKIM - Le message est-il signé ?` dans la carte centrale.
- Former exactement `DMARC - Que faire si l'alignement échoue ?` dans la carte de droite.
- Utiliser uniquement le tiret simple `-`, avec une espace de chaque côté. Un retour à la ligne après le tiret reste acceptable si nécessaire, à condition que le tiret soit visible.

## Interdits

- Ne remplacer le tiret simple par aucun autre signe.
- Ne déplacer, reformuler ou ajouter aucun autre texte.
- Ne modifier aucun autre élément visuel.
- Aucun texte parasite, faux logo ni filigrane.
