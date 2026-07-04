---
name: alt-text
description: "Rédaction et audit d'alternatives textuelles pour images, icônes, logos, graphiques, PDF/PPTX/HTML. Utiliser quand il faut remplir ou vérifier un champ alt, texte de remplacement, image sans alt, image-lien, image décorative, CAPTCHA, image contenant du texte ou image complexe."
allowed-tools: Read, Glob, Grep, Bash
context: conversation
metadata:
  argument-hint: "[images, fichier HTML/PDF/PPTX, tableau d'images ou contexte à auditer]"
---

# Alt-text

## Promesse

Rendre la décision d'alternative textuelle prévisible en forçant l'analyse de la fonction du visuel, du contexte adjacent et de l'incertitude.

Produire un texte de remplacement, pas une description visuelle. L'alt doit transmettre ce que le lecteur aurait compris si l'image n'était pas affichée.

## Principe

Avant de rédiger, déterminer la fonction de l'image dans son contexte. Imaginer la page lue au téléphone : remplacer l'image par les mots qui maintiennent le sens, sans annoncer l'existence de l'image.

Ne jamais commencer par "Image de", "Photo de", "Icône de", "Illustration de", "Logo de" ou "Logo". La technologie d'assistance annonce déjà le type d'élément ; pour un logo, donner le nom de l'organisation ou de la destination.

## Périmètre

Utiliser ce skill pour rédiger, corriger ou auditer des alternatives textuelles dans des livrables web, PDF, PPTX, DOCX, Markdown ou tableaux d'images.

Ne pas utiliser pour :

- produire une description artistique, éditoriale ou SEO d'une image ;
- faire de l'OCR complet quand aucun texte lisible n'est fourni ;
- remplacer un audit RGAA/WCAG complet sur toutes les thématiques ;
- décrire des images hors contexte quand la fonction éditoriale manque.

## Modes d'usage

| Mode | Déclencheur | Critère de fin |
|---|---|---|
| Rédaction unitaire | Une image ou icône avec contexte fourni | Le rôle est identifié, l'alt proposé conserve l'information utile, et l'incertitude éventuelle est signalée. |
| Audit de lot | Plusieurs images, page, document ou tableau d'images | Chaque image a un rôle, un alt proposé ou `alt=""`, et une note justifie les cas ambigus. |
| Image complexe | Graphique, schéma ou visuel riche | Un alt court est proposé et la nécessité d'une description détaillée adjacente ou liée est décidée. |
| Source HTML/PDF/PPTX/DOCX/Markdown | Fichier source à vérifier | Les alt existants sont classés en garder, corriger, vider, relier ou compléter, avec preuve par contexte adjacent. |

## Déploiement contrôlé

Ce skill agit comme copilote d'accessibilité, pas comme moteur de conformité autonome.

- Mode suggestion : produire des propositions, tableaux d'audit ou champs préremplis ; ne pas injecter de code ni modifier les sources sans validation explicite.
- Revue humaine : toute incertitude, mention `À confirmer`, alternative longue ou image complexe doit déclencher une décision humaine.
- Traçabilité : chaque décision doit rester justifiée par la fonction, le contexte, le rôle et la note dans la sortie recommandée.

## Contrat d'exécution

BRANCH-MAP :

| Branche | Déclencheur utilisateur ou modèle | Étapes nécessaires | Références nécessaires | Critère de fin |
|---|---|---|---|---|
| Rédaction | Image ou icône avec contexte | 1. lire le contexte ; 2. choisir le rôle ; 3. rédiger ou vider l'alt | commune: ce fichier | Rôle + alt proposé + incertitude éventuelle |
| Audit de lot | Tableau, page ou document | 1. inventorier ; 2. classer ; 3. proposer garder/corriger/vider/compléter | commune: ce fichier | Chaque ligne a rôle, décision et note si nécessaire |
| Complexe | Graphique, schéma, carte, statistique | 1. alt court ; 2. description longue ; 3. données disponibles | commune: ce fichier | Alt court + description ou demande de données |
| Intégration web | HTML, SVG, lien, figure, texte-image | 1. vérifier le support ; 2. nommer ou masquer ; 3. relier si besoin | commune: section technique | Technique correcte ou point à corriger |

