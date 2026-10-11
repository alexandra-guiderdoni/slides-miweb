Quatre séries Opquast exhaustives : notes cuisine-moi
===================================================

Date : 2026-10-11 | Objectif : cadrer un Goal gouverné pour produire quatre jeux de slides exhaustifs à partir des storyboards et notes Markdown de Formations-MIWEB.

## Résumé / décisions clés

- Chaque série doit couvrir tout le contenu pertinent de ses sources, sans plafond de slides.
- Le nombre de slides s’adapte au contenu ; toute condensation entraînant la suppression d’une information utile est interdite.
- Les jeux doivent respecter la fabrique V2, la continuité visuelle des séries Opquast, le contrat de `slides-miweb` et les deux accordéons par slide.
- Le chantier porte sur exactement quatre séries.
- Les PPTX et accordéons existants sont hors périmètre et ne doivent pas servir de sources.
- Les six Markdown nommés sont l’unique source de contenu métier. Rien ne doit
  être inventé ni complété depuis le modèle, le Web, un support, le MCP ou un
  skill. Chaque élément métier visible ou oral doit être rattaché à des lignes
  précises de ces Markdown.
- Les guides applicables, le MCP Opquast et le skill `opquast-skill` sont les
  références de contrôle : ils peuvent confirmer ou rejeter une affirmation
  trouvée dans les Markdown. En cas de doute, ils doivent être consultés. Ils
  ne fournissent jamais silencieusement un contenu absent du corpus.
- Série « projets et livrables » : `inventaire-59-livrables-V008.md` et `storyboard-opquast-livrables-phases-V008-consolide.md`.
- Série « construction d’une règle » : `storyboard-opquast-construire-regle-60min-v006.md` et `deroule-animation-construire-regle-60min-v006.md`.
- Série « sécurité » : `conversation-opquast-securite.md`.
- Série « performance » : `conversation-opquast-performance.md`.
- Si une candidate `image_gen` n’est pas nativement en 1672 × 941 px, un
  redimensionnement proportionnel est autorisé uniquement si son ratio est déjà
  16:9. Aucun recadrage, ajout ou surimpression n’est autorisé. Si le ratio
  diffère, arrêter la série et demander un arbitrage.
- L’ordre de production validé est : Construction d’une règle, Projets et
  livrables, Sécurité, Performance. Construction d’une règle sert de pilote
  pour vérifier toute la chaîne jusqu’à la publication GitHub Pages.
- La série Construction d’une règle vise un double usage : ses images
  préservent la progression, les votes et les corrections différées de
  l’animation ; ses deux accordéons la rendent compréhensible en consultation
  autonome sans révéler une correction avant la slide prévue.
- Aucun lot n’a de plafond de slides. Pour Construction d’une règle, les 16
  slides V006 constituent une base à développer, déplacer ou scinder autant que
  nécessaire pour couvrir clairement toute la thématique. Le parcours principal
  peut dépasser 16 slides et des annexes peuvent compléter la série.
- Construction d’une règle suit un double parcours : la série complète reste
  exhaustive et sans plafond ; une sélection ordonnée de ses slides constitue
  le parcours essentiel de 60 minutes. Les autres slides sont identifiées comme
  approfondissements ou annexes facultatives. Une même slide n’est pas
  dupliquée entre les parcours.
- Les deux accordéons de Construction d’une règle contiennent uniquement le
  contenu métier. Les consignes d’animation, de régie, de vote, de durée ou de
  gestion du groupe en sont exclues et restent disponibles dans le conducteur
  source.
- L’identité publique de Construction d’une règle est verrouillée : slug
  `construction-regle-opquast-v5`, titre « Comment se construit une règle
  Opquast ? », footer `RÈGLES OPQUAST · CONSTRUIRE UNE RÈGLE` et pagination
  calculée sur le nombre final de slides.
- Les 59 livrables ou objets de projet sont traités par 12 séquences de
  familles, chacune occupant autant de slides que nécessaire. Chaque livrable
  est nommé ; sa fonction, son contexte, son risque utilisateur, son examen
  possible, sa limite et sa provenance restent traçables dans la matrice de
  couverture et sont répartis entre slides et discours oraux.
