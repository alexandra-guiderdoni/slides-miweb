# Édition du support « Nouveautés d’Opquast V5 »

Titre public : Nouveautés d’Opquast V5

Slug de publication : `nouveautes-opquast-v5`

Base éditoriale : storyboard v003, conservé dans `source/storyboard.md`, statut
`VALIDE_POUR_GENERATION` du 17 septembre 2026. Ce storyboard ne couvre que les slides 1 à
10 ; le lot suivant a été livré sans document de conception.

Le texte de `source/transcription-et-discours-oral.md` fournit le contenu des deux
accordéons de chaque slide. Il distingue explicitement deux lots, d’origines différentes.

## Périmètre et numérotation

Le support publie la série complète : 17 visuels, numérotés de 1 à 17 sur le web comme
sur la pagination imprimée des images. Les deux numérotations coïncident.

La publication s’est faite en deux temps, dans ce même dossier :

- le 17 septembre 2026, les slides 1 à 10, alors que les sept suivantes n’étaient pas
  produites ; les visuels portaient déjà la pagination de la série complète, de `1 / 17`
  à `10 / 17`, et cet écart assumé était documenté ici ;
- le même jour, les slides 11 à 17, qui ferment la série sans qu’aucune image des dix
  premières n’ait été retouchée.

## Origine des textes, deux lots distincts

Les slides 1 à 10 reprennent sans réécriture les accordéons rédigés avec les visuels ;
seules les balises HTML d’accordéon et les niveaux de titre ont été transformés pour
entrer dans le format des séries Opquast V5 déjà publiées.

Les slides 11 à 17 ont été livrées sous la forme de sept images seules, sans storyboard
ni accordéons. Leurs titres, alternatives, textes visibles, messages, transcriptions et
discours oraux ont été rédigés à partir des visuels, dans le format et la logique du
premier lot. Ces textes appellent une relecture métier au même titre que tout texte
rédigé en propre : ils ne sont pas la transcription d’un contenu validé en amont.

## Règles couvertes

Huit nouvelles règles de la version 5 du référentiel, chacune traitée sur une slide du
deck après deux slides de cadrage :

- règle 14, détournement de caractères, thématique Contenus ;
- règle 26, existence d’un compte utilisateur, thématique Données personnelles ;
- règle 68, provenance des produits, thématique E-Commerce ;
- règle 96, relance de la double authentification, thématique Formulaires ;
- règle 97, autocomplétion signalée dans le code source, thématique Formulaires ;
- règle 98, boutons désactivés et lecteurs d’écran, thématique Formulaires ;
- règle 216, affichage de la barre d’adresse, thématique Sécurité ;
- règle 217, authentification du domaine de messagerie, thématique Sécurité.

Les slides 11 à 17 citent cinq autres règles de la version 5, à titre d’illustration des
mouvements du référentiel :

- règle 245, tableaux de données non simulés, issue de la fusion présentée slide 12 ;
- règle 112, moyen de contacter le service après-vente ou le support, exemple de
  reformulation slide 13 ;
- règle 235, balisage des listes dans le code source, exemple de numéro réaffecté
  slide 14 ;
- règle 1, possibilité de connaître les nouveaux contenus ou services, citée slide 11
  comme exigence qui continue de couvrir le besoin d’information après le retrait de la
  règle sur les fils de syndication ;
- règle 25, politique de communication des referrers, citée slide 11 comme exemple de
  numéro réaffecté après le retrait de l’ancienne règle 25.

Les libellés et les thématiques de ces treize règles ont été contrôlés le 17 septembre 2026
contre l’API Opquast, version `qualite-numerique`. Les citations portées par les visuels
correspondent aux libellés officiels, aux variantes typographiques près décrites plus bas.

### Règles de la version 4 citées par comparaison

Les slides 11 à 14 citent six règles de la version 4 du référentiel, pour illustrer les
retraits, la fusion et les reformulations. Elles ont été contrôlées le 17 septembre 2026
contre l’API Opquast, version `assurance-qualite-web`, qui sert les 240 règles de cette
version :

- règle 24, politique de communication des referrers, devenue la règle 25 en version 5 ;
- règle 25, liens externes ouvrant une nouvelle fenêtre et information de contexte ;
- règle 107, moyen de contacter le responsable des réclamations ;
- règle 235, détectabilité des fils de syndication ;
- règle 239, tableaux de données non remplacés par des images ;
- règle 240, tableaux de données non simulés à l’aide de texte mis en forme.

