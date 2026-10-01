Web accessible - points de contrôle rapides
============================================

## Statut du document

- Storyboard validé par relecture interne et contre-relecture Claude ; prêt pour la production limitée aux quatre étalons.
- Destination après validation : `web-accessible-points-de-controle-rapides/source/storyboard.md`, copiée par la matrice de création du jeu.
- Source : slides PPTX 79 à 108 du support IGPDE 102846, générées par les modules Python indiqués pour chaque slide.
- Correspondance : 30 visuels web pour 30 slides PPTX, dans le même ordre.
- Numérotation publique : 1 à 30. Les numéros 79 à 108 restent uniquement dans la traçabilité.
- Étalons à produire après validation du storyboard : slides web 01, 02, 16 et 25.
- Verdict de contre-relecture : `VALIDÉ` ; aucun écart résiduel bloquant.

## Diagnostic pédagogique

- Public : communicantes et communicants, sans prérequis de développement web.
- Action attendue : repérer rapidement des signaux d’accessibilité, tester une page et formuler une remontée exploitable sans prétendre réaliser un audit RGAA complet.
- Corpus : 30 slides couvrant un cadrage, 13 points de contrôle, une mission guidée, plusieurs interactions et démonstrations, deux bonus médias, une grille de remontée et un bonus sur les liens et PDF.
- Idées pivots : les contrôles automatiques ne remplacent pas l’audit ; quelques gestes simples révèlent des barrières probables ; un constat utile associe verdict, impact, correctif et preuve.
- Charge cognitive : le PPTX contient plusieurs tableaux et listes détaillées. Les visuels les condensent en scènes ou transformations ; les accordéons conservent tout le contenu exact.
- Niveau cognitif visé : comprendre, appliquer, puis analyser une page réelle.

## Contrat de série

- Titre public : « Web accessible - points de contrôle rapides ».
- Slug : `web-accessible-points-de-controle-rapides`.
- Référence visuelle opposable : le preset local `IGPDE Accessibilité - bleu illustré` de l’usine, dans `_source/imagegen-igpde/`, notamment ses quatre images `reference-01-ouverture.png`, `reference-02-avant-apres.png`, `reference-03-tableau.png` et `reference-04-checklist.png`. La série publique réseaux sociaux V5 reste le témoin de continuité visuelle.
- Grammaire observée à reprendre : très grand titre bleu nuit, fond blanc lumineux, illustration semi-plate bleu clair, contours fins, ombres absentes ou très légères, libellés courts et composition lisible en miniature. Reprendre la mécanique, jamais le contenu métier.
- Format final : image 16:9, 1672 x 941 pixels, soit le canevas réel de la série réseaux sociaux V5 prise comme référence.
- Masque commun : fond blanc lumineux, titre bleu France aligné à gauche, scène ou objet-système central, repère de progression discret dans l’interface web seulement, callout bleu clair centré en bas si nécessaire.
- Personnage fil rouge : une communicante aux cheveux foncés, vue dans la slide 01 de référence, revient dans les scènes humaines ; les personnages secondaires conservent une diversité crédible. Son écran et la page web simulée gardent les mêmes proportions et le même vocabulaire visuel d’une slide à l’autre.
- Palette : bleu France `#000091`, bleu d’action `#2B6DE8`, bleu clair `#E3EEFF`, gris bleuté `#D7E1F0`, rouge `#E1000F` réservé aux erreurs, vert `#00A95F` réservé aux validations.
- Typographie : Marianne, avec Arial comme seul fallback.
- Effets : les modelés et dégradés bleus très légers observés dans les références sont autorisés ; tout effet brillant, métallique, spectaculaire ou toute 3D lourde reste interdit.
- Interdits : faux logo, emblème officiel, photographie, photoréalisme, 3D lourde, texture papier, blob décoratif, ombre lourde, texte parasite, paragraphe dense dans l’image, jargon de développement ajouté, tiret cadratin ou demi-cadratin.
- Fidélité : le titre source reste inchangé. L’image ne garde que le message principal et les libellés indispensables. La transcription reprend tout le contenu visible du PPTX. Le discours oral reprend intégralement `add_notes()`.
- Sources externes : ne pas ajouter d’information au-delà des sources déjà citées dans le PPTX. La source WebAIM reste `https://webaim.org/projects/million/`.
- QR codes : produire les QR codes de façon déterministe et les superposer au visuel final avec leur URL lisible. Ne jamais demander à ImageGen de fabriquer un QR code.
- Traçabilité de génération : après validation des étalons seulement, créer `outputs/ia-slides/2026-10-01-web-accessible-points-de-controle-rapides/`, y conserver le storyboard, les prompts, le reçu ImageGen et la planche-contact, sans versionner ce dossier de travail.

## Règles des deux accordéons

- Accordéon « Transcription » : titre de slide comme premier niveau de titre interne, puis surtitre pédagogique exact sous forme de paragraphe, puis contenu visible exact avec titres, listes et tableaux HTML réels. Ne jamais transformer le surtitre en sous-section ni créer un saut de niveau de titre.
- Accordéon « Lire le discours oral » : texte exact de `add_notes()`, structuré pour la lecture sans ajouter de cours ni supprimer de consigne.
- Éléments de masque exclus de la transcription : logos, pied de page récurrent « Formation 102846 / ... », date et numéro de page. Le surtitre pédagogique propre à chaque slide, par exemple « 3. points de contrôle rapides | WebAIM Million 2026 », reste inclus.
- Code et attributs : utiliser des éléments `code` dans le HTML final pour `h1`, `lang="fr"`, `alt=""`, `required` et les autres extraits techniques.
- Tableaux : conserver les en-têtes de colonnes et toutes les cellules ; utiliser `caption`, `thead`, `tbody` et `scope="col"` dans le HTML final.

## Colonne vertébrale

1. Comprendre pourquoi un contrôle rapide est nécessaire.
2. Vérifier les images et la structure de la page.
3. Tester les contrastes, les liens et la navigation au clavier.
4. Contrôler la langue, le zoom et les médias.
5. Examiner les formulaires et transformer les constats en remontées utiles.

## Points de vigilance de fidélité

- La slide 01 annonce oralement une « mission d’audit groupé sur une page de votre choix », tandis que la slide 16 fait travailler sur le site d’entraînement fourni. Les deux formulations viennent du PPTX et restent conservées sans harmonisation silencieuse.
- La slide 24 conserve l’orthographe source « Audio-description » dans son titre, même si d’autres usages éditoriaux peuvent écrire « audiodescription » en un mot.
- La slide 30 parle des « 13 checks » et présente les liens et PDF comme un bonus, pas comme de nouveaux points de contrôle obligatoires.
- Les reformulations courtes prévues dans les images servent uniquement la lisibilité en projection. Elles ne remplacent jamais les formulations sources, toutes présentes dans la transcription.
- Les codes internes de conception tels que `R11`, `R18` et `R24`, ainsi que le chemin `03-easy-checks/w3c-easy-checks-fr.md`, sont conservés uniquement parce qu’ils appartiennent au discours oral source. Ils ne deviennent jamais du texte visible dans l’image.

## Slide 01 - Partie III - Web accessible - TP - ÉTALON

- Correspondance : PPTX 79, `scripts/slides/28_chapitre-easy-checks.py`.
- Rôle : ouverture et carte du module.
- Famille de mise en page : ouverture illustrée.
- Idée principale : le parcours va du repérage des erreurs à une remontée d’audit rapide.
- Scène : une communicante observe une page web sur un grand écran. Devant elle, cinq étapes illustrées forment un parcours continu.
- Transformation : page inconnue -> cinq familles de vérification -> audit rapide.
- Liste blanche du futur visuel : `Partie III - Web accessible - TP` ; `Repérer les erreurs fréquentes` ; `Vérifier les images et les titres` ; `Contrôler les contrastes, les liens et le clavier` ; `Tester la langue, le zoom et les médias` ; `Examiner les formulaires et réaliser un audit rapide`.
- Ce que l’image seule doit faire comprendre : la séquence suit cinq étapes et se termine par une mise en pratique.
- Continuité : ouvre la partie et prépare la preuve chiffrée WebAIM.
- Contraintes critiques : exactement cinq étapes ; aucun numéro PPTX visible ; aucun faux logo ; les formulations sources « audit rapide » et « audit groupé » désignent ici un pré-diagnostic guidé, jamais un audit RGAA complet ; conserver la divergence documentée entre page au choix et site fourni.
- Alternative courte candidate : `Cinq étapes pour contrôler rapidement une page web.`

### Transcription exacte

### Partie III - Web accessible - TP

*Partie III | Plan*

1. Repérer les erreurs fréquentes
2. Vérifier les images et les titres
3. Contrôler les contrastes, les liens et le clavier
4. Tester la langue, le zoom et les médias
5. Examiner les formulaires et réaliser un audit rapide

### Discours oral exact

Annoncer les cinq thèmes qui structurent la partie III consacrée au Web. Préciser que les points de contrôle rapides permettent de repérer les principaux signaux d’alerte avant un audit approfondi. À la fin de la partie : mission d’audit groupé sur une page de votre choix.

## Slide 02 - WebAIM Million 2026 : le constat - ÉTALON

- Correspondance : PPTX 80, `scripts/slides/28a_webaim-million-2026.py`.
- Rôle : accroche par une preuve externe récente.
- Famille de mise en page : processus horizontal.
- Idée principale : les erreurs détectables automatiquement restent massives, mais les chiffres ne constituent pas un audit complet.
- Scène : une analyste examine un million de pages représentées par une grande mosaïque. Trois compteurs ressortent, puis un thermomètre mène vers une loupe d’audit humain.
- Transformation : volume massif -> signaux détectés -> besoin d’un contrôle humain.
- Liste blanche du futur visuel : `WebAIM Million 2026 : le constat` ; `95,9 %` ; `pages d’accueil avec au moins une erreur WCAG détectée` ; `56,1` ; `erreurs détectées en moyenne par page d’accueil` ; `1 437` ; `éléments par page en moyenne` ; `Thermomètre, pas audit complet`.
- Ce que l’image seule doit faire comprendre : l’automatisation révèle l’ampleur du problème sans prouver la conformité.
- Continuité : justifie la méthode puis prépare les six erreurs fréquentes.
- Contraintes critiques : trois chiffres exacts ; ne pas inventer de taux ; source WebAIM 2026 ; rouge réservé aux barrières probables.
- Alternative courte candidate : `Trois chiffres WebAIM montrent l’ampleur des erreurs détectées.`

