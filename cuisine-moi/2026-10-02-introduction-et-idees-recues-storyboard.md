# Partie 0 - Introduction et idées reçues

## Statut du document

- Storyboard complet, relu indépendamment puis corrigé. Les quatre étalons 01, 04, 07 et 09 ont été validés par Alex. Les quatorze visuels sont produits et la revue consolidée autorise leur intégration HTML après correction des réserves documentaires.
- Source : slides PPTX 1 à 14 du support IGPDE 102846, générées par les modules Python indiqués pour chaque slide.
- Correspondance : 14 visuels web pour 14 slides PPTX, dans le même ordre.
- Numérotation publique : 1 à 14. Les numéros PPTX restent uniquement dans la traçabilité.
- Titre public : « Partie 0 - Introduction et idées reçues ».
- Slug : `introduction-et-idees-recues`.
- Périmètre exclu : la slide PPTX 15 ouvre la Partie I et n'appartient pas à cette série.
- Étalons validés : slides web 01, 04, 07 et 09.

## Diagnostic pédagogique

- Public : communicantes et communicants, sans prérequis technique.
- Action attendue : comprendre le parcours de la journée, faire connaissance, entrer dans une dynamique de coopération et mettre à distance six idées reçues sur l'accessibilité numérique.
- Corpus : huit slides d'accueil et d'organisation, puis six idées reçues présentées à partir des cartes Ideance originales.
- Idée pivot : l'accessibilité est un sujet concret, partagé et praticable, dont les freins peuvent être discutés avant l'apport théorique.
- Charge cognitive : les visuels 1 à 8 simplifient la projection ; les accordéons conservent les contenus textuels complets. Les visuels 9 à 14 préservent les cartes originales en fac-similé et séparent clairement leur décryptage court du décryptage plus développé du PPTX.
- Niveau cognitif visé : se repérer, se présenter, confronter une représentation, puis reformuler une compréhension plus juste.

## Contrat de série

- Référence visuelle opposable : preset local `IGPDE Accessibilité - bleu illustré` de l'usine, dans `_source/imagegen-igpde/`.
- Références inspectées : `reference-01-ouverture.png`, `reference-02-avant-apres.png`, `reference-03-tableau.png` et `reference-04-checklist.png`, en résolution originale.
- Format final : image 16:9, 1672 x 941 pixels.
- Masque commun : fond blanc lumineux, très grand titre bleu nuit aligné à gauche, scène ou objet concret central, cartes bleu clair aux contours fins, espace libre généreux, aucun pied de page dans l'image.
- Progression : repère 1 à 14 dans l'interface web uniquement ; aucun numéro PPTX visible dans l'image. Les titres sources `Idée reçue N / 6` restent visibles sur les six fac-similés, car ils font partie du contenu pédagogique.
- Palette : bleu France `#000091`, bleu d'action `#2B6DE8`, bleu clair `#E3EEFF`, gris bleuté `#D7E1F0`, vert `#00A95F` réservé à la validation et rouge `#E1000F` réservé au problème.
- Typographie : Marianne, avec Arial comme seul fallback.
- Illustrations : semi-plates, institutionnelles, concrètes, accueillantes et non photoréalistes. Les personnages servent une action. La diversité reste crédible, sans effet catalogue ni représentation caricaturale du handicap.
- Ressources authentiques : conserver les photographies des deux intervenants, l'affiche du Service d'information du Gouvernement, les QR codes et les douze pages du PDF Ideance. Ces ressources ne sont jamais recréées par ImageGen.
- Courriels : les deux adresses professionnelles sont absentes des images mais reprises dans le premier accordéon avec le contenu exact du PPTX.
- Interdits : faux logo, emblème officiel inventé, photographie synthétique, photoréalisme, 3D lourde, texture papier, tableau blanc dessiné, blob décoratif, ombre lourde, rouge décoratif, texte parasite, pseudo-lettres, paragraphe dense dans une carte ou contenu absent de la source.
- Fidélité : le titre source reste inchangé dans chaque image. Le visuel garde le message principal et les libellés indispensables. La transcription conserve le contenu de la slide source. Le discours oral reprend intégralement les notes `add_notes()`.
- Éléments déterministes : photographies, affiche, QR codes, URL et fac-similés sont composés à partir des fichiers sources après la génération du fond ou de la scène. ImageGen doit laisser leur emplacement libre et ne jamais les imiter.
- Traçabilité : `outputs/ia-slides/2026-10-02-introduction-et-idees-recues/` conserve le storyboard, les prompts, les reçus et la planche-contact. Ce dossier de travail n'est pas versionné.

## Matrice des familles de mise en page

| Famille canonique | Usage dans la série | Slides |
|---|---|---:|
| `ouverture_illustree` | Couverture et entrée dans l'activité | 01, 08 |
| `checklist_processus` | Objectifs, programme et consignes organisées | 02, 03, 06 |
| `synthese_action` | Présentation d'une personne | 04, 05 |
| `processus_horizontal` | Passage du débat à l'entraide | 07 |
| `fac_simile_cartes` | Composition déterministe recto-verso des cartes originales | 09 à 14 |

- `fac_simile_cartes` n'est pas une nouvelle famille ImageGen. Elle décrit une composition déterministe hors génération, imposée par le choix de préserver les cartes authentiques.
- Les slides 1 à 8 relèvent d'ImageGen. Les slides 9 à 14 utilisent les pages originales du PDF, sans génération ni retouche de leur contenu.
- `DEVIATION` slides 09 à 14 : rendu déterministe depuis le PDF source au lieu d'ImageGen, parce que l'utilisateur exige le fac-similé exact des cartes, de leur QR code et de leur lien visible. Le reçu doit identifier `source_type=facsimile_pdf`, le couple de pages source, la copie projet, le contrôle visuel et le résultat du test QR.

