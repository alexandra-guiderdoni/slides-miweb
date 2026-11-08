# Changelog

## 2026-11-08

- Audit ShipGuard des refontes Formulaires et Identification et contact : 105 PNG inspectés individuellement. Formulaires S33 : alternative courte simplifiée, description et Lecture du visuel corrigées pour nommer l’ordinateur portable. S23 : trois éditions ImageGen rejetées, guillemets non corrigés et image initiale conservée. Les douze repères du grand cas S59 et les storyboards de refonte absents des sources publiées restent à décider dans le run `audit-20261108-1445565860-5fa54243` ; notes, textes visibles, règles, sources et images publiées inchangés.
- Refonte des images de « Formulaires selon Opquast V5 » : les 63 slides deviennent des scènes illustrées avec les personnages de Présentation ; textes affichés, notes du présentateur et liens de règles inchangés, descriptions des images réécrites.
- Refonte des images d’« Identification et contact selon Opquast V5 » : les 42 slides deviennent des scènes illustrées avec les personnages de Présentation ; textes affichés, notes du présentateur et liens de règles inchangés, descriptions des images réécrites.
- Corrections de « Structure et code selon Opquast V5 » après revue ShipGuard : notes orales des slides 6, 20, 21, 30 et 32 sans remarque de relecture et fidèles au livre (date par le code seulement, redirection HTTP distincte du rafraîchissement côté client, exception du menu applicatif dans le corrigé B) ; descriptions des slides 3, 17 et 21 alignées sur les images. Générateur de la matrice : le refus d’une image en double compare le nom porté dans l’archive, plus la seule chaîne du chemin ; test ajouté, rouge avant le correctif.
- Publication de « Structure et code selon Opquast V5 » : 38 slides couvrant les 15 règles Structure et code 231 à 245, en cinq actes après l’introduction (caractères et dates, structure du contenu, garder la main, documents PDF, tableaux), avec quatre checkpoints, cinq distinctions, une évaluation finale en huit questions et un grand cas corrigé. Scènes illustrées avec les personnages de Présentation, au même niveau de qualité. Deux accordéons par slide, sans numéro de règle à l’oral, et liens vers les fiches officielles ; ce jeu devient le dernier inscrit au catalogue.
- « Identification et contact selon Opquast V5 », slide 42 : le lien du glossaire menait à une page introuvable sans connexion ; il pointe désormais vers l’accueil public du site de formation Opquast, comme l’indique la slide.
- « Présentation selon Opquast V5 », suite de la revue ShipGuard : la slide 31 affiche désormais un CSS valide, `@media print {`, `nav { display: none; }`, `}` (image retouchée par ImageGen, décision d’Alex) ; les notes de la correction du grand cas précisent que la petite cible se confirme par un relevé sous 44 × 44 pixels, celles du grand cas qu’un défaut repéré à l’œil se confirme par une mesure. Le README racine liste « Des liens accessibles » et ne cite plus « Comment se construit une règle Opquast ? », retiré du catalogue le 12 octobre.
- Générateur de la matrice : deux slides ne peuvent plus partager une image, une règle ne peut plus être déclarée deux fois dans une slide, et une écriture de page qui échoue ne laisse plus de fichier temporaire. Trois tests ajoutés, rouges avant le correctif. Les jeux déjà publiés gardent leur propre générateur.
- Corrections de « Présentation selon Opquast V5 » après revue ShipGuard : les alternatives courtes des slides 18, 23 et 29 ne portent plus de remarque de contrôle ; la slide 25 explique que « Reliure » s’affiche dans une police de remplacement faute de la police prévue ; la slide 26 suit le contrôle du livre (tout le code CSS et le HTML, y compris tout autre équivalent de text-align: justify) ; la slide 3 parle de cinq angles de lecture, pour ne plus se confondre avec les cinq gestes de la slide 6 ; l’accroche du jeu reprend ses actes.
- Publication de « Présentation selon Opquast V5 » : 40 slides couvrant les 17 règles Présentation 180 à 196, en six actes après l’introduction, avec quatre checkpoints, cinq distinctions, une évaluation finale en huit questions et un grand cas corrigé. Scènes illustrées avec personnages récurrents, au niveau de Sécurité v4. Deux accordéons par slide, description détaillée et discours oral sans numéros de règle, et liens vers les fiches officielles des règles ; ce jeu devient le dernier inscrit au catalogue.

## 2026-11-07

