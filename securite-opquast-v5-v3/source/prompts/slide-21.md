# Prompt ImageGen - slide 21

## Fiche PDS

- Rôle dans la colonne vertébrale : traiter la règle 211 après la protection XSS.
- Idée principale : une page doit décider explicitement qui peut l'intégrer dans un cadre.
- Scène : une page centrale accepte un cadre autorisé et refuse deux cadres tiers trompeurs.
- Objet-système : fenêtre de navigateur placée dans un poste de contrôle des cadres.
- Transformation visible : trois tentatives d'intégration convergent vers une décision autorisée ou refusée.
- Ce que l'image seule doit faire comprendre : l'intégration de la page est limitée à des domaines définis.
- Préparation de la suite : distingue les cadres des autres ressources chargées.
- Contraintes critiques : règle 211 exacte, deux mécanismes exacts, contrôle lisible, aucun faux domaine.

## Prompt complet

Cas d'usage : scientific-educational.
Type d'actif : image finale de slide de formation, paysage 16:9, 1672 x 941 pixels.

Créer une slide institutionnelle française reprenant exactement le masque clair des étalons validés Sécurité Opquast V5 V3 : fond blanc dominant, petit bandeau supérieur, grand titre bleu marine aligné à gauche, badge de règle bleu clair en haut à droite, panneaux pastel très clairs, illustrations plates, traits fins, beaucoup d'espace blanc, callout bleu clair centré en bas, footer bas gauche et pagination bas droite. Typographie Marianne obligatoire, Arial seulement comme fallback. Aucun dégradé, aucune 3D, aucune photographie, aucune ombre lourde, aucun logo.

Composition : au centre, une page web légitime dans une fenêtre de navigateur. Trois cadres tentent de l'intégrer. Un cadre autorisé en bleu ou vert est accepté. Deux cadres tiers en corail sont refusés par un bouclier ou une barrière simple. Au-dessus des décisions, deux petits cartouches techniques nomment `X-Frame-Options` et `CSP frame-ancestors`. Montrer visuellement le contrôle des domaines, sans cadenas géant ni pirate. Le callout inférieur contient le contrôle exact.

Texte visible exact, et aucun autre texte :

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

Contraintes critiques : respecter chaque accent et chaque numéro ; ne pas inventer d'URL ou de nom de domaine ; ne pas ajouter `ALLOW-FROM`, `SAMEORIGIN`, `DENY` ni de code ; ne pas présenter la seule présence d'un entête comme une preuve d'efficacité ; aucun texte parasite.
