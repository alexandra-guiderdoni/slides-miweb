# Corrections proposées dans l’issue #15

État au 2 novembre 2026 : 74 PNG corrigés sur 132, avec synchronisation des textes associés et du storyboard. Les 25 QCM ont été revus ; les diagnostics T0/T1 partagent les mêmes affirmations. Les points conservés et leurs raisons figurent dans [les arbitrages de finition](arbitrages-finitions.md). Les sections suivantes conservent l’historique des étapes, y compris les anciennes mentions « aucune publication » et les versions ensuite remplacées.

Le propriétaire a validé le rendu local et demandé le commit, le push et une revue ShipGuard. La relecture éditoriale indépendante reste partielle : voir [son périmètre exact](relecture-croisee-partielle.md). Cette limite ne doit pas être transformée en réception indépendante complète.

Contrôles de livraison : les 132 PNG mesurent 1672 x 941 pixels ; 74 diffèrent de la base `38556c5`. Les deux ZIP pèsent 59,43 et 69,65 Mio, couvrent exactement 1-66 et 67-132 sans doublon, et embarquent les PNG et alternatives Markdown identiques aux fichiers courants. L’accueil racine et le catalogue sont inchangés.

Vérifications du lot complet avant commit : contrôle des notes (132 slides, 0 erreur, 0 avertissement), 20 tests des scripts, 14 tests du jeu et validation HTML réussis. Scan sécurité des 655 lignes HTML ajoutées : aucun motif dangereux détecté ; scripts et styles intégrés inchangés. Recette Chrome locale sur les slides 98/99 : ouverture des deux accordéons, textes et réponse B cohérents, navigation suivante et retour ; mode toutes les slides affichant les 132 images. Il s’agit d’une recette par échantillon, distincte de la relecture visuelle de chaque PNG pendant sa production et de la réception indépendante complète.

La [revue ShipGuard indépendante de livraison](revue-shipguard-livraison.md) a relevé un écart faible de synchronisation du storyboard 070, corrigé après revue et vérifié sur les 132 listes. Aucun bug des deux HTML modifiés n’a été identifié. Sa limite de réception visuelle exhaustive reste explicite.

## Slide 028 - faute d’en-tête

- Proposition : `slide-028-entete-v1.png`, générée avec ImageGen.
- Correction : « EXPÉRIIENCES DURABLES » devient « EXPÉRIENCES DURABLES ».
- Dimensions vérifiées : 1672 x 941 pixels.
- SHA-256 : `0834b1bdad90851228958cf797fd399a1cb278c665caab6c454226f8c6d96ff1`.
- Prompt : `../prompts/slide-028-correction-entete-v1.txt`.
- Validation utilisateur : accord explicite « oui » dans la conversation du 1 novembre 2026, après présentation de la proposition.
- État : correction validée pour intégration ; aucune publication effectuée à ce stade.

## Slide 049 - faute d’en-tête

- Prompt : `../prompts/slide-049-correction-entete-v1.txt`.
- Proposition : `slide-049-entete-v1.png`, générée avec ImageGen.
- Dimensions vérifiées : 1672 x 941 pixels.
- SHA-256 : `a76a319d0d816e6533115155b1c39e3e399ce4841471330c3585892f56d105ee`.
- Relecture visuelle : en-tête corrigé, autres textes et composition conservés visuellement.
- Validation utilisateur : accord explicite « oui go » après présentation de la proposition.
- État : correction validée pour intégration ; aucune publication effectuée.
- Périmètre : correction de l’en-tête uniquement. Le cadrage du bras, également signalé dans l’issue, reste à traiter séparément.
- Réserve découverte après l’accord : un contrôle OCR complémentaire sans correction linguistique lit « EXPÉRTIENCES DURABLES ». Cette lecture soulève un doute sur un caractère supplémentaire. L’accord utilisateur est conservé, mais l’image doit être réexaminée avant intégration.

### Seconde proposition après réexamen

