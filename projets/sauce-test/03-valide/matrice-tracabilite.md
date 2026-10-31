# Matrice de traçabilité exigences → cas de tests

Générée par `outils/controle.py`. Ne pas modifier.

| Fonctionnalité | Exigence | Criticité | Cas nominaux | Cas négatifs / limites | Types de test | Techniques ISTQB | Questions ouvertes |
|---|---|---|---|---|---|---|---|
| Authentification | EX-001 Afficher le formulaire de connexion | MAJOR | CT0001 | — | fonctionnel | criteres-acceptation | Q-001 |
| Authentification | EX-002 Ouvrir une session avec des identifiants valides | CRITICAL | CT0002 | — | fonctionnel | cas-d-usage | — |
| Authentification | EX-003 Contrôler les champs obligatoires de connexion | MAJOR | **aucun** | CT0003 (negatif), CT0004 (negatif), CT0005 (negatif) | fonctionnel | table-decision | Q-001 |
| Authentification | EX-004 Refuser l'accès en cas d'identifiants incorrects | CRITICAL | **aucun** | CT0006 (negatif), CT0007 (negatif) | fonctionnel | table-decision | Q-001 |
| Authentification | EX-005 Refuser la connexion d'un profil verrouillé | CRITICAL | **aucun** | CT0008 (negatif) | securite | table-decision | Q-001 |
| Authentification | EX-006 Exiger l'authentification avant d'accéder au catalogue | CRITICAL | **aucun** | CT0009 (negatif) | securite | transition-etats | Q-011 |
| Catalogue | EX-007 Afficher la liste des produits | MAJOR | CT0010 | — | fonctionnel | criteres-acceptation | — |
| Catalogue | EX-008 Consulter le détail d'un produit | MAJOR | CT0011 | — | fonctionnel | cas-d-usage | — |
| Catalogue | EX-009 Trier les produits | MAJOR | CT0012, CT0013, CT0014, CT0015 | — | fonctionnel | partitions-equivalence | Q-006 |
| Catalogue | EX-010 Trier sans modifier les données des produits | MAJOR | CT0016 | — | fonctionnel | criteres-acceptation | — |
| Panier | EX-011 Ajouter un produit au panier | CRITICAL | CT0017, CT0018 | — | fonctionnel | cas-d-usage | — |
| Panier | EX-012 Refléter l'ajout dans l'interface et l'indicateur du panier | MAJOR | CT0017, CT0018, CT0023 | — | fonctionnel | cas-d-usage, transition-etats | Q-003, Q-004 |
| Panier | EX-013 Consulter le contenu du panier | MAJOR | CT0019 | — | fonctionnel | cas-d-usage | Q-004 |
| Panier | EX-014 Conserver dans le panier les informations du catalogue | MAJOR | CT0019 | — | fonctionnel | cas-d-usage | — |
| Panier | EX-015 Retirer un produit du panier | MAJOR | CT0020, CT0021, CT0023 | — | fonctionnel | cas-d-usage, transition-etats | — |
| Panier | EX-016 Revenir au catalogue sans perdre le panier | MAJOR | CT0022 | — | fonctionnel | cas-d-usage | — |
| Commande | EX-017 Démarrer la commande depuis le panier | CRITICAL | CT0024 | — | fonctionnel | cas-d-usage | — |
| Commande | EX-018 Demander prénom, nom et code postal | MAJOR | CT0024 | CT0029 (negatif) | fonctionnel | cas-d-usage, devinette-erreurs | Q-007 |
| Commande | EX-019 Contrôler les informations obligatoires de commande | MAJOR | **aucun** | CT0025 (negatif), CT0026 (negatif), CT0027 (negatif), CT0028 (negatif), CT0029 (negatif) | fonctionnel | devinette-erreurs, partitions-equivalence | Q-001, Q-007 |
| Commande | EX-020 Afficher le récapitulatif de commande | MAJOR | CT0024, CT0030 | — | fonctionnel | cas-d-usage, criteres-acceptation | — |
| Commande | EX-021 Afficher un total cohérent avec le sous-total et les taxes | CRITICAL | CT0030 | — | fonctionnel | criteres-acceptation | Q-005 |
| Commande | EX-022 Confirmer la commande simulée | CRITICAL | CT0024 | — | fonctionnel | cas-d-usage | — |
| Commande | EX-023 Afficher l'écran de succès après confirmation | MAJOR | CT0024 | — | fonctionnel | cas-d-usage | Q-001 |
| Commande | EX-024 N'autoriser la confirmation qu'après les étapes précédentes | MAJOR | **aucun** | CT0031 (negatif) | fonctionnel | transition-etats | Q-008 |
| Navigation et session | EX-025 Proposer la déconnexion et la réinitialisation dans le menu | MAJOR | CT0032 | — | fonctionnel | criteres-acceptation | Q-009 |
| Navigation et session | EX-026 Se déconnecter depuis le menu | MAJOR | CT0033 | — | fonctionnel | transition-etats | — |
| Navigation et session | EX-027 Empêcher la poursuite d'une session déconnectée | CRITICAL | **aucun** | CT0034 (negatif) | securite | transition-etats | Q-012 |
| Navigation et session | EX-028 Réinitialiser l'état de démonstration | MAJOR | CT0035 | — | fonctionnel | cas-d-usage | Q-010 |
| Navigation et session | EX-029 Naviguer sans incohérence d'état | MAJOR | CT0036 | — | fonctionnel | cas-d-usage | Q-009 |
| Ergonomie et accessibilité | EX-030 Proposer des libellés compréhensibles et cohérents | MINOR | CT0041 | — | utilisabilite | checklist | Q-016 |
| Compatibilité | EX-031 Rester utilisable sur les navigateurs et tailles d'écran retenus | MAJOR | CT0043 | — | compatibilite | cas-d-usage | Q-014 |
| Performance | EX-032 Répondre dans un délai acceptable | MAJOR | CT0042 | — | performance | cas-d-usage | Q-013 |
| Fiabilité | EX-033 Ne pas perdre ni dupliquer d'articles | MAJOR | CT0038 | CT0037 (negatif) | fiabilite | criteres-acceptation, devinette-erreurs | Q-004 |
| Ergonomie et accessibilité | EX-034 Rendre les champs, contrôles et messages accessibles | MAJOR | CT0039, CT0040 | — | utilisabilite | checklist | Q-015 |
| Maintenabilité des tests | EX-035 Identifier de manière stable les éléments de l'interface | MINOR | CT0044 | — | maintenabilite | checklist | Q-017 |
