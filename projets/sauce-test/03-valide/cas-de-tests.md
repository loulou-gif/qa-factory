<!-- Fichier généré par outils/rendre_revue.py à partir de cas-de-tests.json — NE PAS MODIFIER. empreinte: abe2f7f4553d1e8f -->
# Cas de tests — sauce-test (version 1)

Vue de relecture. Pour corriger : `/corriger sauce-test <demande>` (le JSON est modifié, puis cette vue est régénérée).

Sources analysées : 01-entrant/Cahier_des_charges_SauceDemo.pdf

## Synthèse

| Indicateur | Valeur |
|---|---|
| Fonctionnalités | 10 |
| Exigences | 35 |
| Cas de tests | 44 |
| Cas négatif | 15 |
| Cas nominal | 29 |
| Type de test : test de compatibilité | 1 |
| Type de test : test de fiabilité | 2 |
| Type de test : test fonctionnel (adéquation fonctionnelle) | 33 |
| Type de test : test de maintenabilité | 1 |
| Type de test : test de performance (rendement) | 1 |
| Type de test : test de sécurité | 3 |
| Type de test : test d'utilisabilité (dont accessibilité) | 3 |
| Technique : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA) | 13 |
| Technique : Test basé sur des checklists (CTFL v4.0 §4.4.3) | 4 |
| Technique : Critères d'acceptation (CTFL v4.0 §4.5.2) | 6 |
| Technique : Estimation d'erreurs (CTFL v4.0 §4.4.1) | 3 |
| Technique : Partitions d'équivalence (CTFL v4.0 §4.2.1) | 7 |
| Technique : Tables de décision (CTFL v4.0 §4.2.3) | 6 |
| Technique : Test de transition d'états (CTFL v4.0 §4.2.4) | 5 |
| Questions ouvertes | 18 (dont bloquantes : 2) |

## Stratégie de types de tests (ISTQB)

Chaque type de test ISTQB est examiné : retenu, non retenu (avec la raison) ou à confirmer (avec une question).

