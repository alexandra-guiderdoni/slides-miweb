---
name: alt-text
description: "Rédaction et audit d'alternatives textuelles pour images, icônes, logos, graphiques, PDF/PPTX/HTML. Utiliser quand il faut remplir ou vérifier un champ alt, texte de remplacement, image sans alt, image-lien, image décorative, CAPTCHA, image contenant du texte ou image complexe."
allowed-tools: Read, Glob, Grep, Bash
metadata:
  context: conversation
  argument-hint: "[images, fichier HTML/PDF/PPTX, tableau d'images ou contexte à auditer]"
---

# Alt-text

Produire un texte de remplacement, pas une description visuelle. L'alt doit transmettre ce que le lecteur aurait compris si l'image n'était pas affichée.

## Principe

Avant de rédiger, déterminer la fonction de l'image dans son contexte. Imaginer la page lue au téléphone : remplacer l'image par les mots qui maintiennent le sens, sans annoncer l'existence de l'image.

Ne jamais commencer par "Image de", "Photo de", "Icône de", "Illustration de". La technologie d'assistance annonce déjà le type d'élément.

## Périmètre

Utiliser ce skill pour rédiger, corriger ou auditer des alternatives textuelles dans des livrables web, PDF, PPTX, DOCX, Markdown ou tableaux d'images.

Ne pas utiliser pour :

- produire une description artistique, éditoriale ou SEO d'une image ;
- faire de l'OCR complet quand aucun texte lisible n'est fourni ;
- remplacer un audit RGAA/WCAG complet sur toutes les thématiques ;
- décrire des images hors contexte quand la fonction éditoriale manque.

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
| Logo-lien | Destination, souvent "Accueil" si le lien revient à l'accueil |
| Texte dans l'image | Texte visible repris fidèlement |
| Graphique ou schéma complexe | Alt court + description détaillée adjacente ou liée |
| CAPTCHA | Nature et fonction du test, jamais le contenu du code |

## Contraintes de rédaction

- Viser 80 caractères maximum. Tolérer jusqu'à 120 si le sens l'exige.
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
- Alt inventé : ne pas déduire une information qui n'est ni visible ni donnée par le contexte.
- NE PAS transformer l'alt en légende éditoriale, résumé de slide ou commentaire pédagogique.
- JAMAIS masquer une information nécessaire avec `alt=""`.

Avant de livrer, vérifier :

- [ ] Chaque alt correspond à la fonction de l'image.
- [ ] Les images décoratives ou redondantes ont un alt vide.
- [ ] Les images-liens indiquent l'action ou la destination.
- [ ] Les textes visibles dans l'image sont repris.
- [ ] Aucun alt ne commence par "image de" ou équivalent.
- [ ] Les images complexes ont une description longue si nécessaire.
