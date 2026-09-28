# Édition du support « Navigation selon Opquast V5 »

Titre public : Navigation selon Opquast V5

Slug de publication : `navigation-opquast-v5`

Base éditoriale : storyboard `v001`, conservé dans `source/storyboard.md`, statut
`VALIDE_POUR_GENERATION` du 27 septembre 2026. Il couvre les quarante slides, réparties en
quatre lots de dix, et porte pour chacune une « Idée principale » et un bloc « Textes
visibles exacts ».

Le fichier `source/transcription-et-discours-oral.md` fournit le contenu des deux
accordéons de chaque slide. Le fichier `source/brief.md` conserve la commande initiale et
ses trois extensions de lot.

Projet d'origine des livrables :
`projets-actifs/opquast/Formations-MIWEB/navigation/opquast-navigation/`.

## Périmètre et numérotation

Le support publie la série complète : quarante visuels, numérotés de 1 à 40 sur le web
comme sur la pagination imprimée des images, de `01 / 40` à `40 / 40`. Les deux
numérotations coïncident.

Les titres des quarante slides ont été comparés entre le storyboard, les accordéons, les
descriptions textuelles et le discours oral : les quatre fichiers concordent exactement,
sans un seul écart.

## Origine des textes

Les titres, les textes visibles et les messages viennent du storyboard.

Les deux accordéons de chaque slide, transcription et discours oral, ont en revanche été
**entièrement réécrits** le 28 septembre 2026, sur décision d'Alex, les textes de la source
ayant été jugés non pertinents. Les textes d'origine restent consultables dans
`source/transcription-et-discours-oral.md`.

Le fichier `descriptions-textuelles-opquast-navigation.md` du projet source n'a pas été
repris : il duplique au caractère près, sur les quarante slides, les sections de
transcription déjà portées par les accordéons.

Les alternatives textuelles courtes n'existaient dans aucune source. Elles ont été
rédigées à partir de l'inspection de chacun des quarante visuels.

Alternatives, transcriptions et discours sont donc des textes rédigés en propre. Ils
appellent une relecture métier à ce titre.

## Ancrage des textes réécrits

La trame du discours oral est conservée : une accroche, puis « Relier chaque règle à son
impact », puis « Ce que garantit la règle », puis « Mémo oral ».

La section de garantie ne paraphrase plus le titre de la slide : elle reprend les
**objectifs officiels** de la règle, servis par le serveur MCP Opquast, instantané local
du 3 septembre 2026, version `qualite-numerique`, 245 règles. Les vingt libellés officiels
des règles 153 à 172 sont cités au mot près, contrôle automatisé passé le 28 septembre 2026.

Les étiquettes réelles sont nommées quand elles éclairent la portée d'une règle : `Basics`
pour les règles 156, 159, 165, 166, 168 et 171, `SEO` pour les règles 153 et 171,
`Écoconception` pour les règles 154, 168, 169 et 170.

Les renvois au RGAA 4.1.2 nomment le critère et ne sont jamais présentés comme du Opquast :
critères 3.1, 12.1, 12.6, 12.8, 12.9, 12.10 et 12.11. Source : `notebook-navigation.md` du
projet source.

Les distinctions de vocabulaire viennent du glossaire Opquast, édition du 17 juin 2026,
consulté par le serveur MCP : popup comme fenêtre à part entière du navigateur, fenêtre
modale comme fenêtre simulée en surimpression générée par CSS et JavaScript.

Le cadrage pédagogique et le fil rouge, « Je sais où je suis. Je sais où aller. Je peux y
aller. Et je garde la main. », viennent de `opquast_navigation.md`.

### Ce qui n'a pas pu être ancré

L'API privée Opquast a répondu 403 pendant toute la production, faute de variable
`OPQUAST_API_KEY`. Les champs *explication*, *solution* et *contrôle* des fiches
officielles n'ont donc pas été accessibles. Aucun texte de ce jeu n'énonce de procédure de
mise en œuvre ni de méthode de contrôle comme étant officielle. Une reprise avec une clé
API permettrait d'ajouter une section de mise en œuvre sourcée, comme le fait le jeu
`nouveautes-opquast-v5`.

Le notebook attribue à « la règle Opquast 82 » la reprise de navigation après un
formulaire. Dans l'édition `qualite-numerique`, ce libellé porte le numéro **84**. Ce
numéro n'est cité nulle part dans le jeu.

## Trous de la série, couverts à l'oral

