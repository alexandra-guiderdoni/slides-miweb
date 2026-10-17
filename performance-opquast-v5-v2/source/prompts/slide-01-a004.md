# Prompt image_gen - slide 01, tentative a004

Générer une seule slide raster complète en français, texte compris, sur un canevas paysage 16:9 de 1672 x 941 px.

## Défaut observé

La version précédente montre un échange entre un serveur et un terminal, mais elle n’explique pas clairement que les choix techniques effectués côté serveur causent un coût d’usage côté utilisateur. Le verbe « paie » peut en outre être compris comme un coût financier.

## Invariants à préserver

- Conserver le masque commun de la slide de référence : fond blanc, grille, marges, palette, en-têtes, footer et pagination.
- Conserver le style d’infographie institutionnelle, les traits nets, les aplats pastel légers et les ombres faibles.
- Conserver le serveur à gauche et le côté utilisateur à droite.
- Produire une slide complète, sans surimpression ni ajout ultérieur de texte.

## Correction visuelle attendue

- Montrer une relation causale unique de gauche à droite.
- À gauche : un serveur sobre associé au libellé `SERVEUR` et à une petite carte `CHOIX TECHNIQUES`.
- Au centre : une seule flèche orientée vers la droite, libellée `RESSOURCES TRANSMISES`.
- À droite : une personne utilisant un ordinateur portable, associée au libellé `UTILISATEUR`.
- Autour de l’utilisateur : trois pictogrammes clairement rattachés à la personne et au terminal, libellés `TEMPS`, `DONNÉES` et `CALCUL`.
- Ce que l’image seule doit faire comprendre : les décisions prises côté serveur déterminent des ressources transmises dont le coût est supporté côté utilisateur.

## Texte exact et exhaustif

1. Les choix du serveur ont un coût côté utilisateur
2. SERVEUR
3. CHOIX TECHNIQUES
4. RESSOURCES TRANSMISES
5. UTILISATEUR
6. TEMPS
7. DONNÉES
8. CALCUL
9. Quels coûts inutiles pouvons-nous éviter à l’utilisateur ?
10. QUALITÉ WEB
11. EXPÉRIENCES DURABLES
12. Opquast
13. DES SITES MEILLEURS POUR TOUS
14. RÈGLES OPQUAST · PERFORMANCE
15. 01 / 35

Reproduire exactement les accents, apostrophe, capitales, point médian et pagination. N’ajouter aucun autre mot, lettre, chiffre, pseudo-texte, symbole monétaire ou marque.

## Direction visuelle

- Titre bleu marine, centré et immédiatement lisible.
- Scène principale organisée comme une chaîne causale de gauche à droite.
- `CHOIX TECHNIQUES` doit être clairement rattaché au serveur.
- `TEMPS`, `DONNÉES` et `CALCUL` doivent être clairement rattachés à l’utilisateur, pas au serveur.
- Placer la question `Quels coûts inutiles pouvons-nous éviter à l’utilisateur ?` dans l’encadré bleu clair inférieur.
- En haut à gauche : `QUALITÉ WEB`, puis `EXPÉRIENCES DURABLES`.
- En haut à droite : `Opquast`, puis `DES SITES MEILLEURS POUR TOUS`.
- En bas : footer `RÈGLES OPQUAST · PERFORMANCE` et pagination `01 / 35`.
- Marges de sécurité : 72 px minimum.

## Interdits

- Ne pas utiliser de double flèche ni de flèche orientée vers le serveur.
- Ne pas représenter de pièce, billet, portefeuille, paiement ou échange marchand.
- Ne pas faire flotter les mots `TEMPS`, `DONNÉES` et `CALCUL` entre le serveur et l’utilisateur.
- Ne pas ajouter de texte dans l’écran du terminal, dans le serveur ou dans les pictogrammes.
- Ne pas modifier les en-têtes, le footer ou la pagination.
- Rejeter toute faute, mauvais numéro, texte parasite, faux logo, photo, 3D, gros dégradé, texture, watermark ou relation visuelle ambiguë.