- Projets et livrables conserve les 23 slides V008 comme parcours principal,
  puis ajoute l’atlas exhaustif des 12 familles. La matrice de couverture
  attribue chaque information à un emplacement principal et interdit les
  répétitions entre le parcours et l’atlas.
- Projets et livrables suit un double parcours : les 23 slides V008 forment le
  parcours essentiel de 60 minutes ; l’atlas des 12 familles est publié dans la
  même série comme approfondissement facultatif hors minutage. Une même slide
  n’est pas dupliquée.
- L’identité publique de Projets et livrables est verrouillée : slug
  `projets-livrables-opquast-v5`, titre « Projets et livrables selon Opquast
  V5 », footer `RÈGLES OPQUAST · PROJETS ET LIVRABLES`. Le slogan « La qualité
  circule, la preuve se construit » reste limité à l’ouverture et à la synthèse.
- Sécurité suit le même double parcours : la série complète reste exhaustive et
  sans plafond ; une sélection ordonnée forme le parcours essentiel de
  60 minutes ; le reste devient approfondissements ou annexes facultatives,
  sans duplication d’image.
- L’identité publique de Sécurité est verrouillée : slug
  `securite-opquast-v5`, titre « Sécurité selon Opquast V5 », footer
  `RÈGLES OPQUAST · SÉCURITÉ`. La phrase centrale reste limitée à l’ouverture
  et à la synthèse.
- Performance suit le même double parcours : la série complète reste
  exhaustive et sans plafond ; une sélection ordonnée forme le parcours
  essentiel de 60 minutes ; le reste devient approfondissements ou annexes
  facultatives, sans duplication d’image.
- L’identité publique de Performance est verrouillée : slug
  `performance-opquast-v5`, titre « Performance selon Opquast V5 », footer
  `RÈGLES OPQUAST · PERFORMANCE`. Les deux phrases centrales restent limitées à
  l’ouverture et à la synthèse.
- Chaque série possède son propre gate humain de quatre slides étalons : une
  ouverture, une règle ou notion centrale, un regroupement ou éclairage et une
  synthèse. Après présentation du storyboard, des textes visibles, du prompt,
  du visuel, de la transcription et du discours oral, la production s’arrête
  jusqu’à validation explicite d’Alex.
- La compréhension partagée est confirmée et la cuisine est close. Le Goal doit
  intégrer toutes les décisions de cette trace avant son exécution.
- La définition de terminé inclut la publication locale et la publication
  GitHub Pages. Les fichiers de la mission doivent être commités et poussés sur
  `main` dans les deux dépôts autonomes : le workspace Opquast et
  `slides-miweb`. Aucun changement étranger ne doit être indexé ou publié.
- Le dépôt public cible est
  `https://github.com/alexandra-guiderdoni/slides-miweb`. Le site cible est
  `https://alexandra-guiderdoni.github.io/slides-miweb/`, dont la page d’accueil
  doit présenter les quatre nouvelles séries.

## Risques vérifiés avant lancement

- Les six sources représentent 4 273 lignes et 256 260 octets. Le principal
  risque éditorial est une couverture incomplète ou, à l’inverse, une série
  artificiellement gonflée par des répétitions non dédupliquées.
- Le retour d’expérience historique de la Fabrique documente des numéros de
  règles inversés, un mapping erroné, une ambiguïté lexicale sur « tiers » et
  une dérive graphique propagée par une génération en gros lots.
- L’interface `image_gen` disponible dans la session ne propose pas de champ de
  dimensions. Des séries historiques ont bien produit des PNG de 1672 × 941 px,
  mais cette dimension n’est pas encore vérifiée avec l’interface actuelle.
- Les quatre slugs proposés sont actuellement libres dans `slides-miweb`.
- Les scripts de création, validation, optimisation, serveur local et
  publication locale sont présents, mais ils n’ont pas encore été exécutés
  pour ces quatre séries.
- Le dépôt `slides-miweb` contient déjà une modification étrangère dans
  `DEMARCHE-VERSIONS.md`. Elle doit rester intacte. La présente trace est aussi
  non suivie par Git.
- La validation humaine porte sur quatre slides étalons par série, soit seize
  slides regroupées en quatre gates avant toute généralisation du style.
