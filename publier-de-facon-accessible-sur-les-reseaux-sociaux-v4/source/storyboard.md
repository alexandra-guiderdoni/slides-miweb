Publier de façon accessible sur les réseaux sociaux - V4
=========================================================

## Contrat de série

- Source pédagogique : slides 110 à 131 du support IGPDE 102846.
- Correspondance : 22 visuels web pour 22 slides PPTX, dans le même ordre.
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
- Navigation : les titres des 22 fiches restent identiques aux titres PPTX pour maintenir la correspondance 1 pour 1.

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

## Validation croisée avant génération

- Verdict : corrections P1 intégrées au storyboard ; passage en génération soumis au contrôle ciblé final.
- Les 22 titres et leur ordre correspondent aux 22 fichiers source.
- Les listes blanches visuelles ont été complétées ou réduites à des formulations de la même slide.
- Le tableau de la slide 10 est condensé dans l’image et conservé intégralement en HTML sémantique.
- Le repère de progression est porté par l’interface web et n’ajoute aucun texte dans le visuel.
- Le traitement du masque PPTX est explicite.
- La confidentialité de la slide 22 reste un drapeau ouvert et bloque seulement l’ajout des coordonnées, pas la production d’une clôture neutre.
