FEATURE : FRONT_OFFICE_LOGIN
NAME
Authentification du client sur le portail Orange eFacture Front Office
APPLICATION
Orange eFacture — Front Office
MODULE
Login / Authentification
TAGS
@frontoffice @login @authentification @mot-de-passe @identifiants @smoke @regression @securite
DESCRIPTION
Le portail Front Office d'Orange eFacture permet aux clients d'Orange Liberia de consulter leurs factures et de soumettre des réclamations.

Le client doit se connecter à l'aide des identifiants reçus par e-mail après la création de son compte dans le back office. Il se connecte avec son compte principal. Une fois authentifié et arrivé sur son tableau de bord, il peut, si cette fonctionnalité est disponible pour son compte, ajouter ou gérer des comptes secondaires.

L'écran de connexion propose également deux parcours distincts :
- Réinitialisation du mot de passe : le client indique vouloir réinitialiser son mot de passe et suit la procédure présentée par l'application au moyen d'un formulaire.
- Identifiants oubliés : le client signale qu'il a oublié ses identifiants et suit une procédure spécifique au moyen d'un formulaire.
Les champs, les libellés, les règles de validation, les étapes et les messages exacts de ces deux procédures doivent être découverts sur l'interface réelle. Ne pas supposer qu'elles demandent les mêmes informations ou qu'elles se terminent de la même manière.

Compte de test fourni pour l'exploration : identifiant QA_REQ_01. Le mot de passe fourni doit être conservé dans une variable d'environnement locale et ne doit pas être inscrit en clair dans les scripts, spécifications, journaux ou captures. Ne pas supposer que ce compte est actif ou que ses identifiants ont été vérifiés tant qu'une tentative de connexion contrôlée n'a pas été exécutée.

