# Partie II - Documents bureautiques accessibles - TP

## Statut du document

- Storyboard de conception des 27 visuels web correspondant, dans le même ordre, aux diapositives PPTX 54 à 80 du support IGPDE 102846.
- Source opposable : livrables-IGPDE-2026-102846/Formateur/support-formation-102846-2026-IGPDE.pptx dans le dépôt usine-fabrication-igpde-102846-ay11 ; les fichiers scripts/slides/ indiqués par fiche permettent de retrouver la source de génération.
- Titre public : « Partie II - Documents bureautiques accessibles - TP ».
- Slug prévu : partie-2-documents-bureautiques-accessibles.
- Numérotation web : 01 à 27. Les numéros PPTX restent dans la traçabilité, sans être ajoutés aux images.
- État au 3 octobre 2026 : storyboard rédigé, quatre étalons acceptés, 27 visuels produits ; intégration web et publication demandées.

## Diagnostic pédagogique

- Public : communicantes et communicants, sans prérequis technique.
- Mission : rendre accessible en binôme le guide de Sami, puis remettre un DOCX corrigé, une checklist renseignée et un PDF exporté et contrôlé.
- Parcours : accroche par le lecteur d'écran et le quiz A/B, mission de 90 minutes, cinq stations de manipulation et de preuve, trois pages de checklist, synthèse de la matinée.
- Idée pivot : l'apparence du document ne suffit pas ; sa structure, son sens et ses propriétés doivent être vérifiables.
- Charge cognitive : les images montrent une action ou une comparaison concrète ; les deux accordéons conservent le contenu de chaque diapositive et les notes du formateur.

## Contrat visuel et éditorial

- Référence : preset local « IGPDE Accessibilité - bleu illustré » dans _source/imagegen-igpde/ du dépôt source ; références d'ouverture, de comparaison, de tableau et de checklist inspectées.
- Image finale visée : paysage 16:9, 1672 x 941 pixels, fond blanc lumineux, titre bleu nuit aligné à gauche, illustration semi-plate concrète, cartes bleu clair sobres, marges généreuses et aucun pied de page dans l'image.
- Palette fonctionnelle : bleu nuit #000091 ; bleu d'action #2B6DE8 ; bleu clair #E3EEFF ; gris bleuté #D7E1F0 ; vert #00A95F pour une validation ; rouge #E1000F pour un problème.
- Typographie visée : Marianne, avec Arial comme seul repli. Texte français accentué, lisible en miniature.
- Progression : cinq stations représentées dans les scènes ; repère de numéro web fourni par l'interface, sans recopier les numéros PPTX.
- Les six familles du preset servent de vocabulaire : ouverture illustrée, comparaison ou transformation, processus horizontal, tableau pédagogique, checklist ou processus et synthèse d'action.
- Les titres des images reprennent exactement les titres du PPTX. Les autres textes visibles sont limités à la liste blanche de chaque fiche et proviennent de la même diapositive.
- Les identifiants P, C et S apparaissent dans les vues de station et les checklists. Sur les procédures détaillées, ils restent dans la transcription.
- Les images du quiz A et B de la diapositive PPTX 56 sont conservées à l'identique et intégrées dans la composition finale. Elles sont identiques octet pour octet ; ImageGen ne doit pas les redessiner.
- Aucun faux logo, emblème, pictogramme ambigu, pseudo-texte, photographie synthétique, texte minuscule ou règle métier inventée.

## Règles des deux accordéons

- « Transcription » : titre source, surtitre pédagogique sous forme de paragraphe, puis tout le contenu visible dans son ordre logique. Les tableaux sources gardent leurs en-têtes et leurs lignes ; le futur HTML emploiera de vrais tableaux avec légende et en-têtes.
- « Lire le discours oral » : texte des notes du PPTX repris sans créer de nouveau cours et sans retirer les consignes au formateur. Les retours de ligne peuvent devenir paragraphes ou listes sémantiques.
- Éléments de masque exclus : date du 9 octobre 2026, numéro de page et pied récurrent « Formation 102846 / ... ». Le surtitre propre à la diapositive reste transcrit.
- Les chemins de menus Word et Writer, noms de fichiers, ratios, formulations de preuves et codes de contrôle restent fidèles à la source. Une éventuelle correction de fond devra être décidée et tracée séparément.
- Les alternatives courtes candidates décrivent l'information principale du nouveau visuel ; elles seront relues contre les images finales avant intégration dans slides.json.

## Colonne vertébrale

1. Faire entendre la barrière créée par un document sans structure et révéler la différence entre apparence et accessibilité.
2. Confier une mission concrète autour du guide de Sami.
3. Parcourir cinq stations : structure, sens, couleurs et données, langue et lisibilité, contrôle et export.
4. Relier chaque manipulation à une preuve et à la checklist.
5. Conclure sur le transfert de ces réflexes vers les prochains documents et vers le Web.

## Points de vigilance

- Les pourcentages et l'attribution « OMS 2024 » des diapositives 55 et 58 sont transcrits comme contenu source ; leur exactitude externe n'a pas été vérifiée dans ce storyboard.
- Le préambule annoncé à 5 minutes et les cinq minutages de station (17, 15, 15, 15 et 18 minutes) totalisent 85 minutes, alors que le TP est annoncé à 90 minutes. Ne pas combler les 5 minutes par une consigne inventée.
- La diapositive 80 est une synthèse de 15 minutes hors des 90 minutes du TP et appartient néanmoins à la séquence demandée.
- Les contrôles S-01 à S-05 sont signalés sur la checklist ; les notes précisent qu'ils ne constituent pas des manipulations obligatoires du TP.
- L'absence d'erreur dans le vérificateur Word et un rapport PAC ne valent pas, à eux seuls, preuve de conformité.

## Slide web 01 - Partie II - Documents bureautiques accessibles - TP - ÉTALON

- Correspondance : PPTX 54 ; scripts/slides/03_chapitre-word.py.
- Rôle : ouvrir la partie et annoncer les cinq stations.
- Famille : ouverture illustrée.
- Idée principale : la formation passe du cadre général à la correction d'un document de Sami par étapes.
- Scène : le guide de Sami est posé au centre d'un poste de travail ; cinq repères successifs montrent structure, contenus, couleurs et données, langue, puis vérification et export.
- Transformation : document à examiner -> cinq stations -> document contrôlé.
- Liste blanche du visuel : « Partie II - Documents bureautiques accessibles - TP » ; « Structurer et naviguer » ; « Rendre les contenus et les liens compréhensibles » ; « Sécuriser couleurs, graphiques et tableaux » ; « Régler langues et lisibilité » ; « Finaliser, vérifier, exporter et contrôler ».
- Image seule : un TP sur document progresse par cinq gestes de correction et de contrôle.
- Continuité : reprend la formation générale et prépare l'expérience du lecteur d'écran.
- Contraintes critiques : cinq étapes dans cet ordre ; aucun numéro PPTX ; pas de faux logo ni de texte ajouté.
- Alternative courte candidate : « Cinq stations guident la correction et le contrôle du document de Sami. »

### Transcription exacte

#### Partie II - Documents bureautiques accessibles - TP

Partie II | Plan

1. Structurer et naviguer
2. Rendre les contenus et les liens compréhensibles
3. Sécuriser couleurs, graphiques et tableaux
4. Régler langues et lisibilité
5. Finaliser, vérifier, exporter et contrôler

### Discours oral exact

Annoncer un TP guidé de 90 minutes organisé en 5 stations.
La théorie, la manipulation et la preuve avancent ensemble dans le document de Sami.

## Slide web 02 - Le lecteur d'écran en action

- Correspondance : PPTX 55 ; scripts/slides/04_ouverture-lecteur-ecran.py.
- Rôle : faire éprouver la perte de repères d'un document non structuré.
- Famille : comparaison ou transformation, avec la lecture linéaire problématique comme état dominant.
- Idée principale : sans titres ni repères, la lecture devient longue et la navigation impossible.
- Scène : une personne écoute son lecteur d'écran devant une page dont les lignes se succèdent sans ancrage ; les repères de section manquent visiblement.
- Transformation : document apparemment ordinaire -> restitution linéaire -> difficulté à rejoindre la section utile.
- Liste blanche du visuel : « Le lecteur d'écran en action » ; « Ce qu’entend le lecteur d’écran » ; « Texte, texte, texte, texte, texte, texte ... » ; « Pendant 4 minutes. Sans titre. Sans repère. » ; « 15 % de vos destinataires sont concernés ».
- Image seule : le défaut de structure produit une barrière de navigation.
- Continuité : crée le besoin que le quiz A/B rendra moins visible à l'écran.
- Contraintes critiques : ne pas représenter le handicap par un stéréotype ; ne pas transformer les pourcentages source en données vérifiées ; pas de solution technique anticipée.
- Alternative courte candidate : « Un lecteur d'écran parcourt une longue page sans titres ni repères. »

