# Jeux de données — SauceDemo

Données nécessaires aux cas de tests. Les identifiants réels ne sont jamais écrits ici : ils sont fournis par variables d'environnement.

### JDD-001 — Compte utilisateur standard
- **Type** : valide
- **Cas concernés** : CT0001, CT0002, CT0003, CT0005, CT0008, CT0009, CT0010, CT0011, CT0012, CT0013, CT0014, CT0015, CT0016, CT0017, CT0018, CT0019, CT0020, CT0021, CT0022, CT0023, CT0024, CT0025, CT0026, CT0027
- **Origine** : à fournir par le client
- **Sensibilité** : identifiants (variables d'environnement)
- **Prérequis** : compte actif, non verrouillé, panier vide au début de chaque cas.

| Champ | Valeur | Remarque |
|---|---|---|
| Nom d'utilisateur | variable `APP_USERNAME` | jamais en clair |
| Mot de passe | variable `APP_PASSWORD` | jamais en clair |

### JDD-002 — Compte verrouillé
- **Type** : invalide
- **Cas concernés** : CT0007
- **Origine** : à fournir par le client (voir Q-002)
- **Sensibilité** : identifiants (variables d'environnement)
- **Prérequis** : compte verrouillé par l'administrateur et qui le reste pendant la recette.

| Champ | Valeur | Remarque |
|---|---|---|
| Nom d'utilisateur | variable `APP_LOCKED_USERNAME` | jamais en clair |
| Mot de passe | variable `APP_LOCKED_PASSWORD` | jamais en clair |

### JDD-003 — Identifiants erronés
- **Type** : invalide
- **Cas concernés** : CT0005, CT0006
- **Origine** : fictive
- **Sensibilité** : aucune
- **Prérequis** : le nom d'utilisateur inconnu n'existe pas dans l'application.

| Champ | Valeur | Remarque |
|---|---|---|
| Nom d'utilisateur inconnu | `qa_utilisateur_inconnu` | ne doit correspondre à aucun compte |
| Mot de passe erroné | `Qa_Mauvais_MotDePasse_2026` | valeur fictive |

### JDD-004 — Informations de livraison valides
- **Type** : valide
- **Cas concernés** : CT0021, CT0022, CT0023, CT0024, CT0025
- **Origine** : fictive
- **Sensibilité** : aucune

| Champ | Valeur | Remarque |
|---|---|---|
| Prénom | `Awa` | |
| Nom | `Kouassi` | |
| Code postal | `00225` | format à confirmer (Q-008) |

### JDD-005 — Deux articles du catalogue
- **Type** : valide
- **Cas concernés** : CT0017, CT0018, CT0019, CT0020, CT0021, CT0025
- **Origine** : existante dans l'environnement
- **Sensibilité** : aucune
- **Prérequis** : au moins deux articles différents sont présents dans le catalogue.

| Champ | Valeur | Remarque |
|---|---|---|
| Article 1 | premier article du catalogue trié par nom de A à Z | relever son nom et son prix pendant le test |
| Article 2 | deuxième article du catalogue trié par nom de A à Z | relever son nom et son prix pendant le test |
