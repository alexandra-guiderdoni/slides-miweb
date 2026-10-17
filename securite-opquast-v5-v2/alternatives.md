# Alternatives textuelles - Sécurité selon Opquast V5 - version 2

Règles Opquast - Sécurité - Série Sécurité - version 2

## Slide 1 - La sécurité Opquast part du préjudice utilisateur

### Alternative textuelle

La sécurité Opquast part du préjudice utilisateur.

### Description détaillée du visuel

Une personne au centre ; autour d’elle, six boucliers sobres représentent les grappes documentées, sans personnage d’attaque.

### Message à retenir

Partir du risque concret évite de réduire la sécurité à la technique.

### Transcription

#### Textes et relations

- SÉCURITÉ SELON OPQUAST V5
- La sécurité Opquast, c’est d’abord prévenir des risques concrets pour l’utilisateur.
- Comprendre · Mémoriser · Préparer la certification
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 01 / 35

- Une personne au centre ; autour d’elle, six boucliers sobres représentent les grappes documentées, sans personnage d’attaque.

### Discours oral

#### Prévenir des préjudices concrets

- La **sécurité web** concerne les utilisateurs comme les administrateurs du service.
- Côté utilisateur, les risques incluent données interceptées, usurpations, arnaques et contenus dangereux.
- Côté organisation, une intrusion peut entraîner pertes de données, corrections coûteuses et perte de confiance.
- Opquast couvre un **socle de risques fondamentaux** reliés à des situations observables.

#### Un socle clairement délimité

- La formule affichée est le **fil conducteur éditorial** de cette série, pas une définition officielle d’Opquast.
- Ces règles préviennent des risques courants sans remplacer une démarche complète de cybersécurité.
- Commençons donc par situer cette frontière.

## Slide 2 - Un socle de prévention, pas une expertise cyber complète

### Alternative textuelle

Un socle de prévention, pas une expertise cyber complète.

### Description détaillée du visuel

Trois anneaux concentriques : socle Opquast, métiers numériques, expertise cyber spécialisée.

### Message à retenir

Opquast aide à ne pas ignorer des risques élémentaires ; il ne remplace pas les spécialistes.

### Transcription

#### Textes et relations

- UN SOCLE DE PRÉVENTION
- Risques fondamentaux
- Prévention transverse aux métiers
- Expertise spécialisée au-delà
- Opquast ne sécurise pas intégralement un système d’information.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 02 / 35

- Trois anneaux concentriques : socle Opquast, métiers numériques, expertise cyber spécialisée.

### Discours oral

#### Prévenir les risques fondamentaux

- Opquast fournit un **socle de prévention** pour repérer des risques élémentaires qui peuvent léser l’utilisateur.
- Ce socle donne des repères communs aux différents métiers numériques.
- Il aide à ne pas oublier des protections de base dans les parcours.
- Il ne constitue ni un audit complet ni une sécurisation intégrale du système d’information.

#### Savoir mobiliser une expertise spécialisée

- Une menace complexe ou un contexte sensible exige des compétences cyber dédiées.
- Le respect des règles ne prouve donc pas l’absence de vulnérabilité.
- Cette frontière permet d’organiser les règles autour des situations vécues par l’utilisateur.

## Slide 3 - Six situations structurent la série

### Alternative textuelle

Six situations structurent la série.

### Description détaillée du visuel

Six cartes égales reliées à un centre « Préjudice utilisateur » ; aucune hiérarchie ajoutée.

### Message à retenir

Les règles se mémorisent mieux quand elles répondent à une situation vécue.

### Transcription

#### Textes et relations

- SIX SITUATIONS UTILISATEUR
- Préjudice utilisateur
- Mes échanges sont interceptés
- Je perds le contrôle de mon compte
- Mon navigateur exécute l’inattendu
- Le service expose trop d’informations
- Je ne reconnais pas le vrai service
- Une opération sécurisée me bloque
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 03 / 35

- Six cartes égales reliées à un centre « Préjudice utilisateur » ; aucune hiérarchie ajoutée.

### Discours oral

#### Six situations de préjudice

- Une **interception** menace la confidentialité des échanges.
- La perte du compte prive l’utilisateur de son accès ou de sa maîtrise.
- Une ressource inattendue peut être exécutée par le navigateur.
- Des informations techniques exposées peuvent faciliter une attaque.
- Un site ou un courriel usurpé peut tromper sur l’origine du service.
- Un dispositif de sécurité inaccessible peut bloquer une opération légitime.

#### Un fil conducteur centré sur l’utilisateur

- Chaque groupe de règles répond à l’une de ces situations sans promettre une protection absolue.
- La première chaîne de défense concerne le transport, depuis HTTPS jusqu’à l’absence de contenu mixte.

## Slide 4 - HTTPS répond à quatre problèmes distincts

### Alternative textuelle

HTTPS répond à quatre problèmes distincts.

### Description détaillée du visuel

Quatre cartes numérotées autour d’un canal chiffré continu.

### Message à retenir

HTTPS, certificat, transport strict et contenu mixte répondent à quatre risques différents.

### Transcription

#### Textes et relations

- HTTPS : QUATRE QUESTIONS
- 197 · Toutes les pages en HTTPS
- 198 · Certificat signé et valide
- 199 · HTTPS imposé par HSTS
- 200 · Aucune ressource HTTP dans une page HTTPS
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 04 / 35

- Quatre cartes numérotées autour d’un canal chiffré continu.

### Discours oral

#### Quatre protections autour de HTTPS

- La **règle 197** impose HTTPS sur toutes les pages et leurs ressources.
- La **règle 198** exige des certificats signés et en cours de validité.
- La **règle 199** ajoute HSTS pour imposer au navigateur le transport sécurisé.
- La **règle 200** exclut les ressources HTTP d’une page servie en HTTPS.

#### Une chaîne, pas une exigence unique

- Ces règles ne sont pas interchangeables : elles traitent le chiffrement, le certificat, le chemin de connexion et le contenu mixte.
- En oublier une laisse subsister un risque ou une alerte distincte.
- Le premier maillon consiste à chiffrer tout le parcours avec HTTPS.

## Slide 5 - 197 : chiffrer tous les échanges

### Alternative textuelle

197 : chiffrer tous les échanges.

### Description détaillée du visuel

Navigateur et serveur reliés par un canal fermé ; données visibles seulement à l’intérieur.

### Message à retenir

La règle 197 protège le transport de toutes les pages.

### Transcription

#### Textes et relations

- RÈGLE 197
- Toutes les pages utilisent le protocole HTTPS.
- CHIFFRER LE TRANSPORT
- Prévenir l’interception et le vol de données pendant l’échange.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 05 / 35

