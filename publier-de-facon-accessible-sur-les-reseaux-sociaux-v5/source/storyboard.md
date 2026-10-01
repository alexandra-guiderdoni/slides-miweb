Publier de façon accessible sur les réseaux sociaux - V5
=========================================================

## Contrat de série

- Source pédagogique : slides 110 à 131 du support IGPDE 102846 pour le noyau principal, puis sélection d'approfondissements issue de la V2.
- Correspondance : 22 visuels web pour les 22 slides PPTX, puis 1 conclusion, 1 séparateur et 31 annexes, soit 55 slides.
- Public : communicantes et communicants, sans prérequis technique.
- Format : image finale 16:9, 1600 x 900 visé.
- Masque commun : fond blanc cassé, titre bleu France aligné à gauche, illustration ou objet-système au centre, callout bleu clair centré en bas. La progression reste portée par l’interface du diaporama web, sans numéro ajouté dans l’image.
- Palette : bleu France #000091, bleu clair #E3E3FD, gris froid #F6F6FE, rouge #E1000F réservé aux erreurs ou alertes, vert #18753C réservé aux corrections validées.
- Typographie : Marianne, avec Arial comme seul fallback.
- Interdits : faux logo, emblème officiel, photographie, 3D, dégradé, texte parasite, paragraphe dense dans l’image, tiret cadratin ou demi-cadratin.
- Règle de fidélité : le visuel peut condenser, mais la transcription HTML doit reprendre tout le contenu visible du PPTX et le discours oral doit reprendre ses notes.

## Règles de correspondance sémantique

- Couche visuelle : titre source inchangé, une scène concrète, trois à six repères courts et aucun ajout métier.
- Transcription : tous les textes visibles du PPTX, regroupés sous des titres de niveau cohérent, des listes et de vrais tableaux quand la source est tabulaire.
- Titres de blocs : les libellés visibles comme « Qui en bénéficie ? », « À faire » ou « Déroulé » deviennent des intertitres dans la transcription HTML.
- Discours oral : toutes les notes du présentateur, structurées avec des titres et des listes qui suivent la hiérarchie de la slide, sans les confondre avec la transcription.
- Source opposable du discours oral : le texte de `add_notes()` dans chaque fichier Python, repris intégralement même lorsqu’il s’agit de consignes au formateur.
- Exercices et démonstrations : les consignes, durées, conditions de réussite et modalités de restitution restent distinctes du commentaire du formateur.
- Fidélité : une condensation du visuel ne supprime jamais un élément de la transcription ; une reformulation graphique n’ajoute jamais une règle absente du PPTX.
- Texte des images : toute formulation lisible vient du contenu visible de la même slide. Une idée présente uniquement dans les notes reste dans le discours oral.
- Contradictions de la source : conserver les formulations propres à chaque slide et les signaler dans la traçabilité ; ne pas les harmoniser silencieusement.
- Masque PPTX : transcrire le fil d’Ariane comme rubrique. Exclure de la transcription le pied de page répété, la date et le numéro de page, considérés comme éléments de masque et documentés ici explicitement.
- Sémantique HTML : les tableaux source deviennent de vrais tableaux HTML avec en-têtes et attributs `scope`. Le générateur propre au nouveau jeu devra couvrir ce rendu et son test de contrat.
- Tableau de la slide 10 : le titre exact de la slide sert de légende au tableau HTML, sans légende supplémentaire inventée.
- Navigation : les titres des 22 premières fiches restent identiques aux titres PPTX ; les slides 23 à 55 forment une extension clairement annoncée.

## Traçabilité des variations de la source

- Slides 02 et 07 : conserver respectivement « 1 phrase » et « 1 à 2 phrases » pour le texte alternatif.
- Slides 03 et 05 : conserver respectivement « de la #COVID19 » et « du #COVID19 ».
- Slides 03 à 05 : conserver les trois états distincts du tweet, sans les harmoniser.
- Slides 08 et 10 : conserver les chemins courts et « Twitter/X » sur la première, les chemins complets et « X (Twitter) » sur la seconde.
- Slides 02 et 07 : conserver respectivement les termes « gestes » et « réflexes ».
- Slide 12 : conserver mot pour mot la restitution NVDA, y compris « peau claire ».
- Fil d’Ariane transcrit comme rubrique : 01 « Partie IV | Plan » ; 02 « 4. Réseaux sociaux » ; 03 à 05 « 4. Réseaux sociaux | Cas pratique » ; 06 « 4. Réseaux sociaux | Démonstration » ; 07 « 4. Réseaux sociaux | Réflexes » ; 08 et 09 « 4. Réseaux sociaux | Alt text » ; 10 « 4. Réseaux sociaux | Plateformes » ; 11 et 12 « 4. Réseaux sociaux | Émojis » ; 13 « 4. Réseaux sociaux | Hashtags » ; 14 « 4. Réseaux sociaux | Caractères spéciaux » ; 15 à 17 « 4. Réseaux sociaux | Communication inclusive » ; 18 « 4. Réseaux sociaux | Exercice » ; 19 à 21 « 4. Réseaux sociaux | Checklist » ; 22 « Clôture ».
- Slide 22 : la coquille source « Cloture » est corrigée en « Clôture » conformément à la règle éditoriale du dépôt qui impose les accents en français.

## Colonne vertébrale

Cette structure est un outil interne de conception. Elle ne devient pas un contenu supplémentaire de la présentation.

1. Comprendre le problème à partir d’un post réel.
2. Acquérir quatre réflexes de rédaction et de publication.
3. Élargir à la représentation et au langage inclusif.
4. Mettre les règles en pratique avec une checklist en trois temps.
5. Conclure et ouvrir les questions.
6. Prolonger avec des annexes pratiques mobilisables à la demande.

## Slide 01 - Partie IV - Réseaux sociaux accessibles - TP

- Rôle : ouverture et carte du module.
- Idée principale : le module va de l’analyse d’un post à sa vérification avant publication.
- Scène : une communicante prépare un post sur un grand écran, entourée de cinq cartes étapes.
- Transformation : publication brute -> publication vérifiée.
- Texte exact : titre ; « Comprendre » ; « Décrire » ; « Rendre lisible » ; « Représenter » ; « Vérifier ».
- Image seule : un parcours complet de publication accessible.
- Continuité : ouvre la séquence et prépare la question d’accroche.
- Contraintes critiques : cinq étapes visibles, aucun numéro de slide dans le titre, aucune marque de plateforme.
- Couverture HTML : les cinq thèmes complets du plan, dans l’ordre du PPTX.
- Discours oral : reprendre intégralement la source, dont l’annonce des cinq thèmes, la progression de l’analyse à la vérification, la question sur la publication d’une photo sans texte alternatif et la conclusion « Toutes les mains levées - c’est le problème qu’on va résoudre. ».

## Slide 02 - Pourquoi l’accessibilité sur les réseaux ?

- Rôle : enjeu et bénéfice.
- Idée principale : une publication publique doit rester accessible dans plusieurs contextes d’usage.
- Scène : un même post atteint quatre personnes ou outils dans des situations différentes.
- Transformation : diffusion unique -> accès multiple.
- Texte exact : titre ; « 12 millions » ; « Handicap » ; « Contexte défavorable » ; « Recherche et IA » ; « Sans images » ; « 4 gestes, 2 minutes par post ».
- Image seule : le public réel dépasse la seule personne qui voit parfaitement l’image.
- Continuité : donne l’enjeu puis prépare l’observation d’un post réel.
- Contraintes critiques : ne pas inventer d’autre chiffre ; conserver « 12 millions ».
- Couverture HTML : canal officiel et obligations d’accessibilité ; les quatre publics ou contextes ; les quatre gestes avec leur formulation complète.
- Discours oral : reprendre intégralement la source, dont « INSEE », « ne pas chercher à impressionner », la personne qui ne pourra pas lire le post, les quatre gestes et la question sur les dix derniers posts.

## Slide 03 - Regardez ce tweet - qu’est-ce qui ne va pas ?