- La publication initialement prévue comme locale seulement est remplacée par
  la décision Q20 : commits et push sur `main` dans les deux dépôts, puis
  publication et vérification GitHub Pages.

## Décisions Sécurité déjà présentes dans la source

- Public : candidats à la certification Opquast issus de profils numériques
  variés.
- Objectifs : comprendre la logique Opquast, mémoriser les règles et préparer
  la certification.
- Niveau technique : intermédiaire, avec explication simple des notions.
- Structure : grappes de risques et situations utilisateur, pas catalogue règle
  par règle.
- Fil conducteur : préjudice utilisateur, perte de maîtrise, règles, bénéfice
  limité et point de mémorisation.
- Point de vue organisationnel : second niveau, sans déplacer l’utilisateur du
  centre.
- Frontière : section explicite sur ce qu’Opquast couvre et sur ce qui relève
  d’une démarche spécialisée de cybersécurité.
- Transversalité : uniquement les règles dont le lien matériel avec la sécurité
  est étayé ; ne pas diluer la sécurité dans toute la qualité numérique.
- Privacy : zones de recouvrement traitées en annexe, sans refaire la série
  Données personnelles.
- Accessibilité : tensions avec la sécurité intégrées lorsqu’elles sont
  documentées par les sources.
- Angles morts cyber modernes : aucune comparaison systématique externe ; rester
  centré sur Opquast.
- Histoire : courte généalogie de la sécurité chez Opquast, sans histoire
  générale de la cybersécurité.
- Format initial demandé dans la conversation : une heure.
- Double parcours : une sélection ordonnée forme le parcours essentiel de
  60 minutes ; la série complète reste exhaustive et sans plafond. Les autres
  slides sont des approfondissements ou annexes facultatives, sans duplication
  d’image.
- Idée centrale : « La sécurité Opquast, c’est d’abord prévenir des risques
  concrets pour l’utilisateur. »

## Décisions Performance déjà présentes dans la source

- Public : candidats à la certification Opquast issus de profils numériques
  variés.
- Objectifs : comprendre la logique Opquast, mémoriser les règles et préparer
  la certification.
- Niveau technique : intermédiaire, avec explication simple des notions.
- Structure : grappes de risques et situations utilisateur, pas catalogue de
  la rubrique « Serveur et performances ».
- Fil conducteur : l’utilisateur paie la performance avec son temps, ses
  données et les ressources de son terminal.
- Point de vue organisationnel : second niveau, sans déplacer l’utilisateur du
  centre.
- Frontière : « Serveur et performances » n’est pas synonyme de performance ;
  Opquast fournit un socle, pas un audit Web Performance spécialisé.
- Noyau direct : règles 119, 226, 227, 229 et 230.
- Maîtrise de la consommation : règles 123, 124, 147 et 148.
- Transversalité : UX, accessibilité contextuelle, écoconception, SEO et coûts
  d’infrastructure sont reliés sans être confondus.
- Contextes d’usage : réseau faible, mobilité, itinérance, appareil ancien et
  données mobiles limitées.
- Format initial demandé dans la conversation : une heure.
- Idée centrale : « Performance Opquast = ne pas faire attendre, télécharger
  ou calculer inutilement l’utilisateur. »
- Distinction mémorisable : « Rapide n’est pas forcément léger, affiché n’est
  pas forcément utilisable. »

## Journal questions-réponses

### Q1 - Source de vérité de `construction-regle`
- Question : faut-il reconstruire cette série depuis le storyboard V006 de 16 slides, en traitant le PPTX et les accordéons actuels de 11 slides comme des références historiques seulement, ou préserver la structure actuelle de 11 slides et l’étendre ?
- Capture : Alex exclut les PPTX existants. La série doit utiliser uniquement le storyboard V006 et le conducteur V006. Le chantier comprend exactement quatre séries fondées sur les six fichiers explicitement désignés.
- Drapeaux : aucun.