- Navigateur et serveur reliés par un canal fermé ; données visibles seulement à l’intérieur.

### Discours oral

#### **Règle 197** : chiffrer tout le parcours

- **Règle 197 : « Toutes les pages utilisent le protocole HTTPS. »**
- Le chiffrement concerne chaque page et chaque ressource, pas seulement les formulaires.

##### Impact du non-respect

- Une ressource en HTTP peut exposer les échanges à une interception sur le réseau.
- L’utilisateur perd aussi un repère important de confiance.

##### Garantie apportée

- **Ce que garantit la règle** : les échanges entre navigateur et serveur sont chiffrés sur le réseau.
- Elle ne garantit ni l’identité absolue du service ni sa sécurité complète.

#### Vérifier ensuite le certificat

- Il faut encore contrôler la signature et la validité du certificat.

## Slide 6 - 198 : établir une connexion avec un certificat valide

### Alternative textuelle

198 : établir une connexion avec un certificat valide.

### Description détaillée du visuel

Certificat signé et daté placé à l’entrée du canal HTTPS ; aucune coche de sécurité absolue.

### Message à retenir

Le chiffrement ne dispense pas de vérifier la validité du certificat.

### Transcription

#### Textes et relations

- RÈGLE 198
- Les certificats de sécurité sont signés et en cours de validité.
- CERTIFICAT VALIDE
- Contribue à la sécurisation sans garantir une identité absolue.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 06 / 35

- Certificat signé et daté placé à l’entrée du canal HTTPS ; aucune coche de sécurité absolue.

### Discours oral

#### **Règle 198** : maintenir un certificat valide

- **Règle 198 : « Les certificats de sécurité sont signés et en cours de validité. »**
- Leur renouvellement doit être anticipé avant l’échéance.

##### Impact du non-respect

- Un certificat invalide ou périmé déclenche des alertes et peut interrompre la navigation.
- Le chiffrement seul ne suffit pas à établir un parcours de confiance.

##### Garantie apportée

- **Ce que garantit la règle** : l’utilisateur connaît la validité du certificat, ce qui contribue à sécuriser la transaction.
- Un certificat valide ne prouve pas irréfutablement l’identité du propriétaire.

#### Imposer ensuite le transport sécurisé

- HSTS ajoute une protection au-delà de la présence de HTTPS.

## Slide 7 - 199 : imposer le chemin HTTPS

### Alternative textuelle

199 : imposer le chemin HTTPS.

### Description détaillée du visuel

Deux routes HTTP et HTTPS ; la première est barrée, la seconde imposée.

### Message à retenir

HSTS rend le chemin sécurisé obligatoire pour le navigateur.

### Transcription

#### Textes et relations

- RÈGLE 199
- Les pages utilisant HTTPS ont un entête de transport strict.
- HSTS
- Le navigateur reste en HTTPS et n’essaie pas de repasser par HTTP.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 07 / 35

- Deux routes HTTP et HTTPS ; la première est barrée, la seconde imposée.

### Discours oral

#### **Règle 199** : imposer HTTPS avec HSTS

- **Règle 199 : « Les pages utilisant HTTPS ont un entête de transport strict. »**
- HSTS impose au navigateur compatible une connexion sécurisée.

##### Impact du non-respect

- Une tentative en HTTP peut rester exposée à une interception ou à un détournement.
- Des pages HTTPS ne suffisent donc pas à imposer ce chemin au navigateur.

##### Garantie apportée

- **Ce que garantit la règle** : les requêtes HTTP sont converties en HTTPS pendant la durée déclarée.
- La protection dépend de la prise en charge de HSTS par le navigateur.

#### Protéger toutes les ressources

- La page doit encore exclure les ressources chargées en HTTP.

## Slide 8 - 200 : supprimer le contenu mixte

### Alternative textuelle

200 : supprimer le contenu mixte.

### Description détaillée du visuel

Page HTTPS composée de ressources toutes marquées HTTPS ; une ressource HTTP est exclue.

### Message à retenir

Une page HTTPS reste fragile si elle charge encore des ressources HTTP.

### Transcription

#### Textes et relations

- RÈGLE 200
- Les pages utilisant le protocole HTTPS ne proposent pas de ressources HTTP.
- PAS DE CONTENU MIXTE
- Images, scripts et feuilles de style restent protégés.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 08 / 35

- Page HTTPS composée de ressources toutes marquées HTTPS ; une ressource HTTP est exclue.

### Discours oral

#### **Règle 200** : supprimer le contenu mixte

- **Règle 200 : « Les pages utilisant le protocole HTTPS ne proposent pas de ressources HTTP. »**
- Images, styles et scripts doivent être fournis en HTTPS.

##### Impact du non-respect

- Une ressource HTTP crée une faille potentielle dans une page chargée en HTTPS.
- Le navigateur peut afficher une alerte et interrompre la visite.

##### Garantie apportée

- **Ce que garantit la règle** : toutes les ressources de la page bénéficient du transport HTTPS.
- Elle évite le contenu mixte sans garantir l’intégrité du code reçu.

#### Passer de l’échange au compte

- La suite concerne les cinq moments de gestion d’un mot de passe.

## Slide 9 - Le mot de passe suit un cycle de maîtrise

### Alternative textuelle

Le mot de passe suit un cycle de maîtrise.

### Description détaillée du visuel

Cycle en cinq étapes, de la gestion à la protection du secret, sans flèche circulaire suggérant une répétition infinie.

### Message à retenir

Les cinq règles couvrent cinq moments différents, pas cinq variantes d’une même exigence.

### Transcription

#### Textes et relations

- LE CYCLE DU MOT DE PASSE
- 201 · Gérer en ligne
- 202 · Choisir ou changer
- 203 · Comprendre la robustesse
- 204 · Réinitialiser
- 205 · Ne jamais communiquer en clair
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 09 / 35

- Cycle en cinq étapes, de la gestion à la protection du secret, sans flèche circulaire suggérant une répétition infinie.

### Discours oral

#### Cinq moments de maîtrise

- La **règle 201** rend les opérations relatives au mot de passe réalisables en ligne.
- La **règle 202** permet de choisir ou changer son secret.
- La **règle 203** informe sur le degré de sécurisation du choix.
- La **règle 204** prévoit une réinitialisation en cas de perte.
- La **règle 205** interdit de communiquer le mot de passe en clair.

#### Des protections distinctes

- Disponibilité, choix, information, récupération et confidentialité répondent à cinq problèmes différents.
- Leur combinaison aide l’utilisateur à conserver l’accès et la maîtrise du compte.
- Les deux premières règles distinguent disponibilité du processus et maîtrise du mot de passe.