Les libellés des règles 25, 107, 235, 239 et 240 correspondent à ce qu’affichent les
visuels ; la règle 24 n’est citée que par le discours oral de la slide 11.

La solution officielle de l’ancienne règle 25 demandait `rel="noreferrer noopener"` sur
tout lien portant `target="_blank"`, et sa fiche notait déjà que `target="_blank"` revient
à donner `rel="noopener"`. Le discours oral s’appuie sur ce constat pour expliquer qu’une
exigence appliquée d’office par les navigateurs perd sa valeur ajoutée dans le socle. Le
volet referrer, lui, reste traité par la règle 25 de la version 5, au niveau du serveur.

Le total de 240 règles annoncé par la slide 1 est confirmé par le décompte de cette même
version.

Deux vérifications complémentaires confirment les mouvements présentés : aucune règle de
la version 5 ne reprend la détectabilité des fils de syndication ni le partage
d’information de contexte des liens externes, et les tableaux de données y sont couverts
par les seules règles 242, 243 et 245, contre quatre règles en version 4.

En version 4, le balisage des listes portait le numéro 228 ; il porte le numéro 235 en
version 5, où ce numéro désignait auparavant les fils de syndication. La mise en garde de
la slide 14 est donc exacte.

La traçabilité des règles est portée par le champ `regles_opquast` de `slides.json` et
par la présente fiche. Ce champ ne retient que les numéros de la version 5 ; les numéros
de la version 4 sont cités dans les transcriptions et dans la présente section.

Les chiffres de la slide 1, 240 règles en V4 et 245 en V5, deux suppressions, une fusion
et huit ajouts, proviennent du storyboard source. Ils décrivent l’évolution du
référentiel et ne sont pas issus d’un décompte refait pour cette publication.

## Réserves de lecture

La date du 14 avril 2026 portée par la slide 16 a été vérifiée le 17 septembre 2026 :
c’est la date de publication de l’article d’Opquast « Au programme : livre, tags et
numérique », `https://www.opquast.com/au-programme-livre-tags-et-numerique/`. Cet article
annonce bien le remplacement des tags Conception, Développement et Éditorial par
Fonctionnel, Technique et Contenus, ainsi qu’un travail d’applicabilité des règles par
type de service. Le badge « Complément · 2026 » et le contenu de la slide sont donc
fondés.

Deux nuances relevées à cette occasion, consignées dans la transcription de la slide 16.
Les catégories publiées par Opquast sont notamment les sites web et portails publics, les
intranets et extranets, les applications mobiles, les applications pour ordinateur, les
bornes interactives, la télévision connectée, les médias sociaux, le courriel et les jeux
vidéo : les mentions « Service e-commerce » et « Service métier » du visuel n’en font pas
partie et valent comme exemples d’illustration. Les quatre contextes figurés sur la
slide 15, intranet, application mobile, application pour ordinateur et télévision
connectée, correspondent en revanche à des catégories réelles.

Opquast présente ce travail d’applicabilité comme ouvert et appelle les retours : les
catégories et leurs volumes de règles peuvent évoluer.

La slide 3 illustre le détournement de caractères par un contraste typographique entre
deux panneaux qui affichent tous deux le mot « Bonus ». Le visuel n’emploie pas les
caractères Unicode détournés eux-mêmes, qui ne survivraient pas à toutes les chaînes de
production. La transcription décrit donc un exemple signalé comme tel, sans affirmer que
les deux panneaux emploient des jeux de caractères différents.

Le visuel de la slide 4 ferme la citation de la règle par un guillemet anglais, sans
guillemet ouvrant correspondant : la citation est introduite par un signe typographique
décoratif. Le visuel est conservé en l’état, décision du 17 septembre 2026. Les textes
visibles et la transcription reprennent le libellé sans ces guillemets.

Le titre imprimé de la slide 6 se termine par un point, contrairement aux autres titres
de la série. Le titre web reprend le libellé sans ce point final.

La slide 9 porte le numéro de règle dans une pastille ronde placée dans le corps de la
slide, là où les autres slides de règle utilisent un badge carré près du titre. Cette
variation de gabarit n’a pas d’incidence sur le contenu.