URL Front Office de développement : https://frontoffice-efacture-development.k8s.olr-dev.orange.com.lr/#/auth
USER STORY
En tant que client d'Orange Liberia, je veux me connecter au portail Orange eFacture avec les identifiants qui m'ont été communiqués, ou lancer la procédure adaptée si j'ai oublié mon mot de passe ou mes identifiants, afin d'accéder à mon espace client en toute sécurité.
CRITÈRES D'ACCEPTATION
1. Le client peut ouvrir la page d'authentification du Front Office.
2. Les champs et contrôles du formulaire sont identifiés à partir de l'interface réelle.
3. Une connexion avec un compte de test valide ouvre le portail ou le tableau de bord prévu par l'application.
4. Une connexion avec un mot de passe incorrect est refusée et affiche un retour explicite, selon le comportement réel de l'application.
5. Une connexion avec un identifiant inconnu est refusée sans révéler d'informations sensibles sur l'existence des comptes.
6. La soumission avec les champs vides ou incomplets est gérée conformément aux validations observées.
7. Le mot de passe est masqué par défaut, si tel est le comportement de l'interface, et le contrôle d'affichage éventuel fonctionne.
8. L'action de réinitialisation du mot de passe ouvre le parcours spécifique correspondant.
9. Le formulaire de réinitialisation du mot de passe expose les champs et validations réellement définis par l'application.
10. L'action « identifiants oubliés » ouvre un parcours distinct, si l'application le présente ainsi.
11. Le formulaire de récupération des identifiants expose les champs et validations réellement définis par l'application.
12. Les deux procédures présentent un retour compréhensible après soumission, sans que le test suppose l'envoi effectif d'un e-mail si ce dernier ne peut pas être vérifié.
13. Les liens de retour ou d'annulation, s'ils existent, ramènent à l'écran attendu sans authentifier l'utilisateur.
14. Un utilisateur non authentifié ne peut pas accéder directement au tableau de bord ou à une page protégée.
15. Après une connexion réussie, le compte principal est identifié conformément au comportement réel de l'application.
16. Les erreurs et les résultats de test sont tracés sans exposer le mot de passe, les jetons, les cookies de session ni des données personnelles inutiles.
CONTRAINTES MÉTIER
- L'authentification doit utiliser le compte principal du client.
- Les identifiants sont supposés être communiqués au client par e-mail après la création du compte depuis le back office. Le test du flux d'envoi d'e-mail n'est pas inclus dans ce scénario de connexion, sauf si une boîte de réception de test est explicitement disponible.
- La gestion des comptes secondaires après connexion est hors du périmètre fonctionnel de ce fichier ; elle devra faire l'objet d'une spécification distincte.
- Ne pas confondre la réinitialisation du mot de passe avec la récupération d'identifiants oubliés. Explorer et tester séparément les deux parcours.
- Ne pas inventer les champs de ces formulaires, les messages d'erreur, les règles de verrouillage, la durée de validité des liens, le format des identifiants ou les étapes de vérification.
- Les tests négatifs ne doivent pas déclencher de verrouillage prolongé du compte ni perturber un compte partagé. Limiter les tentatives invalides et vérifier la politique réelle avant d'automatiser des répétitions.
- Ne pas confirmer l'envoi ou la réception d'un e-mail sans preuve observable dans une boîte de réception de test ou un système de test autorisé.
- Ne pas inclure le mot de passe fourni dans le code source, les fichiers .md, les captures, les rapports, les traces ou les commits.
- Stocker les identifiants de test dans des variables d'environnement, par exemple FRONTOFFICE_TEST_USERNAME et FRONTOFFICE_TEST_PASSWORD, dans un fichier local non versionné ou dans le gestionnaire de secrets de l'environnement.
- Ne pas contourner les mécanismes d'authentification, de vérification ou de sécurité.
- Si l'interface ou le comportement réel diffère des hypothèses de cette spécification, consigner l'observation et adapter les tests plutôt que de forcer une assertion inventée.
SCENARIO 1 : Affichage de la page de connexion
GIVEN le navigateur ouvre l'URL du Front Office
WHEN la page d'authentification se charge
THEN l'agent attend que le formulaire soit visible et stable
AND il relève le titre, les champs, les boutons et les liens réellement affichés
AND il capture l'écran initial
AND il confirme que les actions de connexion, de réinitialisation du mot de passe et d'identifiants oubliés sont présentes si elles existent dans l'interface
AND il n'invente aucun libellé ni locator
SCENARIO 2 : Connexion avec des identifiants valides
GIVEN l'écran de connexion est affiché
AND les identifiants du compte de test autorisé sont configurés dans les variables d'environnement
WHEN l'agent saisit l'identifiant et le mot de passe valides
AND il soumet le formulaire
THEN l'application authentifie le client si le compte est actif et les identifiants sont corrects
AND le portail ou le tableau de bord attendu s'affiche
AND l'agent vérifie un élément fiable confirmant l'état authentifié
AND il vérifie que le compte principal est celui utilisé pour la session selon les informations réellement visibles
AND aucun secret n'est écrit dans les logs ou dans les rapports

NOTE : si la connexion échoue, consigner le résultat exact et classer le test comme bloqué ou échoué selon la cause observée. Ne pas affirmer que les identifiants sont valides avant vérification.
SCENARIO 3 : Refus d'un mot de passe incorrect
GIVEN l'écran de connexion est affiché
AND un identifiant de test autorisé est disponible
WHEN l'agent saisit cet identifiant avec un mot de passe incorrect de test
AND il soumet le formulaire
THEN l'accès est refusé
AND l'application affiche le retour réellement prévu
AND aucune page protégée n'est accessible
AND le test ne révèle pas le mot de passe utilisé dans les traces
SCENARIO 4 : Refus d'un identifiant inconnu
GIVEN l'écran de connexion est affiché
WHEN l'agent saisit un identifiant de test non existant et un mot de passe de test
AND il soumet le formulaire
THEN l'accès est refusé
AND l'application reste dans un état non authentifié
AND le message affiché est relevé sans imposer un texte inventé
AND le comportement ne révèle pas inutilement l'existence ou l'absence d'un compte
SCENARIO 5 : Validation des champs obligatoires
GIVEN l'écran de connexion est affiché
WHEN l'agent soumet le formulaire sans renseigner aucun champ
THEN l'application bloque la soumission ou présente les validations réellement prévues
AND aucun accès n'est accordé