### Q2 - Sens de la couverture exhaustive
- Question : pour les fichiers de conversation « sécurité » et « performance », faut-il couvrir chaque idée métier, règle, distinction, risque, limite et mémo au moins une fois, tout en excluant les répétitions et les échanges de pilotage, ou faut-il aussi restituer la conversation brute et ses répétitions ?
- Capture : Alex choisit la couverture métier exhaustive et dédupliquée. Chaque règle, distinction, risque utilisateur, garantie, limite, piège, mémo et relation utile doit apparaître au moins une fois. Les relances, acquiescements, prompts préparatoires et répétitions sans apport sont exclus.
- Drapeaux : aucun.

### Q3 - Dimensions produites par `image_gen`
- Question : si la première candidate n’est pas nativement en 1672 × 941 px,
  faut-il arrêter, autoriser un redimensionnement proportionnel d’une sortie
  déjà en 16:9, ou autoriser aussi un recadrage ou un ajout de marges ?
- Capture : Alex valide le redimensionnement proportionnel uniquement lorsque
  la sortie est déjà en 16:9. Le traitement ne doit comporter aucun recadrage,
  ajout ni surimpression. Un ratio différent impose l’arrêt et un nouvel
  arbitrage.
- Drapeaux : aucun.

### Q4 - Ordre des séries et choix du pilote
- Question : faut-il conserver l’ordre initial du Goal, commencer par
  Construction d’une règle comme pilote, ou ouvrir les quatre séries par leurs
  slides étalons avant d’en terminer une ?
- Capture : Alex valide Construction d’une règle comme série pilote, puis
  Projets et livrables, Sécurité et Performance. Une série doit être menée
  jusqu’à sa publication avant de passer à la suivante. Q20 précise ensuite que
  cette publication inclut GitHub Pages et les deux dépôts distants.
- Drapeaux : aucun.

### Q5 - Usage prioritaire de Construction d’une règle
- Question : faut-il privilégier l’animation de 60 minutes, la consultation
  autonome, ou un double usage qui conserve l’animation et complète la lecture
  par les accordéons ?
- Capture : Alex valide le double usage. Les images conservent la progression,
  les votes et les corrections différées de l’animation. Les transcriptions et
  discours oraux apportent le contexte nécessaire à une consultation autonome,
  sans anticiper la correction d’une activité. La quantité de slides est
  arbitrée séparément en Q6.
- Drapeaux : aucun.

### Q6 - Nombre de slides du lot Construction d’une règle
- Question : faut-il limiter le parcours aux 16 slides V006, conserver 16
  slides principales avec des annexes conditionnelles, ou autoriser une
  extension du parcours principal ?
- Capture : Alex refuse toute limite de slides. Les 16 slides V006 sont une base
  éditoriale, pas un plafond. Le nombre final doit résulter de la couverture
  complète et claire de la thématique, sans condensation entraînant une
  omission. Les annexes sont autorisées. Le choix entre parcours principal et
  annexe dépend de la continuité de l’animation et du rôle du contenu, jamais
  d’un quota de slides.
- Drapeaux : aucun ; la durée est arbitrée en Q7.

### Q7 - Durée du lot Construction d’une règle
- Question : faut-il conserver une durée stricte de 60 minutes, abandonner la
  limite de durée, ou produire un parcours essentiel de 60 minutes au sein
  d’une série exhaustive ?
- Capture : après avoir envisagé une durée libre, Alex retient le double
  parcours. La série publiée couvre toute la thématique sans plafond. Une liste
  ordonnée de slides forme le parcours essentiel de 60 minutes ; les autres
  slides sont des approfondissements ou annexes facultatives. Aucune information
  n’est supprimée et aucune image n’est dupliquée. Le titre public proposé,
  « Comment se construit une règle Opquast ? », ne mentionne pas de durée.
- Drapeaux : mode de repérage du parcours de 60 minutes à expliciter dans le
  storyboard et les métadonnées, sans ajouter un troisième accordéon.

### Q8 - Consignes d’animation dans les accordéons
- Question : faut-il exclure les consignes d’animation des accordéons, les
  transformer en paroles directement prononçables, ou créer un troisième
  accordéon spécialisé ?
- Capture : Alex choisit de les exclure. Les deux accordéons contiennent
  uniquement le contenu métier. Les consignes de vote, de durée, de régie et de
  gestion du groupe restent dans le conducteur source ; aucun troisième
  accordéon n’est créé.
