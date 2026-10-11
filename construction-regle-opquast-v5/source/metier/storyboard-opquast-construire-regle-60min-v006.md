# Storyboard Opquast — Comment se construit une règle ?

**Version :** v006 — proposition refondue le 11 octobre 2026  
**Statut :** `PRET_REVUE_METIER` (contenu préparé, non assimilé à une validation indépendante)  
**Durée :** **60 minutes exactement**, interactions comprises  
**Public :** collègues des métiers numériques préparant la certification Opquast  
**Niveau :** intermédiaire, vocabulaire explicité  
**Livrable compagnon :** `deroule-animation-construire-regle-60min-v006.md`  
**Production :** 16 slides principales, **une scène illustrée par slide**, aucune slide-annexe nécessaire à l'animation ; supports textuels et sources ci-dessous.  
**Intention :** expliquer comment une difficulté réelle peut devenir une proposition, puis — après examen et discussion — une règle Opquast documentée. Ce déroulé reconstruit *pédagogiquement* un processus : il ne prétend pas reproduire les étapes internes exactes de chaque règle publiée.

> **Idée centrale à transmettre :** une bonne idée ne suffit pas à faire une règle Opquast. Il faut un bénéfice utilisateur clair, une exigence suffisamment unitaire et contrôlable, une portée et une mise en œuvre défendables, une rédaction durable, une discussion collective et une documentation exploitable.
>
> **Contre-idée à retenir :** une proposition qui n'entre pas dans la checklist peut rester utile ; elle peut devenir une recommandation ou enrichir la fiche d'une règle existante.

## 1. Cadrage hérité et application du méta-prompt V4

Le cadrage repris des fichiers fournis est confirmé sans nouvel entretien : utilisateur d'abord ; organisation ensuite ; préparation à la certification et compréhension du fond ; enseignement fondé sur des sources Opquast ; ne pas inventer de questions officielles ; notions et règles précises sourcées ; format d'une heure. Le projet existant privilégiait un **atelier de fabrication** plutôt qu'une succession de règles. Cette exception au schéma « grappes de règles par besoin utilisateur » est maintenue : la thématique porte sur **la méthode de construction des règles**, et non sur une rubrique des 245 règles.

### Transposition contrôlée des axes du méta-prompt

- **Noyau explicite (A1 adapté au sujet) :** critères de recevabilité, formulation unitaire, documentation, discussions et arbitrages, stabilité. Ce sont ici des *principes de méthode*, pas des règles numérotées classées officiellement A1.
- **Noyau fonctionnel (A2 adapté) :** difficulté utilisateur, résultat vérifiable, preuve, applicabilité, accord collectif, devenir d'une proposition.
- **Exemples illustratifs (B) :** règles V5 n° 72, 87, 140, 152, 155, 156, 159, 168, 223, 224 et 233 ; leur rôle est de **montrer** la méthode, non d'établir qu'elles constituent « la rubrique fabrication des règles ».
- **Périphérie (D) :** VPTCS, RGAA, WCAG, processus internes de management, standards de qualité, certification. Ils sont mentionnés seulement pour situer les frontières et ne deviennent pas un second cours.
- **Chaîne pédagogique :** besoin → préjudice → proposition → découpage/unicité → examen des exigences → débat/arbitrage → documentation → publication et maintenance. L'ordre de cette chaîne est **une synthèse pédagogique** ; ce n'est pas un organigramme officiel d'Opquast.

### Distinction documentaire capitale : six exigences V5, et non « sept filtres officiels » universels