- Rôle : cas pratique initial.
- Idée principale : les défauts d’accessibilité ne sont pas toujours visibles au premier regard.
- Scène : deux personnes observent un post rempli d’émojis et annotent leurs hypothèses. Le corps du post est figuré par des lignes neutres et les émojis utiles ; le seul extrait lisible est « Protégez-vous de la #COVID19 : ».
- Transformation : voir un post -> chercher les obstacles.
- Texte exact : titre ; « Tweet publié par l’OMS en 2020 » ; « Protégez-vous de la #COVID19 : » ; « En binôme - 2 minutes » ; « Identifiez le maximum de problèmes d’accessibilité » ; « Ne lisez pas le tweet à voix haute » ; « Notez ce qui vous gêne ou vous surprend ».
- Image seule : une enquête collective sur un post problématique.
- Continuité : prépare la révélation de la vocalisation.
- Contraintes critiques : pas de logo OMS ; pas de marque de réseau social ; émojis visibles ; aucun autre extrait lisible que « Protégez-vous de la #COVID19 : ».
- Couverture HTML : texte intégral du tweet affiché ; trois consignes du travail en binôme ; durée de deux minutes.
- Discours oral : reprendre intégralement la source, dont les réponses possibles « émojis », « contraste » ou « rien », sans ajouter d’annonce de la slide suivante.

## Slide 04 - Ce que vous voyez ≠ ce qui est lu

- Rôle : révélation.
- Idée principale : le lecteur d’écran vocalise le nom complet des émojis et casse le flux.
- Scène : à gauche le post vu, à droite une onde sonore longue et encombrée.
- Transformation : phrase courte à l’écran -> restitution orale longue.
- Texte exact : titre ; « Ce que vous voyez » ; « Lavez-vous les 👐 avec du 🧼 & de l’💦. » ; « Ce que NVDA lit à voix haute » ; « Lavez-vous les mains ouvertes avec du savon et éclaboussures de sueur. » ; « Chaque émoji a un nom officiel lu intégralement. Il interrompt le flux de lecture. ».
- Image seule : un message visuellement court devient une écoute chargée.
- Continuité : explique le problème puis prépare la correction.
- Contraintes critiques : comparaison en deux colonnes, émojis sans texte parasite, signe « ≠ » exact.
- Couverture HTML : les trois phrases vues ; les trois phrases vocalisées par NVDA ; le message sur le nom officiel des émojis et l’interruption du flux.
- Discours oral : reprendre intégralement la source, dont la lecture monotone sans pause, le silence, l’effet de surprise, l’absence de commentaire immédiat et la question finale.

## Slide 05 - 3 changements, 0 perte de sens

- Rôle : correction du cas pratique.
- Idée principale : réduire les émojis, numéroter et isoler le hashtag clarifie sans supprimer d’information.
- Scène : un post encombré passe par trois gestes et devient une liste claire.
- Transformation : post problématique -> post accessible.
- Texte exact : titre ; « Version originale - problématique » ; « Version accessible » ; « Les 3 changements » ; « Émojis réduits à 1 » ; « Structure numérotée » ; « Hashtag conservé mais seul » ; « Le message tient sans eux ».
- Image seule : trois gestes simples corrigent le post.
- Continuité : donne la solution puis prépare la démonstration réelle.
- Contraintes critiques : exactement trois changements ; ne pas ajouter une quatrième règle.
- Couverture HTML : les trois phrases originales ; la ligne « Protégez-vous du #COVID19 - trois gestes essentiels : » ; la liste ordonnée de trois gestes ; les trois changements et leur bénéfice.
- Discours oral : reprendre intégralement la source, dont l’absence de perte d’information, le gain pour tout le monde, la question « Combien de temps faut-il pour faire ces 3 modifications ? » et la réponse « 2 minutes ».

## Slide 06 - Démonstration NVDA - le lecteur d’écran en direct

- Rôle : démonstration.
- Idée principale : écouter sans regarder révèle immédiatement les obstacles.
- Scène : ordinateur portable, casque audio et quatre étapes horizontales.
- Transformation : ouvrir -> activer -> naviguer -> écouter.
- Texte exact : titre ; « Ouvrir le post » ; « Activer NVDA » ; « Naviguer » ; « Écouter sans regarder » ; « Notez le premier mot ».
- Image seule : une démonstration guidée en quatre actions.
- Continuité : fait vivre l’obstacle puis prépare les quatre réflexes.
- Contraintes critiques : quatre étapes dans cet ordre ; aucun raccourci clavier inventé dans l’image.
- Couverture HTML : les quatre étapes exactes, dont Ctrl+Alt+N, les flèches ou Tab, et les deux consignes destinées aux stagiaires.
- Discours oral : reprendre intégralement la source, dont le post à 5-6 émojis, Ctrl+Alt+N, Insert+Q, Win+Ctrl+Entrée, 5 minutes maximum et 5 minutes de test individuel si le temps le permet.

## Slide 07 - 4 réflexes, puis une checklist complète

- Rôle : boussole du module.
- Idée principale : quatre réflexes forment le noyau dur avant la checklist complète.
- Scène : une publication au centre, entourée de quatre cartes reliées.
- Transformation : post non vérifié -> quatre contrôles rapides.
- Texte exact : titre ; « Texte alternatif » ; « Émojis sobres » ; « Hashtags CamelCase » ; « Texte natif ».
- Image seule : quatre vérifications simples autour d’un post.
- Continuité : annonce les quatre sujets détaillés ensuite.
- Contraintes critiques : quatre cartes seulement ; aucune mention « Image décorative » tronquée dans le visuel.
- Couverture HTML : les deux règles complètes de chacune des quatre cartes, dont la formulation exacte « Image décorative : utiliser l’option « Décorative » si la plateforme la propose. Sinon, indiquer « Image décorative » dans le texte alternatif. ».
- Discours oral : reprendre intégralement la source, dont le retour prévu en fin de module, les quatre actions, les deux minutes, l’absence de compétence technique et les trois temps de la checklist.

## Slide 08 - Le texte alternatif : votre sous-titre d’image

- Rôle : expliquer l’utilité du texte alternatif.
- Idée principale : le texte alternatif donne accès à l’information de l’image dans plusieurs contextes.
- Scène : une image de réunion mène vers un champ de texte alternatif, puis vers cinq bénéficiaires ou contextes représentés par des pictogrammes. Les plateformes restent dans la transcription HTML et sont détaillées dans le tableau comparatif dédié.
- Transformation : image seule -> information accessible.
- Texte exact : titre ; « L’alt text, c’est comme un sous-titre pour votre image : il dit ce qu’elle montre à ceux qui ne peuvent pas la voir. » ; « Lecteur d’écran » ; « Image non chargée » ; « Recherche » ; « IA et outils d’analyse d’image » ; « Contexte défavorable ».
- Image seule : un même texte alternatif sert plusieurs usages.
- Continuité : explique pourquoi puis prépare la rédaction.
- Contraintes critiques : pas de promesse SEO chiffrée ; ne pas représenter le texte alternatif comme une légende visible.
- Couverture HTML : analogie du sous-titre ; cinq bénéficiaires ou contextes ; cinq plateformes avec le chemin d’accès affiché dans le PPTX.
- Discours oral : reprendre intégralement la source, dont l’analogie du sous-titre, le bénéfice pour le référencement, la démonstration du champ sur LinkedIn et l’annonce du tableau comparatif, sans prétendre qu’il se trouve sur la slide immédiatement suivante.

## Slide 09 - Comment rédiger un bon texte alternatif ?

- Rôle : comparaison et exercice.
- Idée principale : décrire l’information utile, pas le fichier ni une formule vague.
- Scène : deux cartes « À éviter » et « Ce qui fonctionne », puis trois vignettes d’exercice.
- Transformation : alt vague -> alt utile.
- Texte exact : titre ; « À éviter » ; « image.jpg » ; « Photo » ; « Ce qui fonctionne » ; « Trois agents discutent autour d’une table, documents ouverts » ; « Exercice en binôme - 7 min ».
- Image seule : une réécriture guidée du mauvais vers le bon.
- Continuité : donne la règle puis prépare les emplacements dans les plateformes.
- Contraintes critiques : le rouge signale seulement les exemples à éviter ; le vert signale la correction.
- Couverture HTML : les quatre exemples à éviter, les quatre exemples qui fonctionnent et la consigne complète de l’exercice de sept minutes sur trois images professionnelles.
- Discours oral : reprendre intégralement la source, dont la règle « décrire ce qui est utile pour comprendre le message, pas ce qui est visible », l’exemple « Équipe de 5 agents en réunion de travail », le traitement des chiffres d’une infographie et le recueil d’une ou deux propositions.