## Slide 10 - 201 et 202 : disponibilité puis maîtrise

### Alternative textuelle

201 et 202 : disponibilité puis maîtrise.

### Description détaillée du visuel

Diptyque : parcours intégralement en ligne à gauche, choix ou changement du mot de passe à droite.

### Message à retenir

Pouvoir gérer le processus et pouvoir choisir son secret sont deux besoins distincts.

### Transcription

#### Textes et relations

- 201 · TOUT GÉRER EN LIGNE
- Éviter une procédure hors ligne pénalisante.
- 202 · CHOISIR OU CHANGER
- Garder la maîtrise de son moyen d’authentification.
- Disponibilité du processus ≠ maîtrise du mot de passe
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 10 / 35

- Diptyque : parcours intégralement en ligne à gauche, choix ou changement du mot de passe à droite.

### Discours oral

#### Deux capacités complémentaires

- La **règle 201** rend intégralement possibles en ligne modification et réinitialisation du mot de passe.
- Elle évite des procédures hors ligne longues et sujettes à l’échec.
- La **règle 202** permet de choisir un mot de passe ou de changer celui généré par le service.
- Elle rend le moyen d’authentification plus maîtrisable par l’utilisateur.

#### Disponibilité ne signifie pas robustesse

- La première règle concerne l’accès au processus ; la seconde concerne le choix du secret.
- Aucune n’indique encore si le mot de passe choisi est suffisamment sécurisé.
- Cette information relève de la règle 203 et de son dispositif de sensibilisation.

## Slide 11 - 203 : informer sur la robustesse du choix

### Alternative textuelle

203 : informer sur la robustesse du choix.

### Description détaillée du visuel

Champ de mot de passe et jauge à trois niveaux, sans formulaire réaliste ni donnée personnelle.

### Message à retenir

La règle 203 vise d’abord la compréhension du risque associé au choix.

### Transcription

#### Textes et relations

- RÈGLE 203
- Un dispositif sensibilise l’utilisateur sur le degré de sécurisation du mot de passe qu’il choisit.
- FAIBLE · MOYEN · FORT
- Informer sur le risque, sans nécessairement interdire le choix.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 11 / 35

- Champ de mot de passe et jauge à trois niveaux, sans formulaire réaliste ni donnée personnelle.

### Discours oral

#### **Règle 203** : rendre le risque perceptible

- **Règle 203 : « Un dispositif sensibilise l’utilisateur sur le degré de sécurisation du mot de passe qu’il choisit. »**
- Le retour apparaît avant la soumission du formulaire.

##### Impact du non-respect

- Sans indication, l’utilisateur perçoit mal le risque d’un mot de passe faible.
- Il peut conserver un choix devinable sans être alerté.

##### Garantie apportée

- **Ce que garantit la règle** : le degré de sécurisation du mot de passe est indiqué pendant le choix.
- Le dispositif informe sans devoir bloquer la création du compte.

#### Retrouver l’accès sans divulguer

- La maîtrise continue avec la réinitialisation et l’interdiction d’envoyer le secret en clair.

## Slide 12 - 204 et 205 : réinitialiser sans divulguer

### Alternative textuelle

204 et 205 : réinitialiser sans divulguer.

### Description détaillée du visuel

Flux en trois étapes : lien temporaire, procédure en ligne, nouveau mot de passe ; ancien secret verrouillé.

### Message à retenir

Reprendre la main ne doit jamais conduire à renvoyer le mot de passe en clair.

### Transcription

#### Textes et relations

- 204 · RÉINITIALISER
- Créer un nouveau mot de passe.
- 205 · NE JAMAIS COMMUNIQUER EN CLAIR
- Un lien temporaire mène à la procédure en ligne.
- Réinitialiser ≠ restituer l’ancien secret
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 12 / 35

- Flux en trois étapes : lien temporaire, procédure en ligne, nouveau mot de passe ; ancien secret verrouillé.

### Discours oral

#### Réinitialiser sans restituer

- La **règle 204** permet de créer un nouveau mot de passe après une perte.
- La procédure doit être disponible sans authentification et réalisable en ligne.
- Elle ne consiste pas à renvoyer le mot de passe actuel.
- La **règle 205** interdit sa communication en clair par courriel.

#### Restaurer l’accès sans exposer le mot de passe

- Un lien temporaire peut conduire vers la procédure de renouvellement en ligne.
- Cette séparation limite le risque d’interception.
- L’utilisateur reprend la main sans que le service révèle son ancien mot de passe.
- Des règles hors de la rubrique Sécurité complètent ensuite cette protection.

## Slide 13 - Le contrôle du compte dépasse la rubrique Sécurité

### Alternative textuelle

Le contrôle du compte dépasse la rubrique Sécurité.

### Description détaillée du visuel

Cinq cartes autour d’un compte utilisateur, avec la mention « lien matériel direct ».

### Message à retenir

Des règles classées ailleurs réduisent matériellement l’usurpation, l’exposition ou le blocage.

### Transcription

#### Textes et relations

- SÉCURITÉ DU COMPTE — HORS RUBRIQUE
- 18 · Confirmer la création
- 19 · Prévenir l’usurpation
- 23 · Pouvoir se déconnecter
- 26 · Ne pas exposer l’existence d’un compte
- 96 · Pouvoir relancer la double authentification
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 13 / 35

- Cinq cartes autour d’un compte utilisateur, avec la mention « lien matériel direct ».

### Discours oral

#### Le compte se protège au-delà d’une rubrique

- **Règle 18** : une confirmation évite l’activation à l’insu de l’utilisateur.
- **Règle 19** : une authentification forte contribue à prévenir l’usurpation.
- **Règle 23** : la déconnexion globale permet de fermer les sessions actives.
- **Règle 26** : les réponses ne révèlent pas si un compte existe.
- **Règle 96** : le code de double authentification peut être renvoyé.
- Ces règles appartiennent à d’autres rubriques, mais protègent matériellement le même parcours.

#### Maintenir la maîtrise de l’accès

- Confirmation, authentification, déconnexion, discrétion et relance réduisent des risques différents.
- La sécurité doit ensuite rester utilisable par la personne légitime.

## Slide 14 - La sécurité doit laisser passer l’utilisateur légitime

### Alternative textuelle

La sécurité doit laisser passer l’utilisateur légitime.

### Description détaillée du visuel

Deux accès parallèles : attaque arrêtée, utilisateur légitime admis par un moyen prévu.

### Message à retenir

Une sécurité inutilisable peut exclure la personne qu’elle doit protéger.

### Transcription

#### Textes et relations

