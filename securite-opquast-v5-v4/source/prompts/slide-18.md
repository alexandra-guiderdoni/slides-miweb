# Prompt ImageGen - slide 18 V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`
- `securite-opquast-v5-v4/source/etalons/slide-23.png`, étalon V4 le plus proche pour un mécanisme technique séquentiel

Ces cinq images sont fournies directement à ImageGen.

## Fiche PDS

- Rôle : distinguer déclaration du type et interdiction de le deviner.
- Scène : un fichier traverse deux contrôles successifs.
- Transformation : le serveur déclare le type, puis le navigateur reçoit l'ordre de ne pas improviser.
- Contrainte critique : ordre 207 puis 206 et fonctions différentes.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française, paysage 16:9, exactement 1672 x 941 pixels.

Reprendre fidèlement le masque V4 : fond ivoire, micro-entête avec trait vert, repère de chapitre, badge de règles, grand titre bleu marine, mécanisme central lisible, contrôle bleu très clair, limite orange pâle, footer et pagination stables. Illustration plate aux traits fins, bleu institutionnel et vert de validation. Typographie proche de Marianne. Aucun dégradé, photographie, 3D, ombre lourde ou faux logo.

Composition : un fichier abstrait venant du serveur traverse deux portes de même taille. Première porte : le serveur déclare le bon type. Deuxième porte : le navigateur reçoit l'instruction `nosniff`. Une flèche linéaire montre deux fonctions complémentaires mais différentes. Aucun numéro autonome au-dessus des portes.

Texte visible exact, et absolument aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `Type MIME : déclarer et ne pas deviner`
- `207 - Le serveur déclare le bon Content-Type`
- `206 - Le navigateur reçoit X-Content-Type-Options: nosniff`
- `Déclarer ≠ empêcher de deviner`
- `CONTRÔLE - Inspecter les entêtes de plusieurs types de ressources`
- `LIMITE - La présence de Content-Type ne prouve pas que sa valeur est correcte`
- `Opquast - présentation Miweb`
- `18 / 30`

Critères de rejet : faute dans `Content-Type` ou `X-Content-Type-Options: nosniff` ; ordre inversé ; numéro autonome ; symbole `≠` absent ; texte parasite ; mauvaise pagination.