## Règles des deux accordéons

- Accordéon « Transcription » : titre de slide comme premier titre interne, puis contenu visible exact du PPTX et alternatives utiles structuré avec titres, paragraphes et listes HTML sémantiques.
- Accordéon « Lire le discours oral » : texte exact de `add_notes()`, structuré pour la lecture sans ajouter ni supprimer de consigne.
- Éléments exclus : fil d'Ariane, logos du masque, pied de page récurrent, date et numéro de page.
- Liens : conserver le libellé visible exact et la destination source dans le HTML final.
- Slide 02 : conserver les trois objectifs exacts, la description accessible de l'affiche et le lien `https://www.info.gouv.fr/accessibilite`.
- Slides 04 et 05 : conserver les biographies et les adresses professionnelles exactes dans la transcription, sans les afficher dans l'image.
- Slides 09 à 14 : le premier accordéon comporte deux sous-sections obligatoires, `Texte visible des cartes` et `Contenu exact du PPTX`. La première restitue le recto et le verso Ideance ; la seconde restitue les libellés, l'idée reçue, les quatre éléments de décryptage, l'incitation et l'URL du PPTX.
- Les émojis visibles sur les rectos des cartes sont transcrits, sans être utilisés comme seuls porteurs d'information.
- `Recto` et `Verso` sont de vrais sous-titres dans le HTML. L'URL visible reste `ideance.net/blog/4602/idees-recues-a11y` et devient un lien vers `https://ideance.net/blog/4602/idees-recues-a11y`. La marque visible `ideance` est transcrite.
- Les chaînes `[ ]` de la slide 06 restent du texte de transcription et ne deviennent ni champs de formulaire ni cases interactives.

## Colonne vertébrale

1. Accueillir et donner le cap de la formation.
2. Présenter le parcours, les intervenants et les participantes et participants.
3. Installer le travail en binôme et lancer le débat.
4. Confronter six idées reçues à des faits et à des conséquences concrètes.
5. Préparer la Partie I : l'accessibilité concerne les pratiques quotidiennes et se construit dès le départ.

## Points de vigilance de fidélité

- Le titre public `Partie 0 - Introduction et idées reçues` n'est pas ajouté au visuel 01 : le visuel conserve le titre de couverture du PPTX.
- Le sous-titre de couverture est `Formation 102846 | Bureautique et web`.
- Les titres et contenus des slides 1 à 8 viennent exclusivement des sources PPTX. Les scènes peuvent reformuler visuellement une idée, mais aucun libellé inventé ne devient texte affiché.
- Les photographies des intervenants sont des ressources authentiques et ne doivent être ni redessinées ni modifiées par ImageGen.
- Les courriels ne sont pas inscrits dans les images.
- Les pages des cartes Ideance restent inchangées, sans recadrage destructif, correction typographique, recoloration ou remplacement du QR code.
- Les versos Ideance et les décryptages du PPTX ne disent pas exactement la même chose. Ils restent tous deux présents et explicitement séparés.
- La slide PPTX 15 est hors périmètre, même comme transition.

## Slide 01 - L'accessibilité numérique pour la bureautique et le web - ÉTALON

- Correspondance : PPTX 1, `scripts/slides/01_couverture.py`.
- Rôle : accueillir le groupe et installer le sujet général de la journée.
- Famille de mise en page : `ouverture_illustree`.
- Idée principale : la formation relie la production bureautique et la publication web à une même exigence d'accessibilité.
- Scène : une communicante à son poste de travail consulte un écran montrant côte à côte un document bureautique, une page web, une vidéo sous-titrée et un formulaire. Les quatre supports convergent vers une même zone de contrôle accessible, sans texte supplémentaire.
- Transformation : supports dispersés -> démarche commune -> contenus utilisables.
- Textes visibles autorisés : `L'accessibilité numérique pour la bureautique et le web` ; `Formation 102846 | Bureautique et web`.
- Ce que l'image seule doit faire comprendre : la journée porte sur plusieurs supports de communication et sur leur accessibilité.
- Continuité : ouvre la série et prépare les objectifs pédagogiques.
- Contraintes critiques : aucun faux logo ; aucune mention `Partie 0` dans l'image ; conserver les deux libellés exacts ; ne pas ajouter une personne avec un handicap comme symbole décoratif.
- Alternative courte candidate : `Une communicante travaille sur un document, une page web, une vidéo sous-titrée et un formulaire accessibles.`

### Transcription exacte

#### L'accessibilité numérique pour la bureautique et le web

Formation 102846 | Bureautique et web

### Discours oral exact

Slide de couverture - accueil des stagiaires et installation.

## Slide 02 - Objectifs pédagogiques

