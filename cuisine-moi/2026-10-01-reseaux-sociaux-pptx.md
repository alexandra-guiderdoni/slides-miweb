Réseaux sociaux adaptés au PPTX IGPDE : notes cuisine-moi
=========================================================

Date : 2026-10-01 | Objectif : cadrer une nouvelle présentation web autonome qui couvre la section réseaux sociaux du PPTX IGPDE.

## Résumé / décisions clés

- Créer un nouveau dossier autonome dans `slides-miweb` sans modifier la présentation V2 publiée.
- Conserver deux contenus distincts par slide : transcription descriptive et discours oral directement prononçable.
- Prendre la section réseaux sociaux actuelle du PPTX comme source pédagogique de référence.
- Construire 22 slides web en correspondance 1 pour 1 avec les 22 slides du module PPTX.
- Régénérer les 22 visuels dans une grammaire IGPDE-DSFR cohérente : typographie plus grande, bleu institutionnel, compositions sobres et exemples concrets.
- Restituer le contenu du PPTX en HTML structuré et sémantique, sans le remplacer par une synthèse éditoriale différente.
- Alimenter « Lire la transcription de la slide » avec tout le contenu visible du PPTX, dans son ordre logique.
- Alimenter « Lire le discours oral de la slide » avec les notes du présentateur du PPTX, structurées sans créer un nouveau cours.
- Nommer le nouveau jeu `publier-de-facon-accessible-sur-les-reseaux-sociaux-v3`.
- Ne pas publier, committer ni pousser pendant ce chantier sans demande explicite.

## Journal questions-réponses

### Q1 - Granularité de correspondance
- Question : faut-il construire 22 slides en miroir du PPTX, une version condensée ou une version enrichie ?
- Capture : Alex choisit la correspondance 1 pour 1. Chaque slide web devra donc correspondre à une slide du module réseaux sociaux du PPTX, dans le même ordre, avec une adaptation visuelle qui ne change pas la progression pédagogique.
- Drapeaux : Aucun.

### Q2 - Direction visuelle
- Question : faut-il régénérer une série IGPDE-DSFR, conserver la grammaire de la V2 ou réemployer une partie des anciens visuels ?
- Capture : Alex choisit une nouvelle série entièrement régénérée, cohérente avec l’IGPDE et le DSFR, avec une grande typographie, une palette institutionnelle, des compositions sobres et des exemples concrets.
- Drapeaux : Aucun.

### Q3 - Fidélité du contenu HTML
- Question : quel niveau de détail faut-il donner au discours oral ?
- Capture : Alex souhaite idéalement retrouver le même contenu que dans le PPTX, restitué en HTML structuré et sémantique. La priorité est donc la fidélité au support source, plutôt qu’une nouvelle rédaction plus longue ou plus courte.
- Drapeaux : Aucun.

### Q4 - Correspondance des deux accordéons
- Question : la transcription doit-elle reprendre tout le contenu visible et le discours oral toutes les notes du présentateur, sans nouveau cours ?
- Capture : Alex confirme cette correspondance. Les reformulations visuelles nécessaires à la lisibilité n’autorisent aucune perte dans la transcription HTML.
- Drapeaux : Aucun.

## Drapeaux ouverts

- Slide 22 : confirmer si les coordonnées des formateurs doivent être reproduites dans le jeu public. Par défaut, les coordonnées de tiers restent exclues et sont remplacées par une mention de confidentialité.

## Relecture croisée du storyboard

- Une relecture indépendante des 22 scripts source a confirmé l’ordre, la correspondance 1 pour 1 et la progression pédagogique.
- Les formulations destinées aux images ont été nettoyées pour ne contenir que du texte visible sur la slide correspondante.
- La règle complète sur l’image décorative est conservée mot pour mot.
- Les notes `add_notes()` restent la source autoritative du discours oral et doivent être reprises intégralement.
- Les variations volontaires du PPTX sont tracées dans le storyboard au lieu d’être harmonisées.
- La génération reste conditionnée à un contrôle ciblé des corrections P1.

## Prochaine étape

- Extraire les 22 slides et leurs notes depuis les sources du PPTX.
- Produire le storyboard miroir et les visuels IGPDE-DSFR.
- Créer le nouveau jeu avec la matrice, compléter `slides.json`, construire et valider localement.
