# Prompt image_gen - slide 17, tentative a002

## Fiche PDS

- Rôle dans la progression : distinguer une page visible d’une page réellement utilisable après la distinction entre temps d’affichage et volume transféré.
- Idée principale : l’apparition de la page ne marque pas nécessairement le moment où l’utilisateur peut agir.
- Scène : une même interface web est observée à deux moments, séparés par des traitements encore actifs.
- Objet-système : deux représentations cohérentes de la même page web, reliées par une zone de traitements.
- Transformation visible : l’utilisateur passe de `JE VOIS` à `JE PEUX AGIR`.
- Masque commun : marque en haut, grand titre centré, contenu principal horizontal, cartouche final, pied de page et pagination identiques à la série.
- Ce que l’image seule doit faire comprendre : une page peut être visible avant d’être utilisable.
- Ajout à la slide précédente : après avoir séparé temps d’affichage et volume transféré, montrer que le temps d’affichage ne suffit pas non plus à décrire la disponibilité des interactions.
- Préparation de la suivante : introduire la maîtrise laissée à l’utilisateur avant de consommer des données.
- Risque à éviter : présenter téléchargement, affichage et calcul comme un processus officiel strictement séquentiel.

## Prompt complet

Cas d’usage : infographic-diagram.

Type d’actif : image finale complète d’une slide institutionnelle française, paysage 16:9, 1672 x 941 pixels.

Image de référence : la slide 17 actuelle sert uniquement de référence pour le masque, la palette, la typographie, la marque, le pied de page et la pagination. Recomposer entièrement le contenu central.

Demande principale : remplacer la chaîne actuelle à quatre cartes par une progression pédagogique en trois états. À gauche, montrer une page web déjà visible. Au centre, montrer des traitements encore actifs. À droite, montrer la même page devenue utilisable. L’idée doit être comprise immédiatement : voir la page ne signifie pas encore pouvoir agir.

Style et masque à préserver :

- fond blanc dominant et espace blanc généreux ;
- bleu marine institutionnel pour la structure, bleu clair pour l’état visible, orange pâle pour les traitements et vert discret pour l’état utilisable ;
- typographie Marianne, avec Arial comme seul fallback ;
- formes plates, cartes sobres, bordures fines et ombres très faibles ;
- `QUALITÉ WEB` puis `EXPÉRIENCES DURABLES` en haut à gauche ;
- `Opquast` puis `DES SITES MEILLEURS POUR TOUS` en haut à droite ;
- pied de page `RÈGLES OPQUAST · PERFORMANCE` en bas à gauche ;
- pagination `17 / 32` en bas à droite ;
- aucun faux logo, aucun emblème, aucune photo, aucune 3D et aucun filigrane.

Composition centrale :

- grand titre centré en haut : `Affiché ne veut pas dire utilisable` ;
- à gauche, une grande carte bleu clair contenant une fenêtre de navigateur générique déjà visible, avec le libellé `PAGE VISIBLE` et le statut `JE VOIS` ;
- au centre, une carte orange pâle plus étroite contenant un engrenage et un indicateur d’activité, avec le libellé `TRAITEMENTS EN COURS` ;
- à droite, une grande carte vert clair contenant la même fenêtre de navigateur, avec un bouton actif et un pointeur, le libellé `PAGE UTILISABLE` et le statut `JE PEUX AGIR` ;
- relier les trois états par une progression horizontale simple, sans faire croire à une chronologie technique exhaustive ;
- cartouche vert discret centré au-dessus du pied de page : `MESURER JUSQU’À L’INTERACTION` ;
- aucun autre texte dans les fenêtres de navigateur.

Liste blanche exacte des seuls textes visibles :

1. Affiché ne veut pas dire utilisable
2. PAGE VISIBLE
3. JE VOIS
4. TRAITEMENTS EN COURS
5. PAGE UTILISABLE
6. JE PEUX AGIR
7. MESURER JUSQU’À L’INTERACTION
8. QUALITÉ WEB
9. EXPÉRIENCES DURABLES
10. Opquast
11. DES SITES MEILLEURS POUR TOUS
12. RÈGLES OPQUAST · PERFORMANCE
13. 17 / 32

Contraintes critiques :

- reproduire chaque texte exactement, accents, apostrophes, capitales, points médians et pagination compris ;
- représenter la même page web à gauche et à droite avec une structure reconnaissable ;
- ne placer aucun texte supplémentaire dans les fenêtres de navigateur ;
- ne pas ajouter de valeur numérique, de durée, de score, de pourcentage ou de seuil ;
- ne pas afficher `Téléchargement`, `Affichage`, `Calcul`, `Interface utilisable` ni `AVANT D’AGIR` ;
- ne pas présenter le schéma comme un processus officiel Opquast ou une règle individuelle ;
- aucun texte hors liste blanche, aucune légende minuscule et aucun pseudo-texte ;
- lecture compréhensible en trois secondes ;
- marges de sécurité de 72 pixels minimum ;
- une slide raster complète, sans ajout de texte après génération.

Critères de rejet : faute, numéro erroné, texte parasite, mot tronqué, valeur inventée, deux interfaces différentes, séquence technique ambiguë, marque déformée, pagination incorrecte ou contenu central illisible.
