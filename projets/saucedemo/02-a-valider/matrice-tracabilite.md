# Matrice de traçabilité exigences → cas de tests

Générée par `outils/controle.py`. Ne pas modifier.

| Fonctionnalité | Exigence | Criticité | Cas nominaux | Cas négatifs / limites / autres | Questions ouvertes |
|---|---|---|---|---|---|
| Authentification | EX-001 Se connecter avec un nom d'utilisateur et un mot de passe | CRITICAL | CT0001 | — | — |
| Authentification | EX-002 Rendre obligatoires le nom d'utilisateur et le mot de passe | MAJOR | **aucun** | CT0002 (negatif), CT0003 (negatif), CT0004 (negatif) | Q-001 |
| Authentification | EX-003 Refuser des identifiants incorrects | CRITICAL | **aucun** | CT0005 (negatif), CT0006 (negatif) | Q-001 |
| Authentification | EX-004 Refuser la connexion d'un compte verrouillé | MAJOR | **aucun** | CT0007 (negatif) | Q-001, Q-002 |
| Authentification | EX-005 Se déconnecter depuis le menu latéral | MAJOR | CT0009 | CT0010 (securite) | — |
| Catalogue | EX-006 Afficher le catalogue des articles | MAJOR | CT0011 | — | — |
| Catalogue | EX-007 Trier le catalogue par nom ou par prix | MAJOR | CT0012, CT0013, CT0014, CT0015 | — | — |
| Catalogue | EX-008 Consulter la fiche détaillée d'un article | MINOR | CT0016 | — | — |
| Panier | EX-009 Ajouter un article au panier | CRITICAL | CT0017 | — | — |
| Panier | EX-010 Consulter et modifier le contenu du panier | MAJOR | CT0018, CT0019 | — | Q-009 |
| Panier | EX-011 Conserver le panier pendant la navigation | MAJOR | CT0020 | — | Q-006 |
| Commande | EX-012 Saisir les informations de commande obligatoires | CRITICAL | CT0021 | CT0022 (negatif), CT0023 (negatif), CT0024 (negatif) | Q-001, Q-008 |
| Commande | EX-013 Afficher un récapitulatif de commande au total exact | CRITICAL | CT0021, CT0025 | — | Q-003, Q-007 |
| Commande | EX-014 Valider la commande et vider le panier | CRITICAL | CT0021, CT0026 | — | Q-007 |
| Commande | EX-015 Interdire une commande avec un panier vide | MAJOR | **aucun** | CT0027 (negatif) | Q-005 |
| Exigences non fonctionnelles | EX-016 Offrir des temps de réponse rapides | MINOR | **aucun** | — | Q-004 |
| Authentification | EX-017 Ne jamais afficher les mots de passe en clair | MAJOR | **aucun** | CT0008 (securite) | — |