- Correspondance : PPTX 2, `scripts/slides/02_objectifs.py`.
- Rôle : expliciter les trois résultats attendus de la formation.
- Famille de mise en page : `checklist_processus`.
- Idée principale : comprendre, repérer et corriger forment une progression opérationnelle.
- Scène : trois grandes cartes reliées de gauche à droite. La première montre une personne qui explique un cadre commun, la deuxième une loupe sur des erreurs de document et la troisième une main qui corrige un contenu. À droite, un emplacement vertical réservé accueille l'affiche authentique `_assets/affiche-sig-handicap.jpg`. Le QR code `_assets/qrcode-info-gouv-accessibilite.png` et son URL sont ajoutés de manière déterministe sous les cartes.
- Transformation : comprendre les enjeux -> identifier les erreurs -> rendre les contenus accessibles.
- Textes visibles autorisés : `Objectifs pédagogiques` ; `Expliquer les enjeux de l'accessibilité numérique et son cadre légal dans le contexte de la communication` ; `Identifier et évaluer les principales erreurs d'accessibilité` ; `Rendre des contenus numériques accessibles` ; `https://www.info.gouv.fr/accessibilite`.
- Ce que l'image seule doit faire comprendre : la formation débouche sur trois capacités concrètes et progressives.
- Continuité : répond à la couverture et prépare le programme de la journée.
- Contraintes critiques : trois objectifs exactement ; ordre inchangé ; affiche et QR authentiques ; URL lisible ; aucun nouveau slogan ; ne pas demander à ImageGen de recréer l'affiche ou le QR code. Rejeter tout caractère erroné, texte trop petit ou chevauchement avec l'affiche, le QR code ou l'URL.
- Alternative courte candidate : `Trois étapes conduisent de la compréhension des enjeux à la production de contenus numériques accessibles.`

### Transcription exacte

#### Objectifs pédagogiques

- Expliquer les enjeux de l'accessibilité numérique et son cadre légal dans le contexte de la communication
- Identifier et évaluer les principales erreurs d'accessibilité
- Rendre des contenus numériques accessibles

Description de l'affiche : Affiche du Service d'information du Gouvernement pour les 20 ans de la loi handicap. Un ordinateur à l'écran inversé illustre un outil inaccessible. L'affiche invite les agents publics à utiliser les outils disponibles sur accessibilite.gouv.fr.

Scannez-moi !

Lien : https://www.info.gouv.fr/accessibilite

### Discours oral exact

Objectifs repris mot pour mot de la fiche catalogue 102846. Présenter les 3 objectifs, insister sur le caractère opérationnel : cette formation débouche sur des gestes concrets, pas seulement de la théorie.

## Slide 03 - Programme de la journée

- Correspondance : PPTX 3, `scripts/slides/02a_sommaire.py`.
- Rôle : donner une vue d'ensemble des quatre modules.
- Famille de mise en page : `checklist_processus`.
- Idée principale : la journée avance du cadre général vers trois terrains de mise en pratique.
- Scène : quatre grandes cartes numérotées disposées en parcours 2 x 2. Chaque carte porte un pictogramme concret : repères juridiques, document bureautique, contrôle d'une page web et publication sociale.
- Transformation : cadre partagé -> documents -> Web -> réseaux sociaux.
- Textes visibles autorisés : `Programme de la journée` ; `1` ; `2` ; `3` ; `4` ; `Accessibilité et cadre légal` ; `Bureautique accessible` ; `PDF` ; `Points de contrôle rapides W3C` ; `Réseaux sociaux` ; `CC`.
- Ce que l'image seule doit faire comprendre : la formation suit quatre modules complémentaires dans un ordre précis.
- Continuité : développe les objectifs et prépare la présentation des intervenants.
- Contraintes critiques : quatre cartes et quatre numéros exactement ; aucun cinquième module ; ordre inchangé ; toutes les formulations viennent du PPTX. Les sous-puces détaillées restent dans l'accordéon. Rejeter tout caractère erroné, texte trop petit ou chevauchement entre les cartes.
- Alternative courte candidate : `Quatre modules organisent la journée, du cadre légal aux réseaux sociaux.`

### Transcription exacte

#### Programme de la journée

1. **Accessibilité et cadre légal**
   - Enjeux et obligations des acteurs publics
   - Déclaration d'accessibilité
2. **Bureautique accessible**
   - Documents Word (LibreOffice)
   - Export PDF accessible
3. **Points de contrôle rapides W3C**
   - 13 vérifications rapides W3C WAI
   - Démonstration et exercice pratique
4. **Réseaux sociaux**
   - Enjeux et obligations
   - Alt text, hashtags, émojis

### Discours oral exact

Présenter les 4 modules, indiquer les horaires approximatifs. Signaler que chaque module se termine par un geste concret.

## Slide 04 - Bertrand Matge - ÉTALON

- Correspondance : PPTX 4, `scripts/slides/02b_intervenant-bertrand.py`.
- Rôle : présenter le premier intervenant et son expérience.
- Famille de mise en page : `synthese_action` - variante portrait authentique.
- Idée principale : Bertrand Matge apporte une expérience de support web, de qualité web et de sensibilisation à l'accessibilité.
- Scène : photographie authentique à gauche dans un cadre simple. À droite, un grand bloc de rôle et quatre repères professionnels accompagnés de pictogrammes sobres. Le fond illustré évoque un atelier de revue de contenus, sans synthétiser ni retoucher le visage.
- Ressource authentique : `_assets/photo-bertrand.jpg`.
- Transformation : personne -> rôle -> expérience utile à la formation.
- Textes visibles autorisés : `Bertrand Matge` ; `Responsable pôle support web - Mission Ingénierie du Web, SG-SNUM` ; `Formateur Opquast certifié, référent Assurance Qualité Web` ; `Forme et sensibilise à l'accessibilité depuis plusieurs années` ; `Passionné par la conception inclusive et l'expérience utilisateur` ; `Formé à l'audit d'accessibilité numérique`.
- Texte interdit dans l'image : l'adresse électronique.
- Ce que l'image seule doit faire comprendre : l'intervenant relie support web, qualité et accessibilité.
- Continuité : ouvre la présentation de l'équipe et prépare le second portrait.
- Contraintes critiques : photographie originale inchangée ; aucun portrait synthétique ; rôle exact ; quatre repères exactement ; aucun courriel visible ; aucun faux logo. Rejeter tout caractère erroné, texte trop petit ou chevauchement avec la photographie.
- Alternative courte candidate : `Portrait de Bertrand Matge avec quatre repères sur son expérience en qualité web et accessibilité.`

