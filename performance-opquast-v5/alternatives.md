# Alternatives textuelles - Serveur et Performance selon Opquast

Règles Opquast - Performance - Série Performance

## Slide 1 - La performance mobilise les ressources de l’utilisateur

### Alternative textuelle

Un terminal mobilise simultanément du temps, des données et du calcul.

### Transcription

#### Textes et relations

- La performance mobilise les ressources de l’utilisateur
- PERFORMANCE SELON OPQUAST V5
- Performance Opquast = ne pas faire attendre, télécharger ou calculer inutilement l’utilisateur
- Rapide n’est pas forcément léger, affiché n’est pas forcément utilisable
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 01 / 35

- Un ordinateur portable est relié à trois pictogrammes : une horloge, un transfert de données et une puce électronique.

### Message à retenir

Ne pas faire attendre, télécharger ou calculer inutilement l’utilisateur.

### Discours oral

- La phrase affichée est le **fil conducteur de cette série**, pas une définition officielle de la performance selon Opquast.
- Elle invite à observer trois ressources mobilisées côté utilisateur : son **temps**, ses **données** et les capacités de son **terminal**.
- Les règles présentées réduisent certains transferts ou donnent à l’utilisateur davantage d’information et de maîtrise.
- Elles forment un **socle de qualité web**, sans remplacer un audit Web Performance complet.
- **À retenir** : éviter un coût utilisateur qui n’apporte rien à son parcours.
- Commençons par distinguer ces trois ressources.

## Slide 2 - Trois ressources sont directement sollicitées

### Alternative textuelle

Attendre, télécharger et calculer moins côté utilisateur.

### Transcription

#### Textes et relations

- Trois ressources sont directement sollicitées
- CÔTÉ UTILISATEUR
- TEMPS
- Attendre moins
- DONNÉES
- Télécharger moins
- CAPACITÉS DU TERMINAL
- Calculer moins
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 02 / 35

- Trois cartes de même taille présentent les ressources sollicitées côté utilisateur : le temps, les données et les capacités du terminal.

### Message à retenir

La performance mobilise trois ressources côté utilisateur : temps, données et capacités du terminal.

### Discours oral

- Le **temps** est sollicité lorsque l’utilisateur attend l’affichage ou la disponibilité d’une action.
- Les **données** correspondent au volume reçu par sa connexion, avec un effet possible sur un forfait limité.
- Le **terminal** travaille pour afficher la page et exécuter ses traitements.
- Cette triade est une **grille de lecture pédagogique**, pas une classification officielle du référentiel.
- Elle aide à repérer qu’une page peut paraître rapide tout en restant lourde, ou s’afficher avant d’être utilisable.
- Pour éviter les confusions, séparons maintenant quatre diagnostics.

## Slide 3 - Rapide, léger, affiché, utilisable

### Alternative textuelle

Rapide, léger, affiché, utilisable.

### Transcription

#### Textes et relations

- Rapide, léger, affiché, utilisable
- RAPIDE ≠ LÉGER
- AFFICHÉ ≠ UTILISABLE
- Quatre questions distinctes
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 03 / 35

- Une matrice deux par deux oppose RAPIDE à LÉGER et AFFICHÉ à UTILISABLE avec des signes différents.

### Message à retenir

Rapide n’est pas forcément léger, affiché n’est pas forcément utilisable.

### Discours oral

- **Rapide** répond à une question de délai.
- **Léger** répond à une question de volume transféré.
- **Affiché** signifie que des éléments sont visibles.
- **Utilisable** signifie que l’utilisateur peut réellement cliquer, saisir ou naviguer.
- Une page peut donc apparaître vite tout en restant lourde, ou sembler complète alors que ses commandes ne répondent pas encore.
- Cette distinction dépasse le contrôle d’une règle Opquast isolée : elle structure la lecture de la série.
- Nous allons retrouver ces écarts dans cinq situations concrètes.

## Slide 4 - Cinq situations structurent la série

### Alternative textuelle

Cinq situations structurent la série.

### Transcription

#### Textes et relations

- Cinq situations structurent la série
- CINQ SITUATIONS
- Je télécharge trop
- Je retélécharge
- Le site décide
- Affiché mais bloqué
- Ma fibre masque
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 04 / 35

- Cinq cartes égales autour d’un centre COÛT UTILISATEUR.

### Message à retenir

Les règles se mémorisent par situations utilisateur.

### Discours oral

- Cette série regroupe les règles par **situations utilisateur**, et non selon les rubriques officielles du référentiel.
- **Je télécharge trop** : davantage de données sont reçues que nécessaire.
- **Je retélécharge** : une ressource déjà reçue repart sur le réseau.
- **Le site décide** : un média démarre sans décision explicite.
- **Affiché mais bloqué** : la page est visible, mais l’action reste indisponible.
- **Ma fibre masque** : un contexte confortable cache l’expérience d’une connexion ou d’un appareil moins performant.
- Ce regroupement est **pédagogique**, pas officiel.
- Commençons par les données téléchargées.

## Slide 5 - Télécharger seulement ce qui sert

### Alternative textuelle

Télécharger seulement ce qui sert.

### Transcription

#### Textes et relations

- Télécharger seulement ce qui sert
- JE TÉLÉCHARGE TROP
- Bonne ressource
- Fichier allégé
- Transport compressé
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 05 / 35

- Un colis numérique s’allège en trois étapes avant d’atteindre l’utilisateur.

### Message à retenir

La première grappe réduit la ressource, le fichier et le transfert.

### Discours oral

- Une ressource inutilement lourde peut ajouter de l’**attente** et des **données transférées**, surtout sur une connexion limitée.
- Quatre leviers seront distingués : choisir une ressource adaptée, minifier le fichier, compresser son transport et transmettre des informations de cache.
- Ces leviers n’agissent ni au même moment ni de la même manière.
- Le **choix de la ressource** évite un fichier surdimensionné.
- La **minification** allège la version servie ; la **compression** allège le transport.
- Le **cache** peut éviter certains retransferts lors des consultations suivantes.
- Premier levier : servir une image adaptée à son affichage.

