Partie I - Accessibilité numérique et cadre légal
==================================================

## Statut du document

- Storyboard complet, relu en interne et en externe, puis corrigé. La génération est autorisée uniquement pour la planche de référence et les étalons 01, 09, 26 et 38.
- Source : slides PPTX 15 à 53 du support IGPDE 102846, générées par les modules Python indiqués pour chaque slide.
- Correspondance : 39 visuels web pour 39 slides PPTX, dans le même ordre.
- Numérotation publique : 1 à 39. Les numéros PPTX 15 à 53 restent uniquement dans la traçabilité.
- Titre public : « Partie I - Accessibilité numérique et cadre légal ».
- Titre du premier visuel, fidèle au PPTX : « Partie I - Accessibilité et cadre légal ».
- Slug : `partie-1-accessibilite-numerique-et-cadre-legal`.
- Étalons à produire seulement après validation du storyboard : slides web 01, 09, 26 et 38.

## Diagnostic pédagogique

- Public : communicantes et communicants, sans prérequis technique.
- Action attendue : comprendre ce qu’est l’accessibilité numérique, reconnaître la diversité des besoins, situer le cadre légal et identifier des premiers gestes concrets.
- Corpus : 39 slides structurées par cinq questions, de la définition à l’accessibilité dès la conception.
- Idées pivots : l’environnement peut créer ou lever une situation de handicap ; l’accessibilité est un droit et une obligation ; les premiers gestes relèvent déjà du travail quotidien des communicants.
- Charge cognitive : le PPTX associe définitions, six personas, tableaux de synthèse, repères juridiques, activités et méthode FALC. Les visuels condensent chaque message en scène ou système ; les accordéons conservent l’intégralité du contenu source.
- Niveau cognitif visé : comprendre, relier les besoins aux choix de communication, puis se préparer à agir.

## Contrat de série

- Référence visuelle opposable : preset local `IGPDE Accessibilité - bleu illustré` de l’usine, dans `_source/imagegen-igpde/`.
- Références inspectées : `reference-01-ouverture.png`, `reference-02-avant-apres.png`, `reference-03-tableau.png` et `reference-04-checklist.png`, en résolution originale.
- Format final : image 16:9, 1672 x 941 pixels.
- Masque commun : fond blanc lumineux, très grand titre bleu nuit aligné à gauche, scène ou objet-système central, cartes bleu clair aux contours fins, beaucoup d’espace libre, callout bas seulement s’il conclut sans ajouter une seconde idée.
- Progression : repère 1 à 39 dans l’interface web uniquement ; aucun numéro PPTX visible dans l’image.
- Familles de mise en page : utiliser exclusivement les six identifiants du preset local `ouverture_illustree`, `comparaison_transformation`, `processus_horizontal`, `tableau_pedagogique`, `checklist_processus` et `synthese_action`.
- Palette : bleu France `#000091`, bleu d’action `#2B6DE8`, bleu clair `#E3EEFF`, gris bleuté `#D7E1F0`, vert `#00A95F` réservé à la validation et rouge `#E1000F` réservé au problème.
- Typographie : Marianne, avec Arial comme seul fallback.
- Personnages : six personas entièrement régénérés dans le style IGPDE, distincts, crédibles et non caricaturaux. Les situations et technologies d’assistance restent concrètes. Une communicante récurrente peut apparaître dans les scènes hors personas.
- Effets : illustrations semi-plates, modelés et dégradés bleus très légers autorisés ; ombres absentes ou très légères.
- Interdits : faux logo, emblème officiel inventé, photographie, photoréalisme, 3D lourde, texture papier, tableau blanc dessiné, blob décoratif, ombre lourde, rouge décoratif, texte parasite, pseudo-lettres, paragraphe dense dans une carte ou contenu absent de la source.
- Fidélité : titre source inchangé dans chaque image. Le visuel garde le message principal et les libellés indispensables. La transcription reprend tout le contenu visible, hors masque récurrent. Le discours oral reprend intégralement les notes `add_notes()`.
- Éléments déterministes : QR codes, URL lisibles, couvertures et marques authentiques sont ajoutés après génération à partir des ressources sources ; ImageGen ne doit jamais les inventer.
- Traçabilité future : après validation des étalons seulement, créer `outputs/ia-slides/2026-10-02-partie-1-accessibilite-numerique-et-cadre-legal/` et y conserver storyboard, prompts, reçus et planche-contact. Ce dossier de travail ne sera pas versionné.

## Matrice des familles de mise en page

| Famille canonique | Usage dans la série | Variantes autorisées |
|---|---|---|
| `ouverture_illustree` | Ouverture générale ou entrée dans une nouvelle question | ouverture, chapitre |
| `comparaison_transformation` | Opposition entre états, voies, versions ou situations | avant-après, deux voies, plusieurs états, comparaison documentaire |
| `processus_horizontal` | Progression ordonnée, chronologie, parcours ou activité guidée | frise, étapes, flux, exercice |
| `tableau_pedagogique` | Données structurées, matrice ou catégories à comparer | tableau, matrice, colonnes structurées |
| `checklist_processus` | Ensemble de contrôles ou d'actions sans chronologie obligatoire | checklist, questions, outils |
| `synthese_action` | Scène centrale incarnée ou conclusion opérationnelle | définition illustrée, chiffre clé, persona, synthèse finale |

- Les slides 09 à 14 utilisent la famille `synthese_action`, variante `persona` : la variante décrit le contenu de la scène, sans créer une septième famille.
- La famille `processus_horizontal` suppose un ordre de lecture ou une relation directionnelle ; `checklist_processus` rassemble des contrôles indépendants.

## Planche de référence des personnages

- Statut : référence interne à produire avant les quatre étalons ; elle ne constitue pas une slide publique.
- Format : une planche 16:9 composée de sept vignettes de même importance, sur fond blanc, sans décor narratif. Chaque personnage est montré à mi-corps, de trois quarts, dans une posture professionnelle active.
- Fonction : stabiliser les visages, silhouettes, coiffures, tenues et équipements dans les slides individuelles, les scènes de groupe et les éventuels rappels ultérieurs.
- Style commun : illustration semi-plate IGPDE, anatomie naturelle, expressions sobres et attentives, gamme bleue cohérente, diversité crédible d'âges, de carnations et de morphologies.
- Identifiants : les noms peuvent figurer dans la planche interne, mais les attributs visuels doivent suffire à retrouver chaque personnage sans badge nominatif dans les visuels publics.

### Amir

- Homme d'environ 35 ans, peau brun foncé, cheveux noirs courts et bouclés, barbe courte, pull bleu nuit sur chemise claire.
- Équipements invariants : casque léger et plage braille fine placée devant le clavier.
- À préserver : regard naturel, posture autonome, gestes précis sur le clavier ou la plage braille.
- À proscrire : yeux fermés, lunettes noires, canne blanche ajoutée sans fonction dans la scène, lecteur d'écran représenté comme un scanner.

### Anaïs

- Femme d'environ 50 ans, peau mate claire, cheveux bruns légèrement grisonnants coupés au carré, lunettes rondes bleu nuit, veste bleu moyen sur haut clair.
- Équipements invariants : interface agrandie, contraste renforcé et synthèse vocale représentée discrètement.
- À préserver : distance d'écran crédible, posture autonome et lecture concentrée.
- À proscrire : la représenter comme aveugle, coller son visage à l'écran ou ajouter une aide technique non prévue.

### Justine

- Femme d'environ 30 ans, peau claire, cheveux noirs lisses attachés bas, chemise bleu clair et veste bleu nuit.
- Repères invariants : écran de montage ou de lecture vidéo avec sous-titres relus, transcription et alerte visuelle.
- À préserver : action professionnelle de production ou de contrôle d'un média.
- À proscrire : appareil auditif obligatoire, geste de langue des signes isolé ou surdité réduite à un symbole d'oreille.

### Agathe

- Femme d'environ 40 ans, peau brun moyen, cheveux noirs courts et naturels, haut clair et cardigan bleu soutenu.
- Équipements invariants : même fauteuil roulant électrique compact, contacteur sur support réglable, trackball et microphone de commande vocale.
- À préserver : posture active, mains positionnées de façon crédible et environnement de travail à bonne hauteur.
- À proscrire : posture passive, fauteuil disproportionné, contacteur confondu avec une plage braille ou accumulation d'aides sans usage visible.

### Anatole

- Lycéen d'environ 17 ans, peau claire, cheveux châtains courts, sweat bleu clair sous une surchemise bleu nuit.
- Repères invariants : cahier ou tablette avec consigne courte, pictogramme explicatif et blocs bien espacés.
- À préserver : allure adolescente crédible, expression attentive, autonomie dans la lecture.
- À proscrire : infantilisation, posture scolaire enfantine ou exagération des traits associés à la trisomie 21.

### Paul

- Homme d'environ 40 ans, peau claire, cheveux châtain roux courts, barbe légère, chemise bleu moyen aux manches retroussées.
- Repères invariants : revue de presse, commande de pause visible et texte aéré aligné à gauche.
- À préserver : activité professionnelle, espace de travail calme et regard concentré.
- À proscrire : lettres dansantes, désordre spectaculaire ou signe visuel caricatural du TDAH ou de la dyslexie.

### Communicante récurrente

- Femme d'environ 35 à 40 ans, peau mate claire, longs cheveux ondulés bleu-noir, haut bleu moyen, silhouette et coiffure proches de l'illustration d'ouverture appréciée dans la série réseaux sociaux.
- Fonction : accompagner les scènes hors personas, manipuler les supports et matérialiser les gestes professionnels sans devenir une septième situation de handicap.
- À préserver : même coiffure, même gamme de tenue, posture active et expressions sobres d'une slide à l'autre.
- À proscrire : lui attribuer une technologie d'assistance propre à un persona, modifier fortement son âge ou en faire un personnage décoratif sans action.

### Règles de continuité

- Conserver pour chaque personnage la même carnation, la même forme de visage, la même coiffure et la même tenue de base ; seules la pose et l'expression peuvent varier.
- Conserver la forme et la couleur des équipements d'une apparition à l'autre, notamment la plage braille d'Amir et le fauteuil, le contacteur et le trackball d'Agathe.
- Ne jamais ajouter un signe de handicap absent du profil pour rendre le personnage plus immédiatement identifiable.
- Réutiliser la planche comme référence d'image lors de chaque génération où l'un de ces personnages apparaît.
- Contrôler en pleine résolution les mains, les visages, le fauteuil, la plage braille, les contacteurs et les interactions avec les écrans avant d'accepter un visuel.

## Règles des deux accordéons

- Accordéon « Transcription » : titre de slide comme premier titre interne, surtitre pédagogique exact sous forme de paragraphe, puis contenu visible exact avec listes et tableaux HTML sémantiques.
- Accordéon « Lire le discours oral » : texte exact de `add_notes()`, structuré pour la lecture sans ajouter ni supprimer de consigne.
- Éléments exclus : logos du masque, pied de page récurrent, date et numéro de page.
- Liens : conserver le libellé visible exact et la destination source dans le HTML final.
- Tableaux : conserver les en-têtes et toutes les cellules ; utiliser `caption`, `thead`, `tbody`, `th` et les attributs `scope` appropriés.
- Slides 16 et 17 : reconstruire deux tableaux distincts par slide. Utiliser comme légende les paires d'en-têtes présentes dans la source : `Aveugle et Malvoyant`, `Sourd et Malentendant`, `Handicap moteur et Dyslexie / troubles dys`, puis `Handicap mental et TSA`.
- Slide 24 : restituer les treize thèmes comme une liste ordonnée de 1 à 13, dans l'ordre de lecture naturel, et non comme un tableau purement visuel à deux colonnes. Conserver le SPAN et les trois niveaux de conformité dans des sections séparées.
- Orthographe source : les formulations et graphies du PPTX sont conservées dans la transcription et le discours oral, y compris lorsqu’une correction éditoriale pourra être proposée séparément.

## Colonne vertébrale

1. Définir l’accessibilité numérique et ses quatre principes.
2. Relier six profils humains à des besoins concrets.
3. Situer les obligations françaises et européennes.
4. Comprendre pourquoi une communication accessible atteint mieux son objectif.
5. Passer à l’action avec les outils intégrés, le langage clair, le FALC et la conception accessible.

## Points de vigilance de fidélité

- La slide web 01 conserve le titre PPTX « Partie I - Accessibilité et cadre légal », différent du titre public enrichi.
- Les six personas sont régénérés sans reprendre les portraits sources, mais leurs profils, besoins et technologies d’assistance restent inchangés.
- Les tableaux très denses sont traduits visuellement ; leurs cellules exactes restent toutes présentes dans la transcription.
- Les notes et certains textes visibles comportent des graphies sans accents dans la source. Elles sont conservées dans les accordéons exacts et ne doivent pas contaminer les libellés synthétiques des nouveaux visuels.
- Les logos FALC, couvertures de documents et QR codes ne sont jamais recréés par ImageGen. Les ressources authentiques sont superposées de manière déterministe quand elles sont indispensables.
- Les contenus juridiques sont reproduits fidèlement au PPTX ; le storyboard ne constitue pas une actualisation juridique.