## Slide 10 - Alt text : où le trouver sur chaque plateforme ?

- Rôle : mémo opérationnel.
- Idée principale : le champ existe mais son chemin change selon la plateforme.
- Scène : un tableau visuel simplifié à cinq lignes et deux colonnes, « Plateforme » et « Moment ». Les chemins détaillés restent dans le tableau HTML complet à trois colonnes.
- Transformation : chercher l’option -> savoir où agir.
- Texte exact : titre ; « Plateforme » ; « Moment » ; « LinkedIn » ; « Facebook » ; « X (Twitter) » ; « Instagram » ; « Canva » ; « À la publication ou après » ; « Avant publication uniquement » ; « Pendant la création » ; « Astuce : activez-le par défaut ».
- Image seule : cinq chemins d’accès comparables.
- Continuité : clôt le texte alternatif et ouvre les règles d’émojis.
- Contraintes critiques : cinq plateformes ; deux colonnes dans l’image et trois dans le HTML ; aucun faux logo ; noms correctement orthographiés ; distinguer « avant publication uniquement », « à la publication ou après » et « pendant la création ».
- Couverture HTML : tableau complet avec les chemins et moments exacts pour les cinq plateformes ; les deux astuces de rappel.
- Discours oral : reprendre intégralement la source, dont le tableau comme mémo, X avant publication, LinkedIn après publication et l’annonce du mémo PDF.

## Slide 11 - Émojis : 3 règles simples

- Rôle : règle de rédaction.
- Idée principale : limiter, placer à la fin et vérifier le sens.
- Scène : un post passe par trois contrôles numérotés.
- Transformation : message décoré -> message compréhensible sans émoji.
- Texte exact : titre ; « 1 ou 2 maximum » ; « En fin de message » ; « Sens vérifié » ; « Le message est-il toujours clair et complet ? ».
- Image seule : trois règles ordonnent l’usage des émojis.
- Continuité : annonce la règle puis prépare l’écoute d’un exemple.
- Contraintes critiques : exactement trois règles ; aucun émoji ne remplace un mot.
- Couverture HTML : rappel sur la vocalisation ; les trois règles complètes ; les trois étapes du test rapide avant publication.
- Discours oral : reprendre intégralement la source, dont les deux exemples avec leurs émojis et la formulation « ALERTE - Fermeture exceptionnelle » suivie de l’émoji.

## Slide 12 - Ce que ça donne avec trop d’émojis

- Rôle : exemple avant et après.
- Idée principale : une phrase visuelle devient une vocalisation interminable.
- Scène : à gauche un post saturé d’émojis, au centre une longue onde sonore, à droite la version accessible exacte avec l’émoji d’ordinateur final.
- Transformation : bruit vocal -> message clair.
- Texte exact : titre ; « Post original » ; « Ce que NVDA lit » ; « Version accessible » ; « Rejoignez-nous mardi 10 juin, salle B3, pour notre atelier sur l’accessibilité numérique. 💻 ».
- Image seule : l’excès d’émojis allonge l’écoute.
- Continuité : consolide la règle puis passe aux hashtags.
- Contraintes critiques : conserver l’ordre avant -> écoute -> après ; pas de faux texte long.
- Couverture HTML : post original complet, restitution NVDA complète et version accessible complète.
- Discours oral : reprendre intégralement la source, dont la lecture sans intonation, la comparaison, la question et la réponse de trente secondes.

## Slide 13 - Hashtags : le CamelCase qui change tout

- Rôle : règle de lisibilité.
- Idée principale : les majuscules séparent les mots et facilitent la compréhension.
- Scène : comparaison directe entre trois écritures d’un même hashtag.
- Transformation : bloc ambigu -> mots repérables.
- Texte exact : titre ; « #ServicePublic » ; « #servicepublic » ; « #SERVICEPUBLIC » ; « Majuscule au début de chaque mot » ; « 2 à 3 hashtags maximum ».
- Image seule : le CamelCase rend les mots visibles et prononçables.
- Continuité : traite les hashtags puis les faux styles Unicode.
- Contraintes critiques : reproduire exactement les trois hashtags ; ne pas inventer un autre exemple.
- Couverture HTML : les trois comparaisons CamelCase, minuscules et capitales ; les trois règles avant publication ; le mini-test de lecture à voix haute.
- Discours oral : reprendre intégralement la source, dont 2012, le hashtag exact « #susanalbumparty », la longueur et la conclusion sur la norme éditoriale.

## Slide 14 - Faux gras et caractères Unicode : le piège invisible

- Rôle : alerte et solution.
- Idée principale : les générateurs de faux style remplacent les lettres par d’autres caractères.
- Scène : un texte issu d’un générateur de style se fragmente dans le lecteur d’écran, la recherche et la traduction, puis revient en texte simple.
- Transformation : faux gras fragile -> texte simple fiable.
- Texte exact : titre ; « InstaFont, LingoJam ... transforment les lettres en symboles » ; « Le lecteur d’écran peut épeler, déformer ou ignorer le message » ; « Le texte devient moins fiable à copier, indexer ou traduire » ; « Utiliser le gras natif de la plateforme quand il existe » ; « Sinon : écrire en texte simple ».
- Image seule : l’apparence visuelle peut casser les usages du texte.
- Continuité : termine les règles techniques et ouvre la communication inclusive.
- Contraintes critiques : ne pas reproduire de caractères fantaisie illisibles comme contenu principal.
- Couverture HTML : les trois risques des générateurs de style, les trois solutions et le test express avec la référence à la règle Opquast 14 sous forme de lien vers https://checklists.opquast.com/fr/qualite-numerique/les-contenus-ne-detournent-pas-de-caracteres-pour-simuler-une-mise-en-forme-visuelle.
- Discours oral : reprendre intégralement la source, dont la démonstration de « Bonjour », TalkBack, VoiceOver, la référence AQW et les deux solutions.

## Slide 15 - Communication inclusive : les représentations comptent

- Rôle : élargissement aux visuels.
- Idée principale : choisir une image revient aussi à montrer qui est attendu et légitime.
- Scène : une communicante compare trois propositions de visuels montrant des publics différents.
- Transformation : choix automatique -> choix questionné.
- Texte exact : titre ; « Qui est visible ? » ; « Qui est absent ? » ; « Quelle norme est installée ? » ; « Permettre au public de se projeter ».
- Image seule : la sélection d’un visuel est une décision de représentation.
- Continuité : pose les questions puis prépare la cohérence réelle.
- Contraintes critiques : diversité représentée sans stéréotype ni mise à l’écart ; aucun handicap utilisé comme décoration.
- Couverture HTML : message sur la non-neutralité de l’image ; les trois questions de sélection ; les trois bénéfices attendus.
- Discours oral : reprendre intégralement la source, dont le choix d’introduire par les images, le risque de réduire le sujet à l’écriture inclusive, les six normes citées et l’absence de culpabilisation.

## Slide 16 - Représenter sans faire vitrine

- Rôle : comparaison éthique.
- Idée principale : la représentation doit être ordinaire, active et cohérente avec la réalité accessible.
- Scène : deux affiches d’événement, l’une cohérente avec un lieu accessible, l’autre inclusive en apparence mais bloquée à l’entrée.
- Transformation : image symbolique -> cohérence entre image et expérience.
- Texte exact : titre ; « Représentation utile » ; « Rôle actif » ; « Situation ordinaire » ; « Piège à éviter » ; « Règle simple : si vos visuels montrent des personnes handicapées, vos espaces, événements et pratiques doivent être accessibles. ».
- Image seule : un visuel inclusif ne compense pas un service inaccessible.
- Continuité : relie représentation et réalité puis passe au langage.
- Contraintes critiques : ne pas humilier ni caricaturer ; le blocage doit porter sur l’environnement, pas sur la personne.
- Couverture HTML : les trois critères de représentation utile, les trois pièges et la règle de cohérence entre visuel, espaces, événements et pratiques.
- Discours oral : reprendre intégralement la source, dont la représentation opportuniste, la phrase « un visuel inclusif ne compense pas une organisation inaccessible », l’exemple d’un événement dont le lieu, l’inscription ou les supports ne sont pas accessibles et le lien avec la checklist.

