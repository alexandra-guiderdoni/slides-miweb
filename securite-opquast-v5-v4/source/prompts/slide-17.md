# Prompt ImageGen - slide 17 V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`
- `securite-opquast-v5-v4/source/etalons/slide-01.png`, étalon V4 le plus proche pour l'ouverture d'un chapitre

Ces cinq images sont fournies directement à ImageGen.

## Fiche PDS

- Rôle : ouvrir le chapitre C par le risque d'instructions inadaptées données au navigateur.
- Scène : un navigateur central reçoit six consignes distinctes.
- Transformation : les ressources incontrôlées deviennent six points de contrôle explicites.
- Contrainte critique : six consignes distinctes, aucune équivalence implicite.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française, paysage 16:9, exactement 1672 x 941 pixels.

Reprendre fidèlement le masque V4 : fond ivoire, micro-entête avec trait vert, grand repère de chapitre, badge des règles en haut à droite, grand titre bleu marine, panneaux pastel et scène centrale ample, footer et pagination stables. Illustration plate, bleu pour la structure, corail pour un contenu refusé, vert pour une consigne acceptée. Typographie proche de Marianne. Aucun dégradé, photographie, 3D, ombre lourde ou faux logo.

Composition : navigateur central relié à six consignes purement visuelles : type déclaré, interdiction de deviner, protection XSS, encadrement, origines autorisées, intégrité. Les six repères sont équilibrés et sans texte interne. Montrer que le navigateur reçoit des règles avant d'interpréter, charger ou exécuter.

Texte visible exact, et absolument aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `Chapitre C : dire au navigateur ce qu'il peut accepter`
- `Déclarer la nature, les sources, les cadres et l'intégrité.`
- `206 · 207 · 210 · 211 · 212 · 214`
- `Opquast - présentation Miweb`
- `17 / 30`

Critères de rejet : septième consigne ; règle absente, répétée ou erronée ; texte technique parasite ; URL ; fournisseur ; logo ; mauvaise pagination.
