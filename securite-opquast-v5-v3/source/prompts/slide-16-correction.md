# Correction ImageGen - slide 16

## Défaut observé

- Les quatre verdicts sont écrits deux fois : dans le cartouche unique et dans les quatre capsules du bas.

## Invariants à préserver

- Conserver strictement toute la slide, notamment le titre, les personnages, la checklist des cinq actions, le cartouche `VERDICT - Présent, valide, non conforme ou indéterminé`, le footer et la pagination.
- Conserver les quatre capsules colorées et leurs quatre pictogrammes, dans le même ordre : coche verte, coche bleue, croix orange, point d'interrogation gris.
- Conserver le format exact 1672 x 941 pixels.

## Correction visuelle attendue

- Effacer uniquement les quatre libellés `Présent`, `Valide`, `Non conforme` et `Indéterminé` situés dans les capsules du bas.
- Rééquilibrer discrètement les quatre pictogrammes au centre de leurs capsules sans changer leur ordre, leur couleur ni leur forme.

## Interdits

- Ne pas toucher au cartouche unique `VERDICT - Présent, valide, non conforme ou indéterminé`.
- Ne pas modifier la checklist, les personnages, les icônes, les couleurs, le footer ou la pagination.
- Ne pas ajouter de texte parasite.

## Prompt complet

Cas d'usage : precise-object-edit.
Type d'actif : édition ciblée d'une slide de formation existante, paysage 16:9, exactement 1672 x 941 pixels.
Image 1 : cible d'édition. Préserver l'image entière à l'identique.
Demande principale : dans les quatre capsules colorées tout en bas, supprimer seulement les libellés `Présent`, `Valide`, `Non conforme` et `Indéterminé`. Conserver et centrer les quatre pictogrammes existants dans le même ordre : coche verte, coche bleue, croix orange, point d'interrogation gris.
Contraintes : préserver exactement le cartouche `VERDICT - Présent, valide, non conforme ou indéterminé`, tous les autres textes, toute la scène, le footer `Opquast - présentation Miweb` et la pagination `16 / 30`.
À éviter : suppression du cartouche, changement d'ordre, modification d'un pictogramme, ajout de texte, logo ou déplacement global.
