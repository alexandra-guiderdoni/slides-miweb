# Storyboard de production — Projets et livrables selon Opquast V5
## Version v001 dérivée du storyboard V008 consolidé

**Statut :** `VALIDE_POUR_GENERATION`, revue de production signée par
délégation explicite de la référente Opquast le 11 octobre 2026.
**Durée totale :** **60 minutes exactement**, temps d'interactions et de transitions compris (23 séquences, voir le minutage).
**Public :** professionnels de la conception, de la production, du pilotage et de la maintenance, ainsi que candidats à la certification Opquast.
**Niveau :** intermédiaire.
**Périmètre des sources :** livre *Qualité et conformité des services numériques*, 4e édition (2026) ; glossaire et articles Opquast fournis ; API `qualite-numerique` pour les **cinq règles vérifiées individuellement** : 234, 77, 69, 85 et 222.
**Cas :** page éditoriale fictive « Préparer sa demande », formulaire de contact fictif, URL inexistante fictive. Aucune inspection de site réel n'est revendiquée.

### Contrat pédagogique

> **La qualité circule, la preuve se construit.**
> Une règle peut être anticipée sur plusieurs supports, mais chaque contrôle ne prouve que ce qui est observable dans le périmètre examiné.

Cette phrase, l'enchaînement entre les livrables et l'inventaire de 59 objets sont **des constructions pédagogiques**. Ce ne sont ni une règle ni une méthode projet obligatoire d'Opquast.

**Définitions de travail :** « phase » = repère temporel ; « livrable » = document, interface, code, contenu, configuration ou trace produit ; « contrôle » = opération d'examen ; « trace de contrôle » = résultat et limites consignés. Le terme « preuve » désigne ici une trace contextualisée, sans valeur de certification globale. Le glossaire du livre réserve « contrôle qualité » à un emploi plus spécifique en fin de production ; les revues intermédiaires ne doivent pas être présentées comme une validation générale.

### Ce que contient cette version

- **23 slides essentielles intégrées et numérotées**, suivies de 22 slides
  d’atlas dans le même jeu.
- **Une cartographie visible des 12 familles**, puis un **atlas de 59 entrées
  nominatives**, chacune avec fonction, contexte, risque, examen possible,
  limite et provenance.
- **Trois situations utilisateur**, cinq règles officielles vérifiées, des niveaux de preuve distincts.
- **Un déroulé minuté de 60 minutes**, y compris les interactions.
- Des annexes de comparaison, d'exercices, de traçabilité et de préparation graphique.

Les « textes à l'écran » sont exacts en tant que propositions de slide, mais les **citations de règles** sont identifiées séparément comme formulations officielles. Aucun pictogramme, tag ou classement analytique ne doit être confondu avec la métadonnée officielle.

### Verrou de production

- Header gauche exact : `QUALITÉ WEB`, puis `EXPÉRIENCES DURABLES`.
- Header droit exact : `Opquast`, puis `DES SITES MEILLEURS POUR TOUS`.
- Footer exact : `RÈGLES OPQUAST · PROJETS ET LIVRABLES`.
- Pagination exacte : `NN / 45`.
- Slides 01 à 23 : `ESSENTIEL_60`, positions 01 à 23 dans le même ordre.
- Slides 24 à 45 : `ANNEXE`, badge visible `ATLAS`.
- Slogan `La qualité circule, la preuve se construit` : slides 01 et 23
  seulement.
- Référence visuelle : grammaire des 17 premières slides de
  `navigation-opquast-v5-360`, sans reprise de contenu.
- Tous les écrans fictifs portent la mention `SIMULATION`.
- Toute citation de règle reste distincte d’une traduction projet.
- Aucun verdict global, aucune obligation universelle et aucune chronologie
  des 12 familles.
- Les textes visibles des slides 01 et 23 comprennent le slogan en plus des
  textes V008. Pour les slides 02 à 22, les textes visibles V008 restent
  inchangés.
- Chaque slide essentielle reprend comme préparation orale le discours et le
  mémo du bloc V008 correspondant. Les consignes de durée et d’interaction
  restent hors des accordéons.
- Pour chaque slide essentielle, le rôle narratif, la situation, le risque,
  le principe de prévention, la garantie limitée, les règles, les limites,
  les sources, les relations visuelles, les textes visibles et la transition
  sont ceux du bloc V008 correspondant, référencé dans la matrice.
- Critère d’acceptation commun : une idée principale, textes exacts, relations
  conformes au bloc source, header, badge, footer et pagination exacts, aucun
  texte parasite.
- Critère de rejet commun : faute, numéro erroné, relation ajoutée, preuve
  surprometteuse, faux logo, microtexte, élément décoratif interdit ou ratio
  incompatible.

## Sommaire et minutage

| Séquence | Slides | Durée | Objet |
|---|---|---:|---|
| I. Poser le problème | 01 à 06 | 15 min | Risque utilisateur, cartographie des 59 livrables, distinctions et tags |
| II. Comprendre le contenu | 07 à 11 | 16 min | Règle 234, de l'intention au contrôle rendu |
| III. Accomplir une action | 12 à 15 | 12 min | Règles 77, 69 et 85, trois preuves différentes |
| IV. Ressource absente | 16 à 17 | 6 min | Règle 222, page visible et réponse HTTP |
| V. Tracer, décider, maintenir | 18 à 23 | 11 min | Comparaison, constat, correction, limites et exercice |
| **Total** | **23 slides** | **60 min** | **Interactions comprises** |

### Carte des 12 familles de livrables

| Comprendre et spécifier | Concevoir et produire | Vérifier et livrer | Exploiter et piloter |
|---|---|---|---|
| Cadrage (6) | Conception fonctionnelle (5) | Tests et recette (6) | Exploitation (3) |
| Recherche utilisateur (5) | Design graphique (5) | Livraison (3) | Pilotage (4) |
| Spécifications (5) | Développement (6) |  |  |
| Architecture de l'information (5) | CMS et éditorial (6) |  |  |

**Total : 59 objets regroupés en 12 familles.** Ce classement est pédagogique et reflète l'inventaire détaillé en annexe A1. Les familles se chevauchent dans un vrai projet ; ce ne sont pas douze phases chronologiques.

---

# I. Poser le problème


## Slide 01 : L’utilisateur ne voit pas nos phases projet

**Durée : 2 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Partir du vécu utilisateur, pas de la succession des métiers.

**Écran, textes exacts à afficher :** « Je veux trouver une information, transmettre une demande et obtenir une réponse. »

**Scène et intention visuelle :** Un parcours en trois scènes continue : lecture, formulaire, résultat. Sous la ligne de parcours, des silhouettes métiers interviennent sans la découper.

**Préjudice utilisateur :** Une personne peut perdre du temps, faire une erreur ou rester sans réponse. Elle ne connaît pas les frontières internes des équipes.

**Ce que vise la règle ou la démarche :** Le point de vue utilisateur rend intelligibles les exigences communes.

### Discours oral

> « Quand je cherche une information ou que je remplis un formulaire, je ne vois pas les phases de votre projet. Je vois un service. Si je suis bloqué, peu importe que le problème vienne du design, du code ou du contenu. C'est pourquoi nous partirons des difficultés réelles des personnes, avant de parler des métiers et des documents qui permettent de les prévenir. Le parcours est continu, les contributions sont multiples. »

**Mémo oral :** `Un parcours, plusieurs métiers.`

**Sources :** Livre, partie 1, chapitre 1, « Ensemble pour les utilisateurs ».


## Slide 02 : La qualité circule, la preuve se construit

**Durée : 2 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Faire de la phrase centrale une méthode de lecture de tous les exemples.

**Écran, textes exacts à afficher :** « Risque utilisateur → exigence → contributions → contrôle → constat → décision → recontrôle »

**Scène et intention visuelle :** Une ligne traversant plusieurs supports avec des boucles de retour ; aucun tampon « conforme » avant une vérification appropriée.

**Préjudice utilisateur :** Une exigence peut être perdue ou considérée à tort comme déjà vérifiée.

**Ce que vise la règle ou la démarche :** La démarche proposée facilite le partage des exigences et la traçabilité des vérifications.

### Discours oral

> « Une règle peut être utile dès les premières discussions, puis guider une spécification, une maquette, un gabarit ou une configuration. Mais ce cheminement n'est pas une validation progressive automatique. Il faut distinguer ce qui a été prévu, ce qui a été produit et ce qui a été réellement contrôlé. Cette chaîne est une proposition pédagogique inspirée de la démarche qualité décrite dans le livre, pas une procédure obligatoire fixée par Opquast. »

**Mémo oral :** `Circuler n'est pas prouver.`

**Sources :** Livre, partie 2, sections 3.2, 3.4 et 4.1.


## Slide 03 : La carte complète des 59 livrables

**Durée : 4 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Montrer les 12 familles et leurs 59 exemples sans transformer la slide en catalogue.

**Écran, textes exacts à afficher :** « 12 familles · 59 livrables et objets de projet » ; « Documents, interfaces, code, contenus, traces » ; « Inventaire détaillé en annexe »

**Scène et intention visuelle :** 12 blocs reliés en réseau, regroupés visuellement en quatre zones : comprendre et spécifier ; concevoir et produire ; vérifier et livrer ; exploiter et piloter. Chaque bloc affiche sa famille et son nombre, pas les 59 libellés en minuscule.

**Préjudice utilisateur :** Une contribution oubliée peut laisser un défaut utilisateur se propager jusqu'au service final.