### Transcription exacte

#### Bertrand Matge

**Responsable pôle support web - Mission Ingénierie du Web, SG-SNUM**

Alternative de la photographie : Photo Bertrand Matge

- Formateur Opquast certifié, référent Assurance Qualité Web
- Forme et sensibilise à l'accessibilité depuis plusieurs années
- Passionné par la conception inclusive et l'expérience utilisateur
- Formé à l'audit d'accessibilité numérique
- Email : bertrand.matge@finances.gouv.fr

### Discours oral exact

Présentation de Bertrand : parcours SIRCOM, Opquast, sensibilisation accessibilité.

## Slide 05 - Alexandra Guiderdoni

- Correspondance : PPTX 5, `scripts/slides/02c_intervenant-alexandra.py`.
- Rôle : présenter la seconde intervenante et son expérience.
- Famille de mise en page : `synthese_action` - variante portrait authentique.
- Idée principale : Alexandra Guiderdoni relie technologies web, pilotage de projet, audit et formation à l'accessibilité.
- Scène : photographie authentique à gauche, cadrée sans retouche du visage. À droite, un grand bloc de rôle et cinq repères professionnels dans une composition identique à la slide précédente.
- Ressource authentique : `_assets/photo-alexandra.jpg`.
- Transformation : personne -> rôle -> compétences complémentaires.
- Textes visibles autorisés : `Alexandra Guiderdoni` ; `Chef de projet - Mission Ingénierie du Web, SG-SNUM` ; `Spécialisée dans les technologies web et l'accessibilité numérique` ; `Expérience : Ministère des affaires étrangères, ESN` ; `DU-RAN (diplôme universitaire référent accessibilité numérique), 1re session 2024` ; `Formée à l'audit d'accessibilité numérique RGAA` ; `Formatrice et Référente en Assurance Qualité pour le Web - Opquast`.
- Texte interdit dans l'image : l'adresse électronique.
- Ce que l'image seule doit faire comprendre : l'intervenante réunit expérience web, référentiel, audit et pédagogie.
- Continuité : complète la présentation de l'équipe et prépare le tour de table.
- Contraintes critiques : photographie originale inchangée ; même masque que la slide 04 ; cinq repères exactement ; aucun courriel visible ; respecter `1re session 2024`. Rejeter tout caractère erroné, texte trop petit ou chevauchement avec la photographie.
- Alternative courte candidate : `Portrait d'Alexandra Guiderdoni avec cinq repères sur son expérience en technologies web et accessibilité.`

### Transcription exacte

#### Alexandra Guiderdoni

**Chef de projet - Mission Ingénierie du Web, SG-SNUM**

Alternative de la photographie : Photo Alexandra Guiderdoni

- Spécialisée dans les technologies web et l'accessibilité numérique
- Expérience : Ministère des affaires étrangères, ESN
- DU-RAN (diplôme universitaire référent accessibilité numérique), 1re session 2024
- Formée à l'audit d'accessibilité numérique RGAA
- Formatrice et Référente en Assurance Qualité pour le Web - Opquast
- Email : alexandra.guiderdoni@finances.gouv.fr

### Discours oral exact

Présentation d'Alexandra : parcours, spécialisation accessibilité, DU-RAN.

## Slide 06 - Présentez-vous

- Correspondance : PPTX 6, `scripts/slides/02d_tour-de-table.py`.
- Rôle : guider un tour de table court et utile à l'adaptation de la journée.
- Famille de mise en page : `checklist_processus`.
- Idée principale : chaque personne se présente par son rôle, son rapport à l'accessibilité et son attente.
- Scène : trois personnes autour d'une table prennent successivement la parole. Trois grandes cartes au premier plan structurent leur présentation, avec un pictogramme de profil, un curseur de familiarité et une cible.
- Transformation : personnes inconnues -> contexte partagé -> attentes visibles.
- Textes visibles autorisés : `Présentez-vous` ; `Qui êtes-vous ?` ; `Mon rapport à l'accessibilité` ; `Ce que j'attends`.
- Ce que l'image seule doit faire comprendre : le tour de table suit trois questions complémentaires.
- Continuité : passe de la présentation des intervenants à celle du groupe et prépare l'organisation en binômes.
- Contraintes critiques : trois cartes exactement ; aucun texte de réponse inventé ; ne pas afficher les champs entre crochets dans l'image ; conserver le détail complet dans l'accordéon.
- Alternative courte candidate : `Trois questions guident la présentation de chaque participante et participant.`

### Transcription exacte

#### Présentez-vous

##### Qui êtes-vous ?

Bonjour, je m'appelle [prénom]

Je suis [métier / fonction]

chez [direction / service]

depuis [durée]

##### Mon rapport à l'accessibilité

Quand j'entends « accessibilité numérique », je pense à [premier mot]

Je me situe plutôt :

- [ ] Complet débutant
- [ ] J'en ai entendu parler
- [ ] J'ai déjà appliqué quelques règles

##### Ce que j'attends

Je produis principalement [type de contenu]

Pour un usage :

- [ ] Interne
- [ ] Grand public

Ce que j'espère retirer :

J'aimerais [objectif personnel]

### Discours oral exact

Chaque stagiaire suit la grille à voix haute - 2 minutes maxi par personne. Colonne 1 : ancre les métiers présents dans la salle (utile pour choisir les exemples). Colonne 2 : révèle le niveau réel du groupe - adapter le rythme en conséquence. Colonne 3 : noter les attentes au tableau, y revenir en clôture pour montrer qu'elles ont été traitées.