### Transcription exacte

#### Le lecteur d'écran en action

2. Documents accessibles | Ouverture

##### Ce qu’entend le lecteur d’écran

Texte, texte, texte, texte, texte, texte ...

Pendant 4 minutes. Sans titre. Sans repère.
Sans pouvoir naviguer vers la section qui le concerne.

-> C'est ce qu'entend une personne malvoyante face à votre document Word.

**15 % de vos destinataires sont concernés**

- 80 % de ces handicaps sont invisibles
- Dans une réunion de 12 personnes : au moins 1 daltonien
- Parmi 30 destinataires : 4 ou 5 ont un handicap

### Discours oral exact

Lire la citation à voix haute, lentement, avec des pauses.
Ne pas commenter.
Laisser le silence s'installer 5 secondes.
Demander : est-ce que vous avez déjà reçu un document ou un email illisible ?
Cette personne vivait ça tous les jours.

## Slide web 03 - Quiz - lequel de ces deux documents est accessible ? - ÉTALON

- Correspondance : PPTX 56 ; scripts/slides/05_quiz-flash-a-vs-b.py.
- Rôle : demander une hypothèse avant de révéler la différence structurelle.
- Famille : comparaison ou transformation, variante quiz à deux colonnes.
- Idée principale : deux documents visuellement identiques ne sont pas forcément équivalents pour un lecteur d'écran.
- Scène : deux aperçus de document côte à côte, parfaitement identiques, sous les libellés A et B. Le fond et les repères de question sont créés avec ImageGen ; les deux PNG sources sont intégrés à l'identique après génération.
- Transformation : observation visuelle identique -> doute -> question sur la structure invisible.
- Liste blanche du visuel : « Quiz - lequel de ces deux documents est accessible ? » ; « Ils sont visuellement identiques. Lequel préférez-vous pour NVDA ? » ; « Document A » ; « Document B ».
- Image seule : l'apparence ne permet pas de choisir le document accessible.
- Continuité : pose la question dont la slide 04 donnera la réponse.
- Contraintes critiques : conserver les fichiers scripts/images/quiz-document-a-dsfr.png et scripts/images/quiz-document-b-dsfr.png ; ne générer aucun texte à l'intérieur des aperçus ; ne pas signaler B comme gagnant avant la slide suivante ; garder une taille et une position symétriques.
- Alternative courte candidate : « Deux aperçus de documents identiques sont proposés au choix. »

### Transcription exacte

#### Quiz - lequel de ces deux documents est accessible ?

2. Documents accessibles | Quiz flash

Ils sont visuellement identiques. Lequel préférez-vous pour NVDA ?

- Document A
- Document B

### Discours oral exact

Laisser 30 secondes pour que chacun vote.
Demander à main levée.
Ne pas donner la réponse maintenant - la curiosité crée l'attention.
Zeigarnik : la boucle ouverte maintient l'engagement.

## Slide web 04 - Réponse - le document B est accessible

- Correspondance : PPTX 57 ; scripts/slides/05a_quiz-flash-reponse.py.
- Rôle : révéler que la différence se situe dans le fichier, pas dans son rendu.
- Famille : comparaison ou transformation.
- Idée principale : les styles de titre, l'alternative d'image et le nom du fichier changent ce que NVDA peut restituer.
- Scène : les deux documents conservent la même silhouette ; une coupe sous chaque page montre à gauche une structure absente, à droite trois propriétés identifiables.
- Transformation : apparence identique -> propriétés distinctes -> document B accessible.
- Liste blanche du visuel : « Réponse - le document B est accessible » ; « Document A » ; « Document B » ; « Titres mis en gras, police Arial 16 » ; `Titres avec le style « Titre 1 »` ; « Image sans description » ; « Image avec texte alternatif » ; « La structure du fichier détermine ce que NVDA peut restituer. »
- Image seule : deux fichiers visuellement identiques n'offrent pas la même navigation et la même description.
- Continuité : résout le quiz et prépare les gestes accessibles dans Word.
- Contraintes critiques : ne pas déplacer les caractéristiques de A vers B ; ne pas représenter la vérification Word comme preuve finale ; conserver la réponse hors du visuel précédent.
- Alternative courte candidate : « Le document B possède des titres structurés et une image décrite, contrairement à A. »

### Transcription exacte

#### Réponse - le document B est accessible

2. Documents accessibles | Quiz flash

À l'écran, rien ne les distingue. La différence se trouve dans la structure du fichier.

##### Document A

- Titres mis en gras, police Arial 16
- Image sans description
- Fichier nommé Document1.docx

##### Document B

- Titres avec le style « Titre 1 »
- Image avec texte alternatif
- Fichier nommé rapport-bilan-2024.docx

La structure du fichier détermine ce que NVDA peut restituer.

### Discours oral exact

Donner la réponse : le document B.
Expliquer que les deux documents peuvent être identiques à l'écran, mais que NVDA dépend des styles de titres, des textes alternatifs et d'un nom de fichier explicite.

## Slide web 05 - Pourquoi ça vous concerne ?

- Correspondance : PPTX 58 ; scripts/slides/06_pourquoi-concerne.py.
- Rôle : relier le quiz aux pratiques des participantes et participants.
- Famille : synthèse d'action.
- Idée principale : les gestes dans le ruban Word suffisent à commencer une correction vérifiable.
- Scène : une communicante ouvre le ruban Word ; trois grands repères associent personnes concernées, handicaps invisibles et absence de code, puis pointent vers la structure du document.
- Transformation : « cela ne me concerne pas » -> gestes disponibles -> preuve manipulable.
- Liste blanche du visuel : « Pourquoi ça vous concerne ? » ; « 15 % » ; « de vos destinataires sont concernés par un handicap » ; « 80 % » ; « de ces handicaps sont invisibles - rien ne le montre » ; « 0 ligne » ; « de code nécessaire - uniquement des réflexes dans le ruban Word » ; « L'accessibilité ne se voit pas : elle se manipule et se vérifie ».
- Image seule : un document accessible repose sur des gestes concrets accessibles aux communicants.
- Continuité : transforme la découverte du quiz en mission de correction.
- Contraintes critiques : chiffres repris comme contenu source, sans source inventée ; ne pas confondre invisibilité d'un handicap et absence de besoin ; ne pas faire du nom de fichier une preuve suffisante.
- Alternative courte candidate : « Trois repères relient les besoins des destinataires aux gestes possibles dans Word. »

### Transcription exacte

#### Pourquoi ça vous concerne ?

2. Documents accessibles

**15 %** de vos destinataires sont concernés par un handicap

**80 %** de ces handicaps sont invisibles - rien ne le montre

**0 ligne** de code nécessaire - uniquement des réflexes dans le ruban Word

##### L'accessibilité ne se voit pas : elle se manipule et se vérifie

- Le style Titre 1 crée une structure de navigation
- Le texte de remplacement décrit la fonction de l'image
- Le nom de fichier permet de retrouver le document

### Discours oral exact

Faire formuler le message : l'accessibilité ne se voit pas, elle se manipule et se vérifie.
Revenir sur les propriétés qui distinguent les deux documents. 15 % = moyenne nationale Source : OMS 2024.
Le chiffre 0 ligne de code est le déclencheur de confiance : tout le monde peut le faire.

## Slide web 06 - Votre mission : rendre accessible le guide de Sami

- Correspondance : PPTX 59 ; scripts/slides/07_5-piliers-vue-ensemble.py.
- Rôle : donner le point de départ, la durée et les livrables du TP.
- Famille : checklist ou processus.
- Idée principale : chaque binôme corrige un document, renseigne sa checklist et contrôle un PDF.
- Scène : un binôme prend un DOCX de départ ; trois objets successifs représentent le fichier corrigé, la checklist et le PDF contrôlé.
- Transformation : document de départ -> cinq stations -> trois productions.
- Liste blanche du visuel : « Votre mission : rendre accessible le guide de Sami » ; « Point de départ » ; « 5 stations en 90 minutes » ; « Productions à remettre » ; « Le DOCX corrigé par votre binôme » ; « La checklist renseignée au fil des stations » ; « Le PDF exporté puis contrôlé ».
- Image seule : un exercice guidé produit un document corrigé et ses preuves.
- Continuité : donne le document qui sera manipulé dans les cinq stations.
- Contraintes critiques : ne pas révéler le corrigé ; distinguer le DOCX avec pistes conseillé de la variante autonome ; ne pas faire de la checklist une simple conclusion finale.
- Alternative courte candidate : « Un binôme corrige le guide de Sami et remet DOCX, checklist et PDF contrôlé. »

### Transcription exacte

#### Votre mission : rendre accessible le guide de Sami

2. Documents accessibles | Préambule

##### Point de départ