**Ce que vise la règle ou la démarche :** Cette carte aide à repérer les supports pertinents pour chaque exigence et les responsables possibles.

### Discours oral

> « Voici notre carte de référence : douze familles et cinquante-neuf livrables ou objets de projet. Il y a des documents, des maquettes, du code, des contenus publiés et des traces de contrôles. Ils ne sont pas tous obligatoires, et ils ne suivent pas partout le même ordre. Nous les utiliserons comme un répertoire : pour une situation utilisateur, quels supports permettent d'anticiper le risque ? Et sur quel objet pourra-t-on réellement le vérifier ? »

**Mémo oral :** `Inventorier pour relier, pas pour imposer.`

**Interaction prévue :** Demander à deux participants de citer un livrable avant publication et un objet encore modifiable après publication.

**Indication de fabrication :** les 12 familles et leurs nombres doivent être lisibles sans agrandissement. Les 59 noms figurent dans les slides 24 à 45 et en annexe A1, plutôt que d'être entassés dans cette slide.

**Sources :** Inventaire analytique A1 ; livre, partie 2, chapitre 3 et chapitre 4.


## Slide 04 : Phase, livrable, contrôle, preuve : quatre notions

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Ne pas déduire le contrôle d'une phase ou d'un simple intitulé de livrable.

**Écran, textes exacts à afficher :** « Phase : quand ? » ; « Livrable : quoi ? » ; « Contrôle : comment ? » ; « Trace : qu'a-t-on observé ? »

**Scène et intention visuelle :** Quatre colonnes avec un même exemple : production / page rendue / examen des titres / fiche de constat. Une flèche indique le périmètre réel de la preuve.

**Préjudice utilisateur :** Un « validé » ambigu peut masquer un défaut restant.

**Ce que vise la règle ou la démarche :** Le vocabulaire explicite permet de documenter les attentes et les constats.

### Discours oral

> « Une phase est un repère dans le temps. Un livrable est un objet de travail. Un contrôle est une observation selon des critères. Enfin, la trace conserve la méthode, le résultat et les limites. Un prototype peut donc être relu sans que le code final soit vérifié. Le mot « preuve » est ici une trace contextualisée, pas une certification du service. Cette distinction va nous servir dans chaque exemple. »

**Mémo oral :** `La phase situe ; le contrôle constate.`

**Sources :** Livre, partie 2, sections 3.4 et 4.1 ; organisation pédagogique.


## Slide 05 : Les tags de phase ne sont pas un calendrier

**Durée : 2 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Expliquer l'évolution annoncée des tags sans prétendre qu'elle est uniformément déployée.

**Écran, textes exacts à afficher :** « Tags de phase : conception, développement, éditorial » ; « Évolution annoncée : fonctionnel, technique, contenus » ; « Tag ≠ moment obligatoire »

**Scène et intention visuelle :** Deux listes de tags reliées à des contributions. Note en bas : « Article 14 avril 2026 : évolution annoncée ; API actuelle : coexistence constatée sur certains exemples ».

**Préjudice utilisateur :** En enfermant une règle dans une phase, l'équipe peut croire que le sujet ne la concerne pas.

**Ce que vise la règle ou la démarche :** Les tags servent à repérer, pas à attribuer mécaniquement les contrôles.

### Discours oral

> « Dans un article du 14 avril 2026, Opquast a annoncé le remplacement des tags liés aux phases par une classification fonctionnelle, technique et contenus. Nos fiches API vérifiées montrent encore des libellés de familles différents selon les règles. Il ne faut donc ni confondre annonce et déploiement achevé, ni lire un tag comme un planning. Une exigence peut appeler des contributions à plusieurs moments et sur plusieurs supports. »

**Mémo oral :** `Un tag classe, il ne planifie pas.`

**Sources :** Article Opquast « Au programme : livre, tags et numérique », 14 avril 2026 ; métadonnées API des règles étudiées.


## Slide 06 : Choisir les règles d'après le risque et l'applicabilité

**Durée : 2 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Introduire les cas choisis et leurs limites : cinq règles, pas la checklist entière.

**Écran, textes exacts à afficher :** « Titres : 234 » ; « Formulaire : 77, 69, 85 » ; « URL absente : 222 » ; « Sélection pédagogique, pas liste universelle »

**Scène et intention visuelle :** Trois cartes de situations utilisateur menant à cinq règles ; les 59 livrables restent en arrière-plan comme une bibliothèque.

**Préjudice utilisateur :** Une règle non applicable mobilise inutilement l'équipe ; une règle applicable oubliée laisse un risque.

**Ce que vise la règle ou la démarche :** Une sélection raisonnée relie les besoins à des critères précis sans prétendre tout couvrir.

### Discours oral

> « Nous allons étudier trois risques différents : ne pas se repérer dans un contenu, ne pas comprendre ou confirmer un formulaire, et obtenir une réponse incohérente pour une ressource absente. Nous retiendrons cinq règles officiellement vérifiées. Ce sont des cas d'enseignement, pas un classement Opquast de la thématique « phases projet ». Nous verrons que le contrôle officiel porte chaque fois sur un objet différent. L'annexe complète les exemples par une cartographie plus large des livrables. »

**Mémo oral :** `Choisir selon le risque, vérifier selon l'objet.`

**Sources :** API Opquast, règles 234, 77, 69, 85 et 222 ; sélection pédagogique.


# II. Situation 1 : comprendre le contenu


## Slide 07 : Je ne retrouve pas ma section

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Le cas utilisateur de la règle 234 : la hiérarchie du contenu.

**Écran, textes exacts à afficher :** « Après l’envoi : où se trouve cette sous-section ? » ; « 234 : structure des titres et sous-titres »

**Scène et intention visuelle :** Deux plans simulés d'une page « Préparer sa demande » : h1→h2→h2→h4 et h1→h2→h2→h3. La sous-section directe de « Déposer le dossier » est mise en évidence.

**Préjudice utilisateur :** Une personne qui navigue par titres peut mal situer la sous-section et perdre du temps.

**Ce que vise la règle ou la démarche :** La règle 234 vise une structure de titres navigable et interprétable par les outils.

**Règle 234 (formulation officielle exacte) :**
> « Le contenu de chaque page est organisé selon une structure de titres et sous-titres hiérarchisée. »

**Objectif officiel, résumé fidèle :** Permettre de visualiser la structure du contenu et d’y naviguer, et de faciliter l'extraction du plan par les outils.

**Contrôle officiel, synthèse :** Sur chaque page, vérifier au moins un h1 correspondant à la section principale, les sous-titres nécessaires et l'absence de saut descendant. Inclure les titres masqués et générés par JavaScript.

*(API Opquast, règle n° 234, version `qualite-numerique`.)*

**Mécanisme à expliquer :** Titres HTML h1 à h6 organisés selon la structure des contenus.

**Limite / confusion à éviter :** Un h1 n'est pas nécessairement unique ; le contrôle ne se limite pas à la taille visuelle des textes.

### Discours oral

> « Imaginez une personne qui explore les titres de « Préparer sa demande ». La rubrique « Déposer le dossier » est un h2. Sa sous-section « Après l'envoi » devrait suivre la hiérarchie du contenu. Si elle est codée directement en h4, le plan extrait devient trompeur. Le texte n'est pas forcément invisible, mais l'orientation est plus difficile. La règle 234 nous donne un critère vérifiable pour éviter ce problème. »

**Mémo oral :** `Un plan cohérent pour se repérer.`

**Sources :** API Opquast, règle 234, version `qualite-numerique`.


## Slide 08 : Transformer la règle 234 en exigence de projet

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Faire entrer la règle dans les spécifications sans remplacer son texte officiel.

**Écran, textes exacts à afficher :** « Règle 234 » ; « Exigence proposée : les pages éditoriales rendent leur plan de titres cohérent avec leurs sections » ; « Périmètre + critères + responsable »

**Scène et intention visuelle :** Une ligne de cahier des charges liée à la fiche officielle, puis à une User Story et à des critères d'acceptation ; les éléments créés pour l'exercice sont marqués « projet fictif ».

**Préjudice utilisateur :** Sans attente précise, une page mal structurée peut être livrée sans que personne n'ait prévu son contrôle.

**Ce que vise la règle ou la démarche :** Le cahier des charges et les critères rendent l'attente transmissible aux métiers.

**Règle 234 (formulation officielle exacte) :**
> « Le contenu de chaque page est organisé selon une structure de titres et sous-titres hiérarchisée. »

**Objectif officiel, résumé fidèle :** Permettre de visualiser la structure du contenu et d’y naviguer, et de faciliter l'extraction du plan par les outils.

**Contrôle officiel, synthèse :** Sur chaque page, vérifier au moins un h1 correspondant à la section principale, les sous-titres nécessaires et l'absence de saut descendant. Inclure les titres masqués et générés par JavaScript.

*(API Opquast, règle n° 234, version `qualite-numerique`.)*

**Mécanisme à expliquer :** Cahier des charges, backlog et critères d'acceptation.

### Discours oral

> « Le libellé officiel de la règle 234 est notre référence. Dans un projet, nous pouvons le traduire en une exigence plus opérationnelle : pour quels types de pages ? Qui produit le contenu ? Que devra montrer la page rendue ? Les critères d'acceptation ne sont pas la règle elle-même : ils l'appliquent au contexte. La spécification n'atteste aucun résultat, mais elle évite que la question soit découverte trop tard. »

**Mémo oral :** `Spécifier n'est pas valider.`

