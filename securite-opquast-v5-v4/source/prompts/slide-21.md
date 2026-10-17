# Prompt ImageGen - slide 21 V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`
- `securite-opquast-v5-v4/source/etalons/slide-23.png` - étalon V4 le plus proche

Ces cinq images sont fournies directement à ImageGen. Reprendre leur grammaire visuelle, leur hiérarchie, leur respiration et leur niveau de finition sans recopier leur contenu.

## Fiche PDS

- Rôle : traiter la règle 211 après la protection XSS.
- Idée principale : une page doit décider explicitement qui peut l'intégrer dans un cadre.
- Scène : une page centrale accepte un cadre autorisé et refuse deux cadres tiers trompeurs.
- Transformation visible : trois tentatives d'intégration aboutissent à une décision autorisée ou refusée.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française au format paysage 16:9, exactement 1672 x 941 pixels.

Suivre très fidèlement les cinq références fournies : fond ivoire presque blanc, titre bleu marine massif, composition éditoriale aérée, aplats pastel doux, illustration vectorielle plate aux traits fins, formes organiques discrètes, typographie française sans sérif proche de Marianne. Aucun dégradé, photographie, effet 3D, ombre lourde ni faux logo.

Masque V4 stable : micro-entête en haut à gauche, repère `C - INSTRUCTIONS AU NAVIGATEUR` et badge de règle en haut, grand titre, mécanisme central, callout bleu clair, footer bas gauche et pagination bas droite.

Scène : une page web légitime au centre. Trois cadres tentent de l'intégrer. Un cadre autorisé vert est accepté, deux cadres tiers corail sont refusés par une barrière simple. Les deux mécanismes sont nommés dans deux cartouches techniques. Montrer le contrôle des domaines sans pirate ni cadenas dominant.

Texte visible exact, et absolument aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `RÈGLE 211`
- `Qui peut intégrer la page dans un cadre ?`
- `Autoriser explicitement ou interdire l'intégration`
- `X-Frame-Options`
- `CSP frame-ancestors`
- `CONTRÔLE - Vérifier que la politique limite réellement les domaines`
- `Opquast - présentation Miweb`
- `21 / 30`

Critères de rejet : texte manquant ou ajouté, faute, mauvais numéro ou pagination, faux domaine, code inventé, `ALLOW-FROM`, `SAMEORIGIN` ou `DENY`, promesse qu'un entête présent suffit, faux logo, composition éloignée des références.