- Conseillé : tp-doc-aide-correction.docx
- Variante autonome : tp-doc-inaccessible.docx
- 5 stations en 90 minutes

##### Productions à remettre

- Le DOCX corrigé par votre binôme
- La checklist renseignée au fil des stations
- Le PDF exporté puis contrôlé

Checklist dès le départ ; cartes WCAG reliées informellement à chaque contrôle.

### Discours oral exact

Préambule limité à 5 minutes, quiz compris.
Distribuer la checklist et les cartes WCAG, puis proposer le DOCX avec pistes comme point de départ conseillé.
Le DOCX inaccessible constitue la variante autonome.
Ne pas révéler le corrigé avant la remise finale.

## Slide web 07 - Station 1 - Structurer et naviguer

- Correspondance : PPTX 60 ; scripts/slides/08_pilier1-styles-titre.py.
- Rôle : donner la carte des cinq contrôles de structure.
- Famille : tableau pédagogique.
- Idée principale : titres, sommaire, listes et mise en page doivent créer une navigation réelle.
- Scène : le guide de Sami ouvert affiche un plan navigable ; cinq repères P-01 à P-05 convergent vers le volet et le sommaire.
- Transformation : texte visuellement mis en forme -> structure vérifiable -> navigation.
- Liste blanche du visuel : « Station 1 - Structurer et naviguer » ; « P-01 » ; « P-02 » ; « P-03 » ; « P-04 » ; « P-05 » ; « Manipuler la structure, puis prouver le résultat dans le volet et le sommaire. »
- Image seule : les cinq contrôles agissent sur la structure du document.
- Continuité : ouvre la première station et prépare le geste sur les titres.
- Contraintes critiques : cinq codes exacts et dans l'ordre ; ne pas suggérer qu'un titre gras suffit ; conserver le tableau intégral dans la transcription.
- Alternative courte candidate : « Cinq contrôles relient titres, sommaire, listes et mise en page à la navigation. »

### Transcription exacte

#### Station 1 - Structurer et naviguer

2. Documents accessibles | Station 1

##### Tableau : ID, Niveau, Points travaillés

- P-01 | P | Distinguer le titre principal des titres hiérarchiques
- P-02 | P | Construire une hiérarchie de titres cohérente
- P-03 | P | Naviguer et générer un sommaire automatique
- P-04 | P | Utiliser des listes natives
- P-05 | P | Employer les fonctions de mise en page adaptées

Manipuler la structure, puis prouver le résultat dans le volet et le sommaire.

### Discours oral exact

Minutage de la station : 17 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-01, P-02, P-03, P-04, P-05.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire distinguer le rôle du texte de son apparence avant d'ouvrir le ruban.
Question de synthèse : Comment prouver que le document est réellement navigable ?
Preuves attendues :
P-01 : Styles vérifiables dans le DOCX et structure lisible dans le volet de navigation.
P-02 : Ordre des niveaux contrôlé dans le XML et confirmé dans le volet de navigation.
P-03 : Navigation cohérente et sommaire actualisable après modification d'un titre.
P-04 : Structure de liste présente dans le DOCX et annoncée comme liste.
P-05 : Absence des artifices ciblés dans le XML et contrôle visuel avec marques affichées.

## Slide web 08 - Station 1 - Titres, hiérarchie et sommaire

- Correspondance : PPTX 61 ; scripts/slides/09_pilier1-listes.py.
- Rôle : expliquer les manipulations de titres et de sommaire dans Word et Writer.
- Famille : processus horizontal.
- Idée principale : appliquer les styles, vérifier le plan, puis générer un sommaire actualisable.
- Scène : le guide de Sami passe de sections visuellement marquées à un volet de navigation ordonné et à une table des matières liée.
- Transformation : apparence de titre -> niveau de titre -> navigation et sommaire.
- Liste blanche du visuel : « Station 1 - Titres, hiérarchie et sommaire » ; « Accueil > Styles » ; « Affichage > Volet de navigation » ; « Références > Table des matières > Table automatique » ; « Dans Writer - complément ».
- Image seule : le plan du document se construit par les styles et se contrôle dans la navigation.
- Continuité : détaille P-01 à P-03 de la station 1, puis laisse place aux listes et à la mise en page.
- Contraintes critiques : distinguer le titre principal et les niveaux de section ; ne pas représenter la table des matières comme une simple liste saisie ; garder les chemins complets dans la transcription.
- Alternative courte candidate : « Les styles de titre alimentent le volet de navigation et le sommaire. »

### Transcription exacte

#### Station 1 - Titres, hiérarchie et sommaire

2. Documents accessibles | Station 1

##### Dans Word - procédure principale

- P-01 - Accueil > Styles, puis appliquer Titre au titre principal et les niveaux de titre aux sections.
- P-02 - Affichage > Volet de navigation, puis corriger les styles depuis Accueil > Styles.
- P-03 - Références > Table des matières > Table automatique, puis clic droit > Mettre à jour les champs.

##### Dans Writer - complément

- P-01 - Styles > Gérer les styles, puis appliquer Titre et Titre 1 à Titre 3 selon le niveau.
- P-02 - Affichage > Navigateur, puis corriger les styles depuis Styles > Gérer les styles.
- P-03 - Insertion > Table des matières et index > Table des matières, index ou bibliographie.

### Discours oral exact

Minutage de la station : 17 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-01, P-02, P-03.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire ouvrir le volet avant de corriger les styles et rappeler que le sommaire en découle.
Question de synthèse : Le volet et le sommaire racontent-ils le même plan ?
Preuves attendues :
P-01 : Styles vérifiables dans le DOCX et structure lisible dans le volet de navigation.
P-02 : Ordre des niveaux contrôlé dans le XML et confirmé dans le volet de navigation.
P-03 : Navigation cohérente et sommaire actualisable après modification d'un titre.

## Slide web 09 - Station 1 - Listes et mise en page robuste

- Correspondance : PPTX 62 ; scripts/slides/10_pilier1-tableaux-flottants.py.
- Rôle : traiter les listes natives et les artifices de mise en page.
- Famille : comparaison ou transformation.
- Idée principale : les fonctions de liste et de mise en page résistent mieux qu'un alignement simulé par des caractères.
- Scène : des paragraphes du guide affichent les marques de formatage ; les espaces et paragraphes vides cèdent la place à des puces natives, des sauts et des colonnes réglés.
- Transformation : mise en page fragile -> marques visibles -> fonctions appropriées.
- Liste blanche du visuel : « Station 1 - Listes et mise en page robuste » ; « Accueil > Puces ou Numérotation » ; « Accueil > Afficher tout » ; « Manipulation : afficher les marques, corriger les artifices, puis vérifier la structure. »
- Image seule : afficher les marques révèle les faux alignements et oriente leur correction.
- Continuité : termine la structure avant de passer au sens des images et des liens.
- Contraintes critiques : ne pas afficher une liste de caractères typographiques comme une vraie liste ; le tableau source ne demande pas de nouveau contrôle.
- Alternative courte candidate : « Les marques révèlent les artifices ; listes et mise en page natives les remplacent. »

### Transcription exacte

#### Station 1 - Listes et mise en page robuste

2. Documents accessibles | Station 1

##### Dans Word - procédure principale

- P-04 - Sélectionner les paragraphes, puis Accueil > Puces ou Numérotation.
- P-05 - Accueil > Afficher tout, puis régler Paragraphe, Mise en page > Sauts et Mise en page > Colonnes.

##### Dans Writer - complément

- P-04 - Sélectionner les paragraphes, puis Format > Puces et numérotation.
- P-05 - Affichage > Marques de formatage, puis Format > Paragraphe et Format > Style de page.

Manipulation : afficher les marques, corriger les artifices, puis vérifier la structure.

### Discours oral exact

Minutage de la station : 17 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-04, P-05.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire activer les marques avant toute correction et traiter les artifices dans leur ordre d'apparition.
Question de synthèse : Les listes sont-elles annoncées comme telles et la mise en page résiste-t-elle aux marques affichées ?
Preuves attendues :
P-04 : Structure de liste présente dans le DOCX et annoncée comme liste.
P-05 : Absence des artifices ciblés dans le XML et contrôle visuel avec marques affichées.

## Slide web 10 - Station 2 - Rendre les contenus et les liens compréhensibles