## Slide 01 - Partie I - Accessibilité et cadre légal - ÉTALON

- Correspondance : PPTX 15, `scripts/slides/02la_plan-partie-1.py`.
- Rôle : ouvrir la partie et annoncer ses cinq questions.
- Famille de mise en page : `ouverture_illustree` - variante ouverture.
- Idée principale : la partie conduit de la définition de l’accessibilité aux premiers gestes concrets.
- Scène : une communicante face à un grand écran où cinq portes ou cartes forment un parcours continu. Chaque carte porte un pictogramme distinct : définition, publics, droit, bénéfice, action.
- Transformation : question générale -> cinq angles complémentaires -> passage à l’action.
- Liste blanche du futur visuel : `Partie I - Accessibilité et cadre légal` ; `C’est quoi ?` ; `Pour qui ?` ; `Quel cadre légal ?` ; `Pourquoi ?` ; `Comment s’y mettre ?`.
- Ce que l’image seule doit faire comprendre : la partie suit cinq questions dans un ordre progressif.
- Continuité : ouvre la séquence et prépare la définition.
- Contraintes critiques : exactement cinq étapes ; conserver le titre PPTX sans ajouter « numérique » ; aucun numéro PPTX visible ; aucun faux logo.
- Alternative courte candidate : `Cinq questions structurent la partie sur l’accessibilité et le cadre légal.`

### Transcription exacte

#### Partie I - Accessibilité et cadre légal

*Partie I | Plan*

1. L'accessibilité numérique, c'est quoi ?
2. L'accessibilité numérique, c'est pour qui ?
3. L'accessibilité numérique, quel cadre légal ?
4. L'accessibilité numérique, pourquoi ?
5. L'accessibilité numérique, comment s'y mettre ?

### Discours oral exact

Annoncer les cinq questions qui structurent la partie I. Préciser que la progression va de la définition aux premiers gestes concrets.

## Slide 02 - 1. L'accessibilité numérique, c'est quoi ?

- Correspondance : PPTX 16, `scripts/slides/02m_chapitre-cadre-legal.py`.
- Rôle : ouvrir la première question.
- Famille de mise en page : `ouverture_illustree` - variante chapitre.
- Idée principale : commencer par une définition partagée avant d’aborder normes et outils.
- Scène : plusieurs personnes déposent des supports différents sur une table commune - page web, vidéo, document et formulaire - tandis qu’une bulle de question centrale les relie.
- Transformation : représentations spontanées -> définition commune.
- Liste blanche du futur visuel : `1. L'accessibilité numérique, c'est quoi ?`.
- Ce que l’image seule doit faire comprendre : l’accessibilité concerne plusieurs supports et commence par une question ouverte.
- Continuité : reprend la première étape du plan et prépare la définition précise.
- Contraintes critiques : aucun texte secondaire ; aucune définition anticipée ; conserver le point d’interrogation.
- Alternative courte candidate : `Une question ouvre la définition de l’accessibilité numérique.`

### Transcription exacte

#### 1. L'accessibilité numérique, c'est quoi ?

### Discours oral exact

Ouverture du module 1. Poser la question : si je vous dis accessibilité numérique, à quoi pensez-vous ? Laisser 30 secondes de silence avant de basculer vers la définition.

## Slide 03 - L'accessibilité numérique, c'est quoi ?

- Correspondance : PPTX 17, `scripts/slides/02ma_definition-a11y.py`.
- Rôle : poser la définition et élargir le périmètre.
- Famille de mise en page : `synthese_action` - variante définition illustrée.
- Idée principale : rendre l’information et les fonctionnalités accessibles quels que soient le matériel, le logiciel ou la situation.
- Scène : une information centrale circule vers quatre supports concrets, puis vers plusieurs personnes et contextes d’usage. Deux arcs visuels matérialisent « tous les contenus » et « utile pour tous ».
- Transformation : contenu unique -> plusieurs chemins d’accès -> usage possible.
- Liste blanche du futur visuel : `L'accessibilité numérique, c'est quoi ?` ; `Tous les contenus sont concernés` ; `Utile pour tous, indispensable pour certains` ; `Sites web, applications, newsletters, courriels` ; `Vidéos, podcasts, visuels animés` ; `Documents bureautiques, PDF, formulaires` ; `Affiches, flyers, plans, QR codes`.
- Ce que l’image seule doit faire comprendre : l’accessibilité ne se limite ni au Web ni à une seule situation de handicap.
- Continuité : répond à la question d’ouverture et prépare les référentiels.
- Contraintes critiques : ne pas réduire la scène au fauteuil roulant ; représenter plusieurs supports ; ne pas ajouter de définition étrangère au PPTX.
- Alternative courte candidate : `Une même information devient accessible sur plusieurs supports et dans plusieurs situations.`

### Transcription exacte

#### L'accessibilité numérique, c'est quoi ?

*1. Q1 - C'est quoi | Définition*

> Rendre possible l'accès à l'information et aux fonctionnalités numériques aux personnes en situation de handicap, quels que soient leur matériel, leur logiciel ou leur situation.

##### Tous les contenus sont concernés

- Sites web, applications, newsletters, courriels
- Vidéos, podcasts, visuels animés
- Documents bureautiques, PDF, formulaires
- Affiches, flyers, plans, QR codes

##### Utile pour tous, indispensable pour certains

- Handicap permanent, temporaire ou situationnel
- Matériel ancien, connexion lente, écran petit
- Environnement bruyant, lumineux ou contraint
- Langue étrangère, faible littératie numérique

### Discours oral exact

Poser la définition avant tout. Insister sur le fait que l'accessibilité ne concerne pas que le web ni que le handicap lourd. Faire reformuler par le groupe : quels supports produisez-vous au quotidien ?

## Slide 04 - Point sur l'accessibilité numérique

- Correspondance : PPTX 18, `scripts/slides/02mb_point-a11y-numerique.py`.
- Rôle : relier la communication accessible aux référentiels.
- Famille de mise en page : `processus_horizontal` - variante flux institutionnel.
- Idée principale : les WCAG donnent la référence internationale et le RGAA son application française.
- Scène : un contenu passe par un globe W3C stylisé, puis par un référentiel français représenté comme un classeur de contrôle, avant d’aboutir à 13 dossiers et 106 cartes.
- Transformation : besoin d’accès -> référence internationale -> méthode française structurée.
- Liste blanche du futur visuel : `Point sur l'accessibilité numérique` ; `WCAG` ; `RGAA` ; `106 critères` ; `13 thématiques`.
- Ce que l’image seule doit faire comprendre : les WCAG donnent la référence internationale ; le RGAA organise son application française en 106 critères et 13 thématiques.
- Continuité : formalise la définition et prépare les quatre principes WCAG.
- Contraintes critiques : ne pas inventer de logo W3C ou DINUM ; rattacher visuellement les nombres 106 et 13 au RGAA uniquement ; aucun jargon de développement.
- Alternative courte candidate : `Les WCAG servent de référence internationale ; le RGAA français comporte 106 critères regroupés en 13 thématiques.`

### Transcription exacte

#### Point sur l'accessibilité numérique

*1. Q1 - C'est quoi | WCAG et RGAA*

> L'accessibilité numérique permet d'accéder à l'information quel que soit le support, l'outil ou la situation.

- **WCAG**
- **RGAA**
- **106 / 13**

WCAG : référence internationale du W3C. RGAA : référentiel français publié par la DINUM. 106 critères regroupés en 13 thématiques.

### Discours oral exact

Cette slide fait la transition entre l'approche communication et le cadre de conformité. Ne pas détailler les 106 critères maintenant : expliquer que la formation donnera des clés utilisables, puis les points de contrôle rapides permettront de repérer les problèmes les plus fréquents.

## Slide 05 - 4 principes pour tout retenir

- Correspondance : PPTX 19, `scripts/slides/02mc_quatre-principes-wcag.py`.
- Rôle : donner une boussole mémorisable.
- Famille de mise en page : `checklist_processus` - variante quatre questions.
- Idée principale : quatre questions permettent d’interroger tout contenu.
- Scène : une communicante examine le même document sous quatre angles représentés par une oreille et un œil, un clavier, un chemin clair et une connexion avec une aide technique.
- Transformation : référentiel abstrait -> quatre questions concrètes.
- Liste blanche du futur visuel : `4 principes pour tout retenir` ; `Percevoir` ; `Utiliser` ; `Comprendre` ; `Compatible`.
- Ce que l’image seule doit faire comprendre : les quatre principes forment une boussole unique.
- Continuité : conclut la définition et prépare la question « pour qui ? ».
- Contraintes critiques : exactement quatre principes, dans cet ordre ; ne pas transformer « Compatible » en nom de technologie ; le sigle PUCC reste secondaire.
- Alternative courte candidate : `Quatre principes permettent d’interroger l’accessibilité d’un contenu.`

### Transcription exacte

#### 4 principes pour tout retenir

*1. Q1 - C'est quoi | 4 principes WCAG*

> Les WCAG reposent sur 4 principes. Chacun se résume en une question à poser devant tout contenu.

1. **Percevoir** - L'information reste-t-elle disponible si je ne vois pas ou n'entends pas ?
2. **Utiliser** - Puis-je naviguer et agir sans souris, sans geste imposé ?
3. **Comprendre** - Les mots, formulaires et comportements sont-ils prévisibles ?
4. **Compatible** - Les aides techniques peuvent-elles interpréter l'interface ?

### Discours oral exact

Mnémonique : PUCC (Percevoir, Utiliser, Comprendre, Compatible). Faire reformuler par le groupe : 'Si je suis aveugle, quel principe est en jeu ?' (Percevoir). 'Si je ne peux pas utiliser la souris ?' (Utiliser). Ces 4 principes structurent le RGAA et reviendront dans les modules suivants.

## Slide 06 - 2. L'accessibilité numérique, c'est pour qui ?

- Correspondance : PPTX 20, `scripts/slides/02n_chapitre-q2.py`.
- Rôle : ouvrir la deuxième question.
- Famille de mise en page : `ouverture_illustree` - variante chapitre.
- Idée principale : passer du cadre général aux personnes et besoins concrets.
- Scène : un groupe diversifié consulte le même contenu par plusieurs moyens - écran agrandi, sous-titres, clavier et lecture simplifiée.
- Transformation : contenu unique -> usages multiples.
- Liste blanche du futur visuel : `2. L'accessibilité numérique, c'est pour qui ?`.
- Ce que l’image seule doit faire comprendre : plusieurs personnes peuvent avoir besoin de chemins d’accès différents.
- Continuité : applique les quatre principes à des personnes réelles et prépare les quatre familles de besoins.
- Contraintes critiques : diversité crédible ; pas d’effet catalogue ; ne pas utiliser le fauteuil roulant comme symbole unique du handicap.
- Alternative courte candidate : `Plusieurs personnes accèdent au même contenu de façons différentes.`

### Transcription exacte

#### 2. L'accessibilité numérique, c'est pour qui ?

### Discours oral exact

Transition vers les publics concernés. Avant de montrer les 4 familles, demander au groupe : à votre avis, combien de personnes sont concernées par l'accessibilité numérique en France ?

## Slide 07 - C'est pour qui ? 4 familles de besoins

- Correspondance : PPTX 21, `scripts/slides/02na_quatre-deficiences.py`.
- Rôle : organiser la diversité des besoins sans enfermer les personnes.
- Famille de mise en page : `tableau_pedagogique` - variante quatre catégories.
- Idée principale : chaque famille de besoins appelle des réponses concrètes.
- Scène : un même contenu central se décline vers quatre cartes égales montrant un lecteur d’écran, des sous-titres, un clavier et une page simplifiée.
- Transformation : diversité des situations -> quatre familles -> gestes associés.
- Liste blanche du futur visuel : `C'est pour qui ? 4 familles de besoins` ; `Visuelle` ; `Auditive` ; `Motrice` ; `Cognitive`.
- Ce que l’image seule doit faire comprendre : les besoins sont différents mais peuvent être anticipés.
- Continuité : donne la carte d’ensemble et prépare une mise en situation.
- Contraintes critiques : quatre familles exactement ; pictogrammes non stéréotypés ; aucune hiérarchie de gravité.
- Alternative courte candidate : `Quatre familles de besoins appellent des solutions différentes.`

### Transcription exacte

#### C'est pour qui ? 4 familles de besoins

*1. Q2 - Pour qui | 4 familles*

> Chaque type de handicap implique des besoins concrets que vos contenus doivent prendre en compte.

##### Visuelle

- Lecteur d'écran, loupe, contraste
- Alt text, structure, couleurs

##### Auditive

- Sous-titres, transcription, LSF
- Alertes visuelles, pas que sonores