## Slide 17 - Langage inclusif : clarté d’abord

- Rôle : arbitrage rédactionnel.
- Idée principale : choisir la formulation la plus inclusive qui reste claire, lisible et prononçable.
- Scène : quatre cartes montrent les exemples source « Nous vous convions », « le public », « les utilisateurs et utilisatrices » et « iels / amateurices », puis un test oral.
- Transformation : formulation compressée -> phrase inclusive et fluide.
- Texte exact : titre ; « Nous vous convions » ; « le public » ; « les utilisateurs et utilisatrices » ; « iels / amateurices » ; « Claire, lisible et prononçable ».
- Image seule : plusieurs solutions existent, la compréhension décide.
- Continuité : clôt les apports puis prépare l’exercice global.
- Contraintes critiques : aucune caricature du point médian ; ne pas présenter une seule forme comme obligatoire.
- Couverture HTML : les quatre formes à privilégier, les trois formes à éviter ou tester et la recommandation finale de clarté, lisibilité et prononçabilité.
- Discours oral : reprendre intégralement la source, dont la neutralité du traitement, l’évolution des synthèses vocales et des usages, la charge de lecture pour les personnes dyslexiques ou fatiguées cognitivement, les formes épicènes, les mots collectifs et la double flexion.

## Slide 18 - Exercice en binôme : passez la checklist

- Rôle : mise en pratique.
- Idée principale : identifier deux améliorations prioritaires sur un post réel.
- Scène : deux personnes examinent un post et suivent quatre étapes sur une fiche.
- Transformation : observer -> vérifier -> prioriser -> restituer.
- Texte exact : titre ; « Choisir 1 publication » ; « Cocher Anticiper / Rédiger / Publier » ; « Retenir 2 risques prioritaires » ; « Préparer 1 min de restitution ».
- Image seule : un binôme transforme une checklist en deux décisions concrètes.
- Continuité : lance l’exercice puis fournit les trois checklists.
- Contraintes critiques : quatre étapes, deux améliorations, une minute de restitution.
- Couverture HTML : objectif complet ; quatre étapes ; déroulé en trois, huit et quatre minutes ; trois éléments à restituer.
- Discours oral : reprendre intégralement la source, dont la limitation à deux améliorations, le point représentation, le feedback immédiat et l’apprentissage social par la restitution.

## Slide 19 - Checklist réseaux sociaux : anticiper (1/3)

- Rôle : première checklist.
- Idée principale : prévoir les alternatives et la lisibilité avant de fabriquer le visuel.
- Scène : une table de préparation avec média, public, version complète, typographie et contraste.
- Transformation : idée brute -> production accessible dès le départ.
- Texte exact : titre ; « Média et alternative » ; « Représentations cohérentes » ; « Version complète » ; « Police lisible » ; « Contraste >= 4,5:1 ».
- Image seule : cinq contrôles sont réalisés avant la création.
- Continuité : prépare le contenu puis passe à la rédaction.
- Contraintes critiques : exactement cinq items ; contraste écrit « 4,5:1 ».
- Couverture HTML : accroche complète et cinq contrôles exacts sur média, représentations, version complète, police et contraste.
- Discours oral : reprendre intégralement la source, dont l’usage comme support d’exercice, la consigne de cocher uniquement ce qui peut être vérifié, le traitement sans procès d’intention, le piège classique de la réparation au moment de publier et le lien avec Word.

## Slide 20 - Checklist réseaux sociaux : rédiger (2/3)

- Rôle : deuxième checklist.
- Idée principale : le message doit rester compréhensible sans image, effets ni émojis.
- Scène : une rédactrice simplifie un post en cochant cinq contrôles.
- Transformation : post dépendant de la forme -> texte autonome.
- Texte exact : titre ; « Informations dans le texte » ; « Paragraphes courts » ; « 1 ou 2 émojis » ; « Hashtags CamelCase » ; « Langage inclusif clair ».
- Image seule : cinq contrôles rendent le texte autonome.
- Continuité : stabilise la rédaction puis prépare la publication.
- Contraintes critiques : exactement cinq items ; ne pas faire porter l’information par les émojis.
- Couverture HTML : accroche complète et cinq contrôles exacts sur informations, paragraphes, émojis, hashtags et langage inclusif.
- Discours oral : reprendre intégralement la source, dont la transformation en routine éditoriale, la consigne de cocher les cinq points, le choix d’un problème prioritaire, le test à l’écoute et à la lecture rapide et le test UX consistant à retirer les effets.

## Slide 21 - Checklist réseaux sociaux : publier (3/3)

- Rôle : troisième checklist.
- Idée principale : vérifier chaque accès visuel ou sonore juste avant la publication.
- Scène : une action de publication reste verrouillée jusqu’à cinq contrôles validés, sans texte supplémentaire sur le bouton.
- Transformation : publication prête visuellement -> publication accessible.
- Texte exact : titre ; « Alt text par image informative » ; « Chiffres repris dans le post » ; « Audio transcrit » ; « Sous-titres relus » ; « QR code + lien visible ».
- Image seule : cinq portes de contrôle ouvrent la publication.
- Continuité : conclut l’exercice et prépare les questions.
- Contraintes critiques : exactement cinq items ; le QR code ne doit jamais apparaître seul.
- Couverture HTML : accroche complète et cinq contrôles exacts sur alt text, infographie ou carrousel, audio, vidéo et QR code avec lien visible, dont l’appel à l’action exact « Scannez-moi ! », la taille et le contraste.
- Discours oral : reprendre intégralement la source, dont les alternatives réellement manquantes, l’accès multiple et la règle corrigée du QR code.

## Slide 22 - Des questions ?

- Rôle : clôture.
- Idée principale : ouvrir les questions et remercier le groupe.
- Scène : le groupe échange autour d’un post accessible finalisé.
- Transformation : règles apprises -> questions et transfert vers la pratique.
- Texte exact : « Des questions ? » ; « Merci pour votre participation ! ».
- Image seule : une conclusion ouverte et collective.
- Continuité : ferme la séquence.
- Contraintes critiques : aucune coordonnée personnelle ; aucun faux logo ; aucun message supplémentaire.
- Couverture HTML : titre, remerciement et mention « Bloc Vos contacts : coordonnées des formateurs non reproduites dans cette version publique » tant que la règle de confidentialité n’est pas arbitrée.
- Discours oral : reprendre mot pour mot les deux phrases de la source, sans y ajouter de coordonnées.

## Extension V5 - conclusion et annexes

- La slide 23 reprend la conclusion V2-38 dans le style IGPDE bleu illustré.
- La slide 24 annonce cinq familles d'annexes.
- Les slides 25 à 55 reprennent 31 contenus V2 sélectionnés, dans leur ordre pédagogique d'origine.
- La slide issue de V2-26 applique la règle validée pour les images décoratives sur les réseaux sociaux.
- Chaque nouvelle slide possède une transcription du visuel et un discours oral distinct.

## Slide 23 - Produire accessible, c'est produire mieux

- Source : V2-38.
- Rôle : conclusion positive du noyau principal.
- Idée principale : une communication de qualité est une communication qui n'exclut personne.
- Scène : une publication vérifiée mène à trois ressources, puis à un échange d'équipe.
- Contraintes critiques : aucune alerte rouge, aucun logo, aucun ajout technique, beaucoup d'espace blanc.

## Slide 24 - Annexes

- Rôle : séparer clairement le noyau issu du PPTX et les approfondissements.
- Idée principale : les annexes sont des fiches à mobiliser selon les besoins, pas une seconde progression obligatoire.
- Scène : une communicante ouvre un classeur contenant cinq familles de ressources.
- Contraintes critiques : cinq familles visibles et 31 fiches annoncées.

## Slide 25 - Communiquer sans exclure