**Sources :** Livre, partie 2, section 3.2 ; API 234 ; critères proposés.


## Slide 09 : Le prototype anticipe, la maquette transmet

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Rendre visible le niveau de contrôle d'un wireframe et d'une maquette.

**Écran, textes exacts à afficher :** « Prototype : structure prévue » ; « Maquette : sections titrées transmises » ; « HTML final : non prouvé »

**Scène et intention visuelle :** Un wireframe puis une maquette graphique du même contenu, avec annotations « titre principal », « section », « sous-section ».

**Préjudice utilisateur :** L'utilisateur risque de perdre la hiérarchie prévue lors du passage d'un métier à l'autre.

**Ce que vise la règle ou la démarche :** Les revues intermédiaires peuvent identifier des problèmes de structuration avant le code.

**Règle 234 (formulation officielle exacte) :**
> « Le contenu de chaque page est organisé selon une structure de titres et sous-titres hiérarchisée. »

**Objectif officiel, résumé fidèle :** Permettre de visualiser la structure du contenu et d’y naviguer, et de faciliter l'extraction du plan par les outils.

**Contrôle officiel, synthèse :** Sur chaque page, vérifier au moins un h1 correspondant à la section principale, les sous-titres nécessaires et l'absence de saut descendant. Inclure les titres masqués et générés par JavaScript.

*(API Opquast, règle n° 234, version `qualite-numerique`.)*

### Discours oral

> « Le prototype permet de discuter la place des sections. La maquette graphique permet de transmettre cette intention plus précisément, par exemple en annotant les niveaux de titres attendus. Ce sont deux occasions de détecter un plan incohérent. Mais ni le wireframe ni la maquette ne démontrent les éléments HTML que recevra l'utilisateur. C'est exactement notre distinction : une exigence circule, et chaque livrable n'en montre qu'une partie. »

**Mémo oral :** `Voir l'intention n'est pas voir le HTML.`

**Sources :** Livre, partie 2, sections 3.5 et 3.6 ; glossaire « Wireframe », « Maquette graphique » ; API 234.


## Slide 10 : Le gabarit et le CMS matérialisent, le contenu peut changer

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Montrer la dépendance entre gabarit technique et contribution éditoriale.

**Écran, textes exacts à afficher :** « Gabarit : h1 / h2 / h3 » ; « Contribution fictive : h2 → h4 » ; « Page publiée : à examiner »

**Scène et intention visuelle :** Gabarit générant la bonne structure ; éditeur CMS avec une sous-section saisie en h4 ; rendu final marqué d'un point d'interrogation avant examen.

**Préjudice utilisateur :** Un gabarit sain n'empêche pas qu'un titre saisi ultérieurement rende la structure incohérente.

**Ce que vise la règle ou la démarche :** La règle 234 vise la structure effective de chaque page, pas l'intention isolée d'un composant.

**Règle 234 (formulation officielle exacte) :**
> « Le contenu de chaque page est organisé selon une structure de titres et sous-titres hiérarchisée. »

**Objectif officiel, résumé fidèle :** Permettre de visualiser la structure du contenu et d’y naviguer, et de faciliter l'extraction du plan par les outils.

**Contrôle officiel, synthèse :** Sur chaque page, vérifier au moins un h1 correspondant à la section principale, les sous-titres nécessaires et l'absence de saut descendant. Inclure les titres masqués et générés par JavaScript.

*(API Opquast, règle n° 234, version `qualite-numerique`.)*

### Discours oral

> « Une fois le gabarit intégré, on peut inspecter les titres qu'il génère. Le CMS peut aussi guider les contributeurs avec des modèles de saisie ou des consignes. Mais une contribution ultérieure peut réintroduire le défaut : un h4 sous un h2, par exemple. Il faut donc penser à la fois au développeur et à la personne qui publie le contenu. Et surtout, contrôler ce qui est finalement rendu. »

**Mémo oral :** `Le gabarit aide, le contenu décide du rendu.`

**Sources :** Livre, partie 2, sections 3.7 à 3.9 ; API 234.


## Slide 11 : Contrôler la page rendue et borner le constat

**Durée : 4 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Conclure le premier cas par une vérification appropriée et son périmètre.

**Écran, textes exacts à afficher :** « Une page simulée : h1 → h2 → h2 → h4 » ; « Saut descendant constaté dans la simulation » ; « Une page ≠ tout le service »

**Scène et intention visuelle :** Vue du plan de titres, résultat du contrôle, mini-fiche objet/version/constat/limite ; aucune coche de conformité générale.

**Préjudice utilisateur :** L'utilisateur peut rester gêné malgré des validations antérieures.

**Ce que vise la règle ou la démarche :** Le contrôle officiel de la règle 234 permet d'évaluer les titres HTML des pages concernées.

**Règle 234 (formulation officielle exacte) :**
> « Le contenu de chaque page est organisé selon une structure de titres et sous-titres hiérarchisée. »

**Objectif officiel, résumé fidèle :** Permettre de visualiser la structure du contenu et d’y naviguer, et de faciliter l'extraction du plan par les outils.

**Contrôle officiel, synthèse :** Sur chaque page, vérifier au moins un h1 correspondant à la section principale, les sous-titres nécessaires et l'absence de saut descendant. Inclure les titres masqués et générés par JavaScript.

*(API Opquast, règle n° 234, version `qualite-numerique`.)*

### Discours oral

> « Sur notre page fictive, le premier critère est satisfait : un h1 correspond à la section principale. Mais il existe un saut descendant de h2 à h4. Le contrôle simulé conclut donc à un écart sur cette page. Dans un contrôle réel, nous examinerions aussi les titres masqués ou générés par JavaScript. Le constat doit préciser le périmètre observé : il ne dit rien, à lui seul, de toutes les pages du service. »

**Mémo oral :** `La preuve a un périmètre.`

**Interaction prévue :** Faire identifier au groupe ce que la maquette n'aurait pas pu démontrer.

**Sources :** API 234, contrôle officiel ; livre, partie 2, sections 4.1 et 4.6.


# III. Situation 2 : accomplir une action


## Slide 12 : Je ne sais pas quoi saisir

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Le cas utilisateur d'un formulaire mal compréhensible.

**Écran, textes exacts à afficher :** « Quel champ dois-je remplir ? » ; « Les étiquettes me guident-elles ? »

**Scène et intention visuelle :** Formulaire de contact fictif avec deux étiquettes éloignées de leurs champs, puis disposition corrigée. Aucun texte légal.

**Préjudice utilisateur :** La personne peut confondre les champs, commettre des erreurs et perdre du temps.

**Ce que vise la règle ou la démarche :** Les règles sur les étiquettes visent une identification sans ambiguïté des champs et une saisie facilitée.

**Règle 77 (formulation officielle exacte) :**
> « Chaque étiquette de formulaire est visuellement rattachée au champ qu’elle décrit. »

**Objectif officiel, résumé fidèle :** Permettre d'identifier les champs et réduire les erreurs de saisie.

**Contrôle officiel, synthèse :** Vérifier le rattachement visuel sur le formulaire rendu à toutes les tailles d'écran et la position prévisible des étiquettes.

*(API Opquast, règle n° 77, version `qualite-numerique`.)*

**Règle 69 (formulation officielle exacte) :**
> « Chaque champ de formulaire est associé dans le code source à une étiquette qui lui est propre. »

**Objectif officiel, résumé fidèle :** Faciliter la compréhension des champs et leur restitution par les aides techniques.

**Contrôle officiel, synthèse :** Vérifier l'association dans le code (label et attributs ou équivalents ARIA) et la pertinence de l'étiquette, avec examen manuel.

*(API Opquast, règle n° 69, version `qualite-numerique`.)*

### Discours oral

> « Une personne doit pouvoir identifier rapidement à quoi sert chaque champ. Lorsque les étiquettes sont visuellement éloignées ou placées de façon inhabituelle, elle peut hésiter ou se tromper. Mais même une disposition claire sur une maquette ne dit pas si le champ est correctement étiqueté pour les outils d'assistance. C'est pourquoi deux règles différentes interviennent sur le même formulaire. Nous conservons les deux formulations officielles séparées. »

**Mémo oral :** `Un champ compréhensible sous deux angles.`

**Sources :** API Opquast, règles 77 et 69.


## Slide 13 : Règle 77 : le lien doit être visible

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Contrôler le rattachement visuel d'une étiquette et d'un champ.

**Écran, textes exacts à afficher :** « 77 : étiquette proche du champ » ; « Contrôle : formulaire rendu, toutes tailles d'écran »

**Scène et intention visuelle :** Un affichage bureau puis mobile du même formulaire, en soulignant le rapprochement de l'étiquette et du champ ; pas de code HTML présenté comme preuve.

**Préjudice utilisateur :** Un utilisateur peut saisir au mauvais endroit ou devoir déchiffrer la correspondance des champs.

**Ce que vise la règle ou la démarche :** La règle 77 vise une proximité visuelle non ambiguë et prévisible.

**Règle 77 (formulation officielle exacte) :**
> « Chaque étiquette de formulaire est visuellement rattachée au champ qu’elle décrit. »

**Objectif officiel, résumé fidèle :** Permettre d'identifier les champs et réduire les erreurs de saisie.

**Contrôle officiel, synthèse :** Vérifier le rattachement visuel sur le formulaire rendu à toutes les tailles d'écran et la position prévisible des étiquettes.

*(API Opquast, règle n° 77, version `qualite-numerique`.)*

**Mécanisme à expliquer :** Proximité et position prévisible des étiquettes.