### Transcription exacte

### WebAIM Million 2026 : le constat

*3. points de contrôle rapides | WebAIM Million 2026*

- **95,9 %** des pages d’accueil ont au moins une erreur WCAG détectée
- **56,1** erreurs détectées en moyenne par page d’accueil
- **1 437** éléments par page en moyenne : la complexité augmente

#### Comment lire ces chiffres

- WebAIM analyse automatiquement les pages d’accueil : c’est un thermomètre, pas un audit RGAA complet.
- L’absence d’erreur détectée ne prouve pas qu’une page est accessible.
- Mais la présence d’erreurs détectées révèle des barrières très probables pour les utilisateurs.

### Discours oral exact

Source : The WebAIM Million, mise à jour 2026, https://webaim.org/projects/million/. WebAIM a évalué les pages d’accueil des 1 000 000 de sites web les plus visités avec l’API WAVE autonome et des outils complémentaires de collecte technique. Résultats publiés à partir de données de février 2026 et dernière mise à jour indiquée au 30 mars 2026. Expliquer la limite méthodologique : WAVE détecte des erreurs probables et utiles à repérer, mais un résultat automatisé ne remplace pas un audit RGAA complet. Message pédagogique : l’objectif n’est pas de faire peur, mais de rendre visible un problème massif et mesurable. La slide suivante montre pourquoi les points de contrôle rapides sont un bon premier filtre.

## Slide 03 - Six erreurs qui justifient les points de contrôle rapides

- Correspondance : PPTX 81, `scripts/slides/28b_webaim-erreurs-frequentes.py`.
- Rôle : relier la preuve WebAIM au programme.
- Famille de mise en page : checklist ou processus.
- Idée principale : six familles concentrent 96 % des erreurs détectées et donnent des points d’entrée concrets.
- Scène : une page web présente six zones de défaut repérées par une loupe et nommées par leur famille d’erreur.
- Transformation : erreurs dispersées -> six familles -> points d’entrée.
- Liste blanche du futur visuel : titre ; `96 %` ; `Contraste` ; `Images` ; `Liens` ; `Formulaires` ; `Boutons` ; `Langue`.
- Ce que l’image seule doit faire comprendre : quelques familles permettent d’organiser une première vérification.
- Continuité : termine le cadrage et ouvre le contrôle des images.
- Contraintes critiques : six zones et six libellés exacts ; conserver les six pourcentages dans la transcription ; ne pas additionner ni modifier les données ; ne pas promettre une couverture RGAA complète.
- Alternative courte candidate : `Six familles d’erreurs orientent les contrôles rapides.`

### Transcription exacte

### Six erreurs qui justifient les points de contrôle rapides

*3. points de contrôle rapides | WebAIM Million 2026*

| Erreur fréquente | Pages concernées | Point d’entrée |
| --- | ---: | --- |
| Texte à faible contraste | 83,9 % | Contraste |
| Texte alternatif d’image manquant | 53,1 % | Images |
| Étiquette de formulaire manquante | 51 % | Formulaires |
| Liens vides | 46,3 % | Images / clavier (partiel) |
| Boutons vides | 30,6 % | Clavier / formulaires (partiel) |
| Langue du document absente | 13,5 % | Langue |

#### À retenir

- Ces six familles représentent 96 % des erreurs détectées par WebAIM.
- Les points de contrôle rapides donnent une méthode courte pour les repérer sans audit complet.

### Discours oral exact

Source : The WebAIM Million, mise à jour 2026, https://webaim.org/projects/million/. Les pourcentages indiquent la part des pages d’accueil concernées par chaque type d’erreur. Faire le lien avec le programme : les stagiaires vont maintenant apprendre à repérer ces familles par des gestes simples - contraste, images, titres, clavier, langue, formulaires. Préciser que les liens et boutons vides ne sont pas un Point de contrôle rapide autonome dans ce module, mais qu’ils ressortent souvent via les tests images, clavier et formulaires. Insister sur la logique de pré-diagnostic : on ne remplace pas l’audit RGAA, on sait mieux quoi remonter.

## Slide 04 - Texte alternatif : 4 types d’images, 4 décisions

- Correspondance : PPTX 82, `scripts/slides/29_check01_alt-types.py`.
- Rôle : distinguer les quatre décisions possibles face à une image.
- Famille de mise en page : tableau pédagogique.
- Idée principale : le rôle de l’image détermine l’alternative à fournir.
- Scène : quatre images concrètes passent chacune par une décision distincte : bâtiment, séparateur, logo-bouton et infographie.
- Transformation : image observée -> type identifié -> traitement adapté.
- Liste blanche du futur visuel : titre ; `Informative` ; `Décorative` ; `Fonctionnelle` ; `Complexe` ; `Texte court` ; `alt=""` ; `Nommer l’action` ; `Description longue`.
- Ce que l’image seule doit faire comprendre : il n’existe pas un texte alternatif unique pour toutes les images.
- Continuité : pose les quatre cas puis prépare les règles de rédaction.
- Contraintes critiques : exactement quatre types ; l’image décorative du Web garde un alt vide ; ne pas importer l’exception propre aux réseaux sociaux.
- Alternative courte candidate : `Quatre types d’images appellent quatre traitements différents.`

### Transcription exacte

### Texte alternatif : 4 types d’images, 4 décisions

*3. points de contrôle rapides | 1. Texte alternatif des images*

Le texte alternatif est le sous-titre de l’image - sans lui, une partie du message devient muette.

1. **Informative** - Apporte une info : photo d’un bâtiment, graphique. → texte alternatif court.
2. **Décorative** - Pure ambiance : séparateur, icône floue. → `alt=""` (vide).
3. **Fonctionnelle** - Dans un lien ou un bouton : logo cliquable, picto. → nommer l’action attendue.
4. **Complexe** - Diagramme, schéma, infographie. → texte court + description longue à part.

### Discours oral exact

Faire deviner : « Cette carte de métro, quel type ? » (complexe). Insister sur le décoratif - c’est le plus mal compris. Un séparateur graphique avec `alt="ligne bleue"` pollue le lecteur d’écran. Règle mnémo : si je retire l’image, est-ce que je perds une info ? Si non → alt vide.

## Slide 05 - Rédiger un texte alternatif qui sert vraiment

- Correspondance : PPTX 83, `scripts/slides/30_check01_alt-redaction.py`.
- Rôle : donner les règles de rédaction et deux pièges fréquents.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : un texte alternatif utile restitue l’information nécessaire dans le contexte.
- Scène : la communicante transforme un nom de fichier inutile en une phrase courte représentée par trois traits gris sans pseudo-texte. Cinq repères entourent le champ édité.
- Transformation : nom de fichier -> rédaction contextuelle -> information comprise.
- Liste blanche du futur visuel : titre ; `Concis` ; `Objectif` ; `Sans « image de »` ; `Contextuel` ; `Ponctué` ; `IMG_4578.jpg`.
- Ce que l’image seule doit faire comprendre : la qualité dépend du contexte, pas d’une longueur magique.
- Continuité : donne les règles puis prépare le vote passe ou échoue.
- Contraintes critiques : cinq règles seulement ; conserver le point final ; ne pas inventer de limite de caractères ; la phrase cible reste une simulation sans lettres, car aucun exemple rédigé n’est autorisé dans la liste blanche.
- Alternative courte candidate : `Cinq règles transforment un nom de fichier en alternative utile.`

### Transcription exacte

### Rédiger un texte alternatif qui sert vraiment

*3. points de contrôle rapides | 1. Texte alternatif des images*

#### 5 règles pour un texte alternatif utile :

- Concis : une phrase courte, centrée sur l’information utile
- Objectif : décrit, ne commente pas
- Pas de « photo de » ni « image de » - le lecteur d’écran le dit déjà
- Contextuel : ce qui compte dans cette page, pas tout ce qui est visible
- Ponctué : point final, pour que le lecteur marque la pause

#### Piège fréquent

- Un nom de fichier (IMG_4578.jpg) en guise de texte alternatif = information perdue
- Un texte alternatif qui décrit la décoration au lieu du contenu utile

### Discours oral exact

Prédiction avant de montrer les 5 règles : « Qu’est-ce qui rend un texte alternatif vraiment utile ? » La bonne réponse n’est pas une longueur magique : c’est le contexte. Exemple live : une photo du ministère avec `alt="photo du ministère de Bercy prise en 2023"` → refactorer en `"Ministère de Bercy, façade ouest."` - même info, moitié de caractères.

## Slide 06 - Texte alternatif : passe ou échoue ?

- Correspondance : PPTX 84, `scripts/slides/31_check01_alt-exemples.py`.
- Rôle : récupération active par comparaison.
- Famille de mise en page : tableau pédagogique.
- Idée principale : le bon texte alternatif nomme l’information ou l’action utile selon le rôle de l’image.
- Scène : cinq objets passent devant un poste de contrôle. Trois obtiennent un verdict positif, deux repartent en correction.
- Transformation : alt proposé -> analyse du rôle -> verdict.
- Liste blanche du futur visuel : titre ; `Passe` ; `Échoue` ; `Accueil` ; `image` ; `alt=""` ; `Voir détail ci-dessous` ; `Rechercher`.
- Ce que l’image seule doit faire comprendre : décrire l’objet ne suffit pas quand l’image déclenche une action.
- Continuité : consolide le contrôle des images puis passe au titre de page.
- Contraintes critiques : cinq cas exacts dans la transcription ; ne pas inverser les verdicts ; le logo lié est fonctionnel.
- Alternative courte candidate : `Cinq textes alternatifs passent ou échouent selon leur utilité.`

