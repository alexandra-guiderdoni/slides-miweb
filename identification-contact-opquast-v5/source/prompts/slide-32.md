# Prompt image_gen — slide 32 — tentative a002

Use case: productivity-visual.
Type d’actif : image finale 16:9 de la série identification-contact-opquast-v5.
Créer UNE slide raster complète en français, exactement 1672 × 941 px, paysage.
Source verrouillée : storyboard-v002.md S32 ; SHA-256 81944fb744f608a5f5f2dbe36b56b1febdc32ed50a0ffa283155667970b15894.
Image 1 : S32 a001, cible de correction ; image 2 : S01, ancre de série ; image 3 : S13, étalon triptyque.

## Reprise ciblée
Défaut observé : deux petites barres latérales et un rectangle gris sans fonction dans la boîte de réception de la carte A.
Invariant : tous les textes, en-tête, footer, pagination, bandeau, positions et objets des cartes B et C, palette et dimensions.
Correction visuelle : dans l’écran de la carte A seulement, effacer les deux petites barres bleues de la colonne latérale et le rectangle gris en haut du corps. Laisser ces zones vides sur leur fond actuel. Garder l’enveloppe de navigation et les limites de l’interface. La boîte de réception doit avoir un corps vide sans aucune ligne ou barre.
Interdit : aucun remplacement par du pseudo-texte, aucun texte nouveau, ne changer aucun autre élément.

## Bloc de style commun
Fond blanc uni dominant. Illustration pédagogique plane, contours bleu marine réguliers de 3 px environ, aplats bleu très clair, gris froid, vert pâle pour les solutions, orange pour la vigilance ; rouge réservé aux erreurs. Ni texture, ni dégradé, ni ombre décorative, ni 3D. Typographie sans-serif institutionnelle proche de Marianne, Arial en alternative explicite, sans prétendre certifier une police. Grand titre marine centré, gras, casse de phrase, dans la zone y=112–235, deux lignes au maximum. En-tête dans les coins supérieurs, x=40 et x=1632, y=15–65 : première ligne environ 30 px, seconde environ 23 px. Contenu entre y=275 et y=835 ; marges de sécurité 40 px ; cartes arrondies et pictogrammes filaires homogènes. Footer marine discret de 23 px environ à x=34, ligne de base y=909 ; pagination à droite sur la même ligne. Le point médian U+00B7 du footer est petit et fin, jamais une grosse puce. Aucun personnage récurrent : les interfaces et objets portent le point de vue utilisateur. Direction de lecture gauche-droite, respiration entre les blocs. Conserver exactement ce masque commun ; seules les compositions narratives et les chaînes explicitement demandées changent.

Titre exact : Checkpoint 4 : trois attentes déçues
Sous-titre visible : aucun. Aucun badge. Aucun slogan.
Scène principale : trois situations de contact qui laissent attendre.
Storyboard : sous le titre, un bandeau bleu pâle porte « Quelle règle n’est pas respectée ? », comme S20. Puis trois cartes A, B, C côte à côte de largeur égale. Chaque carte contient la phrase exacte et un objet. A : boîte de réception réellement vide ; B : e-mail ouvert, sans bloc contact, son seul contenu est « Ne pas répondre » extrait de sa phrase ; C : formulaire aux vrais champs rectangulaires vides, sans mention de délai. Ne pas remplacer ces situations par des pictogrammes abstraits. Pas de traits simulant des mots dans les interfaces. Les lettres A, B, C introduisent le texte, pas de réponse, de numéro de règle ni de coche. Blanc dominant autour des cartes ; composition lisible.

Texte visible exact :
Quelle règle n’est pas respectée ?
A. Le formulaire est envoyé, aucun e-mail n’arrive.
B. Un e-mail « Ne pas répondre », sans aucune coordonnée.
C. Le formulaire n’indique aucun délai de réponse.
Les phrases complètes gardent leur point final ; ne pas imprimer les séparateurs de liste.

En-tête exact haut gauche : QUALITÉ WEB (gras), puis EXPÉRIENCES DURABLES (normal).
En-tête exact haut droit : Opquast (gras), puis DES SITES MEILLEURS POUR TOUS (normal).
Un seul espace normal entre chaque mot, aucun espacement élargi avant POUR. Reproduire exactement l’espacement de l’image 1.
Footer exact : RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
Pagination exacte : 32 / 42

## Liste blanche exhaustive des chaînes autorisées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Checkpoint 4 : trois attentes déçues
- Quelle règle n’est pas respectée ?
- A. Le formulaire est envoyé, aucun e-mail n’arrive.
- B. Un e-mail « Ne pas répondre », sans aucune coordonnée.
- C. Le formulaire n’indique aucun délai de réponse.
- Ne pas répondre
- RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
- 32 / 42

Contraintes critiques : question dans le bandeau, distincte du titre ; trois situations exactes ; chaque chaîne lettre à lettre, accents et apostrophes typographiques ; footer petit point médian U+00B7 ; boîte A vide, e-mail B sans contact, formulaire C sans délai.
À éviter : tout corrigé, numéro de règle, badge, coche de validation, nom fictif, coordonnées lisibles, marque ajoutée, texte parasite ou pseudo-texte, adresse ou téléphone, notes orales, navigation ajoutée, slogan, photographie, 3D, blob.
Rejet si : texte ajouté, manquant, déformé, rogné ou illisible ; en-tête dont l’espace MEILLEURS → POUR dépasse max(autres espaces)+2 px ; footer ou pagination incorrects ; corrigé visible ; situation non représentée ; dimensions hors tolérance de 3 px.
Test des trois secondes : estimation de l’assistant seulement, aucun test humain chronométré.