LEXICAL-CANDIDATES :

| Intention comportementale | Candidats | Rejetés | Retenu | Effet sémiotique | Raison |
|---|---|---|---|---|---|
| Décider ce que l'image fait | fonction, rôle, action, destination, information, redondance | description, apparence, joli | fonction, rôle | cadrage + trace `Rôle` | Force le choix avant la rédaction. |
| Ancrer la lecture autour de l'image | contexte, adjacent, légende, titre, lien, paragraphe, destination | hors-sol, deviner | contexte | trace dans `Note` | Empêche les alt génériques. |
| Gérer le doute sans inventer | incertitude, confirmer, illisible, manquant, validation, hypothèse | probablement, sûrement | incertitude | trace `À confirmer` | Transforme le doute en revue humaine. |
| Couvrir les contraintes web | structure, SVG, figure, figcaption, données, tableau, HTML/CSS | pixel, couleur, style | structure | trace technique | Stabilise les cas SVG, graphique et légende. |

LEADING-WORDS :

| Mot conducteur | Comportement condensé | Répétition token | Trace observée | Test no-op |
|---|---|---|---|---|
| `fonction` | Décider ce que l'image fait dans la page | Principe, règles, checklist | Colonne Rôle ou Note | Non no-op : distingue lien, décoratif, information |
| `contexte` | Lire autour avant de rédiger | Principe, procédure, sortie | Justification par titre, légende ou lien | Non no-op : empêche l'alt hors sol |
| `rôle` | Classer avant d'écrire | Modes, procédure, tableau | Colonne Rôle obligatoire | Non no-op : stabilise `alt=""` |
| `incertitude` | Signaler au lieu d'inventer | Promesse, gestion, sortie | Note `À confirmer` | Non no-op : évite les alt faux |
| `structure` | Vérifier le support technique avant de conclure | SVG, figure, texte-image, graphique | Note technique ou correction HTML/SVG | Non no-op : distingue nommer, masquer, relier |

INVESTIGATION-WORK :

| Branche | Actions d'investigation obligatoires | Preuve exigée | Critère renforcé avant split | Observation précipitation | Type de split | Décision split |
|---|---|---|---|---|---|---|
| Toutes branches | Lire le contexte adjacent, identifier le rôle, vérifier le support HTML/SVG, citer l'information manquante et ne pas modifier les fichiers source sans demande explicite. | Tableau final avec `Image`, `Rôle`, `Alt proposé`, `Note` ; ou alt unitaire avec rôle et incertitude. | Chaque image traitée a un rôle, un alt proposé ou `alt=""`, et une note seulement si elle lève une incertitude, justifie un alt vide ou demande une description longue. | Aucune précipitation observée après ajout des modes et critères de fin ; le risque principal reste l'alt hors contexte, traité par `contexte` et `rôle`. | Aucun split. | Garder ce skill mono-skill tant que les branches tiennent dans ce fichier et restent sous 300 lignes. |

Critère de fin : chaque image traitée a un rôle, un alt proposé ou `alt=""`, et une note seulement si elle lève une incertitude, justifie un alt vide ou demande une description longue.

COLOCATION :

| Concept critique | Définition | Règles | Limites/pièges | Emplacement unique | Justification si dispersé |
|---|---|---|---|---|---|
| Alternative textuelle | Texte qui remplace la fonction du visuel dans son contexte. | SVG, figure, texte-image, graphique, légende et incertitude restent ici. | Ne couvre pas un audit RGAA/WCAG complet ni l'OCR sans source lisible. | Ce fichier. | Disperser créerait des décisions d'alt contradictoires. |

PRUNING :