- Correspondance : PPTX 63 ; scripts/slides/11_pilier2-contraste.py.
- Rôle : présenter les six contrôles de sens et d'accès au contenu.
- Famille : tableau pédagogique.
- Idée principale : chaque type de contenu appelle un traitement adapté et l'information doit survivre à la perte de son contexte visuel.
- Scène : autour du guide de Sami, six repères P-06 à P-11 pointent vers images, texte, lien et en-tête sans afficher de nouveau jargon.
- Transformation : contenu perçu visuellement -> traitement selon sa fonction -> sens conservé.
- Liste blanche du visuel : « Station 2 - Rendre les contenus et les liens compréhensibles » ; « P-06 » ; « P-07 » ; « P-08 » ; « P-09 » ; « P-10 » ; « P-11 » ; « Choisir le traitement selon l'usage : informative, complexe, décorative ou textuelle. »
- Image seule : les six contrôles de la station rendent les contenus compréhensibles hors du seul visuel.
- Continuité : passe de la structure au sens ; la slide suivante distingue trois rôles d'image.
- Contraintes critiques : six codes exacts et dans l'ordre ; aucune image décorative ne doit porter une information essentielle ; tableau complet réservé à la transcription.
- Alternative courte candidate : « Six contrôles portent sur images, vrai texte, liens et information d'en-tête. »

### Transcription exacte

#### Station 2 - Rendre les contenus et les liens compréhensibles

2. Documents accessibles | Station 2

##### Tableau : ID, Niveau, Points travaillés

- P-06 | P | Rédiger l'alternative d'une image informative simple
- P-07 | P | Décrire une image complexe
- P-08 | P | Marquer une image redondante comme décorative
- P-09 | P | Remplacer une image de texte par du vrai texte
- P-10 | P | Rendre les liens autonomes et identifiables
- P-11 | P | Reprendre dans le corps l'information d'un en-tête

Choisir le traitement selon l'usage : informative, complexe, décorative ou textuelle.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-06, P-07, P-08, P-09, P-10, P-11.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire identifier la fonction de chaque contenu avant d'ouvrir le volet du texte alternatif.
Question de synthèse : L'information reste-t-elle compréhensible si l'image ou le contexte disparaît ?
Preuves attendues :
P-06 : Alternative présente dans le DOCX et jugée pertinente par lecture humaine.
P-07 : Équivalence d'information vérifiée sans consulter l'image.
P-08 : Marqueur décoratif ou équivalent vérifié et absence de perte d'information confirmée.
P-09 : Texte sélectionnable présent dans le DOCX et image de texte absente.
P-10 : Destination inchangée, libellé explicite et identification visuelle vérifiées.
P-11 : Statut compréhensible dans le texte linéarisé sans en-tête ni arrière-plan.

## Slide web 11 - Station 2 - Choisir le bon traitement pour chaque image - ÉTALON

- Correspondance : PPTX 64 ; scripts/slides/12_pilier2-couleur-seule.py.
- Rôle : montrer le choix entre alternative simple, description détaillée et image décorative.
- Famille : comparaison ou transformation à trois cas.
- Idée principale : le traitement d'une image dépend de l'information qu'elle apporte.
- Scène : trois images intégrées dans le guide de Sami sont examinées par une communicante ; l'une reçoit un texte de remplacement, la deuxième une description voisine, la troisième est marquée comme décorative après vérification de sa redondance.
- Transformation : regarder l'image -> déterminer sa fonction -> choisir un traitement proportionné.
- Liste blanche du visuel : « Station 2 - Choisir le bon traitement pour chaque image » ; « texte de remplacement » ; « description détaillée » ; « Marquer comme décoratif » ; « Dans Writer - complément ».
- Image seule : trois fonctions d'image conduisent à trois traitements distincts.
- Continuité : développe P-06 à P-08, puis prépare l'image de texte et les liens.
- Contraintes critiques : ne pas laisser croire qu'une image complexe se résume au texte alternatif ; l'image décorative doit être redondante ; les chemins Word et Writer complets restent dans la transcription.
- Alternative courte candidate : « Trois images reçoivent une alternative, une description détaillée ou un statut décoratif selon leur fonction. »

### Transcription exacte

#### Station 2 - Choisir le bon traitement pour chaque image

2. Documents accessibles | Station 2

##### Dans Word - procédure principale

- P-06 - Clic droit sur l'image > Afficher le texte de remplacement, puis renseigner la description.
- P-07 - Ajouter le texte de remplacement, puis saisir la description détaillée dans un paragraphe voisin.
- P-08 - Afficher le texte de remplacement puis cocher Marquer comme décoratif.

##### Dans Writer - complément

- P-06 - Clic droit sur l'image > Propriétés > Options, puis renseigner le texte alternatif.
- P-07 - Renseigner le texte alternatif dans les propriétés, puis ajouter la description dans le corps.
- P-08 - Si l'option Décoratif existe, l'activer ; sinon laisser titre et description vides seulement après vérification de la redondance.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-06, P-07, P-08.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire verbaliser l'information utile avant de rédiger ou de supprimer une alternative.
Question de synthèse : Que perd-on si l'image est masquée ?
Preuves attendues :
P-06 : Alternative présente dans le DOCX et jugée pertinente par lecture humaine.
P-07 : Équivalence d'information vérifiée sans consulter l'image.
P-08 : Marqueur décoratif ou équivalent vérifié et absence de perte d'information confirmée.

## Slide web 12 - Station 2 - Vrai texte et liens compréhensibles

- Correspondance : PPTX 65 ; scripts/slides/13_pilier3-alt-text.py.
- Rôle : traiter une image de texte et un libellé de lien.
- Famille : comparaison ou transformation.
- Idée principale : le texte doit pouvoir être sélectionné et le lien compris hors contexte.
- Scène : une image contenant du texte est remplacée par un paragraphe structuré ; à côté, un lien vague reçoit un libellé explicite sans changer sa destination.
- Transformation : texte dans l'image et lien ambigu -> vrai texte et libellé autonome.
- Liste blanche du visuel : « Station 2 - Vrai texte et liens compréhensibles » ; « Dans Word - procédure principale » ; « Dans Writer - complément » ; « Preuve : le texte se sélectionne et chaque lien reste clair hors contexte. »
- Image seule : la sélection et la lecture isolée du lien deviennent possibles.
- Continuité : développe P-09 et P-10, puis examine l'information laissée dans l'en-tête.
- Contraintes critiques : conserver la destination du lien ; ne pas laisser l'image de texte comme unique source ; aucun exemple d'URL inventé.
- Alternative courte candidate : « Le texte devient sélectionnable et le lien reste compréhensible hors contexte. »

### Transcription exacte

#### Station 2 - Vrai texte et liens compréhensibles

2. Documents accessibles | Station 2

##### Dans Word - procédure principale

- P-09 - Insérer le texte dans un paragraphe structuré, appliquer les styles utiles puis supprimer l'image de texte.
- P-10 - Modifier le texte affiché du lien via clic droit > Modifier le lien, puis compléter le libellé dans le corps.

##### Dans Writer - complément

- P-09 - Saisir le texte dans le corps, appliquer les styles utiles puis supprimer l'image de texte.
- P-10 - Clic droit > Modifier l'hyperlien, puis compléter le libellé dans le corps.

Preuve : le texte se sélectionne et chaque lien reste clair hors contexte.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-09, P-10.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire tester la sélection du texte puis lire uniquement le libellé du lien.
Question de synthèse : Le texte peut-il être sélectionné et le lien compris tout seul ?
Preuves attendues :
P-09 : Texte sélectionnable présent dans le DOCX et image de texte absente.
P-10 : Destination inchangée, libellé explicite et identification visuelle vérifiées.

## Slide web 13 - Station 2 - L'information essentielle reste dans le corps

- Correspondance : PPTX 66 ; scripts/slides/14_pilier3-liens-infos.py.
- Rôle : corriger une information portée seulement par un en-tête, filigrane ou arrière-plan.
- Famille : comparaison ou transformation.
- Idée principale : le statut du document reste compréhensible dans une lecture linéaire du corps.
- Scène : un statut visible dans un en-tête est repris dans un paragraphe structuré du guide ; une lecture limitée au corps le retrouve.
- Transformation : information périphérique seule -> reprise dans le corps -> compréhension sans arrière-plan.
- Liste blanche du visuel : « Station 2 - L'information essentielle reste dans le corps » ; « Reprendre dans le corps l'information d'un en-tête » ; « Reprendre le même statut à un emplacement logique du corps. »
- Image seule : une information importante ne dépend plus de l'en-tête.
- Continuité : termine la station 2 et prépare le contrôle des couleurs et des données.
- Contraintes critiques : ne pas recréer le filigrane comme exercice ; éviter toute duplication de statut contradictoire ; ne pas ajouter un exemple de statut absent de la source.
- Alternative courte candidate : « Un statut porté par l'en-tête est repris dans le corps du document. »

### Transcription exacte

#### Station 2 - L'information essentielle reste dans le corps

2. Documents accessibles | Station 2

P-11 [P] - Reprendre dans le corps l'information d'un en-tête

##### Dans Word - procédure principale

- Ne jamais faire porter une information essentielle uniquement par un filigrane, un en-tête ou un arrière-plan.
- Ajouter le statut dans le corps avec un style adapté ; l'en-tête peut le conserver, sans en être l'unique porteur.
- Reprendre le même statut à un emplacement logique du corps.

