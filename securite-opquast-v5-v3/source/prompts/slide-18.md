# Prompt ImageGen - slide 18

## Fiche PDS

- Rôle : distinguer déclaration du type et interdiction de le deviner.
- Scène : un fichier passe successivement par deux contrôles.
- Transformation : le serveur déclare le type, puis le navigateur reçoit l’ordre de ne pas improviser.
- Continuité : première comparaison du chapitre C et préparation des politiques de sécurité.
- Contrainte critique : ordre 207 puis 206, deux fonctions différentes.

## Prompt complet

Cas d’usage : scientific-educational.
Type d’actif : image finale de slide de formation, paysage 16:9, 1672 x 941 pixels.

Reprendre exactement le masque clair des étalons : fond blanc, en-tête haut gauche, chapitre discret, repère supérieur bleu clair, titre bleu marine, scène centrale, callout de contrôle bleu clair, capsule de limite orange, footer et pagination stables. Illustration plate, traits fins, bleu institutionnel, vert de validation. Marianne ou Arial en fallback. Aucun dégradé, aucune 3D, aucune photographie, aucun faux logo.

Composition : un fichier venant du serveur traverse deux portes successives de même taille. Première porte : le serveur déclare le bon type. Deuxième porte : le navigateur reçoit l’instruction `nosniff`. Une flèche linéaire montre que déclarer et empêcher de deviner sont complémentaires mais différents. En bas, contrôle et limite lisibles.

Texte visible exact, et aucun autre texte :

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

Contraintes critiques : conserver exactement `Content-Type`, `X-Content-Type-Options: nosniff` et le symbole `≠` ; ordre 207 puis 206 ; aucun texte parasite.
