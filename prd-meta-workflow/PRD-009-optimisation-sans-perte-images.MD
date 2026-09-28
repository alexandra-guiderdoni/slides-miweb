# PRD-009 : Optimisation sans perte des images de slides

**Statut** : Implémenté localement
**Date** : 2026-09-28
**Auteur** : Alex
**Source** : production du jeu `navigation-opquast-v5`, mesures du 28 septembre 2026 sur ses 40 PNG

---

## Vision

Le quoi : la consigne « optimiser les images avant `build.py` » doit devenir une
commande exécutable et vérifiable, au lieu d'un mot laissé à l'interprétation de
celui qui produit le jeu.

Le pourquoi : la consigne existe déjà à six endroits des documents structurants,
mais aucun ne dit avec quel outil, ni comment prouver que l'opération est bien
sans perte. Une consigne qui ne réduit pas l'incertitude occupe du contexte sans
rien garantir. Pire, l'intuition courante conduit à un résultat négatif : sur ce
lot, la normalisation des dimensions a fait grossir les images.

Le comment : un script porte la règle, les documents pointent vers lui en une
ligne, et le seul raisonnement non évident est écrit à un seul endroit.

## Exemple bout-en-bout (réel)

Le jeu `navigation-opquast-v5` reçoit 40 PNG issus du projet source, dont 38 en
1672 par 941 pixels et 2 en 1600 par 900. L'opérateur applique la consigne
existante, « optimiser les images », en normalisant d'abord les dimensions :

```bash
python3 scripts/optimiser-images.sh navigation-opquast-v5 --dimensions 1600x900
```

Résultat attendu et observé le 28 septembre 2026 :

```text
40 images traitées, 38 redimensionnées
poids avant  : 37,5 Mo
après redimensionnement : 39,1 Mo
après oxipng : 36,2 Mo
empreinte des pixels identique : f02fa5c5c7452de04011b2c8b197785f
```

Le script refuse de se déclarer terminé si l'empreinte SHA-256 des pixels
décodés diffère avant et après recompression.

---

## Contexte

La consigne « Optimiser les images avant `build.py` » figure aujourd'hui dans
six emplacements :

- `AGENTS.md` ligne 80 ;
- `README.md` lignes 51 et 103 ;
- `DEMARCHE-VERSIONS.md` ligne 88 ;
- `GUIDE-REGENERATION-SITES-SLIDES.md` ligne 185 ;
- `matrice-slide-ai/MODE-OPERATOIRE.md` ligne 57.

Les six formulations sont équivalentes et ne nomment ni outil, ni seuil, ni
contrôle. Aucun jeu publié ne documente la méthode employée.

Trois mesures faites le 28 septembre 2026 sur les 40 PNG de la série Navigation
éclairent le sujet.

Le rééchantillonnage fait grossir le PNG. Ramener 38 images de 1672 par 941 à
1600 par 900 avec un filtre Lanczos porte le lot de 37,5 à 39,1 mégaoctets, soit
4,3 pour cent de plus. La cause est connue : l'interpolation transforme des
aplats de couleur uniforme, très compressibles, en dégradés à forte entropie.

La recompression sans perte rend davantage. `oxipng` en `-o max --strip safe`
ramène le lot à 36,2 mégaoctets, soit 7,5 pour cent de moins qu'après
normalisation, et 3,5 pour cent de moins que le lot d'origine. L'opération
préserve les pixels : l'empreinte SHA-256 des données décodées des 40 images
concaténées est identique avant et après.

La quantification en palette rendrait beaucoup plus, mais avec perte. Une
palette adaptative de 256 couleurs réduirait le poids de 35 à 55 pour cent selon
l'image, pour un écart colorimétrique moyen de 0,98 sur 255 et un léger banding
dans les halos dégradés, visible au zoom. Les visuels comptent entre 17 000 et
99 000 couleurs uniques.

## Problème

Un opérateur qui suit la consigne actuelle à la lettre obtient un résultat non
déterministe, et peut aggraver le poids du jeu en croyant l'améliorer.

Trois conséquences concrètes :

- rien ne garantit qu'une optimisation annoncée ait réellement eu lieu ;
- rien ne garantit qu'elle soit sans perte, alors que ces visuels portent du
  texte, où la dégradation est la plus coûteuse ;
- l'ordre naturel des opérations, normaliser puis générer, produit un lot plus
  lourd que le lot d'origine si la recompression est omise.

## Solution

Ajouter `scripts/optimiser-images.sh`, qui porte la règle au lieu de la décrire.

Contrat du script :

- il prend un dossier de jeu et agit seulement sur `<dossier>/assets/slides/` ;
- il recompresse sans perte avec `oxipng -o max --strip safe` ;
- il ne rééchantillonne que si `--dimensions LxH` est passé explicitement ;
- il calcule l'empreinte SHA-256 des pixels décodés avant et après la
  recompression, et sort en erreur si elle change ;