WHEN l'agent renseigne uniquement l'identifiant puis soumet le formulaire
THEN l'application indique le champ manquant ou bloque la soumission selon le comportement observé
AND aucun accès n'est accordé

WHEN l'agent renseigne uniquement le mot de passe puis soumet le formulaire
THEN l'application indique le champ manquant ou bloque la soumission selon le comportement observé
AND aucun accès n'est accordé
SCENARIO 6 : Visibilité du mot de passe
GIVEN l'écran de connexion est affiché
WHEN l'agent saisit le mot de passe de test
THEN il vérifie que le mot de passe est masqué par défaut si c'est le comportement observé
AND si un contrôle d'affichage existe, il vérifie que ce contrôle change la visibilité du champ
AND il ne capture ni ne journalise le mot de passe en clair
SCENARIO 7 : Accès au formulaire de réinitialisation du mot de passe
GIVEN l'écran de connexion est affiché
WHEN l'agent active le lien ou bouton de réinitialisation du mot de passe réellement présent
THEN le formulaire ou la première étape de la procédure de réinitialisation s'affiche
AND l'agent relève les champs, les instructions, les validations et les actions réellement présents
AND il confirme que le parcours est distinct de celui des identifiants oubliés lorsque l'interface le prévoit
AND il n'invente pas de champ ni d'étape
SCENARIO 8 : Validation du formulaire de réinitialisation
GIVEN le formulaire de réinitialisation du mot de passe est affiché
WHEN l'agent le soumet sans remplir les champs requis
THEN l'application bloque la soumission ou affiche les validations réellement prévues
AND aucun message de réussite n'est considéré comme preuve d'envoi d'e-mail

WHEN l'agent remplit le formulaire avec une donnée de test autorisée et conforme
AND il le soumet
THEN l'application affiche le résultat réellement observé
AND l'agent consigne la confirmation ou l'erreur affichée
AND l'envoi effectif d'un e-mail n'est déclaré vérifié que si une boîte de réception ou une preuve de test autorisée le confirme

NOTE : ne pas modifier le mot de passe du compte partagé dans un test automatisé standard, sauf si un compte dédié à la réinitialisation est prévu et qu'une procédure de restauration est définie.
SCENARIO 9 : Accès au parcours « identifiants oubliés »
GIVEN l'écran de connexion est affiché
WHEN l'agent active l'action permettant de signaler des identifiants oubliés
THEN le formulaire ou la première étape correspondante s'affiche
AND l'agent relève les champs et instructions réellement présents
AND il vérifie que le parcours est différent de la réinitialisation du mot de passe si l'application distingue ces procédures
AND il consigne tout élément restant à clarifier
SCENARIO 10 : Validation du formulaire d'identifiants oubliés
GIVEN le formulaire d'identifiants oubliés est affiché
WHEN l'agent le soumet sans renseigner les champs requis
THEN l'application bloque la soumission ou affiche les validations réellement prévues