## Slide 07 - Organisation des activités - ÉTALON

- Correspondance : PPTX 7, `scripts/slides/02e_regroupement-binomes.py`.
- Rôle : installer le travail en binôme pour l'activité et encourager l'entraide pendant les ateliers.
- Famille de mise en page : `processus_horizontal` - variante activité en deux scènes.
- Idée principale : le binôme sert d'abord au débat, puis devient une ressource d'apprentissage pendant les ateliers.
- Scène : à gauche, deux personnes piochent une carte et préparent une restitution au groupe. À droite, deux personnes relisent ensemble un document sur un ordinateur. Une flèche discrète relie la première collaboration à la seconde.
- Transformation : rencontre -> échange -> entraide durable.
- Textes visibles autorisés : `Organisation des activités` ; `Activité idées reçues` ; `Pour les ateliers Word et Web` ; `Première étape : trouvez votre binôme et piochez votre carte !`.
- Ce que l'image seule doit faire comprendre : le travail à deux structure l'activité d'ouverture et peut se poursuivre pendant les ateliers.
- Continuité : met en pratique le tour de table et prépare le lancement de l'ice-breaker.
- Contraintes critiques : deux scènes et deux blocs exactement ; aucune obligation de binôme pour Word et Web ; callout exact ; ne pas représenter une compétition.
- Alternative courte candidate : `Un binôme échange sur une carte idée reçue puis relit un document pendant un atelier.`

### Transcription exacte

#### Organisation des activités

##### Activité idées reçues

- Mettez-vous par deux et piochez une carte idée reçue
- Présentez-vous et échangez sur votre quotidien
- Confrontez vos cartes : qu'en pensez-vous ?
- Présentez vos réflexions au groupe - débat ouvert

##### Pour les ateliers Word et Web

- N'hésitez pas à travailler en binôme
- Deux regards repèrent ce qu'un seul ne voit pas
- Expliquer à quelqu'un consolide l'apprentissage

##### Mise en avant

Première étape : trouvez votre binôme et piochez votre carte !

### Discours oral exact

Constituer les binômes en mélangeant les directions si possible - éviter que deux personnes du même bureau soient ensemble (échanges plus riches entre services différents). Si nombre impair : un trinôme. Chaque binôme pioche une carte idée reçue puis prend 2-3 minutes pour se présenter et échanger sur leur quotidien. Ensuite ils confrontent leurs cartes et préparent une courte restitution au groupe. Lancer le débat ouvert après chaque présentation - laisser circuler la parole. Les binômes ne sont pas imposés pour les ateliers Word/Web mais encouragés : insister sur le bénéfice mutuel (relecture croisée, explication = ancrage).

## Slide 08 - Ensemble, faisons tomber les préjugés !

- Correspondance : PPTX 8, `scripts/slides/02f_icebreaker.py`.
- Rôle : lancer le débat vrai ou faux avant les six décryptages.
- Famille de mise en page : `ouverture_illustree` - variante lancement d'activité.
- Idée principale : le groupe formule d'abord ses arguments, puis confronte ses représentations.
- Scène : plusieurs binômes tiennent des cartes carrées, discutent et préparent une prise de parole. Au centre, une grande bulle de question relie les positions sans afficher de réponse correcte.
- Transformation : appréhension -> discussion -> débat ouvert.
- Textes visibles autorisés : `Ensemble, faisons tomber les préjugés !` ; `L'accessibilité numérique, ça fait peur ... mais souvent pour de mauvaises raisons.` ; `Activité : vrai ou faux ?`.
- Ce que l'image seule doit faire comprendre : l'activité commence par un échange argumenté, sans correction immédiate.
- Continuité : active les binômes et prépare la première carte.
- Contraintes critiques : ne pas révéler de réponse ; ne pas remplacer les cartes par des fac-similés Ideance à ce stade ; conserver les trois formulations exactes ; les trois consignes détaillées restent dans l'accordéon.
- Alternative courte candidate : `Des binômes discutent de cartes idées reçues avant un débat avec le groupe.`

### Transcription exacte

#### Ensemble, faisons tomber les préjugés !

##### Accroche

L'accessibilité numérique, ça fait peur ... mais souvent pour de mauvaises raisons.

##### Activité : vrai ou faux ?

- En binôme, confrontez vos cartes : vrai ou faux ?
- Échangez vos arguments, préparez votre position
- Chaque binôme présente sa carte au groupe - débat ouvert

### Discours oral exact

Les cartes ont été piochées au moment de la constitution des binômes. Laisser 2-3 minutes aux binômes pour discuter entre eux de leurs cartes. Puis chaque binôme présente sa carte et dit ce qu'il en pense - le reste du groupe réagit librement. Ne pas corriger immédiatement - laisser le débat s'installer avant d'afficher la slide de décryptage. Objectif : casser les freins avant même de commencer la théorie.

## Règles communes des slides 09 à 14

- Composition : canevas blanc 16:9, titre source en haut à gauche, page recto originale à gauche et page verso originale à droite, de même taille, intégralement visibles.
- Source : paires de pages successives du fichier `livrables-IGPDE-2026-102846/Formateur/ice-breaker-idées-recues-cartes-igpde/6-cartes-idees-recues.pdf`.
- Aucun appel ImageGen : les deux pages sont rendues depuis le PDF source et composées sans retouche de leur contenu.
- Aucun label `Recto` ou `Verso` ajouté dans l'image.
- Le QR code et le lien visible du verso doivent rester nets, lisibles et scannables.
- Rendre chaque page directement depuis le PDF à la résolution nécessaire pour le canevas final. Ne jamais agrandir les PNG diagnostiques de 496 pixels.
- Tester le décodage du QR code sur chacune des six images finales et consigner le résultat dans le reçu.
- L'alternative courte décrit l'idée reçue et la présence du recto et du décryptage, sans recopier tout le verso.