**Limite / confusion à éviter :** La règle ne se réduit pas à une valeur universelle de distance : le contexte compte.

### Discours oral

> « La règle 77 concerne ce que l'utilisateur perçoit à l'écran. Nous cherchons à savoir si chaque étiquette est immédiatement rattachée au champ qu'elle décrit. Sur une maquette, nous pouvons anticiper le problème. Pour le contrôler, il faut regarder le formulaire réellement affiché à différentes tailles d'écran, notamment sur mobile. Une association correcte dans le code ne remplace pas cette vérification visuelle. »

**Mémo oral :** `77 : proche à l'écran.`

**Sources :** API Opquast, règle 77, version `qualite-numerique`.


## Slide 14 : Règle 69 : le lien doit exister dans le code

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Distinguer l'association technique de la proximité visuelle.

**Écran, textes exacts à afficher :** « 69 : champ ↔ étiquette dans le code » ; « Association + pertinence à vérifier »

**Scène et intention visuelle :** Formulaire rendu à gauche et extrait schématique de l'association HTML à droite : label[for] et input[id] correspondants ; option ARIA signalée.

**Préjudice utilisateur :** Un utilisateur d'aide technique peut ne pas connaître le rôle d'un champ ; un libellé imprécis peut aussi le tromper.

**Ce que vise la règle ou la démarche :** La règle 69 vise l'association de chaque champ à une étiquette qui décrit son rôle.

**Règle 69 (formulation officielle exacte) :**
> « Chaque champ de formulaire est associé dans le code source à une étiquette qui lui est propre. »

**Objectif officiel, résumé fidèle :** Faciliter la compréhension des champs et leur restitution par les aides techniques.

**Contrôle officiel, synthèse :** Vérifier l'association dans le code (label et attributs ou équivalents ARIA) et la pertinence de l'étiquette, avec examen manuel.

*(API Opquast, règle n° 69, version `qualite-numerique`.)*

**Mécanisme à expliquer :** Association explicite en HTML ou par attributs ARIA ; pertinence à examiner.

**Limite / confusion à éviter :** L'association technique n'est pas suffisante si l'étiquette est incompréhensible.

### Discours oral

> « La règle 69 pose une autre question : existe-t-il dans le code une étiquette associée à ce champ précis ? Nous vérifions les attributs de liaison ou les solutions ARIA prévues par la fiche, puis nous contrôlons manuellement si le libellé est pertinent. Une capture d'écran ne permet pas d'établir cette association. À l'inverse, cette association ne prouve pas que les deux éléments sont assez proches visuellement. Deux règles, deux preuves. »

**Mémo oral :** `69 : liée dans le code.`

**Sources :** API Opquast, règle 69, version `qualite-numerique`.


## Slide 15 : Règle 85 : ai-je vraiment envoyé ma demande ?

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Une action utilisateur doit produire un retour explicite.

**Écran, textes exacts à afficher :** « Soumission complète → réussite ou échec explicite » ; « Règle 85 »

**Scène et intention visuelle :** Trois cases : formulaire, bouton envoyer, page de résultat « Demande transmise » ou « Envoi impossible », toutes fictives.

**Préjudice utilisateur :** Une personne peut croire sa demande envoyée alors que l'opération a échoué, puis attendre inutilement.

**Ce que vise la règle ou la démarche :** La règle 85 vise un retour immédiat et explicite sur le résultat de l'action.

**Règle 85 (formulation officielle exacte) :**
> « La soumission d’un formulaire est suivie d’un message indiquant la réussite ou non de l’action souhaitée. »

**Objectif officiel, résumé fidèle :** Fournir un retour explicite sur l'action et éviter une réussite seulement supposée.

**Contrôle officiel, synthèse :** Soumettre complètement le formulaire et vérifier une page de confirmation indiquant explicitement réussite ou échec.

*(API Opquast, règle n° 85, version `qualite-numerique`.)*

**Mécanisme à expliquer :** Page de confirmation explicite après la soumission finale.

**Limite / confusion à éviter :** Ne pas confondre confirmation de soumission et traitement ultérieur de la demande.

### Discours oral

> « Le formulaire peut être parfaitement lisible et ses champs correctement étiquetés. Il reste pourtant une question : après avoir envoyé ma demande, que s'est-il passé ? La règle 85 demande un message explicite de réussite ou d'échec après une soumission complète. Un prototype peut prévoir cet écran ; mais pour vérifier la règle, il faut accomplir le parcours. Une promesse de confirmation ne vaut pas une confirmation observée. »

**Mémo oral :** `Après l'action, dire le résultat.`

**Sources :** API Opquast, règle 85, version `qualite-numerique`.


# IV. Situation 3 : la ressource absente


## Slide 16 : Règle 222 : une ressource absente doit répondre 404

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Une règle serveur n'emprunte pas le même parcours de livrables.

**Écran, textes exacts à afficher :** « Ressource introuvable » ; « 222 : statut HTTP 404 »

**Scène et intention visuelle :** Adresse fictive inexistante ; serveur et navigateur échangeant une réponse HTTP avec code affiché distinctement.

**Préjudice utilisateur :** Une personne et les outils peuvent recevoir une information incohérente sur la disponibilité de la ressource.

**Ce que vise la règle ou la démarche :** La règle 222 vise la détection fiable des URL erronées et l'information transmise par le serveur.

**Règle 222 (formulation officielle exacte) :**
> « Le serveur envoie un code HTTP 404 pour les ressources non trouvées. »

**Objectif officiel, résumé fidèle :** Permettre la détection des URL erronées et transmettre une information fiable aux clients et outils.

**Contrôle officiel, synthèse :** Pour chaque service examiné, essayer une URL inexistante et vérifier que la réponse HTTP porte le statut 404.

*(API Opquast, règle n° 222, version `qualite-numerique`.)*

**Mécanisme à expliquer :** Réponse HTTP 404 à une URL inexistante.

**Limite / confusion à éviter :** La règle ne se satisfait pas d'un simple texte « 404 » dans la page.

### Discours oral

> « Cette fois, le risque ne se situe ni dans la maquette ni dans un formulaire. Une adresse demandée n'existe pas. Le serveur doit renvoyer le statut HTTP 404. La configuration technique peut préparer ce comportement, mais la preuve vient de la réponse réellement observée. Voilà pourquoi il serait artificiel de faire passer toutes les règles par les mêmes livrables. Le mécanisme dicte l'objet du contrôle. »

**Mémo oral :** `Le bon contrôle dépend du mécanisme.`

**Sources :** API Opquast, règle 222, version `qualite-numerique`.


## Slide 17 : Même page d'erreur, deux statuts différents

**Durée : 3 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Visualiser l'écart entre apparence et réponse technique.

**Écran, textes exacts à afficher :** « Même écran : page introuvable » ; « 200 ≠ 404 » ; « Lire le statut réseau »

**Scène et intention visuelle :** Deux fenêtres d'aspect identique ; panneau réseau avec `200 OK` barré à gauche et `404 Not Found` à droite.

**Préjudice utilisateur :** Le navigateur et les outils d'indexation peuvent être induits en erreur par une réponse 200 sur une ressource absente.

**Ce que vise la règle ou la démarche :** La règle 222 exige le statut 404 réellement renvoyé.

**Règle 222 (formulation officielle exacte) :**
> « Le serveur envoie un code HTTP 404 pour les ressources non trouvées. »

**Objectif officiel, résumé fidèle :** Permettre la détection des URL erronées et transmettre une information fiable aux clients et outils.

**Contrôle officiel, synthèse :** Pour chaque service examiné, essayer une URL inexistante et vérifier que la réponse HTTP porte le statut 404.

*(API Opquast, règle n° 222, version `qualite-numerique`.)*

### Discours oral

> « Voici deux pages visuellement identiques : toutes deux disent « Page introuvable ». Pourtant, l'une est servie avec un statut HTTP 200 et l'autre avec un 404. Le contrôle de la règle 222 distingue ces cas. On demande une adresse inexistante, puis on inspecte la réponse avec un outil de développement. Une maquette, un texte d'erreur et même une capture d'écran ne suffisent pas. »

**Mémo oral :** `Ne pas confondre l'écran et la réponse.`

**Interaction prévue :** Demander : quelle preuve manque si je montre seulement une capture d'écran ?

**Sources :** API Opquast, règle 222.


# V. Tracer, décider et maintenir


## Slide 18 : Une règle circule différemment selon son objet

**Durée : 2 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Comparer trois chaînes plutôt que dessiner un cycle projet universel.

**Écran, textes exacts à afficher :** « 234 : plan → gabarit/contenu → page » ; « Formulaires : maquette/code/parcours → contrôles distincts » ; « 222 : configuration → réponse HTTP »

**Scène et intention visuelle :** Trois lignes parallèles convergent vers « constat borné », sans présenter les maillons comme obligatoires pour chaque règle.

**Préjudice utilisateur :** Une équipe peut conclure trop tôt sur la base d'un mauvais support.

**Ce que vise la règle ou la démarche :** Le choix du support de contrôle permet de mieux documenter ce que l'on sait et ce qu'on ignore.

**Règles mobilisées (rappel officiel) :**

- **Règle 234 :** « Le contenu de chaque page est organisé selon une structure de titres et sous-titres hiérarchisée. »
- **Règle 77 :** « Chaque étiquette de formulaire est visuellement rattachée au champ qu’elle décrit. »
- **Règle 69 :** « Chaque champ de formulaire est associé dans le code source à une étiquette qui lui est propre. »
- **Règle 85 :** « La soumission d’un formulaire est suivie d’un message indiquant la réussite ou non de l’action souhaitée. »
- **Règle 222 :** « Le serveur envoie un code HTTP 404 pour les ressources non trouvées. »