- Source : V2-03.
- Rubrique : Texte et signes.
- Rôle : poser l'enjeu humain.
- Idée principale : une publication sociale doit rester compréhensible quand l'effet visuel disparaît.
- Scène : une table éditoriale vue de face ; à gauche, une personne prépare une publication visuelle ; au centre, le même contenu est simplifié en message clair ; à droite, une personne écoute le message via un lecteur d'écran et un canal accessible le reprend.
- Transformation : publication décorative -> message clair -> accès par canal accessible.
- Image seule : le même message atteint plusieurs publics quand il reste textuel et clair.
- Contraintes critiques : aucun logo, aucun numéro de progression, conserver le texte exact, ne pas suggérer que les émojis sont interdits.
- Risque à éviter : scène trop technique, texte dense, faux logo de plateforme.

## Slide 26 - Un seul émoji suffit

- Source : V2-05.
- Rubrique : Texte et signes.
- Rôle : donner la première règle concrète.
- Idée principale : répéter un émoji n'ajoute pas d'information.
- Scène : deux publications sont comparées sur une même table ; à gauche, le message est entouré de signes d'alerte rouges et l'écoute devient bruyante ; à droite, un seul signal accompagne le message et la lecture reste nette.
- Transformation : bruit visuel -> signal unique -> message lisible.
- Image seule : la version simple garde le sens sans empiler les signes.
- Contraintes critiques : rouge uniquement sur l'erreur ou l'alerte, aucun numéro de progression, conserver le texte exact.
- Risque à éviter : rouge décoratif excessif, vrai bouton d'urgence, accumulation qui rend la slide illisible.

## Slide 27 - Garder les mots et chiffres en texte

- Source : V2-06.
- Rubrique : Texte et signes.
- Rôle : éviter les contresens.
- Idée principale : les mots et les nombres essentiels doivent rester en texte réel.
- Scène : une carte statistique cassée affiche deux touches décoratives `4` ambiguës ; une flèche de correction mène à une carte lisible où `44 %` est écrit comme du texte réel.
- Transformation : symbole ambigu -> contresens -> texte fiable.
- Image seule : remplacer un chiffre par un pictogramme casse la donnée.
- Contraintes critiques : `44 %` doit apparaître exactement, aucun autre chiffre, aucun numéro de progression, conserver le texte exact.
- Risque à éviter : statistique inventée, texte de carte trop long, confusion entre exemple et vraie donnée.

## Slide 28 - Placer l'émoji après le message

- Source : V2-07.
- Rubrique : Texte et signes.
- Rôle : organiser la lecture.
- Idée principale : l'information doit être entendue avant l'ornement.
- Scène : deux lignes de publication deviennent une chronologie d'écoute ; en haut, des signes décoratifs bloquent le départ ; en bas, la phrase commence par le message et l'ornement arrive en fin de ligne.
- Transformation : obstacle avant le texte -> lecture directe -> ornement final.
- Image seule : l'ordre de lecture change l'effort.
- Contraintes critiques : peu de signes visuels, aucun numéro de progression, conserver le texte exact.
- Risque à éviter : phrase trop longue, trop d'émojis, rendu trop ludique.

## Slide 29 - Ce n'est pas du style

- Source : V2-08.
- Rubrique : Texte et signes.
- Rôle : faire comprendre le mécanisme technique du faux gras, du faux italique et des polices fantaisie.
- Idée principale : un générateur ne met pas le texte en forme, il remplace les lettres par d'autres caractères.
- Scène : à gauche, une publication sociale ne propose pas de vrai bouton gras ou italique ; au centre, un outil tiers transforme un mot en faux gras, faux italique et lettrage fantaisie ; à droite, le résultat semble décoratif mais porte un panneau de risque.
- Transformation : texte réel -> générateur -> caractères détournés.
- Image seule : l'apparence de style est produite par un remplacement de caractères.
- Contraintes critiques : conserver le texte exact, ne pas écrire de vraie phrase en caractères fantaisie, ne pas afficher de logo de plateforme ni de générateur, ne pas suggérer que tout Unicode est interdit.
- Risque à éviter : scène trop abstraite, effet typographique séduisant, trop de styles différents.

## Slide 30 - Le lecteur d'écran perd le mot

- Source : V2-09.
- Rubrique : Texte et signes.
- Rôle : montrer l'impact d'accessibilité le plus direct.
- Idée principale : les caractères détournés peuvent être ignorés, épelés ou restitués comme des symboles.
- Scène : une publication entre dans un lecteur d'écran ; la sortie audio montre un trou, une lecture lettre par lettre et des symboles mathématiques, puis une version corrigée rétablit le mot en texte réel.
- Transformation : faux style -> vocalisation incompréhensible -> texte réel rétabli.
- Image seule : le problème n'est pas esthétique, il bloque l'accès au contenu.
- Contraintes critiques : ne pas écrire de longue restitution vocale, ne pas inventer de phrase technique, conserver les labels courts, garder la bulle audio lisible.
- Risque à éviter : culpabiliser les personnes, faire croire qu'un lecteur d'écran échoue toujours de la même façon.

## Slide 31 - Les outils ne suivent plus

- Source : V2-10.
- Rubrique : Texte et signes.
- Rôle : montrer que le problème touche aussi la diffusion, la recherche et la traduction.
- Idée principale : si les caractères ne sont plus les mêmes, les outils peuvent ne plus reconnaître le mot.
- Scène : une publication avec un mot en faux style passe vers trois outils : recherche, traduction et indexation ; les trois affichent une alerte ou un résultat incomplet. Une seconde carte montre le même mot en texte réel qui circule correctement.
- Transformation : caractères détournés -> outils perturbés -> texte réel retrouvé.
- Image seule : l'artifice visuel réduit aussi la portée du message.
- Contraintes critiques : ne pas citer de plateforme, ne pas afficher de données SEO inventées, conserver le texte exact, ne pas ajouter de logo de moteur de recherche.
- Risque à éviter : transformer la slide en tableau technique, réduire le sujet au référencement.

## Slide 32 - Bannir les faux décors de texte

- Source : V2-11.
- Rubrique : Texte et signes.
- Rôle : nommer les mauvaises pratiques courantes au-delà du faux gras.
- Idée principale : certains signes décoratifs simulent une structure ou une mise en valeur mais ajoutent du bruit.
- Scène : une table de relecture compare quatre cartes à proscrire : fausses puces, lettres espacées, titre encadré de symboles et ASCII art ; une main ou un tampon les classe en éléments décoratifs à retirer.
- Transformation : décor ajouté -> bruit de lecture -> retrait des signes.
- Image seule : les ornements ne doivent pas porter la structure du message.
- Contraintes critiques : ne pas reproduire un long ASCII art, éviter les caractères décoratifs séduisants, conserver les labels exacts, ne pas utiliser d'exemple qui ressemble à une marque.
- Risque à éviter : rendre la mauvaise pratique trop attractive, mélanger puces réelles et faux symboles.

## Slide 33 - Linéariser les faux tableaux

- Source : V2-12.
- Rubrique : Texte et signes.
- Rôle : isoler le cas des colonnes simulées, car il inverse l'ordre de lecture.
- Idée principale : un faux tableau créé avec des espaces ou des barres verticales doit être réécrit en texte linéarisé.
- Scène : à gauche, une publication affiche un faux tableau en deux colonnes avec espaces et barres verticales ; au centre, un lecteur d'écran lit les fragments dans le désordre, marqué comme problème ; à droite, le contenu est transformé en post clair linéarisé, avec une description longue ou un lien accessible si les données sont denses.
- Transformation : faux tableau -> lu dans le désordre -> texte linéarisé.
- Image seule : ce qui semble aligné visuellement peut devenir incompréhensible ; la solution est de reformuler en texte linéaire ou de renvoyer vers un support accessible.
- Contraintes critiques : ne pas écrire de fausse colonne longue, ne pas afficher de vrai tableau accessible, conserver les labels exacts, marquer `Lu dans le désordre` comme problème, ne pas utiliser `Liste simple`, afficher `Post clair`, `Description longue` et `Lien accessible` comme alternatives.
- Risque à éviter : confondre faux tableau et tableau accessible, densifier la slide.

## Slide 34 - Checklist émojis

