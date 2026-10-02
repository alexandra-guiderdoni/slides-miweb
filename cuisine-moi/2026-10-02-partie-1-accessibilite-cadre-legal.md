Partie 1 - Accessibilité et cadre légal : notes cuisine-moi
==========================================================

Date : 2026-10-02 | Objectif : cadrer une présentation visuelle fidèle aux slides 15 à 53 de la partie 1 du PPTX IGPDE.

## Résumé / décisions clés

- Reprendre les slides PPTX 15 à 53 incluses, soit 39 slides.
- Produire 39 visuels en correspondance stricte 1 pour 1 avec les 39 slides PPTX.
- Appliquer une traduction visuelle contrainte : titre exact, message principal et libellés indispensables dans l’image ; contenu complet dans la transcription.
- Numéroter la présentation web de 1 à 39 et conserver la correspondance PPTX 15 à 53 dans le storyboard et les fichiers de traçabilité.
- Conserver la grammaire visuelle « IGPDE Accessibilité - bleu illustré » validée pour les séries précédentes.
- Conserver deux accordéons distincts par slide : transcription fidèle du contenu visible et discours oral issu des notes `add_notes()` existantes.
- Valider le storyboard complet, puis quatre slides étalons représentatives, avant la génération massive.
- Nommer la présentation « Partie I - Accessibilité numérique et cadre légal ».
- Utiliser le slug `partie-1-accessibilite-numerique-et-cadre-legal`.
- Régénérer intégralement les six personas dans le style IGPDE, avec une diversité crédible, des situations concrètes et une représentation non caricaturale des handicaps et technologies d’assistance.
- Conserver dans le visuel et la transcription de la slide web 01 le titre PPTX exact « Partie I - Accessibilité et cadre légal » ; réserver « Partie I - Accessibilité numérique et cadre légal » au titre public de la présentation.
- Après validation du storyboard complet, produire quatre étalons : web 01 / PPTX 15, web 09 / PPTX 23, web 26 / PPTX 40 et web 38 / PPTX 52.
- Compréhension partagée confirmée par Alex avant la rédaction du storyboard complet.
- Pour l'étalon web 38 / PPTX 52, générer à gauche une illustration IGPDE générique d'un PDF accessible et superposer à droite le logo FALC authentique. Ne pas réutiliser `scripts/images/rapport-dia-2024.jpg`, qui est un pictogramme PDF générique et non la couverture du rapport DIA.
- Pour l'étalon web 26 / PPTX 40, n'afficher dans le visuel que le QR code authentique et l'URL principale d'Obligally. Les liens `Simuler` et `Comprendre` restent disponibles dans la transcription HTML.
- Corriger les associations entre besoins et technologies dans les slides web 10 à 12 et dans les sources PPTX correspondantes : agrandissement, contraste et synthèse vocale pour Anaïs ; sous-titres relus, transcription et alertes visuelles pour Justine ; clavier/contacteurs, trackball et commande vocale pour Agathe.
- Limiter chaque transcription HTML au texte visible du PPTX. Exclure les lignes internes `Illustration :` et `Illustrations :`, puis décrire le nouveau visuel avec une alternative textuelle spécifique.
- N'autoriser dans les images que des libellés attestés dans le texte visible de la slide correspondante. Les reformulations pédagogiques restent possibles dans la description de la scène, mais ne doivent pas devenir du texte affiché.
- Pour la slide 39, conserver les usages du support d'origine : poussette, personne âgée, femme enceinte et personne en fauteuil. Ne pas ajouter le bandeau `#accessibleatous` au nouveau visuel.
- Pour la slide 22, appliquer le droit en vigueur depuis 2023 : jusqu'à 50 000 EUR pour le non-respect de l'obligation d'accessibilité des organismes publics et assimilés ; jusqu'à 25 000 EUR pour les obligations déclaratives. Supprimer la formule obsolète `par service non conforme` et identifier l'Arcom comme autorité de contrôle.
- Pour la slide 20, comparer les quatre temporalités à partir de la seule ligne `Manipulation` : `Une seule main`, `Bras cassé`, `Un bébé dans les bras` et `Douleurs`. Conserver la matrice complète dans l'accordéon.
- Pour la slide 28, représenter trois documents de pilotage, un moyen de contact et un RAN humain. Conserver le tableau des mentions de conformité uniquement dans l'accordéon.
- Pour la slide 38, utiliser l'URL FALC officielle terminée par `.pdf`. Conserver `FLAC` dans le chemin, car cette coquille appartient à l'URL publiée par `handicap.gouv.fr` et sa correction casserait le lien.
- Pour la slide 4, présenter les WCAG comme la référence internationale et rattacher exclusivement au RGAA les 106 critères regroupés en 13 thématiques.
- Pour la slide 34, utiliser un symbole de QR volontairement non scannable, sans destination ni fausse URL. Il sert uniquement à illustrer la règle du lien visible associé.
- Avant les quatre étalons, produire une planche de référence unique pour les six personas et la communicante récurrente. Elle verrouille leur apparence, leur tenue et leurs équipements afin d'assurer leur continuité sans caricaturer le handicap.
- Classer les 39 slides dans les six familles canoniques du preset local : `ouverture_illustree`, `comparaison_transformation`, `processus_horizontal`, `tableau_pedagogique`, `checklist_processus` et `synthese_action`. Les personas relèvent de `synthese_action`, avec la variante `persona`.
- Pour la slide 18, rendre les trois chiffres autonomes en associant `1/5`, `85%` et `1er` à leur phrase explicative exacte du PPTX. Aucun chiffre ne doit apparaître seul comme élément décoratif.
- Pour la slide 19, intégrer sous la comparaison un bandeau de conclusion `Ce que ça change pour vous` contenant les trois conséquences pratiques exactes du PPTX.
- Clore la phase `cuisine-moi`, effectuer une passe technique finale du storyboard, puis produire une planche de référence des personnages et les quatre étalons 01, 09, 26 et 38. La génération massive reste interdite avant leur validation.

