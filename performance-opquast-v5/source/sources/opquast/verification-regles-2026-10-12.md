# Vérification des règles Opquast — 12 octobre 2026

- Version : `qualite-numerique`.
- Source : API Opquast via MCP.
- Statut API publique et privée : disponible.
- Usage : contrôle des affirmations déjà présentes dans le Markdown, sans ajout éditorial.

## Règle 119

- Libellé confirmé : Les vignettes et aperçus ne sont pas des images de taille supérieure redimensionnées côté client.
- Objectif confirmé : Diminuer les données, accélérer l’affichage et réduire l’impact énergétique.
- Contrôle confirmé : Comparer dimensions affichées et dimensions réelles.
- Limite publiée : Ne garantit pas à elle seule la performance globale.
- URL : https://checklists.opquast.com/fr/qualite-numerique/119
- Provenance éditoriale : `sources/metier/conversation-opquast-performance.md`.
- Verdict : CONFIRMÉE.

## Règle 123

- Libellé confirmé : La durée des contenus vidéo ou audio est indiquée.
- Objectif confirmé : Permettre de décider de consulter ou télécharger le contenu.
- Contrôle confirmé : Vérifier la durée avant consultation et sa correspondance avec la durée réelle.
- Limite publiée : Informe sur le temps, pas sur le poids.
- URL : https://checklists.opquast.com/fr/qualite-numerique/123
- Provenance éditoriale : `sources/metier/conversation-opquast-performance.md`.
- Verdict : CONFIRMÉE.

## Règle 124

- Libellé confirmé : Les vidéos sont déclenchées par l’utilisateur.
- Objectif confirmé : Laisser le contrôle et ne pas imposer un contenu animé.
- Contrôle confirmé : Vérifier l’absence de démarrage automatique ou imprévisible.
- Limite publiée : Le cœur inclut contrôle et accessibilité, pas uniquement performance.
- URL : https://checklists.opquast.com/fr/qualite-numerique/124
- Provenance éditoriale : `sources/metier/conversation-opquast-performance.md`.
- Verdict : CONFIRMÉE.

## Règle 147

- Libellé confirmé : Le format des fichiers proposés en téléchargement est indiqué.
- Objectif confirmé : Savoir si les outils permettent la consultation et éviter les téléchargements inutiles.
- Contrôle confirmé : Vérifier l’information dans le lien ou son contexte.
- Limite publiée : Le format ne renseigne pas la taille.
- URL : https://checklists.opquast.com/fr/qualite-numerique/147
- Provenance éditoriale : `sources/metier/conversation-opquast-performance.md`.
- Verdict : CONFIRMÉE.

## Règle 148

- Libellé confirmé : La taille des fichiers internes proposés en téléchargement est indiquée.
- Objectif confirmé : Informer sur la quantité de données et permettre de différer en bas débit ou mobile.
- Contrôle confirmé : Vérifier l’information de poids dans le lien ou son contexte.
- Limite publiée : L’information ne réduit pas le volume.
- URL : https://checklists.opquast.com/fr/qualite-numerique/148
- Provenance éditoriale : `sources/metier/conversation-opquast-performance.md`.
- Verdict : CONFIRMÉE.

## Règle 226

- Libellé confirmé : Le serveur transmet des contenus compressés aux clients qui les acceptent.
- Objectif confirmé : Accélérer le rendu et réduire la bande passante.
- Contrôle confirmé : Vérifier la compression de HTML, CSS et JavaScript avec un outil dédié.
- Limite publiée : Les formats déjà compressés ne doivent pas être recompressés mécaniquement.
- URL : https://checklists.opquast.com/fr/qualite-numerique/226
- Provenance éditoriale : `sources/metier/conversation-opquast-performance.md`.
- Verdict : CONFIRMÉE.

## Règle 227

- Libellé confirmé : Le serveur envoie les informations permettant la mise en cache des contenus.
- Objectif confirmé : Accélérer l’affichage et réduire les coûts de bande passante.
- Contrôle confirmé : Vérifier la mise en cache des éléments liés, pas seulement de la page.
- Limite publiée : La présence d’informations ne garantit pas tous les réemplois.
- URL : https://checklists.opquast.com/fr/qualite-numerique/227
- Provenance éditoriale : `sources/metier/conversation-opquast-performance.md`.
- Verdict : CONFIRMÉE.

## Règle 229

- Libellé confirmé : Les feuilles de styles internes sont minifiées.
- Objectif confirmé : Réduire les données et accélérer l’affichage.
- Contrôle confirmé : Vérifier les CSS ou utiliser un outil de détection.
- Limite publiée : Minification et compression restent distinctes.
- URL : https://checklists.opquast.com/fr/qualite-numerique/229
- Provenance éditoriale : `sources/metier/conversation-opquast-performance.md`.
- Verdict : CONFIRMÉE.

## Règle 230

- Libellé confirmé : Les scripts internes sont minifiés.
- Objectif confirmé : Réduire les données et accélérer l’affichage.
- Contrôle confirmé : Vérifier les scripts ou utiliser un outil de détection.
- Limite publiée : Minification et compression restent distinctes.
- URL : https://checklists.opquast.com/fr/qualite-numerique/230
- Provenance éditoriale : `sources/metier/conversation-opquast-performance.md`.
- Verdict : CONFIRMÉE.

## Bilan

- Règles contrôlées : 9.
- Affirmations rejetées : 0.
- Contradictions persistantes : 0.
- Contenu métier importé depuis le MCP : 0.