### Transcription exacte

### Texte alternatif : passe ou échoue ?

*3. points de contrôle rapides | 1. Texte alternatif des images*

| Image | Alt proposé | Verdict |
| --- | --- | --- |
| Logo ministère dans l’en-tête (lien vers l’accueil) | `alt="Ministère de l’Économie - Accueil"` | OK - fonctionnelle, action nommée |
| Photo d’illustration d’un article sur la fraude | `alt="image"` | KO - aucune information |
| Séparateur graphique entre deux sections | `alt=""` | OK - décorative, alt vide |
| Graphique de répartition budgétaire | `alt="graphique montrant la répartition du budget 2026, voir détail ci-dessous"` | OK - alt court + renvoi au détail |
| Icône loupe dans un bouton de recherche | `alt="loupe"` | KO - décrit l’image, pas l’action (devrait être « Rechercher ») |

### Discours oral exact

Masquer la colonne verdict et demander à voter pour chaque ligne. Débrief rapide après chaque cas : pourquoi KO ? que rédiger à la place ? Ligne 5 (loupe) est le piège le plus commun : on décrit ce qu’on voit, pas ce que l’utilisateur fera en cliquant.

## Slide 07 - Titre de page : l’étiquette qui oriente

- Correspondance : PPTX 85, `scripts/slides/32_check02_titre-page.py`.
- Rôle : expliquer l’utilité du titre de page dans l’onglet et au lecteur d’écran.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : chaque page doit posséder une étiquette unique, descriptive et actualisée.
- Scène : plusieurs onglets identiques désorientent une personne, puis des titres distincts rendent chaque destination reconnaissable.
- Transformation : onglets « Accueil » -> titres précis -> orientation immédiate.
- Liste blanche du futur visuel : titre ; `Unique` ; `Contenu puis site` ; `Mis à jour` ; `Résultats de recherche : accessibilité` ; `Accueil` ; `Untitled Document`.
- Ce que l’image seule doit faire comprendre : un bon titre permet de retrouver la bonne page sans l’ouvrir.
- Continuité : passe de l’étiquette de page à la structure interne des titres.
- Contraintes critiques : conserver les trois exemples ; ne pas présenter une règle de nommage universelle au-delà de la source.
- Alternative courte candidate : `Des titres uniques rendent les onglets immédiatement identifiables.`

### Transcription exacte

### Titre de page : l’étiquette qui oriente

*3. points de contrôle rapides | 2. Titre de page*

Le titre de page est la 1ʳᵉ chose que lit un lecteur d’écran et la seule chose visible dans l’onglet.

#### Ce qu’il faut vérifier :

- Chaque page a un titre unique, différent des autres pages du site
- Le titre décrit le contenu puis le nom du site (« Déclarer - impots.gouv.fr »)
- Il change quand le contenu principal change (recherche, étape de formulaire)

#### Exemples

- OK : « Résultats de recherche : accessibilité - Ministère de la Culture »
- KO : « Accueil » sur chaque page du site
- KO : « Untitled Document » (oubli fréquent sur les PDF)

### Discours oral exact

Démo live : ouvrir 3 onglets de sites publics, demander lequel est identifiable juste à l’étiquette. Piège des CMS : beaucoup héritent du titre du template - toutes les pages « Accueil ». Outil : survoler l’onglet dans le navigateur ou regarder la balise `<title>`.

## Slide 08 - Titres : la hiérarchie qui structure

- Correspondance : PPTX 86, `scripts/slides/33_check03_titres-hierarchie.py`.
- Rôle : rendre visible le plan sémantique d’une page.
- Famille de mise en page : processus horizontal.
- Idée principale : les titres forment une table des matières navigable, pas une simple apparence graphique.
- Scène : une personne parcourt une page par une arborescence H1, H2, H3. Un saut vers H4 crée une marche cassée.
- Transformation : gros texte visuel -> hiérarchie réelle -> navigation fiable.
- Liste blanche du futur visuel : titre ; `H1` ; `H2` ; `H3` ; `H2 → H4` ; `Titre réel` ; `Gras/gros ≠ titre`.
- Ce que l’image seule doit faire comprendre : l’ordre des niveaux sert de plan de navigation.
- Continuité : expose la règle puis prépare trois méthodes de vérification.
- Contraintes critiques : un seul H1 selon la source ; aucun niveau inventé ; montrer le saut comme une erreur.
- Alternative courte candidate : `Une arborescence H1, H2, H3 structure la navigation.`

### Transcription exacte

### Titres : la hiérarchie qui structure

*3. points de contrôle rapides | 3. Titres et hiérarchie*

Un utilisateur de lecteur d’écran navigue de titre en titre comme on navigue dans une table des matières.

#### 3 règles qui font passer le check :

- Un seul H1 par page, qui reprend le sujet principal
- Les niveaux s’emboîtent sans saut : H1 → H2 → H3, jamais H2 → H4
- Un titre n’est pas une simple mise en forme gras/gros - c’est une balise `<h1>` à `<h6>`

### Discours oral exact

Analogie : un document Word où tout le texte est en gras 18 pt n’a pas de plan. Même principe sur le web. Prédire : « Quel est le saut de hiérarchie le plus fréquent ? » (H2 → H4, parce que H3 « n’est pas assez joli »). Outil : l’extension HeadingsMap pour Chrome / Firefox affiche l’arbre des titres en un clic.

## Slide 09 - Titres : 3 façons de vérifier

- Correspondance : PPTX 87, `scripts/slides/34_check03_titres-outils.py`.
- Rôle : fournir trois méthodes de contrôle comparables.
- Famille de mise en page : tableau pédagogique.
- Idée principale : le même plan de titres peut être vérifié avec une extension, un plan de document ou l’inspecteur.
- Scène : trois outils alignés observent la même page simulée et révèlent la même arborescence.
- Transformation : page visuelle -> outil de lecture -> structure révélée.
- Liste blanche du futur visuel : titre ; `HeadingsMap` ; `Plan de document` ; `Inspecter` ; `Arbre des titres` ; `Niveaux manquants` ; `H1, H2, H3`.
- Ce que l’image seule doit faire comprendre : trois chemins permettent de vérifier une même structure.
- Continuité : clôt les titres puis ouvre le contraste.
- Contraintes critiques : conserver les noms d’outils ; ne pas ajouter de marque ou de logo ; garder le code dans la transcription.
- Alternative courte candidate : `Trois outils révèlent le plan réel des titres d’une page.`

### Transcription exacte

### Titres : 3 façons de vérifier

*3. points de contrôle rapides | 3. Titres et hiérarchie*

| Méthode | Comment faire | Ce que vous cherchez |
| --- | --- | --- |
| Extension HeadingsMap | Installer l’extension, ouvrir le panneau latéral. | L’arbre complet des titres s’affiche, les anomalies en rouge. |
| Plan de document | Extension Web Developer → Information → View Document Outline. | Le plan liste les titres réels et signale les niveaux manquants. |
| Clic droit « Inspecter » | Rechercher `h1`, `h2`, `h3` dans l’onglet Éléments. | Un seul `<h1>`, pas de saut, pas de titre factice (`<div class="titre">`). |

### Discours oral exact

Démo HeadingsMap sur legifrance.gouv.fr ou service-public.fr. Engagement (R24) : chaque stagiaire teste sa page d’accueil personnelle ou professionnelle ce soir et note le nombre de H1 détectés - idéalement 1, souvent 0 ou 3.

## Slide 10 - Contraste : un seuil chiffré, pas une opinion

- Correspondance : PPTX 88, `scripts/slides/35_check04_contraste-principe.py`.
- Rôle : remplacer l’impression visuelle par une mesure.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : le contraste se contrôle avec des rapports précis selon le type de texte ou de composant.
- Scène : un même écran est observé dans plusieurs conditions de lumière. Trois jauges chiffrées donnent le verdict.
- Transformation : « joli gris » -> mesure -> décision.
- Liste blanche du futur visuel : titre ; `4,5:1` ; `Texte normal` ; `3:1` ; `Texte large et composants graphiques` ; `7:1` ; `Niveau AAA` ; `Mesurer`.
- Ce que l’image seule doit faire comprendre : l’œil ne suffit pas, les rapports tranchent.
- Continuité : pose les seuils puis prépare les outils de mesure.
- Contraintes critiques : chiffres exacts ; conserver les définitions de texte large ; rouge uniquement pour un échec mesuré.
- Alternative courte candidate : `Trois rapports chiffrés remplacent le jugement visuel du contraste.`

### Transcription exacte

### Contraste : un seuil chiffré, pas une opinion

*3. points de contrôle rapides | 4. Contraste des couleurs*

Ce que vous trouvez « joli gris » peut devenir illisible selon l’écran, la lumière ou la vision de l’utilisateur.

- **4,5:1** - Texte normal (sous 18 pt)
- **3:1** - Texte large (18 pt+ ou 14 pt gras) et composants graphiques
- **7:1** - Niveau AAA - recommandé pour texte dense

#### Ce qui compte :

- Le rapport entre la couleur du texte et celle du fond (ou l’arrière-plan visible)
- Sur un dégradé ou une image, mesurer à l’endroit le moins contrasté
- Ne pas se fier seulement à l’œil - mesurer avec un outil

### Discours oral exact

Analogie : lire un SMS à 3 h du matin sur un écran en plein soleil - c’est ce que vit un malvoyant en permanence avec un contraste trop faible. Rappeler : le contraste fait partie des défauts les plus fréquents dans les observations WebAIM Million.

## Slide 11 - Contraste : 3 outils à avoir sous la main

