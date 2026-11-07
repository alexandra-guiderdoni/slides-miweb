# Prompt image_gen — slide 39 — tentative a002

Use case: precise-object-edit.
Type d’actif : image finale 16:9 de la série identification-contact-opquast-v5.
Créer UNE slide raster complète en français, exactement 1672 × 941 px, paysage.
Source verrouillée : storyboard-v002.md, S39 ; S38 lue pour la scène commune explicitement requise par S39. SHA-256 81944fb744f608a5f5f2dbe36b56b1febdc32ed50a0ffa283155667970b15894.
Image 1 : S39 a001, cible de modification. Image 2 : S01 proposée VALIDEE_PRODUCTION, ancre de série ; reprendre son en-tête, sa typographie, footer, marges et palette ; ni ses textes de corps, ni son slogan, ni sa pagination, ni son sujet.

## Reprise ciblée — cadre du skill de génération
Défaut observé : ajout du mot « Contact » dans la page centrale ; enveloppe dans la boîte annoncée vide ; trois barres de texte simulé dans le mail.
Invariants à préserver : dimensions, masque, titre, sept étiquettes vertes et leurs textes exacts, sept pastilles, positions des objets et traits de liaison, onglets, code, formulaire, pied de page, en-tête, footer, pagination. Toute la scène reste identique.
Correction visuelle attendue : dans l’image 1, effacer seulement le mot « Contact » en laissant le fond blanc à cette place ; effacer seulement l’enveloppe dans le corps de la boîte de réception pour laisser ce corps réellement vide, tout en préservant son titre ; effacer seulement les trois barres bleues dans le corps du mail pour laisser un fond blanc sans lignes sous son titre. Ne pas remplir ces espaces par d’autres objets ou textes.
Interdit : ne déplacer ni redimensionner aucun élément ; ne pas ajouter un label de substitution, une enveloppe barrée, un message d’absence, des traits simulant des mots, un texte ou un numéro ; ne pas toucher aux sept corrections. Les zones neutres de coordonnées à côté des pictogrammes de localisation et téléphone doivent rester.

## Bloc de style commun
Fond blanc uni dominant. Illustration pédagogique plane, contours bleu marine réguliers de 3 px environ, aplats bleu très clair, gris froid, vert pâle pour les solutions, orange pour la vigilance ; rouge réservé aux erreurs. Ni texture, ni dégradé, ni ombre décorative, ni 3D. Typographie sans-serif institutionnelle proche de Marianne, Arial en alternative explicite, sans prétendre certifier une police. Grand titre marine centré, gras, casse de phrase, dans la zone y=112–235, deux lignes au maximum. En-tête dans les coins supérieurs, x=40 et x=1632, y=15–65 : première ligne environ 30 px, seconde environ 23 px. Contenu entre y=275 et y=835 ; marges de sécurité 40 px ; cartes arrondies et pictogrammes filaires homogènes. Footer marine discret de 23 px environ à x=34, ligne de base y=909 ; pagination à droite sur la même ligne. Le point médian U+00B7 du footer est petit et fin, jamais une grosse puce. Aucun personnage récurrent : les interfaces et objets portent le point de vue utilisateur. Direction de lecture gauche-droite, respiration entre les blocs. Conserver exactement ce masque commun ; seules les compositions narratives et les chaînes explicitement demandées changent.

Titre exact : Correction du grand cas : sept repères, huit règles
Titre centré sur deux lignes au maximum. Aucun sous-titre. Aucun badge de règle ni d’acte. Les numéros de règles sont du texte dans les repères, sans cartouche distinct.

Scène principale : un parcours de contact, son onglet, sa page et ses e-mails ; sept repères rattachent sept défauts à huit règles.
Storyboard : composition frontale reproductible, sans perspective, avec trois zones. En haut du corps, barre d’onglets dont l’onglet actif affiche « Page » près d’une icône générique ; à côté, petit panneau de code affichant uniquement <head> et </head> sur deux lignes, rien entre ces balises, donc aucun appel d’icône. Au centre-gauche, grande page Contact schématique : formulaire aux champs rectangulaires vides, aucune mention de délai ; pied de page avec un pictogramme de localisation et un de téléphone sur des zones neutres sans coordonnées lisibles ; petit bloc d’assistance et mention de référentiel non soulignée. À droite, en haut boîte de réception vide, en bas e-mail sans contact. Les zones de base restent distinctes et autonomes des corrections vertes, pour que la future S38 conserve la même scène après retrait des étiquettes vertes et repères. Aucun texte de correction ne doit recouvrir les objets.