- Corrections de « Identification et contact selon Opquast V5 » après revue ShipGuard : la slide 31 lie aussi la règle 85 qu’elle affiche ; les descriptions et transcriptions des slides 3 à 6, 11, 16, 21, 28, 39 et 42 ne portent plus de remarques de contrôle (points finaux, corrigé visible). `scripts/check_notes_orales_opquast.py` détecte un badge « R. » inclus dans un texte plus long et signale sans planter des `textes_visibles` ou des `regles` mal formés.
- « Identification et contact selon Opquast V5 » : 29 slides publient désormais les liens vers les fiches officielles de leurs règles (badges, corrigés des checkpoints et de l’évaluation, règles connexes, correction du grand cas), dans la présentation et les alternatives.
- `scripts/check_notes_orales_opquast.py` : une slide portant un badge « R. 101 » ou « R. 101 · 106 · 114 » doit déclarer chaque numéro dans `regles`, avec sa fiche dans `sources` ; les paires règle-source sont aussi contrôlées (même longueur, URL correspondant au numéro). Les badges « Règle 216 » des séries antérieures ne sont pas concernés.
- Publication de « Identification et contact selon Opquast V5 » : 42 slides couvrant les 17 règles Identification et contact 99 à 115, en cinq actes après l’introduction, avec quatre checkpoints, une évaluation finale en huit questions et un grand cas corrigé. Deux accordéons par slide, description détaillée et discours oral sans numéros de règle ; ce jeu devient le dernier inscrit au catalogue.
- Corrections de « Formulaires selon Opquast V5 » après revue ShipGuard : chaque slide liée à des règles publie désormais les liens vers leurs fiches officielles Opquast, dans la présentation et les alternatives ; les liens de téléchargement indiquent le format et le poids de l’archive (ZIP, 64 Mo), y compris dans le pied de page de l’accueil. Slide 23 retouchée : l’exemple affiche `autocomplete="tel"` avec deux guillemets droits. Titres des slides 36 et 49 au tiret simple, messages à retenir propres à chaque partie de l’évaluation finale, chapô des alternatives sans répétition du titre. L’entrée du 6 novembre est rectifiée : trois checkpoints, et des accordéons description détaillée et discours oral.
- Générateur de la matrice : contrôle de l’appariement des règles et de leurs sources, validation des valeurs de `variant.json`, suppression des archives obsolètes, écriture atomique des pages, erreurs de données signalées sans trace Python, sources en sous-dossier listées dans le README du jeu, liens nus suivis d’une parenthèse correctement délimités, et tests de fraîcheur des pages publiées et de cohérence entre textes visibles et transcription. Les jeux déjà publiés gardent leur propre générateur.

## 2026-11-06

- Publication de « Formulaires selon Opquast V5 » : 63 slides couvrant les 30 règles Formulaires 69 à 98, en six actes, avec trois checkpoints, une évaluation finale en seize questions et un grand cas corrigé. Deux accordéons par slide, description détaillée et discours oral, relus de façon croisée ; ce jeu devient le dernier inscrit au catalogue.

## 2026-10-04

- Publication de « Liens et PDF selon Opquast V5 » : 20 slides, dont 9 annexes, avec transcription descriptive et discours oral par slide.
- Publication de « Octobre, Web et accessibilité » : 5 slides avec deux accordéons par slide ; ce jeu devient le dernier inscrit au catalogue.
- Déplacement des tuiles « Liens et PDF » et « Octobre » avant les jeux IGPDE sur l'accueil, sans changer le catalogue ni les liens du dernier jeu.

## 2026-09-28

- Publication de `navigation-opquast-v5` sur l'accueil racine : dix-neuvième entrée du catalogue, README racine mis à jour.
- Ajout du jeu `navigation-opquast-v5` : 40 visuels, règles Opquast 153 à 171.
- Correction locale des dimensions intrinsèques des images : `build.py` lit l'en-tête PNG au lieu d'annoncer 1672 par 941 en dur, et le test de contrat compare les dimensions déclarées aux fichiers réels.
- Correction locale de la linkification des adresses HTTPS : l'hôte doit commencer par un caractère alphanumérique, une adresse tronquée ne produit plus de `href` invalide.
- Implémentation locale du `PRD-009` : optimisation sans perte des images de slides.
- Création du `PRD-009` sur l'optimisation sans perte des images de slides.

## 2026-07-01

- Alignement documentaire local : `PRD-001` à `PRD-008` marqués selon leur état d'implémentation locale.
- Implémentation locale du `PRD-008` : fallback Markdown visuel compatible avec le rapport francisé.
- Création du `PRD-008` sur le fallback Markdown du rapport visuel francisé.
- Correction locale de `SG-Z4-005` : les README générés listent seulement les fichiers réellement présents dans `source/`.
- Implémentation locale du `PRD-007` : nettoyage de `slides=all` à la sortie du mode toutes slides.
- Création du `PRD-007` sur le nettoyage du paramètre `slides=all` à la sortie du mode toutes slides.

## 2026-06-30

- Implémentation locale du `PRD-006` : ZIPs déterministes et liens de téléchargement vérifiés.
- Création du `PRD-006` sur les ZIPs déterministes et les liens de téléchargement.
- Implémentation locale du `PRD-005` : typage strict de `slides.json`.
- Précision du `PRD-005` sur le contrat d'erreur `slides.json` pour `numero`.
- Création du `PRD-005` sur le typage strict de `slides.json`.
- Implémentation locale du `PRD-004` : confinement des images `slides.json` sous `assets/slides/`.
- Création du `PRD-004` sur le confinement des images déclarées dans `slides.json`.
- Implémentation locale du `PRD-003` : validation HTML par dépendances npm racine verrouillées.
- Création du `PRD-003` sur la validation npm verrouillée des variantes.
- Création du `PRD-002` sur la publication centralisée de l'accueil racine.
- Précision du `PRD-001` avec le contrat d'implémentation du garde de fraîcheur des artefacts générés.
- Création du `PRD-001` sur le garde de publication des artefacts générés avant mise à jour de l'accueil racine.