## Slide 6 - 119 : servir une image adaptée

### Alternative textuelle

119 : servir une image adaptée.

### Transcription

#### Textes et relations

- 119 : servir une image adaptée
- RÈGLE 119
- Une vignette n’est pas une grande image réduite côté client.
- Petit à l’écran · petit à télécharger
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 06 / 35

- Une petite vignette reçoit un petit fichier ; un énorme fichier redimensionné est écarté.

### Message à retenir

Petit à l’écran doit aussi pouvoir être petit à télécharger.

### Discours oral

- **Règle 119 : « Les vignettes et aperçus ne sont pas des images de taille supérieure redimensionnées côté client. »**
- Réduire une grande image avec le HTML ou le CSS ne réduit pas le fichier téléchargé.
- L’utilisateur peut attendre davantage et recevoir des données sans bénéfice visible.
- **Ce que garantit la règle** : Une vignette ou un aperçu utilise une image dont les dimensions sont adaptées à cet usage.
- La règle contribue à réduire les téléchargements et à améliorer l’affichage, sans garantir toute la performance du site.
- **Petit à l’écran ne signifie pas forcément petit à télécharger.**

## Slide 7 - L’apparence ne révèle pas le poids

### Alternative textuelle

L’apparence ne révèle pas le poids.

### Transcription

#### Textes et relations

- L’apparence ne révèle pas le poids
- MÊME APPARENCE
- 150 × 150 affichés
- 5000 × 5000 téléchargés
- Le volume reste réel
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 07 / 35

- Deux cadres de même apparence reçoivent des fichiers très différents, avec les dimensions visibles.

### Message à retenir

Une image affichée en 150 × 150 peut provenir d’un original 5000 × 5000.

### Discours oral

- **Règle 119 : « Les vignettes et aperçus ne sont pas des images de taille supérieure redimensionnées côté client. »**
- Deux images peuvent occuper la même place à l’écran tout en ayant des dimensions et un poids très différents.
- Le navigateur télécharge le fichier réel, pas seulement la taille définie par le HTML ou le CSS.
- Le contrôle compare donc les **dimensions du fichier** à ses **dimensions d’affichage**.
- Les valeurs 150 × 150 et 5000 × 5000 illustrent l’écart ; ce ne sont pas des seuils Opquast.
- **À retenir** : l’apparence ne révèle pas le volume reçu.
- Le même souci d’allègement concerne la version servie du code.

## Slide 8 - Minifier enlève l’inutile du fichier

### Alternative textuelle

Minifier enlève l’inutile du fichier.

### Transcription

#### Textes et relations

- Minifier enlève l’inutile du fichier
- MINIFIER
- Même fonction
- Moins de caractères
- CSS · JavaScript
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 08 / 35

- Deux feuilles de code passent d’un bloc aéré à un bloc compact, sans changer la fonction.

### Message à retenir

La minification garde le code utile et retire les caractères inutiles à l’exécution.

### Discours oral

- La **minification** retire de la version servie les caractères inutiles au navigateur, par exemple certains espaces, commentaires et retours à la ligne.
- Elle conserve le code nécessaire et ne doit pas changer le résultat attendu.
- **Règle 229 : « Les feuilles de styles internes sont minifiées. »**
- **Règle 230 : « Les scripts internes sont minifiés. »**
- La minification réduit le fichier ; la **compression** réduira ensuite le volume transporté.
- Ce sont deux mécanismes complémentaires, mais distincts.
- Regardons d’abord les feuilles de styles avec la **règle 229**.

## Slide 9 - 229 : minifier les styles internes

### Alternative textuelle

229 : minifier les styles internes.

### Transcription

#### Textes et relations

- 229 : minifier les styles internes
- RÈGLE 229
- Les feuilles de styles internes sont minifiées.
- CSS plus compact
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 09 / 35

- Une feuille CSS passe d’une forme lisible espacée à une forme compacte.

### Message à retenir

La règle 229 réduit la taille des feuilles de styles internes.

### Discours oral

- **Règle 229 : « Les feuilles de styles internes sont minifiées. »**
- La version CSS servie retire les caractères qui ne sont pas nécessaires à son interprétation par le navigateur.
- L’utilisateur reçoit un fichier plus volumineux, ce qui peut ajouter du transfert et retarder l’affichage.
- **Ce que garantit la règle** : Les feuilles de styles internes sont servies sous une forme minifiée, sans promettre à elles seules un affichage rapide.
- La minification reste distincte de la compression du transport.
- Le même principe s’applique aux scripts internes.

## Slide 10 - 230 : minifier les scripts internes

### Alternative textuelle

230 : minifier les scripts internes.

### Transcription

#### Textes et relations

- 230 : minifier les scripts internes
- RÈGLE 230
- Les scripts internes sont minifiés.
- JavaScript plus compact
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 10 / 35

- Un script JavaScript compact conserve la même sortie qu’un script aéré.

### Message à retenir

La règle 230 réduit la taille des scripts internes.

### Discours oral

- **Règle 230 : « Les scripts internes sont minifiés. »**
- La version JavaScript servie retire les caractères inutiles à son exécution, sans supprimer le code nécessaire.
- L’utilisateur reçoit davantage de données ; ce volume peut retarder le chargement et la disponibilité des interactions.
- **Ce que garantit la règle** : Les scripts internes sont servis sous une forme minifiée, sans garantir que tout le JavaScript soit utile ou rapide à exécuter.
- La règle porte sur le volume du fichier, pas sur toutes les causes possibles de lenteur.
- Après le fichier, examinons le volume transmis sur le réseau.

## Slide 11 - 226 : compresser pendant le transport

### Alternative textuelle

226 : compresser pendant le transport.

### Transcription

#### Textes et relations

- 226 : compresser pendant le transport
- RÈGLE 226
- Le serveur transmet des contenus compressés.
- Moins d’octets pendant le transport
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 11 / 35

