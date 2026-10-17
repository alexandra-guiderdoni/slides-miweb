# Prompt ImageGen - slide 20 - étalon d'éclairage

## Fiche PDS

- Rôle dans la colonne vertébrale : montrer qu'une ancienne réponse technique ne satisfait plus la règle 210.
- Idée principale : il faut contrôler une protection XSS actuelle et applicable, pas rechercher mécaniquement un ancien entête.
- Scène : une développeuse inspecte deux réponses serveur, rejette une ancienne fiche et conserve une politique CSP active.
- Personnage ou objet-système : poste d'inspection des entêtes HTTP.
- Transformation visible : ancien mécanisme barré, mécanisme actuel validé, puis contrôle explicite.
- Ce que l'image seule doit faire comprendre : la recherche de `X-XSS-Protection` est remplacée par la vérification d'une protection moderne.
- Préparation de la suite : ouvre la distinction avec l'encadrement et l'origine des contenus.
- Contraintes critiques : conserver exactement `X-XSS-Protection`, `Content-Security-Policy` et `RÈGLE 210`.

## Prompt complet

Cas d'usage : scientific-educational.
Type d'actif : image finale de slide de formation, paysage 16:9, 1672 x 941 pixels.

Créer une slide institutionnelle française cohérente avec les séries Opquast Miweb : fond blanc, titre bleu marine aligné à gauche, panneaux gris ou bleu très clair, risque corail, validation verte, icônes filaires, illustration plate, typographie Marianne obligatoire avec Arial comme fallback. Aucun dégradé, aucune 3D, aucune photographie, aucun faux logo.

Composition : en haut, repère de chapitre discret à gauche et badge `RÈGLE 210` à droite. Au centre, une développeuse devant un poste d'inspection compare deux cartes serveur. À gauche, une petite carte ancienne contenant `X-XSS-Protection`, barrée sobrement en corail et marquée `obsolète ou déprécié`. À droite, une carte actuelle contenant `Content-Security-Policy`, transmise vers un navigateur et validée en vert. Une flèche claire va de l'ancienne carte vers la politique actuelle. En bas, un callout bleu clair donne le contrôle à effectuer. La scène doit montrer un remplacement de pratique, pas une équivalence entre les deux mécanismes.

Texte visible exact, et aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `RÈGLE 210`
- `La règle 210 ne demande plus X-XSS-Protection`
- `Protection explicite contre les attaques XSS`
- `X-XSS-Protection - obsolète ou déprécié`
- `Content-Security-Policy active`
- `CONTRÔLE - Vérifier un mécanisme transmis et applicable`
- `Opquast - présentation Miweb`
- `20 / 30`

Masque commun : titre et repère supérieur stables, callout de contrôle centré en bas, footer bas gauche, pagination bas droite. Le callout reste bleu clair, jamais rouge.

Contraintes critiques : ne pas présenter `X-XSS-Protection` comme recommandé ; ne pas écrire `XSS-Protection` sans le premier `X-` ; ne pas remplacer `Content-Security-Policy` par une autre expression ; ne pas suggérer que la présence de CSP prouve à elle seule son efficacité ; aucun texte parasite, aucun code long, aucun fournisseur, aucun logo.
