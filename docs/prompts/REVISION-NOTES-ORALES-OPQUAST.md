# Prompt canonique - Révision des notes orales Opquast

Utiliser ce prompt pour créer ou réviser le discours oral d’une série de slides consacrée au référentiel Opquast.

Le travail commence par des slides étalons. La rédaction complète et la délégation en parallèle ne commencent qu’après leur validation explicite.

## Variables à fournir

- `<dossier-jeu>` : dossier autonome contenant `slides.json`.
- `<storyboard>` : storyboard ou trame source.
- `<sources-editoriales>` : notes, notebook ou documents de langage disponibles.
- `<sources-opquast>` : skill ou serveur MCP Opquast accessible.
- `<nombre-slides>` : nombre total de slides.
- `<contraintes-particulieres>` : limites propres à la série.

## Hiérarchie des sources

Appliquer cet ordre d’autorité :

1. Le skill ou le MCP Opquast valide les numéros, les libellés, les objectifs, les contrôles et les limites des règles.
2. La transcription décrit ce qui est réellement affiché sur chaque slide.
3. Le storyboard organise la progression générale et le rôle de chaque slide.
4. Les notes existantes constituent la matière éditoriale à conserver.
5. Les productions NotebookLM ou équivalentes servent à challenger le contenu, jamais à valider seules une affirmation.

En cas de contradiction :

- arrêter la rédaction du passage concerné ;
- identifier précisément les sources en conflit ;
- corriger avec la source la plus autoritative ;
- écrire « à vérifier » si l’arbitrage reste impossible ;
- ne jamais combler un manque par une invention plausible.

## Mission

Réviser les notes orales de `<nombre-slides>` slides à partir de `<dossier-jeu>/slides.json`, du storyboard et des sources fournies.

Produire un discours :

- directement prononçable ;
- dense mais naturel ;
- structuré par le contenu ;
- facile à parcourir grâce aux listes à puces ;
- complémentaire de la transcription ;
- fidèle aux sources et au périmètre Opquast.

## Contrat éditorial

### Ce que les notes doivent faire

- Expliquer le risque utilisateur, la portée de la règle et ses limites utiles.
- Relier les idées sans réciter les numéros de règles.
- Employer des titres qui nomment le contenu réel.
- Utiliser des phrases complètes et directement prononçables.
- Employer généralement 4 à 8 puces quand cette structure améliore le scan.
- Conserver une transition courte vers l’idée suivante.
- Limiter les rapprochements avec le RGAA aux points directement utiles.
- Utiliser uniquement le tiret simple `-`.

### Ce que les notes ne doivent pas faire

- Répéter ou paraphraser la transcription.
- Décrire un objectif pédagogique.
- Donner une consigne au présentateur.
- Organiser la prise de parole du groupe.
- Commenter la fabrication du support, la slide ou le déroulé du module.
- Inventer un exemple, un préjudice, une garantie, un chiffre ou une conformité.
- Transformer un rapprochement RGAA en équivalence automatique.
- Ajouter un développement absent des sources sous prétexte qu’il est pertinent.

### Titres interdits

- `Intention pédagogique`
- `Animation`
- `Mise en perspective`
- `Développement oral`
- `Synthèse orale`
- `Objectif pédagogique`

## Slides étalons obligatoires

Avant de traiter toute la série, sélectionner et réviser :

- une ouverture de partie ;
- une slide de règle ;
- une slide d’éclairage ;
- une synthèse.

Présenter ces quatre slides à validation. Ne pas généraliser le style et ne pas déléguer la rédaction complète avant leur approbation explicite.

Après validation, considérer ces quatre résultats comme le patron éditorial de la série.

## Gabarits

### Slide de règle

```markdown
### Titre portant sur la situation ou le problème

- Contexte utile.
- Explication nécessaire.
- Limite éventuelle.

#### Impact du non-respect

- Préjudice concret.
- Conséquence dans le parcours.

#### Ce que garantit la règle

- Protection ou capacité réellement apportée.
- Limite exacte de cette garantie.

### Transition

Phrase courte vers l’idée suivante.
```

### Slide d’ouverture ou d’éclairage

```markdown
### Titre portant sur l’idée centrale

- Première idée utile.
- Deuxième idée utile.
- Nuance ou limite.
- Conséquence pour l’utilisateur.

### Transition

Phrase courte vers l’idée suivante.
```

### Slide de synthèse

```markdown
### Titre portant sur la relation entre les idées

- Premier enseignement.
- Deuxième enseignement.
- Condition qui relie les règles.
- Capacité finale obtenue par l’utilisateur.

### Transition

Phrase courte vers la partie suivante.
```

Pour la dernière slide, remplacer la transition par une conclusion.

## Organisation multi-agent

Après validation des quatre slides étalons :

1. Un agent vérifie les règles Opquast et signale toute affirmation non validée.
2. Les agents rédacteurs reçoivent des plages distinctes de slides et le même patron éditorial.
3. Aucun agent ne valide seul sa propre production.
4. Une relecture croisée contrôle la fidélité, la métapédagogie et la lisibilité.
5. L’agent principal réconcilie les contributions dans une version unique.
6. Une dernière lecture vérifie les slides comme un seul discours continu.

Chaque sous-mission doit rappeler :

- le périmètre exact de slides ;
- les champs autorisés à changer ;
- les sources disponibles ;
- les invariants éditoriaux ;
- l’interdiction de toucher aux autres champs de `slides.json`.

## Contrôles avant génération

Lancer :

```bash
python3 scripts/check_notes_orales_opquast.py <dossier-jeu>
```

Le contrôle automatique vérifie la structure et les interdits détectables. Il ne remplace pas :

- la validation factuelle auprès du skill ou du MCP Opquast ;
- la comparaison sémantique entre transcription et discours oral ;
- la recherche de redites entre slides ;
- la lecture de la progression globale ;
- la validation humaine des quatre slides étalons.

## Contrôles après génération

Après mise à jour de `slides.json` :

```bash
python3 <dossier-jeu>/build.py
scripts/validate_variant.sh <dossier-jeu>
python3 -m unittest discover -s scripts/tests
```

Inspecter ensuite dans le navigateur :

- le rendu des listes à puces ;
- la hiérarchie des titres ;
- la distinction entre transcription et discours oral ;
- l’affichage des accordéons sur plusieurs slides représentatives ;
- la continuité de lecture de la première à la dernière slide.

## Restitution attendue

Terminer par un bilan court indiquant :

- les slides révisées ;
- les corrections factuelles apportées ;
- les points laissés « à vérifier » ;
- les contrôles effectués ;
- les fichiers modifiés ;
- ce qui n’a pas été modifié ;
- l’absence de commit, de push ou de publication sans demande explicite.