## Journal questions-réponses

### Q1 - Titre public de la présentation
- Question : faut-il nommer la série « Accessibilité numérique et cadre légal », adopter une formulation plus pédagogique ou reprendre l’intitulé général « Communication accessible et cadre légal » ?
- Capture : Alex choisit « Accessibilité numérique et cadre légal » et demande d’ajouter le numéro de la partie. Le titre public retenu est donc « Partie I - Accessibilité numérique et cadre légal ».
- Drapeaux : Aucun.

### Q2 - Slug public
- Question : faut-il inclure le numéro de partie dans le slug, conserver un slug plus court ou reprendre le chiffre romain du titre ?
- Capture : Alex valide `partie-1-accessibilite-numerique-et-cadre-legal`.
- Drapeaux : Aucun.

### Q3 - Traitement visuel des personas
- Question : faut-il régénérer les six personas dans le style IGPDE, réutiliser les portraits actuels ou adopter une approche hybride ?
- Capture : Alex choisit une régénération complète dans le style IGPDE afin de maximiser la cohérence, tout en conservant les profils, besoins et technologies d’assistance. Les personnages doivent refléter une diversité crédible et des situations concrètes, sans caricaturer le handicap.
- Drapeaux : Aucun.

### Q4 - Titre public et titre source de la slide 15
- Question : faut-il conserver dans le visuel et la transcription le titre PPTX exact « Partie I - Accessibilité et cadre légal », tout en utilisant « Partie I - Accessibilité numérique et cadre légal » comme titre public de la présentation ?
- Capture : Alex confirme cette séparation. Le titre du visuel et de sa transcription reste fidèle au PPTX ; le titre public peut être plus explicite.
- Drapeaux : Aucun.

### Q5 - Sélection des quatre étalons
- Question : faut-il valider un panel équilibré couvrant l’ouverture, une scène humaine, une ressource interactive et une comparaison documentaire, ou privilégier davantage le contenu juridique ou la conclusion ?
- Capture : Alex valide le panel recommandé : web 01 / PPTX 15 pour l’ouverture, web 09 / PPTX 23 pour le persona Amir, web 26 / PPTX 40 pour l’activité Obligally avec QR code et liens, et web 38 / PPTX 52 pour la comparaison entre PDF accessible et version FALC.
- Drapeaux : Aucun.