- Drapeaux : aucun.

### Q9 - Identité publique de Construction d’une règle
- Question : faut-il conserver l’identité exacte du storyboard, raccourcir le
  titre ou présenter la série comme un atelier ?
- Capture : Alex valide le slug `construction-regle-opquast-v5`, le titre
  « Comment se construit une règle Opquast ? » et le footer
  `RÈGLES OPQUAST · CONSTRUIRE UNE RÈGLE`. La pagination est calculée sur le
  nombre final de slides et ne reste pas figée à 16.
- Drapeaux : aucun.

### Q10 - Granularité des 59 livrables
- Question : faut-il produire une slide par livrable, organiser la couverture
  par famille, ou concentrer les 59 entrées dans une grande annexe tabulaire ?
- Capture : Alex choisit une séquence par famille. Les 12 familles structurent
  la progression et peuvent chacune occuper plusieurs slides. Chaque livrable
  est affiché par son nom ; sa fonction, son contexte, son risque utilisateur,
  son examen possible, sa limite et sa provenance restent couverts et traçables.
- Drapeaux : aucun.

### Q11 - Architecture de Projets et livrables
- Question : faut-il conserver les 23 slides V008 puis ajouter l’atlas des 12
  familles, insérer les familles dans le parcours, ou remplacer le parcours par
  l’atlas ?
- Capture : Alex valide les 23 slides V008 comme parcours principal, suivies de
  l’atlas exhaustif des 12 familles. La matrice de couverture doit empêcher les
  répétitions et affecter chaque information à un emplacement principal.
- Drapeaux : aucun.

### Q12 - Durée et double parcours de Projets et livrables
- Question : faut-il conserver les 23 slides comme parcours de 60 minutes,
  supprimer la contrainte de durée, ou intégrer l’atlas dans un nouveau
  minutage global ?
- Capture : Alex valide le double parcours. Les 23 slides V008 constituent le
  parcours essentiel de 60 minutes. L’atlas exhaustif des 12 familles reste
  disponible dans la même série comme approfondissement facultatif hors
  minutage. Aucune image n’est dupliquée entre les parcours.
- Drapeaux : aucun.

### Q13 - Identité publique de Projets et livrables
- Question : faut-il employer une identité descriptive, reprendre le titre du
  storyboard ou utiliser le slogan comme titre public ?
- Capture : Alex valide le slug `projets-livrables-opquast-v5`, le titre
  « Projets et livrables selon Opquast V5 » et le footer
  `RÈGLES OPQUAST · PROJETS ET LIVRABLES`. Le slogan « La qualité circule, la
  preuve se construit » est réservé à l’ouverture et à la synthèse.
- Drapeaux : aucun.

### Q14 - Double parcours de Sécurité
- Question : faut-il produire un parcours essentiel de 60 minutes dans une
  série exhaustive, un parcours continu sans durée, ou condenser toute la
  recherche en une heure ?
- Capture : Alex valide le double parcours. La série publiée reste exhaustive
  et sans plafond. Une sélection ordonnée de slides constitue le parcours
  essentiel de 60 minutes ; les autres slides restent accessibles comme
  approfondissements ou annexes facultatives. Aucune image n’est dupliquée.
- Drapeaux : aucun.

### Q15 - Identité publique de Sécurité
- Question : faut-il employer une identité descriptive et réserver la phrase
  centrale à l’ouverture et à la synthèse ?
- Capture : Alex valide le slug `securite-opquast-v5`, le titre « Sécurité
  selon Opquast V5 » et le footer `RÈGLES OPQUAST · SÉCURITÉ`. La phrase « La
  sécurité Opquast, c’est d’abord prévenir des risques concrets pour
  l’utilisateur » est réservée à l’ouverture et à la synthèse.
- Drapeaux : aucun.

### Q16 - Double parcours de Performance
- Question : faut-il produire un parcours essentiel de 60 minutes dans une
  série exhaustive, un parcours continu sans durée, ou condenser toute la
  recherche en une heure ?
- Capture : Alex valide le double parcours. La série publiée reste exhaustive
  et sans plafond. Une sélection ordonnée de slides constitue le parcours
  essentiel de 60 minutes ; les autres slides restent accessibles comme
  approfondissements ou annexes facultatives. Aucune image n’est dupliquée.