La **page publique des ateliers V5 (2025–2030)** énonce **six exigences** dans son *sanity check* : **universalité, utilité, absence de valeur numérique empirique arbitraire, vérifiabilité, réalisme et unicité**. Elle traite à part des lignes directrices de rédaction, du consensus et des décisions en cas de conflit. [Ateliers V5, texte officiel](https://checklists.opquast.com/workshops/assurance-qualite-web/).

L'[article de lancement des ateliers V4, en 2019](https://www.opquast.com/opquast-version-4-lancement-des-ateliers/) présentait une **liste différente de sept points**, dont le consensus et l'absence de méta-règle. Le storyboard fourni en v005 reprenait **sept filtres**, incluant « sans solution technique » mais non « unicité » au même rang : cette liste est documentée dans le **dossier de travail**, mais elle ne doit pas être annoncée comme étant *la* liste textuelle de l'atelier V5. Les différences de source, de millésime et de formulation sont dites explicitement.

**Choix pédagogique v006 :** enseigner les **six exigences formulées par l'atelier V5** comme point d'ancrage ; traiter **l'absence de prescription technique inutile**, **la durabilité de l'écriture**, **le consensus** et **la documentation** à leurs étapes propres. L'unicité a une slide dédiée *et* figure dans les six exigences : cette répétition est intentionnelle.

### Précision sur UTF-8

La [règle 233](https://checklists.opquast.com/fr/qualite-numerique/233) cite expressément UTF-8. Elle montre qu'un libellé peut, dans des cas précis, désigner une technologie. **Le « 8 » de « UTF-8 » n'est pas une valeur numérique empirique ou un seuil arbitraire** : ce n'est donc pas, en soi, une violation du critère « non numériques » des ateliers V5. Ne pas présenter cette règle comme la preuve que tous les seuils sont permis, ni inventer la justification exacte de l'arbitrage historique.

### Paramètres visuels hérités de la série fournie

Les spécifications de présentation non liées au fond sont reprises de la version v005, avec la pagination adaptée :

- **En-tête gauche exact :** `QUALITÉ WEB` / `EXPÉRIENCES DURABLES`.
- **En-tête droit exact :** `Opquast` / `DES SITES MEILLEURS POUR TOUS`.
- **Pied de page principal exact :** `RÈGLES OPQUAST · CONSTRUIRE UNE RÈGLE`.
- **Pagination :** `01 / 16` à `16 / 16` (en bas à droite).
- **Badges de règle :** seulement quand une règle V5 numérotée est précisément citée, position stable dans la zone de contenu.
- **Images :** une image principale par slide ; aucun montage de plusieurs images autonomes. Accompagner chaque scène de sa description textuelle dans l'alternative accessible.
- **Slogan :** aucun ; une phrase de synthèse uniquement en ouverture et en conclusion.
- **Guide de style :** le fichier original référençait `../fabrique-slides/docs/05-GUIDE-STYLE.md` v2.0.0, **non fourni ici** : la conformité graphique effective devra être validée à la production, sans prétendre l'avoir vérifiée.

## 2. Objectifs mesurables de l'heure

À la fin, le participant doit pouvoir :

1. partir d'un **préjudice utilisateur** plutôt que d'une préférence personnelle ;
2. distinguer attente vague, proposition, règle retenue, recommandation et documentation ;
3. décomposer un problème en exigences qui peuvent être évaluées séparément ;
4. expliquer **les six exigences** affichées par l'atelier V5, sans les confondre avec le consensus et les conseils de rédaction ;
5. dire pourquoi un **résultat observable** peut être une règle alors qu'un **processus interne non vérifiable depuis le service** n'en est pas nécessairement une ;
6. montrer comment se négocient des formulations et pourquoi une proposition peut être rejetée, adaptée, fusionnée ou conservée en recommandation ;
7. distinguer **libellé / objectif / solution technique / moyen de contrôle**, sur une fiche V5 authentique ;
8. réaliser un premier diagnostic argumenté sur une nouvelle proposition et accepter le verdict « à retravailler ».

**Critère de réussite de l'atelier :** chaque groupe sait expliciter un bénéfice, une condition d'application et **une preuve de contrôle**, même lorsque sa proposition n'est pas finalement jugée recevable.

## 3. Fil rouge — un échec utilisateur qui traverse la séance

> **Situation :** « Je clique sur un lien du service vers une démarche qui m'intéresse, mais j'arrive sur une erreur. Je dois recommencer ma recherche. »

- **Besoin :** accéder sans interruption au contenu attendu.
- **Préjudice :** perte de temps, confusion, possible renoncement à la démarche.
- **Idée spontanée A :** « Les liens sont vérifiés toutes les semaines. »
- **Idée spontanée B :** « Le site ne contient aucun lien mort. » (exemple historique, **pas** le libellé V5 actuel).
- **Formulation V5 existante à découvrir :** [règle 152 — « Tous les liens internes sont valides. »](https://checklists.opquast.com/fr/qualite-numerique/152).
- **Ce que l'on apprend :** une intention de prévention doit être **reformulée en état contrôlable**, avec un champ précis. La proposition A reste potentiellement une bonne méthode de maintenance, mais n'atteste pas directement de la validité des liens à l'instant du contrôle.

**Important :** nous **reconstruisons** le raisonnement sur la règle 152 : nous ne prétendons pas que la règle a été historiquement élaborée à partir de ces phrases, ni que tous les liens, externes et internes, font l'objet de la même obligation.

## 4. Plan général — 60 minutes, 16 slides

| Slide | Horloge | Durée | Étape et question centrale | Interaction |
|---|---|---:|---|---|
| 01 | 00–03 | 3 min | Une bonne idée fait-elle une règle ? | Vote intuitif |
| 02 | 03–07 | 4 min | Où est le préjudice utilisateur ? | Reformulation orale |
| 03 | 07–10 | 3 min | Pourquoi décomposer l'attente ? | Choix des besoins |
| 04 | 10–14 | 4 min | Règle, conseil, recommandation : même chose ? | Classement rapide |
| 05 | 14–18 | 4 min | Pourquoi une règle doit-elle être unitaire ? | Vote 403/404 |
| 06 | 18–24 | 6 min | Six exigences publiées pour l'atelier V5 | Micro-diagnostic |
| 07 | 24–28 | 4 min | Peut-on vérifier A ou B ? | Vote A/B sans correction |
| 08 | 28–31 | 3 min | Que vérifie exactement la règle 152 ? | Correction argumentée |
| 09 | 31–34 | 3 min | Universelle signifie-t-elle applicable partout ? | Contre-exemple |
| 10 | 34–38 | 4 min | Comment écrire un libellé durable ? | Cas UTF-8 |
| 11 | 38–42 | 4 min | Qui fabrique, discute et arbitre ? | Question au groupe |
| 12 | 42–46 | 4 min | Que devient une proposition non retenue ? | Cas réel 2025 |
| 13 | 46–50 | 4 min | Quelle documentation rend la règle exploitable ? | Trois cases à compléter |
| 14 | 50–56 | 6 min | Mini-atelier : construire et challenger une proposition | Travail court en binômes |
| 15 | 56–58 | 2 min | Faut-il accepter, retravailler ou recommander ? | Verdict motivé |
| 16 | 58–60 | 2 min | Synthèse et transfert professionnel | Question de sortie |
| **Total** | **00–60** | **60 min** | **Une seule séquence continue** | |

## 5. Storyboard détaillé — contrat de production slide par slide

### Slide 01 — Une idée utile est-elle déjà une règle ?

- **Horaire :** 00–03 (3 min). **Fonction :** accroche et annonce du problème.
- **Question :** « Qui serait pour ajouter la règle : *Le site doit être intuitif* ? »
- **Décision d'apprentissage :** l'accord sur une valeur ne produit pas une exigence évaluée de façon reproductible.
- **Écran, texte exact :** `Une idée utile suffit-elle ?` / `« Ce site doit être intuitif. »` / `Intention ≠ règle contrôlable`.
- **Scène unique :** table de discussion ; trois professionnels sont d'accord sur « intuitif » mais présentent trois constats contradictoires. Un espace de formulaire « verdict » reste impossible à remplir.
- **Description textuelle de la scène :** une même attente vague produit trois lectures différentes ; aucune décision commune n'est possible.
- **Oral :** vote immédiat, sans correction prématurée ; annoncer qu'on va reconstruire la règle depuis ce que subit l'utilisateur.
- **Source/autorité :** synthèse pédagogique du chapitre « Donner forme aux attentes » **cité dans le storyboard fourni**, non revérifié intégralement ici ; principe de vérifiabilité confirmé par [l'atelier V5](https://checklists.opquast.com/workshops/assurance-qualite-web/).
- **Mémo :** « Accord sur l'idée ≠ accord sur la preuve. »

### Slide 02 — Ce que l'utilisateur subit avant la règle

- **Horaire :** 03–07 (4 min). **Fonction :** ancrage utilisateur et fil rouge.
- **Question :** « Que perd la personne qui arrive sur une page d'erreur après avoir cliqué ? »
- **Décision :** identifier une difficulté vécue avant de choisir une formulation ou une technologie.
- **Écran :** `Je clique. Je n'arrive pas.` / `Besoin : accéder au contenu` / `Préjudice : temps perdu, parcours interrompu`.
- **Scène unique :** trajet d'une personne de « démarche recherchée » à « lien interne » puis « page introuvable » ; l'action attendue est interrompue.
- **Description :** un lien qui échoue interrompt l'accès au contenu ; le risque n'est pas « un test qui échoue » mais un parcours dégradé pour la personne.
- **Oral :** retenir les mots du groupe : temps, confusion, perte de confiance, abandon éventuel (ne pas prétendre que l'abandon est systématique).
- **Source :** [règle 152 et ses objectifs officiels](https://checklists.opquast.com/fr/qualite-numerique/152).
- **Mémo :** « D'abord le dommage vécu ; ensuite le contrôle. »

### Slide 03 — D'une attente large à plusieurs règles possibles

- **Horaire :** 07–10 (3 min). **Fonction :** décomposition sans récitation des numéros.
- **Question :** « Une seule règle peut-elle rendre la navigation “intuitive” ? »
- **Décision :** un besoin large appelle plusieurs exigences autonomes ; les cinq exemples n'épuisent pas la navigation.
- **Écran :** `« Navigation intuitive »` → `140 · Identifier les liens` / `155 · Revenir à l'accueil` / `156 · Savoir où l'on est` / `159 · Comprendre les icônes` / `168 · Trouver par recherche` / `Labels pédagogiques, pas libellés officiels`.
- **Scène unique :** un besoin central ramifié en cinq expériences distinctes ; chaque branche peut être évaluée séparément.
- **Description :** cinq situations utilisateur différentes sont reliées à cinq règles existantes, sans annoncer une exhaustivité.
- **Oral :** demander quelle expérience serait dégradée si une branche manquait ; ne pas lire les cinq fiches en entier.
- **Sources officielles :** [140](https://checklists.opquast.com/fr/qualite-numerique/140), [155](https://checklists.opquast.com/fr/qualite-numerique/155), [156](https://checklists.opquast.com/fr/qualite-numerique/156), [159](https://checklists.opquast.com/fr/qualite-numerique/159), [168](https://checklists.opquast.com/fr/qualite-numerique/168).
- **Mémo :** « Une intention, plusieurs preuves. »

### Slide 04 — Proposition, règle et recommandation : ne pas confondre

- **Horaire :** 10–14 (4 min). **Fonction :** contrat du référentiel.
- **Question :** « “Contrôlez vos liens chaque lundi” : bonne idée ? Règle Opquast ? »
- **Décision :** utile ne signifie pas automatiquement sélectionné.
- **Écran :** `Proposition` → `Examen` → `Règle retenue / Recommandation / Non retenue / Évolution d'une fiche existante`.
- **Scène unique :** une proposition entre dans une table de tri documentée ; les sorties ne sont pas notées « bien/mal ».
- **Description :** une idée peut être sélectionnée, recommandée, refusée ou contribuer à une règle existante après discussion.
- **Oral :** expliquer « recommandation » sans la disqualifier ; rappeler la [revue d'avril 2025](https://www.opquast.com/check-list-opquast-version-5-point-detape-11-avril-2025/) : recommandation pour non-vérifiabilité, refus pour doublon, adaptation de fiches ou reformulation.
- **Source :** [compte rendu Opquast du 11 avril 2025](https://www.opquast.com/check-list-opquast-version-5-point-detape-11-avril-2025/) et [article 2021 sur le mot « règle »](https://www.opquast.com/la-fin-des-bonnes-pratiques-opquast/).
- **Mémo :** « Une bonne recommandation n'est pas forcément une règle. »

### Slide 05 — Une règle, une décision : le test 403/404

- **Horaire :** 14–18 (4 min). **Fonction :** rendre sensible l'unicité.
- **Question :** « La page 404 est personnalisée et la 403 ne l'est pas : le critère combiné est-il respecté ? »
- **Décision :** si deux exigences sont indépendantes, on doit pouvoir les apprécier séparément ; l'unicité est un principe explicitement mentionné dans l'atelier V5.
- **Écran :** `403 + 404 ?` / `Deux situations, deux décisions` / `223 · Erreur 404 personnalisée` / `224 · Interdiction 403 personnalisée`.
- **Scène unique :** une carte contenant 403 et 404 est divisée en deux fiches séparées, chacune avec sa propre case de contrôle.
- **Description :** un résultat partiel ne doit pas créer une appréciation artificiellement indécidable lorsque les situations sont distinctes.
- **Oral :** faire voter avant d'afficher les deux numéros ; préciser qu'une réponse 404 et une réponse 403 ne sont pas équivalentes.
- **Sources :** [article Opquast 2005](https://www.opquast.com/2005071239-les-dix-regles-du-contributeur-connaitre-il-te-faut/), règles [223](https://checklists.opquast.com/fr/qualite-numerique/223) et [224](https://checklists.opquast.com/fr/qualite-numerique/224).
- **Mémo :** « Deux risques indépendants, deux décisions. »

### Slide 06 — Le banc d'épreuve de l'atelier V5 : six exigences

- **Horaire :** 18–24 (6 min). **Fonction :** moment doctrinal central.
- **Question :** « Parmi ces six questions, laquelle ferait tomber une proposition dont vous aimez pourtant l'idée ? »
- **Décision :** une proposition doit satisfaire un ensemble cohérent d'exigences ; ce n'est pas une compétition de préférences.
- **Écran :** `Six exigences — atelier V5` puis : `Universelle ?` / `Utile ?` / `Sans seuil empirique arbitraire ?` / `Vérifiable depuis le service ?` / `Réaliste ?` / `Unique ?` ; note `Le consensus et les conseils de rédaction seront étudiés à part.`
- **Scène unique :** six cartes interrogatives reliées autour d'une proposition ; aucune carte n'est marquée « critère prioritaire ».
- **Description :** les six exigences proviennent de la page des ateliers V5 ; la répartition graphique est pédagogique et non une hiérarchie officielle.
- **Oral :** donner une phrase concrète par exigence ; insister sur l'**absence de valeur numérique empirique arbitraire**, pas l'interdiction de tout chiffre. Dire explicitement que les listes historiques et le guide cité par les fichiers peuvent formuler autrement certains principes.
- **Source première :** [Atelier V5 — Exigences (Sanity check)](https://checklists.opquast.com/workshops/assurance-qualite-web/).
- **Mémo :** « Utile, contrôlable, réaliste, universelle, unitaire, sans seuil arbitraire. »

### Slide 07 — Vote : que peut vérifier un auditeur en ligne ?

- **Horaire :** 24–28 (4 min). **Fonction :** interaction centrale, sans correction visible.
- **Question :** `A ou B : laquelle exprime un résultat vérifiable depuis le service ?`
- **Décision :** apprendre à identifier ce qui est observable à un instant donné.
- **Écran :** `A · Le site est exempt de liens morts.` / `B · Les liens sont vérifiés chaque semaine.` / `VOTE A / B` / `Justifiez par une preuve`.
- **Scène unique :** deux cartes de même statut graphique ; aucun symbole ni couleur ne révèle la solution.
- **Description :** deux formulations historiquement opposées par Opquast : un état accessible au contrôle et une procédure de maintenance interne.
- **Oral :** 20 secondes de réflexion, vote, deux arguments ; **ne pas montrer la correction avant la slide 08**.
- **Source :** [article de 2005, exemple historique](https://www.opquast.com/2005071239-les-dix-regles-du-contributeur-connaitre-il-te-faut/).
- **Mémo :** laissé volontairement vide jusqu'à la correction.

### Slide 08 — La preuve, pas la promesse : comprendre la règle 152

- **Horaire :** 28–31 (3 min). **Fonction :** correction et précision du périmètre.
- **Question :** « Quelle observation démontre le respect de la règle actuelle ? »
- **Décision :** A décrit un état contrôlable ; B, un processus interne. La règle actuelle est plus précisément **restreinte aux liens internes**.
- **Écran :** `A · Résultat observable` / `B · Processus interne` / `152 · Tous les liens internes sont valides.` / `Contrôle : rechercher les liens internes vers une erreur 404`.
- **Scène unique :** une loupe examine le parcours réel d'un lien interne ; à l'écart, un agenda de vérification représente le processus non observable.
- **Description :** l'auditeur examine les liens internes et non la fréquence des campagnes de maintenance ; l'exemple A est historique, la formulation n° 152 est actuelle.
- **Oral :** éviter « tous les liens externes » et « 100 % de sûreté garantie ». Un contrôle régulier peut être **un moyen** recommandé par la fiche, mais n'est pas le résultat à constater.
- **Sources :** [règle 152, objectif/solution/contrôle](https://checklists.opquast.com/fr/qualite-numerique/152) ; [article 2005](https://www.opquast.com/2005071239-les-dix-regles-du-contributeur-connaitre-il-te-faut/).
- **Mémo :** « Le contrôle constate un état, pas la promesse d'un rituel. »

### Slide 09 — Internationale ne signifie pas applicable à chaque cas

- **Horaire :** 31–34 (3 min). **Fonction :** distinguer deux concepts proches.
- **Question :** « Une règle sur les champs d'un formulaire est-elle invalide pour un site qui n'a pas de formulaire ? »
- **Décision :** universalité de la portée ≠ applicabilité à toutes les pages et tous les services.
- **Écran :** `Universalité = pas de dépendance à une loi locale` / `Applicabilité = contexte effectivement rencontré` / `Non applicable ≠ non conforme`.
- **Scène unique :** deux sites du monde réel, l'un avec un formulaire, l'autre sans ; une règle peut avoir une portée internationale même si elle ne s'applique qu'au premier.
- **Description :** la portée territoriale est séparée du contexte de contrôle ; la règle ne doit pas être jugée non respectée si son objet n'existe pas.
- **Oral :** distinguer sans multiplier les exceptions. L'inapplicabilité dépend du protocole d'audit et de la règle concernée ; ne pas dire qu'un élément « absent » rend automatiquement toute règle inapplicable.
- **Source :** [Atelier V5, universalité](https://checklists.opquast.com/workshops/assurance-qualite-web/) et passage du livre cité dans le storyboard v005 (lecture indirecte, non indépendante).
- **Mémo :** « Universelle dans sa portée, contextuelle dans son contrôle. »

### Slide 10 — Une formulation qui dure : la nuance UTF-8

- **Horaire :** 34–38 (4 min). **Fonction :** vigilance rédactionnelle et faux amis.
- **Question :** « Si une règle écrit UTF-8, contredit-elle le critère “non numériques” ? »
- **Décision :** éviter les seuils empiriques arbitraires, les prescriptions périssables inutiles et les méta-règles, sans inventer une interdiction mécanique de toute référence précise.
- **Écran :** `À éviter : seuil arbitraire ; recette fragile ; norme entière en guise de règle` / `Règle 233 : « Le codage de caractères utilisé est UTF-8. »` / `UTF-8 : nom de codage, pas seuil de performance`.
- **Scène unique :** à gauche, un seuil inventé « chargement en 2,7 secondes » au statut « à justifier » ; à droite, une règle réelle désignant un codage, accompagnée de sa documentation.
- **Description :** on distingue valeur arbitraire mesurable et identifiant d'une technologie ; la rédaction se juge par sa portée et son contexte, pas à la seule présence d'un chiffre.
- **Oral :** expliquer que l'atelier V5 autorise une valeur numérique empirique si adossée à un standard international reconnu ; ne pas affirmer que c'est la justification historique officielle de la règle 233.
- **Sources :** [Atelier V5](https://checklists.opquast.com/workshops/assurance-qualite-web/), [règle 233](https://checklists.opquast.com/fr/qualite-numerique/233), [article 2019](https://www.opquast.com/opquast-version-4-lancement-des-ateliers/).
- **Mémo :** « Durabilité n'est pas interdiction des noms propres ou des chiffres. »

### Slide 11 — On ne fabrique pas un commun tout seul

- **Horaire :** 38–42 (4 min). **Fonction :** la couche collective qui manquait.
- **Question :** « Si deux métiers défendent des réponses opposées, qu'est-ce qui empêche une règle d'imposer une préférence ? »
- **Décision :** participation, contradiction, rédaction et arbitrage permettent de rechercher un socle partagé ; **le consensus est un principe de sélection collective**, pas une septième ligne ajoutée à la liste de six exigences V5.
- **Écran :** `Proposer → Discuter → Reformuler → Arbitrer` / `Consensus recherché, pas unanimité garantie` / `Décision et justification`.
- **Scène unique :** atelier de discussion où une proposition circule entre plusieurs métiers ; des arguments sont consignés ; un arbitrage final est documenté.
- **Description :** le référentiel est élaboré collectivement ; les ateliers V5 précisent qu'en cas de conflit persistant Opquast prend une décision argumentée.
- **Oral :** donner quatre repères temporels très brefs : **2005** vigilance sur la vérifiabilité/unicité, **2019** ateliers et consensus explicite, **2021** préférence pour le mot *règle*, **2025** travaux V5 puis publication. Ne pas attribuer un nombre identique de critères à tous les millésimes.
- **Sources :** [2005](https://www.opquast.com/2005071239-les-dix-regles-du-contributeur-connaitre-il-te-faut/), [2019](https://www.opquast.com/opquast-version-4-lancement-des-ateliers/), [2021](https://www.opquast.com/la-fin-des-bonnes-pratiques-opquast/), [ateliers V5](https://checklists.opquast.com/workshops/assurance-qualite-web/).
- **Mémo :** « La robustesse se discute ; la sélection s'argumente. »

### Slide 12 — Cas réel 2025 : parfois, la meilleure règle est déjà là

- **Horaire :** 42–46 (4 min). **Fonction :** prouver par une trace d'arbitrage authentique.
- **Question :** « Faut-il créer une nouvelle règle pour indiquer les contraintes d'un mot de passe ? »
- **Décision :** un besoin peut être couvert par l'objectif, la solution ou le contrôle **d'une règle existante**. Une proposition peut passer en recommandations sans être déclarée inutile.
- **Écran :** `Proposition 2025 : contraintes de mot de passe indiquées` / `Question : nouveau doublon ou enrichissement ?` / `Issue documentée : recommandation ; rapprochement avec la règle 72`.
- **Scène unique :** une proposition soumise à discussion est rapprochée d'une fiche déjà publiée ; la proposition n'ajoute pas automatiquement une nouvelle ligne au référentiel.
- **Description :** les commentaires datés d'avril 2025 discutent la reformulation et le rattachement possible à la règle existante 72 ; une intervention Opquast annonce le basculement en recommandations.
- **Oral :** bien distinguer *discussion observée*, *suggestion d'enrichissement* et *texte actuel de la règle 72*. La règle 72 explique désormais explicitement, dans son texte de présentation, les difficultés de format des mots de passe ; il n'est pas démontré ici que cette phrase résulte exclusivement de cette discussion. Option de relance : autre proposition « images générées par IA signalées », débattue comme non vérifiable en ligne à l'époque, sans en faire un jugement éternel sur la technologie.
- **Sources :** [fil d'atelier « règles de création de mot de passe »](https://checklists.opquast.com/workshops/assurance-qualite-web/criterion/54578/), [règle 72 actuelle](https://checklists.opquast.com/fr/qualite-numerique/72), [point d'étape d'avril 2025](https://www.opquast.com/check-list-opquast-version-5-point-detape-11-avril-2025/).
- **Mémo :** « Une nouvelle idée n'exige pas toujours une nouvelle règle. »

### Slide 13 — Une règle est aussi une fiche de preuves

- **Horaire :** 46–50 (4 min). **Fonction :** passer de la sélection à l'usage.
- **Question :** « Avec le seul libellé 152, savez-vous déjà pourquoi, comment et quoi contrôler ? »
- **Décision :** ne pas confondre l'exigence avec ses objectifs, ses solutions et son protocole de vérification.
- **Écran :** `Libellé : Tous les liens internes sont valides.` / `Objectif : éviter les impasses de navigation` / `Solution : prévenir ou corriger les liens internes invalides` / `Contrôle : vérifier l'absence de liens internes aboutissant à une 404` / `Objectif, solution, contrôle : résumés pédagogiques`.
- **Scène unique :** une fiche n° 152 au centre ; trois volets distincts « Pourquoi ? », « Comment ? », « Quelle preuve ? » ; une case de contrôle est matérialisée.
- **Description :** le libellé fixe ce qui doit être vrai ; la fiche expose les bénéfices, des modalités de réalisation et les vérifications à mener.
- **Oral :** demander au groupe de remplir les trois volets avant de révéler les exemples ; lire si utile un objectif officiel sur la page source.
- **Source :** [fiche officielle n° 152](https://checklists.opquast.com/fr/qualite-numerique/152). Les résumés de la slide **ne sont pas** des citations littérales.
- **Mémo :** « Libellé ≠ objectif ≠ solution ≠ contrôle. »

### Slide 14 — Mini-atelier : mettez une idée à l'épreuve

- **Horaire :** 50–56 (6 min). **Fonction :** appropriation et transfert.
- **Question :** « Votre règle résiste-t-elle à une vraie question de contrôle ? »
- **Décision :** savoir soumettre une proposition à la critique sans prétendre l'avoir validée comme règle Opquast.
- **Écran :** `CAS : « Je commence une longue démarche et j'ignore les étapes restantes. »` / `1 · Préjudice` / `2 · Proposition unitaire` / `3 · Contrôle depuis le service` / `4 · Premier verdict` / `Exercice pédagogique, non officiel`.
- **Scène unique :** atelier avec trois cartes vierges et un chronomètre ; la carte « preuve de contrôle » est visuellement indispensable au dépôt de la proposition.
- **Description :** les binômes fabriquent une proposition puis l'examinent ; la scène n'affiche **aucune correction**.
- **Oral :** deux minutes de rédaction, deux minutes de contre-examen croisé, une minute de restitution et une minute de transition. Donner le cas d'une démarche en plusieurs étapes dont la durée est opaque. Ne pas autoriser un verdict « règle Opquast validée ».
- **Source de rapprochement pour le débrief :** [règle 87](https://checklists.opquast.com/fr/qualite-numerique/87), non dévoilée avant la correction de la slide 15.
- **Mémo :** « Une proposition doit survivre à la question : comment contrôler ? »

### Slide 15 — Le bon verdict est parfois : retravailler

- **Horaire :** 56–58 (2 min). **Fonction :** rendre la correction formative.
- **Question :** « Votre proposition apporte-t-elle une nouvelle règle, ou précise-t-elle quelque chose de déjà couvert ? »
- **Décision :** choisir un **verdict motivé** (recevabilité à approfondir ; recommandation ; rapprochement avec règle existante) plutôt qu'un oui/non arbitraire.
- **Écran :** `Verdicts possibles : retravailler · recommander · rapprocher d'une règle existante` / `Règle 87 · Les processus complexes sont accompagnés de la liste de leurs étapes.` / `Ne jamais prétendre valider une règle officielle en classe.`
- **Scène unique :** trois sorties non hiérarchisées autour d'une fiche de proposition ; un renvoi explicite vers la règle 87 existante.
- **Description :** la proposition de l'exercice concerne le besoin de connaître les étapes d'une longue démarche, déjà abordé par une règle V5 ; les participant·es cherchent une preuve de contrôle sans inventer une nouvelle règle officielle.
- **Oral :** annoncer un exemple de correction ; reconnaître plusieurs formulations pédagogiques recevables à débattre.
- **Source :** [règle 87](https://checklists.opquast.com/fr/qualite-numerique/87). Le cas d'atelier 2025 [relatif à la règle 72](https://checklists.opquast.com/workshops/assurance-qualite-web/criterion/54578/) reste un exemple séparé de la slide 12.
- **Mémo :** « Justifier la décision compte autant que proposer. »

### Slide 16 — Construire une règle, c'est construire une preuve partagée

- **Horaire :** 58–60 (2 min). **Fonction :** mémorisation et transfert.
- **Question :** « Si vous ne gardiez que trois questions pour challenger une règle demain ? »
- **Décision :** restituer sans sigle inventé et sans prétendre avoir participé à une véritable validation Opquast.
- **Écran :** `1 · Quel préjudice utilisateur ?` / `2 · Quelle exigence, quelle preuve ?` / `3 · Qui peut la discuter, la documenter et la maintenir ?` / `Une règle utile, contrôlable, argumentée et durable.` / `Synthèse pédagogique interne`.
- **Scène unique :** parcours de huit postes : utilisateur → proposition → découpage → six exigences V5 → débat → décision → documentation → référentiel publié/entretenu.
- **Description :** construction d'un commun vérifiable, de la difficulté vécue jusqu'à une règle documentée et entretenue ; représentation pédagogique, pas organigramme officiel.
- **Oral :** recueillir une seule formulation réutilisable le lendemain ; remercier, sans ajouter un quiz imprévu.
- **Sources :** ensemble du corpus indiqué plus bas.
- **Mémo final :** « Le besoin donne le sens ; la preuve et le débat rendent la règle partageable. »

## 6. Références de révision — libellés officiels des règles citées

Pour éviter de substituer les labels courts des slides aux formulations officielles, consulter les fiches publiques correspondantes :

| N° | Libellé V5 consulté | Fonction pédagogique |
|---|---|---|
| [72](https://checklists.opquast.com/fr/qualite-numerique/72) | Le format de saisie des champs de formulaire qui le nécessitent est indiqué | Cas de non-doublon et atelier final |
| [87](https://checklists.opquast.com/fr/qualite-numerique/87) | Les processus complexes sont accompagnés de la liste de leurs étapes. | Atelier final : montrer les étapes à l'utilisateur |
| [140](https://checklists.opquast.com/fr/qualite-numerique/140) | Les liens sont visuellement différenciés du reste du contenu. | Décomposition d'une attente |
| [152](https://checklists.opquast.com/fr/qualite-numerique/152) | Tous les liens internes sont valides. | Fil rouge et distinction résultat/processus |
| [155](https://checklists.opquast.com/fr/qualite-numerique/155) | Il est possible de revenir à la page d’accueil depuis toutes les pages. | Décomposition d'une attente |
| [156](https://checklists.opquast.com/fr/qualite-numerique/156) | Chaque page affiche une information permettant de connaître son emplacement dans l’arborescence. | Décomposition d'une attente |
| [159](https://checklists.opquast.com/fr/qualite-numerique/159) | Les icônes de navigation sont accompagnées d’une légende explicite. | Décomposition d'une attente |
| [168](https://checklists.opquast.com/fr/qualite-numerique/168) | Un moteur de recherche interne est proposé. | Décomposition d'une attente |
| [223](https://checklists.opquast.com/fr/qualite-numerique/223) | Le serveur envoie une page d’erreur 404 personnalisée. | Unicité, 404 |
| [224](https://checklists.opquast.com/fr/qualite-numerique/224) | Le serveur envoie une page d’interdiction 403 personnalisée. | Unicité, 403 |
| [233](https://checklists.opquast.com/fr/qualite-numerique/233) | Le codage de caractères utilisé est UTF-8. | Nuance rédactionnelle et chiffres |

**Attention aux portées :** le rapprochement historique des « liens morts » vise à montrer la vérifiabilité ; la règle V5 152 dit bien **liens internes**. L'exemple 403/404 est un contraste de deux règles réelles, pas une promesse que l'auditeur peut toujours provoquer une 403 dans tous les contextes.

## 7. Pièges à enseigner sans les transformer en questions officielles

| Confusion | Correction à installer | Référence |
|---|---|---|
| « Bonne idée = règle » | Une proposition doit répondre au contrat du référentiel. | Atelier V5 ; article 2021 |
| « Vérifier chaque semaine = liens valides » | Procédure interne ≠ constat du résultat. | Article 2005 ; règle 152 |
| « 403 et 404, c'est pareil » | Deux situations indépendantes, deux règles. | 223 / 224 |
| « Universelle = applicable sur tous les sites » | Une règle peut n'être pertinente que si l'objet existe. | Atelier V5 ; interprétation d'audit |
| « Aucun chiffre possible dans un libellé » | L'atelier V5 vise les valeurs *empiriques* arbitraires ; un identifiant comme UTF-8 n'est pas un seuil. | Atelier V5 ; règle 233 |
| « Consensus = septième critère V5 » | Consensus traité séparément sur la page de l'atelier ; la liste de 2019 est différente. | Atelier V5 ; article 2019 |
| « La règle détaille la technologie » | Les moyens de réalisation peuvent figurer dans la fiche ; ne pas confondre libellé et solution. | Fiches 152/233 |
| « Recommandation = mauvaise pratique » | Peut être pertinente mais non adaptée à la checklist. | Avril 2025 |
| « Déjà couvert = inutile » | Enrichir une fiche peut être préférable à créer une règle. | Fil règle 72 |
| « Un audit Opquast remplace une expertise RGAA » | C'est un socle transversal, non un substitut aux référentiels spécialisés. | Atelier V5 |

## 8. Carte de révision

```text
PERSONNE EN DIFFICULTÉ
   ↓ Quel besoin ? Quel préjudice ?
PROPOSITION
   ↓ Unité ; périmètre ; doublon ?
ATELIER V5 : SIX EXIGENCES
   ├── utilité et réalisme
   ├── universalité
   ├── vérifiabilité
   ├── absence de seuil empirique arbitraire
   └── unicité
   ↓
DISCUSSION, FORMULATION, ARBITRAGE
   ├── accord recherché, désaccord examiné
   ├── recommandation ou refus possibles
   └── enrichissement d'une règle existante possible
   ↓
FICHE : LIBELLÉ + OBJECTIFS + SOLUTION + MOYEN DE CONTRÔLE
   ↓
RÉFÉRENTIEL PUBLIÉ, RÉEXAMINÉ DANS LE TEMPS
```

## 9. Frontières, sources et couverture réelle

### Corpus effectivement accessible et vérifié dans cette refonte

- [Atelier officiel V5, « sanity check », rédaction, conflits et droits](https://checklists.opquast.com/workshops/assurance-qualite-web/) : **lu directement** ; liste V5 des six exigences, rôle des conflits et limite des référentiels spécialisés.
- [Article Opquast 12 juillet 2005](https://www.opquast.com/2005071239-les-dix-regles-du-contributeur-connaitre-il-te-faut/) : **lu directement** ; liens morts/processus, 403/404, contribution et consensus.
- [Article Opquast 25 novembre 2019](https://www.opquast.com/opquast-version-4-lancement-des-ateliers/) : **lu directement** ; processus d'atelier V4 et liste historique à sept items, différente de V5.
- [Article Opquast 26 janvier 2021](https://www.opquast.com/la-fin-des-bonnes-pratiques-opquast/) : **lu directement** ; passage du mot « bonnes pratiques » à « règles ».
- [Compte rendu Opquast du 11 avril 2025](https://www.opquast.com/check-list-opquast-version-5-point-detape-11-avril-2025/) et [discussion 2025 sur les contraintes de mot de passe](https://checklists.opquast.com/workshops/assurance-qualite-web/criterion/54578/) : **lus directement** ; véritables décisions, doublons, recommandations et reformulations.
- [Annonce de publication V5, 2 octobre 2025](https://www.opquast.com/publication-de-la-version-5-du-referentiel-opquast/) : **lue directement** ; travail collectif, numérotation 245, évolution du périmètre applicatif.
- **Onze fiches V5 citées dans la section 6 :** consultées sur le référentiel public en octobre 2026 (avec leurs libellés et, pour les cas centraux, objectifs, solutions et contrôles). La consultation du site **n'est pas présentée comme un appel réussi à `getRuleByNumber`**.
- [Glossaire public Opquast](https://checklists.opquast.com/fr/qualite-numerique/glossaire/) : lu ; **extrait uniquement** de définitions, ne permet pas une étude exhaustive du glossaire réservé aux stagiaires. Le vocabulaire de l'atelier (`règle`, `recommandation`, `contrôle`, `unicité`) est expliqué pédagogiquement ; ne pas prétendre citer des définitions officielles intégrales non accessibles.

### Corpus mentionné dans les fichiers source, mais non relu ici intégralement

- Livre *Qualité et conformité des services numériques*, 4e édition 2026, chapitre « Créer un commun numérique » ; sa teneur est **rapportée par le storyboard v005 fourni**, mais l'intégralité du chapitre n'était pas jointe. Les références précises ne sont pas inventées ni présentées comme une nouvelle consultation.
- Guide de certification *Mobiliser un référentiel qualité numérique*, septembre 2025 ; idem. Certaines formulations présentes dans le storyboard v005 ne sont pas reprises en citation littérale faute d'accès au passage intégral.
- Archives historiques de toutes les versions et corpus complet des newsletters : non parcourus de manière exhaustive.
- API/MCP Opquast `getRuleByNumber` : **non invoqué** lors de cette refonte. Les pages publiques V5 ont été vérifiées individuellement ; une ultime validation API est recommandée avant production si l'outil est disponible.

### Hiérarchie et niveau de confiance

1. **Établi explicitement** : six exigences du *sanity check* V5 ; procédure de discussion/conflit ; exemples historiques datés ; formulations actuelles des règles citées ; structure des fiches V5.
2. **Fortement soutenu** : valeur pédagogique d'examiner la preuve, le doublon et le bénéfice utilisateur avant de retenir un texte ; nécessité d'une rédaction durable.
3. **Interprétation pédagogique assumée** : chaîne en huit postes, fil rouge reconstruit autour du n° 152, découpages et minutages, formulations des mémos, regroupement des activités.

### Ce que cette séance ne prétend pas enseigner

- Les 245 règles une à une ; tous les critères d'audit ou les moyens de contrôle détaillés ; le fonctionnement interne précis des décisions chez Opquast pour chaque règle ; les questions officielles de la certification ; les exigences complètes du RGAA/WCAG/RGESN.
- L'objectif est de comprendre **l'architecture du commun** et d'apprendre à raisonner, pas de se substituer à la méthode intégrale des ateliers ou à la documentation complète.

## 10. Revue finale avant génération des images

- [ ] Accord métier sur le passage de 11 slides/45 min + ajout à **16 slides/60 min intégrées**.
- [ ] Le terme « six exigences V5 » est exact ; aucun « sept critères officiels 2025 » non sourcé n'apparaît sur les images.
- [ ] Les regroupements, chaînes, mémos et exercices portent la mention « pédagogique » lorsqu'un risque de confusion existe.
- [ ] Les libellés officiels des règles citées sont repris sans altération lorsqu'ils apparaissent comme tels ; leurs numéros correspondent.
- [ ] Chaque slide possède **une seule scène** et une **description textuelle**, jamais une distinction transmise uniquement par la couleur.
- [ ] Pas de correction visible pendant les slides 07 et 14.
- [ ] La règle 152 n'est pas étendue aux liens externes.
- [ ] UTF-8 ne devient pas une prétendue « exception aux seuils ».
- [ ] La séance ne laisse pas croire que les binômes ont produit une règle officielle.
- [ ] Les minutages du conducteur ont été testés en répétition orale, avec une marge de gestion des prises de parole.

## 11. Sources bibliographiques et réutilisation

**Référentiel officiel V5 :** [245 règles 2025–2030](https://checklists.opquast.com/fr/qualite-numerique/). Les règles et les objectifs V5 sont diffusés sous [licence CC BY-SA 4.0](https://checklists.opquast.com/fr/qualite-numerique/licence/) : attribution Opquast, lien vers la licence, indication de nos adaptations pédagogiques, et partage dans les mêmes conditions lorsque la licence le requiert. Les articles et contenus de formation n'ont pas nécessairement la même licence : ce dossier leur renvoie par liens et emploie des synthèses brèves plutôt que des reproductions étendues.

**Attribution suggérée pour le futur support :** « Sources : Opquast, référentiel Qualité Numérique V5 et publications Opquast ; adaptation et animation pédagogique indépendante, octobre 2026. Ce support n'est pas une publication officielle d'Opquast. »

---

**Historique de révision :** v005 fourni : 11 slides, périmètre de 30–60 minutes, validation antérieure du 6 octobre 2026 ; v006 : refonte d'une heure intégrant le consensus, les arbitrages réels 2025, le fil rouge, les six exigences affichées par l'atelier V5, la correction UTF-8, une activité intégrée, les descriptions textuelles et un rapport de couverture explicite. La validation du précédent storyboard ne vaut pas validation automatique de cette version.