- Correspondance : PPTX 89, `scripts/slides/36_check04_contraste-outils.py`.
- Rôle : transformer la règle en mesure opérationnelle.
- Famille de mise en page : tableau pédagogique.
- Idée principale : trois outils couvrent la page web, le choix de palette et les maquettes ou documents.
- Scène : une pipette prélève deux couleurs et les fait passer successivement dans trois postes de mesure.
- Transformation : deux couleurs -> mesure -> verdict immédiat.
- Liste blanche du futur visuel : titre ; `DevTools` ; `WebAIM Contrast Checker` ; `Colour Contrast Analyser` ; `2,85:1` ; `Échec`.
- Ce que l’image seule doit faire comprendre : le choix de l’outil dépend du support à tester.
- Continuité : clôt le contraste puis ouvre le lien d’évitement.
- Contraintes critiques : conserver les trois noms ; ne pas afficher de faux logo ; préserver `#999 sur #FFF` et `2,85:1` dans la transcription.
- Alternative courte candidate : `Trois outils mesurent le contraste de pages, palettes et maquettes.`

### Transcription exacte

### Contraste : 3 outils à avoir sous la main

*3. points de contrôle rapides | 4. Contraste des couleurs*

| Outil | Usage | Quand l’utiliser |
| --- | --- | --- |
| DevTools Chrome / Firefox | Clic droit sur un texte → Inspecter → pastille de couleur. | Mesure ponctuelle pendant la rédaction ou la relecture. |
| WebAIM Contrast Checker | webaim.org/resources/contrastchecker - coller les deux couleurs hex. | Avant de choisir une charte graphique ou un thème. |
| Colour Contrast Analyser (CCA) | App desktop - pipette qui mesure n’importe quelle zone d’écran. | Tester des maquettes Figma, des captures d’écran, des PDF. |

#### Piège classique