La slide 10 cite la règle 217 entre guillemets droits. Le libellé officiel de cette règle
ne porte pas de point final, ce que le visuel respecte.

Les exemples suivants sont fictifs et servent uniquement la démonstration : les adresses
`alice@example.com` et `bob@example.com`, le domaine `service.example`, ainsi que la
fiche « Produit exemple » à 12,90 € fabriquée au Portugal, qui porte sur le visuel la
mention « Exemple fictif ».

Les annotations « Compte existant » et « Compte inexistant » de la slide 4 sont des
repères pédagogiques ajoutés pour la démonstration. Elles ne font pas partie de
l’interface vue par la personne qui utilise le service.

Ce support n’a fait l’objet d’aucun audit RGAA dédié et ne déclare aucune conformité.

## Révision des discours oraux

Les discours oraux des 17 slides ont été révisés le 17 septembre 2026 pour suivre une
trame unique : d’abord relier la règle à son impact, en nommant le préjudice concret que
subit l’utilisateur si elle n’est pas appliquée, puis dire ce que la règle garantit, sans
lui attribuer une portée qu’elle n’a pas.

Le préjudice et la garantie sont ancrés dans les champs officiels de l’API Opquast :
objectifs, explication, vulgarisation, solution et contrôle des treize règles citées. Cette
lecture a apporté des éléments que les visuels ne portent pas, repris dans les discours :
l’effet de l’attribut `disabled` sur certains lecteurs d’écran et la recommandation
d’`aria-disabled="true"` pour la règle 98, les valeurs normalisées de l’attribut
`autocomplete` et la réserve sur les champs sensibles pour la règle 97, l’enchaînement
énumération puis force brute pour la règle 26, la conception prudente de la relance pour
la règle 96, la distinction entre lieu de fabrication, d’assemblage et d’expédition pour
la règle 68, et le fait que le contrôle de la règle 112 ne porte que sur la présence d’un
moyen de contact, pas sur sa nature.

Sept slides ne portent pas une règle : les slides 1, 2, 11, 14, 15, 16 et 17. La trame y
est transposée au mouvement du référentiel, et la section de garantie y dit explicitement
ce qui n’est pas garanti, ou qu’il s’agit d’une pratique de migration et non d’une règle.

### Sections de mise en œuvre

Les neuf slides qui portent une règle, soit les slides 3 à 10 et la slide 12, ferment leur
discours par une section « Mise en œuvre ». Son contenu est repris des champs `solution` et
`control` de la fiche officielle de la règle : formulations de messages neutres pour la
règle 26, valeurs normalisées de l’attribut `autocomplete` pour la règle 97, usage
d’`aria-disabled` plutôt que de `disabled` pour la règle 98, options de `window.open()` à
proscrire pour la règle 216, enregistrements SPF, DKIM et DMARC pour la règle 217, balises
de tableau pour la règle 245.

La slide 3 porte en outre une section « Pour aller plus loin » sur le détournement de
caractères Unicode dans les noms de domaine à des fins d’hameçonnage. Ce point vient de la
vulgarisation de la règle 14, qui le présente comme un autre usage du même procédé ; le
texte précise que la règle ne traite pas ce cas.

La slide 6 cite la recommandation de proposer au moins deux moyens d’authentification, que
la fiche de la règle 96 présente explicitement comme allant au-delà de la règle.

### Sources du discours de la slide 15

Le discours de la slide 15 ne porte pas sur une règle mais sur le mouvement du référentiel.
Ses affirmations ont été vérifiées le 17 septembre 2026 contre les sources suivantes :

- la citation « nous évoluons de la notion de web vers la notion de numérique au sens
  applicatif du terme » vient de l’article d’Opquast « Certification Opquast : nouvelle
  version », publié le 7 octobre 2025, qui annonce aussi le nom du parcours certifiant et
  le passage d’une checklist de règles à un référentiel complet ;
- le cadre réglementaire cité, European Accessibility Act, RGAA, RGPD, puis IA Act et
  RGESN à anticiper, vient de la page « Entreprises et grands comptes » du site d’Opquast ;
- le modèle VPTCS et son attribution à Elie Sloïm et Eric Gateau en 2001 viennent du guide
  Opquast, chapitre 1.4, édition de septembre 2025.