- Proposition : `slide-049-entete-v2.png`, générée avec ImageGen à partir de la première proposition.
- Prompt : `../prompts/slide-049-correction-entete-v2.txt`.
- Dimensions vérifiées : 1672 x 941 pixels.
- SHA-256 : `77c165070fbab98caff690329f8b63bc6c02e4f046846eb539148412d3a5e1f8`.
- Contrôle : relecture visuelle et OCR sans correction linguistique ; la ligne est désormais lue « EXPÉRIENCES DURABLES ». Les autres textes et la composition sont conservés visuellement.
- La seconde proposition remplace la première comme candidate à l’intégration. La première reste conservée pour traçabilité et ne doit pas être intégrée.
- Validation utilisateur : accord explicite « go » après présentation de la seconde proposition.
- État : seconde proposition validée et intégrée en local ; aucune publication effectuée.

## Slide 117 - faute d’en-tête

- Tentatives 1 et 2 rejetées : le contrôle OCR lit encore « EXPÉRIIENCES DURABLES ».
- Proposition retenue pour discussion : `slide-117-entete-v3.png`, générée avec ImageGen.
- Prompt : `../prompts/slide-117-correction-entete-v3.txt`.
- Références : image publiée 117 et proposition corrigée 028 pour l’orthographe uniquement.
- Dimensions vérifiées : 1672 x 941 pixels.
- SHA-256 : `3fd034b04e22a18a0ffcd7429ffb48f46a7bfa909df93a840776d6102930eff8`.
- Contrôle : relecture visuelle et OCR sans correction linguistique ; l’en-tête est lu « EXPÉRIENCES DURABLES ». Le contenu du QCM et la composition restent visuellement conservés.
- Validation utilisateur : accord explicite « oui » après présentation de la troisième proposition.
- État : correction validée pour intégration ; aucune publication effectuée.

## Slide 125 - faute d’en-tête

- Tentatives 1 à 3 rejetées : la faute persiste et le contrôle OCR lit « EXPÉRIIENCES DURABLES ».
- Proposition retenue pour discussion : `slide-125-entete-v4.png`, générée avec ImageGen.
- Prompt : `../prompts/slide-125-correction-entete-v4.txt` ; référence : image publiée 125.
- Dimensions vérifiées : 1672 x 941 pixels.
- SHA-256 : `b1ba119e60cfd41d4eeccb71da5d12fd7300decd2d2417745d02fbb4e24405dd`.
- Contrôle : relecture visuelle et OCR sans correction linguistique ; l’en-tête est lu « EXPÉRIENCES DURABLES ». Le contenu du QCM et la composition restent visuellement conservés.
- Validation utilisateur : accord explicite « oui go » après présentation de la quatrième proposition.
- État : correction validée pour intégration ; aucune publication effectuée.

## Intégration locale du premier point

Les mentions « pour intégration » ci-dessus retracent les décisions successives. L’état courant est l’intégration locale des quatre versions retenues, après validation de chacune par l’utilisateur.

| Slide | Proposition retenue | SHA-256 du PNG intégré après optimisation sans perte |
|---|---|---|
| 028 | `slide-028-entete-v1.png` | `8b276bd0937c8dddbdebe0fe4ab851509dbe43b3097012de4ef3d32c45a87374` |
| 049 | `slide-049-entete-v2.png` | `d64a223a244dda2935bfa40d93c971c5e901fd2776b76e995e00168bf4da1c14` |
| 117 | `slide-117-entete-v3.png` | `4992e5690037c57c0dd41fc1874add6b7d2a1421dc8d67f99b32c9dda7ec3884` |
| 125 | `slide-125-entete-v4.png` | `6727d6859a0f43c2e1749756bbe71216a6ae7a49e214c0b66b66b6cad839aa59` |

Contrôles effectués :

- `scripts/optimiser-images.sh` exécuté sur un dossier temporaire contenant uniquement les quatre images retenues : identité des pixels avant et après recompression confirmée.
- Passe `alt-text` sur les quatre entrées : alternatives courtes conservées, pertinentes avec les titres et descriptions adjacentes. Les transcriptions et listes de textes visibles portaient déjà la bonne orthographe ; `slides.json` ne nécessite donc aucune modification pour ce point.
- Contrôle des notes : 132 slides, aucune erreur ni avertissement.
- Tests de `scripts/tests` : 20 réussis.
- Génération autonome du jeu avec `build.py`.
- `scripts/validate_variant.sh ecommerce-opquast-v5` : 14 tests réussis, validations HTML réussies.
- Comparaison avec `HEAD` : seules les images 028, 049, 117 et 125 changent ; les 128 autres PNG sont identiques.
- Archives : 58,28 Mio et 64,38 Mio, chacune strictement sous 100 Mio ; 66 images par partie, couverture exacte des 132 slides, sans trou ni doublon ; images et alternatives embarquées identiques aux fichiers courants.
- Pages HTML, alternatives, catalogue et accueil racine inchangés.