- EMPÊCHER L’ATTAQUANT
- SANS BLOQUER L’UTILISATEUR LÉGITIME
- 17 · Alternative à l’identification tierce
- 75 · Prévenir les erreurs de saisie
- 76 · Afficher le mot de passe
- 92 · Autoriser le copier-coller
- 96 et 215 · Prévoir une relance ou un autre moyen
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 14 / 35

- Deux accès parallèles : attaque arrêtée, utilisateur légitime admis par un moyen prévu.

### Discours oral

#### Une protection doit rester praticable

- **Règle 17** : créer un compte reste possible sans imposer un service d’identification tiers.
- **Règle 75** : un mécanisme prévient les erreurs lors de la création du mot de passe.
- **Règle 76** : les caractères saisis peuvent être affichés en clair.
- **Règle 92** : le copier-coller reste possible, y compris dans les champs de mot de passe.
- **Règles 96 et 215** : relance et moyens alternatifs réduisent les blocages.

#### Ne pas opposer sécurité et usage

- Ces dispositions aident l’utilisateur légitime sans définir seules la robustesse de l’authentification.
- Le contrôle suivant porte sur la façon dont le navigateur interprète les ressources.

## Slide 15 - 206 et 207 : déclarer puis ne pas deviner

### Alternative textuelle

206 et 207 : déclarer puis ne pas deviner.

### Description détaillée du visuel

Un fichier reçoit une étiquette Content-Type, puis un panneau « nosniff » bloque la devinette.

### Message à retenir

Le serveur annonce la nature du fichier et le navigateur respecte cette annonce.

### Transcription

#### Textes et relations

- TYPE MIME : UNE PAIRE
- 207 · Le serveur déclare le type de chaque ressource.
- 206 · Le navigateur ne cherche pas à deviner autre chose.
- Content-Type + X-Content-Type-Options: nosniff
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 15 / 35

- Un fichier reçoit une étiquette Content-Type, puis un panneau « nosniff » bloque la devinette.

### Discours oral

#### **Règles 206 et 207** : déclarer le type sans le deviner

- **Règle 207** : le serveur fournit un entête Content-Type adapté à chaque ressource.
- **Règle 206** : l’entête X-Content-Type-Options avec la valeur nosniff désactive la détection automatique.

##### Impact du non-respect

- Un contenu dangereux peut être dissimulé sous une nature trompeuse.
- Le navigateur risque alors d’interpréter une ressource autrement que prévu.

##### Garantie apportée

- **Ce que garantissent les règles** : le type MIME est annoncé et cette annonce est respectée.
- Elles ne contrôlent ni l’origine ni l’intégrité de la ressource.

#### Contrôler ensuite l’exécution

- La règle 210 active une protection explicite contre les attaques XSS.

## Slide 16 - 210 : limiter l’exécution d’un contenu injecté

### Alternative textuelle

210 : limiter l’exécution d’un contenu injecté.

### Description détaillée du visuel

Contenu injecté arrêté à l’entrée d’une page par une politique de protection.

### Message à retenir

La règle 210 cible l’injection puis l’exécution d’un contenu malveillant.

### Transcription

#### Textes et relations

- RÈGLE 210
- Le serveur envoie les informations d’activation de protection cross site scripting.
- MENACE : CONTENU INJECTÉ
- Un mécanisme explicite de protection est transmis au navigateur.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 16 / 35

- Contenu injecté arrêté à l’entrée d’une page par une politique de protection.

### Discours oral

#### **Règle 210** : transmettre une protection contre les XSS

- **Règle 210 : « Le serveur envoie les informations d’activation de protection cross site scripting. »**
- Une politique CSP adaptée peut constituer ce mécanisme explicite.

##### Impact du non-respect

- Le navigateur dispose de moins de moyens pour limiter l’exécution de scripts non autorisés.
- Un contenu injecté peut produire un comportement malveillant.

##### Garantie apportée

- **Ce que garantit la règle** : le serveur transmet une protection reconnue et maintenue contre les XSS.
- Elle ne prouve pas que l’application est exempte de toute vulnérabilité.

#### Contrôler l’encadrement

- La règle 211 traite l’intégration de la page dans un cadre tiers.

## Slide 17 - 211 : contrôler qui peut encadrer la page

### Alternative textuelle

211 : contrôler qui peut encadrer la page.

### Description détaillée du visuel

La vraie page est placée dans un cadre ; seuls les domaines autorisés passent.

### Message à retenir

La règle 211 vise l’intégration trompeuse de la page dans un cadre tiers.

### Transcription

#### Textes et relations

- RÈGLE 211
- Le serveur indique les domaines autorisés à intégrer ses pages dans des cadres.
- QUI PEUT M’ENCADRER ?
- X-Frame-Options ou CSP frame-ancestors
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 17 / 35

- La vraie page est placée dans un cadre ; seuls les domaines autorisés passent.

### Discours oral

#### **Règle 211** : limiter l’intégration dans des cadres

- **Règle 211 : « Le serveur envoie les informations indiquant les domaines autorisés à intégrer ses pages dans des cadres. »**
- X-Frame-Options ou CSP frame-ancestors peuvent porter cette politique.

##### Impact du non-respect

- Un domaine non autorisé peut intégrer la page et présenter son contenu de manière trompeuse.
- L’utilisateur risque d’agir dans une interface au contexte ambigu.

##### Garantie apportée

- **Ce que garantit la règle** : une politique explicite limite ou interdit l’intégration en cadre.
- Elle ne contrôle pas les origines des ressources chargées.

#### Restreindre les sources

- Cette autre fonction relève de la règle 212.

## Slide 18 - 212 : restreindre l’origine des contenus

### Alternative textuelle

212 : restreindre l’origine des contenus.

### Description détaillée du visuel

Une page reçoit quatre types de ressources depuis une liste d’origines autorisées ; les autres sont écartées.

### Message à retenir

La règle 212 contrôle les origines autorisées des ressources chargées.

### Transcription

#### Textes et relations

- RÈGLE 212
- Un mécanisme de sécurité restreint l’origine des contenus.
- D’OÙ PUIS-JE CHARGER ?
- Scripts · CSS · Images · Polices
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 18 / 35

- Une page reçoit quatre types de ressources depuis une liste d’origines autorisées ; les autres sont écartées.

### Discours oral

#### **Règle 212** : restreindre l’origine des contenus

- **Règle 212 : « Un mécanisme de sécurité restreint l’origine des contenus. »**
- Une politique CSP peut définir les sources autorisées pour scripts, styles, images et polices.

##### Impact du non-respect

- La page peut exécuter ou afficher un contenu indésirable provenant d’une source non autorisée.
- Le navigateur ne dispose pas de la restriction attendue pour chaque famille de ressources.