- Une ressource passe dans une presse avant de voyager puis reprend sa forme côté navigateur.

### Message à retenir

La compression réduit le volume transmis au client qui l’accepte.

### Discours oral

- **Règle 226 : « Le serveur transmet des contenus compressés aux clients qui les acceptent. »**
- La compression agit pendant le transfert des contenus compressibles, notamment HTML, CSS et JavaScript.
- Un client qui accepte la compression reçoit davantage de données et peut attendre plus longtemps, surtout sur un réseau limité.
- **Ce que garantit la règle** : Le serveur négocie et transmet une version compressée lorsque le client l’accepte.
- Cela contribue à réduire la bande passante, le délai de rendu et l’impact énergétique du transfert.
- La minification allège la version servie ; la compression allège son transport.

## Slide 12 - Minifier, compresser, cacher

### Alternative textuelle

Minifier, compresser, cacher.

### Transcription

#### Textes et relations

- Minifier, compresser, cacher
- TROIS GESTES
- MINIFIER · le fichier
- COMPRESSER · le transport
- CACHER · le voyage suivant
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 12 / 35

- Trois postes alignés : fichier compact, transport serré, ressource conservée localement.

### Message à retenir

Trois opérations complémentaires répondent à trois moments différents.

### Discours oral

- **Règles 229 et 230** : minifier réduit la version CSS ou JavaScript servie.
- **Règle 226** : compresser réduit le volume transmis lorsque le client l’accepte.
- **Règle 227** : les informations de cache permettent la conservation, la réutilisation ou la revalidation d’un contenu.
- Le cache n’allège pas forcément le premier transfert et n’évite pas systématiquement tout échange.
- Ces mécanismes sont **complémentaires** : fichier, transport, puis consultations suivantes.
- **À retenir** : ne pas confondre minification, compression et cache.
- Regardons précisément ce que garantit la **règle 227**.

## Slide 13 - 227 : éviter le retransfert

### Alternative textuelle

227 : éviter le retransfert.

### Transcription

#### Textes et relations

- 227 : éviter le retransfert
- RÈGLE 227
- Le serveur permet la mise en cache des contenus.
- Éviter le retransfert
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 13 / 35

- Premier trajet serveur-navigateur complet ; second trajet réduit grâce à une ressource conservée.

### Message à retenir

Le cache permet de ne pas renvoyer ce que le navigateur possède déjà.

### Discours oral

- **Règle 227 : « Le serveur envoie les informations permettant la mise en cache des contenus. »**
- Ces informations indiquent au navigateur comment conserver, réutiliser ou revalider un contenu.
- L’utilisateur peut recevoir de nouveau des ressources inchangées, avec davantage d’attente et de données transférées.
- **Ce que garantit la règle** : Le serveur fournit les métadonnées nécessaires à la mise en cache.
- La règle ne garantit ni la réutilisation de toutes les ressources ni l’absence de tout échange avec le serveur.
- **Déjà reçu** peut alors éviter un nouveau transfert complet.

## Slide 14 - Quatre gestes, trois moments

### Alternative textuelle

Choisir, minifier, compresser et mettre en cache agissent à trois moments.

### Transcription

#### Textes et relations

- Quatre gestes, trois moments
- UNE CHAÎNE PÉDAGOGIQUE, PAS UN PROCESSUS UNIQUE
- AVANT L’ENVOI
- 119 · image adaptée à l’usage
- 229 et 230 · CSS et JavaScript minifiés
- PENDANT LE TRANSPORT
- 226 · contenus compressés
- CONSULTATIONS SUIVANTES
- 227 · mise en cache
- Moins de données inutiles à chaque moment
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 14 / 35

- Trois colonnes distinguent les actions avant l’envoi, pendant le transport et lors des consultations suivantes, sans représenter les transformations successives d’un même fichier.

### Message à retenir

Choisir, minifier, compresser et mettre en cache réduisent les données inutiles à trois moments différents.

### Discours oral

- **Règle 119** : choisir une vignette ou un aperçu adapté à ses dimensions d’affichage.
- **Règles 229 et 230** : minifier les feuilles de styles et les scripts internes servis.
- **Règle 226** : compresser les contenus compressibles pour les clients qui l’acceptent.
- **Règle 227** : fournir les informations nécessaires à la mise en cache.
- Ces leviers interviennent sur la **ressource choisie**, la **version servie**, le **transport** et les **consultations suivantes**.
- Ils sont complémentaires, mais ne forment pas une séquence obligatoire pour chaque fichier.
- Une connexion rapide peut masquer le coût que ces règles cherchent à limiter.

## Slide 15 - Les conditions confortables masquent les défauts

### Alternative textuelle

Les conditions confortables masquent les défauts.

### Transcription

#### Textes et relations

- Les conditions confortables masquent les défauts
- MA FIBRE MASQUE
- Réseau faible
- Mobilité
- Itinérance
- Appareil ancien
- Données limitées
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 15 / 35

- Une bulle confortable se fissure pour révéler cinq contextes réels autour.

### Message à retenir

La fibre et un terminal récent peuvent masquer les difficultés réelles.

### Discours oral

- Une connexion rapide et un terminal récent peuvent masquer le poids ou les délais d’une page.
- Sur un **réseau faible ou instable**, chaque donnée supplémentaire peut prolonger l’attente.
- En **mobilité**, le volume transféré peut aussi peser sur un forfait limité.
- Sur un **appareil ancien**, l’affichage et la disponibilité des interactions peuvent prendre davantage de temps.
- Tester plusieurs contextes révèle ces écarts, sans remplacer un protocole Web Performance spécialisé.
- **À retenir** : rapide sur ma fibre ne signifie pas rapide pour tout le monde.
- Vitesse perçue et volume transféré doivent donc être observés séparément.

## Slide 16 - Une page rapide peut rester lourde

### Alternative textuelle

Le temps d’affichage peut être rapide malgré un volume transféré élevé.

### Transcription

#### Textes et relations

