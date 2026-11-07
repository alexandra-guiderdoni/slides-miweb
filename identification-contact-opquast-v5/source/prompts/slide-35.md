# Prompt image_gen — slide 35 — tentative a002

Use case: productivity-visual.
Type d’actif : image finale 16:9 de la série identification-contact-opquast-v5.
Créer UNE slide raster complète en français, exactement 1672 × 941 px.
Source verrouillée : storyboard-v002.md S35, SHA-256 81944fb744f608a5f5f2dbe36b56b1febdc32ed50a0ffa283155667970b15894.
Image 1 : S35 a001 cible de correction ; image 2 : S01 ancre ; image 3 : S13 étalon.
## Reprise ciblée
Défaut observé : trois traits horizontaux imitant du texte dans la feuille sortant de l’enveloppe de la carte 6 ; huit petits traits imitant du texte dans le livre de la carte 8.
Invariant : huit cartes, chaque mot, numéro et signe ≠, positions, pictogrammes, masque, en-tête, footer et pagination.
Correction visuelle : effacer UNIQUEMENT les trois traits de la feuille de la carte 6 et les huit traits du livre de la carte 8, pour laisser une feuille vierge et les deux pages vierges du livre. Garder contours, plis et formes des pictogrammes.
Interdit : ne pas remplacer les traits par d’autres lignes, textes, symboles ou décorations ; ne changer aucune autre zone.
## Bloc de style commun
Fond blanc uni dominant. Illustration pédagogique plane, contours bleu marine réguliers de 3 px environ, aplats bleu très clair, gris froid, vert pâle pour les solutions, orange pour la vigilance ; rouge réservé aux erreurs. Ni texture, ni dégradé, ni ombre décorative, ni 3D. Typographie sans-serif institutionnelle proche de Marianne, Arial en alternative explicite, sans prétendre certifier une police. Grand titre marine centré, gras, casse de phrase, dans la zone y=112–235, deux lignes au maximum. En-tête dans les coins supérieurs, x=40 et x=1632, y=15–65 : première ligne environ 30 px, seconde environ 23 px. Contenu entre y=275 et y=835 ; marges de sécurité 40 px ; cartes arrondies et pictogrammes filaires homogènes. Footer marine discret de 23 px environ à x=34, ligne de base y=909 ; pagination à droite sur la même ligne. Le point médian U+00B7 du footer est petit et fin, jamais une grosse puce. Aucun personnage récurrent : les interfaces et objets portent le point de vue utilisateur. Direction de lecture gauche-droite, respiration entre les blocs. Conserver exactement ce masque commun ; seules les compositions narratives et les chaînes explicitement demandées changent.

En-tête exact haut gauche : QUALITÉ WEB (gras), puis EXPÉRIENCES DURABLES (normal).
En-tête exact haut droit : Opquast (gras), puis DES SITES MEILLEURS POUR TOUS (normal).
Un seul espace normal entre chaque mot. Même espacement que S01 ; pas d’espace élargi entre MEILLEURS et POUR.
Footer exact : RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
Aucun badge de règle ni d’acte. Aucun slogan sauf demande explicite dans le texte visible.

Pagination exacte : 35 / 42
Titre exact : Les huit confusions qui coûtent des points
Sous-titre visible : aucun.
Scène principale : huit paires d’objets différents, à ne pas confondre.
Storyboard : HUIT cartes, QUATRE colonnes sur DEUX rangées, ordre gauche-droite puis haut-bas. Chaque carte contient deux petits pictogrammes séparés par ≠ en haut, puis la relation exacte sur trois ou quatre lignes en grand corps, environ 29–32 px. Mettre chaque numéro avec son nom, ≠ seul entre les deux concepts si utile. Pictogrammes des huit paires : bâtiment/personne ; onglet site/page ; localisation+téléphone/deux bulles contact ; sablier/enveloppe ; enveloppe/écran ; demande enveloppe/réclamation bulle ; modérateur silhouette/bulle signalement ; livre référentiel/médaille label. Objets filaires très simples, sans mot ni trait de texte simulé. Paires 3 et 6 restent assez larges pour le texte entier. Palette pastel bleue/grise/verte régulière. Aucun titre de carte supplémentaire ; aucun badge.
Texte visible exact :
101 organisation ≠ 114 responsable
102 site ≠ 103 contenu
105 adresse, téléphone ≠ 107 deux moyens
108 délai ≠ 110 accusé
110 accusé ≠ 85 écran
110 demande ≠ 67 réclamation
113 modérateur ≠ 11 signalement
115 référentiel ≠ 64 label

## Liste blanche exhaustive des chaînes autorisées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Les huit confusions qui coûtent des points
- 101 organisation ≠ 114 responsable
- 102 site ≠ 103 contenu
- 105 adresse, téléphone ≠ 107 deux moyens
- 108 délai ≠ 110 accusé
- 110 accusé ≠ 85 écran
- 110 demande ≠ 67 réclamation
- 113 modérateur ≠ 11 signalement
- 115 référentiel ≠ 64 label
- ≠
- RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
- 35 / 42
Contraintes critiques : chaque chaîne lettre à lettre, accents, apostrophes typographiques, guillemets français, signes et numéros exacts ; footer petit point médian U+00B7. Les séparateurs entre cartes ne s’impriment pas. Les phrases complètes gardent leur ponctuation ; les énumérations en cartes n’ont pas de point final isolé sur leur dernier élément.
À éviter : texte hors liste blanche, pseudo-texte (barres imitant du texte comprises), corrigé d’exercice ajouté, coordonnées lisibles, adresse ou téléphone ou immatriculation, marque ajoutée, nom fictif hors fiche, notes orales, badge, navigation ajoutée, photographie, 3D, blob, gros dégradé, ombre décorative.
Rejet si : texte ajouté, manquant, déformé, rogné ou illisible ; relations inversées ; en-tête dont l’espace MEILLEURS → POUR dépasse max(autres espaces)+2 px ; footer ou pagination incorrects ; dimensions hors tolérance de 3 px.
Test des trois secondes : estimation par l’assistant, aucun test humain chronométré.
Point de vigilance : huit cartes exactement, chaque numéro associé au bon mot. Pas de point final sur la dernière carte.