La série annonce vingt règles en ouverture et en traite dix-neuf. La règle 172, « Les
limites de temps imposées à une action ou un accès sont indiquées », n'a aucune slide,
alors que la slide 2 pose la sixième question utilisateur, « Ai-je le temps d'agir ? ».

Le deck ne comporte pas de Synthèse C : il passe de la Synthèse B, slide 21, à la
Synthèse D, slide 33. La séquence des liens d'accès rapide, slides 22 à 25, n'a donc pas
de slide de synthèse.

Conformément à l'arbitrage d'Alex du 28 septembre 2026, ces deux manques sont signalés
dans les discours oraux plutôt que comblés par des slides sans visuel : la règle 172 et son
libellé officiel dans les discours des slides 2, 33 et 40, l'absence de Synthèse C dans le
discours de la slide 25.

## Restructuration des descriptions

Les descriptions de la source enchaînent trois choses dans un même bloc de prose : la
structure de la slide, la reprise des textes visibles, puis une phrase sur l'illustration.

Les deux premières sont conservées telles quelles. Une première version de ce jeu avait
sorti les textes visibles de la prose pour les présenter en liste dans une section
« Textes visibles ». Cette mise en forme a été écartée le 28 septembre 2026 sur décision
d'Alex : l'accordéon de transcription doit garder la forme de la source, une lecture du
visuel en prose continue.

La troisième, en revanche, était fautive sur vingt et une des quarante descriptions : le
nom commun manquait, ce qui donnait « le visuel principal illustre une d'ouverture »,
« illustre une d'éclairage », « illustre une de » ou « illustre une comparant ». Ce défaut
de génération partait sans cela dans `alternatives.html` et `alternatives.md`, les
livrables lus par les utilisateurs de lecteurs d'écran. Ces phrases sont remplacées par une
description de l'illustration vérifiée sur le visuel correspondant.

Les textes imprimés dans les illustrations sont énoncés à la suite, sous la forme
« Textes lisibles dans l'illustration : ... ». Cette reprise est nécessaire : `build.py`
valide le champ `textes_visibles` mais ne le rend sur aucune page, si bien que ces textes
n'atteindraient aucun lecteur sans elle.

La section « Message à retenir » est conservée parce que le test de contrat
`test_variant_pages_expose_transcriptions` l'exige dans `index.html` et dans
`alternatives.html`.

## Textes visibles

Le storyboard préfixe chaque ligne de textes visibles par une étiquette. Certaines sont
réellement composées sur la slide, d'autres ne servent qu'à structurer le document. Chaque
étiquette a été tranchée sur le visuel, et non par convention :

- affichées, donc conservées devant leur valeur : « Préjudice », « Garantie »,
  « Vocabulaire », « Règles », « Question », « Message », « Montrer », « Éclairage RGAA »,
  « Éclairage accessibilité » ;
- structurelles, donc retirées : « Titre », « Badge », « Mémo », « Footer »,
  « Pagination », « Citation », « Bloc », « Questions », « Alerte » ;
- reformulées comme la slide les compose : « Bloc Opquast » devient « Opquast : » et
  « Bloc RGAA » devient « RGAA : ».

Le bandeau d'en-tête de marque, identique sur les quarante visuels, est repris en tête de
chaque liste, parce qu'il est visible à l'écran.

Le storyboard ne décrit que le panneau textuel de gauche. Il ignore tout le texte imprimé
à l'intérieur des illustrations : fils d'Ariane, libellés de schéma, étiquettes de flèches,
contenus des maquettes de navigateur. Ces textes ont donc été transcrits visuel par visuel
et insérés dans `textes_visibles`, juste avant le pied de page. Sans cela, un utilisateur
de lecteur d'écran aurait perdu, par exemple, les huit libellés du schéma de la slide 3 ou
les quatre étapes clavier de la slide 29.

## Défauts relevés dans les visuels

Deux défauts sont cuits dans les images. Ils sont transcrits littéralement, la fidélité au
texte visible primant, mais ils appellent une décision sur une éventuelle regénération des
visuels concernés.

Slide 32 : l'encart rouge affiche « Éniter les raccourcis mono-touche ». La forme attendue
est « Éviter ». Vérifié sur l'image le 28 septembre 2026.

Slide 37 : les deux maquettes de navigateur affichent des libellés de menu incohérents
entre elles, « Resources » à gauche et « Ressources » à droite.

## Images

Les quarante PNG viennent du dossier `slides-png` du projet source, déjà nommés
`slide-01.png` à `slide-40.png`, sans préfixe.