- Une page rapide peut rester lourde
- TEMPS D’AFFICHAGE
- RAPIDE
- VOLUME TRANSFÉRÉ
- ÉLEVÉ
- MESURER LES DEUX
- EN LIEN AVEC LES RÈGLES 119, 226, 227, 229 ET 230
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 16 / 35

- Une même page web est reliée sans flèche à deux instruments indépendants : un chronomètre rapide et un compteur de données élevé.

### Message à retenir

Le temps d’affichage et le volume transféré doivent être mesurés séparément.

### Discours oral

#### Rapide et léger ne sont pas synonymes

- **Règle 119 : « Les vignettes et aperçus ne sont pas des images de taille supérieure redimensionnées côté client. »**
- **Règle 229 : « Les feuilles de styles internes sont minifiées. »**
- **Règle 230 : « Les scripts internes sont minifiés. »**
- **Règle 226 : « Le serveur transmet des contenus compressés aux clients qui les acceptent. »**
- **Règle 227 : « Le serveur envoie les informations permettant la mise en cache des contenus. »**
- Ces règles réduisent certains volumes ou permettent d’éviter certains retransferts.
- Elles ne garantissent pas, à elles seules, un affichage rapide.
- **À retenir** : mesurer séparément le délai observé et les données transférées.

#### De la visibilité à l’action

- Une page visible peut aussi rester inutilisable.

## Slide 17 - Affiché ne veut pas dire utilisable

### Alternative textuelle

La page est visible avant la fin des traitements, puis devient utilisable.

### Transcription

#### Textes et relations

- Affiché ne veut pas dire utilisable
- PAGE VISIBLE
- JE VOIS
- TRAITEMENTS EN COURS
- PAGE UTILISABLE
- JE PEUX AGIR
- MESURER JUSQU’À L’INTERACTION
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 17 / 35

- Une même page web est visible à gauche, séparée par des traitements encore actifs de son état utilisable à droite. Le cartouche relie les deux états et invite à mesurer jusqu’à l’interaction.

### Message à retenir

Une page visible n’est pas nécessairement prête à être utilisée.

### Discours oral

- Une page peut sembler rapide dès que ses premiers éléments apparaissent.
- Pourtant, le navigateur peut encore charger des ressources ou exécuter des traitements.
- Si un bouton, un menu ou un champ ne répond pas, l’utilisateur attend toujours.
- Ce constat relève de la **Web Performance** au sens large ; il ne correspond pas à une règle Opquast précise de cette série.
- Le schéma présente donc des repères d’expérience, pas des étapes techniques strictement séparées.
- **À retenir** : observer aussi le moment où l’utilisateur peut réellement agir.
- Avant certains coûts, Opquast redonne directement le choix à l’utilisateur.

## Slide 18 - Laisser décider avant de consommer

### Alternative textuelle

Laisser décider avant de consommer.

### Transcription

#### Textes et relations

- Laisser décider avant de consommer
- MAÎTRISE UTILISATEUR
- Durée
- Déclenchement
- Format
- Taille
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 18 / 35

- Quatre cartes convergent vers un bouton DÉCIDER.

### Message à retenir

Quatre règles donnent à l’utilisateur des informations ou le déclenchement.

### Discours oral

#### Informer ou laisser déclencher

- **Règle 123 : « La durée des contenus vidéo ou audio est indiquée. »**
- **Règle 124 : « Les vidéos sont déclenchées par l’utilisateur. »**
- **Règle 147 : « Le format des fichiers proposés en téléchargement est indiqué. »**
- **Règle 148 : « La taille des fichiers internes proposés en téléchargement est indiquée. »**
- La durée, le format et la taille **éclairent la décision** ; le déclenchement laisse l’initiative à l’utilisateur.
- Ce regroupement est pédagogique : ces règles n’allègent pas automatiquement les contenus.
- Elles rendent certains coûts visibles ou maîtrisables.

#### Le volume avant le téléchargement

- Commençons par le volume annoncé avant le téléchargement.

## Slide 19 - 148 : annoncer la taille du fichier

### Alternative textuelle

148 : annoncer la taille du fichier.

### Transcription

#### Textes et relations

- 148 : annoncer la taille du fichier
- RÈGLE 148
- La taille du fichier est indiquée.
- Télécharger maintenant · différer
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 19 / 35

- Un lien de téléchargement affiche clairement un poids avant un bouton de décision.

### Message à retenir

La taille annoncée permet de choisir le moment du téléchargement.

### Discours oral

#### **Règle 148** : annoncer la taille

- **Règle 148 : « La taille des fichiers internes proposés en téléchargement est indiquée. »**
- L’information doit être disponible avant de lancer le téléchargement.

##### Impact du non-respect

- L’utilisateur peut engager un téléchargement qu’il aurait préféré différer, notamment avec une connexion ou un forfait limité.

##### Garantie apportée

- **Ce que garantit la règle** : L’utilisateur connaît le volume du fichier et peut décider de le télécharger maintenant, plus tard ou pas du tout.
- La règle informe sur la taille ; elle ne réduit pas le fichier.

#### Du volume au format

- Après le volume, il faut savoir si le fichier pourra être ouvert.

## Slide 20 - 147 : annoncer le format du fichier

### Alternative textuelle

147 : annoncer le format du fichier.

### Transcription

#### Textes et relations

- 147 : annoncer le format du fichier
- RÈGLE 147
- Le format du fichier est indiqué.
- Puis-je l’ouvrir ?
- PDF
- ODS
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 20 / 35

- Deux fichiers nommés PDF et ODS sont identifiables avant téléchargement.

### Message à retenir

Le format annoncé évite un téléchargement que l’utilisateur ne peut pas exploiter.

### Discours oral

#### **Règle 147** : annoncer le format

- **Règle 147 : « Le format des fichiers proposés en téléchargement est indiqué. »**
- Une mention comme PDF, ODS ou DOC identifie le type de fichier avant son téléchargement.

##### Impact du non-respect