WHEN l'agent renseigne les informations de test autorisées et conformes
AND il soumet le formulaire
THEN l'application affiche le résultat réellement observé
AND l'agent vérifie qu'un retour est présenté à l'utilisateur
AND il ne prétend pas que les identifiants ont été envoyés ou récupérés sans preuve observable
SCENARIO 11 : Retour ou annulation d'une procédure
GIVEN l'agent se trouve dans le parcours de réinitialisation ou d'identifiants oubliés
AND une action de retour ou d'annulation est réellement disponible
WHEN l'agent l'active
THEN l'écran correspondant au comportement observé s'affiche
AND aucun utilisateur n'est authentifié par cette seule action
AND aucune donnée sensible saisie n'est exposée dans l'URL ou les journaux
SCENARIO 12 : Refus d'accès direct sans authentification
GIVEN l'agent n'est pas authentifié
WHEN il tente d'ouvrir directement une URL protégée du portail
THEN l'application redirige vers l'authentification ou refuse l'accès selon le comportement réel
AND aucun contenu protégé n'est exposé
AND le test ne se limite pas à vérifier l'URL : il confirme aussi l'absence d'accès au contenu protégé
SCENARIO 13 : Déconnexion et protection de la session
GIVEN l'agent est authentifié avec le compte de test
AND l'interface fournit une action de déconnexion
WHEN l'agent utilise cette action et confirme la déconnexion si une confirmation existe
THEN l'application termine la session
AND l'accès direct à une page protégée est refusé ou redirigé vers la connexion
AND le test ne réutilise pas un état de session devenu invalide

NOTE : relever le mécanisme réel de déconnexion dans le Front Office ; ne pas supposer que l'icône, le dialogue ou les libellés sont identiques à ceux du Back Office.
OBSERVABILITY
Collecter pendant l'exploration et l'exécution :
- capture de la page de connexion sans données sensibles ;
- liste des libellés et contrôles réellement observés ;
- résultats des tentatives valides et invalides ;
- captures d'écran en cas d'échec, après masquage des données sensibles ;
- erreurs de console ou de réseau pertinentes lorsque les outils les exposent ;
- état authentifié/non authentifié confirmé par un indicateur fiable ;
- étapes et messages observés dans les deux parcours de récupération ;
- statut explicite de vérification de l'e-mail : non vérifié, vérifié par une boîte de test ou bloqué ;
- rapports Playwright/Allure si cette intégration existe dans le projet.
Ne jamais écrire dans les logs, rapports ou captures :
- le mot de passe ;
- les cookies ou jetons de session ;
- les liens de récupération contenant un jeton ;
- des informations personnelles qui ne sont pas nécessaires au diagnostic.
LOCATOR_RULES
- Découvrir les locators en inspectant le DOM et l'arbre d'accessibilité de l'application.
- Privilégier les locators Playwright par rôle accessible, label et nom accessible, lorsque ces éléments existent réellement.
- Utiliser les attributs data-testid uniquement s'ils existent et sont stables.
- Ne pas inventer de labels, de sélecteurs CSS, de XPath ou de data-testid.
- Vérifier l'unicité des locators avant les interactions.
- Attendre un état observable plutôt que d'utiliser des délais fixes.
- Ne pas s'appuyer uniquement sur l'URL pour déterminer si la connexion a réussi.
- Masquer les secrets dans les traces et utiliser des variables d'environnement pour les identifiants.
PARTICULAR_RULES
1. Prioriser les tests de connexion et les deux parcours de récupération sans confondre leurs objectifs.
2. Utiliser exclusivement un compte de test autorisé et stocker son mot de passe dans une variable d'environnement locale non versionnée ou dans le gestionnaire de secrets du projet.
3. Ne pas réinitialiser le mot de passe du compte de test partagé sans procédure de restauration approuvée.
4. Limiter les tentatives de connexion invalides pour éviter un verrouillage de compte.
5. Ne pas déclarer un e-mail envoyé ou reçu sans preuve.
6. Ne pas supposer que le Front Office utilise les mêmes libellés, locators ou dialogues que le Back Office.
7. Les scénarios de comptes secondaires sont hors périmètre de ce fichier et devront être décrits dans une spécification dédiée au tableau de bord.
8. Si un comportement n'est pas accessible ou ne peut pas être confirmé, le signaler comme BLOCKED ou NEEDS_DISCOVERY, sans inventer de résultat.
9. Distinguer les défauts de l'application des problèmes de configuration, d'accès ou d'environnement.
10. Respecter l'architecture et les conventions de tests existantes du projet.