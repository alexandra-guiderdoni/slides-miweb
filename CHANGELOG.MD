# Changelog

## 2026-11-08

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