- L’utilisateur peut télécharger un fichier incompatible avec ses outils et perdre du temps ou des données.

##### Garantie apportée

- **Ce que garantit la règle** : Le format annoncé permet d’évaluer la compatibilité avant de télécharger.
- Cette information ne renseigne ni sur la taille du fichier ni sur son accessibilité.

#### Du format à la durée

- Pour un média, une autre information prépare la décision : sa durée.

## Slide 21 - 123 : annoncer la durée du média

### Alternative textuelle

123 : annoncer la durée du média.

### Transcription

#### Textes et relations

- 123 : annoncer la durée du média
- RÈGLE 123
- La durée du contenu est indiquée.
- 2 min ≠ 90 min
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 21 / 35

- Deux lecteurs portent le même titre mais affichent 2 min et 90 min avant lecture.

### Message à retenir

La durée aide à décider de consulter ou télécharger un média.

### Discours oral

#### **Règle 123** : annoncer la durée

- **Règle 123 : « La durée des contenus vidéo ou audio est indiquée. »**
- La durée doit pouvoir être connue avant la consultation du média.

##### Impact du non-respect

- L’utilisateur ignore le temps à consacrer au contenu et peut le lancer dans un contexte inadapté.

##### Garantie apportée

- **Ce que garantit la règle** : La durée annoncée permet de choisir le bon moment pour consulter ou télécharger le média.
- Elle informe sur le temps de consultation, pas sur le poids numérique du fichier.

#### De la durée au déclenchement

- Cette information ne suffit pas si la vidéo démarre sans décision de l’utilisateur.

## Slide 22 - 124 : laisser déclencher la vidéo

### Alternative textuelle

124 : laisser déclencher la vidéo.

### Transcription

#### Textes et relations

- 124 : laisser déclencher la vidéo
- RÈGLE 124
- La vidéo est déclenchée par l’utilisateur.
- Ne pas consommer à sa place
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 22 / 35

- Un lecteur vidéo reste en pause devant une main qui choisit le bouton lecture.

### Message à retenir

La vidéo démarre sur décision de l’utilisateur.

### Discours oral

#### **Règle 124** : laisser déclencher la vidéo

- **Règle 124 : « Les vidéos sont déclenchées par l’utilisateur. »**
- Une vidéo ne démarre pas automatiquement au chargement ni de manière imprévisible après une autre action.

##### Impact du non-respect

- L’utilisateur peut subir une consommation de données et une perturbation sonore ou visuelle qu’il n’a pas choisies.

##### Garantie apportée

- **Ce que garantit la règle** : L’utilisateur garde l’initiative du déclenchement de la vidéo.
- La règle ne garantit ni un fichier léger ni l’accessibilité complète du lecteur.

#### Quatre décisions complémentaires

- Taille, format, durée et déclenchement répondent à quatre décisions distinctes.

## Slide 23 - Quatre questions avant de consommer

### Alternative textuelle

Quatre questions avant de consommer.

### Transcription

#### Textes et relations

- Quatre questions avant de consommer
- AVANT DE CONSOMMER
- Combien de temps ?
- Quand démarrer ?
- Quel format ?
- Quelle taille ?
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 23 / 35

- Un cadran de décision avec quatre questions et un centre JE DÉCIDE.

### Message à retenir

Durée, déclenchement, format et taille couvrent quatre décisions différentes.

### Discours oral

#### Quatre questions avant d’agir

- **Règle 123** : combien de temps dure le média ?
- **Règle 124** : qui décide du démarrage de la vidéo ?
- **Règle 147** : quel est le format du fichier ?
- **Règle 148** : quelle est sa taille ?
- Ces quatre règles ne forment pas une catégorie officielle.
- Elles donnent une **information utile** ou préservent une **décision explicite**.
- Lorsqu’une réponse manque, l’utilisateur perd une partie de sa maîtrise avant de consulter ou de télécharger.
- **À retenir** : informer n’allège pas le contenu, mais permet de choisir.

#### Au-delà d’une rubrique

- Cette sélection dépasse la seule rubrique « Serveur et performances ».

## Slide 24 - Rubrique officielle et sélection : 4 règles en commun

### Alternative textuelle

Rubrique de 13 règles et série de 9 règles, avec 4 règles en commun.

### Transcription

#### Textes et relations

- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Rubrique officielle et sélection : 4 règles en commun
- RUBRIQUE OFFICIELLE
- Serveur et performances
- 13 règles · 218 à 230
- 218
- 219
- 220
- 221
- 222
- 223
- 224
- 225
- 228
- 4 RÈGLES COMMUNES
- 226
- 227
- 229
- 230
- SÉLECTION DE LA SÉRIE
- 9 règles étudiées
- 119 · 123 · 124 · 147 · 148
- Deux périmètres qui se recoupent
- RÈGLES OPQUAST · PERFORMANCE
- 24 / 35

- Deux grands panneaux se chevauchent. Le panneau de gauche représente la rubrique officielle « Serveur et performances » et contient les règles 218 à 230. Le panneau de droite représente les neuf règles étudiées dans la série. Les règles 226, 227, 229 et 230 occupent leur intersection et ne sont pas répétées dans les panneaux latéraux.

### Message à retenir

La rubrique officielle et la sélection de cette série sont deux périmètres distincts qui ont quatre règles en commun.

### Discours oral

#### Rubrique officielle et sélection pédagogique

- La rubrique **« Serveur et performances »** contient treize règles, de **218 à 230**.
- La sélection principale de cette série couvre neuf règles réparties dans plusieurs rubriques.
- Quatre appartiennent aux deux périmètres :
- **Règle 226 : « Le serveur transmet des contenus compressés aux clients qui les acceptent. »**
- **Règle 227 : « Le serveur envoie les informations permettant la mise en cache des contenus. »**
- **Règle 229 : « Les feuilles de styles internes sont minifiées. »**
- **Règle 230 : « Les scripts internes sont minifiés. »**
- Les autres règles de la rubrique visent notamment l’indexation, les erreurs HTTP, la navigation ou l’encodage.

