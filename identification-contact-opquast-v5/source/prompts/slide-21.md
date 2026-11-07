# Prompt image_gen — slide-21-a002

Use case: precise-object-edit.
Type d’actif : image finale 16:9 de la série identification-contact-opquast-v5.
Créer UNE slide raster complète, exactement 1672 × 941 px. Une seule image.
Source verrouillée : storyboard-v002.md, S21, SHA-256 81944fb744f608a5f5f2dbe36b56b1febdc32ed50a0ffa283155667970b15894.
Image 1 : S01, ancre de série pour en-tête et footer. Image 2 : étalon de composition, style seulement, aucun texte à recopier.

## Bloc de style commun
Fond blanc uni dominant. Illustration pédagogique plane, contours bleu marine réguliers de 3 px environ, aplats bleu très clair, gris froid, vert pâle pour les solutions, orange pour la vigilance ; rouge réservé aux erreurs. Ni texture, ni dégradé, ni ombre décorative, ni 3D. Typographie sans-serif institutionnelle proche de Marianne, Arial en alternative explicite, sans prétendre certifier une police. Grand titre marine centré, gras, casse de phrase, dans la zone y=112–235, deux lignes au maximum. En-tête dans les coins supérieurs, x=40 et x=1632, y=15–65 : première ligne environ 30 px, seconde environ 23 px. Contenu entre y=275 et y=835 ; marges de sécurité 40 px ; cartes arrondies et pictogrammes filaires homogènes. Footer marine discret de 23 px environ à x=34, ligne de base y=909 ; pagination à droite sur la même ligne. Le point médian U+00B7 du footer est petit et fin, jamais une grosse puce. Aucun personnage récurrent : les interfaces et objets portent le point de vue utilisateur. Direction de lecture gauche-droite, respiration entre les blocs. Conserver exactement ce masque commun ; seules les compositions narratives et les chaînes explicitement demandées changent.

Titre exact : Adresse et téléphone à portée de chaque page
Sous-titre exact sous le titre : Acte 3 · Pouvoir joindre quelqu’un. Texte simple en graisse normale, comme S16 (image 2), aucune pastille. Badge R. 105 sous le titre aligné à droite, distinct du sous-titre. Image 2 : S16, référence impérative du sous-titre d’acte.
Scène principale : Trois pages schématiques côte à côte, avec des pictogrammes d’accueil, d’article et de panier pour les identifier sans texte ajouté. Chacune possède le même pied de page vert pâle, portant maison et téléphone, avec zones neutres sans coordonnées ni pseudo-texte. Les trois pages rendent visibles l’adresse et le téléphone accessibles partout. Au-dessus, la phrase exacte ; pas de flèches ni contact inventé. Aucun contenu simulé par des lignes dans les pages.
Storyboard : Trois pages schématiques côte à côte, avec des pictogrammes d’accueil, d’article et de panier pour les identifier sans texte ajouté. Chacune possède le même pied de page vert pâle, portant maison et téléphone, avec zones neutres sans coordonnées ni pseudo-texte. Les trois pages rendent visibles l’adresse et le téléphone accessibles partout. Au-dessus, la phrase exacte ; pas de flèches ni contact inventé. Aucun contenu simulé par des lignes dans les pages.
Texte visible exact :
Acte 3 · Pouvoir joindre quelqu’un.
Dans chaque page, ou à un clic depuis chaque page.

En-tête exact haut gauche sur deux lignes : QUALITÉ WEB en gras ; EXPÉRIENCES DURABLES en graisse normale.
En-tête exact haut droit sur deux lignes : Opquast en gras ; DES SITES MEILLEURS POUR TOUS en graisse normale.
Conserver l’en-tête corrigé de S01 : UN seul espace normal entre chaque mot, notamment MEILLEURS POUR, écart maximal de 2 px avec le plus grand autre espace.
Footer exact : RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
Pagination exacte : 21 / 42
Aucun slogan.

## Liste blanche exhaustive des chaînes autorisées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
- 21 / 42
- Adresse et téléphone à portée de chaque page
- Acte 3 · Pouvoir joindre quelqu’un.
- Dans chaque page, ou à un clic depuis chaque page.
- R. 105

Contraintes critiques : tous les mots visibles exacts, sans ajout ni retrait ; accents, apostrophes typographiques, guillemets français, tirets et numéros relus lettre à lettre. Les séparateurs de liste sont remplacés par la disposition ; pas de point final isolé sur le seul dernier élément d’une énumération en cartes. Conserver les points des phrases complètes. Footer : petit point médian U+00B7, jamais une puce. Coordonnées seulement en pictogrammes et zones neutres. Ne jamais remplacer un contenu attendu par un gabarit vide.
À éviter : texte parasite, pseudo-texte y compris barres ou lignes imitant des mots, notes orales, corrigé de checkpoint, badge d’acte, marque réelle ajoutée, logo inventé, nom fictif hors fiche, adresse, téléphone ou immatriculation lisibles, SIREN, photo, 3D, texture, gros dégradé, ombre décorative, blob, progression ajoutée, callout rouge.
Rejet si : faute, ajout, omission, inversion de sens ou numéro, texte coupé ou illisible, pseudo-texte, mauvais badge, footer ou pagination, espace MEILLEURS POUR excessif, masque incohérent, dimensions hors tolérance de 3 px. Test des trois secondes estimé par l’assistant ; aucun test humain chronométré.


## Reprise ciblée
Image 3 : candidates/slide-21-a001.png, CIBLE DE MODIFICATION. L’image 2 est S16 pour le sous-titre d’acte.
Défaut observé : trois traits horizontaux imitent du texte dans le pictogramme de document, au centre de la page du milieu.
Invariants : tous les textes, en-tête, titre, sous-titre, phrase, badge, footer et pagination ; les trois fenêtres, les pieds de page, les maisons, téléphones et zones neutres ; le contour extérieur et le coin replié du document central restent strictement identiques.
Correction visuelle : effacer UNIQUEMENT les trois traits horizontaux à l’intérieur de la petite feuille centrale (environ x=788–884, y=592–662), en laissant l’intérieur blanc sans autre objet. Garder la silhouette de feuille et son coin replié.
Interdit : ne pas remplacer les traits par d’autres signes ; ne pas modifier les fenêtres ou les textes. Aucun pseudo-texte dans la feuille. Aucune autre correction.