Le chiffre de 40 libellés mentionnant « le site » en version 4 contre 6 en version 5 est
une mesure faite sur les deux checklists complètes servies par l’API, et non une donnée
publiée par Opquast. En revanche, le nombre de libellés mentionnant une « page » ne varie
pas entre les deux versions, 42 dans chacune : le discours ne prétend donc pas que les
références aux pages auraient été gommées.

### Sources du discours de la slide 16

Le discours de la slide 16 s’appuie sur l’article « Au programme : livre, tags et
numérique », d’Élie Sloïm, publié le 14 avril 2026, lu dans le corpus documentaire du
serveur MCP Opquast, édition du 8 septembre 2026.

Les deux citations sont reprises mot pour mot de cet article : « l’utilisation de l’IA est
en train de mettre un désordre gigantesque dans les phases projets » et « ces définitions
sont imparfaites ». Les définitions des trois nouveaux tags reprennent la première phrase
de chacune des définitions publiées.

Trois points ont été corrigés après relecture du texte source :

- l’article ne publie aucune correspondance terme à terme entre anciens et nouveaux tags ;
  le discours ne présente donc pas le changement comme un renommage ;
- la phrase « les futures modifications ne sont pas encore en ligne » porte, dans
  l’article, sur les fiches accompagnant le livre, et non sur les tags. Le caractère non
  appliqué du changement de tags est établi autrement : l’article le présente comme une
  proposition soumise aux retours, et la checklist servie par l’API porte encore, au
  17 septembre 2026, les étiquettes conception, développement et éditorial ;
- l’article précise que les 14 rubriques et les tags thématiques ne changent pas, point
  que le discours reprend parce qu’il borne le chantier.

Deux chiffres de l’article ont été recoupés avec l’API et concordent : le référentiel
compte bien 14 rubriques dans les deux versions, et le tag Basics rassemble 65 règles en
version 5, contre 60 en version 4.

Dans l’API, ces étiquettes de phases sont exposées sous le nom « Phases projet », tandis
que le champ « Tags » désigne les tags thématiques. L’article, lui, parle de trois familles
de tags. Le discours suit la terminologie de l’article, celle que porte le visuel.

## Typographie

Les tirets quadratins ont été remplacés par des traits d’union dans l’ensemble des textes
du jeu : `slides.json`, la présente fiche, la source des transcriptions et le storyboard
conservé dans `source/`. Le storyboard d’origine, non normalisé, reste disponible dans le
projet source qui a produit les visuels.

Les visuels ne sont pas retouchés : ils conservent leur typographie d’origine, quadratins
compris. Les champs `textes_visibles` reprennent donc le texte des images avec des traits
d’union là où le visuel affiche un quadratin.

## Choix d’édition

Les champs `textes_visibles` reprennent le pied de page et la pagination de chaque
visuel, parce que cette information varie d’une slide à l’autre et documente le périmètre
partiel de la série. L’en-tête de marque, identique sur les dix visuels, n’y est pas
repris ; il figure dans les descriptions longues.

Pour les slides 1 à 10, les transcriptions de `slides.json` ajoutent, par rapport aux
accordéons source, une section « Message à retenir » sur chaque slide et une section
« Point de vigilance » sur les slides 4, 5, 9 et 10. Ces ajouts signalent les exemples
fictifs et les repères pédagogiques ; ils n’altèrent pas le texte repris de la source.

Pour les slides 11 à 17, la même structure a été appliquée d’emblée, les textes étant
rédigés et non repris. Les slides 11 à 14 portent en outre une section qui donne les
libellés officiels complets des règles comparées, les visuels n’en affichant parfois
qu’un résumé ; les slides 15 et 16 portent une réserve sur le caractère non officiel des
listes d’exemples et de la date annoncée.

## Traçabilité des images

Les dix premiers visuels ont été repris le 17 septembre 2026 entre 10h33 et 10h36, après
l’enregistrement du journal de production `run.json` de 06h12. Les empreintes SHA-256 de
ce journal ne décrivent donc plus les fichiers publiés.

Les sept visuels du second lot ont été livrés le 17 septembre 2026 entre 11h10 et 11h13,
sans journal de production.

Les empreintes des images effectivement publiées sont consignées dans
`source/transcription-et-discours-oral.md`, slide par slide, et ont été vérifiées
identiques entre le dossier source et `assets/slides/` au moment de la copie, pour les
deux lots.
