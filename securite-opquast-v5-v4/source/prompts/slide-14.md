# Prompt ImageGen - slide 14 V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`
- `securite-opquast-v5-v4/source/etalons/slide-23.png`, étalon V4 le plus proche pour un mécanisme en chaîne

Ces cinq images sont fournies directement à ImageGen.

## Fiche PDS

- Rôle : distinguer création d'un nouveau secret et interdiction de divulguer l'ancien.
- Scène : un lien temporaire mène à un nouveau formulaire tandis qu'une enveloppe ne contient jamais le secret.
- Transformation : récupérer le compte aboutit à un nouveau mot de passe, pas à la restitution de l'ancien.
- Contrainte critique : aucun mot de passe lisible.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française, paysage 16:9, exactement 1672 x 941 pixels.

Reprendre fidèlement le masque V4 : fond ivoire, micro-entête avec trait vert, repère de chapitre, badge de règles, grand titre bleu marine, scène vectorielle plate, panneaux pastel, contrôle bleu très clair, limite orange pâle, footer et pagination stables. Typographie proche de Marianne. Aucun dégradé, photographie, 3D, ombre lourde ou faux logo.

Composition : flux de gauche à droite. Une enveloppe contient uniquement un lien temporaire, puis une flèche mène à un formulaire où une personne crée un nouveau mot de passe abstrait. À côté, l'ancien secret est masqué et barré en corail. Le symbole `≠` reste central. Contrôle et limite forment deux cartouches alignés en bas.

Texte visible exact, et absolument aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `B - MAÎTRISE DU COMPTE`
- `RÈGLES 204 ET 205`
- `Réinitialiser n'est pas restituer l'ancien secret`
- `204 - Créer un nouveau mot de passe`
- `205 - Ne jamais envoyer le mot de passe en clair`
- `Réinitialiser ≠ restituer`
- `CONTRÔLE - Suivre la procédure sans être connecté et examiner le courriel reçu`
- `LIMITE - Ne jamais utiliser de compte réel ou de donnée personnelle dans la démonstration`
- `Opquast - présentation Miweb`
- `14 / 30`

Critères de rejet : secret lisible ; ancien secret présenté comme récupéré ; symbole `≠` absent ; texte parasite ; mauvais numéro ; mauvaise pagination.
