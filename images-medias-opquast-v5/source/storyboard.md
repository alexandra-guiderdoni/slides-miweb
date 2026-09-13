# Storyboard utilisé — Opquast « Images et médias »

Source : brief utilisateur `opquast_images_medias_brief_agent(1).md`

Ce document reprend le storyboard final recommandé ayant servi de base à la génération du lot de 15 slides.

---

# 9. Storyboard final recommandé

## Slide 1 — Images et médias

**Titre** \
Images et médias

**Sous-titre** \
Accès · Sobriété · Contrôle

**Message clé** \
Les médias doivent enrichir l'expérience sans rendre l'information inaccessible, alourdir inutilement le service ou retirer le contrôle à l'utilisateur.

**Visuel** \
Interface web avec image, graphique, vidéo, audio et animation. Trois notions autour : Accès, Sobriété, Contrôle.

**Brief image** \
Illustration éditoriale professionnelle d'une interface numérique moderne avec photo, graphique, lecteur vidéo, lecteur audio et animation. Organiser l'ensemble autour de trois notions : accès à l'information, sobriété des ressources et contrôle utilisateur. Style pédagogique épuré.

**Discours oral** \
« Les images, les vidéos, le son et les animations enrichissent énormément nos interfaces. Mais ils peuvent aussi créer des difficultés très concrètes. Une information peut disparaître lorsqu'une image n'est pas perçue. Une vidéo peut devenir inaccessible sans transcription ou sous-titres. Une image de plusieurs milliers de pixels peut être téléchargée pour être affichée comme une petite vignette. Un son peut démarrer sans que personne ne l'ait demandé. Nous allons donc lire cette rubrique avec trois idées simples : accès, sobriété et contrôle. »

---

## Slide 2 — Commencer par le problème utilisateur

**Message clé** \
Avant de mémoriser une règle, comprendre ce qu'elle cherche à éviter.

**Schéma** \
Situation → Risque → Principe → Règle → Mise en œuvre

**Brief visuel** \
Infographie horizontale en cinq étapes avec une icône par étape.

**Discours oral** \
« Nous n'allons pas parcourir douze règles comme douze éléments indépendants. Pour chacune, nous allons d'abord regarder la situation et le problème rencontré par l'utilisateur. Ensuite seulement, nous verrons le principe de prévention, la règle et sa mise en œuvre. »

---

## Slide 3 — Une image n'a pas toujours le même rôle

**Message clé** \
L'alternative dépend de la fonction de l'image dans son contexte.

**Contenu**
- décorative — 116 ;
- image-lien — 117 ;
- informative — 118.

**Situation** \
La même illustration apparaît dans trois contextes différents.

**Risque** \
Traiter toutes les images de la même manière produit trop d'informations inutiles, un lien incompréhensible ou une perte d'information.

**Visuel** \
Même image dans trois usages.

**Discours oral** \
« On ne regarde pas seulement ce que représente l'image. On regarde ce qu'elle fait dans cette page. »

---

## Slide 4 — Que doit restituer l'alternative ?

| Rôle | Question | Réponse |
|---|---|---|
| Décorative | Que perd-on sans l'image ? | Rien |
| Image-lien | Que fait ce lien ? | Fonction ou destination |
| Informative | Quelle information disparaît ? | Cette information |

**Exemples**

```html
alt=""
```

```html
alt="Accueil"
```

```html
alt="Livraison gratuite dès 50 €"
```

**Risques**
- 116 : pollution de la restitution ;
- 117 : lien incompréhensible ;
- 118 : perte d'information.

---

## Slide 5 — Quand une alternative courte ne suffit plus

**Message clé** \
Une image complexe peut nécessiter plusieurs niveaux d'accès.

**Contenu**
1. Alternative courte.
2. Description étendue.
3. Données numériques pour un graphique.

**Règles**
- 118 ;
- règle connexe 12.

**Données illustratives**
- 2023 : 100
- 2024 : 125
- 2025 : 145
- 2026 : 180

**Visuel** \
Graphique + phrase de synthèse + tableau.

**Discours oral** \
« L'utilisateur doit pouvoir accéder aux données, pas seulement à leur dessin. »

---

## Slide 6 — Petit à l'écran ne veut pas dire petit à télécharger

**Situation** \
5000 × 5000 px affiché en 100 × 100 px.

**Risque** \
Ressource inutilement lourde téléchargée.

**Principe** \
Ne pas télécharger une grande image pour l'afficher en petit.

**Règle** \
119.

**Mise en œuvre**
- variantes réellement réduites ;
- dimensions adaptées ;
- `srcset` lorsque pertinent.

**Visuel** \
Comparaison grande image redimensionnée / vraie vignette.

---

## Slide 7 — Si l'objet intégré ne fonctionne pas, que reste-t-il ?

