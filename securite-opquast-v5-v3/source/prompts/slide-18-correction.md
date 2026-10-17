# Correction ImageGen - slide 18

## Défaut observé

- Les deux portes ne portent que les numéros et les noms techniques, sans les deux libellés complets exigés.
- Après la première correction, les badges autonomes `207` et `206` répètent inutilement les numéros déjà présents dans les formulations complètes.

## Invariants à préserver

- Conserver strictement le titre, le chapitre, le serveur, le fichier, les deux portes, les flèches, la fenêtre finale, le callout, les encadrés de contrôle et de limite, le footer et la pagination.
- Conserver l'ordre : règle 207 à gauche, puis règle 206 à droite.
- Conserver le format exact 1672 x 941 pixels.

## Correction visuelle attendue

- Remplacer uniquement le texte intérieur de la porte gauche par `207 - Le serveur déclare le bon Content-Type`.
- Remplacer uniquement le texte intérieur de la porte droite par `206 - Le navigateur reçoit X-Content-Type-Options: nosniff`.
- Répartir chaque libellé sur plusieurs lignes lisibles, sans modifier aucun caractère.
- Supprimer les deux badges autonomes `207` et `206` placés au-dessus des formulations complètes et laisser un espace blanc propre à leur emplacement.

## Interdits

- Ne pas abréger, reformuler, tronquer ou dupliquer les deux libellés.
- Ne pas inverser 207 et 206.
- Ne pas conserver de numéro autonome au-dessus des portes.
- Ne modifier aucun autre élément et ne pas ajouter de texte parasite.

## Prompt complet

Cas d'usage : text-localization.
Type d'actif : édition ciblée d'une slide de formation existante, paysage 16:9, exactement 1672 x 941 pixels.
Image 1 : cible d'édition. Préserver l'image entière à l'identique.
Demande principale : remplacer seulement les textes à l'intérieur des deux portes centrales par deux libellés complets, lisibles et exacts.
Texte exact de la porte gauche : `207 - Le serveur déclare le bon Content-Type`.
Texte exact de la porte droite : `206 - Le navigateur reçoit X-Content-Type-Options: nosniff`.
Supprimer uniquement les deux badges autonomes `207` et `206` situés au-dessus de ces formulations, puis laisser un espace blanc propre à leur emplacement.
Contraintes : ordre gauche vers droite 207 puis 206 ; conserver chaque caractère, les tirets simples, les deux-points et `nosniff` en minuscules ; répartir sur plusieurs lignes si nécessaire ; ne conserver aucun numéro autonome ; préserver tous les autres textes, la composition, le footer `Opquast - présentation Miweb` et la pagination `18 / 30`.
À éviter : ancien texte partiel, badge autonome, abréviation, inversion, faute dans `Content-Type`, faute dans `X-Content-Type-Options: nosniff`, modification globale, logo ou texte parasite.