| Cible | Décision | Preuve comportementale de conservation | Saint-Exupéry |
|---|---|---|---|
| Duplication | Conserver seulement les interdits critiques. | Sans rappel, l'agent remplit les alt décoratifs par prudence. | Retirer casserait la décision `alt=""`. |
| Sédiment | Supprimer les normes non actionnables. | Une citation qui ne change aucune décision d'alt est retirée. | Retirer améliore la lecture sans perte. |
| Sprawl | Garder ici tant que le fichier reste sous 300 lignes. | Externaliser seulement si une branche technique devient autonome. | Scinder maintenant dégraderait COLOCATION. |
| No-op | Supprimer les conseils esthétiques génériques. | Les adjectifs visuels sans effet informatif sont déjà interdits. | Retirer évite de payer des tokens inutiles. |

TALK-FIDELITY :

| Marqueur | Couverture | Preuve | Décision |
|---|---|---|---|
| Description comme pointeur de contexte | Présent | La description déclenche champ alt, image sans alt, image-lien, décoratif, CAPTCHA et image complexe. | Garder model-invoked. |
| Superpowers / skills invoqués par l'utilisateur | NA justifié | Le skill ne dépend pas d'une méthode de développement externe. | Ne pas ajouter de dépendance. |
| skill-writing-great-skills | Présent | Promesse, BRANCH-MAP, LEADING-WORDS, INVESTIGATION-WORK, PRUNING et METHOD-COMPLETE. | Contrat suffisant. |
| 2PRD, ADR, plan mode, Matt Pocock, domain modeling | NA justifié | Le skill promet une décision d'alt vérifiable, pas une architecture ou un plan produit. | La trace utile reste le tableau de sortie. |

SMOKE-TRIGGER :

| Prompt de routage | Verdict attendu | Raison |
|---|---|---|
| `J'ai une page HTML avec des images sans alt, des SVG et des icônes-liens : propose les alternatives.` | Déclencher `alt-text` | Contient image sans alt, SVG, icônes-liens et demande d'alternatives. |
| `Décris cette photo de façon poétique pour une accroche marketing.` | Ne pas déclencher | Demande description artistique ou SEO, explicitement hors périmètre. |

METHOD-COMPLETE

Promesse : rendre la décision d'alternative textuelle prévisible par fonction, contexte et incertitude.
Invocation : model-invoked ; charge contexte assumée par la description.
Branche : rédaction, audit de lot, complexe, intégration web.
Scénario représentatif : lot HTML avec icône bouton, SVG décoratif, graphique chiffré et image légendée.
Risque sans skill : descriptions visuelles, alt redondants ou masquage décoratif oublié.
Comportement avec skill : rôle choisi, alt ou masquage décidé, données du graphique et liaison de légende vérifiées.
Déclenchement modèle : smoke prompt sans nommer le skill et near-miss négatif définis dans `SMOKE-TRIGGER` ; runtime non mesuré ici.
Trace des mots conducteurs : `fonction` et `rôle` dans la colonne Rôle ; `contexte` et `incertitude` dans Note ; `structure` dans la note technique.
Test no-op : chaque mot conducteur change une décision observable : rédiger, vider, relier, masquer ou demander confirmation.
Preuve : tableau de sortie couvrant `Image`, `Rôle`, `Alt proposé` et `Note`.
Verdict : GO local

Ce skill reste mono-skill : ne pas le scinder ni créer de référence externe tant que la procédure tient dans ce fichier et que les cas complexes se résolvent par une description détaillée adjacente ou liée.

## Procédure

1. Lire le contexte adjacent : titre, légende, paragraphe, bouton, lien, consigne, destination.
2. Identifier le rôle réel de l'image :
   - décorative ou redondante ;
   - informative ;
   - lien ou bouton ;
   - logo ou marque ;
   - image contenant du texte ;
   - graphique, schéma ou image complexe ;
   - CAPTCHA.
3. Rédiger l'alt selon le rôle, avec la formulation la plus courte qui conserve l'information.
4. Vérifier que la phrase environnante reste naturelle si l'image est remplacée par l'alt.
5. Si l'information utile est inconnue ou illisible, signaler le besoin de validation au lieu d'inventer.

## Gestion des incertitudes