- Source : V2-13.
- Rubrique : Texte et signes.
- Rôle : transformer les règles sur les émojis en contrôle de publication.
- Idée principale : chaque émoji doit être vérifié sur le sens, le nombre et la position.
- Scène : une personne relit une publication avec une grille de contrôle en trois zones ; à gauche, le message reste lisible sans émoji ; au centre, les mots clés et chiffres restent écrits ; à droite, les émojis sont rares et placés en fin de phrase.
- Transformation : publication décorée -> suppression temporaire des émojis -> message encore compréhensible.
- Image seule : l'émoji est un complément, jamais le porteur unique du sens.
- Contraintes critiques : checklist limitée aux cinq labels, ne pas afficher de formulation interdite longue comme `Inscription lien bio`, ne pas intercaler d'émojis entre les mots, conserver le texte exact.
- Risque à éviter : rendre la checklist trop dense, suggérer que tous les émojis sont interdits.

## Slide 35 - Checklist caractères spéciaux

- Source : V2-14.
- Rubrique : Texte et signes.
- Rôle : transformer les règles Unicode en contrôle avant publication.
- Idée principale : les caractères spéciaux ne doivent jamais simuler du style, une structure ou une urgence.
- Scène : une personne inspecte une publication avec un filtre de contrôle ; plusieurs pièges sont barrés : faux gras ou italique, police fantaisie, fausses puces, ASCII art, faux tableau et ponctuation excessive. La règle orale précise que, sur LinkedIn, une liste accessible se structure avec un tiret standard, une numérotation `1. 2. 3.` ou, avec prudence, un émoji unique accompagné d'un texte réel.
- Transformation : texte décoré -> pièges détectés -> texte simplifié.
- Image seule : les caractères spéciaux deviennent dangereux quand ils remplacent une vraie mise en forme ou une vraie structure ; pour les listes, on privilégie tiret standard, numéros et texte réel plutôt que symboles décoratifs ou séries d'émojis.
- Contraintes critiques : ne pas écrire de long ASCII art, ne pas reproduire `★彡 Titre 彡★` en grand, ne pas afficher de ponctuation excessive attractive ni de bloc entier en majuscules, conserver les huit labels exacts.
- Risque à éviter : donner envie d'utiliser les exemples décoratifs, confondre ponctuation normale et ponctuation excessive.

## Slide 36 - Relire avant de publier

- Source : V2-15.
- Rubrique : Texte et signes.
- Rôle : conclure par un geste de production.
- Idée principale : l'accessibilité se vérifie avec quatre contrôles, puis l'information importante est diffusée sur un support accessible.
- Scène : une grande carte de décision éditoriale, sans métaphore d'envoi. À gauche, une publication prête à relire. Au centre, un bloc intitulé `4 contrôles` regroupe clairement `Sens`, `Nombre`, `Position` et `Texte réel`. À droite, un bloc séparé intitulé `Canal accessible` montre une page ou un document accessible très sobre, sans enveloppe, sans smartphone et sans icônes de destination multiples.
- Transformation : publication prête -> 4 contrôles -> canal accessible.
- Image seule : publier accessible demande une vérification courte et explicite ; le canal accessible est l'étape après contrôle, pas un cinquième pilier.
- Contraintes critiques : les quatre contrôles doivent être visuellement groupés ensemble sous `4 contrôles` ; rappeler à l'oral de tester les outils de programmation pour vérifier qu'ils conservent les textes alternatifs et sous-titres ; `Canal accessible` doit être séparé comme étape après contrôle et pas comme cinquième pilier ; ne pas utiliser d'enveloppe, de smartphone, d'email, de réseau social, de mégaphone ou de pictogramme de diffusion ambigu ; aucun logo, aucune promesse de conformité automatique, aucun numéro de progression, conserver le texte exact.
- Risque à éviter : métaphore de diffusion ambiguë, checklist trop longue, faux logo, scène administrative froide sans action visible.

## Slide 37 - Placer le lien dans le post

- Source : V2-16.
- Rubrique : Liens et actions.
- Rôle : préciser le canal le plus robuste pour l'action à accomplir.
- Idée principale : le lien essentiel est plus accessible quand il reste dans la publication principale, à la fin du message et avec un texte d'action clair.
- Scène : une comparaison gauche-droite. À gauche, une publication principale contient le message puis un lien clair en fin de post ; le parcours est direct vers une page accessible. À droite, le lien est envoyé vers un commentaire séparé, ce qui ajoute une étape et une incertitude.
- Transformation : action dans le post -> parcours direct ; action déportée -> détour.
- Image seule : le lien dans le post principal est plus simple à trouver et à suivre.
- Contraintes critiques : ne pas citer de plateforme, ne pas afficher de logo, ne pas dessiner une vraie interface, ne pas suggérer que le commentaire est toujours interdit, conserver le texte exact.
- Risque à éviter : transformer la slide en débat algorithmique, minimiser le parcours utilisateur.

## Slide 38 - Le commentaire ajoute un détour

- Source : V2-17.
- Rubrique : Liens et actions.
- Rôle : expliquer pourquoi le premier commentaire est une zone de risque.
- Idée principale : même épinglé, un commentaire peut être moins atteignable au clavier, moins lisible par lecteur d'écran ou moins visible selon l'interface.
- Scène : un post principal pointe vers une zone de commentaires. Le chemin passe par plusieurs obstacles : ouvrir les commentaires, trouver le commentaire épinglé, vérifier l'accès clavier et garder la découvrabilité. Une carte de correction rappelle qu'il faut contrôler ce parcours si la stratégie impose le commentaire.
- Transformation : post principal -> commentaires -> obstacles -> contrôle nécessaire.
- Image seule : l'information essentielle ne doit pas dépendre d'un espace séparé non vérifié.
- Contraintes critiques : ne pas affirmer que tous les commentaires sont inaccessibles, ne pas citer Instagram ou LinkedIn comme logos, ne pas afficher de données de recherche inventées, conserver le texte exact.
- Risque à éviter : faire croire qu'un commentaire épinglé résout automatiquement l'accessibilité.

## Slide 39 - Écrire l'action explicitement

- Source : V2-18.
- Rubrique : Liens et actions.
- Rôle : rappeler que la qualité du lien dépend du texte d'appel à l'action.
- Idée principale : que le lien soit dans le post ou dans un commentaire, son libellé doit dire clairement la destination ou l'action.
- Scène : à gauche, deux formulations vagues sont barrées : `Lien 👇` et `Cliquez ici`. À droite, deux formulations explicites sont validées : `Télécharger le guide RGAA en PDF` et `Consulter la checklist`. Une miniature d'aperçu tronqué montre pourquoi le texte autour du lien doit suffire.
- Transformation : appel vague -> destination inconnue -> action explicite.
- Image seule : le problème n'est pas l'URL seule, mais l'absence de finalité explicite.
- Contraintes critiques : afficher exactement `Lien 👇`, `Cliquez ici`, `Télécharger le guide RGAA en PDF` et `Consulter la checklist`, ne pas afficher de vraie URL, ne pas ajouter de logo, conserver le texte exact ; préciser à l'oral qu'un lien raccourci opaque doit être précédé d'un texte d'action parfaitement explicite.
- Risque à éviter : rendre `Cliquez ici` trop séduisant, laisser croire que l'URL brute suffit.

## Slide 40 - Utiliser le commentaire en réparation

- Source : V2-19.
- Rubrique : Liens et actions.
- Rôle : distinguer la stratégie éditoriale discutable de l'usage utile du commentaire après publication.
- Idée principale : le commentaire peut servir de roue de secours quand une plateforme empêche de corriger le post principal.
- Scène : une publication déjà publiée affiche un défaut d'accessibilité : alternative textuelle manquante, transcription absente ou lien corrigé. Une flèche mène vers un commentaire de réparation épinglé, qui contient une alternative, une transcription ou un lien corrigé.
- Transformation : défaut après publication -> impossibilité de modifier -> commentaire de réparation.
- Image seule : le commentaire est utile pour corriger un défaut, pas pour cacher par défaut l'action principale.
- Contraintes critiques : ne pas suggérer que le commentaire remplace une correction native quand elle est possible, ne pas afficher de logo de plateforme, conserver le texte exact.
- Risque à éviter : normaliser le commentaire comme emplacement principal des liens.

## Slide 41 - Faire des listes accessibles