Trente-huit d'entre eux mesuraient 1672 par 941 pixels, les deux autres, `slide-01` et
`slide-10`, 1600 par 900. L'ensemble a été ramené à 1600 par 900 par rééchantillonnage
Lanczos, pour une série homogène. Le ratio 16/9 est préservé et l'écart est invisible à
l'œil.

La normalisation seule a un coût : elle fait passer le poids total de 37,5 à
39,1 mégaoctets, soit 4,3 pour cent de plus. Le rééchantillonnage transforme des aplats
nets en dégradés interpolés, qui se compressent moins bien que les originaux.

Les images ont donc été recompressées avec `oxipng` 10.2.1, installé le 28 septembre 2026
sur décision d'Alex, en `-o max --strip safe`. Le poids retombe à 36,2 mégaoctets, soit
7,5 pour cent de moins qu'après normalisation, et 3,5 pour cent de moins que le lot
d'origine. Le ZIP a été reconstruit dans la foulée, comme l'exige toute modification
d'image postérieure à une génération.

Cette recompression est sans perte, et la preuve est faite : l'empreinte SHA-256 des
pixels décodés des quarante images concaténées est identique avant et après,
`f02fa5c5c7452de04011b2c8b197785f`. Les dimensions restent 1600 par 900 sur les quarante.

Une quantification en palette aurait réduit le poids de 35 à 55 pour cent, mais avec
perte : mesure du 28 septembre 2026, écart colorimétrique moyen de 0,98 sur 255 et léger
banding dans les halos dégradés, visible au zoom. Cette piste a été écartée au profit de
la compression sans perte.

## Typographie

Les trois jeux Opquast déjà publiés ne portent aucun demi-cadratin. Le pied de page des
visuels affiche « LOTS 1–4 » avec un demi-cadratin : il est ramené au trait d'union dans
`slides.json`, comme le jeu `nouveautes-opquast-v5` l'avait fait pour les cadratins. Les
visuels ne sont pas retouchés et conservent leur typographie d'origine.

Le titre de la slide 1 portait une apostrophe droite dans le titre de section du
storyboard, là où le bloc de textes visibles et le visuel portent l'apostrophe
typographique. C'est cette dernière qui est retenue.

Aucun cadratin, aucun demi-cadratin et aucune apostrophe droite ne subsistent dans
`slides.json`.

## Divergence du générateur

Le `build.py` de ce jeu diverge d'une ligne de celui de `matrice-slide-ai/`.

La substitution qui transforme les adresses HTTPS en liens cliquables s'applique après
l'échappement HTML. À ce stade, le caractère `<` est déjà devenu `&lt;`, si bien que la
classe `[^\s<]` qui devait borner l'adresse ne borne plus rien. La slide 20 affiche un
extrait de sitemap XML contenant `<loc>https://…</loc>` : l'adresse tronquée et la balise
fermante échappée étaient avalées ensemble dans un `href`, que `vnu` rejetait comme hôte
invalide sur `index.html` et sur `alternatives.html`.

Le motif exige désormais que l'hôte commence par un caractère alphanumérique. L'adresse
réelle de la slide 17 reste cliquable, l'adresse tronquée de la slide 20 reste affichée
mais n'est plus transformée en lien.

Ce défaut est présent à l'identique dans `matrice-slide-ai/build.py` et n'y a pas été
corrigé : la décision d'une correction en amont revient à Alex. Tout futur jeu comportant
une adresse tronquée rencontrera le même rejet.

## Réserves de lecture

Ce support n'a fait l'objet d'aucun audit RGAA dédié et ne déclare aucune conformité.

Le fichier `README-LIVRABLES.txt` du projet source déclare explicitement quatre contrôles
non exécutés à la production des visuels : publication GitHub, revue externe, test humain
des trois secondes, et vérification API Opquast règle par règle. Aucun de ces quatre
contrôles n'a été rejoué à l'occasion de cette publication.

Les numéros et libellés des règles Opquast cités par les visuels et par les discours
n'ont donc pas été confrontés à l'API Opquast. Cette vérification reste à faire.

Les alternatives textuelles courtes et les transcriptions du texte des illustrations ont
été produites à partir des visuels lors de cette édition. Elles n'ont pas été relues par
un tiers.

## Traçabilité

Le projet source conserve `MANIFESTE.json` et `MANIFESTE-SHA256.txt`, qui portent les
empreintes des livrables d'origine, ainsi que `preuves-production/` avec les prompts de
génération, les revues par slide et les rapports de contrôle qualité par lot.

Les images publiées dans `assets/slides/` ayant été rééchantillonnées, leurs empreintes ne
correspondent plus à celles du manifeste source.