**Situation** \
Contenu intégré via `object` ou `embed`.

**Risque** \
Perte d'information ou de service.

**Principe** \
Prévoir une alternative.

**Règle** \
120.

**Mise en œuvre**
- HTML équivalent ;
- texte ;
- transcription ;
- lien alternatif.

---

## Slide 8 — Plusieurs chemins vers le même contenu

**Situation** \
Interview uniquement en vidéo.

**Risques**
- absence de transcription ;
- absence de sous-titres ;
- durée inconnue.

**Règles**
- 121 : transcription ;
- 122 : sous-titres ;
- 123 : durée.

**Visuel** \
Lecteur vidéo avec transcription, sous-titres et durée.

---

## Slide 9 — Transcription ≠ sous-titres

**Transcription** \
Texte indépendant du média.

**Sous-titres** \
Texte synchronisé avec la vidéo.

**Règles** \
121 / 122.

**Visuel** \
Article texte vs vidéo sous-titrée.

---

## Slide 10 — C'est l'utilisateur qui décide

**Situation** \
Vidéo + musique + animation.

**Risques**
- démarrage inattendu ;
- perturbation ;
- consommation non demandée ;
- distraction persistante.

**Principe** \
L'utilisateur déclenche et contrôle.

**Règles**
- 124 : vidéo ;
- 125 : son ;
- 126 : pause / contrôle.

**Repères**
- animation > 5 s ;
- son > 3 s.

**Visuel** \
Commandes lecture / pause / muet / volume.

**Discours oral** \
« Le service propose. L'utilisateur décide. »

---

## Slide 11 — Une animation ne doit jamais faire barrage

**Situation** \
Animation d'introduction avant le contenu.

**Risque** \
Attente imposée.

**Principe** \
Une animation ne doit pas devenir un passage obligatoire.

**Règle** \
127.

**Visuel**
- mauvais : Arrivée → animation → attente → contenu
- adapté : Arrivée → passer → contenu

---

## Slide 12 — La thématique dépasse la rubrique

**Message clé** \
La rubrique s'arrête à 127, mais les problématiques médias sont transversales.

**Familles affichées**
- graphiques ;
- liens ;
- téléchargements ;
- présentation visuelle ;
- PDF.

**Règles**
- 12 ;
- 136-137 ;
- 147-150 ;
- 159 ;
- 181, 183, 187-189 ;
- 240-241.

**Visuel** \
« Images et médias » au centre, familles connexes autour.

---

## Slide 13 — Cas pratiques

> Ces cas sont des exercices originaux de formation, pas des questions officielles de certification.

### Cas A
Image décorative :

```html
alt="Jolie décoration bleue"
```

- **Risque** : pollution de la restitution.
- **Principe** : ne pas restituer une information inutile.
- **Règle** : 116.

### Cas B
Vidéo de 45 minutes sans durée.

- **Risque** : engagement inconnu avant lancement.
- **Principe** : informer avant consultation.
- **Règle** : 123.

### Cas C
Graphique accompagné de son tableau de données.

- **Analyse** : le risque de perdre les données est réduit, sans permettre de conclure à la conformité globale.
- **Règle connexe** : 12.

### Cas D
Musique automatique à l'ouverture.

- **Risque** : surprise sonore et perte de contrôle.
- **Principe** : déclenchement volontaire.
- **Règle** : 125.

### Cas E
Vidéo automatique sans son.

- **Risque** : lecture et consommation de données sans demande.
- **Principe** : lancement volontaire.
- **Règle** : 124.

**Animation pédagogique** \
Faire apparaître :
1. situation ;
2. risque ;
3. principe ;
4. règle.

---

## Slide 14 — Les 12 règles en trois questions

### Puis-je toujours accéder à l'information ?
116, 117, 118, 120, 121, 122, 123

### Est-ce que je télécharge inutilement ?
119

### Est-ce que je garde le contrôle ?
124, 125, 126, 127

> **Note : regroupement pédagogique, non classement officiel Opquast.**

---

## Slide 15 — Conclusion

**Titre** \
Le média doit rester au service de l'utilisateur

**Trois phrases**
- Rendre l'information accessible.
- Télécharger seulement ce qui est nécessaire.
- Laisser l'utilisateur décider.

**Trois questions finales**
1. Si le média disparaît, l'information reste-t-elle accessible ?
2. Est-ce que je fais télécharger plus que nécessaire ?
3. Est-ce que l'utilisateur garde la main ?

**Discours oral** \
« Une image, une vidéo, un son ou une animation ne sont pas des problèmes. Ils deviennent des problèmes lorsqu'ils enferment l'information, consomment inutilement des ressources ou prennent le contrôle à la place de l'utilisateur. »

---