## Slide 09 - Idée reçue 1 / 6 - ÉTALON

- Correspondance : PPTX 9, `scripts/slides/02g_idee-recue-1.py` ; pages PDF 1 et 2.
- Rôle : élargir le public concerné au-delà du handicap permanent.
- Famille de mise en page : `fac_simile_cartes`.
- Idée principale : l'accessibilité concerne une part importante de la population et profite aussi dans des situations temporaires ou contextuelles.
- Scène : recto et verso authentiques de la première carte, côte à côte.
- Textes visibles autorisés : `Idée reçue 1 / 6` et tous les textes déjà présents dans les deux pages originales, sans ajout.
- Ce que l'image seule doit faire comprendre : l'affirmation sur une minorité est confrontée à l'estimation d'une personne sur six.
- Continuité : ouvre la série des six cartes et prépare l'idée reçue sur la créativité.
- Contraintes critiques : pages 1 et 2 uniquement ; conserver l'émoji 🤨 ; aucune correction de la typographie source ; QR et URL intacts.
- Alternative courte candidate : `Recto et verso d'une carte Ideance sur l'idée reçue selon laquelle l'accessibilité ne concernerait qu'une minorité.`

### Transcription exacte

#### Idée reçue 1 / 6

##### Texte visible des cartes

###### Recto

Accessibilité numérique

Cela ne concerne qu’une minorité de personnes 🤨

Idée reçue !

###### Verso

L'OMS (Organisation Mondiale de la Santé) estime que plus d'un milliard de personnes dans le monde vivent avec une forme de handicap significative.

Soit environ 15 % de la population mondiale (1 personne sur 6).

