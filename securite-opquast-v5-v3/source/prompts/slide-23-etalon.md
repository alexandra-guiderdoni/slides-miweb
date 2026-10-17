# Prompt ImageGen - slide 23 - étalon de règle

## Fiche PDS

- Rôle dans la colonne vertébrale : expliquer l'empreinte d'intégrité avant de donner l'acronyme SRI.
- Idée principale : une origine autorisée ne garantit pas que le fichier reçu est resté inchangé.
- Scène : un navigateur reçoit un script tiers et compare son empreinte à celle annoncée dans la page.
- Personnage ou objet-système : navigateur comme poste de contrôle.
- Transformation visible : le fichier reçu entre, son empreinte est calculée, puis comparée à l'empreinte attendue.
- Ce que l'image seule doit faire comprendre : le fichier n'est accepté que si les deux empreintes correspondent.
- Préparation de la suite : prépare l'atelier de lecture du code source et des entêtes.
- Contraintes critiques : ne pas présenter SHA-384 comme un chiffrement ou une signature secrète ; conserver exactement l'attribut `integrity`.

## Prompt complet

Cas d'usage : scientific-educational.
Type d'actif : image finale de slide de formation, paysage 16:9, 1672 x 941 pixels.

Créer une slide institutionnelle française cohérente avec les séries Opquast Miweb : fond blanc, titre bleu marine aligné à gauche, bleu clair pour la structure, vert pour la correspondance validée, corail uniquement pour un fichier modifié refusé, icônes filaires, panneaux très clairs, typographie Marianne obligatoire avec Arial comme fallback. Aucun dégradé, aucune 3D, aucune photographie, aucun faux logo.

Composition : au centre, une chaîne visuelle simple de gauche à droite. À gauche, un petit serveur tiers envoie un fichier JavaScript. Au milieu, un navigateur calcule une empreinte représentée par un motif circulaire simple. À droite, deux empreintes visuellement identiques sont comparées et reliées par un signe égal vert. Sous la chaîne, montrer un court fragment HTML dans un cartouche monospace très lisible : `integrity="sha384-..."`. Ajouter un petit label qui nomme ensuite le mécanisme `SRI - Subresource Integrity`. Le callout bas rappelle que l'origine ne suffit pas.

Texte visible exact, et aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `C - INSTRUCTIONS AU NAVIGATEUR`
- `RÈGLE 214`
- `Vérifier le fichier exact, pas seulement son origine`
- `Fichier tiers reçu`
- `Empreinte reçue = empreinte attendue`
- `integrity="sha384-..."`
- `SRI - Subresource Integrity`
- `Une origine autorisée ne garantit pas un fichier inchangé.`
- `Opquast - présentation Miweb`
- `23 / 30`

Masque commun : titre et repère supérieur stables, chaîne principale au centre, callout bleu clair centré en bas, footer bas gauche et pagination bas droite.

Contraintes critiques : rendre le code court exactement ; ne pas écrire `sha256` ou `sha512` ; ne pas transformer SRI en chiffrement, certificat ou signature ; ne pas ajouter de clé, de secret, de fournisseur ou d'URL ; aucun texte parasite.