- il affiche le poids avant et après, et le gain ;
- il rappelle, quand la recompression suit un redimensionnement, que
  `build.py` doit être relancé pour reconstruire le ZIP ;
- si `oxipng` est absent, il échoue proprement en donnant la ligne
  d'installation, sans bloquer une génération en cours.

Les six emplacements documentaires passent de « optimiser les images » à un
renvoi d'une ligne vers ce script, sans allonger le texte.

Le raisonnement non évident, celui qui explique pourquoi l'ordre compte, est
écrit dans `GUIDE-REGENERATION-SITES-SLIDES.md` seulement, qui est le manuel
long du dépôt.

## Options évaluées

### Option A (retenue) : un script, six renvois d'une ligne, un seul exposé du pourquoi

**Avantages** :
- la règle devient exécutable et vérifiable, au lieu d'être interprétable ;
- le caractère sans perte est prouvé à chaque exécution, pas supposé ;
- le contexte documentaire n'augmente pas : six lignes remplacées par six
  lignes de même longueur ;
- le raisonnement contre-intuitif est écrit une fois, là où il est cherché.

**Inconvénients** :
- introduit `oxipng` comme dépendance externe non verrouillée, là où les
  validateurs HTML sont épinglés par `package-lock.json` ;
- ajoute un script à maintenir dans `scripts/`.

### Option B : détailler la méthode en prose dans les six documents

**Avantages** :
- aucune dépendance nouvelle ;
- aucun script supplémentaire.

**Inconvénients** :
- multiplie par six un texte qui devra être tenu à jour en six endroits ;
- gonfle le contexte fixe sans rendre la règle vérifiable ;
- laisse l'opérateur libre de déclarer une optimisation qu'il n'a pas faite.

### Option C : intégrer l'optimisation dans `build.py`

**Avantages** :
- impossible d'oublier l'étape ;
- un seul point d'entrée pour produire un jeu.

**Inconvénients** :
- fait dépendre chaque `build.py` de jeu d'un binaire externe, alors que le
  dépôt exige qu'un jeu publié reste autonome ;
- allonge chaque génération de plus d'une minute, y compris quand seules les
  transcriptions changent ;
- mélange génération et préparation des sources, deux responsabilités que le
  dépôt sépare volontairement.

## Décision

Retenir l'option A.

Le problème est une consigne creuse, pas une architecture à revoir. Un script
la rend exécutable, une ligne par document la rend trouvable, et un seul bloc
de texte porte le raisonnement qui ne se devine pas.

L'option C est écartée parce qu'elle contredit l'autonomie des jeux publiés,
exigence déjà portée par `AGENTS.md`. L'option B est écartée parce qu'elle
augmente le contexte fixe sans rien garantir.

La dépendance à `oxipng` est assumée et bornée : le script est facultatif,
n'est appelé par aucune génération, et échoue en nommant la commande
d'installation.

## Plan d'implémentation

1. Écrire `scripts/optimiser-images.sh` conforme au contrat ci-dessus.
2. Vérifier qu'il échoue proprement quand `oxipng` est absent du `PATH`.
3. L'exécuter sur `navigation-opquast-v5` et confirmer qu'il ne change plus
   rien, les images étant déjà optimisées.
4. L'exécuter sur une copie de travail d'un lot non optimisé et confirmer le
   gain annoncé ainsi que l'égalité des empreintes.
5. Remplacer la ligne d'optimisation dans les six emplacements documentaires.
6. Ajouter dans `GUIDE-REGENERATION-SITES-SLIDES.md` le bloc qui explique
   l'ordre des opérations et les trois mesures.
7. Relancer `scripts/validate_variant.sh navigation-opquast-v5`.
8. Mettre à jour `CHANGELOG.MD` et `BACKLOG.MD`, puis committer localement
   sans push.

## Métriques de succès

- `scripts/optimiser-images.sh navigation-opquast-v5` sort en code 0 et
  annonce un gain nul, les images étant déjà recompressées.
- Sur un lot neuf, le script annonce un gain non nul et une empreinte de pixels
  identique avant et après.
- Le script sort en code différent de 0, avec la ligne d'installation, quand
  `oxipng` est absent du `PATH`.
- Le script sort en code différent de 0 si l'empreinte des pixels change.
- `grep -c "Optimiser les images" ` sur les six emplacements ne renvoie plus de
  formulation sans renvoi au script.
- `scripts/validate_variant.sh navigation-opquast-v5` reste en code 0.
- Aucun `build.py` de jeu ne dépend de `oxipng`.

## Changelog

| Date | Auteur | Changement |
|------|--------|------------|
| 2026-09-28 | Alex + Claude | Implémentation locale du PRD |
| 2026-09-28 | Alex + Claude | Création du PRD |