Limites : pas de nouvelle recette navigateur complète, aucun commit, push ni mise à jour de la case GitHub à ce stade. Le cadrage du bras de la slide 049 et les révisions pédagogiques des QCM restent hors de ce premier point.

## Slide 017 - mention explicite d’indisponibilité

- Proposition : `slide-017-indisponible-v1.png`, générée avec ImageGen à partir de l’image publiée 017.
- Prompt et liste blanche : `../prompts/slide-017-indisponible-v1.txt`.
- Modification autorisée : ajouter « Indisponible » sur la fiche du tee-shirt central grisé. Les barres grises de remplissage à cet endroit sont remplacées par la mention ; le tee-shirt et le bouton restent grisés.
- Dimensions vérifiées : 1672 x 941 pixels.
- SHA-256 : `4cda3c3243bc6f326c26c6274780f469bed4e6864dbd55b418b57d8fdaec9c2b`.
- Contrôle : relecture visuelle et OCR sans correction linguistique ; mention correctement orthographiée et rattachée au bon produit, autres textes conservés.
- Source : [fiche officielle de la règle 65](https://checklists.opquast.com/fr/qualite-numerique/les-produits-indisponibles-font-lobjet-dune-differenciation-visuelle-et-textuelle), consultée pendant cette correction. Elle distingue la mention textuelle et l’indication graphique accompagnée d’une alternative appropriée. Le MCP avait renvoyé le même contrôle depuis son instantané local du 3 septembre 2026, en repli après un accès API refusé ; la page publique confirme ces éléments.
- Validation utilisateur : accord explicite « oui go » après présentation de la proposition.
- État : correction validée et intégrée en local ; aucune publication effectuée.
- Contenus synchronisés : alternative courte de 72 caractères relue selon `alt-text`, description, textes visibles, transcription et phrase des notes décrivant le grisé seul ; storyboard actualisé avec renvoi vers le prompt courant. Les 131 autres entrées de `slides.json` sont inchangées.
- Optimisation : `scripts/optimiser-images.sh` exécuté sur un dossier temporaire contenant uniquement la slide 017, sans changement des pixels. SHA-256 du PNG intégré : `d73ceb0ce372c77b54b07964c52e2118c73e882647e2c23798c1641a5dd58503`.
- Vérifications : notes orales sans erreur ni avertissement pour les 132 slides, 20 tests des scripts et 14 tests du jeu réussis, validations HTML réussies, exports HTML et Markdown synchronisés.
- Archives reconstruites : 58,29 Mio et 64,38 Mio, 66 slides par partie ; couverture exacte des 132 images sans trou ni doublon ; images et alternatives embarquées identiques aux fichiers courants.
- Bilan cumulé : cinq PNG modifiés par rapport à `HEAD` (017, 028, 049, 117 et 125), 127 PNG identiques ; aucune modification de l’accueil racine ni du catalogue.

## Slide 047 - mémo sur la finalisation de la commande

- Proposition : `slide-047-finalisation-v1.png`, générée avec ImageGen à partir de l’image publiée 047.
- Prompt et liste blanche : `../prompts/slide-047-finalisation-v1.txt`.
- Modification : remplacer les deux occurrences de « Avant validation définitive, je corrige. » par « Avant de finaliser la commande, je corrige. », dans la carte verte et le bandeau inférieur.
- Source : [API publique Opquast](https://api.opquast.com/checklist/public/?version=qualite-numerique), règle 38, consultée pendant cette correction. Le libellé actuel emploie « finalisation de la commande ». Le MCP renvoie encore l’ancien libellé depuis son instantané du 3 septembre 2026, en repli après un accès API refusé.
- Dimensions vérifiées : 1672 x 941 pixels.
- SHA-256 : `d8230a25cf2f9938d0cc209523e5aeb0787e8cd2f9b5da9fa9d5b57178ae55f4`.
- Contrôle : relecture visuelle à la résolution originale et OCR sans correction linguistique ; les deux mémos sont correctement orthographiés, les autres textes et la composition restent visuellement conservés.
- Les boutons « Ajouter » de chaque ligne sont conservés : leur révision relève d’un autre point de l’issue.
- Validation utilisateur : accord explicite « oui la suite ? » après présentation de la proposition.
- État : correction intégrée en local ; aucune publication effectuée.
- Contenus synchronisés : description, mémo visible, message, transcription et storyboard. La réserve des notes sur l’ancien mémo a été supprimée. Passe `alt-text` : alternative courte conservée, toujours fidèle au panier représenté et complétée par la description détaillée.
- Optimisation sans perte limitée à la slide 047 : pixels identiques. SHA-256 du PNG intégré : `e37e35833b86790b392561d5dac471e85f524303e022ced4c81cf9a94a917786`.
- Vérifications : 132 notes sans erreur ni avertissement, 20 tests des scripts et 14 tests du jeu réussis, validations HTML réussies et `git diff --check` sans erreur.
- Archives reconstruites : 58,47 Mio et 64,38 Mio, chacune 66 slides ; couverture exacte des 132 slides sans trou ni doublon, PNG et alternatives identiques aux fichiers courants.
- Bilan cumulé : six PNG modifiés, 126 identiques à `HEAD` ; seules les entrées 017 et 047 de `slides.json` changent. Accueil racine et catalogue inchangés. Pas de nouvelle recette navigateur complète à ce stade.


## Slide 070 - enveloppe sous la loupe

- Nouvelle observation : le trait blanc asymétrique pouvait se lire comme une coche ; ambiguïté retenue, sans affirmer la présence certaine d’un symbole de validation.
- Proposition : `slide-070-enveloppe-v1.png`, générée avec ImageGen à partir de l’image publiée.
- Prompt complet et liste blanche : `../prompts/slide-070-enveloppe-v1.txt`.
- Correction : rabat triangulaire symétrique et coutures inférieures de l’enveloppe sous la loupe de la carte C. La coche de l’option préactivée dans la carte B est conservée.
- Dimensions : 1672 x 941 pixels. SHA-256 : `34c9cd86e0c323457ceed3f1be41cbc4863d46ebe62375694d359e82080f7582`.
- Contrôle visuel et OCR : textes, numéros et pagination conservés ; l’enveloppe dispose de coutures explicites.
- Validation utilisateur : accord explicite « go » après présentation de la proposition.
- État : intégrée en local après optimisation sans perte limitée à 070 ; pixels identiques. SHA-256 intégré : `cce75ceda746d9a7f98e7758be1587e028af8c9abd30ed9320708a93dee694cc`.
- Description et transcription précisées, storyboard synchronisé ; glyphes ? et ! déjà visibles ajoutés à la liste canonique. Passe `alt-text` : alternative conservée, car le sens des trois constats reste identique ; description détaillée disponible.
- Notes : 132 slides sans erreur ni avertissement. Tests des scripts : 20 réussis. Archives reconstruites ; aucun commit ni push.

- Validation du jeu : 14 tests et validations HTML réussis. Couverture exacte des 132 PNG dans les deux archives, sans doublon, contenus embarqués identiques aux fichiers courants ; chaque archive reste sous 100 Mio. Bilan cumulé : sept PNG modifiés et 125 identiques à `HEAD`. Accueil et catalogue inchangés, `git diff --check` réussi.


## Slide 050 - bouclier et case précochée

- Observation à la résolution originale : la coche de la carte R32 est inscrite dans un contour de bouclier ; la carte R33 montre une case carrée bleue précochée. Les deux formes restent distinctes.
- Arbitrage proposé : conserver le visuel, confusion non confirmée lors de cette observation.
- Validation utilisateur : accord explicite « go » après présentation de cet arbitrage.
- État : image et contenus conservés, aucune régénération.

## Slides 046 et 064 - doute sur les chaussures

- Observation à la résolution originale : les bandes claires de 046 se situent sur le dessus et représentent les lacets. En 064, les traits blancs sont également des lacets ; les zones bleues latérales sont des empiècements.
- Aucun logo identifiable retenu lors de cette observation ; cela ne constitue pas une expertise de marques.
- Arbitrage validé par l’utilisateur (« oui ») : conserver les deux images. Aucune régénération.


## Slide 054 - pictogramme des cartes bancaires

- Observation à la résolution originale : quatre petits carrés clairs à la place habituelle d’une puce bancaire. Le dessin est stylisé ; aucun logo certain retenu.
- Arbitrage validé par l’utilisateur (« ok ») : conserver la slide. Aucune régénération.


## Slides 091 et 096 - écarts typographiques incertains

- Observation à la résolution originale : en 091, le séparateur du pied de page apparaît plus rond et marqué que sur certains autres visuels, sans gêner la lecture. En 096, « POUR TOUS » reste lisible avec une séparation entre les mots ; aucune fusion certaine retenue.
- Arbitrage proposé : conserver ces images pour ces seuls points typographiques, sans régénération dédiée. Les autres révisions des QCM et de mise en page restent ouvertes.
- Arbitrage validé par l’utilisateur (« ok ») : conservation pour ces seuls points typographiques.


## QCM 1 - slides 082/083

- Rédaction conservée après examen des indices de formulation ; accord utilisateur « ok ». Distracteurs fondés sur des confusions entre informations descriptives et mesures. La distribution des lettres reste à examiner sur la série.


## QCM 2 - slides 084/085

- Rédaction validée par l’utilisateur (« ok ») : le scénario précise un label attribué par un organisme indépendant fictif. Le lien aboutit chez le vendeur, qui nomme l’organisme mais ne donne pas accès à la source.
- Les distracteurs opposent page explicative du vendeur, identification de l’organisme et accès à la source. Le distracteur sur la validité au titre de R40 est remplacé. Bonne réponse maintenue en C à ce stade ; distribution globale encore à traiter.
- R64 et R40 consultées via MCP : repli local au 3 septembre 2026 après HTTP 403, puis vérification des fiches publiques officielles, qui confirment la portée des deux règles.
- Sources : https://checklists.opquast.com/fr/qualite-numerique/les-mentions-dappartenance-a-un-ordre-ou-groupe-professionnel-dun-label-ou-dune-recompense-sont-accompagnees-dun-lien-vers-la-source et https://checklists.opquast.com/fr/qualite-numerique/la-periode-et-les-conditions-de-validite-des-offres-speciales-et-promotions-sont-indiquees
- Prompts complets : `../prompts/slide-084-qcm2-v1.txt` et `../prompts/slide-085-qcm2-v1.txt`.
- Propositions graphiques en cours ; aucune intégration dans les assets publiés pour ce point.

- Propositions générées : `slide-084-qcm2-v1.png` et `slide-085-qcm2-v1.png`, chacune 1672 x 941 pixels.
- SHA-256 084 : `abd2b24d66671884dd83fe6bed54de6b9bf815d48defa2b84c05edb8bbd61052` ; 085 : `88fa3a2b433953b38890c6e4f55c78c84bffc00c9edfa38d2343fddf69a1bf22`.
- Contrôle visuel et OCR sans correction linguistique : rédaction conforme au prompt, en-têtes et numéros conservés, C concordante entre question et correction, justifications A/B correspondant aux nouveaux choix ; aucun corrigé visuel sur la question.
- Propositions soumises à validation utilisateur avant intégration ; contenus canoniques et archives encore inchangés pour cette paire.

- Validation graphique utilisateur : « go ». Paire intégrée en local après optimisation sans perte des seules images 084/085, pixels identiques.
- SHA-256 intégrés : 084 `88b0810aeeeb70c8f2fc334b04a3a1f241ada937c10ba9578929f1ebb34a2da0` ; 085 `45b81312d5743885cb70dff53f53c3248209663262d84207d121c10230dda0cf`.
- Passe `alt-text` : alternatives courtes actualisées sans dévoiler la réponse sur la question. Descriptions, textes visibles, transcriptions, notes et storyboard synchronisés. R40 retirée des règles et sources de cette paire car le distracteur correspondant a disparu.
- Contrôle des notes : 132 slides, aucune erreur ni avertissement après séparation de deux phrases sur une ligne ; 20 tests des scripts, 14 tests du jeu et validations HTML réussis.
- Archives : couverture exacte de 132 slides sans trou ni doublon, PNG et alternatives embarqués identiques aux fichiers courants ; tailles sous 100 Mio.
- Portée cumulée vérifiée : neuf PNG modifiés, 123 identiques à `HEAD` ; seules les entrées 017, 047, 070, 084 et 085 de `slides.json` diffèrent. Accueil et catalogue inchangés ; `git diff --check` réussi. Aucun commit ni push, pas de nouvelle recette navigateur complète.


## QCM 3 - slides 086/087

- Rédaction validée par l’utilisateur (« ok go poursuit ») : remplacer B par « B. R65 reste à satisfaire : une mention visible doit accompagner le pictogramme. » pour retirer le marqueur « nécessairement ».
- Bonne réponse A conservée ; justification B de 087 toujours pertinente : « la phrase visible n’est pas l’unique possibilité ». A et C inchangées. R65 avait été vérifiée lors du point 017 ; cette modification porte sur la formulation d’un distracteur, sans changement de portée du corrigé.
- Prompt complet : `../prompts/slide-086-qcm3-v1.txt`. Seule 086 est proposée à la régénération ; 087 est conservée pour ce point.
- Production graphique en cours, aucune intégration pour ce point.

- Proposition `slide-086-qcm3-v1.png` : 1672 x 941 pixels, SHA-256 `1c6635bd7467661def1fc2b052435e1ab6c7a14adf26f7b0c8a625452d94fc7e`. Contrôles visuel et OCR : B conforme à la rédaction approuvée, autres textes et pagination conservés. Correction 087 examinée à la résolution originale, cohérente avec le nouveau distracteur. Validation graphique en attente avant intégration.

- Validation graphique utilisateur : « oui go ». Slide 086 intégrée en local ; correction 087 conservée. Optimisation limitée à 086 sans modification des pixels ; SHA-256 intégré `a0ecd0213539325f426fe048f07f2adfe36fa63ac04e69733165780aa7aba6ad`.
- Texte visible B et transcription synchronisés dans `slides.json` et storyboard. Passe `alt-text` : alternative et description toujours pertinentes, conservées ; notes orales cohérentes, conservées.
- Notes : 132 slides sans erreur ni avertissement. Tests : 20 des scripts et 14 du jeu réussis ; validations HTML et `git diff --check` réussis.
- Deux archives reconstruites sous 100 Mio : couverture exacte de 132 slides sans doublon, PNG et alternatives embarqués identiques aux fichiers courants.
- Bilan cumulé : dix PNG modifiés, 122 identiques à `HEAD`. Seules les entrées 017, 047, 070, 084, 085 et 086 de `slides.json` changent ; accueil et catalogue inchangés. Aucun commit ni push ; pas de nouvelle recette navigateur complète.


## QCM 4 - slides 088/089

- Rédaction validée par l’utilisateur (« ok go ») : C devient « C. R40 est satisfaite : le pourcentage de réduction précise les conditions de l’offre. » ; justification « C écartée : le taux de réduction ne précise pas les produits concernés ni l’éligibilité. » Bonne réponse B conservée.
- Prompts complets : `../prompts/slide-088-qcm4-v1.txt` et `../prompts/slide-089-qcm4-v1.txt`. Tentatives supplémentaires de géométrie 088 documentées dans les prompts v2 et v3.
- Propositions initiales 1672 x 941 : 088 v1 SHA-256 `2b1621a1c582a096695cf84139e0f78fcd6cf65999b813182a23ea691da43e77`, 089 v1 SHA-256 `0ff486dc5202f8bb456b637fc180f9568f42aa728f389dde1a8e28257b4ef61e`.
- 089 v1 : texte contrôlé visuellement et par OCR, justification C conforme, réponse B cohérente.
- 088 v1 et v2 : textes conformes, mais cartes A/B/C de hauteurs inégales ; non retenues comme versions finales à ce stade. Aucun asset publié ni contenu canonique modifié pour ce point.

- 088 v3 : `slide-088-qcm4-v3.png`, 1672 x 941, SHA-256 `c55b608a7dd2dd74f7e3cca3e568896aca4b819dd6d58b1556041eaead62d802`. Textes contrôlés visuellement et par OCR, contenu C conforme. Hauteurs des cartes rapprochées ; l’égalité stricte aux coordonnées demandées n’est pas atteinte. B et C occupent désormais deux lignes dans des cartes de hauteur comparable à A ; aucun indice de couleur ou de graisse ajouté.
- Paire proposée à validation : 088 v3 et 089 v1. Textes, règles, lettres, justifications et pagination cohérents. Validation graphique utilisateur en attente avant intégration.

- Validation graphique utilisateur : « oui go », après signalement explicite du léger écart résiduel de hauteur des cartes. Versions intégrées : 088 v3 et 089 v1.
- Optimisation sans perte des deux seules images, pixels identiques ; SHA-256 intégrés 088 `516224ae2d6378acbc3cc9bc0e9ed2a265dfd0b878908ca76fffe79bcb5cb6e0` et 089 `09aed8ec6beead8eb25ab03737c468e0fe08822f66cb519aaaab822687251ec4`.
- Choix C, justification C, transcription, notes et storyboard synchronisés ; R41 retirée des règles/sources de cette paire. Passe `alt-text` : alternative de 088 conservée, celle de 089 actualisée pour remplacer la référence au sous-total par le taux de réduction.
- Notes : 132 slides sans erreur ni avertissement ; 20 tests des scripts et 14 du jeu réussis, validations HTML et `git diff --check` réussis.
- Archives reconstruites : couverture exacte de 132 images sans doublon, PNG et alternatives embarqués identiques aux fichiers courants, tailles sous 100 Mio.
- Portée cumulée : douze PNG modifiés, 120 identiques à `HEAD` ; seules les entrées 017, 047, 070, 084, 085, 086, 088 et 089 de `slides.json` changent. Accueil et catalogue inchangés. Aucun commit ni push ; pas de nouvelle recette navigateur complète.


## QCM 5 - slides 090/091

- Rédaction validée par l’utilisateur (« oui je valide poursuit »), après explication de la confusion marque/produit : B devient « B. R68 est satisfaite : l’origine française de la marque renseigne la provenance des chaussures. » ; justification « B écartée : l’origine de la marque ne permet pas de déduire celle du produit. » Bonne réponse C conservée.
- Source R68 : MCP en repli local du 3 septembre 2026 après HTTP 403 ; portée confirmée sur la fiche publique https://checklists.opquast.com/fr/qualite-numerique/la-provenance-des-produits-est-indiquee lors de la préparation.
- Prompts complets : `../prompts/slide-090-qcm5-v1.txt` et `../prompts/slide-091-qcm5-v1.txt`.
- Propositions : `slide-090-qcm5-v1.png`, SHA-256 `57c5c522dc44ac3450fefc5b370d0dc0f2c076744b37da4729f42aa9fbcabebb` ; `slide-091-qcm5-v1.png`, SHA-256 `f4ff51a7c51e6893b044f7ac7c634c74c3fe04c1b7f12664cd2f8ad47b65b47b` ; chacune 1672 x 941 pixels.
- Textes, règles, lettres et pagination contrôlés visuellement et par OCR ; nouveau distracteur et justification concordants. Les autres textes sont conservés. L’égalité stricte des hauteurs des cartes de 090 n’est pas atteinte, comme sur la référence ; C reste légèrement plus haute. Cet écart doit être signalé à la validation graphique, sans prétendre à une harmonisation achevée.
- État : propositions en attente de validation graphique ; aucune intégration dans les assets, contenus canoniques ou archives pour ce point.

- Validation graphique utilisateur : « go on avance pour terminer s’il te plait », après signalement de la carte C légèrement plus haute. Paire 090/091 v1 intégrée en local.
- Optimisation limitée aux deux PNG, sans perte de pixels. SHA-256 intégrés : 090 `c40b74d5f945ff260891ae72c692058144897cb97e2f6e8b6f28c373e1e5921d` ; 091 `6c0a7df3727d1c17f2377b7b7e3ed2efe2563bf78c95ebf1a46498d07f82c256`.
- Textes B, justification B, description/transcription, notes et storyboard synchronisés ; R47 retirée des règles/sources de cette paire. Passe `alt-text` : alternatives existantes conservées, toujours fidèles au scénario et au corrigé C.
- Notes : 132 slides sans erreur ni avertissement ; 20 tests des scripts et 14 du jeu réussis, validations HTML et `git diff --check` réussis. Archives reconstruites sous 100 Mio, couverture exacte des 132 slides sans doublon et contenus embarqués identiques aux fichiers courants.
- Bilan cumulé : quatorze PNG modifiés, 118 identiques à `HEAD` ; seules les entrées 017, 047, 070, 084, 085, 086, 088, 089, 090 et 091 de `slides.json` changent. Accueil et catalogue inchangés. Aucun commit ni push ; pas de nouvelle recette navigateur complète.