### Q6 - Confirmation du cadrage
- Question : le cadrage partagé est-il suffisamment précis pour rédiger le storyboard détaillé des 39 slides ?
- Capture : Alex confirme la compréhension partagée et autorise la rédaction du storyboard complet.
- Drapeaux : Aucun.

### Q7 - Traitement documentaire de l'étalon 38
- Question : faut-il régénérer une illustration générique de PDF accessible dans le style IGPDE, conserver le pictogramme PDF actuel ou attendre une couverture authentique du rapport DIA ?
- Capture : Alex valide la recommandation : générer une illustration IGPDE générique du PDF accessible à gauche et superposer uniquement le logo FALC authentique dans la colonne FALC à droite. Le fichier `scripts/images/rapport-dia-2024.jpg` ne doit pas être utilisé comme couverture, car il contient seulement un pictogramme PDF générique.
- Drapeaux : la transcription reste fidèle au contenu actuel du PPTX ; la description d'illustrations inexacte dans la source sera traitée séparément si Alex autorise une correction du PPTX.

### Q8 - Liens visibles de l'étalon 26
- Question : faut-il afficher uniquement le QR code et l'URL principale d'Obligally dans le visuel, en conservant les liens secondaires `Simuler` et `Comprendre` dans l'accordéon HTML ?
- Capture : Alex confirme cette hiérarchie. Le QR code authentique, la mention `Scannez-moi !` et l'URL principale seront superposés de façon déterministe ; les deux liens secondaires resteront dans la transcription exacte, sans être intégrés au visuel.
- Drapeaux : Aucun.

### Q9 - Technologies des personas 10 à 12
- Question : faut-il corriger également les sources PPTX avant d'aligner le storyboard et les accordéons sur des associations cohérentes entre besoins et technologies ?
- Capture : Alex autorise la correction des sources. Les trois ensembles retenus sont : agrandissement, contraste renforcé et synthèse vocale pour la malvoyance ; sous-titres relus, transcription et alertes visuelles pour la surdité ; clavier/contacteurs, souris trackball et commande vocale pour la déficience motrice. Les galeries d'images ambiguës sont remplacées par trois cartes textuelles afin de ne pas attribuer un visuel trompeur à une technologie.
- Drapeaux : le deck complet ne sera pas régénéré pendant le chantier parallèle sur la partie 2.

### Q10 - Périmètre des transcriptions HTML
- Question : faut-il retirer des transcriptions les lignes internes `Illustration : …`, absentes du texte visible du PPTX, et réserver la description du nouveau visuel à sa véritable alternative textuelle ?
- Capture : Alex confirme cette règle pour toute la série. Les six descriptions internes repérées dans le storyboard sont exclues des transcriptions ; le reste du contenu visible demeure inchangé. Chaque image générée conservera son alternative courte candidate, ajustée au visuel final si nécessaire.
- Drapeaux : les descriptions internes erronées restent présentes dans les sources PPTX tant qu'une correction spécifique de ces métadonnées n'est pas autorisée ; elles ne bloquent plus la présentation web.

### Q11 - Provenance du texte affiché dans les visuels
- Question : faut-il limiter les listes blanches aux libellés réellement présents dans le PPTX, en réservant les reformulations à la mise en scène non textuelle ?
- Capture : Alex confirme cette règle. L'audit exhaustif repère 17 slides contenant au moins un libellé absent ou reformulé. Ces libellés sont supprimés ou remplacés par une formulation attestée dans la transcription correspondante ; les scènes peuvent continuer à traduire pédagogiquement le message sans ajouter de texte inventé.
- Drapeaux : Aucun.

### Q12 - Usages représentés sur la slide 39
- Question : faut-il rétablir la femme enceinte du support d'origine à la place de la personne avec un bagage et écarter le bandeau `#accessibleatous` du nouveau visuel ?
- Capture : Alex confirme. La scène finale représente une poussette, une personne âgée, une femme enceinte et une personne en fauteuil utilisant le même chemin intégré. Aucun bandeau `#accessibleatous` n'est généré ni superposé.
- Drapeaux : Aucun.