- Drapeaux : aucun.

### Q17 - Identité publique de Performance
- Question : faut-il employer une identité descriptive et réserver les deux
  phrases centrales à l’ouverture et à la synthèse ?
- Capture : Alex valide le slug `performance-opquast-v5`, le titre
  « Performance selon Opquast V5 » et le footer
  `RÈGLES OPQUAST · PERFORMANCE`. Les phrases « Performance Opquast = ne pas
  faire attendre, télécharger ou calculer inutilement l’utilisateur » et
  « Rapide n’est pas forcément léger, affiché n’est pas forcément utilisable »
  sont réservées à l’ouverture et à la synthèse.
- Drapeaux : aucun.

### Q18 - Gate humain des slides étalons
- Question : faut-il valider quatre étalons par série, quatre étalons seulement
  pour la série pilote, ou regrouper seize étalons avant toute production ?
- Capture : Alex valide un gate distinct pour chaque série. Il porte sur une
  ouverture, une règle ou notion centrale, un regroupement ou éclairage et une
  synthèse. La production du reste de la série est interdite tant que le
  storyboard, les textes visibles, le prompt, le visuel, la transcription et le
  discours oral de ces quatre étalons n’ont pas reçu sa validation explicite.
- Drapeaux : aucun.

### Q19 - Clôture de la cuisine
- Question : la compréhension partagée est-elle atteinte et toutes les
  décisions peuvent-elles être intégrées dans le Goal ?
- Capture : Alex confirme la compréhension partagée, clôt la cuisine et
  autorise l’intégration de toutes les décisions dans
  `goal-quatre-series-opquast-visuelles.md`.
- Drapeaux : aucun.

### Q20 - Définition de terminé et publication distante
- Question : faut-il commiter et pousser seulement `slides-miweb`, ou également
  le workspace Opquast qui contient le Goal et les artefacts de la fabrique ?
- Capture : Alex exige les deux dépôts. La mission n’est terminée qu’après des
  commits limités aux fichiers de la mission, leur présence sur `main` local et
  `origin/main` dans le workspace Opquast et dans `slides-miweb`, la publication
  GitHub Pages et la vérification des pages publiques. Les modifications
  étrangères restent exclues.
- Drapeaux : aucun.

### Q21 - Destinations publiques
- Question : quel dépôt et quel site public doivent constituer les destinations
  vérifiables de `slides-miweb` ?
- Capture : Alex désigne le dépôt
  `https://github.com/alexandra-guiderdoni/slides-miweb` et le site
  `https://alexandra-guiderdoni.github.io/slides-miweb/`. Les quatre séries
  doivent être visibles depuis la page d’accueil publique.
- Drapeaux : aucun.

### Q22 - Provenance exclusive et références de contrôle
- Question : le contenu peut-il être complété depuis les guides, le MCP, le
  skill Opquast ou la connaissance du modèle lorsqu’un Markdown est incomplet ?
- Capture : Alex impose que rien ne soit inventé et que tout contenu métier
  publié provienne des six Markdown nommés. Les guides applicables, le MCP
  Opquast et le skill `opquast-skill` font autorité pour contrôler, confirmer ou
  rejeter les affirmations trouvées dans ces Markdown ; ils peuvent être
  interrogés en cas de doute, mais ne peuvent pas enrichir silencieusement le
  contenu publié. Une absence de source, un doute non levé ou une contradiction
  impose `STOP_SERIE` jusqu’à correction du Markdown ou arbitrage explicite.
- Drapeaux : aucun.

## Drapeaux ouverts

- Vérifier le ratio et les dimensions natives de la première candidate
  `image_gen` ; appliquer la règle d’arrêt validée si le ratio n’est pas 16:9 ->
  exécution du Goal.
- Faire valider les quatre slides étalons de chaque série avant de produire le
  reste de cette série -> Alex pendant l’exécution du Goal.
- Les scripts de la fabrique, les contrôles de `slides-miweb`, la génération,
  les commits, les push et les publications locale et GitHub Pages restent non
  exécutés à ce stade -> exécution du Goal.