##### Dans Writer - complément

- Ajouter le statut dans le corps avec un style adapté ; l'en-tête peut le conserver, sans en être l'unique porteur.
- Preuve : Statut compréhensible dans le texte linéarisé sans en-tête ni arrière-plan.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-11.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire masquer mentalement l'en-tête et l'arrière-plan, sans recréer de filigrane dans l'exercice.
Question de synthèse : Le statut reste-t-il compréhensible quand on lit uniquement le corps ?
Preuves attendues : P-11 : Statut compréhensible dans le texte linéarisé sans en-tête ni arrière-plan.

## Slide web 14 - Station 3 - Sécuriser couleurs, graphiques et tableaux

- Correspondance : PPTX 67 ; scripts/slides/15_exercice-sami.py.
- Rôle : introduire les trois contrôles de couleurs et de données.
- Famille : tableau pédagogique.
- Idée principale : mesure du contraste, indépendance de la couleur et structure de tableau demandent des preuves distinctes.
- Scène : trois zones du guide de Sami sont examinées : un texte coloré, un graphique à séries et un tableau de données ; chacune reçoit son repère P-12, P-13 ou P-14.
- Transformation : impression visuelle -> mesure ou structure -> preuve conservée.
- Liste blanche du visuel : « Station 3 - Sécuriser couleurs, graphiques et tableaux » ; « P-12 » ; « P-13 » ; « P-14 » ; « Mesurer, rendre l'information indépendante de la couleur, puis vérifier la structure. »
- Image seule : trois objets différents exigent trois contrôles.
- Continuité : ouvre la station 3 et prépare la mesure du contraste.
- Contraintes critiques : ne pas confondre contraste et codage par couleur ; ne pas transformer le tableau en élément décoratif ; conserver les trois codes.
- Alternative courte candidate : « Contraste, graphique et tableau sont contrôlés avec trois preuves distinctes. »

### Transcription exacte

#### Station 3 - Sécuriser couleurs, graphiques et tableaux

2. Documents accessibles | Station 3

##### Tableau : ID, Niveau, Points travaillés

- P-12 | P | Mesurer les contrastes utiles
- P-13 | P | Ne pas transmettre une information par la couleur seule
- P-14 | P | Structurer un tableau de données simple

Mesurer, rendre l'information indépendante de la couleur, puis vérifier la structure.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-12, P-13, P-14.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire choisir le seuil avant la mesure et rappeler que le graphique se reconstruit directement dans Word.
Question de synthèse : Quelle preuve distingue une impression visuelle d'un contrôle vérifiable ?
Preuves attendues :
P-12 : Ratio calculé conservé et couleurs finales vérifiées dans le document.
P-13 : Séries et conclusions identifiables en niveaux de gris et dans l'équivalent textuel.
P-14 : XML sans fusion ni imbrication et relations de cellules vérifiées à la lecture.

## Slide web 15 - Station 3 - Le contraste se mesure

- Correspondance : PPTX 68 ; scripts/slides/16_pilier4-langue-lisibilite.py.
- Rôle : faire choisir le seuil applicable avant de mesurer le contraste.
- Famille : comparaison ou transformation.
- Idée principale : un contraste se mesure et se corrige à partir du seuil propre au contenu.
- Scène : un extrait du guide et ses couleurs de police et de fond sont examinés avec un outil de mesure ; les seuils pour texte normal et grands éléments sont clairement séparés.
- Transformation : couleurs repérées -> seuil choisi -> combinaison mesurée et corrigée.
- Liste blanche du visuel : « Station 3 - Le contraste se mesure » ; « P-12 » ; « 4,5:1 » ; « Texte normal » ; « 3:1 » ; « Grand texte et éléments graphiques ».
- Image seule : choisir le seuil précède la lecture du ratio et la correction des couleurs.
- Continuité : développe P-12 puis passe au graphique de P-13.
- Contraintes critiques : ne pas présenter 3:1 comme seuil du texte normal ; ne pas inventer un ratio mesuré pour le document de Sami.
- Alternative courte candidate : « Deux seuils de contraste sont distingués avant la mesure d'un extrait du document. »

### Transcription exacte

#### Station 3 - Le contraste se mesure

2. Documents accessibles | Station 3

P-12 [P] - Mesurer les contrastes utiles

- 4,5:1 : Texte normal
- 3:1 : Grand texte et éléments graphiques

##### Dans Word - procédure principale

- Relever les couleurs de police et de fond, mesurer avec l'outil de contraste, puis modifier la couleur de police.
- Mesurer la combinaison puis choisir une couleur qui atteint le seuil applicable.

##### Dans Writer - complément

- Relever les couleurs de caractère et d'arrière-plan, mesurer, puis modifier la couleur de caractère.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-12.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire relever les couleurs, choisir le seuil, puis seulement lancer l'outil de mesure.
Question de synthèse : Quel seuil s'applique avant même de lire le résultat ?
Preuves attendues : P-12 : Ratio calculé conservé et couleurs finales vérifiées dans le document.

## Slide web 16 - Station 3 - Un graphique compréhensible sans la couleur

- Correspondance : PPTX 69 ; scripts/slides/17_pilier4-espaces-clignotants.py.
- Rôle : faire reconstruire un graphique dont les séries restent identifiables sans couleur.
- Famille : comparaison ou transformation.
- Idée principale : étiquettes, motifs ou équivalent textuel portent les valeurs et les conclusions au-delà des couleurs.
- Scène : un graphique coloré du guide devient un histogramme dans Word, avec étiquettes et motifs ; une lecture en niveaux de gris permet de distinguer les séries.
- Transformation : séries distinguées par couleur -> graphique reconstruit -> séries identifiables en gris et dans le texte.
- Liste blanche du visuel : « Station 3 - Un graphique compréhensible sans la couleur » ; « P-13 » ; « Ajouter étiquettes, motifs ou un équivalent textuel complet à tout code couleur porteur d'information. »
- Image seule : la distinction entre séries doit résister à la disparition de la couleur.
- Continuité : suit la mesure de contraste et précède la structure du tableau.
- Contraintes critiques : aucune donnée chiffrée inventée dans le graphique ; la preuve inclut les conclusions, pas seulement les séries.
- Alternative courte candidate : « Des étiquettes et des motifs distinguent les séries d'un histogramme en niveaux de gris. »

### Transcription exacte

#### Station 3 - Un graphique compréhensible sans la couleur

2. Documents accessibles | Station 3

P-13 [P] - Ne pas transmettre une information par la couleur seule

##### Dans Word - procédure principale

- Ajouter étiquettes, motifs ou un équivalent textuel complet à tout code couleur porteur d'information.
- Insertion > Graphique > Histogramme groupé, reporter les valeurs affichées dans l'image, puis afficher les étiquettes et appliquer des motifs distincts.
- Reconstruire dans Word le graphique à partir des valeurs affichées dans l'image, puis ajouter des étiquettes et des motifs ou conserver un équivalent textuel complet.

##### Dans Writer - complément

- Insertion > Diagramme, reporter les valeurs affichées dans l'image, puis afficher les étiquettes et choisir des remplissages distincts.
- Preuve : Séries et conclusions identifiables en niveaux de gris et dans l'équivalent textuel.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-13.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire reconstruire le graphique dans Word à partir des valeurs, puis ajouter étiquettes et motifs.
Question de synthèse : Les séries restent-elles identifiables en niveaux de gris ?
Preuves attendues : P-13 : Séries et conclusions identifiables en niveaux de gris et dans l'équivalent textuel.

## Slide web 17 - Station 3 - Un tableau de données simple

- Correspondance : PPTX 70 ; scripts/slides/18_pilier5-avant-publier.py.
- Rôle : simplifier la grille de données et identifier son en-tête.
- Famille : comparaison ou transformation.
- Idée principale : un tableau de données accessible garde une grille simple et lisible cellule par cellule.
- Scène : un tableau du guide est représenté comme une grille régulière, titrée, dont la ligne d'en-tête est reconnaissable et répétée.
- Transformation : tableau complexe -> défusion et réglages de lignes -> grille de données vérifiable.
- Liste blanche du visuel : « Station 3 - Un tableau de données simple » ; « P-14 » ; « Structurer un tableau de données simple » ; « Simplifier la structure, identifier l'en-tête et régler sa répétition ainsi que les lignes. »
- Image seule : la simplicité de la grille rend les relations entre cellules vérifiables.
- Continuité : clôt la station 3 et prépare les propriétés de langue et de style.
- Contraintes critiques : pas de tableau de mise en page ; aucune cellule fusionnée ni grille flottante présentée comme solution.
- Alternative courte candidate : « Un tableau titré possède une grille simple et un en-tête identifié. »

### Transcription exacte