- Source : V2-22.
- Rubrique : Texte et signes.
- Rôle : donner l'alternative concrète aux fausses puces et aux listes simulées.
- Idée principale : quand l'éditeur ne propose pas de vraies puces, on structure avec des signes simples et prévisibles, sans détourner des caractères décoratifs.
- Scène : une comparaison en deux colonnes. À gauche, une carte `À éviter` montre des symboles décoratifs utilisés comme puces et une ligne avec plusieurs émojis répétés en début de ligne ; la sortie audio devient bruyante. À droite, une carte `À privilégier` montre trois options sobres : tiret standard, liste numérotée et émoji unique accompagné d'un texte réel.
- Transformation : fausses puces décoratives -> bruit audio -> structure simple.
- Image seule : les alternatives accessibles sont simples, textuelles et prévisibles.
- Contraintes critiques : afficher exactement `Tiret standard`, `Liste numérotée` et `Émoji unique + texte` côté solution ; ne pas utiliser de faux caractère décoratif séduisant en grand ; ne pas afficher une vraie interface LinkedIn ou un logo ; ne pas écrire de longue liste ; conserver le texte exact.
- Risque à éviter : faire croire que les listes sont impossibles sur les réseaux, confondre tiret standard et symbole décoratif.

## Slide 42 - Calmer la ponctuation bruyante

- Source : V2-23.
- Rubrique : Texte et signes.
- Rôle : isoler le cas de la ponctuation excessive, déjà mentionnée dans la checklist.
- Idée principale : la ponctuation doit aider le sens ; répétée en série, elle devient bruyante à l'écoute et agressive à la lecture.
- Scène : à gauche, une publication affiche une alerte avec une série de points d'exclamation et de points d'interrogation ; la sortie audio est longue et instable. À droite, la même intention est reformulée avec des mots clairs, une ponctuation sobre et un niveau d'urgence explicite.
- Transformation : ponctuation répétée -> vocalisation bruyante -> phrase claire.
- Image seule : réduire les signes répétés améliore la lecture visuelle et vocale.
- Contraintes critiques : ne pas afficher une longue série exacte de points d'exclamation en grand, ne pas créer un effet d'urgence séduisant, rouge seulement sur le problème, conserver le texte exact.
- Risque à éviter : confondre ponctuation normale et ponctuation excessive, donner une règle punitive.

## Slide 43 - Proscrire les séries bruyantes

- Source : V2-24.
- Rubrique : Texte et signes.
- Rôle : formuler la règle opérationnelle à retenir sur la ponctuation.
- Idée principale : les séries de ponctuation comme `!!!` ou `???` créent une décoration sonore, une charge cognitive inutile et doivent être remplacées par du langage clair.
- Scène : une comparaison avant/après très explicite. À gauche, une carte rouge `À fuir` montre `ALERTE !!!!!!` avec deux problèmes visibles : majuscules continues et ponctuation répétée. Une sortie audio hachée matérialise la décoration sonore. À droite, une carte bleue `À privilégier` montre `Important :` avec une seule majuscule initiale, une ponctuation sobre et une lecture calme.
- Transformation : emphase visuelle bruyante -> charge cognitive -> langage clair.
- Image seule : l'avant cumule majuscules et ponctuation, l'après formule l'urgence en texte clair.
- Contraintes critiques : afficher exactement `ALERTE !!!!!!` seulement dans la carte `À fuir`, afficher exactement `Important :` dans la carte `À privilégier`, ne pas transformer `Pas de MAJUSCULES` en interdiction des majuscules initiales, ne pas ajouter d'autres exemples, rouge seulement sur l'avant, conserver le texte exact.
- Risque à éviter : rendre l'alerte attractive, confondre majuscule initiale et mot entier en majuscules, densifier la slide.

## Slide 44 - Contrôler les signes avant publication

- Source : V2-25.
- Rubrique : Texte et signes.
- Rôle : conclure en nommant la famille complète à contrôler.
- Idée principale : les émojis, hashtags, ponctuations répétées, faux styles et symboles décoratifs appartiennent au même contrôle éditorial.
- Scène : une table de relecture rassemble cinq cartes déjà vues dans la série : émojis, hashtags, ponctuation, faux style et faux décors. Elles convergent vers une carte finale de validation qui porte la formule de synthèse.
- Transformation : signes dispersés -> famille de contrôle -> publication relue.
- Image seule : le sujet n'est pas seulement les émojis ; toute mise en forme simulée ou tout signe non alphabétique doit être contrôlé.
- Contraintes critiques : la formule `éléments non alphabétiques, ponctuation et caractères spéciaux` doit être lisible ; ne pas inventer une nouvelle règle contradictoire avec les quatre contrôles ; ne pas afficher d'enveloppe ou de smartphone ; aucun logo ; conserver le texte exact.
- Risque à éviter : conclusion trop abstraite, liste trop dense, confusion entre signes utiles et signes interdits.

## Slide 45 - Image décorative : quelle solution ?

- Source : V2-26.
- Rubrique : Images et carrousels.
- Rôle : ouvrir le chapitre des images avec le cas décoratif.
- Idée principale : Une image décorative ne doit pas ajouter de bruit à l'écoute ; le geste dépend de l'option proposée par la plateforme.
- Scène : Deux chemins : option Décorative native, ou mention Image décorative dans le texte alternatif quand l'option manque.
- Transformation : image décorative -> choix de plateforme -> silence ou exception textuelle courte
- Image seule : l'image décorative ne doit pas être décrite longuement, mais il faut éviter l'auto-description automatique bruyante.
- Contraintes critiques : ne pas recommander un champ vide sur une plateforme qui ne permet pas de déclarer l'image décorative ; conserver la règle validée.
- Risque à éviter : appliquer mécaniquement la règle du Web sans tenir compte des possibilités de la plateforme.

## Slide 46 - Décrire l'image informative

- Source : V2-27.
- Rubrique : Images et carrousels.
- Rôle : poser la règle stricte pour les images qui portent de l'information.
- Idée principale : toute image informative doit avoir un texte alternatif manuel qui restitue l'information utile.
- Scène : une publication contient une image qui porte un message. Une personne relit le champ Alt et transforme l'image en un texte alternatif court, placé dans un bloc de validation. Les mauvaises pratiques sont barrées : redite, mots-clés SEO et description physique inutile.
- Transformation : message visuel -> Alt text manuel -> information restituée.
- Image seule : le champ alternatif sert à transmettre l'information décisive, pas à tout décrire ni à référencer le post.
- Contraintes critiques : ne pas commencer l'alt par `image de` ou `photo de` en exemple principal, ne pas bourrer le champ de mots-clés, ne pas décrire des attributs physiques sans raison, conserver le texte exact.
- Risque à éviter : donner une description trop longue, transformer la slide en norme technique RGAA détaillée, faire croire que l'auto-alt suffit.

## Slide 47 - Retaper le texte incrusté

- Source : V2-28.
- Rubrique : Images et carrousels.
- Rôle : traiter le piège courant des affiches et visuels événementiels.
- Idée principale : le texte visible dans l'image doit aussi exister en vrai texte dans le post ou dans une description longue.
- Scène : à gauche, une affiche d'événement contient une date, un lieu et une information pratique uniquement dans l'image. Une alerte signale que l'apparence porte seule l'information. À droite, les mêmes éléments sont recopiés dans le texte du post ou dans une description longue.
- Transformation : texte piégé dans l'image -> information inaccessible -> texte recopié.
- Image seule : une affiche lisible visuellement ne suffit pas si son texte n'est pas disponible comme texte réel.
- Contraintes critiques : ne pas inventer de vraie date ou adresse détaillée, ne pas afficher une affiche trop riche, conserver les labels exacts, ne pas faire croire que le champ Alt remplace toujours le texte du post.
- Risque à éviter : densifier la slide, faire croire que l'image doit être interdite, oublier la description longue.

## Slide 48 - Prévoir une description longue