### Q13 - Sanctions d'accessibilité numérique
- Question : faut-il vérifier le montant de 25 000 EUR auprès d'une source officielle puis corriger la source PPTX, le storyboard et l'accordéon si nécessaire ?
- Capture : Alex autorise la vérification et la correction. L'article 47-1 de la loi du 11 février 2005, en vigueur depuis le 8 septembre 2023, distingue deux plafonds : 50 000 EUR pour le non-respect de l'obligation d'accessibilité mentionnée au I de l'article 47, et 25 000 EUR pour le non-respect des obligations déclaratives prévues aux III et IV. La formule `par service non conforme` ne figure plus dans le texte en vigueur. La slide précise aussi que l'Arcom est l'autorité de contrôle depuis 2023 ; la DINUM édite le RGAA et accompagne les administrations.
- Drapeaux : les sanctions ne sont pas présentées comme automatiques ; l'Arcom procède d'abord à une mise en demeure.

### Q14 - Densité visuelle de la slide 20
- Question : faut-il limiter l'image à un exemple illustré pour chacun des quatre types de situations et conserver la matrice complète dans l'accordéon sémantique ?
- Capture : Alex confirme cette simplification puis valide la ligne `Manipulation` comme fil conducteur. Le visuel comporte quatre colonnes : `Permanent - Une seule main`, `Temporaire - Bras cassé`, `Situationnel - Un bébé dans les bras` et `Vieillissement - Douleurs`. Les seize exemples de la source restent intégralement présents dans la transcription HTML.
- Drapeaux : Aucun.

### Q15 - Nature des obligations de la slide 28
- Question : faut-il représenter trois documents, un canal de contact et un RAN humain, sans reprendre le tableau des statuts dans l'image ?
- Capture : Alex confirme cette formulation corrigée. Le SPAN, le plan d'action annuel et l'audit RGAA sont représentés comme des documents ; le moyen de contact comme un canal ; le RAN comme une personne qui pilote la démarche. Les trois mentions de conformité restent dans le tableau sémantique de la transcription.
- Drapeaux : Aucun.

### Q16 - Lien FALC du rapport DIA 2024
- Question : faut-il vérifier l'adresse officielle puis corriger la source PPTX et le storyboard pour rendre le lien FALC fonctionnel ?
- Capture : Alex autorise la vérification et la correction. La page officielle de la DIA lie le document vers `delegation-interministerielle-accessibilite-synthese-FLAC-rapport-activite-2024.pdf`. Le segment `FLAC` est donc conservé tel quel dans le chemin officiel ; l'erreur locale était l'absence de l'extension `.pdf`. Le lien visible `Télécharger (handicap.gouv.fr)` de la colonne FALC doit pointer vers cette adresse exacte.
- Drapeaux : Aucun.

### Q17 - Distinction WCAG et RGAA sur la slide 4
- Question : faut-il corriger l'alternative afin de ne plus attribuer les 106 critères et 13 thèmes à l'ensemble WCAG/RGAA ?
- Capture : Alex confirme. Les WCAG sont présentées comme la référence internationale du W3C ; le RGAA est le référentiel français composé de 106 critères regroupés en 13 thématiques. La scène conserve le passage de la référence internationale vers la méthode française.
- Drapeaux : Aucun.

### Q18 - Statut du QR de la slide 34
- Question : faut-il inscrire dans le storyboard que le QR est purement schématique, non scannable et dépourvu d'URL inventée ?
- Capture : Alex confirme. La source PPTX ne contient ni composant QR, ni image QR, ni URL : la troisième carte expose seulement les règles de production. Le nouveau visuel utilise donc un symbole simplifié de QR pour montrer qu'un lien visible doit toujours l'accompagner, sans simuler un accès réel.
- Drapeaux : Aucun.

