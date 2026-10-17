# Prompt ImageGen - slide 26

## Fiche PDS

- Rôle dans la colonne vertébrale : montrer les deux contrôles pratiques du chapitre D.
- Idée principale : l'énumération de fichiers et la divulgation des technologies se vérifient séparément.
- Scène : une URL de répertoire est testée à gauche et une réponse HTTP inspectée à droite.
- Objet-système : poste de contrôle en deux panneaux.
- Transformation visible : chaque observation aboutit à un résultat attendu distinct.
- Ce que l'image seule doit faire comprendre : une erreur ou redirection remplace la liste, et les entêtes ne révèlent pas les technologies.
- Préparation de la suite : ferme l'exposition serveur et conduit à la confiance hors de la page.
- Contraintes critiques : trois noms d'entêtes exacts, aucun exemple de valeur, limite entière lisible.

## Prompt complet

Cas d'usage : scientific-educational.
Type d'actif : image finale de slide de formation, paysage 16:9, 1672 x 941 pixels.

Créer une slide institutionnelle française reprenant exactement le masque clair des étalons validés Sécurité Opquast V5 V3 : fond blanc dominant, petit bandeau supérieur, grand titre bleu marine aligné à gauche, repère de chapitre bleu clair, panneaux pastel très clairs, illustrations plates, traits fins, beaucoup d'espace blanc, callout orange très pâle pour la limite, footer bas gauche et pagination bas droite. Typographie Marianne obligatoire, Arial seulement comme fallback. Aucun dégradé, aucune 3D, aucune photographie, aucune ombre lourde, aucun logo.

Composition : deux panneaux de même taille. À gauche, règle 209 : un navigateur appelle un répertoire sans page d'index ; une liste de fichiers est barrée et remplacée par un symbole d'erreur ou de redirection. À droite, règle 213 : une réponse HTTP est examinée à la loupe ; les trois noms d'entêtes sont visibles, mais aucune valeur technique n'est révélée. Un callout inférieur porte la limite exacte.

Texte visible exact, et aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `D - EXPOSITION MINIMALE`
- `Contrôler ce que le serveur révèle`
- `209 - Appeler un répertoire sans page d'index`
- `Attendu - erreur ou redirection, jamais la liste des fichiers`
- `213 - Inspecter Server, X-Powered-By et X-AspNet-Version`
- `Attendu - aucune information sur les logiciels et langages`
- `LIMITE - Un répertoire et une réponse ne prouvent pas la configuration globale`
- `Opquast - présentation Miweb`
- `26 / 30`

Contraintes critiques : conserver exactement `Server`, `X-Powered-By` et `X-AspNet-Version` ; ne pas ajouter de valeur d'entête, de produit, d'URL ou de nom de fichier ; ne pas montrer une liste de fichiers comme résultat attendu ; aucun texte parasite.