#### Un effet transversal

- La **règle 119** illustre au contraire un effet transversal depuis « Images et médias ».

## Slide 25 - 119 : dans Images et médias, avec un effet sur la performance

### Alternative textuelle

La règle 119 reste dans Images et médias et réduit les données transférées.

### Transcription

#### Textes et relations

- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- 119 : dans Images et médias, avec un effet sur la performance
- RÈGLE 119
- RUBRIQUE OFFICIELLE
- Images et médias
- EFFET SUR LA PERFORMANCE
- Moins de données à télécharger
- Affichage plus rapide
- VIGNETTE ADAPTÉE
- Pas une grande image réduite
- RÈGLES OPQUAST · PERFORMANCE
- 25 / 35

- Une carte unique « RÈGLE 119 » est commune aux deux panneaux. À gauche, le panneau bleu indique le classement officiel « Images et médias ». À droite, le panneau vert indique deux effets sur la performance : moins de données à télécharger et un affichage plus rapide. En dessous, une vignette adaptée est validée, tandis qu’une grande image seulement réduite à l’écran est rejetée.

### Message à retenir

La règle 119 reste dans « Images et médias », mais son application améliore directement la performance.

### Discours oral

#### **Règle 119** : un effet transversal

- **Règle 119 : « Les vignettes et aperçus ne sont pas des images de taille supérieure redimensionnées côté client. »**
- Elle appartient officiellement à la rubrique **« Images et médias »**.

##### Impact du non-respect

- Une grande image réduite seulement par le HTML ou le CSS reste entièrement téléchargée, avec davantage de données et d’attente possibles.

##### Garantie apportée

- **Ce que garantit la règle** : La vignette ou l’aperçu utilise une **image adaptée** à ses dimensions d’affichage.
- Son effet sur la performance est transversal ; sa rubrique officielle ne change pas.

#### Vers la rubrique serveur

- Passons maintenant aux autres règles de la rubrique « Serveur et performances ».

## Slide 26 - Accéder au site sans être bloqué

### Alternative textuelle

Les règles 218 et 221 évitent deux blocages d’accès au site.

### Transcription

#### Textes et relations

- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Accéder au site sans être bloqué
- RÈGLE 218
- AVEC OU SANS WWW
- exemple.fr
- www.exemple.fr
- Le même site reste accessible
- RÈGLE 221
- VERSION MOBILE OU CLASSIQUE
- L’utilisateur garde le choix
- RÈGLES OPQUAST · PERFORMANCE
- 26 / 35

- Deux panneaux de même importance présentent deux configurations serveur. Dans le premier, exemple.fr et www.exemple.fr convergent vers le même site. Dans le second, un téléphone et un ordinateur représentent deux versions entre lesquelles l’utilisateur garde le choix.

### Message à retenir

Le serveur doit rendre le site accessible par ses adresses usuelles sans imposer une version à l’utilisateur.

### Discours oral

#### Deux règles contre les impasses d’accès

- **Règle 218 : « L’adresse du site fonctionne avec et sans préfixe www. »**
- **Règle 221 : « Le serveur ne force pas la redirection vers la version ou l’application mobile. »**

##### Impact du non-respect

- Une forme usuelle de l’adresse peut échouer, ou l’utilisateur peut être enfermé dans une version mobile qui ne répond pas à son besoin.

##### Ce que garantissent les règles

- Le site reste accessible avec et sans `www`, sans imposer une version mobile à l’utilisateur.
- La **règle 218** ne désigne pas l’adresse principale ; la **règle 221** n’interdit pas de proposer une version adaptée.

#### L’exploration du site

- La configuration serveur guide aussi l’exploration du site par les robots.

## Slide 27 - Deux fichiers pour guider les robots

### Alternative textuelle

robots.txt donne des consignes et sitemap.xml indique les contenus à explorer.

### Transcription

#### Textes et relations

- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Deux fichiers pour guider les robots
- RÈGLE 219
- robots.txt
- Donner des instructions
- RÈGLE 220
- sitemap.xml
- Indiquer les contenus à explorer
- Guider l’exploration ne garantit pas le classement
- RÈGLES OPQUAST · PERFORMANCE
- 27 / 35

- Deux panneaux de même importance présentent deux fichiers placés à la racine du site. robots.txt donne des instructions aux robots d’indexation. sitemap.xml indique les contenus à explorer. Les deux sont reliés à un robot, sans promesse de classement.

### Message à retenir

robots.txt donne des instructions aux robots ; sitemap.xml leur indique les contenus à explorer.

### Discours oral

#### Deux fichiers pour guider les robots

- **Règle 219 : « La racine du site contient des instructions pour les robots d’indexation. »**
- **Règle 220 : « Le site propose un fichier sitemap indiquant les contenus à explorer. »**

##### Impact du non-respect

- Les robots disposent de moins d’indications sur les zones et contenus à explorer.

##### Ce que garantissent les règles

- `robots.txt` transmet des **instructions** ; le sitemap fournit un **inventaire de contenus à explorer**.
- `robots.txt` n’est pas une barrière de sécurité et ne contraint pas tous les robots.
- Aucun de ces fichiers ne garantit l’indexation ou le classement.

#### Le bon signal pour une ressource absente

- Lorsqu’une ressource manque, le serveur doit aussi envoyer le bon signal.

## Slide 28 - Une ressource absente doit répondre 404

### Alternative textuelle

Une ressource introuvable produit le statut HTTP 404.

### Transcription

#### Textes et relations

- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Une ressource absente doit répondre 404
- RÈGLE 222
- RESSOURCE INTROUVABLE
- HTTP 404
- Un signal fiable pour les navigateurs et les robots
- RÈGLES OPQUAST · PERFORMANCE
- 28 / 35

- Une ressource introuvable est transmise au serveur, qui répond avec le statut HTTP 404. Une zone commune représente les navigateurs et les robots qui reçoivent ce signal technique.

### Message à retenir

