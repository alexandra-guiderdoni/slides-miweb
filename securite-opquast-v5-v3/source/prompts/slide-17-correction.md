# Correction ImageGen - slide 17

## Défaut observé

- La silhouette humaine barrée suggère un refus d'utilisateur et ne représente pas clairement l'interdiction de deviner le type MIME.

## Invariants à préserver

- Conserver strictement toute la composition, les cinq autres pictogrammes, les six panneaux, les flèches, la fenêtre centrale, le personnage, les couleurs, les textes, le footer et la pagination.
- Conserver le panneau rose à gauche au milieu et son raccord rouge.
- Conserver le format exact 1672 x 941 pixels.

## Correction visuelle attendue

- Remplacer uniquement la silhouette barrée du panneau rose par un pictogramme non textuel clair : un fichier générique associé à une loupe, l'ensemble barré par le même symbole d'interdiction rouge.
- Le nouveau pictogramme doit signifier visuellement que le navigateur ne doit pas inspecter ou deviner le type du fichier.

## Interdits

- Aucun mot, acronyme, lettre, numéro ou symbole typographique dans le pictogramme.
- Ne pas modifier les cinq autres panneaux ni aucun texte existant.
- Ne pas ajouter de logo ou de texte parasite.

## Prompt complet

Cas d'usage : precise-object-edit.
Type d'actif : édition ciblée d'une slide de formation existante, paysage 16:9, exactement 1672 x 941 pixels.
Image 1 : cible d'édition. Préserver l'image entière à l'identique.
Demande principale : dans le panneau rose situé à gauche au milieu, remplacer uniquement la silhouette humaine barrée par un pictogramme filaire non textuel composé d'un fichier générique et d'une loupe, barrés par le même cercle rouge d'interdiction. Le sens attendu est `ne pas inspecter ou deviner le type du fichier`.
Contraintes : conserver le panneau, son fond rose, le cercle rouge, le raccord rouge, les cinq autres pictogrammes, tous les textes, le footer `Opquast - présentation Miweb` et la pagination `17 / 30`.
À éviter : personne barrée, texte, lettres, acronyme MIME, numéro, modification globale, logo.
