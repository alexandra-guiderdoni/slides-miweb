# Édition web Opquast Miweb

La version web reprend les 44 slides du PowerPoint `opquast-presentation-miweb-2026.pptx`, dans le même ordre. Les images sont conservées. Leur optimisation PNG est sans perte, avec comparaison des dimensions et de tous les pixels RGBA.

`slides.json` est la source de génération des pages et du Markdown téléchargé. Chaque slide comporte une alternative courte, une description du visuel, une transcription structurée, un relevé des textes visibles, un message et le discours oral extrait des notes du PPTX.

Les textes visibles ont été relus sur les 44 images. Ils conservent les chiffres et les formulations du visuel, avec normalisation des sauts de ligne et de la typographie des apostrophes. Les descriptions expliquent les relations représentées. Les discours sont distincts de ces transcriptions.

## Structuration des transcriptions

À la demande de l’utilisateur, les 44 transcriptions sont organisées par idées, avec des sous-titres et, si nécessaire, un second niveau de titres. Les correspondances simples réunissent le libellé et sa valeur sur une même ligne : « Liens : 17 », « V : Visibilité ». Seule la comparaison à trois colonnes de la slide 26 conserve un tableau. Les étapes restent dans leur ordre. Les mots qui forment une même idée sont réunis en phrases, notamment pour les responsabilités, les modalités de formation et les consignes d’examen.

Le champ `transcription` porte cette structure dans `slides.json`. Le relevé `textes_visibles` est conservé pour la traçabilité ; il n’est plus affiché comme une longue liste de mots isolés. Les mêmes regroupements sont rendus sous chaque slide, dans la page des transcriptions et dans le Markdown du ZIP. Les notes orales conservent leur formulation et restent dans un bloc distinct.

Tous les tirets cadratins des textes du jeu sont remplacés par des tirets simples, y compris dans les copies des storyboards publiées. Les notes orales n’en contenaient aucun. Les documents de préparation originaux et le PowerPoint restent conservés dans le dossier de travail Opquast, hors du dépôt publié.

## Correction demandée sur le tarif