### Q19 - Planche de référence des personnages
- Question : faut-il créer avant les quatre étalons une planche de référence unique pour les six personas et la communicante, afin de stabiliser leurs visages, tenues et technologies dans toute la série ?
- Capture : Alex confirme. La planche comprendra sept vignettes cohérentes dans le style IGPDE. Les six personas restent fidèles à leurs profils professionnels, besoins et technologies, sans reprendre les portraits sources ni utiliser de marqueur caricatural du handicap. La communicante reprend la silhouette féminine aux longs cheveux foncés et à la tenue bleue déjà appréciée dans la série réseaux sociaux.
- Drapeaux : Aucun.

### Q20 - Familles canoniques de mise en page
- Question : faut-il respecter les six familles techniques du preset local et traiter `persona` comme une variante de `synthese_action`, plutôt que remplacer la famille `checklist_processus` par une famille persona non canonique ?
- Capture : Alex confirme. Les 39 slides utilisent exclusivement `ouverture_illustree`, `comparaison_transformation`, `processus_horizontal`, `tableau_pedagogique`, `checklist_processus` et `synthese_action`. Les slides 09 à 14 sont classées `synthese_action`, variante `persona`.
- Drapeaux : Aucun.

### Q21 - Contexte des chiffres de la slide 18
- Question : faut-il accompagner `1/5`, `85%` et `1er` d'un libellé explicatif court repris mot pour mot du PPTX, afin que les chiffres ne soient pas ambigus dans le visuel ?
- Capture : Alex confirme. Chaque carte conserve le nombre affiché dans le PPTX et sa phrase explicative complète : `1 personne sur 5 est en situation de handicap ou connaît un trouble invalidant.`, `des handicaps sont acquis au cours de la vie` et `Le handicap est le 1er facteur de discrimination selon le Défenseur des droits`.
- Drapeaux : Aucun.

### Q22 - Conclusion pratique de la slide 19
- Question : faut-il intégrer `Ce que ça change pour vous` comme conclusion basse du visuel, avec le contenu exact du PPTX, plutôt que le conserver uniquement dans l'accordéon ?
- Capture : Alex confirme. Un bandeau bas suit la comparaison en trois états et reprend les trois formulations sources : `C'est l'environnement qui crée le handicap, pas la personne`, `Un document inaccessible = une barrière que vous pouvez lever` et `Mettre en accessibilité votre communication supprime la situation de handicap`.
- Drapeaux : Aucun.

### Q23 - Clôture du storyboard et passage aux étalons
- Question : faut-il clore la phase `cuisine-moi`, effectuer une dernière passe technique sans nouvel arbitrage éditorial, puis produire la planche des personnages avant les quatre étalons ?
- Capture : Alex confirme. La passe technique peut corriger la sémantique prévue pour les accordéons, réduire la densité des visuels sans retirer de contenu aux transcriptions et harmoniser les libellés. Elle est suivie de la planche de référence, puis des seuls étalons 01, 09, 26 et 38.
- Drapeaux : la génération des 35 autres visuels reste soumise à la validation explicite des quatre étalons.

## Drapeaux ouverts

- Les descriptions internes erronées du PPTX pourront faire l'objet d'une correction séparée ; elles sont hors transcription web et ne bloquent pas la série.
- La note orale de la slide 26 mentionne le chemin inexistant `_source/références/`. Le chemin réel est `_source/references/`. La transcription orale reste fidèle à la source tant qu'une correction du PPTX n'est pas autorisée ; ce point ne bloque pas les visuels.

## Prochaine étape

- Storyboard complet rédigé dans `cuisine-moi/2026-10-02-partie-1-accessibilite-numerique-et-cadre-legal-storyboard.md`.
- Passe interne de fidélité et de cohérence terminée : 39 slides, 39 transcriptions, 39 discours oraux, 39 alternatives et correspondance PPTX 15 à 53 continue.
- Phase `cuisine-moi` close : compréhension partagée confirmée.
- Prochaine étape autorisée : passe technique finale, planche de référence des personnages, puis étalons 01, 09, 26 et 38.
- Génération massive, intégration HTML, publication, commit et push : hors périmètre à ce stade.