- Texte gris clair sur fond blanc (#999 sur #FFF) : 2,85:1 - échec même en texte large
- Bouton bleu avec texte bleu marine « moderne » : souvent sous le seuil

### Discours oral exact

Démo live : prendre la page d’accueil de Bercy et mesurer 3 textes au hasard. Laisser les stagiaires deviner avant la mesure. Engagement (R24) : choisissez votre outil préféré d’ici la fin de la session et testez 5 couleurs de votre charte dans la semaine.

## Slide 12 - Lien d’évitement : le raccourci vers le contenu

- Correspondance : PPTX 90, `scripts/slides/37_check05_lien-evitement.py`.
- Rôle : matérialiser le gain du premier lien clavier.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : un lien d’évitement permet de contourner le menu et d’atteindre directement le contenu principal.
- Scène : une personne au clavier fait face à un long escalier « Menu ». Un raccourci visible au focus agit comme un ascenseur vers « Contenu ».
- Transformation : traversée du menu -> lien visible au focus -> contenu atteint.
- Liste blanche du futur visuel : titre ; `Menu` ; `Contenu` ; `Visible au focus` ; `Tab` ; `Entrée`.
- Ce que l’image seule doit faire comprendre : le raccourci évite une répétition longue à chaque page.
- Continuité : introduit le clavier puis prépare le test sans souris.
- Contraintes critiques : le lien peut être masqué avant le focus ; il devient visible au focus ; ne pas montrer une ancre qui mène au menu.
- Alternative courte candidate : `Un lien visible au focus contourne le menu et rejoint le contenu.`

### Transcription exacte

### Lien d’évitement : le raccourci vers le contenu

*3. points de contrôle rapides | 5. Lien d'évitement*

Sans lien d’évitement, un utilisateur clavier doit souvent traverser tout le menu avant d’atteindre le contenu.

#### Ce qu’il faut vérifier :

- Le premier lien interactif permet d’aller directement au contenu principal
- Il devient visible dès qu’il a le focus, même s’il était masqué
- Il mène au bloc principal via une ancre (#contenu, #main)

#### Démo en 3 Tab

- Ouvrez gouvernement.fr et appuyez Tab : le lien « Contenu » apparaît en haut
- Entrée → vous voilà au contenu, menu contourné

### Discours oral exact

Analogie : l’ascenseur dans un immeuble. Sans ascenseur, chacun monte les 10 étages à pied - y compris les personnes qui ne peuvent pas. Faire deviner : combien de tabulations sur la page de leur intranet pour arriver au contenu ? Rappel : le lien d’évitement peut être masqué visuellement mais doit apparaître au focus clavier.

## Slide 13 - Naviguer sans souris : le test qui change tout

- Correspondance : PPTX 91, `scripts/slides/38_navigation-clavier-ouverture.py`.
- Rôle : ouverture active du contrôle clavier.
- Famille de mise en page : ouverture illustrée.
- Idée principale : un focus invisible suffit à désorienter complètement une personne qui navigue sans souris.
- Scène : une personne éloigne la souris, pose les mains sur le clavier et suit un repère de focus dans une page. Le repère disparaît au milieu du parcours.
- Transformation : navigation visible -> focus perdu -> besoin d’un test clavier.
- Liste blanche du futur visuel : titre ; `En 15 minutes` ; `5 touches` ; `3 signaux` ; `Test en 3 minutes` ; `Focus invisible`.
- Ce que l’image seule doit faire comprendre : retirer la souris révèle immédiatement les défauts de parcours.
- Continuité : crée le besoin puis présente les cinq touches.
- Contraintes critiques : associer visuellement `En 15 minutes` aux trois acquis ; `Test en 3 minutes` qualifie seulement la reproduction de l’expérience ; le focus disparaît dans la scène ; ne pas afficher de lecteur d’écran comme substitut au test clavier.
- Alternative courte candidate : `Une personne perd son repère quand le focus clavier disparaît.`

### Transcription exacte

### Naviguer sans souris : le test qui change tout

*3. points de contrôle rapides | 6. Focus et navigation clavier*

Quand on navigue au clavier, un focus invisible suffit à perdre toute la page.

#### En 15 minutes, vous saurez :

- Utiliser 5 touches pour tester n’importe quelle page
- Repérer 3 signaux qui trahissent un défaut d’accessibilité
- Reproduire l’expérience d’un lecteur d’écran en 3 minutes

### Discours oral exact

Annoncer le rattachement : cette séquence correspond au point de contrôle rapide n° 6 du W3C, focus et navigation clavier : visibilité du focus, parcours, activation et absence de piège (tabulation, activation, lecture). Corpus de référence local : 03-easy-checks/w3c-easy-checks-fr.md. Ouvrir par une question : « Posez la main loin de la souris. Combien de temps tenez-vous sur votre site préféré ? » Laisser 10 secondes de silence. Analogie : le clavier est le GPS de votre site - s’il ne s’allume pas, personne ne trouve la route. Objectif : transformer le regard des stagiaires. Après cette slide, ils ne regarderont plus une page comme avant.

## Slide 14 - 5 touches, 3 intentions

- Correspondance : PPTX 92, `scripts/slides/39_cinq-touches.py`.
- Rôle : donner le vocabulaire moteur du test clavier.
- Famille de mise en page : checklist ou processus.
- Idée principale : cinq touches suffisent pour naviguer, agir et lire lors d’un contrôle rapide.
- Scène : un clavier agrandi met en évidence cinq touches regroupées en trois chemins d’action vers une page web.
- Transformation : touches isolées -> trois intentions -> test complet.
- Liste blanche du futur visuel : titre ; `Naviguer` ; `Tab` ; `Shift + Tab` ; `Agir` ; `Entrée` ; `Espace` ; `Lire` ; `Flèches ↑ ↓`.
- Ce que l’image seule doit faire comprendre : le test clavier repose sur trois intentions simples.
- Continuité : donne les commandes puis prépare les trois signaux d’alerte.
- Contraintes critiques : cinq touches exactes ; ne pas ajouter Échap ; ne pas inverser Entrée et Espace.
- Alternative courte candidate : `Cinq touches couvrent navigation, action et lecture.`

### Transcription exacte

### 5 touches, 3 intentions

*3. points de contrôle rapides | 6. Focus et navigation clavier*

Naviguer → Tab / Shift+Tab    Agir → Entrée / Espace    Lire → Flèches ↑ ↓

| Touche | À quoi elle sert | Ce qu’il faut vérifier |
| --- | --- | --- |
| Tab | Avancer sur l’élément interactif suivant (lien, bouton, champ). | Le focus se déplace et reste visible à chaque étape. |
| Shift + Tab | Reculer sur l’élément interactif précédent. | L’ordre inverse est logique, sans saut imprévu. |
| Entrée | Activer un lien ou soumettre un formulaire. | L’action attendue se déclenche immédiatement. |
| Barre d’espace | Cocher, décocher, sélectionner un bouton radio. | L’état coché / non coché est annoncé vocalement. |
| Flèches ↑ ↓ | Lire le contenu ligne par ligne avec un lecteur d’écran. | Le texte alternatif des images est lu à haute voix. |

### Discours oral exact

Faire deviner avant de révéler la 3e colonne (R11) : « Devinez ce qui doit se passer quand j’appuie sur Tab ». Insister sur l’indicateur de focus visible - c’est LE critère qui tombe en premier. Piège fréquent : un site qui n’annonce jamais l’état d’une case à cocher (ligne Espace).

## Slide 15 - 3 signaux qui trahissent un défaut

- Correspondance : PPTX 93, `scripts/slides/40_signaux-alerte.py`.
- Rôle : transformer le parcours clavier en diagnostic observable.
- Famille de mise en page : checklist ou processus.
- Idée principale : trois signaux suffisent à prouver qu’un test clavier doit entrer dans la routine.
- Scène : une même page montre successivement un focus qui s’efface, un ordre de parcours qui saute et une case cochée sans annonce. Une personne consigne les trois observations.
- Transformation : tabulation -> anomalie visible ou audible -> signal consigné.
- Liste blanche du futur visuel final : titre ; `Le focus disparaît` ; `L’ordre est illogique` ; `L’état n’est pas annoncé` ; `Scannez-moi !` ; `https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/`.
- Ce que l’image seule doit faire comprendre : les défauts clavier laissent trois traces simples à repérer.
- Continuité : prépare immédiatement la mission sur le site d’entraînement.
- Contraintes critiques : trois signaux exacts ; réserver en bas une zone vide pour la superposition déterministe ; le prompt ImageGen interdit tout QR code, toute URL et tout pseudo-texte dans cette zone ; superposer ensuite `Scannez-moi !`, le QR code fonctionnel et l’URL exacte ; ne pas culpabiliser les équipes.
- Alternative courte candidate : `Trois défauts révèlent une navigation clavier inaccessible.`

### Transcription exacte

### 3 signaux qui trahissent un défaut

*3. points de contrôle rapides | 6. Focus et navigation clavier*

1. **Le focus disparaît** - Plus de contour visible pendant la tabulation. L’utilisateur est perdu dès la 3ᵉ touche Tab.
2. **L’ordre est illogique** - Le focus saute à droite avant le menu à gauche. Le lecteur d’écran parcourt la page dans le désordre.
3. **L’état n’est pas annoncé** - Une case qui coche sans dire « coché ». L’information est invisible pour qui ne voit pas l’écran.

Scannez-moi !

https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/

### Discours oral exact

Avant de révéler les 3 cartes, demander : « Quel est le signal qui vous semble le plus grave ? » Laisser parler 2 stagiaires. Rappel rassurant (R18) : détecter un de ces signaux ne sert pas à désigner un coupable, mais à prouver qu’un test clavier doit entrer dans la routine de publication. Faire ouvrir le site d’entraînement : https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/

## Slide 16 - Votre mission - ÉTALON

- Correspondance : PPTX 94, `scripts/slides/41_mission-clavier.py`.
- Rôle : mise en pratique immédiate sur le site d’entraînement.
- Famille de mise en page : synthèse et passage à l’action.
- Idée principale : un parcours clavier court suffit pour observer, noter et qualifier des défauts réels.
- Scène : la communicante fil rouge cache sa souris, teste une page au clavier et note les trois signaux sur une fiche. Le QR code et l’URL restent clairement séparés de l’illustration.
- Transformation : consigne -> test de dix tabulations -> signaux détectés.
- Liste blanche du futur visuel final : titre ; `Cachez votre souris` ; `10 fois Tab` ; `Entrée / Espace` ; `3 signaux` ; `Votre permis clavier` ; `Scannez-moi !` ; `https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/`.
- Ce que l’image seule doit faire comprendre : l’exercice demande de tester une page réelle sans souris et d’identifier les signaux vus précédemment.
- Continuité : met le clavier en pratique puis revient à des contrôles de page plus généraux.
- Contraintes critiques : quatre consignes exactes dans la transcription ; réserver une zone vide pour la superposition déterministe ; le prompt ImageGen interdit `Scannez-moi !`, tout QR code, toute URL et tout pseudo-texte dans cette zone ; superposer ensuite `Scannez-moi !`, le QR code vers l’URL exacte et le lien visible ; aucun chronomètre de trente minutes.
- Alternative courte candidate : `Une participante teste le site d’entraînement uniquement au clavier.`

### Transcription exacte

### Votre mission

*3. points de contrôle rapides | 6. Focus et navigation clavier*

#### Site d’entraînement :

- Cachez votre souris derrière l’écran
- Tabulez 10 fois et notez chaque fois que le focus disparaît
- Essayez Entrée sur un bouton, Espace sur une case à cocher
- Listez les pièges détectés et associez-les aux 3 signaux

#### Objectif : votre permis clavier

- 1 signal détecté = vous avez l’œil
- 3 signaux détectés = vous êtes auditeur clavier

Scannez-moi !

https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/

### Discours oral exact

Distribuer l’URL du site d’entraînement (fabriqué en interne, avec pièges volontaires). Chronométrer 5 minutes. Débriefer en collectif : quel signal a été le plus difficile à repérer ? pourquoi ? Clore le module avec la question métacognitive (R25) : « Qu’est-ce qui vous aurait aidé à repérer plus vite ? » Engagement : chaque stagiaire annonce ce qu’il testera dès demain sur son propre site.

## Slide 17 - Langue de la page : l’accent juste du lecteur d’écran

- Correspondance : PPTX 95, `scripts/slides/42_check07_langue.py`.
- Rôle : expliquer l’effet concret de la langue déclarée.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : la langue du code permet au lecteur d’écran d’utiliser la bonne prononciation.
- Scène : un même passage simulé par des barres gris bleuté est lu par une voix avec un mauvais accent, puis par une voix adaptée après la pose de `lang="fr"`. Un second passage simulé porte `lang="en"`, sans mot lisible hors liste blanche.
- Transformation : langue absente -> mauvaise prononciation -> langue déclarée.
- Liste blanche du futur visuel : titre ; `lang="fr"` ; `lang="en"` ; `fr, en, de, es` ; `Code source` ; `Web Developer`.
- Ce que l’image seule doit faire comprendre : un code langue court change la restitution vocale.
- Continuité : contrôle la lecture vocale puis prépare le zoom visuel.
- Contraintes critiques : préserver les exemples de code ; ne pas transformer la slide en cours HTML ; conserver les deux méthodes sans coder dans la transcription.
- Alternative courte candidate : `La langue déclarée règle la prononciation du lecteur d’écran.`

### Transcription exacte

### Langue de la page : l’accent juste du lecteur d’écran

*3. points de contrôle rapides | 7. Langue de la page*

Sans langue déclarée, le lecteur d’écran peut choisir une mauvaise prononciation et rendre le texte pénible à écouter.

#### Ce qu’il faut vérifier :

- La balise `<html>` porte un attribut `lang` (ex. `lang="fr"`)
- Les passages dans une autre langue sont balisés : `<span lang="en">workshop</span>`
- Le code langue suit la norme ISO 639 : fr, en, de, es - pas « français »

#### Comment vérifier sans coder

- Clic droit → Afficher le code source → regarder la 1ʳᵉ ligne `<html lang="…">`
- Ou extension « Web Developer » → Information → View Document Language

### Discours oral exact

Démo : activer VoiceOver ou NVDA sur une page sans lang et comparer la prononciation. Analogie : un comédien à qui on ne dit pas dans quelle langue jouer - il bute sur chaque mot. Piège : un gabarit peut être visuellement français tout en oubliant `lang="fr"` dans le code.

## Slide 18 - Zoom à 200 % : tout doit rester lisible

- Correspondance : PPTX 96, `scripts/slides/43_check08_zoom.py`.
- Rôle : faire tester la robustesse de l’interface agrandie.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : à 200 %, le service doit rester lisible, navigable et utilisable.
- Scène : la communicante fil rouge agrandit une page de 100 % à 200 %. Le contenu se réorganise sans texte coupé, superposé ni défilement horizontal.
- Transformation : page à 100 % -> zoom à 200 % -> service toujours utilisable.
- Liste blanche du futur visuel : titre ; `100 % → 200 %` ; `Lisible` ; `Navigable` ; `Utilisable` ; `Ctrl + / Cmd +`.
- Ce que l’image seule doit faire comprendre : zoomer ne doit pas casser l’usage de la page.
- Continuité : termine les contrôles d’affichage puis ouvre les médias.
- Contraintes critiques : 200 % exact ; ne pas confondre zoom navigateur et agrandissement d’une image ; conserver les deux raccourcis.
- Alternative courte candidate : `Une page reste utilisable après un zoom à 200 %.`

### Transcription exacte

### Zoom à 200 % : tout doit rester lisible

*3. points de contrôle rapides | 8. Zoom à 200 %*

À 200 %, votre site doit rester le même service : lisible, navigable et utilisable.

#### Ce qu’il faut vérifier :

- À 200 % de zoom, aucun texte n’est coupé ni superposé
- Pas d’apparition d’un défilement horizontal sur une page classique
- Les menus, boutons et formulaires restent utilisables, pas seulement visibles

#### Comment tester

- Ctrl + (ou Cmd + sur Mac) pour zoomer jusqu’à 200 % - répéter 4 fois depuis 100 %
- Parcourir la page : formulaire, menu, pied de page. Si ça casse, le check échoue

### Discours oral exact

Analogie : zoomer, c’est mettre des lunettes. Votre site doit rester opérationnel avec les lunettes. Test immédiat : demander à 2 stagiaires de zoomer à 200 % sur leur intranet et de tenter de remplir un formulaire. Souvent, un champ ou un bouton devient inaccessible. Ne pas confondre zoom navigateur (OK) et zoom tactile (mobile) - les deux doivent fonctionner.

## Slide 19 - Sous-titres : le son que tout le monde lit

- Correspondance : PPTX 97, `scripts/slides/44_check09_sous-titres-principe.py`.
- Rôle : poser le contrôle minimal des vidéos parlées.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : les sous-titres synchronisés rendent le son accessible quand il manque ou ne peut pas être entendu.
- Scène : dans un train bruyant, plusieurs personnes suivent une vidéo grâce au bouton CC et aux sous-titres, y compris une indication sonore.
- Transformation : son indisponible -> sous-titres activés -> contenu compris.
- Liste blanche du futur visuel : titre ; `Sous-titres synchronisés` ; `Paroles et sons essentiels` ; `CC` ; `Activables`.
- Ce que l’image seule doit faire comprendre : les sous-titres servent dans plusieurs contextes, pas seulement à un public unique.
- Continuité : établit le principe puis prépare la relecture des sous-titres automatiques.
- Contraintes critiques : ne pas remplacer les sous-titres par une transcription ; bouton CC activable ; sons importants inclus.
- Alternative courte candidate : `Des sous-titres synchronisés rendent une vidéo compréhensible sans son.`

### Transcription exacte

### Sous-titres : le son que tout le monde lit

*3. points de contrôle rapides | 9. Sous-titres vidéo*

Une vidéo sans sous-titres devient inutilisable dès que le son manque, est coupé ou ne peut pas être entendu.

#### Ce qu’il faut vérifier :

- La vidéo propose des sous-titres synchronisés (pas seulement une transcription)
- Les sous-titres incluent les paroles ET les informations sonores importantes : « (rires) », « (sonnerie) »
- Ils sont activables/désactivables par l’utilisateur (bouton CC)

### Discours oral exact

Analogie : dans un train bruyant, même un entendant lit les sous-titres. Bénéficiaires (faire deviner) : personnes sourdes ou malentendantes, utilisateurs en open space, apprenants d’une langue étrangère, personnes qui préfèrent lire. Nuance capitale : une transcription écrite sur la page n’est pas un sous-titre - les deux sont utiles, pas interchangeables.

## Slide 20 - Sous-titres auto : brouillon utile, livrable à relire

- Correspondance : PPTX 98, `scripts/slides/45_check09_sous-titres-auto.py`.
- Rôle : corriger la confiance excessive dans l’automatisation.
- Famille de mise en page : processus horizontal.
- Idée principale : la génération automatique accélère le brouillon, mais une personne doit relire avant publication.
- Scène : une piste de sous-titres simulée par des barres gris bleuté contient quatre zones soulignées en rouge, sans mot lisible. La communicante fil rouge les corrige puis vérifie le rendu.
- Transformation : brouillon automatique -> relecture humaine -> sous-titres publiables.
- Liste blanche du futur visuel : titre ; `Générer` ; `Relire` ; `Tester le rendu` ; `Noms et chiffres` ; `Ponctuation et sons`.
- Ce que l’image seule doit faire comprendre : l’automatique est une étape, pas le livrable final.
- Continuité : sécurise les sous-titres puis distingue la transcription autonome.
- Contraintes critiques : conserver l’exemple de ponctuation dans la transcription ; ne pas promouvoir un outil unique ; sous-titres non masqués.
- Alternative courte candidate : `Une relecture humaine corrige les sous-titres automatiques avant publication.`

### Transcription exacte

### Sous-titres auto : brouillon utile, livrable à relire

*3. points de contrôle rapides | 9. Sous-titres vidéo*

#### Pourquoi l’auto ne suffit pas :

- Les sous-titres automatiques peuvent déformer les mots, surtout les noms propres et acronymes
- Noms propres, acronymes, chiffres : souvent mal reconnus
- Ponctuation absente : « on mange les enfants » vs « on mange, les enfants »
- Pas d’indication sonore non verbale (musique, applaudissements)

#### Méthode recommandée

- Générer l’auto (YouTube, Whisper, outil interne) pour accélérer le brouillon
- Relire : noms, chiffres, ponctuation et [indications sonores]
- Tester le rendu : 2 lignes max, contraste fort, sous-titres non masqués

### Discours oral exact

Faire deviner : « Quels mots un sous-titrage auto rate le plus souvent ? » Exemple concret à projeter : une vidéo ministérielle avec sous-titres automatiques - pointer 3 erreurs. Règle d’or (R18) : l’automatique est un allié pour brouillonner, mais la publication demande une relecture humaine. Faire aussi vérifier le cadrage sur les formats réseaux sociaux : les interfaces peuvent masquer le bas de la vidéo.

## Slide 21 - Transcription : la version texte qui accompagne

- Correspondance : PPTX 99, `scripts/slides/46_check10_transcriptions.py`.
- Rôle : distinguer un texte autonome des sous-titres synchronisés.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : une transcription visible, complète et proche du média permet de lire, retrouver et citer le contenu.
- Scène : un podcast et une vidéo convergent vers un document texte accessible simulé par des barres gris bleuté. La communicante fil rouge recherche un passage et le cite, sans mot lisible hors liste blanche.
- Transformation : média temporel -> transcription autonome -> contenu retrouvable.
- Liste blanche du futur visuel : titre ; `Lire la transcription` ; `Paroles, sons et actions visibles` ; `Retrouver` ; `Relire` ; `Citer`.
- Ce que l’image seule doit faire comprendre : la transcription reste utilisable hors du lecteur média.
- Continuité : distingue le texte autonome puis prépare l’information visuelle portée par l’audiodescription.
- Contraintes critiques : quatre contrôles exacts ; ne pas confondre avec les sous-titres ; transcription relue.
- Alternative courte candidate : `Une transcription rend un média lisible, recherchable et citable.`

### Transcription exacte

### Transcription : la version texte qui accompagne

*3. points de contrôle rapides | 10. Transcriptions audio et vidéo*

La transcription est au podcast ce que le script est au film : la version lisible, indexable, citable.

#### Ce qu'il faut vérifier :

- Toute vidéo / audio propose un lien visible « Lire la transcription »
- La transcription est complète : paroles + informations sonores essentielles
- Elle est sur la même page ou à un clic, pas cachée à deux étages de menu
- Pour une vidéo : la transcription descriptive inclut aussi l’action visible

#### Bonus souvent oublié

- La transcription rend le contenu plus facile à retrouver, relire et citer
- Elle sert aussi aux personnes qui ne peuvent pas lancer la vidéo ou l’audio

### Discours oral exact

Différence avec les sous-titres : sous-titres = synchronisés avec la vidéo, transcription = texte autonome lisible hors vidéo. Les deux coexistent pour une vidéo de référence. Piège : publier une transcription brute générée automatiquement sans relecture.

## Slide 22 - Audiodescription : la voix qui montre

- Correspondance : PPTX 100, `scripts/slides/47_check11_audiodescription.py`.
- Rôle : rendre perceptible l’information uniquement visuelle d’une vidéo.
- Famille de mise en page : processus horizontal.
- Idée principale : une voix off décrit les images clés dans les silences sans couvrir les dialogues.
- Scène : une séquence vidéo alterne dialogue, silence et action visuelle. Une piste AD s’insère seulement dans les espaces disponibles.
- Transformation : action uniquement visible -> description dans le silence -> compréhension sans l’image.
- Liste blanche du futur visuel : titre ; `AD` ; `Images clés` ; `Silences` ; `Sans couvrir les dialogues` ; `Description textuelle synchronisée`.
- Ce que l’image seule doit faire comprendre : l’audiodescription complète la bande-son quand l’image porte le sens.
- Continuité : termine les trois contrôles médias puis prépare leur synthèse.
- Contraintes critiques : ne pas couvrir les dialogues ; conserver l’exception de la vidéo entièrement commentée dans l’oral ; ne pas inventer un bouton de plateforme.
- Alternative courte candidate : `Une piste audio décrit les images clés pendant les silences.`

### Transcription exacte

### Audiodescription : la voix qui montre

*3. points de contrôle rapides | 11. Audiodescription*

L’audiodescription ajoute une voix off qui décrit les images clés pendant les silences.

#### Ce qu’il faut vérifier :

- La vidéo propose une piste audiodécrite activable (bouton AD)
- L’audiodescription décrit les éléments visuels essentiels à la compréhension
- Elle s’intercale dans les silences, sans couvrir les dialogues
- Pour une vidéo sans dialogue essentiel : une description textuelle synchronisée suffit

> Quand l’image porte l’information, elle doit aussi être disponible autrement que par la vue.
>
> Principe d’accessibilité vidéo

### Discours oral exact

Démo : montrer 30 secondes d’un film d’animation sans dialogue, puis avec audiodescription. Le contraste est saisissant. Exception pratique : si la vidéo est entièrement commentée en voix off (ex. reportage narré), l’audiodescription est souvent superflue - tout est déjà dit.

## Slide 23 - Bonus médias : toujours 2 accès

- Correspondance : PPTX 101, `scripts/slides/47a_bonus-medias-regle-or.py`.
- Rôle : synthétiser les contrôles médias sans créer un nouveau critère.
- Famille de mise en page : checklist ou processus.
- Idée principale : toute information portée par un média doit rester compréhensible par au moins deux chemins.
- Scène : la communicante fil rouge rencontre trois médias. Chaque média se divise vers deux accès représentés par des pictogrammes cohérents pour voir, lire et écouter.
- Transformation : média unique -> second accès -> information maintenue.
- Liste blanche du futur visuel : titre ; `Image` ; `Vidéo` ; `Audio` ; `Deux accès`.
- Ce que l’image seule doit faire comprendre : aucun média ne doit enfermer l’information dans un seul canal.
- Continuité : synthétise les médias puis approfondit audiodescription et transcription.
- Contraintes critiques : trois familles exactes ; ne pas présenter la synthèse comme un quatorzième contrôle ; conserver les pièges dans la transcription.
- Alternative courte candidate : `Chaque média propose au moins deux chemins pour comprendre.`

### Transcription exacte

### Bonus médias : toujours 2 accès

*3. points de contrôle rapides | Bonus médias*

Règle d'or : un média en ligne doit rester compréhensible par au moins deux chemins : voir, lire ou écouter.

#### Le réflexe

- Image, schéma ou plan -> description ou texte alternatif
- Vidéo -> sous-titres + informations visuelles essentielles
- Audio ou podcast -> transcription visible et relue

#### Les pièges à repérer

- Sous-titres lisibles : contraste fort, bandeau si besoin
- Format réseau social : sous-titres non masqués par l'interface
- PDF : texte sélectionnable, pas une image scannée

### Discours oral exact

Positionner cette slide comme une synthèse, pas comme un nouveau critère. Elle relie les contrôles déjà vus : alternatives textuelles, sous-titres, transcription et audiodescription. Question à poser au groupe : si je coupe le son, si je ne vois pas l'image, ou si le PDF est scanné, est-ce que l'information reste accessible ?

## Slide 24 - Bonus médias : Audio-description et transcription

- Correspondance : PPTX 102, `scripts/slides/47b_bonus-vsme-transcriptions.py`.
- Rôle : préciser ce que l’audiodescription ajoute et comment choisir le niveau de transcription.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : l’audiodescription complète le visuel ; la transcription adopte le niveau nécessaire à l’usage.
- Scène : deux personnages secondaires occupent deux postes de travail. À gauche, une monteuse place une voix dans les silences. À droite, une rédactrice choisit entre trois profondeurs de transcription. Une validation humaine réunit les deux.
- Transformation : média brut -> accès complémentaire adapté -> publication relue.
- Liste blanche du futur visuel : titre ; `Audio-description : ce que ça ajoute` ; `Transcription : choisir le niveau` ; `Semi-intégrale` ; `Intégrale éditée` ; `Verbatim` ; `Relecture humaine`.
- Ce que l’image seule doit faire comprendre : les deux traitements répondent à des besoins différents et exigent une validation humaine.
- Continuité : clôt les médias puis ouvre les formulaires.
- Contraintes critiques : orthographe exacte `Audio-description` selon la source ; trois niveaux exacts ; IA seulement comme brouillon ; six libellés courts autorisés par exception, regroupés en deux colonnes et un callout.
- Alternative courte candidate : `Audio-description et trois niveaux de transcription complètent les médias.`

### Transcription exacte

### Bonus médias : Audio-description et transcription

*3. points de contrôle rapides | Bonus médias*

Image et son : proposer un autre accès à toute information utile.

#### Audio-description : ce que ça ajoute

- Décors, lieux et changements de scène utiles
- Actions, gestes et expressions qui ne s’entendent pas
- Textes et informations importantes affichés à l’écran
- Une voix placée dans les silences, sans couvrir les dialogues

#### Transcription : choisir le niveau

- Semi-intégrale : résumé détaillé + citations
- Intégrale éditée : texte complet, corrigé et lisible
- Verbatim : mot à mot, hésitations et sons inclus

IA utile pour brouillonner. Publication seulement après relecture humaine.

### Discours oral exact

L’audio-description rend accessibles les informations visuelles essentielles : lieux, actions, gestes, expressions et textes affichés. Elle s’insère dans les silences sans couvrir les dialogues ni les sons utiles. Pour la transcription, faire choisir le niveau adapté à l’usage : semi-intégrale pour restituer l’essentiel, intégrale éditée pour une lecture complète et fluide, verbatim lorsqu’une restitution mot à mot est nécessaire. Un outil d’IA peut produire un premier jet, mais la publication exige une relecture humaine.

## Slide 25 - Étiquettes : chaque champ a un nom - ÉTALON

- Correspondance : PPTX 103, `scripts/slides/48_check12_etiquettes-principe.py`.
- Rôle : poser le principe des étiquettes de formulaire.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : un champ sans étiquette ne permet pas de savoir quelle information fournir.
- Scène : une rangée de boîtes aux lettres sans nom devient un formulaire dont chaque champ possède une étiquette visible et cliquable. Le clic déplace le focus dans le champ.
- Transformation : champ anonyme -> étiquette associée -> saisie orientée.
- Liste blanche du futur visuel : titre ; `Étiquette visible` ; `Reste affichée` ; `Cliquer place le focus` ; `Nom + type de champ`.
- Ce que l’image seule doit faire comprendre : l’étiquette nomme le champ pour la vue, le clic et la restitution vocale.
- Continuité : pose le principe puis montre pourquoi le placeholder ne suffit pas.
- Contraintes critiques : quatre vérifications exactes ; association visible et fonctionnelle ; ne pas réduire la règle à une proximité graphique.
- Alternative courte candidate : `Chaque champ reçoit une étiquette visible et associée.`

### Transcription exacte

### Étiquettes : chaque champ a un nom

*3. points de contrôle rapides | 12. Étiquettes de formulaire*

Sans étiquette, un champ est comme une boîte aux lettres sans nom - on ne sait pas ce qu’on glisse dedans.

#### Ce qu’il faut vérifier :

- Chaque champ (texte, case, menu déroulant) a une étiquette visible à côté
- L’étiquette reste affichée quand on commence à saisir - elle ne disparaît pas
- Cliquer sur l’étiquette déplace le focus dans le champ (test rapide et décisif)
- Le lecteur d’écran annonce l’étiquette ET le type de champ

### Discours oral exact

Analogie : une rue d’immeubles où les boîtes aux lettres n’ont aucun nom - impossible de distribuer. Test décisif : cliquer sur le TEXTE de l’étiquette. Si le curseur saute dans le champ, c’est bien balisé. Sinon, l’association est cassée - même si visuellement ça semble OK.

## Slide 26 - Placeholder ≠ étiquette

- Correspondance : PPTX 104, `scripts/slides/49_check12_etiquettes-placeholder.py`.
- Rôle : rendre visible le piège du texte indicatif qui disparaît.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : un placeholder peut donner un exemple, mais il ne remplace jamais une étiquette persistante.
- Scène : dans un premier champ, le mot indicatif disparaît dès une saisie simulée par une barre gris bleuté et la communicante hésite. Dans le second, l’étiquette reste au-dessus et le placeholder donne seulement le format.
- Transformation : indication éphémère -> perte de contexte -> étiquette persistante.
- Liste blanche du futur visuel : titre ; `Disparaît à la saisie` ; `Contraste faible` ; `Exemple, pas nom` ; `Étiquette visible` ; `JJ/MM/AAAA`.
- Ce que l’image seule doit faire comprendre : l’exemple de format peut disparaître, le nom du champ doit rester.
- Continuité : corrige le champ isolé puis prépare les groupes de champs.
- Contraintes critiques : conserver le signe `≠` ; ne pas suggérer d’interdire tout placeholder ; étiquette toujours visible.
- Alternative courte candidate : `L’étiquette reste visible quand le placeholder disparaît.`

### Transcription exacte

### Placeholder ≠ étiquette

*3. points de contrôle rapides | 12. Étiquettes de formulaire*

#### Pourquoi le placeholder ne remplace pas l’étiquette :

- Il disparaît dès qu’on commence à saisir - on oublie ce qu’on remplit
- Son contraste est souvent trop faible pour passer le check 4
- Il peut être annoncé comme exemple, pas comme nom fiable du champ
- Il devient difficile d’y revenir dès que la saisie commence

#### Pattern recommandé

- Étiquette visible au-dessus du champ (ou à gauche)
- Placeholder optionnel, pour donner un exemple de format : « JJ/MM/AAAA »
- Ne pas mettre l’information essentielle uniquement dans le placeholder

### Discours oral exact

Démo : formulaire courant (type CAF, impots.gouv) avec labels floating - zoomer à 200 % et montrer que l’étiquette disparaît derrière le texte saisi. Règle pragmatique : si on doit choisir entre joli et utilisable, on choisit utilisable. Les labels au-dessus du champ sont plus hauts mais clairs pour tous.

## Slide 27 - Groupes de champs : l’étiquette commune

- Correspondance : PPTX 105, `scripts/slides/50_check12_etiquettes-groupes.py`.
- Rôle : expliquer la question commune des radios et cases à cocher.
- Famille de mise en page : comparaison ou transformation.
- Idée principale : des choix liés doivent rester rattachés à la question à laquelle ils répondent.
- Scène : trois boutons radio isolés perdent leur question. Un cadre `fieldset` et une légende `Civilité` réunissent ensuite la famille.
- Transformation : choix orphelins -> groupe nommé -> question comprise.
- Liste blanche du futur visuel : titre ; `Civilité` ; `M` ; `Mme` ; `autre` ; `Question claire`.
- Ce que l’image seule doit faire comprendre : l’étiquette commune donne du sens à chaque option.
- Continuité : complète les étiquettes puis prépare l’obligation et les erreurs.
- Contraintes critiques : conserver les deux restitutions vocales ; ne pas présenter la bordure visuelle comme preuve suffisante ; question commune requise.
- Alternative courte candidate : `Une légende commune relie les boutons radio à leur question.`

### Transcription exacte

### Groupes de champs : l’étiquette commune

*3. points de contrôle rapides | 12. Étiquettes de formulaire*

#### Quand regrouper :

- Plusieurs boutons radio qui répondent à la même question (« Civilité : M / Mme / autre »)
- Plusieurs cases à cocher qui partagent un thème (« Jours travaillés »)
- Adresse découpée en plusieurs champs (n°, rue, code postal, ville)

| Cas | Code vérifié | Verdict lecteur d’écran |
| --- | --- | --- |
| 3 radios « Civilité » sans regroupement | Chaque radio a son label seul | « M, bouton radio » - question perdue |
| 3 radios dans un `<fieldset>` avec `<legend>` | `<fieldset><legend>Civilité</legend>… <input type="radio">…` | « Civilité, M, bouton radio » - question claire |

### Discours oral exact

Analogie : sans `<fieldset>`/`<legend>`, les radios sont comme des enfants sans nom de famille - on les entend, on ne sait pas à quelle question ils répondent. Côté visuel : le fieldset se traduit souvent par une bordure ou un titre de section - le design peut l’habiller, il ne doit pas le supprimer.

## Slide 28 - Champs obligatoires : prévenir puis guider

- Correspondance : PPTX 106, `scripts/slides/51_check13_champs-obligatoires.py`.
- Rôle : séparer le contrôle avant envoi du guidage après erreur.
- Famille de mise en page : processus horizontal.
- Idée principale : l’obligation doit être comprise avant la soumission et l’erreur doit ensuite conduire vers la correction.
- Scène : un formulaire suit deux temps. Avant envoi, les champs obligatoires sont annoncés. Après un envoi vide, un message précis mène le focus au champ concerné.
- Transformation : obligation annoncée -> soumission -> erreur précise et focus guidé.
- Liste blanche du futur visuel : titre ; `Avant soumission` ; `Après soumission` ; `obligatoire` ; `Focus guidé`.
- Ce que l’image seule doit faire comprendre : prévenir et corriger sont deux contrôles complémentaires.
- Continuité : termine les contrôles de formulaire puis prépare la remontée dans la grille.
- Contraintes critiques : aucune erreur visible avant interaction ; deux temps distincts ; conserver l’exemple précis dans l’oral.
- Alternative courte candidate : `Le formulaire annonce l’obligation puis guide vers chaque erreur.`

### Transcription exacte

### Champs obligatoires : prévenir puis guider

*3. points de contrôle rapides | 13. Champs obligatoires et erreurs*

Test #13 = avant envoi + après soumission vide : l'obligation prévient, l'erreur guide.

#### Avant soumission

- Obligation écrite : « obligatoire » ou règle « tous sauf téléphone »
- Astérisque expliqué s'il est utilisé
- Attribut `required` ou `aria-required="true"` présent

#### Après soumission

- Aucune erreur ne doit apparaître avant l'envoi
- Message précis relié au champ, avec `aria-invalid` si erreur
- Focus vers le récapitulatif ou le premier champ en erreur

### Discours oral exact

Règle d'or : le contrôle 13 ne commence pas par les erreurs. D'abord, vérifier que l'obligation est comprise avant l'envoi. Ensuite, soumettre volontairement un formulaire vide : le message doit nommer le champ, être relié au champ et guider le focus. Message à éviter : « Erreur champ 3 ». Préférer : « L'adresse électronique doit respecter le format nom@domaine.fr ».

## Slide 29 - Ce qu’on remonte dans la grille

- Correspondance : PPTX 107, `scripts/slides/51a_grille-remontee.py`.
- Rôle : transformer une observation en remontée exploitable.
- Famille de mise en page : tableau pédagogique.
- Idée principale : une équipe peut agir lorsque le constat associe verdict, sévérité, correction et preuve.
- Scène : une anomalie clavier entre dans une fiche de suivi. Cinq champs se remplissent puis la fiche est remise à l’équipe web.
- Transformation : défaut observé -> cinq informations -> correction possible.
- Liste blanche du futur visuel : titre ; `Verdict` ; `Sévérité` ; `Constat` ; `Correctif` ; `Preuve` ; `C / NC / NA` ; `Bloquant / gênant / mineur / info`.
- Ce que l’image seule doit faire comprendre : une remontée complète permet de comprendre, retrouver et prioriser le défaut.
- Continuité : concrétise l’audit rapide puis prépare les signaux bonus.
- Contraintes critiques : cinq champs exacts ; ne pas ajouter de statut ; conserver les quatre niveaux de sévérité ; densité autorisée par exception dans un tableau pédagogique aéré à deux niveaux de lecture.
- Alternative courte candidate : `Cinq champs transforment un défaut en remontée exploitable.`

### Transcription exacte

### Ce qu’on remonte dans la grille

*3. points de contrôle rapides | Grille d’audit*

| Champ | Ce qu’il faut écrire | Exemple court |
| --- | --- | --- |
| Verdict | C, NC ou NA | NC |
| Sévérité | Bloquant, gênant, mineur ou info | Gênant |
| Constat | Ce que vous observez concrètement | Le lien d’évitement n’apparaît pas au focus. |
| Correctif | Ce que l’équipe doit corriger | Rendre le lien visible et cibler #contenu. |
| Preuve | URL, capture, sélecteur ou extrait | /actualites - premier appui sur Tab |

#### Règle de travail

- Un défaut sans preuve est difficile à traiter.
- Une preuve sans sévérité est difficile à prioriser.

### Discours oral exact

Faire ouvrir 03-easy-checks/grille-audit-easy-checks.xlsx. Expliquer que l’objectif n’est pas seulement de dire « ça passe » ou « ça échoue ». Une remontée utile doit permettre à l’équipe web de comprendre le problème, mesurer l’impact, retrouver l’endroit exact et corriger sans refaire toute l’enquête. Insister sur les quatre niveaux de sévérité : bloquant, gênant, mineur, info.

## Slide 30 - Bonus site web : liens et PDF à repérer

- Correspondance : PPTX 108, `scripts/slides/51b_bonus-liens-pdf.py`.
- Rôle : ouvrir deux familles de signaux utiles sans les transformer en nouveaux contrôles obligatoires.
- Famille de mise en page : synthèse et passage à l’action.
- Idée principale : les libellés de liens et la structure des PDF améliorent l’expérience et méritent une remontée quand un défaut apparaît.
- Scène : la communicante fil rouge inspecte une page qui contient un lien de téléchargement et un document PDF. Deux chemins de vigilance restent reliés à la grille comme signaux bonus.
- Transformation : signaux repérés -> note dans la grille -> renvoi vers un audit adapté.
- Liste blanche du futur visuel : titre ; `Liens` ; `Libellé explicite` ; `Type + poids` ; `Documents PDF` ; `Texte sélectionnable` ; `Structure` ; `Texte alternatif` ; `Signal bonus`.
- Ce que l’image seule doit faire comprendre : liens et PDF se signalent sans élargir artificiellement les 13 contrôles.
- Continuité : clôt la série sur une vigilance transférable.
- Contraintes critiques : ne pas annoncer un quatorzième ou quinzième contrôle ; ne pas déclarer un PDF conforme sur la seule sélection du texte ; ne pas inventer de poids de fichier ; densité autorisée par exception dans deux colonnes courtes clairement titrées.
- Alternative courte candidate : `Deux signaux bonus portent sur les liens et les documents PDF.`

### Transcription exacte

### Bonus site web : liens et PDF à repérer

*3. points de contrôle rapides | Bonus*

Pendant l'audit, ces points ne remplacent pas les 13 checks. Mais si vous les voyez, notez-les : ils améliorent vraiment l'expérience utilisateur.

#### Liens

- Éviter les pages saturées de liens sans hiérarchie
- Libellé explicite : « programme de l'exposition photo »
- Éviter « cliquez ici », « en savoir plus », « programme » seul
- Téléchargement : indiquer type et poids du fichier

#### Documents PDF

- Texte sélectionnable : pas de PDF image ou scanné non navigable
- Structure : titres, sommaire et liens internes si le document est long
- Images avec texte alternatif
- Si possible : proposer aussi un format éditable ou OpenDocument

### Discours oral exact

Positionner cette slide comme un bonus volontaire, pas comme un 14e et 15e point de contrôle. Pour les liens, rappeler le principe RGAA : un lien doit être compréhensible seul ou avec son contexte immédiat. La meilleure pratique reste un libellé directement explicite, surtout pour les personnes qui listent les liens avec un lecteur d'écran. Pour les fichiers en téléchargement, citer la logique Opquast : indiquer le format et la taille aide l'utilisateur à décider avant de télécharger. Nuance importante : ne pas transformer l'exercice en audit documentaire complet. Si un PDF pose problème, le noter comme signal bonus dans la grille, puis renvoyer vers les méthodes d'audit PDF ou vers le module Word/PDF.

## Validation interne du storyboard

- Couverture : les 30 slides web correspondent aux PPTX 79 à 108 sans ajout ni suppression.
- Titres : les 30 titres sont ceux des modules Python sources.
- Visuels : chaque slide possède une scène concrète, une transformation et une liste blanche de texte.
- Accessibilité : chaque slide possède une alternative courte candidate, une transcription et un discours oral distincts.
- Exercices : les slides 15 et 16 conservent l’URL visible ; les QR codes futurs seront générés de manière déterministe.
- Données : les chiffres WebAIM, les rapports de contraste, les durées et les exemples restent inchangés.
- Limite : les points de contrôle rapides sont présentés comme un pré-diagnostic, jamais comme un audit RGAA complet.
- Jalon suivant : produire uniquement les quatre étalons 01, 02, 16 et 25 après autorisation explicite, puis les faire valider avant la génération des 26 autres images.

## Auto-évaluation pédagogique

| Dimension | Score | Preuve dans le storyboard |
| --- | ---: | --- |
| Couverture | 10/10 | Correspondance stricte des 30 slides et reprise exacte des contenus. |
| Clarté | 9/10 | Cinq étapes, une idée centrale et une transformation par slide. |
| Conviction | 9/10 | Données WebAIM, seuils de contraste, exemples et tests concrets. |
| Engagement | 9/10 | Prédictions, votes, démonstrations, test clavier et mission sur site. |
| Actionnabilité | 10/10 | Outils, gestes de test, exercice et grille de remontée. |

- Phrase-clé à retenir à six mois : `Un contrôle rapide ne remplace pas l’audit, mais il révèle des barrières et permet de les remonter avec une preuve.`
- Verdict pédagogique : `[★] transformatif`.

### Règles neuropédagogiques appliquées

- Engagement immédiat : les données WebAIM installent le besoin dès les slides 02 et 03.
- Primauté et récence : la limite du pré-diagnostic apparaît dès le cadrage et reste explicitement rappelée dans les notes de conclusion bonus.
- Utilité concrète : chaque contrôle répond à « que regarder et comment le tester ? ».
- Charge cognitive réduite : une scène et une transformation par visuel, avec le détail déplacé dans l’accordéon.
- Chunking : trois à cinq repères dominants par image, sauf données indispensables.
- Double codage : l’image montre l’action, la transcription documente, le discours oral explique.
- Analogies concrètes : étiquette d’onglet, table des matières, ascenseur, lunettes, boîte aux lettres.
- Prédiction : votes, questions et essais précèdent plusieurs révélations.
- Récupération active : passe ou échoue, navigation clavier et mission sur le site d’entraînement.
- Variation des stimuli : chiffres, comparaisons, parcours, vidéo, formulaires et exercice.
- Sécurité psychologique : les signaux servent à améliorer une routine, pas à désigner un coupable.
- Feedback immédiat : verdicts OK ou KO, mesures de contraste et réponse du site d’entraînement.
- Apprentissage social : échanges, votes et audit groupé prévus dans les notes.
- Échafaudage : principe, méthode, exercice, puis grille de remontée.
- Plan d’action : les stagiaires choisissent un outil et annoncent un test à réaliser.
- Métacognition : la mission demande ce qui aurait aidé à repérer le défaut plus vite.
- Transformation : le public passe de l’observation d’une page à une remontée exploitable.

Score neuropédagogique : **17/26** règles présentes ou directement mobilisées dans la séquence.

### Avant / après représentatif

- Avant : un tableau complet de cinq touches, de leurs fonctions et des résultats attendus est projeté en petit.
- Après : le visuel montre un clavier et trois intentions immédiatement reconnaissables ; le tableau exact reste disponible dans la transcription sémantique.