La slide 44 reste inchangée et affiche **450 euros HT**. Le discours oral et le message de la version web indiquent **485 € HT**, tarif vérifié sur la [page officielle de la certification](https://www.opquast.com/certification/) le 8 septembre 2026. Une précision explicite signale l’écart entre le visuel et le tarif corrigé.

Les notes du PPTX sont conservées hors correction du tarif. Le discours original de la slide 44 reste conservé dans [le document de préparation](storyboard.md#slide-44). Aucune actualisation générale des images ni des modalités de certification n’a été demandée.

## Précisions issues de la relecture

La slide 39 conserve les notes avec l’ancien intitulé de certification. Une précision indique l’intitulé actuel, « Mobiliser un Référentiel Qualité Numérique », présenté sur la [page officielle de la certification](https://www.opquast.com/certification/).

Pour la slide 42, la [FAQ officielle](https://www.opquast.com/a-propos/faq/) annonce 120 questions tandis que la [page officielle destinée aux écoles](https://www.opquast.com/metiers/ecoles-et-centres-de-formation/) en annonce 125, lors de la vérification du 8 septembre 2026. Les deux sources indiquent 1 h 30. Le visuel et ses notes restent conservés ; la précision expose cette divergence et renvoie aux consignes de la session. Le nombre exact de questions n’est donc pas présenté comme vérifié.

Les précisions des slides 39, 42 et 44 sont visibles sous l’image, même lorsque les accordéons sont fermés. Les citations et les fragments de code des discours sont mis en forme sans modifier les notes sources. Le pied de page donne accès à la page « Accessibilité : non auditée ».

## Complément du discours de la slide 15

À la demande de l’utilisateur, dix autres formules mnémotechniques ont été ajoutées après les notes originales de la slide 15. Les formulations fournies sont conservées telles quelles, de « Emphatique » à « Philosophe ». Le visuel et sa transcription restent inchangés.

## Traçabilité

- [Provenance et empreintes](provenance.json) : correspondances entre l’ordre du PPTX, les images sources et les PNG publiés.
- [Consignes et notes originales](storyboard.md) : les 44 entrées de préparation.
- `origines/` : les six storyboards sources et leurs exports de prompts disponibles.

Les exports signalent que les appels complets au générateur d’images n’ont pas été retrouvés. Les storyboards sont des consignes conservées, sans attestation des prompts exacts exécutés.

## Génération et contrôles

Le jeu est créé depuis `matrice-slide-ai/create_variant.py`. Son générateur autonome ajoute le discours oral, les précisions sourcées et les transcriptions structurées au modèle existant. L’accueil racine est géré séparément par `matrice-slide-ai/publish_variant.py`.

Les pages HTML, `alternatives.md`, le README du jeu et le ZIP se régénèrent avec `python3 opquast-miweb/build.py`. Les contrôles standard passent par `scripts/validate_variant.sh opquast-miweb` depuis la racine du dépôt.

Le statut d’accessibilité reste « non audité ». Les contrôles techniques et l’inspection locale ne constituent pas un audit RGAA complet.

## PDG pass

Contrôle ciblé des sorties générées et de la conservation des sources : `PDG self-check, not independent review`. Les générateurs de la matrice, le générateur du jeu et ses tests ont été inspectés. Les ajouts au modèle portent sur les discours, la précision tarifaire et les transcriptions structurées ; le code de navigation et les anciennes variantes sont conservés.

| Vérification | Preuve | Résultat |
| --- | --- | --- |
| Couverture | `slides.json`, `source/provenance.json`, comparaison au PPTX | 44 images dans l’ordre, 44 transcriptions et 44 discours. |
| Fidélité | Comparaison de tous les pixels RGBA et empreintes des notes | Images identiques ; notes originales conservées avec les deux adaptations demandées aux slides 15 et 44. |
| Régression | `scripts/validate_variant.sh opquast-miweb` | 19 tests réussis ; HTML validé par html-validate et vnu. |
| Structure | Tests des transcriptions et contrôle des exports | En-têtes de tableaux associés aux données, titres imbriqués sans dépasser le niveau 6, Markdown du ZIP conforme au rendu courant. |
| Parcours local | `/opquast-miweb/`, `#slide-15`, `#slide-44`, `?slides=all#diaporama` | Navigation par bouton et flèche clavier, accordéons et dix formules de la slide 15 observés dans Chrome. |
| Fichiers publiables | Lecture indépendante des quatre pages, du ZIP et de `slides.json` | Liens et ancres locaux valides, identifiants uniques, un titre h1 par page ; 44 PNG et Markdown du ZIP identiques aux fichiers courants. |
| Écran étroit | Chrome, largeur utile observée de 323 pixels | Tableau de la slide 26 lisible sans débordement horizontal ; transcription de la slide 16 également contrôlée à 250 pixels. |

Une recompression sans perte des PNG a été détectée après un premier build. Les empreintes et le ZIP ont été régénérés ; le test de provenance vérifie désormais les fichiers et les notes.

NOT VERIFIED: une activation du plein écran a été observée, mais elle n’est pas reproductible de manière fiable dans le navigateur automatisé ; la projection complète reste à contrôler manuellement. Le geste tactile sur appareil physique et l’audit RGAA complet n’ont pas été exécutés. Cette recette locale ne constitue pas une preuve du déploiement distant. Les indications de la slide 41 proviennent du support et n’ont pas été confirmées indépendamment dans une source publique actuelle.

## Vérification du rendu des transcriptions et des discours

Recette du 8 septembre 2026, selon le skill `verifier-etat`. Source de vérité : `slides.json`, HTML et Markdown générés, contenu extrait du ZIP et état du navigateur.

| Déclencheur | Traitement | Résultat attendu | Source de vérité | Preuve observable |
| --- | --- | --- | --- | --- |
| Génération du jeu | Rendu des rubriques et des notes | 44 transcriptions et 44 discours distincts | HTML, Markdown et ZIP | Lecture séparée des fichiers et comparaison du Markdown archivé. |
| Citation et code dans des notes synthétiques | Échappement puis mise en forme | Citation HTML et code lisibles, texte source conservé | HTML temporaire puis lecture séparée | `> Citation de recette` devient une citation ; `label` devient un élément code. |
| Précision avec deux sources | Rendu avant les accordéons | Une seule précision visible, deux liens | HTML de la slide 42 et Markdown | Contrôle de position et présence des deux URL officielles. |

Les cas limites ont été exécutés sur des copies synthétiques, puis leurs résultats ont été relus séparément. Aucune donnée de production n’a été modifiée pour ces essais.

| Cas | Avant | Après observé | Verdict |
| --- | --- | --- | --- |
| Notes vides | Copie valide, puis chaîne vide | Rejet : `notes_orateur` doit être une chaîne non vide. | OK |
| Transcription vide | Copie valide, puis liste vide | Rejet : la transcription exige des rubriques. | OK |
| Source complémentaire non HTTPS | Copie valide, puis URL `javascript:` | Rejet : la source complémentaire doit utiliser HTTPS. | OK |
| Code contenant une balise script | Notes synthétiques contenant `<script>alert(1)</script>` | Balises échappées dans le code affiché ; aucune balise script injectée. | OK |

Corrections : regroupements des correspondances, précision sortie des accordéons, prise en charge des citations et fragments de code. Les 19 tests de régression et les validateurs HTML passent après ces changements. `/simplify` est indisponible et n’a pas été exécuté.

Verdict : **VALIDÉ pour le rendu des transcriptions, des discours et des exports**, dans le périmètre décrit. Les réserves de projection, de contrôle tactile et de vérification métier restent celles indiquées ci-dessus.

## Revue des alternatives courtes

Les 44 images ont été revues visuellement dans leur ordre, avec leur titre, leur description et leur transcription adjacente. Ce sont des visuels informatifs complexes, conservés comme images à la demande de l’utilisateur. Chaque alternative courte est gardée et complétée par la description détaillée existante ; la plus longue compte 65 caractères. Les données et les textes complets restent dans la transcription. L’image et sa légende utilisent `figure` et `figcaption`.

| Slide | Rôle | Alternative gardée | Note |
| --- | --- | --- | --- |
| 1 | Informatif complexe | Vérifier la qualité, de la recherche à l’action. | Parcours détaillé adjacent. |
| 2 | Informatif complexe | Le référentiel évolue de 240 à 245 règles. | Valeurs transcrites. |
| 3 | Informatif complexe | Les défauts passent entre les périmètres métiers. | Relations décrites. |
| 4 | Informatif complexe | Les contrôles métiers laissent des besoins sans réponse. | Besoins détaillés. |
| 5 | Informatif complexe | Un référentiel partagé complète les contrôles existants. | Périmètre explicité. |
| 6 | Informatif complexe | E-commerce et formulaires regroupent le plus de règles affichées. | Rubriques et volumes associés. |
| 7 | Informatif complexe | Une lecture de travail relie cinq domaines aux règles. | Domaines et valeurs associés. |
| 8 | Informatif complexe | Une règle peut servir plusieurs dimensions. | Dimensions et volumes associés. |
| 9 | Informatif complexe | La qualité se construit à plusieurs étapes du projet. | Étapes et volumes associés. |
| 10 | Informatif complexe | La livraison peut s’éloigner du besoin du client. | Scènes décrites. |
| 11 | Informatif complexe | Un besoin se transforme au passage entre les métiers. | Scènes décrites. |
| 12 | Informatif complexe | Chaque étape participe à la qualité du résultat. | Étapes transcrites. |
| 13 | Informatif complexe | Cinq attentes jalonnent le parcours utilisateur. | Attentes et lettres associées. |
| 14 | Informatif complexe | VPTCS suit le parcours, de la visibilité aux services. | Dimensions ordonnées. |
| 15 | Informatif complexe | « Va Pas Te Croire Supérieur » aide à retenir VPTCS. | Lettres et mots associés. |
| 16 | Informatif complexe | L’interface contribue à une expérience plus large. | UI et UX explicitées. |
| 17 | Informatif complexe | L’UX couvre l’avant, l’usage et l’après du service. | Parcours hiérarchisé. |
| 18 | Informatif complexe | Classer les attentes permet de vérifier les exigences. | Modèle décrit. |
| 19 | Informatif complexe | VPTCS relie les dimensions aux compétences nécessaires. | Métiers associés. |
| 20 | Informatif complexe | Un langage partagé facilite le travail entre métiers. | Relations décrites. |
| 21 | Informatif complexe | Les cinq dimensions mobilisent des métiers différents. | Compétences regroupées par dimension. |
| 22 | Informatif complexe | Comprendre, organiser, mesurer et prédire pour décider. | Actions transcrites. |
| 23 | Informatif complexe | Les contenus et les services portent la valeur du site. | Relations décrites. |
| 24 | Informatif complexe | Deux circuits internes doivent rendre un seul service. | Circuits décrits. |
| 25 | Informatif complexe | Les dimensions convergent vers une expérience unique. | Dimensions associées. |
| 26 | Informatif complexe | Communication et informatique découpent le projet. | Tableau à trois colonnes. |
| 27 | Informatif complexe | Cinq domaines contribuent ensemble à la qualité du service. | Domaines détaillés. |
| 28 | Informatif complexe | VPTCS aide à analyser les forces et les limites d’un site. | Dimensions et critères détaillés. |
| 29 | Informatif complexe | Les exigences suivent aussi un parcours de service physique. | Étapes et lieux associés. |
| 30 | Informatif complexe | Énoncé, objectif, solution et vérification sont distincts. | Quatre éléments détaillés. |
| 31 | Informatif complexe | Une difficulté réelle devient un contrôle utile. | Étapes détaillées. |
| 32 | Informatif complexe | Une règle unitaire permet un verdict clair. | Question et verdict explicités. |
| 33 | Informatif complexe | Une règle compréhensible s’applique à plusieurs contextes. | Trois qualités et explications regroupées. |
| 34 | Informatif complexe | La discussion et la documentation éprouvent une règle. | Conditions transcrites. |
| 35 | Informatif complexe | Cinq questions évaluent l’acceptabilité d’une règle. | Questions transcrites. |
| 36 | Informatif complexe | La discussion améliore la précision d’une règle. | Processus décrit. |
| 37 | Informatif complexe | Chaque champ doit être relié à sa propre étiquette. | Règle et exemple détaillés. |
| 38 | Informatif complexe | Le parcours clavier doit conserver un focus visible. | Règle et exemple détaillés. |
| 39 | Informatif complexe | La certification porte sur les personnes et leur maîtrise. | Intitulé actuel précisé séparément. |
| 40 | Informatif complexe | La formation présentée se suit en ligne à son rythme. | Modalités du support transcrites. |
| 41 | Informatif complexe | Trois seuils conditionnent l’accès à l’examen présenté. | Seuils du support transcrits. |
| 42 | Informatif complexe | Le support présente les conditions matérielles de l’examen. | Divergence des sources signalée sous l’image. |
| 43 | Informatif complexe | Le score rend visible la progression des compétences. | Seuil et niveaux transcrits. |
| 44 | Informatif complexe | Le support chiffre le temps et le coût de la formation. | Tarif actuel précisé séparément. |

PDG-LARGE-FILE-JUSTIFICATION: `slides.json` réunit les 44 entrées exigées par le générateur canonique, avec leurs discours ; le format JSON reste sans commentaire. Les exports complets et le générateur autonome suivent le contrat existant du dépôt.

PDG-BINARY-ASSET-JUSTIFICATION: les 44 PNG sont les visuels du support sélectionné. Le ZIP duplique ces images pour le téléchargement hors ligne prévu par le dépôt et inclut les transcriptions ainsi que le discours oral. Le PPTX n’est pas dupliqué dans le site.
