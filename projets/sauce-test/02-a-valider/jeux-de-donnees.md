# Jeux de données — sauce-test

Données nécessaires aux cas de tests. Les profils sont les comptes de démonstration publics cités au CDC §10 ; le mot de passe n'est jamais écrit ici, il est fourni par la variable d'environnement `APP_PASSWORD`.

### JDD-001 — Profil standard
- **Type** : valide
- **Cas concernés** : CT0002, CT0004, CT0005, CT0010, CT0011, CT0012, CT0013, CT0014, CT0015, CT0016, CT0017, CT0018, CT0019, CT0020, CT0021, CT0022, CT0023, CT0024, CT0025, CT0026, CT0027, CT0028, CT0029, CT0030, CT0031, CT0032, CT0033, CT0034, CT0035, CT0036, CT0037, CT0038, CT0039, CT0041, CT0043, CT0044
- **Origine** : existante dans l'environnement (CDC §10)
- **Sensibilité** : identifiants (variables d'environnement)
- **Prérequis** : panier vide au début de chaque cas, sauf prérequis contraire (réinitialiser l'état de démonstration si besoin). Mot de passe confirmé sur la page de connexion (Q-002).

| Champ | Valeur | Remarque |
|---|---|---|
| Identifiant | `standard_user` (variable `APP_USERNAME`) | profil de démonstration public, CDC §10 |
| Mot de passe | variable `APP_PASSWORD` | jamais en clair |

### JDD-002 — Profil verrouillé
- **Type** : invalide
- **Cas concernés** : CT0008
- **Origine** : existante dans l'environnement (CDC §10)
- **Sensibilité** : identifiants (variables d'environnement)
- **Prérequis** : le profil reste verrouillé pendant la campagne ; même mot de passe que les autres profils (CDC §10, Q-002).

| Champ | Valeur | Remarque |
|---|---|---|
| Identifiant | `locked_out_user` | profil de démonstration public, CDC §10 |
| Mot de passe | variable `APP_PASSWORD` | mot de passe correct, jamais en clair |

### JDD-003 — Identifiants erronés
- **Type** : invalide
- **Cas concernés** : CT0006, CT0007
- **Origine** : fictive
- **Sensibilité** : aucune
- **Prérequis** : l'identifiant inconnu n'existe pas dans l'application.

| Champ | Valeur | Remarque |
|---|---|---|
| Identifiant inconnu | `utilisateur_inconnu_qa` | CT0006, avec le mot de passe `APP_PASSWORD` |
| Identifiant connu | `standard_user` | CT0007 |
| Mot de passe incorrect | `mot_de_passe_errone_01` | CT0007, valeur fictive non sensible |

### JDD-004 — Informations client valides
- **Type** : valide
- **Cas concernés** : CT0024, CT0025, CT0026, CT0027, CT0030, CT0042, CT0043
- **Origine** : fictive
- **Sensibilité** : aucune
- **Prérequis** : aucun. Valeurs fictives et non sensibles (CDC §10).

| Champ | Valeur | Remarque |
|---|---|---|
| Prénom | `Jean` | |
| Nom | `Recette` | |
| Code postal | `75001` | format non documenté (Q-007) |

### JDD-005 — Informations client avec caractères inhabituels
- **Type** : invalide
- **Cas concernés** : CT0029
- **Origine** : fictive
- **Sensibilité** : aucune
- **Prérequis** : aucun. Résultat attendu à confirmer (Q-007).

| Champ | Valeur | Remarque |
|---|---|---|
| Prénom | `Zoé-Anaïs` | accents et tiret |
| Nom | `O'Connor #2` | apostrophe, symbole et chiffre |
| Code postal | `AB-12 !` | lettres, tiret, espace et ponctuation |

### JDD-006 — Profil à latence
- **Type** : valide
- **Cas concernés** : CT0042
- **Origine** : existante dans l'environnement (CDC §10)
- **Sensibilité** : identifiants (variables d'environnement)
- **Prérequis** : comportement volontairement ralenti (CDC §4) ; traitement des écarts selon Q-018.

| Champ | Valeur | Remarque |
|---|---|---|
| Identifiant | `performance_glitch_user` | profil de démonstration public, CDC §10 |
| Mot de passe | variable `APP_PASSWORD` | jamais en clair |
