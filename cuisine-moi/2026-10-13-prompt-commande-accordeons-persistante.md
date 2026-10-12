Prompt LLM - commande persistante des accordéons
================================================

Tu travailles dans le dépôt :

`/Users/alex/Claude/projets-heberges/slides-miweb`

La série concernée est :

`projets-livrables-opquast-v5`

## Mission

Ajouter à chaque slide une commande accessible placée juste avant ses deux accordéons. Cette commande ouvre ou ferme ensemble la description détaillée et le discours oral.

En mode diaporama, l’état choisi doit persister pendant la navigation de slide en slide. Il doit être réinitialisé au rechargement de la page. En mode « Afficher toutes les slides », chaque commande doit agir uniquement sur les deux accordéons de sa propre slide.

## Verrou de périmètre

Pour cette exécution :

- MUST modifier uniquement `projets-livrables-opquast-v5` ;
- MUST préserver tous les contenus des slides et les comportements de navigation existants ;
- MUST traiter `build.py` comme source de vérité et régénérer les sorties ;
- MUST NOT modifier manuellement `index.html` sans modifier le générateur correspondant ;
- MUST NOT modifier la matrice, une autre série, le catalogue racine ou la publication distante ;
- MUST NOT commiter, pousser ou déployer sans une demande explicite ultérieure ;
- MUST préserver les modifications utilisateur déjà présentes dans l’arbre Git ;
- MUST limiter le changement à cette fonctionnalité et à ses tests.

La généralisation à la matrice des futurs jeux de slides constitue une phase 2 soumise à validation humaine. La rétroaction sur les autres séries constitue une phase 3 distincte, également soumise à validation humaine.

## Sources à inspecter avant toute modification

Lire au minimum :

- `projets-livrables-opquast-v5/build.py` ;
- `projets-livrables-opquast-v5/tests/test_site_contracts.py` ;
- le `index.html` généré pour vérifier le DOM réel ;
- l’état Git du dépôt pour ne pas écraser les changements existants.

Référence fonctionnelle :

`https://dsfr-accordeons-demo-20260722.alexandra-guiderdoni.chatgpt.site`

Réutiliser le générateur, les accordéons DSFR et le mécanisme de navigation existants. MUST NOT créer un second moteur de diaporama ni un système de persistance externe.

## Interface attendue

Pour chacune des 45 slides :

1. Ajouter un bouton natif `<button type="button">` juste avant le groupe des deux accordéons.
   Il doit rester hors de `.fr-accordions-group`, utiliser une classe de bouton DSFR ordinaire telle que `fr-btn` et MUST NOT utiliser `.fr-accordion__btn`.
2. Son libellé visible initial est `Tout ouvrir`.
3. Lorsque les deux accordéons qu’il contrôle sont ouverts, son libellé visible devient `Tout fermer`.
4. Lorsqu’au moins un des deux accordéons est fermé, son libellé visible est `Tout ouvrir`.
5. La commande doit rester utilisable avec `Entrée` et `Espace`, sans gestion clavier personnalisée inutile.
6. Le focus doit rester sur la commande après son activation.
7. Le style doit utiliser les classes DSFR déjà chargées et ne provoquer aucun débordement à 390 px de largeur.

## Contrat d’accessibilité de la commande

Chaque commande :

- MUST posséder un `aria-controls` contenant exactement les deux identifiants des panneaux voisins ;
- MUST exposer `aria-expanded="true"` uniquement lorsque les deux panneaux sont ouverts ;
- MUST exposer `aria-expanded="false"` dans les états fermé ou mixte ;
- MUST mettre à jour simultanément le libellé visible, le nom accessible et `aria-expanded` ;
- MUST conserver le libellé visible dans le nom accessible, conformément au principe « label visible inclus dans le nom » ;
- MUST utiliser un nom accessible enrichi composé d’un `<span>` visible (`Tout ouvrir` ou `Tout fermer`) suivi d’un `<span class="fr-sr-only">, description et discours oral de la slide 12</span>` ; MUST NOT utiliser `aria-label` ou `title` pour ce nom afin d’éviter une double synchronisation ;
- MUST référencer des identifiants existants et uniques ;
- MUST NOT ajouter de rôle `button` à un bouton natif ;
- MUST NOT déplacer le focus ni annoncer deux fois le changement d’état ;
- MUST préserver le focus visible fourni par le DSFR.