Décryptage complet : [ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

ideance

##### Contenu exact du PPTX

###### Idée reçue

« Ça ne concerne qu'une minorité de personnes »

###### Décryptage

- 1 milliard+ de personnes dans le monde vivent avec un handicap (OMS)
- Soit 15 % de la population mondiale - 1 personne sur 6
- En France : 12 millions de personnes en situation de handicap
- Et chacun sera concerné un jour : âge, accident, maladie temporaire

###### Ressource

Scannez-moi !

[https://ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

### Discours oral exact

Laisser le groupe répondre vrai/faux avant d'afficher le décryptage. Insister : le handicap permanent n'est qu'une fraction. Le handicap temporaire (bras cassé, conjonctivite) et situationnel (plein soleil sur téléphone) touchent tout le monde. Analogie : l'ascenseur est utile aux personnes en fauteuil, aux parents avec poussette, aux livreurs les mains prises. L'accessibilité profite à tous.

## Slide 10 - Idée reçue 2 / 6

- Correspondance : PPTX 10, `scripts/slides/02h_idee-recue-2.py` ; pages PDF 3 et 4.
- Rôle : dissocier accessibilité et appauvrissement du design.
- Famille de mise en page : `fac_simile_cartes`.
- Idée principale : les contraintes d'accessibilité n'interdisent ni la créativité ni une expérience soignée.
- Scène : recto et verso authentiques de la deuxième carte, côte à côte.
- Textes visibles autorisés : `Idée reçue 2 / 6` et tous les textes déjà présents dans les deux pages originales, sans ajout.
- Ce que l'image seule doit faire comprendre : la crainte d'un design dégradé est contredite par le décryptage.
- Continuité : suit l'élargissement du public et prépare l'étendue des exigences.
- Contraintes critiques : pages 3 et 4 uniquement ; conserver l'émoji 🫣 ; QR et URL intacts.
- Alternative courte candidate : `Recto et verso d'une carte Ideance sur l'idée reçue selon laquelle l'accessibilité dégraderait la créativité et l'expérience utilisateur.`

### Transcription exacte

#### Idée reçue 2 / 6

##### Texte visible des cartes

###### Recto

Accessibilité numérique

La créativité et l’UX seront dégradées 🫣

Idée reçue !

###### Verso

L'accessibilité numérique est parfois ressentie comme une contrainte fonctionnelle et esthétique.

Pourtant, en réalité, l'accessibilité numérique n'est aucunement synonyme de design archaïque, austère, minimaliste, sans inspiration…

Décryptage complet : [ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

ideance

##### Contenu exact du PPTX

###### Idée reçue

« La créativité et l'UX seront dégradées »

###### Décryptage

- L'accessibilité n'impose pas un design archaïque, austère ou sans inspiration
- Les contraintes sont des leviers de créativité, pas des freins
- Les interfaces les plus accessibles sont souvent les plus claires et élégantes
- Exemple : le DSFR (Design System de l'État) est à la fois accessible et soigné

###### Ressource

Scannez-moi !

[https://ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

### Discours oral exact

Montrer un contre-exemple si possible : un site très accessible peut être très design. La contrainte de contraste 4,5:1 produit des palettes plus sereines, pas plus laides. Analogie : les normes de sécurité incendie n'ont pas empêché d'architecturer de beaux bâtiments.

## Slide 11 - Idée reçue 3 / 6

- Correspondance : PPTX 11, `scripts/slides/02i_idee-recue-3.py` ; pages PDF 5 et 6.
- Rôle : montrer que l'accessibilité dépasse deux contrôles visibles.
- Famille de mise en page : `fac_simile_cartes`.
- Idée principale : contraste et textes alternatifs ne sont qu'une petite partie d'une chaîne plus large.
- Scène : recto et verso authentiques de la troisième carte, côte à côte.
- Textes visibles autorisés : `Idée reçue 3 / 6` et tous les textes déjà présents dans les deux pages originales, sans ajout.
- Ce que l'image seule doit faire comprendre : deux exigences importantes ne résument pas l'ensemble de l'accessibilité.
- Continuité : approfondit le sujet et prépare la responsabilité partagée.
- Contraintes critiques : pages 5 et 6 uniquement ; conserver l'émoji 😮‍💨 ; QR et URL intacts.
- Alternative courte candidate : `Recto et verso d'une carte Ideance rappelant que l'accessibilité ne se limite pas au contraste et aux descriptions d'images.`

### Transcription exacte

#### Idée reçue 3 / 6

##### Texte visible des cartes

###### Recto

Accessibilité numérique

C’est juste du contraste et des images décrites 😮‍💨

Idée reçue !

###### Verso

Ces sujets sont effectivement fondamentaux. Notamment aux personnes déficientes visuelles.

Toutefois, ces 2 exigences ne représentent qu'une petite partie de l'ensemble des autres règles et bonnes pratiques à suivre.

Décryptage complet : [ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

ideance

##### Contenu exact du PPTX

###### Idée reçue

« C'est juste du contraste et des images décrites »

###### Décryptage

- Le contraste et les textes alternatifs ne sont que 2 exigences sur des centaines
- Le RGAA compte 106 critères, les WCAG 2.1 en comptent 78
- Titres, liens, tableaux, formulaires, langue, ordre de lecture ... autant de dimensions
- L'accessibilité touche toute la chaîne : rédaction, mise en forme, export, publication

###### Ressource

Scannez-moi !

[https://ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

### Discours oral exact

Bonne nouvelle pour les stagiaires : on ne peut pas tout apprendre en 1 jour. L'objectif de cette formation, c'est d'ouvrir les yeux sur l'étendue du sujet et d'acquérir les réflexes sur les points les plus fréquents. Le reste vient avec la pratique et les ressources (RGAA, points de contrôle rapides W3C).

## Slide 12 - Idée reçue 4 / 6

- Correspondance : PPTX 12, `scripts/slides/02j_idee-recue-4.py` ; pages PDF 7 et 8.
- Rôle : installer la responsabilité de chaque producteur de contenu.
- Famille de mise en page : `fac_simile_cartes`.
- Idée principale : l'accessibilité ne peut pas être déléguée à une seule personne ou équipe.
- Scène : recto et verso authentiques de la quatrième carte, côte à côte.
- Textes visibles autorisés : `Idée reçue 4 / 6` et tous les textes déjà présents dans les deux pages originales, sans ajout.
- Ce que l'image seule doit faire comprendre : l'accessibilité est une responsabilité collective.
- Continuité : passe des règles aux responsabilités et prépare la question du coût.
- Contraintes critiques : pages 7 et 8 uniquement ; conserver l'émoji 😑 ; QR et URL intacts.
- Alternative courte candidate : `Recto et verso d'une carte Ideance sur l'idée reçue selon laquelle l'accessibilité ne serait pas du ressort de chacun.`

### Transcription exacte

#### Idée reçue 4 / 6

##### Texte visible des cartes

###### Recto

Accessibilité numérique

Ce n'est pas de mon ressort 😑

Idée reçue !

###### Verso

En réalité, la prise en compte de l’accessibilité dans les projets numériques ne peut et ne doit pas être portée par une seule et unique équipe.

Et encore moins par une seule et unique personne.

Décryptage complet : [ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

ideance

##### Contenu exact du PPTX

###### Idée reçue

« Ce n'est pas de mon ressort »

###### Décryptage

- L'accessibilité ne peut pas être portée par une seule équipe ou une seule personne
- Elle implique tous les producteurs de contenu : rédacteurs, communicants, designers ...
- Chaque document Word, chaque image publiée engage une responsabilité
- La loi de 2005 et la directive européenne 2016/2102 s'appliquent à tous les agents publics

###### Ressource

Scannez-moi !

[https://ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

### Discours oral exact

Cette idée reçue est la plus difficile à déconstruire car elle repose sur une logique réelle : il y a des spécialistes. Répondre : oui, les développeurs et chefs de projet ont leurs responsabilités. Mais vous aussi - c'est précisément pourquoi vous êtes là aujourd'hui. Votre document Word mal structuré empêche un lecteur d'écran de lire. Votre image sans texte alternatif prive un non-voyant de l'information. Personne n'est exempté.

## Slide 13 - Idée reçue 5 / 6

- Correspondance : PPTX 13, `scripts/slides/02k_idee-recue-5.py` ; pages PDF 9 et 10.
- Rôle : montrer que le coût dépend du moment de prise en compte.
- Famille de mise en page : `fac_simile_cartes`.
- Idée principale : intégrer l'accessibilité dès le départ évite une correction tardive coûteuse.
- Scène : recto et verso authentiques de la cinquième carte, côte à côte.
- Textes visibles autorisés : `Idée reçue 5 / 6` et tous les textes déjà présents dans les deux pages originales, sans ajout.
- Ce que l'image seule doit faire comprendre : la charge augmente surtout quand l'accessibilité est traitée en fin de projet.
- Continuité : relie responsabilité et anticipation, puis prépare la dernière idée reçue.
- Contraintes critiques : pages 9 et 10 uniquement ; conserver l'émoji 😞 ; QR et URL intacts.
- Alternative courte candidate : `Recto et verso d'une carte Ideance sur l'idée reçue selon laquelle l'accessibilité coûterait trop cher.`

### Transcription exacte

#### Idée reçue 5 / 6

##### Texte visible des cartes

###### Recto

Accessibilité numérique

Ça coûte trop cher 😞

Idée reçue !

###### Verso

Effectivement, l’accessibilité numérique peut engendrer une charge financière conséquente.

Mais essentiellement lorsqu’elle est traitée comme un simple ajustement en fin de projet.

Décryptage complet : [ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

ideance

##### Contenu exact du PPTX

###### Idée reçue

« Ça coûte trop cher »

###### Décryptage

- Oui - si l'accessibilité est traitée comme un ajustement en fin de projet
- Non - si elle est intégrée dès la conception (approche « shift left »)
- Corriger un document Word après publication : 10 fois plus cher que le faire d'emblée
- Les réflexes appris aujourd'hui ne coûtent rien : juste un changement d'habitude

###### Ressource

Scannez-moi !

[https://ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

### Discours oral exact

Analogie bâtiment : une rampe d'accès intégrée dès la construction coûte quelques centaines d'euros. La reprise après construction, plusieurs milliers. Pour les documents : appliquer les styles Titre dans Word, c'est 30 secondes de plus. Corriger un PDF de 50 pages après coup, c'est des heures. L'accessibilité est rentable quand elle est intégrée - c'est le message central.

## Slide 14 - Idée reçue 6 / 6

- Correspondance : PPTX 14, `scripts/slides/02l_idee-recue-6.py` ; pages PDF 11 et 12.
- Rôle : conclure l'ice-breaker et faire la transition vers les premiers réflexes.
- Famille de mise en page : `fac_simile_cartes`.
- Idée principale : remettre l'accessibilité à la fin conduit à des corrections lourdes, nuit à l'efficacité du projet et génère de la frustration.
- Scène : recto et verso authentiques de la sixième carte, côte à côte.
- Textes visibles autorisés : `Idée reçue 6 / 6` et tous les textes déjà présents dans les deux pages originales, sans ajout.
- Ce que l'image seule doit faire comprendre : une prise en compte tardive entraîne de grosses corrections et de la frustration pour les équipes.
- Continuité : clôt la Partie 0 et prépare la Partie I, sans intégrer la slide PPTX 15.
- Contraintes critiques : pages 11 et 12 uniquement ; conserver l'émoji 🙂 ; QR et URL intacts ; aucune slide de transition supplémentaire.
- Alternative courte candidate : `Recto et verso d'une carte Ideance sur l'idée reçue selon laquelle l'accessibilité pourrait être traitée à la fin.`

### Transcription exacte

#### Idée reçue 6 / 6

##### Texte visible des cartes

###### Recto

Accessibilité numérique

On s’en occupe à la fin ! 🙂

Idée reçue !

###### Verso

Quand ce sujet est pris en compte trop tard, cela entraîne souvent de grosses corrections après coup.

Cela pèse sur l’efficacité des projets et peut générer de la frustration pour les équipes.

Décryptage complet : [ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

ideance

##### Contenu exact du PPTX

###### Idée reçue

« On s'en occupe à la fin ! »

###### Décryptage

- Prise en compte tardive = grosses corrections après coup
- Cela pèse sur l'efficacité des projets et génère de la frustration pour les équipes
- L'accessibilité « à la fin » est souvent l'accessibilité jamais faite
- Solution : intégrer les bons réflexes à chaque étape, pas les accumuler en sprint final

###### Ressource

Scannez-moi !

[https://ideance.net/blog/4602/idees-recues-a11y](https://ideance.net/blog/4602/idees-recues-a11y)

### Discours oral exact

Dernière idée reçue - transition naturelle vers la journée : « Aujourd'hui, on ne remet pas à la fin. On commence par les bons réflexes et on les ancre maintenant. » Demander au groupe : laquelle de ces 6 idées reçues vous parlait le plus ce matin ? Cette question fait le lien entre l'icebreaker et la suite du programme.

## Relecture indépendante

- Première relecture : 0 P0, 5 P1 et 4 P2, tous corrigés avant la production des étalons.
- Relecture consolidée après production des 14 visuels : `VALIDÉ SOUS RÉSERVE`, avec 0 P0, 2 P1 et 8 P2 documentaires.
- Réserves corrigées avant l'intégration HTML : état d'avancement, contenu exact des QR codes, libellés réels `Idée reçue` et `Décryptage`, URL du PPTX, alternatives des photographies, sous-titres `Recto` et `Verso`, marque Ideance, liste des textes réellement visibles sur la slide 03 et formulation de la slide 14.
- Étalons maintenus et validés : 01, 04, 07 et 09. La slide 07 relève de `processus_horizontal`, ce qui distingue l'ouverture, le portrait, le processus d'activité et le fac-similé.

## Vérifications internes après relecture indépendante

- 14 correspondances continues : PPTX 1 à 14, sans slide 15.
- 14 titres sources présents.
- 14 transcriptions structurées présentes.
- 14 discours oraux exacts présents.
- 14 alternatives courtes candidates présentes.
- Huit visuels produits à partir d'ImageGen, dont trois enrichis par composition de ressources authentiques, et six compositions fac-similées produites.
- Quatre étalons validés : 01, 04, 07 et 09.
- Les photographies, l'affiche, les QR codes, les URL et les cartes restent authentiques.
- Les courriels figurent dans les transcriptions des slides 04 et 05, jamais dans les textes visibles des images.
- L'intégration HTML locale est autorisée. La publication, le commit et le push restent des étapes séparées.

## Étape de livraison

- Les 14 visuels, leurs prompts, leur reçu et la planche-contact constituent le lot source de la variante `introduction-et-idees-recues`.
- `slides.json` doit reprendre les 14 transcriptions et les 14 discours oraux dans deux accordéons distincts.
- La publication sur l'accueil, le commit et le push nécessitent une étape de livraison séparée après validation locale.