##### Garantie apportée

- **Ce que garantit la règle** : les origines permises sont explicitement limitées.
- Elle ne vérifie pas qu’un fichier autorisé est resté intact.

#### Vérifier le fichier reçu

- La règle 214 complète ce contrôle par une empreinte d’intégrité.

## Slide 19 - 214 : contrôler l’intégrité d’une ressource tierce

### Alternative textuelle

214 : contrôler l’intégrité d’une ressource tierce.

### Description détaillée du visuel

Deux empreintes comparées ; l’exécution n’est permise qu’en cas d’égalité.

### Message à retenir

Une origine autorisée ne garantit pas que le fichier tiers est resté inchangé.

### Transcription

#### Textes et relations

- RÈGLE 214
- Le contrôle d’intégrité des ressources tierces est présent et valide.
- EST-CE TOUJOURS LE FICHIER ATTENDU ?
- Empreinte reçue = empreinte attendue
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 19 / 35

- Deux empreintes comparées ; l’exécution n’est permise qu’en cas d’égalité.

### Discours oral

#### **Règle 214** : vérifier l’intégrité d’une ressource tierce

- **Règle 214 : « Le contrôle d’intégrité des ressources tierces est présent et valide. »**
- L’attribut integrity fournit le hachage attendu pour chaque script ou feuille de style externe.

##### Impact du non-respect

- Une ressource tierce modifiée peut être exécutée ou appliquée sans contrôle de son empreinte.
- Du code malveillant peut ainsi être diffusé depuis une origine pourtant autorisée.

##### Garantie apportée

- **Ce que garantit la règle** : le navigateur compare la ressource reçue au hachage déclaré.
- Elle ne décide pas quelles origines sont autorisées.

#### Réduire les informations exposées

- Les règles 209 et 213 limitent deux divulgations inutiles.

## Slide 20 - 209 et 213 : ne pas renseigner une attaque

### Alternative textuelle

209 et 213 : ne pas renseigner une attaque.

### Description détaillée du visuel

Deux panneaux d’information serveur se ferment avant exposition publique.

### Message à retenir

Une information sans utilité utilisateur n’a pas à faciliter la préparation d’une attaque.

### Transcription

#### Textes et relations

- NE PAS EXPOSER L’INUTILE
- 209 · Pas de liste de fichiers sans page d’index
- 213 · Pas d’informations sur logiciels et langages
- Inutile pour l’utilisateur · Utile à un attaquant
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 20 / 35

- Deux panneaux d’information serveur se ferment avant exposition publique.

### Discours oral

#### **Règles 209 et 213** : limiter les informations exposées

- **Règle 209** : un répertoire sans page d’index ne liste pas ses fichiers.
- **Règle 213** : les entêtes ne révèlent pas les technologies utilisées côté serveur.

##### Impact du non-respect

- Une liste peut exposer des ressources qui ne devaient pas être parcourues.
- Des technologies révélées peuvent faciliter la préparation d’une intrusion.

##### Garantie apportée

- **Ce que garantissent les règles** : ces deux sources d’information ne sont pas communiquées.
- Elles ne corrigent pas une vulnérabilité et ne rendent pas le serveur invisible.

#### Informer sans confondre

- La règle 208 concerne l’information fournie à l’utilisateur.

## Slide 21 - 208 : informer n’est pas sécuriser

### Alternative textuelle

208 : informer n’est pas sécuriser.

### Description détaillée du visuel

Deux couches séparées : mécanisme technique dessous, information compréhensible dessus.

### Message à retenir

La règle 208 porte sur l’information relative à la sécurisation, pas sur le mécanisme lui-même.

### Transcription

#### Textes et relations

- RÈGLE 208
- Les informations sur la sécurité des transactions sont indiquées.
- INFORMATION ≠ MÉCANISME
- Indiquer le mode ou le niveau de sécurisation à l’utilisateur.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 21 / 35

- Deux couches séparées : mécanisme technique dessous, information compréhensible dessus.

### Discours oral

#### **Règle 208** : informer sur la sécurité des transactions

- **Règle 208 : « Les informations sur la sécurité des transactions sont indiquées. »**
- Le mode et le niveau de chiffrement peuvent figurer dans une aide ou une foire aux questions.

##### Impact du non-respect

- L’utilisateur manque d’informations sur la sécurisation des échanges de données sensibles.
- Il ne sait pas où retrouver ces indications dans son navigateur.

##### Garantie apportée

- **Ce que garantit la règle** : l’information sur le mécanisme de sécurisation reste accessible.
- Elle ne prouve pas que la transaction est correctement sécurisée.

#### Préserver la continuité

- La règle 215 évite qu’un seul moyen bloque l’opération.

## Slide 22 - 215 : deux chemins, pas deux facteurs

### Alternative textuelle

215 : deux chemins, pas deux facteurs.

### Description détaillée du visuel

Une opération sécurisée est accessible par deux chemins alternatifs ; un encart distinct montre la 2FA.

### Message à retenir

La règle 215 protège la continuité de l’opération, elle ne définit pas la double authentification.

### Transcription

#### Textes et relations

- RÈGLE 215
- Les opérations sécurisées peuvent être validées par au moins deux moyens.
- 2FA · Deux preuves
- 215 · Deux chemins possibles
- Une solution de secours sécurisée évite le blocage.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 22 / 35

- Une opération sécurisée est accessible par deux chemins alternatifs ; un encart distinct montre la 2FA.

### Discours oral

#### **Règle 215** : proposer au moins deux moyens de validation

- **Règle 215 : « Les opérations sécurisées peuvent être validées par au moins deux moyens. »**
- L’utilisateur peut choisir, par exemple, entre un SMS et un terminal de validation.

##### Impact du non-respect

- L’indisponibilité d’un dispositif peut bloquer une opération légitime.
- Cette dépendance peut entraîner échec, abandon ou exclusion.

##### Garantie apportée

- **Ce que garantit la règle** : un autre mécanisme permet de valider l’opération sécurisée.
- Elle ne demande pas deux preuves simultanées et ne définit pas la double authentification.

#### Rendre l’origine visible

- La règle 216 maintient la barre d’adresse comme repère.

## Slide 23 - 216 : toujours savoir où je suis

### Alternative textuelle

216 : toujours savoir où je suis.

### Description détaillée du visuel

Deux fenêtres identiques ; seule la barre d’adresse permet de distinguer le domaine attendu du domaine frauduleux.

### Message à retenir

La barre d’adresse donne un repère extérieur au contenu imitable de la page.

### Transcription

#### Textes et relations

