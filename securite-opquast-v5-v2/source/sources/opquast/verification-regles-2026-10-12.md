# Vérification MCP Opquast — Sécurité

- Date : 12 octobre 2026.
- Version demandée : `qualite-numerique`.
- État MCP : API publique et privée disponibles.
- Résultat : 39 règles présentes dans la source vérifiées individuellement ; toutes les réponses portent `source=api`.
- Usage : contrôle uniquement, sans enrichissement éditorial.

## Rubrique sécurité

- 197 — Toutes les pages utilisent le protocole HTTPS.
- 198 — Les certificats de sécurité sont signés et en cours de validité.
- 199 — Les pages utilisant HTTPS ont un entête de transport strict.
- 200 — Les pages utilisant le protocole HTTPS ne proposent pas de ressources HTTP.
- 201 — Les opérations relatives aux mots de passe peuvent être effectuées intégralement en ligne.
- 202 — Les mots de passe peuvent être choisis ou changés par l’utilisateur.
- 203 — Un dispositif sensibilise l’utilisateur sur le degré de sécurisation du mot de passe qu’il choisit.
- 204 — Les mots de passe peuvent être réinitialisés.
- 205 — Les mots de passe ne sont pas communiqués en clair.
- 206 — Les entêtes envoyés par le serveur désactivent la détection automatique du type MIME de chaque ressource.
- 207 — Le serveur indique le type MIME de chaque ressource.
- 208 — Les informations sur la sécurité des transactions sont indiquées.
- 209 — Le serveur n’envoie pas la liste des fichiers des répertoires n’ayant pas de page d’index.
- 210 — Le serveur envoie les informations d’activation de protection cross site scripting.
- 211 — Le serveur envoie les informations indiquant les domaines autorisés à intégrer ses pages dans des cadres.
- 212 — Un mécanisme de sécurité restreint l’origine des contenus.
- 213 — Le serveur ne communique pas d’informations sur les logiciels et langages utilisés.
- 214 — Le contrôle d’intégrité des ressources tierces est présent et valide.
- 215 — Les opérations sécurisées peuvent être validées par au moins deux moyens.
- 216 — L’affichage de la barre d’adresse du navigateur n’est pas bloqué.
- 217 — Le domaine de messagerie est authentifié.

## Règles transversales ou satellites présentes dans la source

- 14 — Les contenus ne détournent pas de caractères pour simuler une mise en forme visuelle.
- 17 — La création de compte est possible sans recours à un système d’identification tiers.
- 18 — La création d’un compte est soumise à un processus de confirmation.
- 19 — Un mécanisme de prévention des usurpations de compte ou d’identité est proposé.
- 22 — La connexion à tous les services proposés est possible avec les mêmes identifiants.
- 23 — Il est possible de se déconnecter des espaces privés.
- 25 — Les entêtes envoyés par le serveur spécifient la politique de communication des referrers.
- 26 — Aucune information n’est exposée sur l’existence d’un compte utilisateur.
- 27 — Les échanges de données sensibles sont sécurisés et signalés comme tels.
- 28 — Les données sensibles ne sont pas transmises en clair dans les URL.
- 60 — Les données bancaires mémorisées peuvent être modifiées ou supprimées.
- 75 — La création d’un mot de passe par l’utilisateur fait l’objet d’un mécanisme de prévention des erreurs de saisie.
- 76 — Les caractères saisis dans un champ de mot de passe peuvent être affichés en clair.
- 92 — Le copier-coller est possible dans les champs de formulaire.
- 96 — Les procédures d’authentification à double facteur peuvent être relancées.
- 97 — Les champs permettant l’autocomplétion sont signalés dans le code source.
- 172 — Les limites de temps imposées à une action ou un accès sont indiquées.
- 173 — L’inscription aux newsletters est soumise à un processus de confirmation.

## Verdict

- Numéros et libellés rejetés : 0.
- Données non actualisées : 0.
- Contenu ajouté depuis le MCP : 0.
- Contrôle : `measured` et `retrieved`.