| Situation | Action |
|---|---|
| Image absente ou illisible | Demander l'image, une capture ou le contexte source |
| Contexte adjacent absent | Proposer une hypothèse prudente et marquer `À confirmer` |
| Texte dans l'image partiellement lisible | Ne reprendre que le texte certain et signaler l'incertitude |
| Image complexe sans description longue | Proposer un alt court et demander ou rédiger une description détaillée séparée |
| Image possiblement décorative mais utilisée comme lien | Traiter comme lien : action ou destination obligatoire |

Ne jamais inventer une information métier, un chiffre, une identité ou une destination qui n'est pas visible dans l'image ou donnée par le contexte.

## Règles par type

| Type d'image | Alt attendu |
|---|---|
| Décorative | `alt=""` |
| Redondante avec le texte adjacent | `alt=""` |
| Informative | Information portée par l'image, sans détail inutile |
| Lien ou bouton | Destination ou action, pas l'apparence |
| Logo seul | Nom de l'organisation ou du service |
| Logo-lien | Destination, souvent "Accueil" si le lien revient à l'accueil, sans préfixe `Logo` |
| Texte dans l'image | Texte visible repris fidèlement ; en audit, recommander le remplacement par du texte HTML/CSS sauf logotype ou contrainte justifiée |
| Graphique ou schéma complexe | Alt court + description détaillée adjacente ou liée, avec données chiffrées exactes si elles existent |
| CAPTCHA | Nature et fonction du test, jamais le contenu du code |

## Contraintes web techniques

| Cas technique | Décision attendue |
|---|---|
| `<img>` décoratif | Utiliser `alt=""` et ne pas ajouter de titre redondant. |
| `<svg>` décoratif | Retirer de l'arbre d'accessibilité avec `aria-hidden="true"` si le SVG n'est pas focusable ni interactif. |
| `<svg>` informatif | Ajouter un rôle image et un nom accessible : `role="img"` avec `aria-label`, `aria-labelledby` ou un `<title>` fiable ; utiliser `aria-describedby` ou un lien pour une description longue. |
| Image-lien ou bouton icône seul | Le nom accessible indique l'action ou la destination ; si un texte visible existe déjà, masquer l'icône décorative. |
| Image texte informative | Préférer du texte HTML stylé en CSS ; si impossible ou logotype, reprendre le texte visible dans l'alt. |
| Image complexe ou graphique | Fournir la tendance dans l'alt court et les données numériques dans la description détaillée, souvent sous forme de tableau. |
| Image avec légende visible | Vérifier l'association programmée : image et légende dans `<figure>`, légende dans `<figcaption>`, et nom du groupe cohérent avec la légende si nécessaire. |

## Contraintes de rédaction

- Viser 80 caractères maximum. Tolérer jusqu'à 120 si le sens l'exige.
- En audit, une alternative de plus de 80 caractères est un candidat à revue humaine, pas une non-conformité automatique.
- Traiter les préfixes `image de`, `photo de`, `illustration de`, `logo de` ou `logo` comme des candidats redondants à vérifier, pas comme une suppression automatique hors contexte.
- Éviter les adjectifs visuels sans valeur informative : joli, bleu, grand, stylisé.
- Ne pas répéter une légende, un titre ou un texte immédiatement adjacent.
- Ne pas écrire un alt vide pour une image porteuse d'information.
- Ne pas utiliser le nom de fichier comme alt.
- Pour une image complexe, ne pas compresser toute l'analyse dans l'alt : ajouter ou demander une description longue visible ou liée.

## Exemples

| Contexte | Mauvais | Bon |
|---|---|---|
| Logo Twitter non cliquable | `Logo constitué d'un oiseau bleu` | `Twitter` |
| Loupe qui lance une recherche | `Loupe` | `Lancer la recherche` |
| Séparateur décoratif | `Trait décoratif` | `alt=""` |
| Image affichant "Soldes -50 %" | `Bannière de promotion` | `Soldes -50 %` |
| CAPTCHA avant envoi | `Lettres A7K9` | `Code de sécurité anti-spam` |
| Photo déjà légendée avec la même info | répétition de la légende | `alt=""` |
| Graphique de progression | `Graphique en barres bleu` | `Progression des inscriptions 2024` + description longue |