- RÈGLE 216
- L’affichage de la barre d’adresse du navigateur n’est pas bloqué.
- DANS LA PAGE : LE GRAPHISME PEUT ÊTRE COPIÉ
- DANS LA BARRE : JE VÉRIFIE OÙ JE SUIS
- Protocole · Certificat · Nom de domaine
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 23 / 35

- Deux fenêtres identiques ; seule la barre d’adresse permet de distinguer le domaine attendu du domaine frauduleux.

### Discours oral

#### **Règle 216** : conserver la barre d’adresse visible

- **Règle 216 : « L’affichage de la barre d’adresse du navigateur n’est pas bloqué. »**
- Ce repère montre le protocole, le certificat et le domaine.

##### Impact du non-respect

- Sans barre d’adresse, l’utilisateur ne voit plus où il se trouve.
- Une interface copiée peut faciliter l’usurpation ou le vol d’identifiants.

##### Garantie apportée

- **Ce que garantit la règle** : la fenêtre conserve une barre d’adresse visible.
- Elle n’assure pas que l’utilisateur l’examine ni que le service est légitime.

#### Contrôler les courriels

- La règle 217 concerne ensuite le domaine de messagerie.

## Slide 24 - 217 : authentifier le domaine de messagerie

### Alternative textuelle

217 : authentifier le domaine de messagerie.

### Description détaillée du visuel

Un courriel traverse trois contrôles SPF, DKIM et DMARC avant d’atteindre l’utilisateur.

### Message à retenir

L’authentification du domaine aide à vérifier l’origine revendiquée d’un courriel.

### Transcription

#### Textes et relations

- RÈGLE 217
- Le domaine de messagerie est authentifié.
- SPF · Serveurs autorisés
- DKIM · Signature du message
- DMARC · Politique et rapports
- Réduire faux courriels, phishing et usurpation
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 24 / 35

- Un courriel traverse trois contrôles SPF, DKIM et DMARC avant d’atteindre l’utilisateur.

### Discours oral

#### **Règle 217** : authentifier le domaine de messagerie

- **Règle 217 : « Le domaine de messagerie est authentifié. »**
- SPF liste les serveurs autorisés, DKIM signe les messages et DMARC définit une politique avec des rapports.

##### Impact du non-respect

- Des courriels frauduleux peuvent plus facilement usurper le domaine du service.
- Les messages légitimes risquent aussi une délivrabilité et une réputation dégradées.

##### Garantie apportée

- **Ce que garantit la règle** : SPF, DKIM et DMARC sont présents et correctement configurés.
- Elle réduit l’usurpation sans garantir l’authenticité de chaque message reçu.

#### Relier site et messagerie

- Barre d’adresse et authentification du domaine fournissent deux indices complémentaires d’origine.

## Slide 25 - 216 et 217 : reconnaître le vrai service

### Alternative textuelle

216 et 217 : reconnaître le vrai service.

### Description détaillée du visuel

Diptyque navigateur et courriel reliés par la question « Est-ce vraiment le bon service ? ».

### Message à retenir

Site et courriel donnent deux points de contrôle complémentaires sur l’origine du service.

### Transcription

#### Textes et relations

- RECONNAÎTRE LE VRAI SERVICE
- 216 · Est-ce vraiment le site auquel je crois parler ?
- 217 · Est-ce vraiment le service qui m’envoie ce courriel ?
- Usurpation et ingénierie sociale
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 25 / 35

- Diptyque navigateur et courriel reliés par la question « Est-ce vraiment le bon service ? ».

### Discours oral

#### Reconnaître l’origine dans deux contextes

- La règle **216** maintient la barre d’adresse visible pour examiner le protocole, le certificat et le domaine du site.
- La règle **217** authentifie le domaine de messagerie grâce aux contrôles SPF, DKIM et DMARC.
- Ces repères se trouvent hors du contenu graphique, qui peut être imité.
- Le premier concerne la navigation web ; le second concerne l’infrastructure d’envoi des courriels.

#### Une complémentarité contre l’usurpation

- Ensemble, ils réduisent les risques de phishing, d’usurpation et de manipulation.
- Ils ne rendent pas automatiquement chaque page ou message fiable, mais restaurent des indices vérifiables.
- Cette distinction conduit au recouvrement entre sécurité et vie privée.

## Slide 26 - Sécurité et privacy : quatre zones de recouvrement

### Alternative textuelle

Sécurité et privacy : quatre zones de recouvrement.

### Description détaillée du visuel

Deux cercles Security et Privacy se recouvrent sur quatre règles ; frontières nettes.

### Message à retenir

Les deux disciplines se recouvrent sans devenir interchangeables.

### Transcription

#### Textes et relations

- ANNEXE · SÉCURITÉ ET PRIVACY
- 25 · Politique de referrers
- 27 · Échanges de données sensibles sécurisés
- 28 · Aucune donnée sensible en clair dans l’URL
- 60 · Modifier ou supprimer les données bancaires mémorisées
- Privacy : quelles données et quelle maîtrise ?
- Sécurité : empêcher interception, détournement ou exploitation.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 26 / 35

- Deux cercles Security et Privacy se recouvrent sur quatre règles ; frontières nettes.

### Discours oral

#### Sécurité et vie privée se recouvrent

- La règle **25** maîtrise les informations de navigation transmises par les referrers.
- La règle **27** sécurise les échanges de données sensibles et les signale comme tels.
- La règle **28** empêche leur transmission en clair dans les URL.
- La règle **60** permet de modifier ou supprimer les données bancaires mémorisées.
- Ces quatre règles protègent des données contre la divulgation, l’interception ou la fraude.

#### Des finalités à maintenir distinctes

- La vie privée interroge les données collectées et leur maîtrise ; la sécurité prévient leur exploitation ou leur détournement.
- Le recouvrement est réel, mais il ne transforme pas ces disciplines en une seule rubrique.

## Slide 27 - Le périmètre transversal reste gradué

### Alternative textuelle

Le périmètre transversal reste gradué.

### Description détaillée du visuel

Quatre bandes graduées, sans présenter les catégories analytiques comme officielles.

### Message à retenir

La relation avec la sécurité peut être officielle, directe, liée à l’utilisabilité ou secondaire.

### Transcription

#### Textes et relations

- CARTE DU PÉRIMÈTRE
- Sécurité officielle · 197 à 217
- Lien direct hors rubrique · 18, 19, 23, 25, 26, 27, 28, 60, 96, 173
- Sécurité par l’utilisabilité · 75, 76, 92
- Satellites documentés · 14, 17, 22, 97, 172
- Tout n’est pas une « règle de sécurité ».
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 27 / 35

