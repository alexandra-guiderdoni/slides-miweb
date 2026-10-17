# Notes orales étalons - Sécurité selon Opquast V5 - version 3

## Slide 01 - Ouverture

### Une chaîne de confiance plus large que HTTPS

- La présence de **HTTPS** répond à une question essentielle : les échanges entre le navigateur et le serveur sont-ils chiffrés ?
- Elle ne répond pas, à elle seule, aux questions qui concernent le **compte**, les **ressources chargées**, les informations révélées par le **serveur** ou les **courriels** envoyés au nom du service.
- Les 21 règles de la rubrique Sécurité construisent donc une chaîne de précautions observables, depuis l'arrivée sur le service jusqu'aux messages reçus hors de la page.
- Cette chaîne constitue un **socle de prévention**.
- Elle ne garantit pas la sécurité globale du système et ne remplace pas un audit de sécurité.

### Relier chaque règle à une preuve bornée

- Pour suivre cette chaîne sans confondre les mécanismes, chaque règle sera reliée à un risque, un contrôle et une limite.

## Slide 20 - Éclairage

### Une protection XSS actuelle et applicable

- Une attaque **XSS** cherche à faire exécuter dans une page un script qui n'aurait pas dû l'être.
- La règle 210 demande au serveur de transmettre une information explicite qui active ou renforce une protection côté navigateur.
- La fiche Opquast actuelle cite notamment une **Content Security Policy** adaptée, transmise dans les entêtes HTTP et applicable aux pages concernées.
- Elle précise aussi qu'il ne faut plus reposer sur `X-XSS-Protection`, mécanisme désormais considéré comme **obsolète ou déprécié**.
- La présence d'une CSP ne suffit pas : sa politique peut rester trop permissive ou ne pas couvrir la page réellement contrôlée.

### Contrôler l'encadrement de la page

- Après les scripts exécutés dans la page, examinons qui peut intégrer cette page dans un cadre.

## Slide 23 - Règle

### Vérifier le fichier réellement reçu

- Une origine autorisée peut servir aujourd'hui le fichier attendu, puis un fichier modifié demain.
- L'attribut `integrity` fournit au navigateur l'**empreinte cryptographique attendue** pour chaque ressource tierce appelée par un élément `script` ou `link`.
- `sha384` désigne ici une fonction de hachage.
- Ce n'est ni un chiffrement, ni un mot de passe, ni une information secrète.
- Le navigateur calcule l'empreinte du fichier reçu et la compare à celle déclarée dans la page.

#### Impact du non-respect

- Une ressource tierce modifiée peut diffuser ou exécuter un code qui n'était pas celui prévu lors de son intégration.
- Faire confiance au seul domaine d'origine ne permet pas de détecter cette modification du fichier.

#### Ce que garantit la règle

- Si les empreintes correspondent, le navigateur dispose d'une preuve que la ressource reçue correspond au contenu attendu.
- Si elles diffèrent, le navigateur refuse d'exécuter le script ou d'appliquer la feuille de styles concernée.
- Cette garantie porte uniquement sur la ressource associée à l'attribut `integrity` et sur l'empreinte déclarée.

### Réunir les autres preuves

- Il reste à réunir les preuves des entêtes et du code source sans confondre présence, validité et efficacité.

## Slide 30 - Synthèse

### Relier chaque règle à une action vérifiable

- **Protéger le parcours**, c'est sécuriser le canal, préserver la maîtrise du compte et donner au navigateur des instructions explicites.
- **Limiter l'exposition**, c'est éviter de révéler des fichiers ou des informations techniques inutiles.
- **Vérifier les preuves**, c'est contrôler le mécanisme réellement transmis, le parcours réellement utilisable et le message réellement reçu.
- Chaque résultat doit rester associé à son périmètre, à son instant d'observation et à ce qui demeure indéterminé.
- La responsabilité est distribuée entre infrastructure, produit, développement, éditorial, support, messagerie et DNS.

### Conclusion

- La sécurité Opquast devient concrète lorsqu'une règle est reliée à un risque utilisateur, à une preuve contrôlable, à une limite explicite et à un propriétaire capable d'agir.