- Source : V2-29.
- Rubrique : Images et carrousels.
- Rôle : traiter les graphiques, infographies et carrousels denses.
- Idée principale : quand l'image est trop dense pour un champ Alt, il faut fournir une description longue accessible.
- Scène : un graphique dense entre dans un petit champ Alt qui déborde. La solution montre un Alt court qui annonce une description longue, puis un bloc lisible contenant la conclusion et les valeurs clés, dans le post ou via un lien accessible.
- Transformation : visuel complexe -> Alt insuffisant -> description longue structurée.
- Image seule : l'alt court oriente, la description longue donne le fond.
- Contraintes critiques : ne pas créer un graphique avec données réelles inventées, ne pas faire tenir toute l'infographie dans l'alt, ne pas oublier `Conclusion` et `Valeurs clés`, conserver le texte exact.
- Risque à éviter : transformer la description longue en pièce jointe inaccessible, confondre alt court et absence d'alternative.

## Slide 49 - Fournir une version texte des carrousels

- Source : V2-30.
- Rubrique : Images et carrousels.
- Rôle : compléter le chapitre multimédia après les images fixes et infographies.
- Idée principale : un carrousel social n'est pas une simple image ; s'il porte une méthode, des données ou plusieurs étapes, il doit exister en version texte.
- Scène : un carrousel de plusieurs cartes informatives est comparé à une version texte complète dans le post ou via un lien accessible ; un document PDF est montré comme non automatiquement accessible s'il n'est pas balisé.
- Transformation : carrousel dense -> version texte complète -> accès fiable.
- Image seule : quand le carrousel contient une vraie information, il faut offrir une alternative textuelle complète.
- Contraintes critiques : ne pas inventer de données, ne pas afficher un vrai logo PDF propriétaire, ne pas suggérer qu'un PDF LinkedIn est accessible par défaut, conserver le texte exact.
- Risque à éviter : transformer la slide en mode d'emploi PDF, rendre le carrousel illisible, oublier la version texte.

## Slide 50 - Relire les sous-titres automatiques

- Source : V2-31.
- Rubrique : Vidéos.
- Rôle : poser la règle minimale pour les vidéos parlées.
- Idée principale : les sous-titres automatiques sont des brouillons ; ils doivent être relus et corrigés avant publication.
- Scène : une vidéo parlée génère des sous-titres automatiques avec erreurs ; une étape de relecture corrige les noms propres, sigles, chiffres et sons utiles au sens.
- Transformation : sous-titres automatiques -> erreurs détectées -> sous-titres corrigés.
- Image seule : publier la vidéo sans relire les sous-titres automatiques laisse des erreurs d'accès.
- Contraintes critiques : ne pas inventer de sous-titre réel, ne pas afficher de visage réel, ne pas citer de plateforme, conserver le texte exact, montrer les sons utiles comme information à intégrer.
- Risque à éviter : faire croire que l'automatique suffit, réduire les sous-titres aux personnes sourdes uniquement, densifier la piste.

## Slide 51 - Décrire l'action visuelle non parlée

- Source : V2-32.
- Rubrique : Vidéos.
- Rôle : montrer que les sous-titres ne suffisent pas si l'information importante n'est jamais dite.
- Idée principale : une vidéo qui montre une action ou une information sans la dire doit compenser cette information par un script vocal, une audiodescription ou une transcription.
- Scène : une vidéo muette montre un itinéraire ou un tutoriel visuel ; le parcours de correction ajoute un script vocal, une audiodescription ou une transcription textuelle.
- Transformation : action muette -> sens perdu -> compensation textuelle ou audio.
- Image seule : ce qui n'est ni parlé ni décrit reste inaccessible à une partie du public.
- Contraintes critiques : ne pas faire une vidéo réelle, ne pas afficher de carte ou itinéraire précis, conserver le texte exact, ne pas suggérer que les sous-titres couvrent tout.
- Risque à éviter : rendre l'audiodescription optionnelle quand elle porte le sens, confondre transcription et résumé marketing.

## Slide 52 - Sécuriser la lecture vidéo

- Source : V2-33.
- Rubrique : Vidéos.
- Rôle : protéger l'attention, la santé et le contrôle utilisateur dans les contenus animés.
- Idée principale : les flashs rapides, transitions agressives, autoplay, son imprévisible et GIF non contrôlable peuvent exclure une partie de l'audience.
- Scène : une vidéo avec flashs, son automatique et GIF en boucle est marquée comme risquée ; une version corrigée montre une lecture contrôlée avec pause, son maîtrisé et transitions calmes.
- Transformation : animation imposée -> risque -> contrôle utilisateur.
- Image seule : la sécurité d'un contenu animé dépend du rythme, du contrôle et de la possibilité de pause.
- Contraintes critiques : ne pas simuler un flash violent dans l'image, ne pas créer d'effet agressif, rouge seulement sur le risque, conserver le texte exact, ne pas citer de plateforme.
- Risque à éviter : slide elle-même visuellement agressive, banaliser les GIF en boucle, oublier le contrôle du son.

## Slide 53 - Alléger la charge cognitive

- Source : V2-34.
- Rubrique : Clarté éditoriale.
- Rôle : passer de la forme au fond du message.
- Idée principale : l'accessibilité ne dépend pas seulement des signes et des images ; la clarté rédactionnelle réduit l'effort de compréhension.
- Scène : une publication dense est relue par une personne. Les phrases longues sont simplifiées en cartes courtes : une idée par phrase, acronyme développé, date complète, ordre logique et mot simple.
- Transformation : texte dense -> effort cognitif -> message clarifié.
- Image seule : écrire clairement rend le post plus facile à comprendre pour tout le monde.
- Contraintes critiques : ne pas réduire le langage clair à une simplification infantilisante, ne pas afficher de paragraphe dense illisible, conserver les labels exacts, ne pas utiliser d'acronyme non développé dans l'exemple.
- Risque à éviter : faire une slide de conseils génériques sans transformation visible, confondre langage clair et FALC.

## Slide 54 - Corriger après publication

- Source : V2-36.
- Rubrique : Après publication.
- Rôle : ouvrir la conclusion opérationnelle sur le service après-vente éditorial.
- Idée principale : l'accessibilité continue après publication ; un signalement doit déclencher une correction ou une alternative publiée.
- Scène : une publication reçoit un commentaire de signalement. Le parcours de décision propose d'abord `Corriger le post` si la plateforme le permet. Si la correction native est bloquée, une alternative manquante est publiée en commentaire épinglé : texte alternatif, sous-titres, transcription ou lien corrigé.
- Transformation : défaut signalé -> correction native ou réparation épinglée.
- Image seule : un retour utilisateur n'est pas un embarras, c'est une boucle de correction.
- Contraintes critiques : ne pas faire croire que le commentaire est la première solution si le post peut être corrigé, ne pas afficher de logo ni de vraie interface, conserver le texte exact.
- Risque à éviter : redondance avec la slide 19 sans notion de signalement, minimiser la correction native, présenter la réparation comme option facultative.

## Slide 55 - Mesurer les vrais KPI d'accessibilité

- Source : V2-37.
- Rubrique : Après publication.
- Rôle : conclure par des indicateurs de pilotage plutôt que par la seule portée.
- Idée principale : un post viral inaccessible reste un échec d'accessibilité ; il faut mesurer les pratiques qui rendent les contenus accessibles.
- Scène : un tableau de bord compare deux familles d'indicateurs. À gauche, les métriques de portée seules, comme likes et vues, ne suffisent pas. À droite, les KPI d'accessibilité sont validés : images avec vrai Alt text, vidéos relues, sous-titres contrôlés et délai de correction d'un défaut signalé.
- Transformation : succès viral incomplet -> tableau de bord d'accessibilité -> pilotage utile.
- Image seule : la performance éditoriale doit inclure des indicateurs d'accès réel, pas seulement de visibilité.
- Contraintes critiques : ne pas inventer de pourcentage, ne pas afficher de données de performance réelles, ne pas transformer les likes en objectif principal, conserver le texte exact.
- Risque à éviter : conclusion marketing, tableau de bord trop dense, indicateurs trop techniques pour des communiquants.

## Validation croisée avant génération

- Les slides 1 à 22 conservent la correspondance exacte avec le PPTX.
- Les slides 23 à 55 sont explicitement identifiées comme conclusion et annexes.
- Les 55 slides possèdent une image, une transcription et un discours oral.
- Les 33 nouveaux visuels respectent le preset IGPDE bleu illustré.
- La règle des images décoratives distingue l'option native et l'exception des réseaux sociaux.
- Le séparateur annonce les 31 fiches sans les transformer en parcours obligatoire.