Disposition conseillée des sept repères : 1 près de l’onglet ; 2 près du panneau de code ; 3 près de l’assistance ; 4 près du formulaire ; 5 près de la mention de référentiel ; 6 près de la boîte vide ; 7 près du mail sans contact. Sept petites pastilles vertes numérotées 1 à 7, chacune reliée par un trait fin à une étiquette vert très pâle portant la relation exacte ci-dessous. Numéros et flèches intégrés au texte de chaque étiquette, sans badge de règle. Ne pas créer une huitième pastille : le premier repère concerne deux règles.
Garder le texte des sept étiquettes de 26 à 30 px environ, avec retours à la ligne si besoin ; le texte de scène peut être 21–23 px. Tout doit rester lisible sur la slide de 1672 px. Lecture de gauche à droite, pas d’entrelacs de traits.

Texte visible exact des sept étiquettes, dans cet ordre :
1. Onglet « Page » → 102 et 103
2. Aucun appel d’icône → 104
3. Surtaxé, sans horaires ni tarif → 109
4. Aucun délai → 108
5. Référentiel sans lien → 115
6. Aucun accusé → 110
7. E-mail sans contact → 111

Textes du fond de scène, repris mot pour mot de S38 pour matérialiser la composition commune imposée par S39, pas de nouveau commentaire pédagogique :
- Page (onglet actif, sans guillemets ajoutés)
- <head> puis </head> (extrait sans link, grand et très simple)
- Assistance : numéro surtaxé
- Site conforme au référentiel X (non souligné, pas d’icône de lien)
- Boîte de réception : vide
- E-mail : « Ne pas répondre »
Ne pas imprimer « Trouvez sept défauts. », qui appartient à la consigne de S38 et pas à sa scène.

En-tête exact haut gauche :
QUALITÉ WEB
EXPÉRIENCES DURABLES
En-tête exact haut droit :
Opquast
DES SITES MEILLEURS POUR TOUS
Footer exact : RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
Pagination exacte : 39 / 42
Aucun slogan.

## Liste blanche exhaustive des chaînes autorisées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Correction du grand cas : sept repères, huit règles
- 1. Onglet « Page » → 102 et 103
- 2. Aucun appel d’icône → 104
- 3. Surtaxé, sans horaires ni tarif → 109
- 4. Aucun délai → 108
- 5. Référentiel sans lien → 115
- 6. Aucun accusé → 110
- 7. E-mail sans contact → 111
- 1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7 (pastilles correspondantes)
- Page
- <head>
- </head>
- Assistance : numéro surtaxé
- Site conforme au référentiel X
- Boîte de réception : vide
- E-mail : « Ne pas répondre »
- RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
- 39 / 42

Contraintes critiques : sept relations intégrales, aucune correction reformulée ; règle 102 ET 103 ensemble au premier repère ; 104 code sans appel d’icône et non simple icône absente ; 109 horaires ET tarif absents ; 108 délai absent ; 115 mention sans lien ; 110 accusé absent ; 111 mail sans contact. Ne pas déclarer 101, 105, 106, 107 ou 114 en erreur. Adresse et téléphone restent matérialisés par pictogrammes et zones neutres, pas effacés du fond de scène. La boîte vide et le mail sans contact sont deux objets distincts, à deux moments du parcours. La mention « Site conforme au référentiel X » est une déclaration fictive défectueuse de la scène, jamais une certification de cette slide. Conserver apostrophe typographique de d’icône, guillemets « », accents, flèche et tous les chiffres exacts. Footer petit point médian « · » U+00B7.
À éviter : texte parasite, ajout de diagnostic, numéro lisible de téléphone ou d’immatriculation, adresse, SIREN, marque réelle ajoutée, nom fictif ajouté, code link, faux logo, badge de règle, badge d’acte, slogan, titre S38, notes orales, fil d’Ariane, barre de progression, huitième repère, photo, 3D, blob, texture, gros dégradé, ombre décorative, callout rouge, fond sombre dominant.
Rejet si : repère manquant ou doublonné, numéro faux, règle associée au mauvais objet, code contenant un appel d’icône, repère 1 privé de l’une des deux règles, mot manquant ou déformé, texte ajouté hors liste blanche, scène impossible à reproduire sans les corrections, coordonnées lisibles, texte illisible ou coupé, footer/pagination inexact, dimensions hors tolérance de 3 px. Test rapide estimé par l’assistant ; aucune prétention de test humain chronométré.