#### Station 3 - Un tableau de données simple

2. Documents accessibles | Station 3

P-14 [P] - Structurer un tableau de données simple

##### Dans Word - procédure principale

- Utiliser un tableau de données titré, sans fusion, imbrication, fractionnement de ligne ni usage de mise en page, avec en-tête identifié et répété.
- Outils de tableau > Disposition pour défusionner ; Propriétés du tableau pour répéter l'en-tête et interdire le fractionnement des lignes.
- Simplifier la structure, identifier l'en-tête et régler sa répétition ainsi que les lignes.

##### Dans Writer - complément

- Tableau > Propriétés pour simplifier la grille, répéter les premières lignes et éviter le fractionnement.
- Preuve : XML sans fusion ni imbrication et relations de cellules vérifiées à la lecture.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-14.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire distinguer tableau de données et mise en page avant d'ouvrir les propriétés du tableau.
Question de synthèse : Chaque cellule appartient-elle à une grille de données simple ?
Preuves attendues : P-14 : XML sans fusion ni imbrication et relations de cellules vérifiées à la lecture.

## Slide web 18 - Station 4 - Régler langues et lisibilité

- Correspondance : PPTX 71 ; scripts/slides/19_pilier5-verificateur.py.
- Rôle : présenter les quatre réglages de langue et de lisibilité.
- Famille : tableau pédagogique.
- Idée principale : les propriétés et styles sources doivent porter les corrections pour tout le document.
- Scène : quatre zones d'un document sont associées aux codes P-15 à P-18 : langue, typographie, casse et sigles ; le style du corps est visible comme réglage commun.
- Transformation : corrections visuelles isolées -> réglages portés par les propriétés et styles -> document cohérent.
- Liste blanche du visuel : « Station 4 - Régler langues et lisibilité » ; « P-15 » ; « P-16 » ; « P-17 » ; « P-18 » ; « Corriger les styles sources : la langue et la lisibilité se règlent à l'échelle du document. »
- Image seule : quatre contrôles partagent un même principe de réglage durable.
- Continuité : ouvre la station 4 après les données et précède les procédures de langue et de style.
- Contraintes critiques : ne pas réduire la langue à une apparence typographique ; ne pas traiter les paragraphes un par un comme méthode principale.
- Alternative courte candidate : « Quatre contrôles relient langue, styles typographiques, casse et sigles. »

### Transcription exacte

#### Station 4 - Régler langues et lisibilité

2. Documents accessibles | Station 4

##### Tableau : ID, Niveau, Points travaillés

- P-15 | P | Définir les langues du document et des passages
- P-16 | P | Régler une typographie lisible par les styles
- P-17 | P | Appliquer la casse par la mise en forme
- P-18 | P | Développer les sigles et vérifier les majuscules

Corriger les styles sources : la langue et la lisibilité se règlent à l'échelle du document.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-15, P-16, P-17, P-18.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire corriger le style source et la langue du passage plutôt que les paragraphes un par un.
Question de synthèse : Le réglage est-il porté par les propriétés et les styles, ou seulement par l'apparence ?
Preuves attendues :
P-15 : Propriétés et XML de langue cohérents
P-16 : Propriétés typographiques contrôlées dans le DOCX et lisibilité relue.
P-17 : Texte XML accentué et contrôle visuel de la casse.
P-18 : Première occurrence compréhensible et faute témoin en majuscules détectée.

## Slide web 19 - Station 4 - Langues et styles typographiques

- Correspondance : PPTX 72 ; scripts/slides/20_export-pdf-accessible.py.
- Rôle : régler la langue principale, celle d'un passage et la typographie du corps.
- Famille : processus horizontal.
- Idée principale : les corrections de langue et de lisibilité passent par les propriétés et les styles.
- Scène : un passage du guide change de langue de vérification tandis que la modification du style Normal se répercute sur plusieurs paragraphes.
- Transformation : langue et paragraphes mal réglés -> modification ciblée des propriétés et du style -> corps cohérent.
- Liste blanche du visuel : « Station 4 - Langues et styles typographiques » ; « Dans Word - procédure principale » ; « P-15 » ; « P-16 » ; « Preuve : langue cohérente, corps à 12 points minimum, interligne 1,15 et alignement à gauche. »
- Image seule : un réglage du style corrige tout le corps et la langue d'un passage se définit séparément.
- Continuité : précise la station 4 puis passe à la casse et aux sigles.
- Contraintes critiques : ne pas confondre langue principale et langue du passage ; conserver les seuils typographiques de la source.
- Alternative courte candidate : « La langue d'un passage et le style du corps sont réglés dans Word. »

### Transcription exacte

#### Station 4 - Langues et styles typographiques

2. Documents accessibles | Station 4

##### Dans Word - procédure principale

- P-15 - Révision > Langue > Définir la langue de vérification pour le document puis pour le passage sélectionné.
- P-16 - Accueil > Styles > Modifier le style Normal, puis régler police, taille, alignement et paragraphe.

##### Dans Writer - complément

- P-15 - Outils > Langue pour tout le texte, puis langue du caractère pour le passage sélectionné.
- P-16 - Styles > Gérer les styles > modifier Style de paragraphe par défaut, puis régler police et retraits et espacement.

Preuve : langue cohérente, corps à 12 points minimum, interligne 1,15 et alignement à gauche.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-15, P-16.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire distinguer la langue principale de celle du passage, puis modifier le style plutôt que chaque paragraphe.
Question de synthèse : Une correction du style Normal améliore-t-elle tout le corps ?
Preuves attendues :
P-15 : Propriétés et XML de langue cohérents
P-16 : Propriétés typographiques contrôlées dans le DOCX et lisibilité relue.

## Slide web 20 - Station 4 - Casse, accents et sigles

- Correspondance : PPTX 73 ; scripts/slides/21_etude-cas-sophie.py.
- Rôle : conserver un texte correctement écrit sous l'apparence en majuscules et développer les sigles.
- Famille : comparaison ou transformation.
- Idée principale : la casse d'affichage ne remplace ni les accents dans le texte source ni la première forme développée d'un sigle.
- Scène : une ligne en majuscules est reliée à son texte source accentué et à un sigle développé dans le corps ; les réglages de contrôle sont représentés comme dernière vérification.
- Transformation : saisie en majuscules et sigle opaque -> texte normal, effet de casse et développement -> lecture compréhensible.
- Liste blanche du visuel : « Station 4 - Casse, accents et sigles » ; « P-17 » ; « P-18 » ; « Preuve : texte source accentué, première occurrence développée et majuscules contrôlées. »
- Image seule : l'apparence en majuscules conserve une source correctement écrite et un sigle explicité.
- Continuité : termine la station 4 avant la vérification et l'export.
- Contraintes critiques : ne pas inventer de sigle ni de phrase source ; distinguer texte saisi et effet de mise en forme.
- Alternative courte candidate : « Une ligne en majuscules garde ses accents dans le texte source et un sigle est développé. »

### Transcription exacte

#### Station 4 - Casse, accents et sigles

2. Documents accessibles | Station 4

##### Dans Word - procédure principale

- P-17 - Corriger le texte, puis Police > Effets > Majuscules si cette apparence est nécessaire.
- P-18 - Développer le terme dans le corps, puis Fichier > Options > Vérification et décocher Ignorer les mots en MAJUSCULES.

##### Dans Writer - complément

- P-17 - Corriger le texte, puis Format > Caractère > Effets de caractères > Majuscules.
- P-18 - Développer le terme dans le corps, puis Outils > Options > Paramètres linguistiques > Linguistique et vérifier les options de contrôle.

Preuve : texte source accentué, première occurrence développée et majuscules contrôlées.

### Discours oral exact

Minutage de la station : 15 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-17, P-18.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire restaurer la saisie normale avant d'appliquer la casse, puis rechercher la première occurrence du sigle.
Question de synthèse : Le texte reste-t-il correctement écrit sous son apparence visuelle ?
Preuves attendues :
P-17 : Texte XML accentué et contrôle visuel de la casse.
P-18 : Première occurrence compréhensible et faute témoin en majuscules détectée.

## Slide web 21 - Station 5 - Finaliser, vérifier, exporter et contrôler

- Correspondance : PPTX 74 ; scripts/slides/22_par-ou-commencer.py.
- Rôle : ordonner les quatre contrôles finaux sans confondre alerte automatique et conformité.
- Famille : tableau pédagogique.
- Idée principale : propriétés, vérificateur Word, export structuré et contrôle du PDF produisent des preuves complémentaires.
- Scène : un DOCX traverse quatre étapes nommées P-19, C-01, P-20 et C-02 ; une checklist humaine conclut le parcours.
- Transformation : document corrigé -> métadonnées et vérification -> PDF structuré puis contrôlé.
- Liste blanche du visuel : « Station 5 - Finaliser, vérifier, exporter et contrôler » ; « P-19 » ; « P-20 » ; « C-01 » ; « C-02 » ; « Les outils automatiques filtrent ; la checklist et la vérification humaine concluent. »
- Image seule : un document finalisé passe par plusieurs contrôles avant remise.
- Continuité : ouvre la station 5 et annonce ses deux procédures détaillées.
- Contraintes critiques : les quatre codes doivent rester distincts ; un écran sans erreur n'est pas présenté comme conformité.
- Alternative courte candidate : « Le document passe des propriétés à la vérification, à l'export PDF et au contrôle humain. »