### Discours oral

> « Les trois situations montrent trois circulations différentes. Pour la structure éditoriale, la contribution au CMS peut changer le résultat. Pour le formulaire, le visuel, le code et la soumission exigent trois examens distincts. Pour la ressource absente, la réponse HTTP est décisive. Nous ne pouvons donc pas plaquer un calendrier sur la checklist. En revanche, nous pouvons décrire pour chaque règle les livrables utiles, le contrôle officiel et les limites de ce contrôle. »

**Mémo oral :** `À chaque risque, son objet et sa preuve.`

**Sources :** API 234, 77, 69, 85 et 222 ; synthèse pédagogique.


## Slide 19 : Une trace utile ne cache pas ses limites

**Durée : 2 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Transformer une observation en information pour la décision.

**Écran, textes exacts à afficher :** « Objet + version + méthode + résultat + limites » ; « Testé ≠ conformité globale »

**Scène et intention visuelle :** Fiche de constat fictive, page « Préparer sa demande », date fictive, h2→h4, portée : une page.

**Préjudice utilisateur :** Un problème peut être minimisé ou amplifié si la portée du test n'est pas explicitée.

**Ce que vise la règle ou la démarche :** La traçabilité aide à arbitrer et à cibler les recontrôles.

### Discours oral

> « Écrire « testé » ne suffit pas. Nous devons savoir sur quel objet, quelle version, selon quelle méthode et avec quel résultat. Notre constat fictif concerne une seule page et son plan de titres. Il ne prouve ni l'état des autres pages ni l'absence de tous les risques. Cette trace est une proposition de gestion de projet. Le livre insiste sur le besoin de constats documentés et sur les limites des outils automatiques. »

**Mémo oral :** `Une preuve a toujours un périmètre.`

**Sources :** Livre, partie 2, sections 4.1 et 4.6 ; fiche projet proposée.


## Slide 20 : Constat, décision et recontrôle : trois responsabilités

**Durée : 2 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Attribuer l'arbitrage sans transformer la décision en verdict technique.

**Écran, textes exacts à afficher :** « Évaluateur : constate » ; « Responsable : arbitre » ; « Équipe : corrige » ; « Contrôle : recommence »

**Scène et intention visuelle :** Quatre rôles autour d'un ticket fictif ; case « recontrôle » vide tant que non effectué.

**Préjudice utilisateur :** Le défaut peut subsister si la correction n'est ni décidée ni vérifiée.

**Ce que vise la règle ou la démarche :** Une décision attribuée et un recontrôle borné contribuent à la maîtrise du risque.

### Discours oral

> « L'évaluateur documente un résultat. Le décideur choisit les suites, dans le cadre du projet et des obligations applicables. L'équipe intervient, puis le résultat doit être vérifié de nouveau. Décider de corriger ne transforme pas l'ancien contrôle en succès. Les attributions affichées sont un exemple d'organisation, pas une répartition officiellement imposée à tous les projets numériques. Une vérification sur un exemplaire n'exclut pas qu'un composant partagé ait affecté d'autres pages : le périmètre de reprise doit donc être explicité. »

**Mémo oral :** `Constater n'est pas décider ; corriger n'est pas recontrôler.`

**Sources :** Livre, partie 2, sections 4.1 et 6.4.


## Slide 21 : Critères d'acceptation, recette et Definition of Done

**Durée : 2 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Ne pas confondre le résultat attendu, son examen et le travail déclaré terminé.

**Écran, textes exacts à afficher :** « Critère : résultat attendu » ; « Recette : vérification » ; « DoD : conditions de fin de travail »

**Scène et intention visuelle :** Ticket fictif avec critères, contrôle non satisfait, DoD encore ouverte.

**Préjudice utilisateur :** L'utilisateur peut rencontrer un défaut sur une fonctionnalité considérée comme finie.

**Ce que vise la règle ou la démarche :** Ces outils de projet peuvent structurer les décisions sans remplacer le contrôle réel.

### Discours oral

> « Dans le livre, les critères d'acceptation précisent le résultat attendu. La recette examine un livrable par rapport à ces attentes. La Definition of Done établit les conditions décidées pour déclarer un travail terminé. Une équipe peut exiger le recontrôle avant clôture d'un ticket. Mais une DoD remplie n'est pas un audit général du service, et ces outils ne sont pas imposés comme méthode universelle par Opquast. »

**Mémo oral :** `Terminé n'est pas conforme partout.`

**Sources :** Livre, partie 1, chapitre 4, « Vocabulaire et culture agile » ; partie 2, section 4.1.


## Slide 22 : Les frontières de la démarche Opquast

**Durée : 1 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Dire explicitement ce que le référentiel et cet inventaire ne démontrent pas.

**Écran, textes exacts à afficher :** « Socle de prévention ≠ expertise spécialisée » ; « Inventaire ≠ méthode imposée »

**Scène et intention visuelle :** Un socle de qualité entouré d'autres expertises, puis un repère « contrôle ciblé ».

**Préjudice utilisateur :** Des risques spécialisés peuvent subsister, même si les exemples étudiés sont maîtrisés.

**Ce que vise la règle ou la démarche :** Le référentiel apporte des règles de prévention générales et un langage commun, pas une protection absolue.

### Discours oral

> « Opquast aide à prévenir des risques de base et à mieux travailler ensemble. Il ne décrit ni tous les risques possibles, ni une méthode projet universelle. Nos cinquante-neuf livrables forment une cartographie pédagogique, pas une liste d'obligations. Et notre choix de cinq règles ne remplace pas un audit spécialisé. Les résultats d'audit doivent toujours être rapportés aux pages et fonctionnalités examinées. Une liste de livrables n'est pas, en soi, une preuve de qualité. »

**Mémo oral :** `Un socle, pas une garantie totale.`

**Sources :** Livre, partie 2, section 2.2 ; inventaire proposé.


## Slide 23 : Exercice final : quelle preuve manque ?