Une ressource absente doit être signalée par le véritable statut HTTP 404, pas seulement par l’apparence de la page.

### Discours oral

#### **Règle 222** : répondre avec le statut 404

- **Règle 222 : « Le serveur envoie un code HTTP 404 pour les ressources non trouvées. »**
- Le message visible et le statut HTTP sont deux informations distinctes.

##### Impact du non-respect

- Une page peut annoncer une erreur tout en renvoyant un faux succès HTTP 200, ce qui trompe les moteurs et les outils de contrôle.

##### Garantie apportée

- **Ce que garantit la règle** : Une ressource absente produit le **signal technique 404** attendu.
- La règle ne demande pas encore que la page affichée soit personnalisée.

#### Du code à la page d’erreur

- La **règle 223** complète ce signal par une page compréhensible pour l’utilisateur.

## Slide 29 - La rubrique couvre aussi les erreurs et l’encodage

### Alternative textuelle

Quatre règles concernent les erreurs, la navigation et l’encodage.

### Transcription

#### Textes et relations

- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- La rubrique couvre aussi les erreurs et l’encodage
- RUBRIQUE OFFICIELLE
- Serveur et performances
- ERREURS SERVEUR
- 223 · page 404 personnalisée
- 224 · page 403 personnalisée
- CONTINUITÉ DE NAVIGATION
- 225 · menu principal sur les pages d’erreur
- AFFICHAGE DES CARACTÈRES
- 228 · jeu de caractères dans les entêtes
- RÈGLES OPQUAST · PERFORMANCE
- 29 / 35

- Une grande carte représente la rubrique officielle « Serveur et performances ». Elle contient trois modules horizontaux : erreurs serveur pour les règles 223 et 224, continuité de navigation pour la règle 225 et affichage des caractères pour la règle 228. Des coches vertes signalent la présence du menu principal et le bon affichage des caractères.

### Message à retenir

La rubrique « Serveur et performances » couvre aussi la compréhension des erreurs, la continuité de navigation et l’encodage.

### Discours oral

#### Erreurs compréhensibles et encodage fiable

- **Règle 223 : « Le serveur envoie une page d’erreur 404 personnalisée. »**
- **Règle 224 : « Le serveur envoie une page d’interdiction 403 personnalisée. »**
- Ces pages expliquent l’absence ou l’interdiction et confirment que le serveur répond.
- **Règle 225 : « Le menu principal de navigation figure sur les pages d’erreur personnalisées. »** : ce menu permet précisément de reprendre la navigation.
- **Règle 228 : « Les entêtes envoyés par le serveur contiennent les informations relatives au jeu de caractères employé. »** : l’entête indique au navigateur l’encodage déclaré.
- Ces règles appartiennent à la rubrique sans mesurer la vitesse d’affichage.

#### Le contrôle des médias

- Deux règles sur les médias complètent maintenant la question du contrôle utilisateur.

## Slide 30 - 125 et 126 restent en périphérie

### Alternative textuelle

125 et 126 restent en périphérie.

### Transcription

#### Textes et relations

- 125 et 126 restent en périphérie
- ANNEXE · PÉRIPHÉRIE
- 125 · sons
- 126 · animations
- Contrôle et accessibilité d’abord
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 30 / 35

- Deux satellites restent autour du noyau performance avec une distance visible.

### Message à retenir

Sons et animations relèvent surtout du contrôle et de l’accessibilité.

### Discours oral

#### Deux règles placées en périphérie de cette série

- **Règle 125 : « Les sons sont déclenchés par l’utilisateur. »**
- **Règle 126 : « Les animations, sons et clignotements peuvent être mis en pause. »**
- Leur objectif principal est le **contrôle utilisateur** et l’accessibilité, pas la réduction du poids des fichiers.
- La **règle 125** évite un déclenchement sonore automatique ou imprévisible.
- La **règle 126** impose des moyens d’interrompre les animations de plus de cinq secondes et les sons de plus de trois secondes.
- Les placer ici en périphérie est un **choix éditorial de la présentation**, pas une catégorie Opquast.

#### Du socle à la mesure

- Distinguons maintenant ce socle de règles d’un audit Web Performance spécialisé.

## Slide 31 - Opquast pose le socle, l’audit mesure la performance

### Alternative textuelle

Le socle Opquast et l’audit Web Performance sont complémentaires.

### Transcription

#### Textes et relations

- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Opquast pose le socle, l’audit mesure la performance
- SOCLE OPQUAST
- Fondamentaux durables et vérifiables
- 119 · images adaptées
- 226 · contenus compressés
- 227 · mise en cache
- 229 · CSS minifiées
- 230 · scripts minifiés
- AUDIT WEB PERFORMANCE
- Performance réelle du site
- MESURER
- DIAGNOSTIQUER
- OPTIMISER
- Deux démarches complémentaires
- RÈGLES OPQUAST · PERFORMANCE
- 31 / 35

- Deux panneaux de même niveau distinguent le socle Opquast de l’audit Web Performance. Le panneau de gauche rassemble cinq fondamentaux Opquast. Le panneau de droite présente trois actions d’un audit spécialisé. Une capsule commune indique que les deux démarches sont complémentaires ; aucune flèche ni forme englobante ne suggère une inclusion.

### Message à retenir

Opquast pose des fondamentaux durables ; un audit Web Performance mesure et optimise la performance réelle du site.

### Discours oral

#### Deux démarches complémentaires

- Les **règles 119, 226, 227, 229 et 230** posent des fondamentaux sur les images, la compression, le cache et la minification.
- Leur respect ne prouve pas que le site est globalement performant.
- Un audit **Web Performance** mesure le comportement dans des contextes testés : réseau, appareil, navigateur, parcours.
- Il recherche les causes de délai, de transfert ou de calcul et suit des indicateurs adaptés.
- Opquast n’impose ici ni score d’outil ni seuil numérique arbitraire.
- **À retenir** : les règles donnent un socle ; l’audit mesure, diagnostique et optimise dans un contexte défini.