Utiliser en priorité l’API publique de collapse du DSFR pour ouvrir et fermer les panneaux. `window.dsfr` n’existe pas encore quand le script inline s’exécute et `dsfr(panneau)` peut renvoyer `null` tant que l’instance n’est pas créée : garder chaque accès avec `const proxy = window.dsfr && window.dsfr(panneau); const collapse = proxy && proxy.collapse;`.

Avant la disponibilité de l’API, appliquer le repli initial sans clic simulé : poser `aria-expanded` sur les boutons d’accordéon et `fr-collapse--expanded` sur les panneaux. Le DSFR doit reprendre cet état lors de son initialisation. Au chargement, le mode fermé ne déclenche aucune mutation puisque le HTML est déjà fermé. MUST NOT maintenir durablement deux états concurrents.

Le DSFR applique l’état au rendu suivant. Les événements `dsfr.disclose` et `dsfr.conceal`, émis sur `.fr-collapse`, précèdent la mise à jour de `aria-expanded`. Recalculer le libellé, le nom accessible et `aria-expanded` de la commande dans un écouteur de ces événements différé par `requestAnimationFrame`, en lisant l’état effectif des deux boutons d’accordéon. MUST NOT lire cet état juste après l’appel à l’API ni depuis l’écouteur de clic.

La conformité demandée porte sur les deux états de cette nouvelle commande et sur sa relation avec les panneaux. MUST NOT déclarer le site globalement conforme RGAA sur cette seule base.

## Machine d’état attendue

### Chargement et rechargement

- État initial : les deux accordéons sont fermés et la commande affiche `Tout ouvrir`.
- La persistance reste exclusivement en mémoire JavaScript.
- MUST NOT utiliser `localStorage`, `sessionStorage`, cookie ou paramètre d’URL.
- Après rechargement, le mode persistant revient à fermé.

### Mode diaporama

- Activer `Tout ouvrir` ouvre les deux accordéons de la slide active et active le mode persistant ouvert.
- Toute navigation vers une autre slide ouvre alors ses deux accordéons.
- Activer `Tout fermer` ferme les deux accordéons de la slide active et remet le mode persistant à fermé.
- Une action manuelle sur l’un des deux accordéons annule le mode persistant, sans forcer immédiatement l’autre accordéon à changer d’état. Seul un événement `click` reçu par un `.fr-accordion__btn` réalise cette annulation ; les événements DSFR déclenchés par la commande ou la navigation ne l’annulent jamais.
- Après cette annulation, la slide courante peut rester dans un état mixte ; la slide suivante doit afficher ses deux accordéons fermés.
- À chaque affichage d’une slide, après `applyVisibility()`, appliquer symétriquement le mode persistant : le mode ouvert ouvre ses deux panneaux et le mode fermé les ferme. L’état manuel d’une slide ne survit donc pas à la navigation.
- Toutes les voies de navigation intra-page doivent appliquer la même règle : boutons, flèches du clavier, `Home`, `End`, sommaire, historique du navigateur et commandes de projection.
- Le chargement direct d’une URL comportant un fragment de slide constitue un nouveau chargement : il doit donc repartir avec les deux accordéons fermés.

### Mode « Afficher toutes les slides »

- Entrer dans ce mode annule immédiatement le mode persistant.
- Les 45 commandes sont visibles.
- Chaque commande agit uniquement sur les deux accordéons de sa slide.
- Les commandes ne sont pas synchronisées entre les slides.
- Ouvrir les accordéons d’une slide ne doit modifier aucun accordéon d’une autre slide.
- À l’entrée du mode, resynchroniser chaque commande locale depuis l’état effectif de ses deux panneaux sans modifier ces panneaux ; résoudre les panneaux depuis `aria-controls` de la commande, jamais depuis `currentIndex`.
- Revenir au mode diaporama repart avec le mode persistant fermé ; la slide active affiche alors ses deux accordéons fermés.

## Synchronisation avec les actions individuelles

Après toute activation d’un bouton d’accordéon individuel :

- laisser le `click` annuler la persistance en mode diaporama, puis attendre l’événement DSFR correspondant et un `requestAnimationFrame` avant de recalculer l’état de la commande locale ;
- si les deux panneaux sont ouverts, afficher `Tout fermer` et exposer `aria-expanded="true"` ;
- sinon, afficher `Tout ouvrir` et exposer `aria-expanded="false"` ;
- en mode diaporama, annuler la persistance uniquement depuis le `click` individuel, jamais depuis les événements DSFR ;
- en mode « Afficher toutes les slides », ne modifier aucune autre slide.