**Durée : 2 min** (introduction orale d'environ 30 à 45 secondes, puis observation guidée, transition ou exercice).

**Idée :** Évaluer la compréhension en distinguant supports et preuves.

**Écran, textes exacts à afficher :** « 234 : où vérifier ? » ; « 77 / 69 / 85 : trois preuves ? » ; « 222 : quel statut ? »

**Scène et intention visuelle :** Trois cartes de cas à compléter ; dernière carte « après le constat : qui décide, qui recontrôle ? ».

**Préjudice utilisateur :** Une équipe peut laisser persister des risques si elle confond anticipation et contrôle.

**Ce que vise la règle ou la démarche :** Le candidat sait rattacher un risque utilisateur à une règle, un objet vérifiable et une trace bornée.

**Règles mobilisées (rappel officiel) :**

- **Règle 234 :** « Le contenu de chaque page est organisé selon une structure de titres et sous-titres hiérarchisée. »
- **Règle 77 :** « Chaque étiquette de formulaire est visuellement rattachée au champ qu’elle décrit. »
- **Règle 69 :** « Chaque champ de formulaire est associé dans le code source à une étiquette qui lui est propre. »
- **Règle 85 :** « La soumission d’un formulaire est suivie d’un message indiquant la réussite ou non de l’action souhaitée. »
- **Règle 222 :** « Le serveur envoie un code HTTP 404 pour les ressources non trouvées. »

### Discours oral

> « À vous de jouer : pour la structure des titres, quel est l'objet qui permet le contrôle ? Pour un formulaire, pourquoi la maquette, le code et la soumission apportent-ils des preuves différentes ? Pour une adresse inexistante, que faut-il lire ? Enfin, après un constat, qui décide et que faut-il recontrôler ? Si vous savez répondre sans réciter un calendrier, vous avez compris le fil conducteur : la qualité circule, la preuve se construit. »

**Mémo oral :** `La qualité circule, la preuve se construit.`

**Interaction prévue :** Réponses attendues : page rendue ; affichage/code/soumission ; statut HTTP 404 ; décision attribuée et recontrôle ciblé.

**Sources :** Exercice original sur API 234, 77, 69, 85, 222 et livre, partie 2, section 4.1.


# Atlas publié — slides 24 à 45

Le contrat suivant s’applique à chaque slide de l’atlas :

- rôle narratif : annexe de consultation ;
- idée nouvelle : les objets nommés et leur fonction, sans prescription ;
- situation, risque, examen possible, limite et provenance : intégralité des
  lignes A1 référencées, sans ajout ;
- principe : un objet prépare ou documente un examen borné ; il ne prouve que
  ce que la ligne source autorise ;
- composition : deux ou trois cartes de même statut, contenant le nom exact et
  la fonction exacte ; aucune flèche chronologique ;
- textes visibles : titre de famille, badge `ATLAS`, noms et fonctions exacts,
  header, footer et pagination ;
- transcription : disposition et textes visibles seulement ;
- discours oral : contexte, risque, examen possible, limite et provenance de
  chaque ligne source, puis mémo `Inventorier pour relier, pas pour imposer.` ;
- ambiguïtés exclues : famille officielle, phase obligatoire, conformité
  globale, audit complet ou livrable universel ;
- transition : famille suivante, sauf slide 45 qui conclut l’atlas ;
- acceptation : toutes les chaînes exactes, cartes lisibles, aucun objet omis ;
- rejet : attribut ajouté, objet fusionné, hiérarchie inventée ou caractère
  obligatoire suggéré.

| Slide | Famille et titre | Objets visibles avec fonction exacte | Source |
|---|---|---|---|
| 24 | Cadrage — clarifier avant de produire | Note d’opportunité — Clarifier utilité et objectifs ; Expression de besoins — Formuler les attentes ; Cartographie des parties prenantes — Identifier les contributions | Inventaire lignes 12 à 14 |
| 25 | Cadrage — expliciter risques et exigences | Analyse / registre des risques — Documenter les risques ; Cahier des charges — Formaliser les attentes ; Annexe de règles Opquast sélectionnées — Associer les règles au projet | Inventaire lignes 15 à 17 |
| 26 | Recherche utilisateur — préparer et observer | Plan de recherche — Préparer l’écoute des publics ; Entretiens et synthèses — Documenter des besoins observés ; Personas ou profils d’usage — Représenter des contextes | Inventaire lignes 18 à 20 |
| 27 | Recherche utilisateur — parcours et tests | Cartographie de parcours utilisateur — Visualiser les étapes vécues ; Rapport de test utilisateur — Restituer les observations | Inventaire lignes 21 à 22 |
| 28 | Spécifications — décrire et suivre | Spécifications fonctionnelles — Décrire comportements attendus ; Backlog produit — Suivre les demandes ; User Stories — Exprimer un besoin en contexte | Inventaire lignes 23 à 25 |
| 29 | Spécifications — vérifier et tracer | Critères d’acceptation — Définir résultat vérifiable ; Matrice exigences-règles-livrables — Tracer la circulation | Inventaire lignes 26 à 27 |
| 30 | Architecture de l’information — recenser et organiser | Inventaire de contenus — Recenser contenus et états ; Arborescence du site — Organiser les pages ; Plan de contenu / hiérarchie éditoriale — Organiser sections et sous-sections | Inventaire lignes 28 à 30 |
| 31 | Architecture de l’information — classer et orienter | Taxonomie et règles de classement — Classer les ressources ; Plan de site destiné aux personnes — Prévoir l’accès aux contenus | Inventaire lignes 31 à 32 |
| 32 | Conception fonctionnelle — structurer | Zoning — Positionner les grandes zones ; Wireframe — Schématiser zones et interactions ; Maquette fonctionnelle — Décrire fonctions et agencement | Inventaire lignes 33 à 35 |
| 33 | Conception fonctionnelle — simuler | Prototype — Simuler un parcours ; Diagramme de parcours et états — Documenter transitions et erreurs | Inventaire lignes 36 à 37 |
| 34 | Design graphique — rendre cohérent | Maquette graphique — Décrire le rendu visuel ; Charte graphique — Stabiliser identité visuelle ; Guide de style — Préciser usages visuels | Inventaire lignes 38 à 40 |
| 35 | Design graphique — mutualiser et adapter | Design system / bibliothèque de composants — Mutualiser composants et états ; Déclinaisons responsive — Prévoir différents affichages | Inventaire lignes 41 à 42 |
| 36 | Développement — produire et versionner | Gabarit HTML / template — Produire structure réutilisable ; Composants d’interface codés — Produire comportements réutilisables ; Code applicatif et dépôt versionné — Conserver l’implémentation | Inventaire lignes 43 à 45 |
| 37 | Développement — documenter et configurer | Documentation technique — Expliquer architecture et réglages ; Contrat d’API — Décrire échanges attendus ; Configuration serveur / hébergement — Définir réponses techniques | Inventaire lignes 46 à 48 |
| 38 | CMS et éditorial — préparer la publication | Installation test du CMS — Examiner la production initiale ; Modèles de saisie / consignes CMS — Guider la contribution ; Contenus rédactionnels publiés — Fournir l’information attendue | Inventaire lignes 49 à 51 |
| 39 | CMS et éditorial — rendre les contenus disponibles | Images et alternatives — Restituer l’information non textuelle ; Transcriptions audio/vidéo — Rendre l’information textuelle disponible ; Versions traduites — Fournir contenus en autres langues | Inventaire lignes 52 à 54 |
| 40 | Tests et recette — prévoir et exécuter | Stratégie et plan de tests — Définir périmètre et méthodes ; Scénarios de test / cahier de recette — Décrire opérations à exécuter ; Résultats de tests unitaires / intégration — Documenter contrôles techniques | Inventaire lignes 55 à 57 |
| 41 | Tests et recette — constater et décider | Rapport d’audit / fiche de constat — Consigner observations ; Registre d’anomalies — Suivre les défauts ; Procès-verbal de recette — Formaliser une décision de réception | Inventaire lignes 58 à 60 |
| 42 | Livraison — mettre en production | Version livrée / note de version — Identifier ce qui change ; Plan de déploiement et retour arrière — Organiser la mise en ligne ; Dossier de transfert / exploitation — Transmettre connaissances | Inventaire lignes 61 à 63 |
| 43 | Exploitation — suivre dans la durée | Journal des changements — Tracer les évolutions ; Procédures et tickets d’incident — Gérer les dysfonctionnements ; Plan de maintenance et recontrôles — Organiser la surveillance | Inventaire lignes 64 à 66 |
| 44 | Pilotage — attribuer et suivre | Matrice de responsabilités — Clarifier qui contribue et décide ; Tableau de bord qualité — Suivre constats et actions | Inventaire lignes 67 à 68 |
| 45 | Pilotage — améliorer et connaître le parc | Plan d’amélioration continue — Prioriser les corrections ; Inventaire de parc de services — Connaître les objets pilotés | Inventaire lignes 69 à 70 |

# Annexes

## A1. Répertoire de 59 livrables ou objets de projet

**Inventaire pédagogique élargi, exhaustif seulement pour les 59 entrées de cette version**, non exhaustif pour les projets numériques possibles et non prescriptif. Certains items sont des documents (cahier des charges), d'autres des objets de production (gabarit, CMS), des produits livrés (contenus) ou des traces (rapports).

**Codes de provenance :** `L3.2`, `L3.5`, etc. = notion étayée dans la section indiquée de la partie 2 du livre ; `L-agile` = livre, partie 1, chapitre 4 ; `L1.1` = partie 1, chapitre 1 ; `G` = glossaire Opquast ; `R234`, `R77`, `R69`, `R85`, `R222` = fiches API individuellement vérifiées ; `P` = **exemple de pratique projet proposé**, sans caractère officiel Opquast. Une référence au livre appuie une notion ou un usage, **pas l'obligation de produire le livrable nommé**.

La colonne « examen possible » décrit une revue limitée à l'objet concerné. Elle ne remplace pas le contrôle officiel d'une règle sur le produit final. Les préjudices de cette table sont des hypothèses pédagogiques plausibles pour un scénario, **pas des objectifs officiels attribués indistinctement à chaque livrable**.

| Famille | Livrable ou objet | Fonction | Contexte possible | Risque utilisateur abordé | Examen possible | Ce que cela ne prouve pas | Provenance |
|---|---|---|---|---|---|---|---|
| Cadrage | Note d’opportunité | Clarifier utilité et objectifs | Amont, révisions | Service inutile ou mal ciblé | Objectifs et publics explicités | Ne démontre pas l’utilité réelle | P |
| Cadrage | Expression de besoins | Formuler les attentes | Cadrage, évolutions | Besoins essentiels oubliés | Besoins et contraintes identifiables | Ne prouve pas leur satisfaction | P |
| Cadrage | Cartographie des parties prenantes | Identifier les contributions | Cadrage, pilotage | Responsabilité laissée sans acteur | Acteurs et décisions identifiés | Ne prouve pas la coordination effective | P |
| Cadrage | Analyse / registre des risques | Documenter les risques | Tout au long du projet | Risques utilisateur ignorés | Risques, actions et responsables documentés | Ne prouve pas la réduction du risque | P |
| Cadrage | Cahier des charges | Formaliser les attentes | Commande, cadrage | Exigences qualité absentes | Périmètre, exigences et exclusions explicités | Ne valide aucun résultat produit | L3.2 |
| Cadrage | Annexe de règles Opquast sélectionnées | Associer les règles au projet | Cadrage, consultation | Règles pertinentes omises | Applicabilité et sélection motivées | Sélection non exhaustive, pas un audit | L3.2 |
| Recherche utilisateur | Plan de recherche | Préparer l’écoute des publics | Découverte, itérations | Besoins mal compris | Questions et populations prévues | Ne garantit pas représentativité | P |
| Recherche utilisateur | Entretiens et synthèses | Documenter des besoins observés | Découverte, itérations | Parcours inadaptés | Méthode, verbatims, constats documentés | Ne couvre pas tous les risques | P |
| Recherche utilisateur | Personas ou profils d’usage | Représenter des contextes | Conception, révision | Usagers oubliés | Hypothèses et besoins tracés | Représentations non équivalentes aux usagers | P |
| Recherche utilisateur | Cartographie de parcours utilisateur | Visualiser les étapes vécues | Conception, amélioration | Rupture entre avant, pendant et après | Étapes, attentes et points de friction | Ne démontre pas le parcours réel | P; L1.1 |
| Recherche utilisateur | Rapport de test utilisateur | Restituer les observations | Conception, recette | Difficultés non détectées | Scénario, observations, limites | Échantillon et contexte bornés | P |
| Spécifications | Spécifications fonctionnelles | Décrire comportements attendus | Conception, itérations | Fonction incomprise ou incomplète | Scénarios et états attendus | Ne démontre pas le fonctionnement | L3.2 |
| Spécifications | Backlog produit | Suivre les demandes | Itérations | Exigence perdue entre équipes | Règles reliées aux items concernés | N’atteste pas le résultat | L-agile |
| Spécifications | User Stories | Exprimer un besoin en contexte | Itérations | Besoin utilisateur implicite | Besoin et résultat formulés | Ne garantit pas la qualité | L-agile |
| Spécifications | Critères d’acceptation | Définir résultat vérifiable | Spécification, recette | Livraison acceptée à tort | Critères précis et testables | Ne remplacent pas leur exécution | L-agile |
| Spécifications | Matrice exigences-règles-livrables | Tracer la circulation | Tout au long du projet | Exigence perdue au transfert | Correspondances et responsables documentés | Méthode pédagogique, non officielle | P |
| Architecture de l’information | Inventaire de contenus | Recenser contenus et états | Conception, migration | Contenu manquant ou obsolète | Périmètre et propriétaires identifiés | Ne prouve pas pertinence des contenus | P |
| Architecture de l’information | Arborescence du site | Organiser les pages | Conception, évolution | Difficulté à trouver une page | Hiérarchie et destinations prévues | Ne prouve pas navigation finale | G |
| Architecture de l’information | Plan de contenu / hiérarchie éditoriale | Organiser sections et sous-sections | Conception, édition | Plan de titres trompeur | Sections et sous-sections prévues | Ne prouve pas HTML rendu | P; R234 |
| Architecture de l’information | Taxonomie et règles de classement | Classer les ressources | Conception, contribution | Contenus difficiles à retrouver | Catégories cohérentes documentées | Ne prouve pas qualité de recherche | P |
| Architecture de l’information | Plan de site destiné aux personnes | Prévoir l’accès aux contenus | Conception, production | Navigation en impasse | Liens et rubriques prévus | Ne prouve pas exhaustivité réelle | G |
| Conception fonctionnelle | Zoning | Positionner les grandes zones | Conception | Information mal placée | Zones et fonctions repérées | Ni graphisme ni comportement vérifiés | G |
| Conception fonctionnelle | Wireframe | Schématiser zones et interactions | Conception | Hiérarchie peu claire | Structure prévue examinable | Pas de preuve HTML | G; L3.5 |
| Conception fonctionnelle | Maquette fonctionnelle | Décrire fonctions et agencement | Conception | Parcours incohérent | États et étapes visibles | Ne prouve pas interaction finale | G |
| Conception fonctionnelle | Prototype | Simuler un parcours | Conception, tests | Difficulté non anticipée | Enchaînement simulé observable | Fidélité variable au produit | L3.5 |
| Conception fonctionnelle | Diagramme de parcours et états | Documenter transitions et erreurs | Conception, développement | Action sans retour compréhensible | États succès/échec prévus | Ne prouve pas exécution | P; R85 |
| Design graphique | Maquette graphique | Décrire le rendu visuel | Conception, production | Rattachement visuel confus | Proximité des étiquettes anticipable | Ne prouve pas rendu responsive réel | G; L3.6; R77 |
| Design graphique | Charte graphique | Stabiliser identité visuelle | Conception, maintenance | Incohérences de présentation | Règles graphiques explicites | Ne démontre pas leur application | G |
| Design graphique | Guide de style | Préciser usages visuels | Conception, développement | Variantes incohérentes | Règles d’usage documentées | Ne prouve pas interface livrée | G |
| Design graphique | Design system / bibliothèque de composants | Mutualiser composants et états | Conception, développement, maintenance | Défauts répétés sur plusieurs pages | Variantes et états documentés | Chaque intégration reste à vérifier | P |
| Design graphique | Déclinaisons responsive | Prévoir différents affichages | Conception, réalisation | Étiquettes déplacées sur mobile | Configurations prévues | Ne prouve pas affichage réel toutes tailles | P; R77 |
| Développement | Gabarit HTML / template | Produire structure réutilisable | Développement, maintenance | Titres mal structurés | Éléments HTML générés inspectables | Contenu ajouté peut modifier la page | L3.7; R234 |
| Développement | Composants d’interface codés | Produire comportements réutilisables | Développement, maintenance | Champs mal associés | Association label/champ inspectable | Rendu et pertinence encore à contrôler | P; R69 |
| Développement | Code applicatif et dépôt versionné | Conserver l’implémentation | Développement, maintenance | Régression non suivie | Modifications et versions inspectables | Ne prouve pas le comportement réel | P |
| Développement | Documentation technique | Expliquer architecture et réglages | Développement, transfert | Correction difficile | Hypothèses et réglages explicités | Ne prouve pas réglages actifs | P |
| Développement | Contrat d’API | Décrire échanges attendus | Conception, intégration | Échec d’échange incompris | Entrées, sorties, erreurs documentées | Ne démontre pas le service en production | P |
| Développement | Configuration serveur / hébergement | Définir réponses techniques | Déploiement, exploitation | URL absente mal signalée | Configuration inspectable | Seule réponse réelle confirme le statut | P; R222 |
| CMS et éditorial | Installation test du CMS | Examiner la production initiale | Choix, déploiement | Défaut systémique du gabarit | Page de test générée examinable | Ne valide pas les futurs contenus | L3.8 |
| CMS et éditorial | Modèles de saisie / consignes CMS | Guider la contribution | Déploiement, exploitation | Titre ou média mal renseigné | Contraintes et consignes présentes | N’assurent pas la pertinence du contenu | P; L3.8 |
| CMS et éditorial | Contenus rédactionnels publiés | Fournir l’information attendue | Publication, maintenance | Information difficile à comprendre | Page réelle et structure examinables | Contrôle limité aux pages observées | L3.9; R234 |
| CMS et éditorial | Images et alternatives | Restituer l’information non textuelle | Production, publication | Information inaccessible sans image | Alternative et contexte examinables | Pertinence dépend de chaque image | L3.9 |
| CMS et éditorial | Transcriptions audio/vidéo | Rendre l’information textuelle disponible | Production, publication | Contenu inaccessible sans média | Présence et équivalence à examiner | Contrôle propre aux contenus concernés | L3.9 |
| CMS et éditorial | Versions traduites | Fournir contenus en autres langues | Production, maintenance | Version attendue difficile à atteindre | Correspondances et liens examinables | Qualité de traduction distincte | P |
| Tests et recette | Stratégie et plan de tests | Définir périmètre et méthodes | Préparation, recette | Défauts hors couverture | Périmètre et cas prévus | Plan ne prouve pas tests réalisés | P |
| Tests et recette | Scénarios de test / cahier de recette | Décrire opérations à exécuter | Recette, régression | Comportement non testé | Étapes et résultat attendu définis | Ne prouve pas exécution | P; G |
| Tests et recette | Résultats de tests unitaires / intégration | Documenter contrôles techniques | Développement, CI | Régression technique | Tests exécutés et résultats tracés | Couverture partielle, pas audit global | P |
| Tests et recette | Rapport d’audit / fiche de constat | Consigner observations | Recette, exploitation | Décision fondée sur impression | Objet, méthode, résultat, limites | Ne prouve que le périmètre observé | L4.1 |
| Tests et recette | Registre d’anomalies | Suivre les défauts | Recette, exploitation | Défaut oublié | État, impact, responsable, suite | Ticket clos n’est pas preuve de correction | P |
| Tests et recette | Procès-verbal de recette | Formaliser une décision de réception | Livraison | Acceptation ambiguë | Décision et réserves tracées | Ne vaut pas conformité globale | P |
| Livraison | Version livrée / note de version | Identifier ce qui change | Mise en production | Modification non identifiée | Version et périmètre documentés | Ne prouve pas absence de régression | P |
| Livraison | Plan de déploiement et retour arrière | Organiser la mise en ligne | Livraison | Interruption ou défaut persistant | Étapes et responsabilités prévues | Ne prouve pas déploiement réussi | P |
| Livraison | Dossier de transfert / exploitation | Transmettre connaissances | Passage en exploitation | Perte de maîtrise après livraison | Accès et procédures documentés | Ne garantit pas exécution future | P |
| Exploitation | Journal des changements | Tracer les évolutions | RUN | Ancien contrôle devenu caduc | Modifications et impacts repérables | N’indique pas à lui seul quels tests réussiront | P |
| Exploitation | Procédures et tickets d’incident | Gérer les dysfonctionnements | RUN | Utilisateur bloqué durablement | Signalement et traitement traçables | Ne prouve pas résolution effective | P |
| Exploitation | Plan de maintenance et recontrôles | Organiser la surveillance | RUN | Réapparition de défauts | Déclencheurs et périmètres définis | Planification ne vaut pas contrôle exécuté | P; L3.9 |
| Pilotage | Matrice de responsabilités | Clarifier qui contribue et décide | Tout au long du projet | Défaut sans décideur | Rôles et escalades explicites | N’impose pas une répartition universelle | P; L4.1 |
| Pilotage | Tableau de bord qualité | Suivre constats et actions | Projet, parc | Dégradation non repérée | Indicateurs, dates, périmètres visibles | Comparaison exige périmètres compatibles | P; L5.4 |
| Pilotage | Plan d’amélioration continue | Prioriser les corrections | Exploitation, parc | Défauts récurrents | Actions, décisions et échéances tracées | Ne prouve pas bénéfice final | P; L5.4 |
| Pilotage | Inventaire de parc de services | Connaître les objets pilotés | Exploitation, portefeuille | Services sans suivi | Périmètres et responsables identifiés | Inventaire n’est pas audit | L5.4 |

## A2. Matrice de circulation des cinq règles étudiées

| Règle | Préjudice ciblé dans l'exemple | Supports d'anticipation proposés | Objet du contrôle officiel | Trace projet possible | Ne prouve pas |
|---|---|---|---|---|---|
| 234 | Difficulté à se repérer dans les sections | Cahier des charges, plan éditorial, prototype, maquette, gabarit, consignes CMS | Titres de **chaque page rendue** et hiérarchie HTML | Page/version, plan constaté, écarts, contexte | Conformité d'autres pages |
| 77 | Confusion entre une étiquette et son champ | Wireframe, maquette responsive, guide de style | Proximité et position de l'étiquette sur **chaque formulaire rendu**, différentes tailles d'écran | Écran, taille, champ, anomalie | Association dans le code |
| 69 | Rôle du champ mal restitué ou incompris | Spécification, composant, formulaire codé | Association **dans le code** et pertinence de chaque étiquette | Champ, méthode d'inspection, libellé, résultat | Bonne proximité visuelle |
| 85 | Doute sur l'envoi du formulaire | Scénario, prototype, critères d'acceptation, page de résultat prévue | **Soumission complète** et confirmation explicite de réussite ou d'échec | Scénario, résultat affiché, date/version | Traitement ultérieur de la demande |
| 222 | Ressource absente mal signalée au navigateur et aux outils | Spécification technique, configuration serveur, déploiement | **Réponse HTTP 404** pour une URL inexistante | URL testée, statut HTTP, outil, date | Qualité d'une page d'erreur ou de tout le serveur |

**Attention :** les colonnes « supports » et « trace » représentent nos applications projet. Seule la colonne « objet du contrôle officiel » restitue synthétiquement les fiches de contrôle API.

## A3. Repères de certification : distinctions à ne pas confondre

| Confusion fréquente | Distinction à retenir | Appui |
|---|---|---|
| Phase du projet = propriétaire de la règle | Les métadonnées aident au classement ; les responsabilités dépendent du contexte de projet | Article du 14 avril 2026, livre |
| Prototype validé = page conforme | Le prototype montre une intention ; la page rendue permet des contrôles qui lui sont propres | Livre, sections 3.5 et 3.7 ; règle 234 |
| Règle 77 = règle 69 | 77 est **visuelle** ; 69 porte sur **l'association dans le code** et la pertinence de l'étiquette | API 77, API 69 |
| Formulaire compréhensible = envoi confirmé | La règle 85 examine le **résultat de la soumission** | API 85 |
| Message « 404 » à l'écran = vrai statut 404 | Le serveur doit répondre **HTTP 404**, même si un écran d'erreur est visible | API 222 |
| Rapport de test = conformité globale | Le résultat dépend des éléments examinés, des méthodes et de la couverture | Livre, section 4.1 |
| Correction annoncée = correction vérifiée | La décision précède l'examen du résultat modifié | Proposition projet, livre 4.1 |
| Definition of Done = audit | La DoD fixe des conditions de fin de travail convenues ; elle ne remplace pas l'évaluation du service | Livre, partie 1, chapitre 4 |
| 59 livrables = documents obligatoires | Il s'agit d'un inventaire analytique de documents, objets et traces possibles | Construction pédagogique |

## A4. Glossaire ciblé

**Wireframe :** schéma de zones, fonctionnalités et interactions, en faisant abstraction du design graphique. *(Glossaire Opquast, « Wireframe ».)*

**Maquette fonctionnelle :** représentation des zones et fonctionnalités, sans le style final. *(Glossaire Opquast, « Maquette fonctionnelle ».)*

**Maquette graphique :** représentation graphique de pages et de leur présentation. *(Glossaire Opquast, « Maquette graphique ».)*

**CMS :** système de gestion de contenu permettant de concevoir, produire et actualiser un service ou site. *(Glossaire Opquast, « CMS ».)*

**Page web :** résultat rendu par le navigateur à partir de HTML et d'autres ressources, éventuellement dynamiques. *(Glossaire Opquast, « Page web ».)*

**En-tête HTTP / statut HTTP :** information échangée entre client et serveur, utile notamment pour exprimer l'état d'une réponse. *(Glossaire Opquast, « En-tête HTTP », « Erreur 404 ».)*

**Critères d'acceptation / Definition of Done :** notions projet mobilisées dans le livre et distinguées en slide 21. Elles ne sont pas des règles Opquast autonomes.

## A5. Carte mentale de révision

```text
LA QUALITÉ CIRCULE, LA PREUVE SE CONSTRUIT
│
├── J'essaie de comprendre un contenu
│   └── 234 : plan prévu → gabarit + contenu → titres rendus
│
├── J'essaie d'envoyer une demande
│   ├── 77 : étiquette visuellement proche
│   ├── 69 : étiquette liée au champ dans le code
│   └── 85 : confirmation après soumission complète
│
├── Une ressource est absente
│   └── 222 : réponse HTTP avec statut 404
│
├── Les livrables et les métiers
│   ├── 12 familles
│   ├── 59 exemples nommés en A1
│   └── ni une chronologie ni des obligations universelles
│
└── Après l'observation
    ├── objet et périmètre
    ├── constat documenté
    ├── décision attribuée
    └── recontrôle après correction ou changement
```

## A6. Histoire, sources et limites de couverture

### Sources examinées pour cette consolidation

- **Livre :** Élie Sloïm et Laurent Denis, *Qualité et conformité des services numériques*, 4e édition, 2026. Partie 1, chapitre 1 (« Exigences utilisateurs : le modèle VPTCS »), chapitre 4 (méthodes et culture agile) ; partie 2, chapitre 3 (« Déploiement en projet numérique »), sections 3.2, 3.4 à 3.9 ; chapitre 4.1 (« Audit et inspection ») et chapitre 6.4 (« L'expert assurance qualité numérique »).
- **API Opquast :** règles **234, 77, 69, 85 et 222**, version `qualite-numerique`, fiches vérifiées individuellement et formulations exactes reprises dans le storyboard. Les numéros sont les numéros de règles, et non les identifiants internes de l'API.
- **Glossaire Opquast :** définitions mentionnées en annexe A4 et les termes mobilisés par les exemples.
- **Article :** « Au programme : livre, tags et numérique », 14 avril 2026, <https://www.opquast.com/au-programme-livre-tags-et-numerique/>. Il décrit une **évolution annoncée** de la famille des tags des phases projet vers fonctionnel, technique et contenus. L'annonce ne démontre pas un déploiement intégral à toutes les fiches.
- **Storyboards sources :** V006 (22 slides, 4 annexes), V007 (23 slides, 4 annexes) et versions intermédiaires V008.
- **Méta-prompt :** « Méta-prompt Opquast 360° V4 », appliqué avec les décisions de cadrage validées dans la conversation.

### Couverture effective

La tentative de récupération de la checklist Opquast étendue a échoué avec une réponse trop volumineuse. **Il n'est donc pas établi que les 245 règles ont été examinées.** Les cinq règles développées constituent un échantillon choisi pour illustrer des supports et modes de contrôle différents.

Le répertoire de 59 entrées est une synthèse pédagogique de notions du livre, du glossaire et de **pratiques de projet explicitement signalées comme exemples**. Il couvre douze familles utiles mais ne prétend pas couvrir tous les documents d'un projet complexe ou spécialisé.

L'historique est limité à l'évolution explicitement documentée par l'article cité. La lecture VPTCS du cas reste une **interprétation pédagogique** : contenus (plan et libellés), perception (proximité visible), technique (association et réponse HTTP), services (issue de la demande) ; visibilité apparaît seulement dans les objectifs d'indexation de certaines règles.

### Niveau de confiance

- **Établi explicitement :** formulation et contrôles des cinq règles API, concepts du livre et définitions du glossaire.
- **Fortement soutenu :** intérêt d'anticiper des défauts sur des livrables intermédiaires puis de vérifier les objets finaux, dans les limites des sections du livre.
- **Interprétation pédagogique :** les 59 entrées, leurs familles, les chaînes de circulation, les scènes fictives et l'attribution des rôles.

## A7. Préparation de la fabrication des slides

**Consignes :** visuels d'illustration seulement, pas de captures prétendument réelles ; afficher la mention « simulation » sur les écrans de contrôle fictifs ; privilégier une idée par slide ; rendre les citations officielles distinctes des traductions projet ; pas de verdict « conforme » fondé sur une maquette ou sur une page simulée.

**Contrôles avant publication :**

- Relire les textes à l'écran, dont la formulation exacte des règles affichées.
- Vérifier la lisibilité des 12 familles sur la slide 03 et répartir les 59
  libellés dans l’atlas plutôt qu’en microtexte.
- Respecter le minutage prévu pour **60 minutes**, répétition orale comprise.
- Vérifier les contrastes, la lisibilité, la structure et les alternatives des slides produites.
- Ne pas attribuer de caractère officiel aux responsabilités, flux et artefacts proposés.
- Vérifier le rendu final des slides, les éventuelles nouvelles versions de règles et les références si la production intervient après cette rédaction.
- Réaliser une revue humaine et, idéalement, un essai pédagogique avant `VALIDE_POUR_GENERATION`.

**Statut de la source V008 au terme de sa livraison :**
`CONSOLIDÉ_POUR_RELECTURE`. Le présent storyboard de production v001 ajoute
l’atlas et suit son propre statut enregistré en tête et dans `run.json`.