#### Des effets dans plusieurs disciplines

- Les gains obtenus peuvent alors contribuer à plusieurs disciplines, sans les confondre.

## Slide 32 - Relier sans confondre les disciplines

### Alternative textuelle

Relier sans confondre les disciplines.

### Transcription

#### Textes et relations

- Relier sans confondre les disciplines
- RELATIONS, PAS ÉQUIVALENCES
- UX
- Accessibilité contextuelle
- Écoconception
- SEO
- Coûts d’infrastructure
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 32 / 35

- Un centre UTILISATEUR relié à cinq domaines distincts, sans fusion des cercles.

### Message à retenir

Performance, UX, accessibilité contextuelle, écoconception, SEO et coûts se recouvrent sans être synonymes.

### Discours oral

#### Des relations, pas des équivalences

- Réduire l’**attente** et les **données transférées** améliore d’abord l’expérience de l’utilisateur.
- Cela peut aussi mieux servir les personnes équipées d’un appareil ancien ou soumises à une connexion instable.
- Moins de transferts peut contribuer à l’**écoconception** et réduire certains coûts de bande passante.
- La vitesse peut également avoir un effet sur la visibilité dans les moteurs de recherche.
- Mais un site rapide n’est pas automatiquement accessible, écoconçu, bien référencé ou agréable à utiliser.
- Chaque discipline conserve ses objectifs, ses critères et ses méthodes.

#### Une lecture globale de la qualité

- Le modèle VPTCS aide à situer ces effets dans une lecture globale de la qualité.

## Slide 33 - VPTCS : une lecture transversale

### Alternative textuelle

VPTCS : une lecture transversale.

### Transcription

#### Textes et relations

- VPTCS : une lecture transversale
- LECTURE VPTCS
- Visibilité
- Perception
- Technique
- Contenus
- Services
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 33 / 35

- Cinq branches V, P, T, C, S partent d’un centre PERFORMANCE.

### Message à retenir

La performance traverse visibilité, perception, technique, contenus et services.

### Discours oral

#### VPTCS, une lecture des qualités attendues

- **Visibilité** : le service peut être rencontré.
- **Perception** : il peut être correctement perçu et utilisé.
- **Technique** : il fonctionne correctement.
- **Contenus** : il fournit une information de qualité.
- **Services** : il délivre les services attendus.
- VPTCS structure ces qualités ; il ne décrit pas une chronologie stricte du parcours.
- La performance a un noyau technique, mais ses effets peuvent toucher plusieurs dimensions.
- Cette lecture transversale n’est pas un classement officiel des règles Opquast.

#### Six distinctions structurantes

- Six distinctions permettent maintenant de consolider l’essentiel.

## Slide 34 - Six distinctions à retenir

### Alternative textuelle

Six cartes distinguent des notions proches de la performance.

### Transcription

#### Textes et relations

- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- Six distinctions à retenir
- RUBRIQUE
- PERFORMANCE
- COMPRESSION
- CACHE
- MINIFICATION
- COMPRESSION
- POIDS RÉEL
- INFORMATION SUR LE POIDS
- AFFICHÉ
- UTILISABLE
- PERFORMANCE
- ÉCOCONCEPTION
- RÈGLES OPQUAST · PERFORMANCE
- 34 / 35

- Six cartes disposées en deux colonnes et trois lignes présentent deux notions de même niveau séparées par un seul signe « ≠ ». Chaque carte forme une opposition complète et autonome.

### Message à retenir

Distinguer le périmètre, les techniques, l’information et les bénéfices évite les raccourcis sur la performance.

### Discours oral

#### Six distinctions à conserver

- **Thème et rubrique** : la performance dépasse « Serveur et performances », qui contient aussi erreurs et encodage.
- **Compression et cache** : l’une réduit un transfert ; l’autre permet la réutilisation ou la revalidation.
- **Minification et compression** : l’une allège la version servie ; l’autre agit pendant le transport.
- **Réduire et informer** : la **règle 119** réduit le fichier reçu ; la **règle 148** annonce sa taille.
- **Affiché et utilisable** : voir une page ne prouve pas que ses commandes répondent.
- **Performance et écoconception** : la performance peut y contribuer, sans couvrir tout le cycle de vie.

#### Trois verbes pour conclure

- La conclusion tient en trois verbes : réduire, éviter, laisser décider.

## Slide 35 - Rendre le coût utile, visible et maîtrisable

### Alternative textuelle

Rendre le coût utile, visible et maîtrisable.

### Transcription

#### Textes et relations

- Rendre le coût utile, visible et maîtrisable
- PERFORMANCE SELON OPQUAST V5
- Performance Opquast = ne pas faire attendre, télécharger ou calculer inutilement l’utilisateur
- Rapide n’est pas forcément léger, affiché n’est pas forcément utilisable
- RÉDUIRE · ÉVITER · LAISSER DÉCIDER
- QUALITÉ WEB
- EXPÉRIENCES DURABLES
- Opquast
- DES SITES MEILLEURS POUR TOUS
- RÈGLES OPQUAST · PERFORMANCE
- 35 / 35

- Trois gestes entourent l’utilisateur : RÉDUIRE, ÉVITER, LAISSER DÉCIDER.

### Message à retenir

La performance Opquast évite les coûts inutiles et rend les choix visibles.

### Discours oral

- **Réduire** : les **règles 119, 226, 229 et 230** limitent certains volumes téléchargés ou transmis.
- **Éviter** : la **règle 227** permet la mise en cache et peut éviter certains retransferts complets.
- **Laisser décider** : les **règles 123, 124, 147 et 148** rendent un coût visible ou préservent l’initiative de l’utilisateur.
- Cette synthèse est un **choix éditorial**, pas une définition officielle de la performance selon Opquast.
- Ces règles agissent sur l’attente, les données transférées et la maîtrise de certains contenus.
- Le calcul relève aussi d’un audit Web Performance plus large.
- **À retenir** : rendre le coût utile, visible et maîtrisable.
