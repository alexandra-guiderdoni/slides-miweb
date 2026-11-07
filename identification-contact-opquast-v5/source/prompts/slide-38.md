# Prompt image_gen — slide 38 — tentative a001

Use case: precise-object-edit.
Type d’actif : image finale 16:9 de la série identification-contact-opquast-v5.
Créer UNE image 1672 × 941 px. Éditer S39 pour produire sa version d’exercice S38, en conservant rigoureusement la scène.
Source verrouillée : storyboard-v002.md S38 et scène commune S39 ; SHA-256 81944fb744f608a5f5f2dbe36b56b1febdc32ed50a0ffa283155667970b15894.
Image 1 : S39 validée, CIBLE D’ÉDITION et étalon de composition ; image 2 : S01, ancre du masque. Le fond de scène de S39 doit être conservé aux mêmes positions et tailles. Ne pas créer un autre cas.
## Bloc de style commun
Fond blanc uni dominant. Illustration pédagogique plane, contours bleu marine réguliers de 3 px environ, aplats bleu très clair, gris froid, vert pâle pour les solutions, orange pour la vigilance ; rouge réservé aux erreurs. Ni texture, ni dégradé, ni ombre décorative, ni 3D. Typographie sans-serif institutionnelle proche de Marianne, Arial en alternative explicite, sans prétendre certifier une police. Grand titre marine centré, gras, casse de phrase, dans la zone y=112–235, deux lignes au maximum. En-tête dans les coins supérieurs, x=40 et x=1632, y=15–65 : première ligne environ 30 px, seconde environ 23 px. Contenu entre y=275 et y=835 ; marges de sécurité 40 px ; cartes arrondies et pictogrammes filaires homogènes. Footer marine discret de 23 px environ à x=34, ligne de base y=909 ; pagination à droite sur la même ligne. Le point médian U+00B7 du footer est petit et fin, jamais une grosse puce. Aucun personnage récurrent : les interfaces et objets portent le point de vue utilisateur. Direction de lecture gauche-droite, respiration entre les blocs. Conserver exactement ce masque commun ; seules les compositions narratives et les chaînes explicitement demandées changent.

En-tête exact haut gauche : QUALITÉ WEB (gras), puis EXPÉRIENCES DURABLES (normal).
En-tête exact haut droit : Opquast (gras), puis DES SITES MEILLEURS POUR TOUS (normal).
Un seul espace normal entre chaque mot. Même espacement que S01 ; pas d’espace élargi entre MEILLEURS et POUR.
Footer exact : RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
Aucun badge de règle ni d’acte. Aucun slogan sauf demande explicite dans le texte visible.

Pagination exacte : 38 / 42
Titre exact : Grand cas final : une page Contact à auditer en cinq minutes
Sous-titre visible : aucun.
Consigne exacte : Trouvez sept défauts.
La consigne se place sur une ligne simple, juste sous le titre, en zone blanche y=235–269. Adapter les retours du titre dans y=95–227 sans empiéter sur le fond de scène qui commence à y=277.
Scène principale : le même parcours que S39, AVANT révélation des sept corrections.
Storyboard : garder le grand panneau et tous les objets de S39 aux mêmes positions, mêmes zones, mêmes tailles, même vue frontale :
- barre d’onglets x=374–911, y=331–399, avec icône générique et le mot Page ;
- panneau de code x=943–1200, y=305–398 : <head> puis </head>, rien entre les deux ;
- grande page au centre-gauche x=276–735, y=420–842, formulaire de trois vrais champs vides sans délai ;
- sous le formulaire, mêmes textes Assistance : numéro surtaxé et Site conforme au référentiel X, ce dernier sans lien ni soulignement ;
- deux pictogrammes de localisation et téléphone, chacun avec une zone neutre sans coordonnée, dans le pied de cette page ;
- boîte à droite x=936–1323, y=421–599, titre Boîte de réception : vide, corps réellement vide ;
- e-mail à droite x=940–1326, y=621–836, titre E-mail : « Ne pas répondre », corps réellement vide sans contact.
EFFACER les sept pastilles numérotées vertes, les sept étiquettes de correction et leurs traits verts. Reconstituer simplement le fond de la scène à leur place, sans déplacer un objet ni écrire un substitut. Aucun numéro de règle, aucune correction. Ne pas confondre les zones neutres de coordonnées avec des barres de pseudo-texte à ajouter.
Dans l’espace libéré de l’ancienne étiquette 1, x=55–337 y=305–390, poser le libellé de scène exact « Onglet : « Page » » en marine, sans vert ni encadré de correction. Le mot Page dans l’onglet reste le même que S39. Ne pas ajouter le nom du fil rouge.

Texte visible exact de la fiche, en plus du titre :
Trouvez sept défauts.
Onglet : « Page »
Assistance : numéro surtaxé
Site conforme au référentiel X
Boîte de réception : vide
E-mail : « Ne pas répondre »
Chaînes techniques/objet nécessaires déjà dans le fond de S39 : Page ; <head> ; </head>.

## Liste blanche exhaustive des chaînes autorisées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Grand cas final : une page Contact à auditer en cinq minutes
- Trouvez sept défauts.
- Onglet : « Page »
- Assistance : numéro surtaxé
- Site conforme au référentiel X
- Boîte de réception : vide
- E-mail : « Ne pas répondre »
- Page
- <head>
- </head>
- RÈGLES OPQUAST · IDENTIFICATION ET CONTACT
- 38 / 42
Contraintes critiques : chaque chaîne lettre à lettre, accents, apostrophes typographiques, guillemets français, signes et numéros exacts ; footer petit point médian U+00B7. Les séparateurs entre cartes ne s’impriment pas. Les phrases complètes gardent leur ponctuation ; les énumérations en cartes n’ont pas de point final isolé sur leur dernier élément.
À éviter : texte hors liste blanche, pseudo-texte (barres imitant du texte comprises), corrigé d’exercice ajouté, coordonnées lisibles, adresse ou téléphone ou immatriculation, marque ajoutée, nom fictif hors fiche, notes orales, badge, navigation ajoutée, photographie, 3D, blob, gros dégradé, ombre décorative.
Rejet si : texte ajouté, manquant, déformé, rogné ou illisible ; relations inversées ; en-tête dont l’espace MEILLEURS → POUR dépasse max(autres espaces)+2 px ; footer ou pagination incorrects ; dimensions hors tolérance de 3 px.
Test des trois secondes : estimation par l’assistant, aucun test humain chronométré.
Interdits spécifiques : aucune pastille numérotée, aucune étiquette verte, aucun trait de correction, aucun numéro de règle, aucune réponse, aucune huitième anomalie ajoutée. La mention de référentiel fictive appartient à la situation défectueuse, pas à une certification. Ne pas imprimer les étiquettes de correction de S39. Rejet si un objet ou un libellé de scène disparaît ou change de position.

