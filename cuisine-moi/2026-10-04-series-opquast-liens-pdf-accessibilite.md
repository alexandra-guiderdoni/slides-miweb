Séries Opquast Liens et PDF, et accessibilité web : notes cuisine-moi
====================================================================

Date : 2026-10-04 | Objectif : cadrer la publication de deux nouveaux jeux web dans slides-miweb, avec leurs accordéons.

## Résumé / décisions clés

- Alex souhaite publier les deux séries issues de la fabrique de slides dans ce dépôt et remplir les accordéons comme dans les autres séries Opquast.
- Les sources visuelles disponibles comprennent 20 slides pour « Liens et PDF » et 5 slides pour « Accessibilité web en octobre » ; les deux `run.json` de la fabrique indiquent `VALIDEE_PRODUCTION` pour chaque slide.
- Le dépôt impose un dossier autonome par nouveau jeu, une transcription descriptive et un discours oral distincts, des alternatives textuelles, une validation avant l'inscription au catalogue et la préservation des jeux déjà publiés.
- La source à reprendre pour « Accessibilité web en octobre » est `Formations-MIWEB/Access/accessibilite-web-octobre-5-slides-validees/` : cinq PNG, brief, storyboard et sources W3C. Leurs empreintes sont identiques aux fichiers correspondants de la fabrique.
- Le brief qualifie ce jeu de série éditoriale Opquast/Miweb, fondée sur le W3C, et interdit de présenter ses principes comme des règles Opquast officielles.
- Titres et chemins publics confirmés par Alex : « Liens et PDF selon Opquast V5 » dans `liens-et-pdf-opquast-v5/` et « Octobre, Web et accessibilité » dans `accessibilite-web-octobre/`.
- Ordre de publication confirmé par Alex : « Liens et PDF » d'abord, puis « Octobre, Web et accessibilité » ; le jeu d'octobre sera mis en avant sur l'accueil après la publication des deux.
- La fabrique conserve cinq fichiers d'accordéons pour « Accessibilité web en octobre » ; ils restent à adapter au schéma `slides.json` et au contrat éditorial du dépôt. Aucun fichier d'accordéons n'est référencé dans le `run.json` de « Liens et PDF ».
- Le dossier « Liens et PDF » contient une synthèse brute de conversation fondée notamment sur le livre. La publication des slides n'implique pas de publier cette synthèse ; la provenance publique peut être documentée par le storyboard, les vérifications et les consignes de production utiles.
- Alex confirme la compréhension partagée du cadre d'exécution : deux jeux autonomes, 20 slides avec annexes puis 5 slides, deux accordéons par slide, étalons à valider avant rédaction complète, contrôles puis publication dans l'ordre choisi.
- Le dépôt est propre, sur `main`, avec une divergence de `0/0` après `git fetch` le 2026-10-04.

## Journal questions-réponses

### Q1 - Positionnement éditorial d'« Accessibilité web en octobre »

- Question : faut-il conserver les cinq visuels comme éclairage éditorial W3C dans la collection Opquast, ou intégrer des règles officielles ?
- Capture : Alex a précisé le dossier source exact. Son `brief.md` donne déjà la réponse : conserver la série éditoriale Opquast/Miweb, la citation et les sources W3C, sans présenter le contenu comme des règles Opquast officielles. La question était donc inutile ; aucun nouveau choix utilisateur n'est requis sur ce point.
- Drapeaux : Aucun pour le positionnement éditorial.

### Q2 - Titres et chemins publics

- Question : retenir les titres descriptifs avec le slug `liens-et-pdf-opquast-v5`, ou garder les slugs de la fabrique, dont `liens-et-pdf` ?
- Capture : après un « ok » ambigu, Alex confirme explicitement « oui » aux noms recommandés : « Liens et PDF selon Opquast V5 » (`liens-et-pdf-opquast-v5`) et « Octobre, Web et accessibilité » (`accessibilite-web-octobre`).
- Drapeaux : Aucun pour les titres et chemins publics.

### Q3 - Ordre d'inscription au catalogue

- Question : publier « Liens et PDF » puis « Octobre, Web et accessibilité », ou l'inverse ? Le dernier jeu inscrit est mis en avant sur l'accueil.
- Capture : Alex répond « oui » à la recommandation explicite de publier « Liens et PDF » d'abord, puis « Octobre, Web et accessibilité ».
- Drapeaux : Aucun pour l'ordre d'inscription.

### Q4 - Compréhension partagée du cadre

- Question : le cadre d'exécution proposé correspond-il au résultat attendu avant la production ?
- Capture : Alex reprend le cadre complet et répond explicitement « oui ».
- Drapeaux : Aucun pour le cadrage ; la validation des étalons reste un jalon de production distinct.

## Cadre d'exécution proposé

- Créer deux jeux web autonomes en conservant les 20 PNG de « Liens et PDF », annexes comprises, et les cinq PNG d'« Accessibilité web en octobre ».
- Rédiger pour chaque slide l'alternative courte, la description, la transcription et le discours oral. Pour « Accessibilité web en octobre », repartir des accordéons conservés dans la fabrique et distinguer les principes W3C des règles Opquast.
- Soumettre d'abord quatre slides étalons de « Liens et PDF » à validation explicite, conformément au contrat des séries Opquast, avant de rédiger le reste ; utiliser aussi un exemple éditorial du jeu d'octobre pour fixer son traitement.
- Conserver dans `source/` les storyboards, références vérifiées et éléments de production utiles ; ne pas recopier par défaut la synthèse brute de conversation.
- Vérifier les règles Opquast, les alternatives, les notes orales, les pages générées et le rendu navigateur, puis inscrire les deux jeux au catalogue dans l'ordre confirmé et contrôler leurs URL publiques.

## Drapeaux levés

- Les quatre slides étalons de « Liens et PDF » et l'exemple d'octobre ont été validés avant la rédaction complète.
- Les pièces de provenance ont été vérifiées avant leur inclusion ; la synthèse brute de conversation n'a pas été publiée.