### Transcription exacte

#### Station 5 - Finaliser, vérifier, exporter et contrôler

2. Documents accessibles | Station 5

##### Tableau : ID, Niveau, Points travaillés

- P-19 | P | Renseigner les propriétés et le nom du fichier
- P-20 | P | Exporter un PDF structuré
- C-01 | C | Utiliser le vérificateur d'accessibilité Word
- C-02 | C | Contrôler le PDF après export

Les outils automatiques filtrent ; la checklist et la vérification humaine concluent.

### Discours oral exact

Minutage de la station : 18 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-19, P-20, C-01, C-02.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire distinguer propriété, vérification Word, export PDF et contrôle post-export.
Question de synthèse : Qu'est-ce que l'outil automatique ne peut pas décider à votre place ?
Preuves attendues :
P-19 : Métadonnées inspectées dans le DOCX et nom de sortie relu.
P-20 : Propriétés et structure inspectées dans le PDF
C-01 : Relevé du vérificateur conservé et alertes résiduelles justifiées.
C-02 : Rapport PAC ou Acrobat conservé

## Slide web 22 - Station 5 - Propriétés et vérificateur Word

- Correspondance : PPTX 75 ; scripts/slides/26_checklist-21-criteres.py.
- Rôle : renseigner les propriétés et interpréter les alertes du vérificateur Word.
- Famille : processus horizontal.
- Idée principale : les métadonnées et le vérificateur fournissent deux types de preuves avant l'export.
- Scène : le panneau de propriétés d'un DOCX et le panneau des alertes du vérificateur sont reliés ; une alerte résiduelle est expliquée dans une note de contrôle.
- Transformation : fichier sans propriétés et alertes brutes -> titre, auteur, langue, nom descriptif et relevé justifié.
- Liste blanche du visuel : « Station 5 - Propriétés et vérificateur Word » ; « P-19 » ; « C-01 » ; « Traiter les alertes pertinentes et expliquer toute alerte résiduelle ; viser zéro erreur sans en faire une preuve de conformité. »
- Image seule : les propriétés sont renseignées puis les alertes du vérificateur sont examinées avec discernement.
- Continuité : applique la première moitié de la station 5 puis prépare l'export.
- Contraintes critiques : ne pas montrer un écran vert comme preuve de conformité ; ne pas effacer une alerte sans explication.
- Alternative courte candidate : « Les propriétés du DOCX sont renseignées et les alertes Word sont examinées. »

### Transcription exacte

#### Station 5 - Propriétés et vérificateur Word

2. Documents accessibles | Station 5

##### Dans Word - P-19 [P] - Renseigner les propriétés et le nom du fichier

- Renseigner titre, auteur et langue puis enregistrer sous un nom descriptif.
- Fichier > Informations > Propriétés > Propriétés avancées, puis Fichier > Enregistrer sous.
- Preuve : Métadonnées inspectées dans le DOCX et nom de sortie relu.

##### Dans Word - C-01 [C] - Utiliser le vérificateur d'accessibilité Word

- Traiter les alertes pertinentes et expliquer toute alerte résiduelle ; viser zéro erreur sans en faire une preuve de conformité.
- Révision > Vérifier l'accessibilité, parcourir chaque résultat et utiliser les actions recommandées avec discernement.
- Preuve : Relevé du vérificateur conservé et alertes résiduelles justifiées.

Dans Writer - complément : Fichier > Propriétés, puis Fichier > Enregistrer sous. | Outils > Vérification de l'accessibilité, parcourir les résultats et vérifier manuellement les points non couverts.

### Discours oral exact

Minutage de la station : 18 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-19, C-01.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire renseigner les propriétés avant l'analyse, puis discuter chaque alerte au lieu de viser un écran vert à tout prix.
Question de synthèse : Une absence d'erreur suffit-elle à prouver l'accessibilité ?
Preuves attendues :
P-19 : Métadonnées inspectées dans le DOCX et nom de sortie relu.
C-01 : Relevé du vérificateur conservé et alertes résiduelles justifiées.

## Slide web 23 - Station 5 - Exporter puis contrôler le PDF

- Correspondance : PPTX 76 ; scripts/slides/26a_checklist-exercice-2.py.
- Rôle : exporter un PDF structuré et vérifier le fichier produit.
- Famille : processus horizontal.
- Idée principale : les options d'export et le contrôle après export sont deux gestes distincts.
- Scène : un DOCX est exporté avec propriétés, balises et signets ; le PDF obtenu est ouvert dans un outil de contrôle et un rapport est conservé.
- Transformation : DOCX vérifié -> export structuré -> PDF contrôlé et checklist humaine.
- Liste blanche du visuel : « Station 5 - Exporter puis contrôler le PDF » ; « P-20 » ; « C-02 » ; « Exporter avec propriétés, balises de structure et signets générés depuis les titres. »
- Image seule : le PDF n'est finalisé qu'après vérification de sa structure et de son ordre de lecture.
- Continuité : termine la station 5 et mène aux trois pages de checklist.
- Contraintes critiques : PAC et Acrobat Pro sont des outils de contrôle, pas une remédiation avancée enseignée ici ; ne pas inventer un rapport sans export réel.
- Alternative courte candidate : « Le PDF balisé est contrôlé après son export depuis Word. »

### Transcription exacte

#### Station 5 - Exporter puis contrôler le PDF

2. Documents accessibles | Station 5

##### Dans Word - P-20 [P] - Exporter un PDF structuré

- Exporter avec propriétés, balises de structure et signets générés depuis les titres.
- Vérifier les propriétés dans Fichier > Informations, puis Fichier > Enregistrer sous ou Exporter > PDF > Options et activer les balises de structure ainsi que les signets issus des titres.
- Preuve : Propriétés et structure inspectées dans le PDF

##### Dans Word - C-02 [C] - Contrôler le PDF après export

- Contrôler avec PAC, ou Acrobat Pro en alternative, le titre, la langue, les balises et l'ordre de lecture, puis terminer par la checklist humaine.
- Ouvrir le PDF exporté dans PAC ; utiliser Acrobat Pro comme alternative si PAC n'est pas disponible.
- Preuve : Rapport PAC ou Acrobat conservé

Dans Writer - complément : Vérifier les propriétés dans Fichier > Propriétés, puis Fichier > Exporter vers > Exporter au format PDF et activer PDF balisé ainsi que l'export des repères. | Ouvrir le PDF exporté dans PAC ; utiliser Acrobat Pro comme alternative si PAC n'est pas disponible.

### Discours oral exact

Minutage de la station : 18 minutes, synthèse comprise.
Contrôles travaillés sur cette slide : P-20, C-02.
Parcours guidé : partir du DOCX avec pistes, reformuler le problème et laisser le binôme réaliser la correction.
Variante autonome : partir du DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.
Points d'aide possibles : Faire vérifier les options avant l'export, puis commenter le rapport PAC sans enseigner la remédiation avancée.
Question de synthèse : Le PDF conserve-t-il le titre, la langue, les balises, les signets et un ordre lisible ?
Preuves attendues :
P-20 : Propriétés et structure inspectées dans le PDF
C-02 : Rapport PAC ou Acrobat conservé

## Slide web 24 - Checklist progressive - Stations 1 et 2 - ÉTALON

- Correspondance : PPTX 77 ; scripts/slides/26b_checklist-autres.py.
- Rôle : reprendre les contrôles P-01 à P-11 après les deux premières stations.
- Famille : checklist ou processus.
- Idée principale : la correction de la structure et du sens se vérifie point par point.
- Scène : deux ensembles de cases cochables, l'un pour la structure, l'autre pour les contenus et les liens ; les codes P-01 à P-11 restent repérables et l'illustration occupe un espace secondaire.
- Transformation : corrections réalisées -> cases renseignées -> points encore ouverts identifiés.
- Liste blanche du visuel : « Checklist progressive - Stations 1 et 2 » ; « Structurer et naviguer » ; « Rendre les contenus et les liens compréhensibles » ; « P-01 » à « P-11 ».
- Image seule : deux familles de contrôles permettent de relire les corrections des stations 1 et 2.
- Continuité : ouvre les trois pages de checklist et prépare les stations 3 et 4.
- Contraintes critiques : conserver les onze codes dans l'ordre ; la checklist illustrée ne remplace pas le texte intégral de l'accordéon ; aucun état de coche ne doit annoncer une correction non constatée.
- Alternative courte candidate : « La checklist regroupe onze contrôles de structure, de contenus et de liens. »

