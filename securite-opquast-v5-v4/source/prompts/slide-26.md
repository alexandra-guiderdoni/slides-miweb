# Prompt ImageGen - slide 26 V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`
- `securite-opquast-v5-v4/source/etalons/slide-20.png` - étalon V4 le plus proche

Ces cinq images sont fournies directement à ImageGen.

## Fiche PDS

- Rôle : montrer les deux contrôles pratiques du chapitre D.
- Idée principale : l'énumération de fichiers et la divulgation des technologies se vérifient séparément.
- Scène : deux panneaux égaux, répertoire à gauche et réponse HTTP à droite.
- Transformation visible : chaque observation conduit à un attendu distinct.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française au format paysage 16:9, exactement 1672 x 941 pixels.

Suivre très fidèlement les cinq références : fond ivoire presque blanc, titre bleu marine massif, composition aérée, aplats pastel doux, illustration vectorielle plate, typographie proche de Marianne. Aucun dégradé, photographie, effet 3D, ombre lourde ni faux logo.

Masque V4 stable : micro-entête haut gauche, repère de chapitre, grand titre, deux panneaux centraux égaux, limite orange très pâle, footer et pagination.

Scène : à gauche, un navigateur appelle un répertoire sans page d'index ; une liste abstraite barrée mène à un symbole d'erreur ou de redirection. À droite, une réponse HTTP est inspectée à la loupe ; tous ses contenus internes sont uniquement des traits abstraits sans lettres ni chiffres. Les noms `Server`, `X-Powered-By` et `X-AspNet-Version` apparaissent uniquement dans l'intitulé autorisé de la règle 213, jamais comme lignes internes.

Texte visible exact, et absolument aucun autre texte :

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

Critères de rejet : texte manquant ou ajouté, faute, mauvais numéro ou pagination, nom d'entête répété dans la fausse réponse HTTP, valeur, produit, URL ou fichier inventé, faux logo.