- Quatre bandes graduées, sans présenter les catégories analytiques comme officielles.

### Discours oral

#### Une carte graduée des liens avec la sécurité

- Les règles **197 à 217** constituent la rubrique officielle Sécurité.
- Les règles citées comme liens directs concernent le compte, les données sensibles ou la fraude.
- Les règles 75, 76 et 92 relient sécurité et **utilisabilité** autour des mots de passe.
- Les autres satellites cités apportent un effet ou un contexte de sécurité plus secondaire.

#### Une distinction éditoriale, pas officielle

- Cette graduation explique la proximité entre règles sans modifier leur thématique dans le référentiel.
- Une règle peut contribuer à la prévention sans devenir une règle de la rubrique Sécurité.
- Le vocabulaire permet maintenant de distinguer précisément ces mécanismes.

## Slide 28 - Huit termes structurent le vocabulaire sécurité

### Alternative textuelle

Huit termes structurent le vocabulaire sécurité.

### Description détaillée du visuel

Huit cartes terminologiques égales, sans définitions supplémentaires.

### Message à retenir

Le vocabulaire relie disponibilité, authentification, origine, intégrité et nature des ressources.

### Transcription

#### Textes et relations

- GLOSSAIRE SÉCURITÉ
- Attaque par déni de service
- Authentification à double facteur
- Barre d’adresse du navigateur
- Contrôle d’intégrité
- Domaine de messagerie du site
- Entête de transport strict
- Opération sécurisée
- Type MIME
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 28 / 35

- Huit cartes terminologiques égales, sans définitions supplémentaires.

### Discours oral

#### Huit termes pour distinguer les mécanismes

- Le **déni de service** concerne la disponibilité ; la double authentification demande deux preuves distinctes.
- La barre d’adresse et le domaine de messagerie fournissent des repères sur l’origine du service.
- L’entête de transport strict force le navigateur à utiliser HTTPS.
- Le contrôle d’intégrité compare l’empreinte reçue à celle attendue.
- Une opération sécurisée exige des mesures adaptées ; le type MIME identifie le format d’une donnée.

#### Du mot à la règle

- Ce vocabulaire distingue transport, identité, disponibilité, nature et intégrité des ressources.
- Le glossaire facilite la compréhension des règles sans créer d’exigence supplémentaire.
- Cette précision prépare une lecture transversale avec le modèle VPTCS.

## Slide 29 - VPTCS traverse la sécurité

### Alternative textuelle

VPTCS traverse la sécurité.

### Description détaillée du visuel

Pentagone VPTCS avec les règles associées ; badge explicite « lecture analytique ».

### Message à retenir

La sécurité traverse VPTCS, mais cette association reste une lecture analytique.

### Transcription

#### Textes et relations

- LECTURE VPTCS — ANALYSE, PAS CLASSEMENT OFFICIEL
- Visibilité · 216, 217
- Perception · 203, 208
- Technique · 197–200, 206, 207, 209–214
- Contenus · 208
- Services · 201–205, 215, 96
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 29 / 35

- Pentagone VPTCS avec les règles associées ; badge explicite « lecture analytique ».

### Discours oral

#### VPTCS offre cinq angles de lecture

- Le modèle distingue **visibilité, perception, technique, contenus et services**.
- La visibilité éclaire ici les règles 216 et 217 sur l’origine du site et des courriels.
- La perception relie 203 et 208 à l’information fournie à l’utilisateur.
- La technique rassemble les mécanismes HTTPS, MIME, exposition, injection, origine et intégrité.
- Les contenus et services couvrent notamment l’information de sécurité, le compte et la continuité des opérations.

#### Une association strictement analytique

- Cette répartition soutient la compréhension, mais ne constitue pas un classement officiel des règles.
- Une même règle peut éclairer plusieurs dimensions selon le risque étudié.
- La transversalité conduit ensuite du contrôle opérationnel au pilotage.

## Slide 30 - De la règle au pilotage de la sécurité

### Alternative textuelle

De la règle au pilotage de la sécurité.

### Description détaillée du visuel

Chaîne sobre de quatre niveaux : règle, test, production, pilotage QSE-IP.

### Message à retenir

Le livre relie le socle de règles aux pratiques de production et au management intégré.

### Transcription

#### Textes et relations

- DU RÉFÉRENTIEL AU PILOTAGE
- Tests de sécurité
- Qualité logicielle
- DevSecOps
- QSE-IP
- Qualité · Sécurité · Environnement · Inclusion · Privacy
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 30 / 35

- Chaîne sobre de quatre niveaux : règle, test, production, pilotage QSE-IP.

### Discours oral

#### Sortir du traitement en silos

- Les règles Opquast donnent un **socle opérationnel**, mais les risques numériques traversent toute l’organisation.
- L’approche **QSE-IP** rapproche qualité, sécurité, environnement, inclusion et vie privée dans le pilotage.
- Elle ne fusionne pas ces expertises et ne réduit pas leurs exigences propres.
- Elle permet de partager priorités, moyens et décisions entre des équipes souvent séparées.

#### Relier contrôle et management

- Les tests de sécurité et les pratiques de production restent nécessaires pour appliquer les règles.
- Le pilotage intégré ajoute une responsabilité de management aux pratiques techniques et opérationnelles.
- Cette perspective conduit à observer comment la place de la sécurité évolue.

## Slide 31 - La sécurité Opquast évolue avec les risques

### Alternative textuelle

La sécurité Opquast évolue avec les risques.

### Description détaillée du visuel

Chronologie horizontale sobre de 2009 à 2026 ; l’IA reste le dernier jalon, sans robot décoratif.

### Message à retenir

La place de la sécurité s’élargit sans transformer Opquast en référentiel cyber complet.

### Transcription

#### Textes et relations

- ÉVOLUTION DOCUMENTÉE
- 2009–2010 · La sécurité devient un grand sujet
- 2020 · Séparation Sécurité / Données personnelles
- 2023 · QSE-IP
- 2024 · Transversalité renforcée
- 2025 · Nouvelles règles 26, 96, 216, 217
- 2026 · Risques du code et des attaques renforcés par l’IA
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 31 / 35

- Chronologie horizontale sobre de 2009 à 2026 ; l’IA reste le dernier jalon, sans robot décoratif.

### Discours oral

#### La sécurité gagne en transversalité

- La source situe en 2009-2010 l’entrée explicite de la sécurité dans le référentiel.
- En 2020, la thématique Données personnelles est séparée de la rubrique Sécurité.
- En 2023, la démarche **QSE-IP** propose un management intégré des risques numériques.
- En 2024, les publications Opquast insistent sur la pensée transversale.
- En 2025, la version 5 introduit notamment les règles 26, 96, 216 et 217.
- Le jalon éditorial 2026 attire l’attention sur les risques liés au code et aux attaques renforcées par l’IA.