### Transcription exacte

#### Checklist progressive - Stations 1 et 2

2. Documents accessibles | Checklist

##### Structurer et naviguer

- P-01 [P] - Le titre principal et les titres de section utilisent des styles adaptés.
- P-02 [P] - La hiérarchie des titres ne saute aucun niveau.
- P-03 [P] - Le volet de navigation et le sommaire automatique reflètent le même plan.
- P-04 [P] - Les listes sont créées avec les fonctions de puces ou de numérotation.
- P-05 [P] - La mise en page n'est pas simulée par des caractères ou des paragraphes vides.

##### Rendre les contenus et les liens compréhensibles

- P-06 [P] - Chaque image informative simple possède une alternative pertinente.
- P-07 [P] - Une image complexe possède une alternative courte et une description détaillée adjacente.
- P-08 [P] - Les images redondantes sont traitées comme décoratives sans masquer d'information.
- P-09 [P] - Les informations textuelles sont fournies en vrai texte, pas seulement en image.
- P-10 [P] - Chaque lien est compréhensible hors contexte et chaque téléchargement est décrit.
- P-11 [P] - Toute information essentielle portée par un en-tête, un filigrane ou un arrière-plan est aussi présente dans le corps.

### Discours oral exact

Faire relire les cases renseignées après les deux premières stations.
La formulation et l'ordre proviennent de la matrice et de la checklist distribuée.

## Slide web 25 - Checklist progressive - Stations 3 et 4

- Correspondance : PPTX 78 ; scripts/slides/26c_checklist-autres-2.py.
- Rôle : relire les corrections et les preuves des stations 3 et 4.
- Famille : checklist ou processus.
- Idée principale : chaque contrôle des couleurs, données, langues et styles doit être assorti d'une preuve.
- Scène : sept cases P-12 à P-18 sont réparties entre « couleurs, graphiques et tableaux » et « langues et lisibilité » ; une petite zone de preuve accompagne chaque famille sans contenir de preuve inventée.
- Transformation : corrections des stations 3 et 4 -> relecture des cases -> preuve conservée identifiée.
- Liste blanche du visuel : « Checklist progressive - Stations 3 et 4 » ; « Sécuriser couleurs, graphiques et tableaux » ; « Régler langues et lisibilité » ; « P-12 » à « P-18 ».
- Image seule : les contrôles des stations 3 et 4 appellent chacun une preuve.
- Continuité : poursuit la checklist et prépare les contrôles finaux.
- Contraintes critiques : ne pas laisser croire qu'une simple case cochée constitue une preuve ; garder les codes et familles dans l'ordre source.
- Alternative courte candidate : « Sept contrôles relient couleurs, données, langues et lisibilité à leurs preuves. »

### Transcription exacte

#### Checklist progressive - Stations 3 et 4

2. Documents accessibles | Checklist

##### Sécuriser couleurs, graphiques et tableaux

- P-12 [P] - Les contrastes sont mesurés et atteignent le seuil correspondant au contenu.
- P-13 [P] - Une information donnée par la couleur possède aussi un repère non coloré.
- P-14 [P] - Les tableaux de données sont simples, titrés et possèdent des en-têtes identifiés.

##### Régler langues et lisibilité

- P-15 [P] - La langue principale et les changements de langue sont correctement définis.
- P-16 [P] - Le corps utilise une police sans sérif, au moins 12 points, un interligne de 1,15 et un alignement à gauche.
- P-17 [P] - Les mots sont saisis normalement avec leurs accents avant toute mise en forme en majuscules.
- P-18 [P] - Les sigles sont développés à leur première occurrence et les majuscules sont vérifiées.

### Discours oral exact

Faire relire les cases renseignées après les stations 3 et 4.
Demander quelle preuve a été conservée pour chaque correction.

## Slide web 26 - Checklist progressive - Station 5 et points signalés

- Correspondance : PPTX 79 ; scripts/slides/26d_checklist-station-5-signales.py.
- Rôle : finaliser la checklist et distinguer les contrôles travaillés des contrôles signalés.
- Famille : checklist ou processus.
- Idée principale : l'export et son contrôle concluent la pratique ; cinq points complémentaires restent signalés sans devenir des manipulations obligatoires.
- Scène : les quatre cases P-19, P-20, C-01 et C-02 occupent la première zone ; les cinq cases S-01 à S-05 sont visibles dans une seconde zone clairement intitulée « Contrôles signalés ».
- Transformation : livrables finaux -> vérification humaine -> points complémentaires repérés.
- Liste blanche du visuel : « Checklist progressive - Station 5 et points signalés » ; « Finaliser, vérifier, exporter et contrôler » ; « Contrôles signalés » ; « P-19 » ; « P-20 » ; « C-01 » ; « C-02 » ; « S-01 » à « S-05 ».
- Image seule : les contrôles finaux et les points signalés sont deux groupes distincts.
- Continuité : termine la checklist et mène à la synthèse de la matinée.
- Contraintes critiques : ne pas présenter les cinq S comme manipulations obligatoires ; ne cocher aucun contrôle par défaut ; conserver l'ordre de la source.
- Alternative courte candidate : « Quatre contrôles finaux et cinq points signalés terminent la checklist. »

### Transcription exacte

#### Checklist progressive - Station 5 et points signalés

2. Documents accessibles | Checklist

##### Finaliser, vérifier, exporter et contrôler

- P-19 [P] - Le titre, l'auteur, la langue et le nom de fichier sont renseignés de façon descriptive.
- P-20 [P] - Le PDF est exporté avec ses propriétés, ses balises et ses signets.
- C-01 [C] - Le vérificateur a été exécuté, ses alertes pertinentes traitées et les alertes résiduelles expliquées.
- C-02 [C] - Le PDF a été contrôlé après export avec PAC ou Acrobat Pro puis avec la checklist humaine.

##### Contrôles signalés

- S-01 [S] - Le document n'est pas protégé lorsque sa modification doit rester possible.
- S-02 [S] - Le document ne contient aucun contenu clignotant.
- S-03 [S] - Le document ne contient pas de formulaire Word interactif.
- S-04 [S] - Les objets et zones de texte flottants ne portent aucune information essentielle.
- S-05 [S] - Les tableaux ne servent pas à la mise en page et ne sont pas flottants.

### Discours oral exact

Faire terminer la checklist humaine.
Les contrôles signalés restent importants, mais ne deviennent pas des manipulations obligatoires dans ce TP.

## Slide web 27 - Synthèse de la matinée - de l'intention à la preuve

- Correspondance : PPTX 80 ; scripts/slides/26e_synthese-matinee.py.
- Rôle : faire formuler un acquis transférable et annoncer la partie III.
- Famille : synthèse d'action.
- Idée principale : une correction utile relie structure, compréhension et preuve vérifiable.
- Scène : le document corrigé passe par quatre gestes successifs représentés sobrement ; une ouverture finale mène aux contrôles rapides sur le Web.
- Transformation : intentions et manipulations -> preuve vérifiée -> réemploi dans les prochains documents et sur le Web.
- Liste blanche du visuel : « Synthèse de la matinée - de l'intention à la preuve » ; « Ce que nous retenons » ; « Questions et transition » ; « Structurer, rendre compréhensible, vérifier avec les outils, puis contrôler humainement. »
- Image seule : les gestes de structuration, de compréhension et de contrôle forment une méthode réutilisable.
- Continuité : clôt la partie II et passe à la partie III consacrée aux points de contrôle rapides sur le Web.
- Contraintes critiques : synthèse de 15 minutes hors TP ; ne pas annoncer que les outils automatiques suffisent ; ne pas ajouter de nouveau contrôle.
- Alternative courte candidate : « Un document est structuré, rendu compréhensible, vérifié et contrôlé humainement. »

### Transcription exacte

#### Synthèse de la matinée - de l'intention à la preuve

Matin | Synthèse

##### Ce que nous retenons

- L'environnement peut créer ou supprimer une situation de handicap
- La structure et le sens comptent autant que l'apparence
- Une correction doit produire une preuve vérifiable

##### Questions et transition

- Quel réflexe allez-vous réutiliser dans votre prochain document ?
- Quel point demande encore une clarification ?
- Après les documents, nous appliquerons la même démarche au Web

Structurer, rendre compréhensible, vérifier avec les outils, puis contrôler humainement.

### Discours oral exact

Cette synthèse dure 15 minutes, de 12 h à 12 h 15, hors des 90 minutes du TP.
Recueillir les questions, faire formuler un acquis transférable et annoncer la partie III consacrée aux points de contrôle rapides sur le Web.