| ID | Type de test | Décision | Niveau | Approche | Objectif | Exigences | Cas | Outil | Justification | Questions |
|---|---|---|---|---|---|---|---|---|---|---|
| TT-01 | Test fonctionnel (adéquation fonctionnelle) | Retenu | systeme | Cas de tests de ce fichier | Vérifier les exigences fonctionnelles du CDC §5 et les règles de gestion §6 (authentification, catalogue, panier, commande, navigation). Compléter en temps B par une session exploratoire avec le profil à comportement dégradé. | EX-001, EX-002, EX-003, EX-004, EX-007, EX-008, EX-009, EX-010, EX-011, EX-012, EX-013, EX-014, EX-015, EX-016, EX-017, EX-018, EX-019, EX-020, EX-021, EX-022, EX-023, EX-024, EX-025, EX-026, EX-028, EX-029 | CT0001, CT0002, CT0003, CT0004, CT0005, CT0006, CT0007, CT0010, CT0011, CT0012, CT0013, CT0014, CT0015, CT0016, CT0017, CT0018, CT0019, CT0020, CT0021, CT0022, CT0023, CT0024, CT0025, CT0026, CT0027, CT0028, CT0029, CT0030, CT0031, CT0032, CT0033, CT0035, CT0036 | Squash TM (exécution manuelle), Playwright (automatisation) | CDC §5 et §6 : exigences fonctionnelles explicites ; CDC §4 et §10 : profil problem_user prévu pour explorer les anomalies. | Q-018 |
| TT-02 | Test de sécurité | Retenu | systeme | Cas de tests de ce fichier | Vérifier le contrôle d'accès : refus du profil verrouillé, accès interdit sans session, session non réutilisable après déconnexion. | EX-005, EX-006, EX-027 | CT0008, CT0009, CT0034 | Playwright | CDC §6 RG-01, RG-02 et §7 Sécurité de session. Aucun test intrusif (injection, force brute, scan) : non demandé par le CDC et application publique d'un tiers, sans autorisation écrite ni environnement dédié. |  |
| TT-03 | Test de performance (rendement) | À confirmer | systeme | Campagne dédiée | Relever les temps de réponse du parcours d'achat, en particulier avec le profil à latence. | EX-032 | CT0042 | Chronométrage manuel ou traces du navigateur ; pas d'outil de charge | CDC §7 Performance : « délai acceptable » non mesurable. Pas de test de charge sur une application publique d'un tiers. | Q-013 |
| TT-04 | Test d'utilisabilité (dont accessibilité) | Retenu | systeme | Checklist | Contrôler l'accessibilité (champs identifiables, clavier, messages perceptibles) et la cohérence des libellés. | EX-030, EX-034 | CT0039, CT0040, CT0041 | Checklist RGAA ou WCAG (à confirmer), axe | CDC §7 Ergonomie et Accessibilité : exigences présentes ; référentiel et niveau de conformité à confirmer. | Q-015, Q-016 |
| TT-05 | Test de compatibilité | À confirmer | systeme | Cas de tests de ce fichier | Exécuter le parcours d'achat sur les navigateurs et tailles d'écran retenus. | EX-031 | CT0043 | Playwright (projets multi-navigateurs) | CDC §7 Compatibilité : navigateurs et tailles d'écran « retenus pour la campagne » non listés. | Q-014 |
| TT-06 | Test de fiabilité | Retenu | systeme | Cas de tests de ce fichier | Vérifier l'absence de perte ou de duplication d'articles lors d'actions répétées et de changements d'écran. | EX-033 | CT0037, CT0038 | Squash TM, Playwright | CDC §7 Fiabilité : exigence vérifiable par des actions répétées sur le panier. |  |
| TT-07 | Test de maintenabilité | À confirmer | systeme | Checklist | Vérifier que les éléments de l'interface sont identifiables de manière stable pour l'automatisation. | EX-035 | CT0044 | Outils de développement du navigateur, pendant l'exploration | CDC §7 Maintenabilité des tests : critère de stabilité non défini. | Q-017 |
| TT-08 | Test de portabilité | Non retenu |  |  |  |  |  |  | Application web publique sans installation ni déploiement à la charge de l'équipe de test ; aucune exigence de portabilité dans le CDC (la compatibilité navigateurs est traitée en TT-05). |  |
| TT-09 | Test de confirmation (re-test d'une anomalie corrigée) | Retenu | systeme | Cas de tests de ce fichier | Rejouer les cas en échec après correction de chaque anomalie signalée. |  |  | Squash TM | Pratique standard de recette ; CDC §12 prévoit des rapports d'anomalies. |  |
| TT-10 | Test de régression | Retenu | systeme | Cas de tests de ce fichier | Rejouer les parcours critiques A à D à chaque évolution de l'application publique. |  | CT0002, CT0008, CT0017, CT0019, CT0020, CT0024, CT0030, CT0033, CT0035 | Playwright (suite automatisée) | CDC §2 et §12 : suite de fumée et de régression sur les parcours critiques ; CDC §11 : l'application publique peut évoluer. |  |

## Authentification

### Exigences

| ID | Exigence | Criticité | Source | Questions |
|---|---|---|---|---|
| EX-001 | **Afficher le formulaire de connexion**<br>Le système affiche un formulaire de connexion comportant un champ identifiant, un champ mot de passe et une action de connexion. | MAJOR | CDC §5.1 EF-AUTH-01 | Q-001 |
| EX-002 | **Ouvrir une session avec des identifiants valides**<br>Lorsque les identifiants sont valides pour un profil autorisé, le système ouvre une session et redirige l'utilisateur vers le catalogue. | CRITICAL | CDC §5.1 EF-AUTH-02, §9 Connexion |  |
| EX-003 | **Contrôler les champs obligatoires de connexion**<br>Lorsque les champs obligatoires sont vides, le système affiche un message de validation et empêche la connexion. | MAJOR | CDC §5.1 EF-AUTH-03, §9 Connexion | Q-001 |
| EX-004 | **Refuser l'accès en cas d'identifiants incorrects**<br>Lorsque les identifiants sont incorrects, le système refuse l'accès et affiche un message d'erreur compréhensible ; l'utilisateur reste sur l'écran de connexion. | CRITICAL | CDC §5.1 EF-AUTH-04, §8 Parcours C | Q-001 |
| EX-005 | **Refuser la connexion d'un profil verrouillé**<br>Un profil verrouillé ne peut pas ouvrir une session, même si le mot de passe saisi est correct ; la connexion est refusée avec un message explicite. | CRITICAL | CDC §4, §5.1 EF-AUTH-04, §6 RG-02 | Q-001 |
| EX-006 | **Exiger l'authentification avant d'accéder au catalogue**<br>Un utilisateur doit être authentifié avant d'accéder au catalogue et aux fonctionnalités réservées à une session. | CRITICAL | CDC §4 Visiteur non connecté, §6 RG-01 | Q-011 |

### Cas de tests

#### CT0001 — Afficher le formulaire de connexion

- **Exigences** : EX-001
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Critères d'acceptation (CTFL v4.0 §4.5.2)
- **Prérequis** : Être déconnecté. Avoir le lien de l'application.
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ouvrir le lien de l'application | L'écran de connexion s'affiche avec un champ identifiant, un champ mot de passe et une action de connexion. |

#### CT0002 — Se connecter avec le profil standard

- **Exigences** : EX-002
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : VERY_HIGH
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être déconnecté, sur l'écran de connexion. Disposer du profil standard JDD-001.
- **Objectif** : Parcours A, étapes 1 à 3 ; colonne R7 de la table de décision décrite dans CT0003.
- **Jeux de données** : JDD-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Renseigner l'identifiant et le mot de passe du profil JDD-001 | Les deux champs sont remplis. |
| 2 | Déclencher l'action de connexion | La session est ouverte et le catalogue des produits s'affiche. |

#### CT0003 — Bloquer la connexion avec les deux champs vides

- **Exigences** : EX-003
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Tables de décision (CTFL v4.0 §4.2.3)
- **Prérequis** : Être déconnecté, sur l'écran de connexion.
- **Objectif** : Table de décision de la connexion (CDC §5.1 EF-AUTH-02 à 04, §6 RG-02). Conditions : C1 identifiant renseigné, C2 mot de passe renseigné, C3 identifiant connu, C4 mot de passe correct, C5 profil verrouillé. Actions : A1 message de validation, A2 message d'erreur, A3 ouverture de session et catalogue. R1 : C1=N, C2=N -> A1 (CT0003). R2 : C1=N, C2=O -> A1 (CT0004). R3 : C1=O, C2=N -> A1 (CT0005). R4 : C1=O, C2=O, C3=N -> A2 (CT0006). R5 : C3=O, C4=N, C5=N -> A2 (CT0007). R6 : C3=O, C4=O, C5=O -> A2 (CT0008). R7 : C3=O, C4=O, C5=N -> A3 (CT0002). Colonne écartée : profil verrouillé avec mot de passe incorrect, refusée par R5 comme tout mot de passe incorrect.
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Laisser les champs identifiant et mot de passe vides | Les deux champs sont vides. |
| 2 | Déclencher l'action de connexion | Un message de validation s'affiche ; la connexion est empêchée et l'écran de connexion reste affiché. |

#### CT0004 — Bloquer la connexion sans identifiant

- **Exigences** : EX-003
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Tables de décision (CTFL v4.0 §4.2.3)
- **Prérequis** : Être déconnecté, sur l'écran de connexion. Disposer du mot de passe JDD-001.
- **Objectif** : Colonne R2 de la table de décision (CT0003).
- **Jeux de données** : JDD-001
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Laisser le champ identifiant vide et renseigner le mot de passe JDD-001 | Seul le champ mot de passe est rempli. |
| 2 | Déclencher l'action de connexion | Un message de validation s'affiche ; la connexion est empêchée et l'écran de connexion reste affiché. |

#### CT0005 — Bloquer la connexion sans mot de passe

- **Exigences** : EX-003
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Tables de décision (CTFL v4.0 §4.2.3)
- **Prérequis** : Être déconnecté, sur l'écran de connexion. Disposer de l'identifiant JDD-001.
- **Objectif** : Colonne R3 de la table de décision (CT0003).
- **Jeux de données** : JDD-001
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Renseigner l'identifiant JDD-001 et laisser le champ mot de passe vide | Seul le champ identifiant est rempli. |
| 2 | Déclencher l'action de connexion | Un message de validation s'affiche ; la connexion est empêchée et l'écran de connexion reste affiché. |

#### CT0006 — Refuser la connexion avec un identifiant inconnu

- **Exigences** : EX-004
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Tables de décision (CTFL v4.0 §4.2.3)
- **Prérequis** : Être déconnecté, sur l'écran de connexion.
- **Objectif** : Colonne R4 de la table de décision (CT0003). Parcours C.
- **Jeux de données** : JDD-003
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Renseigner l'identifiant inconnu et le mot de passe du jeu JDD-003 | Les deux champs sont remplis. |
| 2 | Déclencher l'action de connexion | L'accès est refusé : un message d'erreur s'affiche et l'écran de connexion reste affiché. |

#### CT0007 — Refuser la connexion avec un mot de passe incorrect

- **Exigences** : EX-004
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Tables de décision (CTFL v4.0 §4.2.3)
- **Prérequis** : Être déconnecté, sur l'écran de connexion.
- **Objectif** : Colonne R5 de la table de décision (CT0003). Parcours C.
- **Jeux de données** : JDD-003
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Renseigner l'identifiant du profil standard et le mot de passe incorrect du jeu JDD-003 | Les deux champs sont remplis. |
| 2 | Déclencher l'action de connexion | L'accès est refusé : un message d'erreur s'affiche et l'écran de connexion reste affiché. |

#### CT0008 — Refuser la connexion d'un profil verrouillé

- **Exigences** : EX-005
- **Nature** : Négatif — **Type de test** : Test de sécurité — **Importance** : HIGH
- **Technique ISTQB** : Tables de décision (CTFL v4.0 §4.2.3)
- **Prérequis** : Être déconnecté, sur l'écran de connexion. Disposer du profil verrouillé JDD-002.
- **Objectif** : Colonne R6 de la table de décision (CT0003). Parcours C.
- **Jeux de données** : JDD-002
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Renseigner l'identifiant et le mot de passe correct du profil JDD-002 | Les deux champs sont remplis. |
| 2 | Déclencher l'action de connexion | La connexion est refusée : un message explicite s'affiche, aucune session n'est ouverte et l'écran de connexion reste affiché. |

#### CT0009 — Refuser l'accès au catalogue sans session

- **Exigences** : EX-006
- **Nature** : Négatif — **Type de test** : Test de sécurité — **Importance** : HIGH
- **Technique ISTQB** : Test de transition d'états (CTFL v4.0 §4.2.4)
- **Prérequis** : État de départ : non authentifié (aucune session ouverte dans le navigateur). Avoir relevé l'adresse de la page catalogue lors d'une session précédente.
- **Objectif** : Session : états non authentifié et authentifié. Transitions valides : connexion (CT0002), déconnexion (CT0033). Transition invalide visée : non authentifié -> catalogue.
- **Questions liées** : Q-011

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ouvrir directement l'adresse de la page catalogue | Le catalogue ne s'affiche pas. |
| 2 | Observer l'écran obtenu | L'utilisateur est sur l'écran de connexion ou reçoit une indication que l'authentification est nécessaire (comportement exact à confirmer, Q-011). |

## Catalogue

### Exigences

| ID | Exigence | Criticité | Source | Questions |
|---|---|---|---|---|
| EX-007 | **Afficher la liste des produits**<br>Après connexion, le système affiche une liste de produits avec au minimum leur nom, image, description et prix. | MAJOR | CDC §5.2 EF-CAT-01, §9 Catalogue |  |
| EX-008 | **Consulter le détail d'un produit**<br>L'utilisateur peut consulter la fiche ou le détail d'un produit. | MAJOR | CDC §3 Détail produit, §5.2 EF-CAT-02 |  |
| EX-009 | **Trier les produits**<br>L'utilisateur peut trier les produits par nom croissant, nom décroissant, prix croissant et prix décroissant ; chaque option de tri produit l'ordre attendu. | MAJOR | CDC §5.2 EF-CAT-03, §9 Catalogue | Q-006 |
| EX-010 | **Trier sans modifier les données des produits**<br>Le tri doit réordonner les produits affichés sans modifier les données propres aux produits. | MAJOR | CDC §5.2 EF-CAT-04 |  |

### Cas de tests

#### CT0010 — Afficher la liste des produits avec leurs informations

- **Exigences** : EX-007
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Critères d'acceptation (CTFL v4.0 §4.5.2)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Être sur le catalogue.
- **Jeux de données** : JDD-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Parcourir la liste des produits du catalogue | Chaque produit affiche au minimum un nom, une image, une description et un prix. |

#### CT0011 — Consulter le détail d'un produit

- **Exigences** : EX-008
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Être sur le catalogue.
- **Jeux de données** : JDD-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Relever le nom et le prix d'un produit du catalogue | Le nom et le prix sont notés. |
| 2 | Ouvrir la fiche de ce produit depuis le catalogue | La fiche du produit sélectionné s'affiche avec le nom et le prix relevés. |

#### CT0012 — Trier les produits par nom croissant

- **Exigences** : EX-009
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Partitions d'équivalence (CTFL v4.0 §4.2.1)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Être sur le catalogue.
- **Objectif** : Option de tri : 4 partitions valides documentées (nom croissant, nom décroissant, prix croissant, prix décroissant), un cas par partition. Aucune partition invalide possible depuis l'interface.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-006

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Choisir l'option de tri par nom croissant | Les produits sont affichés par ordre alphabétique croissant de leur nom. |

#### CT0013 — Trier les produits par nom décroissant

- **Exigences** : EX-009
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Partitions d'équivalence (CTFL v4.0 §4.2.1)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Être sur le catalogue.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-006

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Choisir l'option de tri par nom décroissant | Les produits sont affichés par ordre alphabétique décroissant de leur nom. |

#### CT0014 — Trier les produits par prix croissant

- **Exigences** : EX-009
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Partitions d'équivalence (CTFL v4.0 §4.2.1)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Être sur le catalogue.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-006

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Choisir l'option de tri par prix croissant | Les produits sont affichés du prix le plus bas au prix le plus élevé. |

#### CT0015 — Trier les produits par prix décroissant

- **Exigences** : EX-009
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Partitions d'équivalence (CTFL v4.0 §4.2.1)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Être sur le catalogue.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-006

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Choisir l'option de tri par prix décroissant | Les produits sont affichés du prix le plus élevé au prix le plus bas. |

#### CT0016 — Conserver les données des produits après un tri

- **Exigences** : EX-010
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Critères d'acceptation (CTFL v4.0 §4.5.2)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Être sur le catalogue.
- **Jeux de données** : JDD-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Relever le nom, la description et le prix de deux produits | Les données des deux produits sont notées. |
| 2 | Appliquer successivement deux options de tri différentes | L'ordre des produits change. |
| 3 | Comparer les données des deux produits avec celles relevées | Le nom, la description et le prix de chaque produit sont identiques aux valeurs relevées. |

## Panier

### Exigences

| ID | Exigence | Criticité | Source | Questions |
|---|---|---|---|---|
| EX-011 | **Ajouter un produit au panier**<br>L'utilisateur peut ajouter un produit au panier depuis le catalogue ou depuis sa fiche détaillée. | CRITICAL | CDC §5.3 EF-CART-01 |  |
| EX-012 | **Refléter l'ajout dans l'interface et l'indicateur du panier**<br>Après ajout, l'interface doit refléter l'état du produit et mettre à jour l'indicateur du panier. L'indicateur représente le nombre d'articles ajoutés selon le fonctionnement de l'application. | MAJOR | CDC §5.3 EF-CART-02, §6 RG-03 | Q-003, Q-004 |
| EX-013 | **Consulter le contenu du panier**<br>L'utilisateur peut ouvrir le panier et consulter les produits sélectionnés, leurs prix et les quantités affichées. | MAJOR | CDC §5.3 EF-CART-03 | Q-004 |
| EX-014 | **Conserver dans le panier les informations du catalogue**<br>Un produit ajouté doit apparaître dans le panier avec les mêmes informations de référence que dans le catalogue. | MAJOR | CDC §6 RG-04, §9 Panier |  |
| EX-015 | **Retirer un produit du panier**<br>L'utilisateur peut retirer un produit du panier ; le contenu du panier et son indicateur doivent être actualisés. Le retrait est aussi possible depuis le détail produit. | MAJOR | CDC §3 Détail produit, §5.3 EF-CART-04, §6 RG-05 |  |
| EX-016 | **Revenir au catalogue sans perdre le panier**<br>L'utilisateur peut revenir au catalogue sans perdre l'état courant du panier pendant le parcours. | MAJOR | CDC §5.3 EF-CART-05, §8 Parcours B |  |

### Cas de tests

#### CT0017 — Ajouter un produit au panier depuis le catalogue

- **Exigences** : EX-011, EX-012
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : VERY_HIGH
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier est vide (réinitialiser l'état de démonstration si besoin).
- **Objectif** : Parcours A, étape 5.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-003, Q-004

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ajouter un produit au panier depuis le catalogue | L'état du produit change dans le catalogue pour indiquer qu'il est dans le panier (forme exacte à confirmer, Q-003). |
| 2 | Observer l'indicateur du panier | L'indicateur du panier affiche 1. |

#### CT0018 — Ajouter un produit au panier depuis sa fiche détaillée

- **Exigences** : EX-011, EX-012
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier est vide (réinitialiser l'état de démonstration si besoin). Être sur la fiche d'un produit.
- **Objectif** : Scénario alternatif d'EF-CART-01.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-003, Q-004

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ajouter le produit au panier depuis sa fiche | L'état du produit change sur la fiche pour indiquer qu'il est dans le panier (forme exacte à confirmer, Q-003). |
| 2 | Observer l'indicateur du panier | L'indicateur du panier affiche 1. |

#### CT0019 — Consulter le panier contenant plusieurs produits

- **Exigences** : EX-013, EX-014
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier est vide (réinitialiser l'état de démonstration si besoin).
- **Objectif** : Parcours B, étapes 2 et 3.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-004

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Relever le nom et le prix de deux produits du catalogue, puis les ajouter au panier | L'indicateur du panier affiche 2. |
| 2 | Ouvrir le panier | Le panier liste les deux produits ajoutés, avec un prix et une quantité pour chacun. |
| 3 | Comparer le nom et le prix de chaque produit avec ceux relevés dans le catalogue | Le nom et le prix de chaque produit sont identiques à ceux du catalogue. |

#### CT0020 — Retirer un produit depuis le panier

- **Exigences** : EX-015
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient deux produits.
- **Objectif** : Parcours B, étapes 4 et 5.
- **Jeux de données** : JDD-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ouvrir le panier | Le panier liste les deux produits et l'indicateur affiche 2. |
| 2 | Retirer un des deux produits | Le produit retiré n'apparaît plus dans le panier ; l'autre produit est toujours listé. |
| 3 | Observer l'indicateur du panier | L'indicateur du panier affiche 1. |

#### CT0021 — Retirer un produit depuis sa fiche détaillée

- **Exigences** : EX-015
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient un seul produit. Être sur la fiche de ce produit.
- **Objectif** : Scénario alternatif : retrait depuis le détail produit (CDC §3).
- **Jeux de données** : JDD-001
- **Questions liées** : Q-003, Q-004

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Retirer le produit du panier depuis sa fiche | L'état du produit sur la fiche indique qu'il n'est plus dans le panier. |
| 2 | Ouvrir le panier | Le panier ne contient plus le produit et l'indicateur n'affiche plus de quantité (affichage exact à confirmer, Q-004). |

#### CT0022 — Revenir au catalogue sans perdre le panier

- **Exigences** : EX-016
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient deux produits.
- **Objectif** : Parcours B, étape 5.
- **Jeux de données** : JDD-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ouvrir le panier | Le panier liste les deux produits. |
| 2 | Revenir au catalogue par la commande de navigation proposée | Le catalogue s'affiche ; l'indicateur du panier affiche toujours 2. |
| 3 | Ouvrir de nouveau le panier | Le panier liste toujours les deux mêmes produits. |

#### CT0023 — Faire évoluer l'indicateur du panier de vide à deux articles puis à vide

- **Exigences** : EX-012, EX-015
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Test de transition d'états (CTFL v4.0 §4.2.4)
- **Prérequis** : Être connecté avec le profil standard JDD-001. État de départ : panier vide.
- **Objectif** : États du panier : vide, 1 article, plusieurs articles (CDC RG-03, RG-05). Couverture de toutes les transitions valides par ajout et retrait.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-004

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ajouter un premier produit depuis le catalogue | Transition vide -> 1 article : l'indicateur affiche 1. |
| 2 | Ajouter un second produit | Transition 1 -> 2 articles : l'indicateur affiche 2. |
| 3 | Retirer le premier produit | Transition 2 -> 1 article : l'indicateur affiche 1. |
| 4 | Retirer le second produit | Transition 1 article -> vide : l'indicateur n'affiche plus de quantité (affichage exact à confirmer, Q-004). |

## Commande

### Exigences

| ID | Exigence | Criticité | Source | Questions |
|---|---|---|---|---|
| EX-017 | **Démarrer la commande depuis le panier**<br>Depuis le panier, l'utilisateur peut démarrer le processus de commande. | CRITICAL | CDC §5.4 EF-CMD-01 |  |
| EX-018 | **Demander prénom, nom et code postal**<br>Le système demande les informations nécessaires à la commande : prénom, nom et code postal. | MAJOR | CDC §5.4 EF-CMD-02 | Q-007 |
| EX-019 | **Contrôler les informations obligatoires de commande**<br>Les champs obligatoires doivent être contrôlés et renseignés avant le passage à l'étape suivante. | MAJOR | CDC §5.4 EF-CMD-03, §6 RG-06, §9 Commande | Q-001, Q-007 |
| EX-020 | **Afficher le récapitulatif de commande**<br>Le système affiche un récapitulatif des articles, le sous-total, les taxes et le total. | MAJOR | CDC §5.4 EF-CMD-04, §9 Commande |  |
| EX-021 | **Afficher un total cohérent avec le sous-total et les taxes**<br>Le total affiché doit être cohérent avec le sous-total et les taxes calculées par l'application. Les règles de calcul exactes (taux, arrondis, quantités) sont à vérifier sur l'environnement cible. | CRITICAL | CDC §6 RG-07 et note, §11 Risques | Q-005 |
| EX-022 | **Confirmer la commande simulée**<br>L'utilisateur peut confirmer la commande simulée. Aucun paiement réel n'est attendu. | CRITICAL | CDC §1, §5.4 EF-CMD-05 |  |
| EX-023 | **Afficher l'écran de succès après confirmation**<br>Après confirmation, le système affiche un écran de succès et un message confirmant la fin du parcours. | MAJOR | CDC §5.4 EF-CMD-06, §9 Commande | Q-001 |
| EX-024 | **N'autoriser la confirmation qu'après les étapes précédentes**<br>La confirmation de commande n'est possible qu'après validation des étapes précédentes. | MAJOR | CDC §6 RG-08 | Q-008 |

### Cas de tests

#### CT0024 — Passer une commande complète avec le profil standard

- **Exigences** : EX-017, EX-018, EX-020, EX-022, EX-023
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : VERY_HIGH
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient deux produits. Disposer des informations client JDD-004.
- **Objectif** : Parcours A, étapes 6 à 9.
- **Jeux de données** : JDD-001, JDD-004
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ouvrir le panier et démarrer la commande | Le système demande le prénom, le nom et le code postal. |
| 2 | Renseigner les informations client JDD-004 et passer à l'étape suivante | Le récapitulatif s'affiche avec les deux articles, le sous-total, les taxes et le total. |
| 3 | Confirmer la commande | Un écran de succès s'affiche avec un message confirmant la fin du parcours. |

#### CT0025 — Bloquer la commande sans prénom

- **Exigences** : EX-019
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Partitions d'équivalence (CTFL v4.0 §4.2.1)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient un produit. Être sur l'étape des informations client.
- **Objectif** : Chaque champ obligatoire : partition valide (renseigné), partition invalide (vide). Une seule partition invalide par cas.
- **Jeux de données** : JDD-001, JDD-004
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Laisser le prénom vide, renseigner le nom et le code postal JDD-004 | Seul le prénom est vide. |
| 2 | Passer à l'étape suivante | Le passage est empêché : un message de validation s'affiche et l'étape des informations client reste affichée. |

#### CT0026 — Bloquer la commande sans nom

- **Exigences** : EX-019
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Partitions d'équivalence (CTFL v4.0 §4.2.1)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient un produit. Être sur l'étape des informations client.
- **Jeux de données** : JDD-001, JDD-004
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Laisser le nom vide, renseigner le prénom et le code postal JDD-004 | Seul le nom est vide. |
| 2 | Passer à l'étape suivante | Le passage est empêché : un message de validation s'affiche et l'étape des informations client reste affichée. |

#### CT0027 — Bloquer la commande sans code postal

- **Exigences** : EX-019
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Partitions d'équivalence (CTFL v4.0 §4.2.1)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient un produit. Être sur l'étape des informations client.
- **Jeux de données** : JDD-001, JDD-004
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Laisser le code postal vide, renseigner le prénom et le nom JDD-004 | Seul le code postal est vide. |
| 2 | Passer à l'étape suivante | Le passage est empêché : un message de validation s'affiche et l'étape des informations client reste affichée. |

#### CT0028 — Bloquer la commande avec toutes les informations vides

- **Exigences** : EX-019
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Estimation d'erreurs (CTFL v4.0 §4.4.1)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient un produit. Être sur l'étape des informations client.
- **Objectif** : Erreur visée : formulaire soumis entièrement vide (jeu « vide » demandé par CDC §10).
- **Jeux de données** : JDD-001
- **Questions liées** : Q-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Laisser le prénom, le nom et le code postal vides | Les trois champs sont vides. |
| 2 | Passer à l'étape suivante | Le passage est empêché : un message de validation s'affiche et l'étape des informations client reste affichée. |

#### CT0029 — Saisir des caractères inhabituels dans les informations client — **suspendu à une question bloquante**

- **Exigences** : EX-018, EX-019
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Estimation d'erreurs (CTFL v4.0 §4.4.1)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient un produit. Être sur l'étape des informations client.
- **Objectif** : Erreur visée : caractères spéciaux, accents, apostrophes, lettres dans le code postal (jeu « caractères inhabituels » demandé par CDC §10). Résultat attendu non documenté.
- **Jeux de données** : JDD-001, JDD-005
- **Questions liées** : Q-007

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Renseigner le prénom, le nom et le code postal avec les valeurs du jeu JDD-005 | Les trois champs sont remplis. |
| 2 | Passer à l'étape suivante | Le système accepte ou refuse la saisie selon la règle à confirmer (Q-007) ; en cas de refus, un message de validation s'affiche. |

#### CT0030 — Vérifier la cohérence des montants du récapitulatif

- **Exigences** : EX-020, EX-021
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Critères d'acceptation (CTFL v4.0 §4.5.2)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient deux produits dont les prix ont été relevés dans le catalogue. Disposer des informations client JDD-004.
- **Objectif** : Parcours A, étape 8.
- **Jeux de données** : JDD-001, JDD-004
- **Questions liées** : Q-005

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Démarrer la commande, renseigner les informations JDD-004 et passer à l'étape suivante | Le récapitulatif affiche les deux articles avec les mêmes noms et prix que dans le catalogue. |
| 2 | Relever le sous-total, les taxes et le total affichés | Les trois montants sont affichés. |
| 3 | Comparer le total à la somme du sous-total et des taxes | Le total est égal au sous-total augmenté des taxes (interprétation de « cohérent » à confirmer, Q-005). |

#### CT0031 — Empêcher la confirmation sans avoir validé les informations client — **suspendu à une question bloquante**

- **Exigences** : EX-024
- **Nature** : Négatif — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Test de transition d'états (CTFL v4.0 §4.2.4)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient un produit. Avoir relevé, lors d'une commande précédente, l'adresse de l'étape récapitulatif.
- **Objectif** : États de la commande : panier, informations client, récapitulatif, confirmée. Transitions valides couvertes par CT0024. Transition invalide visée : informations client non validées -> récapitulatif -> confirmée.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-008

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Démarrer la commande sans renseigner les informations client | L'étape des informations client s'affiche. |
| 2 | Ouvrir directement l'adresse de l'étape récapitulatif | La confirmation de la commande n'est pas possible (comportement exact à confirmer, Q-008). |
| 3 | Ouvrir le catalogue puis le panier | Aucune commande n'a été confirmée : le panier contient toujours le produit. |

## Navigation et session

### Exigences

| ID | Exigence | Criticité | Source | Questions |
|---|---|---|---|---|
| EX-025 | **Proposer la déconnexion et la réinitialisation dans le menu**<br>Le menu permet d'accéder aux options de navigation proposées par l'application, notamment la déconnexion et la réinitialisation de l'état. | MAJOR | CDC §3 Navigation et session, §5.5 EF-NAV-01 | Q-009 |
| EX-026 | **Se déconnecter depuis le menu**<br>L'utilisateur connecté peut se déconnecter depuis le menu de navigation ; la déconnexion termine la session et ramène l'utilisateur à l'écran de connexion. | MAJOR | CDC §5.1 EF-AUTH-05, §5.5 EF-NAV-02, §9 Déconnexion |  |
| EX-027 | **Empêcher la poursuite d'une session déconnectée**<br>La déconnexion doit empêcher la poursuite normale d'une session déconnectée via les parcours applicatifs. | CRITICAL | CDC §7 Sécurité de session | Q-012 |
| EX-028 | **Réinitialiser l'état de démonstration**<br>La réinitialisation remet à zéro les éléments de démonstration concernés, notamment l'état du panier et les boutons d'ajout/retrait, et restaure les données d'interface prévues par l'application. | MAJOR | CDC §5.5 EF-NAV-03, §6 RG-09, §8 Parcours D, §9 Réinitialisation | Q-010 |
| EX-029 | **Naviguer sans incohérence d'état**<br>Les commandes de navigation doivent conduire vers l'écran correspondant sans incohérence d'état. | MAJOR | CDC §5.5 EF-NAV-04 | Q-009 |

### Cas de tests

#### CT0032 — Afficher les options du menu de navigation

- **Exigences** : EX-025
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Critères d'acceptation (CTFL v4.0 §4.5.2)
- **Prérequis** : Être connecté avec le profil standard JDD-001.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-009

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ouvrir le menu de navigation | Le menu affiche au moins une option de déconnexion et une option de réinitialisation de l'état (liste complète à confirmer, Q-009). |

#### CT0033 — Se déconnecter depuis le menu

- **Exigences** : EX-026
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Test de transition d'états (CTFL v4.0 §4.2.4)
- **Prérequis** : État de départ : authentifié avec le profil standard JDD-001.
- **Jeux de données** : JDD-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ouvrir le menu de navigation | Le menu affiche l'option de déconnexion. |
| 2 | Choisir la déconnexion | Transition authentifié -> non authentifié : l'écran de connexion s'affiche. |

#### CT0034 — Empêcher la reprise d'une session après déconnexion

- **Exigences** : EX-027
- **Nature** : Négatif — **Type de test** : Test de sécurité — **Importance** : HIGH
- **Technique ISTQB** : Test de transition d'états (CTFL v4.0 §4.2.4)
- **Prérequis** : État de départ : authentifié avec le profil standard JDD-001, sur le catalogue. Avoir relevé l'adresse de la page catalogue.
- **Objectif** : Transition invalide visée : non authentifié (après déconnexion) -> catalogue.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-012

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Se déconnecter depuis le menu | L'écran de connexion s'affiche. |
| 2 | Utiliser la commande Précédent du navigateur | Le catalogue n'est pas utilisable comme dans une session ouverte (comportement exact à confirmer, Q-012). |
| 3 | Ouvrir directement l'adresse de la page catalogue | Le catalogue ne s'affiche pas ; l'écran de connexion ou une indication d'authentification nécessaire s'affiche. |

#### CT0035 — Réinitialiser l'état de démonstration avec un panier rempli

- **Exigences** : EX-028
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : HIGH
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient deux produits ajoutés depuis le catalogue.
- **Objectif** : Parcours D.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-010

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ouvrir le menu et déclencher la réinitialisation | La réinitialisation est appliquée. |
| 2 | Observer l'indicateur du panier | L'indicateur du panier est revenu à son état initial (panier vide). |
| 3 | Observer les deux produits dans le catalogue | Les boutons d'ajout/retrait des deux produits sont revenus à leur état initial (ajout possible). |

#### CT0036 — Naviguer entre fiche produit, catalogue et panier sans incohérence

- **Exigences** : EX-029
- **Nature** : Nominal — **Type de test** : Test fonctionnel (adéquation fonctionnelle) — **Importance** : MEDIUM
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient un produit.
- **Jeux de données** : JDD-001
- **Questions liées** : Q-009

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ouvrir la fiche d'un autre produit puis revenir au catalogue | Le catalogue s'affiche ; l'indicateur du panier affiche 1. |
| 2 | Ouvrir le panier puis revenir au catalogue | Le catalogue s'affiche ; l'indicateur affiche 1 et le produit du panier est indiqué comme ajouté. |
| 3 | Démarrer la commande puis revenir en arrière par la commande proposée | L'écran précédent s'affiche et le panier contient toujours le produit (commande de retour à confirmer, Q-009). |

## Ergonomie et accessibilité

### Exigences

| ID | Exigence | Criticité | Source | Questions |
|---|---|---|---|---|
| EX-030 | **Proposer des libellés compréhensibles et cohérents**<br>Les libellés, boutons, messages et éléments de navigation doivent être compréhensibles et cohérents. | MINOR | CDC §7 Ergonomie | Q-016 |
| EX-034 | **Rendre les champs, contrôles et messages accessibles**<br>Les champs doivent être identifiables, les contrôles utilisables au clavier et les messages d'erreur perceptibles. | MAJOR | CDC §7 Accessibilité | Q-015 |

### Cas de tests

#### CT0039 — Se connecter et ajouter un produit au clavier uniquement

- **Exigences** : EX-034
- **Nature** : Nominal — **Type de test** : Test d'utilisabilité (dont accessibilité) — **Importance** : MEDIUM
- **Technique ISTQB** : Test basé sur des checklists (CTFL v4.0 §4.4.3)
- **Prérequis** : Être déconnecté, sur l'écran de connexion. Disposer du profil standard JDD-001. Ne pas utiliser la souris.
- **Objectif** : Checklist accessibilité, point « contrôles utilisables au clavier » (CDC §7). Référentiel à confirmer (Q-015).
- **Jeux de données** : JDD-001
- **Questions liées** : Q-015

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Atteindre les champs et l'action de connexion avec la touche Tabulation, saisir les identifiants JDD-001 et valider avec Entrée | Le focus est visible sur chaque élément atteint ; la session s'ouvre et le catalogue s'affiche. |
| 2 | Atteindre l'action d'ajout d'un produit au clavier et l'activer | Le produit est ajouté : l'indicateur du panier affiche 1. |

#### CT0040 — Identifier les champs et percevoir les messages d'erreur

- **Exigences** : EX-034
- **Nature** : Nominal — **Type de test** : Test d'utilisabilité (dont accessibilité) — **Importance** : MEDIUM
- **Technique ISTQB** : Test basé sur des checklists (CTFL v4.0 §4.4.3)
- **Prérequis** : Être déconnecté, sur l'écran de connexion.
- **Objectif** : Checklist accessibilité, points « champs identifiables » et « messages d'erreur perceptibles » (CDC §7).
- **Questions liées** : Q-015

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Observer les champs de l'écran de connexion | Chaque champ porte une étiquette ou une indication visible de la donnée attendue. |
| 2 | Déclencher l'action de connexion avec les champs vides | Le message d'erreur s'affiche sous forme de texte lisible, à proximité du formulaire. |

#### CT0041 — Contrôler la cohérence des libellés entre les écrans

- **Exigences** : EX-030
- **Nature** : Nominal — **Type de test** : Test d'utilisabilité (dont accessibilité) — **Importance** : MEDIUM
- **Technique ISTQB** : Test basé sur des checklists (CTFL v4.0 §4.4.3)
- **Prérequis** : Être connecté avec le profil standard JDD-001.
- **Objectif** : Checklist ergonomie, point « cohérence des libellés » (CDC §7). Critères de compréhensibilité à confirmer (Q-016).
- **Jeux de données** : JDD-001
- **Questions liées** : Q-016

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Parcourir connexion, catalogue, fiche produit, panier, commande et menu en relevant les libellés des boutons et messages | Les libellés sont relevés pour chaque écran. |
| 2 | Comparer les libellés d'une même action d'un écran à l'autre | Une même action porte le même libellé sur tous les écrans. |

## Compatibilité

### Exigences

| ID | Exigence | Criticité | Source | Questions |
|---|---|---|---|---|
| EX-031 | **Rester utilisable sur les navigateurs et tailles d'écran retenus**<br>L'application doit rester utilisable sur les navigateurs et tailles d'écran retenus pour la campagne de test. | MAJOR | CDC §7 Compatibilité | Q-014 |

### Cas de tests

#### CT0043 — Exécuter le parcours d'achat sur chaque navigateur et taille d'écran retenus

- **Exigences** : EX-031
- **Nature** : Nominal — **Type de test** : Test de compatibilité — **Importance** : MEDIUM
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Liste des navigateurs et tailles d'écran retenus disponible (Q-014).
- **Jeux de données** : JDD-001, JDD-004
- **Questions liées** : Q-014

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Sur chaque configuration retenue, exécuter le parcours A (connexion, ajout, panier, commande, confirmation) | Sur chaque configuration, l'écran de succès s'affiche et tous les éléments du parcours sont visibles et activables. |

## Performance

### Exigences

| ID | Exigence | Criticité | Source | Questions |
|---|---|---|---|---|
| EX-032 | **Répondre dans un délai acceptable**<br>Les écrans et actions doivent répondre dans un délai acceptable ; les profils à latence doivent être évalués séparément. | MAJOR | CDC §4 Utilisateur à latence, §7 Performance | Q-013 |

### Cas de tests

#### CT0042 — Mesurer les temps de réponse du parcours d'achat avec le profil à latence

- **Exigences** : EX-032
- **Nature** : Nominal — **Type de test** : Test de performance (rendement) — **Importance** : MEDIUM
- **Technique ISTQB** : Test des cas d'utilisation (CTFL v3.1 §4.2.5, CTAL-TA)
- **Prérequis** : Être déconnecté. Disposer du profil à latence JDD-006 et des informations client JDD-004. Configuration réseau consignée (CDC §10).
- **Objectif** : Évaluation séparée du profil à latence (CDC §4, §7). Pas de test de charge : non demandé par le CDC.
- **Jeux de données** : JDD-004, JDD-006
- **Questions liées** : Q-013

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Se connecter avec le profil JDD-006 en relevant le temps d'affichage du catalogue | Le catalogue s'affiche ; le temps est relevé. |
| 2 | Ajouter un produit, ouvrir le panier et passer la commande avec JDD-004 en relevant le temps de chaque écran | L'écran de succès s'affiche ; chaque temps est relevé et comparé au seuil à confirmer (Q-013). |

## Fiabilité

### Exigences

| ID | Exigence | Criticité | Source | Questions |
|---|---|---|---|---|
| EX-033 | **Ne pas perdre ni dupliquer d'articles**<br>Les actions répétées ou les changements d'écran ne doivent pas provoquer de perte ou de duplication inattendue des articles. | MAJOR | CDC §7 Fiabilité | Q-004 |

### Cas de tests

#### CT0037 — Répéter l'ajout et le retrait d'un produit sans duplication

- **Exigences** : EX-033
- **Nature** : Négatif — **Type de test** : Test de fiabilité — **Importance** : MEDIUM
- **Technique ISTQB** : Estimation d'erreurs (CTFL v4.0 §4.4.1)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier est vide (réinitialiser l'état de démonstration si besoin).
- **Objectif** : Erreur visée : actions répétées provoquant une duplication ou une perte d'article (CDC §7 Fiabilité).
- **Jeux de données** : JDD-001
- **Questions liées** : Q-004

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Ajouter puis retirer le même produit trois fois de suite depuis le catalogue | Après le dernier retrait, l'indicateur n'affiche plus de quantité. |
| 2 | Ajouter ce produit une dernière fois et ouvrir le panier | Le panier contient le produit une seule fois ; l'indicateur affiche 1. |

#### CT0038 — Changer d'écran plusieurs fois sans perte d'article

- **Exigences** : EX-033
- **Nature** : Nominal — **Type de test** : Test de fiabilité — **Importance** : MEDIUM
- **Technique ISTQB** : Critères d'acceptation (CTFL v4.0 §4.5.2)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Le panier contient deux produits.
- **Jeux de données** : JDD-001

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Enchaîner trois fois : catalogue, fiche d'un produit, panier | À chaque écran, l'indicateur du panier affiche 2. |
| 2 | Ouvrir le panier | Le panier contient les deux mêmes produits, chacun une seule fois. |

## Maintenabilité des tests

### Exigences

| ID | Exigence | Criticité | Source | Questions |
|---|---|---|---|---|
| EX-035 | **Identifier de manière stable les éléments de l'interface**<br>Les éléments de l'interface doivent pouvoir être identifiés de manière stable pour les tests automatisés. | MINOR | CDC §7 Maintenabilité des tests | Q-017 |

### Cas de tests

#### CT0044 — Relever l'identification des éléments interactifs

- **Exigences** : EX-035
- **Nature** : Nominal — **Type de test** : Test de maintenabilité — **Importance** : MEDIUM
- **Technique ISTQB** : Test basé sur des checklists (CTFL v4.0 §4.4.3)
- **Prérequis** : Être connecté avec le profil standard JDD-001. Accès aux outils de développement du navigateur.
- **Objectif** : Checklist de maintenabilité des tests (CDC §7). Réalisée pendant l'exploration (temps B).
- **Jeux de données** : JDD-001
- **Questions liées** : Q-017

| # | Action | Résultat attendu |
|---|---|---|
| 1 | Pour chaque champ, bouton et lien des écrans du parcours A, relever l'attribut qui l'identifie | Chaque élément interactif possède un identifiant qui ne dépend ni de sa position ni de son texte (critère de stabilité à confirmer, Q-017). |