#### Une chronologie, pas une extension illimitée

- Cette évolution élargit la lecture des risques sans transformer Opquast en référentiel cyber complet.
- La limite du socle reste essentielle.

## Slide 32 - Savoir où s’arrête le socle Opquast

### Alternative textuelle

Savoir où s’arrête le socle Opquast.

### Description détaillée du visuel

Frontière nette entre socle Opquast et démarche spécialisée ; aucune opposition caricaturale.

### Message à retenir

Connaître les règles implique aussi de connaître leur limite.

### Transcription

#### Textes et relations

- OPQUAST FOURNIT UN SOCLE
- Repérer des risques fondamentaux
- Connaître une prévention générale
- Mobiliser une expertise spécialisée quand nécessaire
- OPQUAST NE GARANTIT PAS
- La sécurisation intégrale d’un système d’information
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 32 / 35

- Frontière nette entre socle Opquast et démarche spécialisée ; aucune opposition caricaturale.

### Discours oral

#### Un socle de prévention

- Le guide couvre les types MIME, les politiques CSP, les referrers et les mots de passe.
- Chaque règle associe une situation observable à un objectif de prévention et à un contrôle.
- Ce **socle** aide les professionnels à repérer un risque et à engager une première action.
- Les enjeux critiques exigent encore des compétences, des tests et une organisation spécialisés.

#### Ce que la maîtrise des règles ne prouve pas

- Respecter la checklist ne démontre pas la sécurisation intégrale d’un système d’information.
- Le référentiel ne remplace ni la veille permanente ni une analyse adaptée au contexte.
- Connaître la limite permet de mobiliser l’expertise nécessaire.

## Slide 33 - Pièges de certification : transport, mots de passe et MIME

### Alternative textuelle

Pièges de certification : transport, mots de passe et MIME.

### Description détaillée du visuel

Cinq cartes de révision avec signes de distinction, sans quiz ajouté.

### Message à retenir

Les confusions portent souvent sur des règles voisines qui répondent à des problèmes différents.

### Transcription

#### Textes et relations

- PIÈGES DE CERTIFICATION · 1/2
- 197–200 · Quatre problèmes HTTPS distincts
- 206–207 · Déclarer et ne pas deviner
- 201–205 · Cinq moments du mot de passe
- 204 ≠ 205 · Réinitialiser sans divulguer
- Sécurité et Privacy restent distinctes
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 33 / 35

- Cinq cartes de révision avec signes de distinction, sans quiz ajouté.

### Discours oral

#### Distinguer des règles voisines

- Les règles **197 à 200** distinguent HTTPS partout, validité du certificat, transport strict et absence de ressources HTTP.
- Les règles **201 à 205** couvrent cinq moments différents de la gestion du mot de passe.
- La règle 204 permet la réinitialisation, tandis que 205 interdit de communiquer le secret en clair.
- La règle 207 déclare le type MIME ; 206 empêche le navigateur d’en deviner un autre.

#### Retenir le problème traité

- Un numéro devient plus facile à retrouver lorsque le risque associé est nommé.
- La sécurité et la vie privée peuvent se recouvrir sans devenir interchangeables.
- Les autres contrôles se distinguent par la menace ou la fonction traitée.

## Slide 34 - Pièges de certification : contrôles et continuité

### Alternative textuelle

Pièges de certification : contrôles et continuité.

### Description détaillée du visuel

Matrice de sept distinctions avec libellés très courts et espaces généreux.

### Message à retenir

Nommer la menace ou la fonction évite d’intervertir les règles.

### Transcription

#### Textes et relations

- PIÈGES DE CERTIFICATION · 2/2
- 210 · Injection
- 211 · Encadrement
- 212 · Origine
- 214 · Intégrité
- 208 · Informer, pas sécuriser à elle seule
- 215 · Deux moyens, pas deux facteurs
- 216 · Site · 217 · Courriel
- Aucune sécurité absolue
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 34 / 35

- Matrice de sept distinctions avec libellés très courts et espaces généreux.

### Discours oral

#### Quatre contrôles techniques non interchangeables

- La règle **210** vise l’injection puis l’exécution d’un contenu malveillant.
- La règle **211** contrôle les domaines autorisés à encadrer la page.
- La règle **212** restreint l’origine des contenus chargés.
- La règle **214** vérifie qu’une ressource tierce correspond toujours à l’empreinte attendue.

#### Information, continuité et origine du service

- La règle 208 informe sur la sécurité d’une transaction sans constituer son mécanisme.
- La règle 215 propose deux moyens de validation, pas deux facteurs simultanés.
- La règle 216 conserve le domaine du site visible ; 217 authentifie le domaine de messagerie.
- Aucun de ces contrôles ne garantit une sécurité absolue : ils réduisent des risques distincts.

## Slide 35 - Prévenir avant qu’un risque devienne un préjudice

### Alternative textuelle

Prévenir avant qu’un risque devienne un préjudice.

### Description détaillée du visuel

Les six grappes convergent vers la personne centrale ; reprise du slogan uniquement ici.

### Message à retenir

Le socle Opquast relie chaque prévention à un préjudice utilisateur évitable.

### Transcription

#### Textes et relations

- SÉCURITÉ OPQUAST
- Protéger le canal
- Préserver la maîtrise du compte
- Contrôler ce qui s’exécute et se charge
- Éviter l’exposition inutile
- Reconnaître le vrai service
- Maintenir l’opération réalisable
- La sécurité Opquast, c’est d’abord prévenir des risques concrets pour l’utilisateur.
- OPQUAST
- RÈGLES OPQUAST · SÉCURITÉ
- 35 / 35

- Les six grappes convergent vers la personne centrale ; reprise du slogan uniquement ici.

### Discours oral

#### Six protections complémentaires

- **Protéger le canal** limite l’interception des échanges.
- **Préserver le compte** permet de gérer un mot de passe sans divulgation.
- **Contrôler les ressources** réduit les risques liés au type, à l’origine ou à l’intégrité.
- **Limiter l’exposition** évite de fournir des informations utiles à une attaque.
- **Reconnaître le service** identifie le site ou domaine de messagerie.
- **Maintenir l’action possible** prévient les blocages dans les opérations sécurisées.

#### Une prévention centrée sur l’utilisateur

- Ces six familles forment une **synthèse éditoriale**, pas un classement officiel.
- Opquast fournit un socle sans promettre une sécurité absolue.
- La sécurité protège la personne sans l’empêcher d’agir.
