Commande persistante des accordéons : notes cuisine-moi
======================================================

Date : 2026-10-12 | Objectif : cadrer une commande accessible qui ouvre ou ferme les deux accordéons et conserve cet état pendant la navigation entre les slides.

## Résumé / décisions clés

- Périmètre initial : uniquement `projets-livrables-opquast-v5`.
- Généralisation ultérieure : matrice des futurs jeux de slides, puis rétroaction vers les autres séries, seulement après validation de l’expérimentation.
- La démo de référence utilise un bouton à libellé dynamique « Tout ouvrir » / « Tout fermer », avec `aria-expanded` et `aria-controls`.
- La série possède deux accordéons indépendants par slide : description détaillée et discours oral.
- Persistance choisie : navigation uniquement ; l’état est conservé de slide en slide et réinitialisé au rechargement de la page.
- Une action manuelle sur un accordéon annule le mode global ; à la slide suivante, les deux accordéons sont fermés.
- En mode « Afficher toutes les slides », chacune des 45 commandes contrôle uniquement les deux accordéons de sa slide.
- Les libellés visibles sont courts : « Tout ouvrir » et « Tout fermer ».
- Une commande est placée juste avant les deux accordéons de chaque slide ; 45 commandes sont donc visibles lorsque toutes les slides sont affichées.
- Le passage en mode « Afficher toutes les slides » annule la persistance ; au retour au diaporama, le mode global repart fermé.

## Journal questions-réponses

### Q1 - Durée de persistance
- Question : l’état doit-il persister pendant la navigation, dans l’onglet courant après rechargement ou lors des visites suivantes ?
- Capture : navigation uniquement ; l’état est conservé de slide en slide et réinitialisé au rechargement.
- Drapeaux : aucun.

### Q2 - Action manuelle sur un accordéon
- Question : après « Tout ouvrir », une fermeture manuelle doit-elle annuler le mode global, rester une exception locale ou conserver séparément l’état de chaque accordéon ?
- Capture : annuler le mode global ; la slide courante peut devenir mixte et la slide suivante affiche les deux accordéons fermés.
- Drapeaux : aucun.

### Q3 - Mode « Afficher toutes les slides »
- Question : la commande doit-elle être masquée, agir sur les 90 accordéons ou être déclinée par slide lorsque toutes les slides sont affichées ?
- Capture : choix initial d’ouvrir ou fermer les 90 accordéons.
- Drapeaux : décision remplacée par Q6 après le choix d’une commande placée avant les accordéons de chaque slide.

### Q4 - Libellés des deux états
- Question : faut-il employer des libellés courts, génériques ou dynamiques et précis ?
- Capture : libellés visibles courts « Tout ouvrir » et « Tout fermer » ; le contexte d’utilisation est accepté comme nécessaire à leur compréhension.
- Drapeaux : préciser le nom accessible enrichi dans le prompt afin de conserver le libellé visible dans le nom accessible.

### Q5 - Emplacement de la commande
- Question : faut-il placer la commande dans les contrôles du diaporama, avant les accordéons de chaque slide ou en position flottante ?
- Capture : une commande juste avant les accordéons de chaque slide ; en mode « Afficher toutes les slides », 45 commandes sont visibles.
- Drapeaux : aucun ; la portée locale est fixée par Q6.

### Q6 - Portée des commandes en mode « Afficher toutes les slides »
- Question : les 45 commandes doivent-elles agir sur les 90 accordéons ou seulement sur les deux accordéons voisins ?
- Capture : chaque commande contrôle seulement les deux accordéons de sa slide ; le choix initial de Q3 est remplacé.
- Drapeaux : aucun ; le changement de mode est fixé par Q7.

### Q7 - Changement de mode
- Question : faut-il annuler la persistance en entrant dans « Afficher toutes les slides » ou la suspendre puis la restaurer au retour au diaporama ?
- Capture : annuler la persistance ; les commandes deviennent locales et le mode global repart fermé au retour au diaporama.
- Drapeaux : aucun.

## Drapeaux ouverts

- Aucun drapeau fonctionnel. Le prompt final doit enrichir le nom accessible tout en conservant les libellés visibles courts.