## Implémentation minimale attendue

- Étendre `render_slide()` pour générer la commande et ses relations ARIA.
- Étendre le JavaScript existant dans `MAIN_JS` plutôt que créer un nouveau script ou un nouvel état global parallèle.
- Centraliser l’ouverture, la fermeture et la synchronisation dans de petites fonctions nommées par responsabilité.
- Brancher l’application de la persistance dans le flux existant de changement de slide.
- Réinitialiser la persistance dans le flux existant qui active « Afficher toutes les slides ».
- Régénérer `index.html` avec `build.py`.
- Mettre à jour les tests de contrat existants.

MUST NOT modifier le texte des descriptions, des discours oraux, des titres, des alternatives ou des images.

## Tests automatisés obligatoires

Ajouter des tests qui vérifient au minimum :

- exactement 45 commandes de groupe sont générées ;
- chaque commande précède le groupe des deux accordéons de sa slide ;
- chaque commande est un bouton DSFR ordinaire placé hors de `.fr-accordions-group` et ne possède pas la classe `.fr-accordion__btn` ;
- chaque `aria-controls` référence exactement deux panneaux existants de la même slide ;
- aucun identifiant n’est dupliqué ;
- l’état initial est fermé avec le libellé `Tout ouvrir` ;
- les 90 accordéons individuels existants sont toujours présents ;
- le JavaScript contient un état en mémoire et n’utilise aucun stockage persistant ;
- la sortie générée reste synchronisée avec `build.py` ;
- les contrats existants restent verts.

Exécuter :

```bash
python3 projets-livrables-opquast-v5/build.py
python3 -m unittest discover -s projets-livrables-opquast-v5/tests
python3 -m unittest discover -s scripts/tests
python3 scripts/check_notes_orales_opquast.py projets-livrables-opquast-v5
scripts/validate_variant.sh projets-livrables-opquast-v5
git diff --check -- projets-livrables-opquast-v5
```

## Recette navigateur obligatoire

Sur `http://127.0.0.1:8001/projets-livrables-opquast-v5/`, vérifier réellement :

1. Slide 1 fermée au chargement.
2. `Tout ouvrir` ouvre exactement les deux panneaux, devient `Tout fermer`, expose `aria-expanded="true"` et conserve le focus.
3. La slide suivante hérite de l’état ouvert.
4. La fermeture manuelle d’un accordéon produit un état mixte, remet la commande sur `Tout ouvrir` et annule la persistance.
5. La slide suivante affiche alors ses deux accordéons fermés.
6. Le rechargement rétablit l’état fermé.
   Le chargement direct d’une URL avec un fragment de slide produit le même état fermé.
7. En mode « Afficher toutes les slides », la commande d’une slide n’agit que sur ses deux panneaux.
8. Le retour au diaporama repart fermé.
9. `Entrée` et `Espace` activent la commande.
10. Aucun débordement horizontal n’apparaît à 390 × 844.
11. Aucune erreur JavaScript ni requête locale en échec n’est présente.
12. Le nom accessible contient le libellé visible et décrit la description ainsi que le discours oral de la bonne slide.

Ne pas masquer un échec de recette. Distinguer les défauts introduits par cette modification des anomalies préexistantes.

## Anomalie préexistante à préserver hors de ce changement

Un audit local a déjà identifié que le premier appui sur `Tab` à l’URL racine atteint directement `#description-active` après la réécriture automatique vers `#slide-01`, au lieu du premier lien d’évitement. Cette anomalie est hors périmètre de cette fonctionnalité.

MUST NOT la corriger silencieusement dans ce chantier. MUST la mentionner comme limite empêchant toute affirmation de conformité RGAA globale.

## Livrable attendu

À la fin, fournir :

1. les fichiers modifiés ;
2. le comportement implémenté dans les deux modes ;
3. les commandes de test et leurs résultats exacts ;
4. la recette navigateur exécutée et ses limites ;
5. les anomalies restantes ;
6. une demande de validation humaine sur l’URL locale.

Arrêter après la phase 1. Après validation humaine explicite seulement, préparer une phase 2 pour intégrer ce comportement à la matrice des futurs jeux de slides. Après une seconde validation explicite seulement, préparer la phase 3 de rétroaction sur les autres séries.