##### Motrice

- Clavier seul, contacteur, voix
- Cibles larges, pas de geste imposé

##### Cognitive

- Langage clair, mise en page aérée
- Navigation prévisible, pas de surcharge

### Discours oral exact

Ne pas détailler chaque handicap - l'objectif est de montrer la diversité des besoins. Faire le lien avec les gestes concrets vus dans les modules suivants : alt text (visuelle), sous-titres (auditive), clavier (motrice), langage clair (cognitive).

## Slide 08 - Comprendre pour mieux agir

- Correspondance : PPTX 22, `scripts/slides/02nab_comprendre-pour-agir.py`.
- Rôle : faire observer les barrières plutôt que simuler une identité.
- Famille de mise en page : `processus_horizontal` - variante activité guidée.
- Idée principale : observer ce que les choix numériques facilitent ou bloquent.
- Scène : une communicante navigue sur une page d’exercice ; cinq lentilles de simulation révèlent successivement des obstacles différents.
- Transformation : supposition sur le handicap -> observation d’une barrière -> capacité d’agir.
- Liste blanche du futur visuel : `Comprendre pour mieux agir` ; `Daltonisme` ; `Malvoyance` ; `Cécité` ; `Surdité` ; `Handicap moteur` ; `L'accessibilité numérique, et si nous agissions ?`.
- Ce que l’image seule doit faire comprendre : l’activité sert à observer l’effet de choix de conception.
- Continuité : concrétise les quatre familles et prépare les six personas.
- Contraintes critiques : ne pas présenter la simulation comme une expérience équivalente au vécu ; lien Atalan conservé dans le support HTML ; pas de faux écran lisible généré.
- Alternative courte candidate : `Cinq simulations aident à observer les barrières créées par les choix numériques.`

### Transcription exacte

#### Comprendre pour mieux agir

*1. Q2 - Pour qui | Comprendre*

> Il ne s’agit pas de se mettre à la place d’une personne handicapée, mais d’observer ce que nos choix numériques peuvent faciliter ou bloquer.

##### Testez les simulations suivantes

- Daltonisme
- Malvoyance
- Cécité
- Surdité
- Handicap moteur