Exemple HTML :

```html
<button type="submit">
  <img src="loupe.svg" alt="Lancer la recherche">
</button>

<img src="separateur.svg" alt="">

<a href="/">
  <img src="logo.svg" alt="Accueil">
</a>

<svg aria-hidden="true" focusable="false">
  <!-- icône décorative -->
</svg>

<figure role="group" aria-label="Répartition des inscriptions par année">
  <img src="inscriptions.png" alt="Progression des inscriptions 2022-2024">
  <figcaption>Répartition des inscriptions par année</figcaption>
</figure>
```

Exemple de demande :

```text
Entrée : icône loupe dans un bouton submit du formulaire de recherche.
Sortie : Lancer la recherche

Entrée : photo déjà légendée "Marie Dupont remet le prix Accessibilité 2026".
Sortie : alt=""
Note : information déjà donnée par la légende adjacente.

Entrée : graphique sans description longue montrant les inscriptions 2022-2024.
Sortie : Progression des inscriptions 2022-2024
Note : ajouter une description détaillée des valeurs et tendances.
```

## Sortie recommandée

Pour un lot d'images, produire un tableau court :

| Image | Rôle | Alt proposé | Note |
|---|---|---|---|
| `slide08-Image_20.png` | décorative | `alt=""` | Redondante avec le titre adjacent |
| `search-icon.svg` | bouton | `Lancer la recherche` | Action déclenchée |
| `chart.svg` | image complexe | `Progression des inscriptions 2022-2024` | Ajouter les valeurs exactes dans un tableau adjacent |

Si l'image est ambiguë, mettre `À confirmer` dans la note, pas dans l'attribut `alt`.

## Pièges connus et checklist

Excuses interdites :

- "Je décris ce que je vois, ce sera plus complet" : non, l'alt remplace l'information utile.
- "Je remplis tous les alt pour éviter les champs vides" : non, `alt=""` est correct pour le décoratif.
- "Je laisse l'alt long pour être exhaustif" : non, utiliser une description longue séparée.
- "Je devine le message de l'image" : non, signaler l'incertitude.

Pièges fréquents :

- Alt visuel au lieu de fonctionnel : ne pas écrire `Loupe` si l'image lance une recherche.
- Alt non vide sur élément décoratif : ne pas remplir pour rassurer un validateur automatique.
- Alt trop long sur graphique : ne pas remplacer la description détaillée par une phrase de 300 caractères.
- Longueur ou mot redondant transformé en verdict RGAA : remonter un signal de revue humaine, jamais une conformité ou non-conformité automatique.
- SVG traité comme `<img>` : ne pas proposer `alt=""` sur un `<svg>` ; choisir `aria-hidden` ou nom accessible.
- Image texte conservée sans raison : proposer du texte HTML/CSS sauf logotype ou contrainte justifiée.
- Légende visible non reliée : vérifier la structure `<figure>` / `<figcaption>` en audit web.
- Alt inventé : ne pas déduire une information qui n'est ni visible ni donnée par le contexte.
- NE PAS transformer l'alt en légende éditoriale, résumé de slide ou commentaire pédagogique.
- JAMAIS masquer une information nécessaire avec `alt=""`.

Avant de livrer, vérifier :

- [ ] Chaque alt correspond à la fonction de l'image.
- [ ] Les alt de plus de 80 caractères sont signalés comme candidats à revue, sans verdict automatique.
- [ ] Les préfixes redondants comme `image de`, `photo de`, `illustration de` ou `logo` sont signalés si présents.
- [ ] Les images décoratives ou redondantes ont un alt vide.
- [ ] Les images-liens indiquent l'action ou la destination.
- [ ] Les textes visibles dans l'image sont repris.
- [ ] Les images textes remplaçables sont signalées pour remplacement HTML/CSS.
- [ ] Les SVG sont masqués ou nommés selon leur rôle.
- [ ] Les légendes visibles sont reliées à l'image.
- [ ] Aucun alt ne commence par "image de" ou équivalent.
- [ ] Les images complexes ont une description longue avec données chiffrées si nécessaire.
