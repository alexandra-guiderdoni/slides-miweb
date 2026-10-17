# Prompt ImageGen - slide 28 V4

## Références visuelles obligatoires

- `navigation-opquast-v5-360/assets/slides/slide-01.png`
- `navigation-opquast-v5-360/assets/slides/slide-03.png`
- `navigation-opquast-v5-360/assets/slides/slide-10.png`
- `navigation-opquast-v5-360/assets/slides/slide-17.png`
- `securite-opquast-v5-v4/source/etalons/slide-23.png` - étalon V4 le plus proche

Ces cinq images sont fournies directement à ImageGen.

## Fiche PDS

- Rôle : traiter la règle 217 et fermer le chapitre E.
- Idée principale : SPF, DKIM et DMARC apportent trois preuves différentes reliées au courriel reçu.
- Scène : trois cartes convergent vers une enveloppe anonymisée.
- Transformation visible : trois contrôles distincts deviennent un verdict sur un message concret.

## Prompt complet

Créer une image finale de slide de formation institutionnelle française au format paysage 16:9, exactement 1672 x 941 pixels.

Suivre très fidèlement les cinq références : fond ivoire presque blanc, titre bleu marine massif, composition aérée, aplats pastel doux, illustration vectorielle plate aux traits fins, typographie proche de Marianne. Aucun dégradé, photographie, effet 3D, ombre lourde ni faux logo.

Masque V4 stable : micro-entête haut gauche, repère de chapitre et badge de règle, grand titre, trois cartes égales, contrôle bleu clair, limite orange très pâle, footer et pagination.

Scène : trois cartes parallèles `SPF`, `DKIM` et `DMARC`, chacune avec une icône et sa question exacte. Elles convergent vers une enveloppe de courriel anonymisée. Ne pas les présenter comme trois étapes successives ni comme des garanties équivalentes. Aucun domaine, adresse, IP, valeur DNS, entête réel ou fournisseur.

Texte visible exact, et absolument aucun autre texte :

- `QUALITÉ NUMÉRIQUE - OPQUAST V5`
- `E - CONFIANCE AU-DELÀ DE LA PAGE`
- `RÈGLE 217`
- `Authentifier le domaine qui envoie les courriels`
- `SPF - Qui peut envoyer ?`
- `DKIM - Le message est-il signé ?`
- `DMARC - Que faire si l'alignement échoue ?`
- `CONTRÔLE - DNS + entêtes d'un courriel réellement reçu`
- `LIMITE - Le DNS seul ne prouve pas l'application sur un message`
- `Opquast - présentation Miweb`
- `28 / 30`

Critères de rejet : texte manquant ou ajouté, faute, tiret absent, mauvais numéro ou pagination, mécanismes confondus, domaine ou donnée inventée, faux logo.
