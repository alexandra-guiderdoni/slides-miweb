# Prompt ImageGen - slide 08 V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`
- `securite-opquast-v5-v4/source/etalons/slide-20.png`, étalon V4 le plus proche pour une inspection technique bornée

Ces cinq images sont fournies directement à ImageGen. Elles servent uniquement de références de masque, de hiérarchie, de respiration et de finition.

## Fiche PDS

- Rôle : montrer le premier contrôle complet.
- Idée principale : quatre preuves techniques doivent être inspectées sans conclure pour tout le service.
- Scène : une développeuse inspecte une interface centrale reliée à quatre encarts de preuve.
- Transformation visible : quatre observations produisent un contrôle borné par une limite explicite.
- Contraintes critiques : quatre preuves exactes, HSTS avec max-age, interface sans texte parasite.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française au format paysage 16:9, exactement 1672 x 941 pixels.

Suivre très fidèlement la direction artistique des cinq références fournies : fond ivoire presque blanc, bleu marine, panneaux bleu très clair, vert pour les contrôles positifs, orange pour la limite, corail uniquement pour la ressource HTTP refusée, illustration vectorielle plate, typographie française sans sérif proche de Marianne. Aucun dégradé, aucune photographie, aucune 3D, aucune ombre lourde, aucun faux logo.

Masque stable V4 : micro-entête en haut à gauche, petit repère `CONTRÔLE`, scène centrale ample, quatre encarts équilibrés, bande de limite orange pâle en bas, footer bas gauche, pagination bas droite.

Composition : placer une développeuse devant une grande interface abstraite sans caractères lisibles. Disposer quatre encarts autour de l'interface et les relier par des traits verts à des zones abstraites : pages et ressources en HTTPS, certificat signé et valide, entête HSTS avec max-age, aucune ressource HTTP. Le callout de limite occupe la largeur sous la scène. Aucun texte à l'intérieur de la fausse interface.

Texte visible exact, et absolument aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `CONTRÔLE`
- `197 - Pages et ressources en HTTPS`
- `198 - Certificat signé et valide`
- `199 - Strict-Transport-Security avec max-age`
- `200 - Aucune ressource chargée en HTTP`
- `LIMITE - Une page ne représente pas tout le service`
- `Opquast - présentation Miweb`
- `08 / 30`

Priorités de lecture : 1. les quatre preuves ; 2. l'interface inspectée ; 3. la limite.

Critères de rejet : faute dans `Strict-Transport-Security` ou `max-age`, valeur numérique ajoutée, texte interne à l'interface, HTTPS et HTTP confondus, preuve manquante, texte parasite, faux logo, mauvaise pagination.