[L'accessibilité numérique, et si nous agissions ?](https://atalan.fr/agissons/fr/index.html)

### Discours oral exact

Daltonisme : environ 8 % des hommes et 0,4 % des femmes. Laisser les stagiaires naviguer librement sur le site Atalan pendant 5 minutes. Chaque simulation illustre un type de handicap et montre ce que nos choix de mise en forme peuvent faciliter ou bloquer.

## Slide 09 - Amir, chargé d'études - cécité - ÉTALON

- Correspondance : PPTX 23, `scripts/slides/02nac_persona-amir.py`.
- Rôle : incarner les besoins liés à la cécité.
- Famille de mise en page : `synthese_action` - variante persona en situation de travail.
- Idée principale : la structure et les alternatives rendent le travail possible avec un lecteur d’écran.
- Scène : Amir, professionnel aveugle, travaille devant un ordinateur avec casque et plage braille. Un document structuré circule clairement vers ses outils ; une image sans alternative reste bloquée en retrait rouge discret.
- Transformation : contenu visuel non décrit -> structure et alternative -> information restituée.
- Liste blanche du futur visuel : `Amir, chargé d'études - cécité` ; `Percevoir + Compatible` ; `Lecteurs d'écran` ; `Plage braille` ; `Synthèse vocale`.
- Ce que l’image seule doit faire comprendre : plusieurs choix éditoriaux conditionnent l’accès d’Amir au contenu.
- Continuité : ouvre la série des personas et prépare le besoin d’agrandissement d’Anaïs.
- Contraintes critiques : ne pas montrer les yeux fermés ni une posture d’assistance ; plage braille crédible ; lecteur d’écran représenté par restitution vocale, pas comme un scanner ; personnage entièrement régénéré.
- Alternative courte candidate : `Amir utilise un lecteur d’écran et une plage braille pour consulter un document structuré.`

### Transcription exacte

#### Amir, chargé d'études - cécité

*1. Q2 - Pour qui | Amir*

##### Ses besoins au quotidien

- Alternative textuelle sur chaque image (attribut alt)
- Structure logique du document (titres, listes, tableaux)
- Liens explicites (pas de « cliquez ici »)
- Formulaires avec des étiquettes associées aux champs

**Percevoir + Compatible**

- Lecteurs d'écran
- Plage braille
- Synthèse vocale

### Discours oral exact

Amir est aveugle de naissance et utilise un lecteur d'écran (NVDA ou JAWS) pour tout son travail. Ce profil est central pour les communicants : chaque image sans alt, chaque tableau sans structure, chaque lien « cliquez ici » est un mur pour lui. Faire la demo du lecteur d'écran sur un document mal structure vs bien structure pour marquer les esprits.

## Slide 10 - Anaïs, gestionnaire RH - malvoyance

- Correspondance : PPTX 24, `scripts/slides/02nb_persona-anais.py`.
- Rôle : incarner les besoins liés à la malvoyance.
- Famille de mise en page : `synthese_action` - variante persona en situation de travail.
- Idée principale : taille, contraste et information non dépendante de la couleur améliorent l’accès visuel.
- Scène : Anaïs règle une interface RH. Trois commandes visibles montrent agrandissement, contraste renforcé et synthèse vocale ; un état important combine forme et couleur.
- Transformation : interface difficile à percevoir -> réglages et conception lisible -> lecture autonome.
- Liste blanche du futur visuel : `Anaïs, gestionnaire RH - malvoyance` ; `Percevoir` ; `Agrandissement` ; `Contraste renforcé` ; `Synthèse vocale` ; `Sans dépendre uniquement des couleurs`.
- Ce que l’image seule doit faire comprendre : l’interface doit rester lisible après adaptation.
- Continuité : complète la déficience visuelle et prépare l’équivalent textuel des contenus audio.
- Contraintes critiques : ne pas représenter Anaïs comme aveugle ; garder une distance d’écran crédible ; le ratio doit s’écrire `4,5:1` dans le nouveau visuel, tandis que la transcription conserve `4.5:1`.
- Alternative courte candidate : `Anaïs agrandit une interface dont les contrastes et repères restent lisibles.`

### Transcription exacte

#### Anaïs, gestionnaire RH - malvoyance

*1. Q2 - Pour qui | Anaïs*

##### Ses besoins au quotidien

- Agrandir la taille des textes et des interfaces
- Contraste suffisant entre texte et fond (ratio 4.5:1 minimum)
- Pouvoir naviguer sans dépendre uniquement des couleurs

**Percevoir**

- Agrandissement
- Contraste renforcé
- Synthèse vocale

### Discours oral exact

Anaïs a une DMLA précoce diagnostiquée il y a 10 ans. Ce profil illustre la déficience visuelle. Insister sur le fait que le contraste et la taille de texte sont des leviers que le communicant maîtrise directement dans ses documents.

## Slide 11 - Justine, chargée de communication - surdité

- Correspondance : PPTX 25, `scripts/slides/02nc_persona-justine.py`.
- Rôle : incarner les besoins liés à la surdité.
- Famille de mise en page : `synthese_action` - variante persona en situation de travail.
- Idée principale : toute information sonore doit disposer d’un équivalent visuel ou textuel.
- Scène : Justine prépare une vidéo institutionnelle. La piste audio se transforme en sous-titres relus, transcription et alerte visuelle.
- Transformation : son seul -> équivalents textuels et visuels -> information disponible.
- Liste blanche du futur visuel : `Justine, chargée de communication - surdité` ; `Percevoir` ; `Sous-titres relus` ; `Transcription` ; `Alertes visuelles`.
- Ce que l’image seule doit faire comprendre : une vidéo ou un podcast reste compréhensible sans entendre le son.
- Continuité : passe de l’adaptation visuelle à l’équivalent des contenus audio et prépare l’interaction sans souris.
- Contraintes critiques : ne pas réduire la surdité à un appareil auditif ; montrer une action professionnelle ; les sous-titres automatiques ne sont pas présentés comme suffisants.
- Alternative courte candidate : `Justine ajoute des sous-titres relus, une transcription et des alertes visuelles.`

### Transcription exacte

#### Justine, chargée de communication - surdité

*1. Q2 - Pour qui | Justine*

##### Ses besoins au quotidien

- Sous-titres sur toutes les vidéos et contenus audio
- Transcription textuelle des podcasts et webinaires
- Alertes visuelles, jamais uniquement sonores

**Percevoir**

- Sous-titres relus
- Transcription
- Alertes visuelles

### Discours oral exact

Justine est sourde de naissance. Ce profil illustre la déficience auditive. Le message clé pour les communicants : tout contenu audio doit avoir un équivalent textuel. Les sous-titres automatiques ne suffisent pas toujours, une relecture humaine est nécessaire.

## Slide 12 - Agathe, chargée de mission - déficience motrice

- Correspondance : PPTX 26, `scripts/slides/02nd_persona-agathe.py`.
- Rôle : incarner les besoins liés à la motricité.
- Famille de mise en page : `synthese_action` - variante persona en situation de travail.
- Idée principale : l’interface doit rester utilisable sans souris et avec des cibles suffisamment grandes.
- Scène : Agathe alterne entre clavier/contacteurs, souris trackball et commande vocale. Un focus visible avance entre de grandes cibles d’un formulaire.
- Transformation : petites cibles et souris imposée -> clavier, contacteurs et voix -> interaction réussie.
- Liste blanche du futur visuel : `Agathe, chargée de mission - déficience motrice` ; `Utiliser` ; `Clavier et contacteurs` ; `Souris trackball` ; `44 x 44 px minimum` ; `Commande vocale`.
- Ce que l’image seule doit faire comprendre : plusieurs modes d’interaction doivent permettre la même action.
- Continuité : complète les besoins sensoriels et prépare les besoins cognitifs.
- Contraintes critiques : fauteuil roulant éventuel sans posture passive ; contacteur crédible ; cibles réellement plus grandes ; ne pas confondre plage braille et contacteurs.
- Alternative courte candidate : `Agathe utilise un contacteur et la voix pour parcourir de grandes cibles visibles.`

### Transcription exacte

#### Agathe, chargée de mission - déficience motrice

*1. Q2 - Pour qui | Agathe*

##### Ses besoins au quotidien

- Naviguer sans souris, avec des contacteurs adaptés
- Cibles cliquables suffisamment larges (44 x 44 px minimum)
- Commande vocale pour piloter l'interface

**Utiliser**

- Clavier et contacteurs
- Souris trackball
- Commande vocale

### Discours oral exact

Agathe utilise un fauteuil roulant et des contacteurs adaptés. Ce profil illustre la déficience motrice. Pour les communicants : penser aux zones cliquables suffisamment grandes dans les PDF et formulaires, et à la navigation au clavier.

## Slide 13 - Anatole, lycéen - handicap cognitif

- Correspondance : PPTX 27, `scripts/slides/02nda_persona-anatole.py`.
- Rôle : incarner les besoins liés à la compréhension.
- Famille de mise en page : `synthese_action` - variante persona en situation de lecture.
- Idée principale : phrases courtes, mise en page aérée et repères prévisibles facilitent la compréhension.
- Scène : Anatole lit une consigne qui se simplifie visuellement : une idée par bloc, pictogramme explicatif et chemin de navigation stable.
- Transformation : texte dense -> information segmentée et illustrée -> consigne comprise.
- Liste blanche du futur visuel : `Anatole, lycéen - handicap cognitif` ; `Comprendre` ; `Phrases courtes` ; `Une idée par paragraphe` ; `Pictogrammes` ; `Navigation prévisible`.
- Ce que l’image seule doit faire comprendre : la présentation de l’information peut réduire l’effort de compréhension.
- Continuité : ouvre les besoins cognitifs et prépare la charge attentionnelle de Paul.
- Contraintes critiques : ne pas infantiliser Anatole ; ne pas symboliser la trisomie par des traits exagérés ; garder un contexte de lycéen crédible ; titre source conservé tel quel.
- Alternative courte candidate : `Anatole suit une consigne courte, illustrée et organisée de façon prévisible.`

### Transcription exacte

#### Anatole, lycéen - handicap cognitif

*1. Q2 - Pour qui | Anatole*

##### Ses besoins au quotidien

- Phrases courtes et simples, sans double négation
- Mise en page aérée, une idee par paragraphe
- Pictogrammes pour accompagner le texte
- Navigation prévisible, sans changements inattendus

**Comprendre**

##### Profil

- Porteur de trisomie 21
- Lire lui demande du temps et de la concentration
- Il comprend mieux les phrases simples et courtes
- Le langage clair et le FALC lui sont indispensables

### Discours oral exact

Anatole illustre la déficience cognitive. Pour les communicants : les règles du FALC et du langage clair ne profitent pas qu'aux personnes handicapees mentales - elles aident aussi les personnes agees, fatiguees, en situation de stress ou dont le français n'est pas la langue maternelle. Faire le lien avec les slides FALC.

## Slide 14 - Paul, attaché de presse - TDAH et dyslexie

- Correspondance : PPTX 28, `scripts/slides/02ndb_persona-paul.py`.
- Rôle : incarner les besoins liés à l’attention et à la lecture.
- Famille de mise en page : `synthese_action` - variante persona en situation de veille.
- Idée principale : maîtriser les mouvements et alléger la mise en page aide Paul à lire et se concentrer.
- Scène : Paul prépare une revue de presse. Un carrousel se met en pause, le texte se désencombre et l’alignement à gauche crée une ligne de lecture stable.
- Transformation : animation et texte compact -> pause et mise en page aérée -> lecture continue.
- Liste blanche du futur visuel : `Paul, attaché de presse - TDAH et dyslexie` ; `Comprendre + Percevoir` ; `Mettre en pause les animations` ; `Polices lisibles, sans empattement (sans serif)` ; `Mise en page aérée, paragraphes courts`.
- Ce que l’image seule doit faire comprendre : réduire les distractions et structurer le texte facilite la lecture.
- Continuité : clôt les six personas et prépare leur synthèse avec les principes WCAG.
- Contraintes critiques : ne pas montrer de lettres dansantes ni caricaturer la dyslexie ; le bouton pause doit être évident ; titre source conservé tel quel.
- Alternative courte candidate : `Paul met une animation en pause et lit un texte aéré aligné à gauche.`

### Transcription exacte

#### Paul, attaché de presse - TDAH et dyslexie

*1. Q2 - Pour qui | Paul*

##### Ses besoins au quotidien

- Mettre en pause les animations (carrousels, vidéo autoplay)
- Textes non justifies, avec un espacement suffisant
- Polices lisibles, sans empattement (sans serif)
- Mise en page aérée, paragraphes courts

**Comprendre + Percevoir**

##### Profil

- Consulte quotidiennement des sites d'info pour ses revues de presse
- Trouble de l'attention : les animations non contrôlables le déconcentrent
- Dyslexie : le texte justifié et les polices a empattement ralentissent sa lecture

### Discours oral exact

Paul illustre les troubles dys et le TDAH. Pour les communicants : ne jamais justifier le texte dans un document Word ou PDF, privilegier les polices sans serif (Marianne, Arial), éviter les carrousels en lecture automatique sans bouton pause, et garder des paragraphes courts. Ces règles beneficient a tous les lecteurs.

## Slide 15 - 6 profils, 4 questions - votre boussole WCAG

- Correspondance : PPTX 29, `scripts/slides/02ndc_matrice-personas-wcag.py`.
- Rôle : relier les personas aux quatre principes.
- Famille de mise en page : `tableau_pedagogique` - variante matrice.
- Idée principale : les quatre questions WCAG permettent de lire les besoins de profils très différents.
- Scène : les six personas entourent une boussole à quatre directions. De fins connecteurs relient chaque profil au ou aux principes concernés.
- Transformation : six situations distinctes -> quatre questions communes -> méthode réutilisable.
- Liste blanche du futur visuel : `6 profils, 4 questions - votre boussole WCAG` ; `Percevoir` ; `Utiliser` ; `Comprendre` ; `Compatible` ; `Amir` ; `Anaïs` ; `Justine` ; `Agathe` ; `Anatole` ; `Paul`.
- Ce que l’image seule doit faire comprendre : une même boussole aide à analyser des besoins différents.
- Continuité : synthétise les personas et prépare les fiches de solutions.
- Contraintes critiques : six profils et quatre principes exactement ; connecteurs non ambigus ; la transcription conserve chaque cellule du tableau source.
- Alternative courte candidate : `Six personas sont reliés aux quatre principes WCAG par une même boussole.`

### Transcription exacte

#### 6 profils, 4 questions - votre boussole WCAG

*1. Q2 - Pour qui | Synthèse*

| Persona | Percevoir | Utiliser | Comprendre | Compatible |
| --- | --- | --- | --- | --- |
| Amir (aveugle) | Alt text, structure |  |  | Lecteur d'écran |
| Anaïs (malvoyante) | Contrastes, taille |  |  |  |
| Justine (sourde) | Sous-titres, transcription |  |  |  |
| Agathe (motrice) |  | Clavier, cibles 44px |  |  |
| Anatole (cognitif) |  |  | FALC, phrases courtes |  |
| Paul (TDAH, dyslexie) | Polices lisibles |  | Pas de justification |  |

### Discours oral exact

Slide de synthèse qui fait le lien entre les personas et les 4 principes WCAG. Distribuer la fiche stagiaire (fiche-stagiaire-principes-wcag.pdf) à ce moment-là. Dire : « Vous n'avez pas besoin de retenir tout WCAG. Gardez les 4 questions sous la main. À chaque anomalie Word ou web, demandez-vous : est-ce un problème pour percevoir, utiliser, comprendre ou être lu par les outils ? »

## Slide 16 - Solutions par type de déficience (1/2)

- Correspondance : PPTX 30, `scripts/slides/02ndd_fiches-solutions-visuel-auditif.py`.
- Rôle : associer difficultés, solutions et technologies pour les besoins visuels et auditifs.
- Famille de mise en page : `tableau_pedagogique` - variante deux bandes.
- Idée principale : une difficulté sensorielle appelle un équivalent ou un renforcement adapté.
- Scène : deux canaux, visuel et audio, sont chacun déclinés en accès absent puis partiel. Une flèche conduit de la difficulté à la solution et à la technologie.
- Transformation : canal inaccessible -> équivalent ou renforcement -> technologie d’assistance.
- Liste blanche du futur visuel : `Solutions par type de déficience (1/2)` ; `Aveugle` ; `Malvoyant` ; `Sourd` ; `Malentendant` ; `Difficultés` ; `Solutions` ; `Technologies`.
- Ce que l’image seule doit faire comprendre : remplacer un canal absent et renforcer un canal partiellement disponible sont deux réponses différentes.
- Continuité : transforme les personas sensoriels en solutions et prépare les besoins moteurs et cognitifs.
- Contraintes critiques : ne pas mélanger solution et technologie ; conserver les quatre profils en deux paires ; pas de photo d’équipement.
- Alternative courte candidate : `Deux tableaux relient besoins visuels et auditifs à leurs solutions et technologies.`

### Transcription exacte

#### Solutions par type de déficience (1/2)

*1. Q2 - Pour qui | Fiches solutions*

> Chaque déficience appelle des solutions et des technologies d'assistance spécifiques.

|  | Aveugle | Malvoyant |
| --- | --- | --- |
| Difficultés | Inaccessibilité au visuel | Inaccessibilité partielle |
| Solutions | Remplacer par audio et tactile | Grossissement, contrastes, luminosité |
| Technologies | Plage braille, synthèse vocale | Loupe logicielle, synthèse vocale |

|  | Sourd | Malentendant |
| --- | --- | --- |
| Difficultés | Inaccessibilité à l'audio | Inaccessibilité partielle à l'audio |
| Solutions | Remplacer par le visuel (sous-titres, LSF) | Renforcement du signal auditif, visuel |
| Technologies | Sous-titrage, velotypie, LSF | Appareil auditif, boucle magnétique |

### Discours oral exact

Faire le lien avec les personas vus juste avant : Amir = aveugle, Anais = malvoyante, Justine = sourde. Ce tableau récapitule les solutions de manière structurée. La plage braille et la loupe logicielle sont des technologies d'assistance qu'on peut montrer en photo ou en vidéo courte si le temps le permet.

## Slide 17 - Solutions par type de déficience (2/2)

- Correspondance : PPTX 31, `scripts/slides/02nde_fiches-solutions-moteur-cognitif.py`.
- Rôle : associer difficultés, solutions et technologies pour les besoins moteurs et cognitifs.
- Famille de mise en page : `tableau_pedagogique` - variante deux bandes.
- Idée principale : simplifier l’interaction répond à des difficultés motrices comme cognitives, avec des moyens différents.
- Scène : une interaction physique et une lecture complexe suivent chacune un chemin distinct vers une interface plus simple. Deux cartes complémentaires montrent handicap mental et TSA.
- Transformation : manipulation ou compréhension difficile -> interaction simplifiée -> autonomie accrue.
- Liste blanche du futur visuel : `Solutions par type de déficience (2/2)` ; `Handicap moteur` ; `Dyslexie / troubles dys` ; `Handicap mental` ; `TSA` ; `Difficultés` ; `Solutions` ; `Technologies`.
- Ce que l’image seule doit faire comprendre : la simplification de l’interaction peut prendre plusieurs formes.
- Continuité : complète les fiches de solutions et prépare les chiffres sur l’ampleur du handicap.
- Contraintes critiques : ne pas suggérer une technologie spécifique quand la source dit qu’il n’en existe pas ; garder les quatre profils ; continuité graphique stricte avec la slide 16.
- Alternative courte candidate : `Deux tableaux relient besoins moteurs et cognitifs à leurs solutions.`

### Transcription exacte

#### Solutions par type de déficience (2/2)

*1. Q2 - Pour qui | Fiches solutions*

> Les déficiences motrices et cognitives impliquent des réponses différentes, mais un principe commun : simplifier l'interaction.

|  | Handicap moteur | Dyslexie / troubles dys |
| --- | --- | --- |
| Difficultés | Manipulation, préhension, pointage | Lecture, repérage, décodage |
| Solutions | Navigation clavier, zones cliquables larges | Polices simples, texte non justifié, mise en page aérée |
| Technologies | Trackball, clavier virtuel, commande oculaire | Synthèse vocale, règle de lecture |

|  | Handicap mental | TSA |
| --- | --- | --- |
| Difficultés | Compréhension, défilement, animation | Structuration, repérage |
| Solutions | Interfaces simples, FALC, pictogrammes | Consignes claires, structure documentaire |
| Technologies | Pas de technologie d'assistance spécifique | Pas de technologie d'assistance spécifique |

### Discours oral exact

Faire le lien avec Agathe (motrice), Paul (dyslexie/TDAH) et Anatole (cognitif). Pour le handicap mental et le TSA, insister sur le fait qu'il n'existe pas de technologie d'assistance spécifique : c'est le contenu et l'interface qui doivent s'adapter. Le FALC et le langage clair sont les réponses principales.

## Slide 18 - Handicap : sortir de l'angle mort

- Correspondance : PPTX 32, `scripts/slides/02ne_handicap-validisme.py`.
- Rôle : rendre visible l’ampleur et la diversité du handicap.
- Famille de mise en page : `synthese_action` - variante chiffres clés.
- Idée principale : l’accessibilité répond à des situations nombreuses, souvent invisibles ou acquises.
- Scène : une foule stylisée traverse un faisceau de lumière. Trois cartes associent chacune un nombre à son explication exacte, puis une loupe révèle des situations auparavant masquées.
- Transformation : public supposé valide -> réalités visibles -> accès équitable.
- Liste blanche du futur visuel : `Handicap : sortir de l'angle mort` ; `1/5` ; `1 personne sur 5 est en situation de handicap ou connaît un trouble invalidant.` ; `85%` ; `des handicaps sont acquis au cours de la vie` ; `1er` ; `Le handicap est le 1er facteur de discrimination selon le Défenseur des droits` ; `Validisme : le piège à déconstruire`.
- Ce que l’image seule doit faire comprendre : le handicap est fréquent, souvent acquis et encore discriminé.
- Continuité : donne l’ampleur du sujet et prépare le modèle social du handicap.
- Contraintes critiques : chiffres exacts ; chaque nombre reste indissociable de sa phrase explicative ; conserver `1/5` et non `1 sur 5` comme valeur affichée ; ne pas transformer les statistiques en décor ; le rouge sert seulement à signaler l’angle mort ou la discrimination.
- Alternative courte candidate : `Trois chiffres révèlent l’ampleur du handicap et le risque de validisme.`

### Transcription exacte

#### Handicap : sortir de l'angle mort

*1. Q2 - Pour qui | Chiffres*

> L'accessibilité n'est pas une faveur : c'est une condition d'accès équitable à l'information.

- **1/5** - 1 personne sur 5 est en situation de handicap ou connaît un trouble invalidant.
- **85%** - des handicaps sont acquis au cours de la vie
- **1er** - Le handicap est le 1er facteur de discrimination selon le Défenseur des droits

##### Validisme : le piège à déconstruire

- Penser le public comme valide par défaut
- Confondre bonne intention et accès réel
- Oublier les handicaps invisibles, acquis ou temporaires

### Discours oral exact

Les chiffres viennent du guide Accessibiliser sa communication. Ne pas transformer cette slide en cours théorique sur le validisme. Objectif : faire comprendre que l'accessibilité de la communication répond à des situations nombreuses, souvent invisibles, et qu'une bonne intention ne garantit pas l'accès effectif.

## Slide 19 - Déficience n'est pas situation de handicap

- Correspondance : PPTX 33, `scripts/slides/02nf_deficience-vs-situation.py`.
- Rôle : introduire le modèle social du handicap.
- Famille de mise en page : `comparaison_transformation` - variante trois états.
- Idée principale : c’est l’environnement inadapté qui crée la situation de handicap.
- Scène : la même personne en fauteuil apparaît devant un bureau adapté, seule sur un sol plat, puis face à un escalier. L’environnement change, pas la personne. Sous les trois états, un bandeau `Ce que ça change pour vous` relie la démonstration aux trois conséquences pratiques du PPTX.
- Transformation : personne identique -> environnement adapté ou barrière -> situation différente.
- Liste blanche du futur visuel : `Déficience n'est pas situation de handicap` ; `environnement inadapté` ; `Déficience` ; `barrière` ; `Ce que ça change pour vous` ; `C'est l'environnement qui crée le handicap, pas la personne` ; `Un document inaccessible = une barrière que vous pouvez lever` ; `Mettre en accessibilité votre communication supprime la situation de handicap`.
- Ce que l’image seule doit faire comprendre : une barrière environnementale transforme une déficience en situation de handicap.
- Continuité : donne le modèle explicatif et prépare les temporalités du handicap.
- Contraintes critiques : même personnage et même fauteuil dans les trois états ; ne pas utiliser la tristesse comme raccourci ; montrer clairement le rôle du bureau et de l’escalier ; placer sous la comparaison un seul bandeau de conclusion contenant les trois formulations exactes, sans les répartir dans les états.
- Alternative courte candidate : `La même personne rencontre ou non une situation de handicap selon l’environnement.`

### Transcription exacte

#### Déficience n'est pas situation de handicap

*1. Q2 - Pour qui | Déficience vs situation*

> Le handicap n'est pas un état fixe : c'est la rencontre entre une déficience et un environnement inadapté.

Texte dans l’illustration : « Déficience ≠ situation de handicap » ; « situation » ; « Etat » ; « situation ».

##### Ce que ça change pour vous

- C'est l'environnement qui crée le handicap, pas la personne
- Un document inaccessible = une barrière que vous pouvez lever
- Mettre en accessibilité votre communication supprime la situation de handicap

### Discours oral exact

Le schéma illustre le modèle social du handicap, opposé au modèle médical. La personne en fauteuil n'est pas en situation de handicap devant un bureau adapté, mais le devient face à un escalier. Transposer au numérique : un PDF non structuré = un escalier pour un lecteur d'écran.

## Slide 20 - Le spectre du handicap

- Correspondance : PPTX 34, `scripts/slides/02ng_tableau-temporalite.py`.
- Rôle : montrer que le handicap varie dans le temps et selon la situation.
- Famille de mise en page : `comparaison_transformation` - variante quatre situations.
- Idée principale : permanent, temporaire, situationnel et vieillissement peuvent produire des besoins comparables.
- Scène : quatre colonnes montrent la même action de manipulation dans des contextes différents : une personne n’utilise qu’une main, une autre a le bras cassé, une autre porte un bébé et une personne âgée ressent des douleurs.
- Transformation : même action -> quatre temporalités différentes -> besoin commun d’une interaction plus simple.
- Liste blanche du futur visuel : `Le spectre du handicap` ; `Manipulation` ; `Permanent` ; `Une seule main` ; `Temporaire` ; `Bras cassé` ; `Situationnel` ; `Un bébé dans les bras` ; `Vieillissement` ; `Douleurs`.
- Ce que l’image seule doit faire comprendre : une même barrière peut concerner durablement ou momentanément des personnes différentes.
- Continuité : clôt la question « pour qui ? » et prépare le passage au cadre légal.
- Contraintes critiques : quatre colonnes et un exemple illustré par colonne ; conserver exactement l’ordre permanent, temporaire, situationnel, vieillissement ; ne pas reproduire la matrice complète dans l’image ; conserver les seize cellules dans l’accordéon sémantique ; aucun personnage stigmatisant.
- Alternative courte candidate : `Une même action de manipulation est comparée dans quatre situations : une seule main, bras cassé, bébé porté et douleurs.`

### Transcription exacte

#### Le spectre du handicap

*1. Q2 - Pour qui | Spectre du handicap*

> Le handicap n'est pas binaire. Il peut être permanent, temporaire, situationnel ou lié au vieillissement.

| Handicap | Permanent | Temporaire | Situationnel | Vieillissement |
| --- | --- | --- | --- | --- |
| Manipulation | Une seule main | Bras cassé | Un bébé dans les bras | Douleurs |
| Vision | Visibilité faible | Oeil gonflé | Lumière tamisée | Vue qui baisse |
| Cognition | Amnésie | Fatigue | Première utilisation | Alzheimer |
| Mobilité | Fauteuil roulant | Jambe cassée | Chaussures inconfortables | Canne |

### Discours oral exact

Laisser les stagiaires découvrir le tableau. Demander : dans quelle colonne vous êtes-vous déjà retrouvés ? Tout le monde a déjà été en situation de handicap temporaire ou situationnel. C'est là que le déclic se produit : l'accessibilité concerne tout le monde.

## Slide 21 - 3. L'accessibilité numérique, quel cadre légal ?

- Correspondance : PPTX 35, `scripts/slides/02o_chapitre-q3.py`.
- Rôle : ouvrir la troisième question.
- Famille de mise en page : `ouverture_illustree` - variante chapitre.
- Idée principale : l’accessibilité est aussi une obligation organisée et contrôlée.
- Scène : une communicante pose un document numérique sur une balance. De l’autre côté, une chronologie, un référentiel et un contrôle public rendent le cadre concret.
- Transformation : bonne pratique perçue -> obligation structurée.
- Liste blanche du futur visuel : `3. L'accessibilité numérique, quel cadre légal ?`.
- Ce que l’image seule doit faire comprendre : le droit encadre l’accessibilité numérique.
- Continuité : s’appuie sur les besoins humains et prépare la chronologie juridique.
- Contraintes critiques : ne pas utiliser marteau de juge, palais de justice ou drapeau décoratif ; rester centré sur les contenus numériques.
- Alternative courte candidate : `Une chronologie et un référentiel matérialisent le cadre légal de l’accessibilité.`

### Transcription exacte

#### 3. L'accessibilité numérique, quel cadre légal ?

### Discours oral exact

Transition vers le cadre juridique. Rappeler que l'accessibilité n'est pas seulement une bonne pratique, c'est une obligation légale avec des sanctions.

## Slide 22 - Le cadre légal : de 2005 à aujourd'hui

- Correspondance : PPTX 36, `scripts/slides/02oa_cadre-legal-rgaa.py`.
- Rôle : montrer la progression du droit en quatre jalons.
- Famille de mise en page : `processus_horizontal` - variante frise chronologique.
- Idée principale : l’obligation s’est précisée, étendue et dotée de contrôles.
- Scène : quatre bornes datées jalonnent une route de 2005 à 2023. Une structure publique suit la route jusqu’au contrôle exercé par l’Arcom.
- Transformation : principe légal -> extension européenne -> référentiel opposable -> contrôle.
- Liste blanche du futur visuel : `Le cadre légal : de 2005 à aujourd'hui` ; `2005` ; `2016` ; `RGAA 4.1.2` ; `2023` ; `Arcom` ; `50 000 EUR` ; `25 000 EUR`.
- Ce que l’image seule doit faire comprendre : le droit s’est renforcé par étapes.
- Continuité : pose les jalons puis prépare les deux directives européennes.
- Contraintes critiques : quatre étapes dans l’ordre ; l’Arcom est l’autorité de contrôle depuis 2023 ; distinguer les plafonds de 50 000 EUR pour l’obligation d’accessibilité et de 25 000 EUR pour les obligations déclaratives ; ne pas écrire `par service non conforme` ; ne pas présenter la sanction comme automatique.
- Alternative courte candidate : `Quatre jalons montrent le renforcement du cadre légal depuis 2005.`

### Transcription exacte

#### Le cadre légal : de 2005 à aujourd'hui

*1. Q3 - Cadre légal | Jalons législatifs*

1. Loi Handicap 2005 : 1re obligation d'accessibilité
2. Directive européenne 2016 : extension au secteur public
3. RGAA 4.1.2 (décret 2019-768) : référentiel opposable
4. 2023 : l'Arcom devient l'autorité de contrôle

##### Qui est concerné ?

- État, collectivités, établissements publics
- Entreprises privées gérant un service public ou CA > 250 M EUR
- Jusqu'à 50 000 EUR : accessibilité des organismes publics et assimilés
- Jusqu'à 25 000 EUR : obligations déclaratives

### Discours oral exact

Chronologie en 4 étapes : montrer la progression du droit. Le RGAA 4.1.2 = 106 critères regroupés en 13 thèmes. Depuis 2023, l'Arcom est l'autorité de contrôle de l'article 47. La DINUM édite le RGAA et accompagne les administrations. La sanction peut atteindre 50 000 EUR pour le non-respect de l'obligation d'accessibilité par les organismes publics et assimilés, et 25 000 EUR pour le non-respect des obligations déclaratives.

## Slide 23 - Le cadre européen

- Correspondance : PPTX 37, `scripts/slides/02ob_cadre-europeen.py`.
- Rôle : distinguer les deux directives européennes.
- Famille de mise en page : `comparaison_transformation` - variante deux voies.
- Idée principale : une directive encadre le secteur public et l’autre étend l’obligation au secteur privé.
- Scène : deux voies parallèles partent d’un même cadre européen. La première aboutit à des services publics et au RGAA ; la seconde à des services privés depuis juin 2025.
- Transformation : cadre européen commun -> deux périmètres -> obligations complémentaires.
- Liste blanche du futur visuel : `Le cadre européen` ; `Directive 2016/2102` ; `Secteur public` ; `Directive 2019/882` ; `Secteur privé` ; `28 juin 2025`.
- Ce que l’image seule doit faire comprendre : les obligations couvrent désormais des acteurs publics et privés.
- Continuité : précise l’échelon européen et prépare les thèmes du RGAA.
- Contraintes critiques : ne pas inverser les deux directives ; ne pas représenter l’Union européenne avec un faux emblème ; juin 2025 appartient à la directive 2019/882.
- Alternative courte candidate : `Deux directives européennes couvrent le secteur public et une partie du secteur privé.`

### Transcription exacte

#### Le cadre européen

*1. Q3 - Cadre légal | Directives européennes*

> Deux directives européennes structurent l'obligation d'accessibilité numérique en France.

##### Directive 2016/2102 - secteur public

- Sites web et applications mobiles du secteur public
- Transposée en droit français par le décret 2019-768
- Obligation de déclaration d'accessibilité
- Base du RGAA actuel

##### Directive 2019/882 - secteur privé

- Acte européen d'accessibilité (EAA)
- Applicable à partir du 28 juin 2025
- Commerce en ligne, banque, transport, télécom
- Élargit l'obligation au-delà du secteur public

### Discours oral exact

La directive 2016/2102 est déjà transposée et applicable. L'EAA (2019/882) étend l'obligation au secteur privé depuis juin 2025. Pointer que le mouvement est européen, pas seulement français : les obligations vont continuer à se renforcer.

## Slide 24 - RGAA : 13 thèmes, 3 niveaux de conformité

- Correspondance : PPTX 38, `scripts/slides/02oc_rgaa-13-themes.py`.
- Rôle : donner la carte du référentiel et ses niveaux.
- Famille de mise en page : `tableau_pedagogique` - variante tableau et synthèse.
- Idée principale : le RGAA organise l’audit en 13 thèmes et trois niveaux de conformité.
- Scène : un classeur de contrôle ouvre treize onglets ; sous lui, un calendrier SPAN sur trois ans et une jauge à trois niveaux structurent la démarche.
- Transformation : référentiel perçu comme massif -> treize thèmes organisés -> pilotage dans le temps.
- Liste blanche du futur visuel : `RGAA : 13 thèmes, 3 niveaux de conformité` ; `13 thèmes` ; `SPAN` ; `Schéma pluriannuel d'accessibilité sur 3 ans` ; `Non conforme` ; `Partiellement conforme` ; `Totalement conforme`.
- Ce que l’image seule doit faire comprendre : le référentiel combine contenu audité, stratégie et résultat de conformité.
- Continuité : traduit les directives en méthode française et prépare le détail du RGAA.
- Contraintes critiques : treize thèmes exacts dans la transcription ; trois niveaux dans le bon ordre ; ne pas présenter le SPAN comme un niveau de conformité.
- Alternative courte candidate : `Le RGAA combine treize thèmes, un schéma sur trois ans et trois niveaux de conformité.`

### Transcription exacte

#### RGAA : 13 thèmes, 3 niveaux de conformité

*1. Q3 - Cadre légal | 13 thèmes RGAA*

| Les 13 thèmes du RGAA |  |
| --- | --- |
| 1. Images | 8. Éléments obligatoires |
| 2. Cadres | 9. Structuration |
| 3. Couleurs | 10. Présentation |
| 4. Multimédia | 11. Formulaires |
| 5. Tableaux | 12. Navigation |
| 6. Liens | 13. Consultation |
| 7. Scripts |  |

##### SPAN

Schéma pluriannuel d'accessibilité sur 3 ans

##### Trois niveaux de conformité

- Non conforme : moins de 50 % des critères
- Partiellement conforme : de 50 % à 99 %
- Totalement conforme : 100 % des critères applicables

### Discours oral exact

Ne pas détailler chaque thème : les participants les retrouveront dans les modules suivants. Insister sur le SPAN : c'est le document stratégique que chaque organisme public doit publier. Environ 25 % des tests RGAA sont automatisables, le reste nécessite un audit humain.

## Slide 25 - Le RGAA - Référentiel Général d'Amélioration de l'Accessibilité

- Correspondance : PPTX 39, `scripts/slides/02oca_rgaa-detail.py`.
- Rôle : montrer la structure et l’ampleur du référentiel.
- Famille de mise en page : `tableau_pedagogique` - variante trois colonnes.
- Idée principale : le RGAA articule obligations légales, méthode technique, thèmes, critères et tests.
- Scène : un poste de contrôle ouvre trois panneaux : structure du référentiel, thèmes orientés contenus, thèmes orientés usage. Des compteurs 13, 106 et 258 restent attachés au premier panneau.
- Transformation : sigle abstrait -> structure lisible -> exemples de critères concrets.
- Liste blanche du futur visuel : `Le RGAA - Référentiel Général d'Amélioration de l'Accessibilité` ; `2 parties` ; `13 thématiques` ; `106 critères` ; `258 tests` ; `Images` ; `Éléments obligatoires`.
- Ce que l’image seule doit faire comprendre : le RGAA transforme l’obligation en méthode détaillée.
- Continuité : approfondit la carte générale et prépare l’activité sur les obligations propres à chaque structure.
- Contraintes critiques : trois nombres exacts et non interchangeables ; aucune promesse d’automatisation complète ; titre long sur deux lignes maximum.
- Alternative courte candidate : `Le RGAA relie deux parties, treize thèmes, 106 critères et 258 tests.`

### Transcription exacte

#### Le RGAA - Référentiel Général d'Amélioration de l'Accessibilité

*1. Q3 - Cadre légal | RGAA détail*

##### Structure en 2 parties

- Obligations légales
- Méthode technique
- 13 thématiques
- 106 critères au total
- 258 tests unitaires

##### Images

- Cadres
- Couleurs
- Multimédia
- Tableaux
- Liens
- Scripts

##### Éléments obligatoires

- Structuration
- Navigation
- Présentation
- Formulaires
- Consultation

### Discours oral exact

Trois taux de conformité :

- Non conforme : site non audité ou niveau inférieur à 50 %
- Partiellement conforme : de 50 % a 99 %
- Totalement conforme : 100 % des critères validés

Exemptions :

- Fichiers bureautiques publiés avant le 23 septembre 2018
- Contenus intranets/extranets publiés avant le 23 septembre 2019
- Contenus audios/vidéos publiés avant le 23 septembre 2020
- Contenus vidéos, tiers, cartes peuvent aussi être exemptés

Exemples de critères :

1. Les images porteuses d'informations doivent avoir un texte alternatif. Les images décoratives ne doivent pas en avoir.
2. Les médias avec du son doivent avoir une alternative (sous-titrage, LSF) et les vidéos une audiodescription.
3. Plusieurs systèmes de navigation doivent être disponibles (menu, plan du site, recherche). Les éléments-clés sont toujours au même endroit.

Ref : https://accessibilite.numerique.gouv.fr/

Critères : https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/

## Slide 26 - Quelles obligations pour votre structure ? - ÉTALON

- Correspondance : PPTX 40, `scripts/slides/02od_obligally-simulateur.py`.
- Rôle : faire appliquer le cadre juridique à sa propre structure.
- Famille de mise en page : `processus_horizontal` - variante activité guidée.
- Idée principale : un simulateur permet d’identifier les normes applicables à sa situation.
- Scène : une communicante répond à un court arbre de décision sur un écran. Le résultat prend la forme d’une fiche « obligations », reliée à un QR code réel et à l’URL principale visible.
- Transformation : cadre général -> réponses à des questions -> obligations propres à la structure.
- Liste blanche du futur visuel : `Quelles obligations pour votre structure ?` ; `Activité - simulateur Obligally (10 min)` ; `Scannez-moi !` ; `https://obligations-legales-accessibilite-numerique.fr/fr/`.
- Ce que l’image seule doit faire comprendre : il faut répondre au simulateur et noter les obligations obtenues.
- Continuité : transforme le référentiel en activité et prépare la recherche d’une déclaration d’accessibilité.
- Contraintes critiques : réserver dans l’image générée une zone vide clairement délimitée pour la superposition ; ajouter ensuite de façon déterministe le QR authentique `scripts/images/qr-obligally.png`, la mention `Scannez-moi !` et l’URL principale complète ; interdire à ImageGen de produire un QR code, une URL, la mention `Scannez-moi !` ou du pseudo-texte dans cette zone ; conserver les liens `Simuler` et `Comprendre` dans la transcription HTML uniquement ; l’arbre de décision reste générique sans faux résultat.
- Alternative courte candidate : `Une communicante utilise le simulateur Obligally depuis un QR code et un lien visible.`

### Transcription exacte

#### Quelles obligations pour votre structure ?

*1. Q3 - Cadre légal | Obligations*

> Vous connaissez le cadre. Mais concrètement, quelles obligations s'appliquent à votre poste et à votre structure ?

##### Activité - simulateur Obligally (10 min)

- Cliquez sur Simuler et répondez aux questions
- Notez le résultat : quelles normes s'appliquent à vous ?

**Scannez-moi !**

- https://obligations-legales-accessibilite-numerique.fr/fr/
- Simuler : https://obligations-legales-accessibilite-numerique.fr/fr/simulation/
- Comprendre : https://obligations-legales-accessibilite-numerique.fr/fr/comprendre/

### Discours oral exact

Activité individuelle 10 min + débrief collectif 5 min. Faire ressortir : la plupart des structures publiques sont soumises au RGAA ; les communicants produisent des contenus concernés (PDF, vidéos, réseaux sociaux). Fallback si pas de réseau : distribuer le PDF de l'arbre de décision Idéance (dans _source/références/).

## Slide 27 - La déclaration d'accessibilité

- Correspondance : PPTX 41, `scripts/slides/02oe_declaration-accessibilite.py`.
- Rôle : rendre concret un document obligatoire.
- Famille de mise en page : `tableau_pedagogique` - variante tableau et activité.
- Idée principale : une déclaration relie un taux, un statut, un environnement de test et une voie de recours.
- Scène : une communicante cherche une déclaration dans le pied d’un site. Une fiche s’ouvre et cinq champs structurés sont vérifiés avec une loupe.
- Transformation : document introuvable ou opaque -> cinq informations repérées -> taux noté.
- Liste blanche du futur visuel : `La déclaration d'accessibilité` ; `Taux` ; `Statut` ; `Technologies` ; `Environnements de test` ; `Contact` ; `Cherchez la déclaration d'accessibilité de votre site`.
- Ce que l’image seule doit faire comprendre : la déclaration doit être trouvée puis lue comme une fiche structurée.
- Continuité : prolonge l’activité Obligally et prépare le récapitulatif des obligations.
- Contraintes critiques : ne pas inventer une adresse de ministère dans le nouveau visuel ; les exemples exacts restent dans la transcription ; l’absence de déclaration doit apparaître comme un signal, pas comme un jugement final.
- Alternative courte candidate : `Une déclaration d’accessibilité est recherchée puis contrôlée à travers cinq informations.`

### Transcription exacte

#### La déclaration d'accessibilité

*1. Q3 - Cadre légal | Déclaration*

| Que doit-elle contenir ? | Exemple concret |
| --- | --- |
| Taux de conformité RGAA | Ex. : 62 % conforme |
| Statut global | Partiellement conforme |
| Technologies utilisées | HTML5, CSS3, JavaScript |
| Environnements de test | Chrome + NVDA, Safari + VoiceOver |
| Contact et voie de recours | accessibilite@mon-ministere.gouv.fr |

##### Exercice pratique

- Cherchez la déclaration d'accessibilité de votre site
- URL type : /déclaration-accessibilité
- Notez le taux de conformité affiché

### Discours oral exact

5 minutes : chaque stagiaire cherche la déclaration de son propre site. Si introuvable : c'est déjà une non-conformité à signaler. La voie de recours = Défenseur des droits si absence de réponse en 2 mois.

## Slide 28 - Les obligations légales de mise en accessibilité

- Correspondance : PPTX 42, `scripts/slides/02oea_recap-obligations.py`.
- Rôle : synthétiser les documents et mentions attendus.
- Famille de mise en page : `processus_horizontal` - variante flux de pilotage.
- Idée principale : la démarche associe des documents de pilotage, un contact, un référent et une mention de conformité.
- Scène : trois documents - SPAN, plan d'action annuel et audit RGAA - rejoignent un même dossier. Un canal de contact relie ce dossier au public, tandis qu’un RAN humain coordonne la démarche.
- Transformation : obligations dispersées -> documents, contact et rôle clairement distingués -> démarche pilotée.
- Liste blanche du futur visuel : `Les obligations légales de mise en accessibilité` ; `SPAN` ; `Plan d'action annuel` ; `Audit d'accessibilité RGAA` ; `Un moyen de contact` ; `RAN (Référent Accessibilité Numérique)`.
- Ce que l’image seule doit faire comprendre : plusieurs documents et rôles forment une même démarche de mise en accessibilité.
- Continuité : clôt le cadre légal et prépare le passage du devoir à la conviction.
- Contraintes critiques : trois documents exactement ; un moyen de contact représenté comme un canal ; un RAN représenté comme une personne, jamais comme un document ; ne pas afficher les trois mentions de conformité dans l’image ; conserver leur tableau et leurs seuils exacts dans la transcription.
- Alternative courte candidate : `Trois documents, un moyen de contact et un référent accessibilité numérique structurent la démarche.`

### Transcription exacte

#### Les obligations légales de mise en accessibilité

*1. Q3 - Cadre légal | Récap obligations*

##### Documents obligatoires

- Schéma pluriannuel d'accessibilité numérique (SPAN)
- Plan d'action annuel
- Audit d'accessibilité RGAA en version 4.1.2
- Un moyen de contact
- RAN (Référent Accessibilité Numérique)

| Mention | Signification |
| --- | --- |
| Accessibilité : non conforme | 49 % et moins, ou aucun audit en cours de validité |
| Accessibilité : partiellement conforme | De 50 % à 99 % des critères respectés |
| Accessibilité : totalement conforme | 100 % des critères applicables validés |

### Discours oral exact

Rappel : environ 25 % des tests RGAA sont automatisables, le reste nécessite un audit humain. Attention : 100 % conforme ne veut pas forcément dire accessible - le RGAA ne couvre pas tous les usages. Le RAN est le référent accessibilité numérique, interlocuteur interne pour piloter la démarche.

## Slide 29 - 4. L'accessibilité numérique, pourquoi ?

- Correspondance : PPTX 43, `scripts/slides/02p_chapitre-q4.py`.
- Rôle : ouvrir la quatrième question.
- Famille de mise en page : `ouverture_illustree` - variante chapitre.
- Idée principale : dépasser la seule obligation pour comprendre la valeur d’une communication accessible.
- Scène : une communicante retire une barrière devant un chemin d’information ; le contenu atteint alors plusieurs personnes.
- Transformation : obligation subie -> accès réel -> bénéfice partagé.
- Liste blanche du futur visuel : `4. L'accessibilité numérique, pourquoi ?`.
- Ce que l’image seule doit faire comprendre : rendre accessible permet au message d’atteindre son public.
- Continuité : quitte le récapitulatif légal et prépare l’argument du droit fondamental.
- Contraintes critiques : ne pas utiliser une métaphore charitable ; le bénéfice porte sur l’accès et l’autonomie.
- Alternative courte candidate : `Une barrière retirée permet à l’information d’atteindre plusieurs personnes.`

### Transcription exacte

#### 4. L'accessibilité numérique, pourquoi ?

### Discours oral exact

Au-delà du cadre légal, pourquoi s'investir ? Cette section passe du devoir à la conviction : droit fondamental, charte de l'État, bénéfice pour tous.

## Slide 30 - Pourquoi agir ?

- Correspondance : PPTX 44, `scripts/slides/02pa_pourquoi-agir.py`.
- Rôle : relier droit à l’information et effets concrets.
- Famille de mise en page : `comparaison_transformation` - variante avant-après.
- Idée principale : une communication accessible transforme exclusion et décrochage en accès, autonomie et inclusion.
- Scène : à gauche, une personne se heurte à un message opaque ; quatre conséquences descendent vers l’exclusion. À droite, le même message devient accessible et quatre effets remontent vers l’inclusion sociale.
- Transformation : non-compréhension -> accès à l’information ; frustration -> confiance ; décrochage -> autonomie ; exclusion -> inclusion.
- Liste blanche du futur visuel : `Pourquoi agir ?` ; `Un droit, pas une faveur` ; `Communication inaccessible` ; `Communication accessible` ; `Accès` ; `Confiance` ; `Autonomie` ; `Inclusion`.
- Ce que l’image seule doit faire comprendre : l’accessibilité change concrètement l’effet de la communication.
- Continuité : donne les bénéfices humains et prépare la définition de la communication accessible.
- Contraintes critiques : lecture gauche-droite évidente ; rouge seulement côté barrière, vert seulement côté résultat ; ne pas inventer de logo de l’État ; la couverture authentique de la charte peut être superposée de manière déterministe si elle reste utile.
- Alternative courte candidate : `Une communication accessible transforme quatre conséquences négatives en accès, confiance, autonomie et inclusion.`

### Transcription exacte

#### Pourquoi agir ?

*1. Q4 - Pourquoi | Droit et charte*

##### Un droit, pas une faveur

- Droit fondamental d'acces a l'information
- Lutte contre la discrimination numérique
- Inclusion dans la vie professionnelle et citoyenne

| Communication inaccessible | Communication accessible |
| --- | --- |
| Non compréhension | Acces a l'information |
| Frustration, enervement | Confiance en soi |
| Decrochage | Autonomie |
| Exclusion | Inclusion sociale |

### Discours oral exact

Le tableau gagnant-gagnant est tire de la Charte d'accessibilité de la communication de l'État (SIG, mars 2021). Cote gauche : ce que vit la personne face a un contenu inaccessible. Cote droit : ce qu'une communication accessible lui apporte. Pour le communicant, une communication accessible est une communication qui atteint son objectif. Montrer la couverture de la charte : c'est un document officiel du Premier Ministre.

## Slide 31 - Communication accessible, de quoi parle-t-on ?

- Correspondance : PPTX 45, `scripts/slides/02pb_accessibiliser-communication.py`.
- Rôle : traduire le principe en questions métier.
- Famille de mise en page : `checklist_processus` - variante trois questions.
- Idée principale : une communication accessible peut être lue, comprise et utilisée sur le support final.
- Scène : une communicante prépare une campagne composée d’une page web, d’une vidéo, d’un PDF et d’une affiche. Trois filtres contrôlent public empêché, autre chemin et règle simple.
- Transformation : production par support -> trois questions communes -> accès au message.
- Liste blanche du futur visuel : `Communication accessible, de quoi parle-t-on ?` ; `Lire` ; `Comprendre` ; `Utiliser` ; `Qui risque d'être empêché par ce support ?` ; `Quel autre chemin donne accès à la même information ?` ; `Quelle règle simple peut être appliquée dès maintenant ?`.
- Ce que l’image seule doit faire comprendre : trois questions permettent d’examiner tous les supports de communication.
- Continuité : généralise le bénéfice et prépare les outils pour agir.
- Contraintes critiques : quatre catégories de supports représentées ; pas de paragraphe ; ne pas transformer les trois questions en audit complet.
- Alternative courte candidate : `Trois questions aident une communicante à rendre quatre familles de supports accessibles.`

### Transcription exacte

#### Communication accessible, de quoi parle-t-on ?

*1. Q4 - Pourquoi | Communication accessible*

> Contenus que le public peut lire, comprendre et utiliser.

##### 3 questions à garder en tête

- Qui risque d'être empêché par ce support ?
- Quel autre chemin donne accès à la même information ?
- Quelle règle simple peut être appliquée dès maintenant ?

##### Les supports concernés

- Web : site, application, newsletter, mails
- Médias : vidéo, podcast, visuel animé
- Documents : PDF, bureautique, formulaires
- Imprimés : affiche, flyer, plan, QR code...

### Discours oral exact

Cette slide sert de cadrage. Le guide source est une introduction utile, pas un référentiel complet ni un substitut à une formation. Faire reformuler par le groupe : accessibiliser une communication, ce n'est pas seulement corriger un site web, c'est penser le support final et l'usage réel.

## Slide 32 - 5. L'accessibilité numérique, comment s'y mettre ?

- Correspondance : PPTX 46, `scripts/slides/02q_chapitre-q5.py`.
- Rôle : ouvrir la cinquième question.
- Famille de mise en page : `ouverture_illustree` - variante chapitre.
- Idée principale : les premiers gestes sont déjà à portée de main.
- Scène : une communicante ouvre une boîte à outils contenant réglages système, vérificateur, règles de rédaction et méthode FALC.
- Transformation : intention -> outils disponibles -> premiers gestes.
- Liste blanche du futur visuel : `5. L'accessibilité numérique, comment s'y mettre ?`.
- Ce que l’image seule doit faire comprendre : la mise en accessibilité commence avec des outils et pratiques accessibles immédiatement.
- Continuité : répond à la question laissée par la slide 31 et prépare les fonctions déjà intégrées aux postes.
- Contraintes critiques : boîte à outils concrète, pas de magie ni automatisation totale ; pas de marque inventée.
- Alternative courte candidate : `Une boîte à outils rassemble les premiers moyens de rendre les contenus accessibles.`

### Transcription exacte

#### 5. L'accessibilité numérique, comment s'y mettre ?

### Discours oral exact

Dernière question du module : passer à l'action. Les slides suivantes donnent les premiers outils concrets avant d'entrer dans les modules pratiques (Word, web, réseaux sociaux).

## Slide 33 - Des outils déjà intégrés à vos postes

- Correspondance : PPTX 47, `scripts/slides/02qa_outils-os.py`.
- Rôle : montrer que des fonctions d’accessibilité sont déjà disponibles.
- Famille de mise en page : `checklist_processus` - variante outils.
- Idée principale : systèmes et suites bureautiques offrent déjà des fonctions pour voir, entendre et interagir autrement.
- Scène : autour d'un poste de travail, quatre cartes montrent une communicante activant successivement le zoom, les sous-titres, la navigation au clavier et le vérificateur d'accessibilité.
- Transformation : poste standard perçu comme figé -> réglages activés -> plusieurs modes d’usage.
- Liste blanche du futur visuel : `Des outils déjà intégrés à vos postes` ; `Loupe et zoom intégrés` ; `Sous-titres en temps réel` ; `Navigation au clavier` ; `Vérification d'accessibilité (Word, PowerPoint)`.
- Ce que l’image seule doit faire comprendre : il n’est pas nécessaire d’attendre un outil spécialisé pour commencer.
- Continuité : ouvre la boîte à outils et prépare les règles transversales de production.
- Contraintes critiques : quatre cartes exactement ; reprendre les quatre libellés complets et exacts ; ne pas inventer une interface Windows ou macOS précise ; aucun faux logo NVDA ; ne pas transformer les filtres de couleur ou le mode sombre en mesure de contraste ; distinguer outil d'usage et vérificateur de document ; conserver la liste exhaustive des fonctions dans l'accordéon.
- Alternative courte candidate : `Un poste de travail propose déjà zoom, lecteur d’écran, sous-titres, voix, clavier et vérification.`

### Transcription exacte

#### Des outils déjà intégrés à vos postes

*1. Q5 - Comment | Outils intégrés*

> Les systèmes d'exploitation et les suites bureautiques intègrent déjà des fonctions d'accessibilité. Pas besoin de tout réinventer.

##### Vision

- Loupe et zoom intégrés
- Filtres de couleur et mode sombre
- Narrateur / NVDA (lecteur d'écran)
- Réglage de la taille du texte

##### Audition et interaction

- Sous-titres en temps réel
- Commandes vocales
- Navigation au clavier
- Vérification d'accessibilité (Word, PowerPoint)

### Discours oral exact

Montrer rapidement où trouver ces réglages : Windows > Paramètres > Accessibilité / macOS > Préférences Système > Accessibilité. Word et PowerPoint proposent un vérificateur d'accessibilité intégré (onglet Révision). On le verra en détail dans le module 2.

## Slide 34 - Règles transversales : texte, contraste, QR

- Correspondance : PPTX 48, `scripts/slides/02qb_regles-transversales.py`.
- Rôle : installer trois réflexes communs aux supports.
- Famille de mise en page : `checklist_processus` - variante trois contrôles.
- Idée principale : lisibilité, contraste et accès alternatif ne dépendent pas du support.
- Scène : une communicante valide successivement un bloc de texte, une paire de couleurs et un symbole simplifié de QR accompagné de la règle `Lien visible à côté`. Le symbole ne forme pas un code scannable.
- Transformation : contrôle à l’œil ou canal unique -> trois vérifications -> support utilisable.
- Liste blanche du futur visuel : `Règles transversales : texte, contraste, QR` ; `Textes lisibles` ; `Contrastes testés` ; `QR codes utiles` ; `Un support accessible ne dépend jamais d'un seul canal.`.
- Ce que l’image seule doit faire comprendre : trois contrôles simples s’appliquent partout.
- Continuité : transforme les outils en règles de production et prépare l’écriture accessible.
- Contraintes critiques : trois cartes exactement ; ratio 4,5:1 visible si un chiffre est utilisé ; symbole QR volontairement non scannable ; aucun QR réel, aucune URL, aucun pseudo-lien et aucune superposition déterministe ; la règle `Lien visible à côté` peut être affichée car elle provient de la source ; rouge absent sauf défaut explicite.
- Alternative courte candidate : `Trois contrôles portent sur le texte, les contrastes et la présence d’un lien visible à côté d’un QR.`

### Transcription exacte

#### Règles transversales : texte, contraste, QR

*1. Q5 - Comment | Règles transversales*

##### 1. Textes lisibles

- Police simple, sans empattement
- Alignement à gauche
- Paragraphes courts et aérés
- Taille adaptée au support final

##### 2. Contrastes testés

- Ratio 4,5:1 minimum
- Idéal : viser 7:1
- Éviter les dégradés sous le texte
- Tester avec un outil, pas à l'œil

##### 3. QR codes utiles

- Jamais le seul accès
- Lien visible à côté
- Mention « Scannez-moi ! »
- Taille et contraste suffisants

> Un support accessible ne dépend jamais d'un seul canal.

### Discours oral exact

Cette slide annonce les réflexes qui seront travaillés ensuite dans Word, le web et les réseaux sociaux. Ne pas entrer trop tôt dans les détails techniques : elle doit installer un filtre de lecture commun. Pour les QR codes, rappeler la règle demandée : toujours ajouter le lien visible à côté et la mention Scannez-moi !

## Slide 35 - FALC et langage clair

- Correspondance : PPTX 49, `scripts/slides/02qc_falc-langage-clair.py`.
- Rôle : distinguer deux démarches complémentaires.
- Famille de mise en page : `comparaison_transformation` - variante deux colonnes.
- Idée principale : le FALC suit un cadre formel avec validation, tandis que le langage clair améliore tout contenu.
- Scène : un texte dense se divise en deux voies. La voie FALC comporte trois cartes pour les phrases courtes, les images explicatives et la validation par des personnes concernées. La voie langage clair comporte trois cartes pour structurer, expliquer et tester.
- Transformation : contenu difficile -> deux démarches -> message plus accessible.
- Liste blanche du futur visuel : `FALC et langage clair` ; `FALC` ; `Phrases courtes` ; `Images explicatives` ; `Validation par des personnes concernées` ; `Langage clair` ; `Structurer` ; `Expliquer` ; `Tester`.
- Ce que l’image seule doit faire comprendre : les deux démarches se complètent mais ne se confondent pas.
- Continuité : applique les règles de texte et prépare les premiers pas de formation.
- Contraintes critiques : trois cartes par voie exactement ; la validation par des personnes concernées appartient au FALC ; ne pas faire apparaître `Guider` dans le visuel, mais le conserver dans l'accordéon ; aucun faux logo FALC généré ; logo authentique superposé seulement si utile.
- Alternative courte candidate : `Un même contenu suit deux voies complémentaires : FALC formel et langage clair.`

### Transcription exacte

#### FALC et langage clair

*1. Q5 - Comment | FALC et langage clair*

> Simplifier ne veut pas dire appauvrir : c'est rendre le message accessible au plus grand nombre.

##### FALC - Facile à lire et à comprendre

- Règles européennes d'accessibilité cognitive
- Phrases courtes, mots simples, une idée par phrase
- Images explicatives, mise en page aérée
- Validation par des personnes concernées

##### Langage clair

- Structurer : titres, listes, paragraphes courts
- Expliquer : sigles, jargon, termes techniques
- Guider : verbes d'action, consignes explicites
- Tester : relecture à voix haute, lisibilité

### Discours oral exact

Le FALC est un cadre formel européen, le langage clair est une démarche applicable à tout contenu. Les deux se complètent. Ne pas confondre FALC et écriture simplifiée : le FALC suit des règles précises et implique une validation par des lecteurs en situation de handicap cognitif.

## Slide 36 - Comment s'y mettre ?

- Correspondance : PPTX 50, `scripts/slides/02qca_comment-sy-mettre.py`.
- Rôle : donner une progression rassurante et des ressources de formation.
- Famille de mise en page : `processus_horizontal` - variante quatre étapes.
- Idée principale : sensibilisation, écoute, connaissance des outils et formation permettent d’avancer progressivement.
- Scène : une communicante monte quatre marches basses. À l’arrivée, trois panneaux orientent vers Mentor, IGPDE et DINUM.
- Transformation : ne pas savoir par où commencer -> quatre étapes -> offre de formation.
- Liste blanche du futur visuel : `Comment s'y mettre ?` ; `Sensibilisation` ; `Écoute` ; `Connaître les matériels et logiciels adaptés` ; `Formation` ; `Mentor` ; `IGPDE` ; `DINUM`.
- Ce que l’image seule doit faire comprendre : on avance par étapes et des ressources existent déjà.
- Continuité : élargit les pratiques d’écriture et prépare la méthode FALC détaillée.
- Contraintes critiques : quatre étapes dans l’ordre ; ne pas inventer de logo pour les organismes ; la formation IGPDE porte la référence 102846 dans la transcription seulement.
- Alternative courte candidate : `Quatre étapes mènent vers trois ressources de formation.`

### Transcription exacte

#### Comment s'y mettre ?

*1. Q5 - Comment | Premiers pas*

> Des règles et bonnes pratiques simples permettent de garantir l'accessibilité à toutes et tous.

##### 4 étapes pour avancer

- Être sensibilisé - c'est ce qu'on fait aujourd'hui
- Être à l'écoute des besoins spécifiques
- Connaître les matériels et logiciels adaptés
- Se former pour découvrir un nouvel univers

##### Offre de formation

- Mentor (en ligne) : l'accessibilité numérique selon votre métier
- IGPDE : l'accessibilité numérique pour la bureautique et le web (réf. 102846)
- DINUM : sensibilisation, design inclusif, audit RGAA

### Discours oral exact

Rassurer les stagiaires : ils ne partent pas de zéro. La sensibilisation d'aujourd'hui est la première étape. Mentor est un parcours en ligne gratuit. La formation IGPDE 102846 est le prolongement de cette journée. La DINUM propose des formats plus techniques pour ceux qui veulent aller plus loin.

## Slide 37 - FALC : la méthode en 5 étapes

- Correspondance : PPTX 51, `scripts/slides/02qcb_falc-methode.py`.
- Rôle : montrer que le FALC est un processus rigoureux.
- Famille de mise en page : `processus_horizontal` - variante cinq étapes.
- Idée principale : la simplification nécessite préparation, travail en duo, validation, publication et itération.
- Scène : un document traverse cinq postes de travail. La validation par des personnes concernées forme une porte obligatoire avant publication.
- Transformation : texte source -> simplification collaborative -> validation -> publication -> amélioration.
- Liste blanche du futur visuel : `FALC : la méthode en 5 étapes` ; `Préparatoire` ; `Transcription en duo` ; `Validation` ; `Publication` ; `Itération` ; `Personnes concernées` ; `80 % des critères`.
- Ce que l’image seule doit faire comprendre : un texte ne devient pas FALC par simple réécriture individuelle.
- Continuité : approfondit une méthode citée précédemment et prépare son exemple concret.
- Contraintes critiques : cinq étapes dans l’ordre ; validation obligatoire avant logo ; ne pas générer de faux logo européen ; couverture Unapei authentique uniquement en superposition déterministe si nécessaire.
- Alternative courte candidate : `Un document suit cinq étapes, dont une validation obligatoire par des personnes concernées.`

### Transcription exacte

#### FALC : la méthode en 5 étapes

*1. Q5 - Comment | FALC méthode*

> Il est très difficile de faire simple ! Le FALC suit un processus rigoureux.

##### Les 5 étapes

1. Préparatoire : recherches, résumé simplifié, contrôle des contre-sens
2. Transcription en duo : simplification, illustrations, mise en page
3. Validation : relecture par des personnes handicapees intellectuelles
4. Publication : logo FALC, credit des personnes impliquees
5. Itération : savoir dire stop - un texte ne sera jamais compris a 100 %

##### Conditions obligatoires

- Validation par des personnes concernées (obligatoire)
- 80 % des critères FALC respectes (Unapei)
- Logo europeen FALC + credit des valideurs

### Discours oral exact

Insister sur le fait que le FALC n'est pas juste 'ecrire simple'. C'est un processus formalise avec une validation obligatoire par des personnes concernées. 'Rien pour nous sans nous' est le principe fondamental. Le logo FALC ne peut pas être appose sans cette validation. En pratique, contacter des associations comme l'Unapei ou des ESAT pour trouver des relecteurs. Le guide Unapei 'L'information pour tous' est téléchargeable gratuitement.

## Slide 38 - Exemple : le rapport DIA en version accessible et FALC - ÉTALON

- Correspondance : PPTX 52, `scripts/slides/02qcc_falc-exemple-dia.py`.
- Rôle : montrer deux versions complémentaires d’un même rapport.
- Famille de mise en page : `comparaison_transformation` - variante comparaison documentaire.
- Idée principale : PDF accessible et version FALC répondent à des usages complémentaires.
- Scène : un document institutionnel source se divise en deux versions côte à côte. À gauche, une illustration IGPDE générique de PDF accessible montre une structure balisée et un ordre de lecture. À droite, phrases courtes, pictogrammes et validation humaine accompagnent le logo FALC authentique.
- Transformation : contenu institutionnel unique -> deux versions complémentaires -> public élargi.
- Liste blanche du futur visuel : `Exemple : le rapport DIA en version accessible et FALC` ; `PDF accessible` ; `Structure balisée` ; `Ordre de lecture logique` ; `Version FALC` ; `Phrases courtes` ; `Pictogrammes` ; `Validé par des personnes concernées`.
- Cibles des liens HTML : `PDF accessible` -> `https://handicap.gouv.fr/sites/handicap/files/2025-03/delegation-interministerielle-accessibilite-rapport-activite-2024.pdf` ; `Version FALC` -> `https://handicap.gouv.fr/sites/handicap/files/2025-03/delegation-interministerielle-accessibilite-synthese-FLAC-rapport-activite-2024.pdf`.
- Ce que l’image seule doit faire comprendre : accessibilité technique et simplification cognitive ne sont pas la même version.
- Continuité : rend la méthode tangible et prépare la conclusion sur la conception accessible.
- Contraintes critiques : deux colonnes équilibrées ; ne pas opposer les versions ; générer à gauche une illustration générique de PDF accessible, sans faux titre, faux logo ni pseudo-texte ; réserver à droite une zone propre pour superposer de façon déterministe `scripts/images/logo-falc-europe.jpg` dans la colonne `Version FALC` ; ne pas utiliser `scripts/images/rapport-dia-2024.jpg`, qui est un pictogramme PDF générique et non la couverture du rapport DIA ; ne pas prétendre montrer une couverture authentique.
- Alternative courte candidate : `Le rapport DIA existe en PDF accessible et en version FALC complémentaire.`

### Transcription exacte

#### Exemple : le rapport DIA en version accessible et FALC

*1. Q5 - Comment | FALC exemple*

> Le rapport d'activité 2024 de la Délégation interministérielle à l'accessibilité existe en PDF accessible et en version FALC.

##### PDF accessible

- Structure balisée (titres, listes, tableaux)
- Alt text sur les images, ordre de lecture logique
- Télécharger (handicap.gouv.fr)

##### Version FALC

- Phrases courtes, vocabulaire simple, pictogrammes
- Validé par des personnes concernées
- Télécharger (handicap.gouv.fr)

### Discours oral exact

Montrer les deux documents si possible. Le rapport de la DIA est un bon exemple car il vient d'une institution publique et montre que le FALC n'est pas reserve aux associations. Le PDF accessible et la version FALC sont complementaires : le premier est le document officiel rendu navigable, le second est une version simplifiee pour un public plus large.

PDF accessible : https://handicap.gouv.fr/sites/handicap/files/2025-03/delegation-interministerielle-accessibilite-rapport-activite-2024.pdf

Version FALC : https://handicap.gouv.fr/sites/handicap/files/2025-03/delegation-interministerielle-accessibilite-synthese-FLAC-rapport-activite-2024.pdf

## Slide 39 - L'accessibilité dès la conception

- Correspondance : PPTX 53, `scripts/slides/02qd_by-design.py`.
- Rôle : conclure la partie par le design universel.
- Famille de mise en page : `synthese_action` - variante métaphore concrète.
- Idée principale : concevoir accessible dès le départ est plus simple et profite à davantage de personnes.
- Scène : un escalier et une pente douce sont dessinés comme un seul chemin intégré. Poussette, personne âgée, femme enceinte et personne en fauteuil l’utilisent sans détour.
- Transformation : adaptation ajoutée après coup -> chemin intégré dès la conception -> usage partagé.
- Liste blanche du futur visuel : `L'accessibilité dès la conception` ; `L'accessibilité rend les choses possibles pour certains et plus simples pour tous` ; `Concevoir accessible, pas adapter après`.
- Ce que l’image seule doit faire comprendre : une solution intégrée dès le début sert plusieurs usages sans stigmatiser.
- Continuité : synthétise toute la partie et prépare les modules pratiques Word, Web et réseaux sociaux.
- Contraintes critiques : rampe réellement intégrée aux marches ; diversité d’usages crédible ; pas de photographie ; le fauteuil n’est pas isolé sur un parcours séparé ; aucun faux label institutionnel ; ne pas générer ni superposer de bandeau `#accessibleatous`.
- Alternative courte candidate : `Une rampe intégrée aux marches est utilisée par plusieurs personnes sans détour.`

### Transcription exacte

#### L'accessibilité dès la conception

*1. Q5 - Comment | Conception accessible*

> L'accessibilité rend les choses possibles pour certains et plus simples pour tous.

##### Concevoir accessible, pas adapter après

- Intégrer l'accessibilité dès le début, pas en rattrapage
- Un document bien structuré profite à tous les lecteurs
- La rampe intégrée est plus élégante que la rampe ajoutée

### Discours oral exact

L'escalier avec rampe intégrée est un exemple emblématique du design universel. Faire le parallèle avec la communication : un document structuré dès le départ (titres, alt text, contraste) est accessible sans effort supplémentaire. Le bandeau #accessibleatous rappelle que les bénéficiaires dépassent largement le public handicapé.

## Contrôles de préparation avant génération

- Nombre attendu : 39 slides web et 39 correspondances PPTX.
- Étalons : 01, 09, 26 et 38 uniquement avant validation visuelle.
- Titres : 39 titres issus du PPTX, sans renumérotation visible dans les images.
- Transcriptions : 39 blocs, contenus visibles conservés hors masque récurrent.
- Descriptions d'illustration internes au PPTX : exclues des transcriptions ; l'alternative du nouveau visuel est portée séparément.
- Discours oraux : 39 blocs issus des notes `add_notes()`.
- Alternatives : 39 candidates courtes, centrées sur l’information ou la fonction du visuel.
- Familles de mise en page : 39 affectations utilisant exclusivement les six identifiants canoniques du preset local.
- Tableaux à reconstruire sémantiquement dans le HTML : slides 15, 16, 17, 20, 24, 27, 28 et 30.
- Superpositions déterministes prévues : slide 26 pour le QR authentique, la mention d'appel et l'URL principale ; slide 38 pour le logo FALC authentique dans la colonne `Version FALC` ; slides 30, 35 et 37 pour les ressources authentiques seulement si elles restent nécessaires à la compréhension.
- Familles inspectées en pleine résolution après génération : ouverture, persona, processus, tableau, comparaison et synthèse.
- Aucun appel ImageGen ne doit commencer avant validation du présent storyboard.

## Relecture interne

- Structure : 39 slides, 39 correspondances, 39 transcriptions, 39 discours oraux et 39 alternatives candidates.
- Séquences : numérotation web 01 à 39 et correspondance PPTX 15 à 53 continues, sans trou ni doublon.
- Sources : 39 modules Python distincts, tous présents dans l’usine.
- Titres : les 39 titres du storyboard correspondent exactement aux titres du PPTX.
- Fidélité textuelle : aucun paragraphe visible, cellule de tableau ou bloc de notes du PPTX ne manque dans la section correspondante après normalisation typographique.
- Grammaire visuelle : chaque slide possède une scène, une transformation, une liste blanche, une continuité et des contraintes critiques.
- Étalons : seules les slides 01, 09, 26 et 38 portent le marqueur `ÉTALON`.
- État : relecture externe intégrée et passe technique terminée ; génération ImageGen autorisée uniquement pour la planche de référence et les quatre étalons.
