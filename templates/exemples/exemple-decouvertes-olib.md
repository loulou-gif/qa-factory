# Découvertes — Front office Orange eFacture (exploration du 28/10/2026)

Environnement : `FRONTOFFICE_BASE_URL` (développement), application Angular 20 (`ng-version="20.3.29"`), titre d'onglet « Orange CI | My Facture ».
Méthode : scripts Playwright de lecture (snapshots ARIA, DOM, requêtes réseau) et lecture des routes du bundle `main-*.js`. Pendant l'exploration des formulaires, une **garde réseau** interrompait toute requête d'écriture (POST hors `getByCriteria`). Aucune réclamation ni demande n'a été envoyée.
Légende : **[Observé]** fait constaté ; **[Bundle]** lu dans le code livré, non exécuté ; **[À confirmer]** hypothèse ou règle non établie.

## 0. Limite principale : pas de session authentifiée

- Le compte de test `QA_REQ_01` est cité dans LOGIN.md, mais **aucun mot de passe n'est disponible** : la variable `FRONTOFFICE_TEST_PASSWORD` est vide.
- Le tableau de bord, My Invoice, les réclamations authentifiées, l'aide authentifiée et la déconnexion **n'ont donc pas été explorés**. Ils sont classés BLOCKED.
- Une seule tentative de connexion `QA_REQ_01` avec un mauvais mot de passe a été faite pendant l'exploration (réponse : code 919). Les tests en font deux par exécution complète.

## 1. Routes

| Route | Accès | Constat |
|---|---|---|
| `#/auth` | Public | Écran de connexion **[Observé]** |
| `#/open-help` → `#/open-help/tutorial`, `#/open-help/faq` | Public | Tutoriels et FAQ **[Observé]** |
| `#/accueil`, `#/factures`, `#/reclamations`, `#/help` | Protégé (garde Angular) | Redirection vers `#/auth`, formulaire de connexion affiché **[Observé]** |
| Route inconnue | — | Redirigée vers `#/accueil` puis vers `#/auth` **[Observé]** |
| `#/auth-by-token`, `#/ext-invoice-consult/:token` | Public avec jeton | Non testé : aucun jeton de test **[Bundle]** |

## 2. Connexion (`#/auth`)

- Champs :
  - `#auth-username`, libellé « Account number or line number », placeholder `ex: 1.xxxxx ou 2722xx00xx` ;
  - `#auth-password`, libellé « Password », `type=password`.
- Bouton « Login » ; lien-bouton `#forgot-password` « Forgot password ? » ; tuiles « Make a new claim — No login needed » et « Forgotten identifier — We'll help you find it ».
- Groupe « Interface language » (FR / EN, `aria-pressed`) et bouton thème `#theme-toggle` sans nom accessible. Le titre « Good morning. » dépend probablement de l'heure : il n'est pas assertionné.
- **Icône œil** : bouton **sans nom accessible**. Il bascule le champ entre `password` et `text` et ne soumet pas le formulaire.
- Champs vides, ou un seul champ rempli → toast « Please enter your login and password ! », sans aucun appel à `/api/compteClient/login`.
- **Énumération de comptes [Observé]** :
  - identifiant inconnu → code `924`, toast « : connection failed to the platform » ;
  - `QA_REQ_01` avec un mauvais mot de passe → code `919`, « login and/or password incorrect(s) ».
  - Les deux messages diffèrent, ce qui révèle l'existence du compte et contredit le critère 5 de LOGIN.md.
- Traduction FR : « Bonjour. », « Numéro de compte ou de ligne », « Mot de passe », « Connexion », « Mot de passe oublié ? ».
  - Le placeholder FR ajoute « ou login@ofibre.ci » (absent en EN).
  - Le placeholder EN est rédigé en français (« ou »).
- **[Bundle]** Comportements lus dans le code, à confirmer (non exécutés) :
  - après 2 échecs, une astuce « mot de passe oublié » s'affiche ;
  - si l'identifiant est égal au mot de passe, une demande de réinitialisation est lancée ;
  - lors d'une première connexion (`isFirstConnexion`), un changement de mot de passe est demandé (10 caractères minimum, avec confirmation et OTP).

## 3. Mot de passe oublié

- Le panneau remplace le formulaire sur `#/auth`. Il contient :
  - le texte « Forgotten your password ? » (pas un titre) ;
  - « Please enter your account number or line number to receive a reset code. » ;
  - un champ (placeholder `ex: 1.xxxxx ou 2722xx00xx`), les boutons « Submit » et « Go back to the login page ».
- Soumission vide → « Please enter your account number or line number ! », sans appel OTP.
- Compte inconnu → `POST /api/otp/external/sendOtp` : `hasError`, code `902`, « data not exists: customer account: <saisie> ». Le message **confirme l'inexistence du compte** (énumération).
- **Non exécuté** : soumission avec `QA_REQ_01`. Elle enverrait un code de réinitialisation réel au compte partagé.

## 4. Formulaire public « Online support form » (réclamation sans connexion)

- C'est une modale `<app-create-reclamation>` : titre « Welcome to your online support form », sous-titre « How can we help you ? », bouton « Close ».
- Les libellés ne sont pas liés aux champs : le nom accessible vient du placeholder.
- **Make a new claim** : champs
  - Full name ;
  - Customer account (placeholder `The account number of the claim (e.g. 1.21222)`) ;
  - contact « By Phone » (par défaut) / « By Email » → champ `Your mobile number..` (`minlength=maxlength=10`) ou `Your email..` ;
  - Universe : Other, Internet, Mobile, Landline (via `refUnivers/no-auth/getByCriteria`) ;
  - Reason of claim (`select`, « Please select... », via `refTypeReclamation/no-auth/getByCriteria`) ;
  - Description (facultative), bouton « Send ».
- **Forgotten identifier** : la même modale, sans les champs Full name et Customer account.
- Validations observées. Toutes affichent le même message générique, « Please fill in the required fields with the necessary information! », et **aucune requête n'est envoyée** :
  - formulaire vide ;
  - téléphone non numérique (`abcdefghij`) ;
  - e-mail invalide (`not-an-email`).
- Les champs sont en état d'erreur (`input-error`) dès l'ouverture, avant toute saisie.
- **Lien avec le back office [Observé et automatisé]** : les 8 motifs proposés correspondent exactement aux 8 types de Settings › Complaint Type. Ils incluent les types de test `QA TYPE 1793148426527591` et `QA_TEST_COMPLAINT_TYPE_1793`, **visibles par tout visiteur du portail**.
- **Non exécuté** : envoi d'une réclamation avec des données de test. Il créerait une réclamation réelle dans l'environnement partagé, ce qui demande une autorisation explicite.

## 5. Aide publique (`#/open-help`)

- Titre « Tutorials and FAQ. », « Learn more about MyFacture. », recherche « Search using keywords.. ».
- Liens « Tutorials » et « Frequently asked questions », bouton « Go back to the login page ».
- États vides le 28/10 : « No tutorials available. » et « No question available. ». Les tests n'en dépendent pas.

## 6. Points à confirmer

- Mot de passe du compte `QA_REQ_01`, et existence d'un second identifiant de test (My Identifier, compte secondaire).
- Autorisation de créer **une** réclamation de test via le formulaire public. Elle débloquerait aussi les tests Claims du back office (CLM-07 à CLM-11).
- Environnement de paiement de test (Orange Money code / QR, Visa) : aucune information.
- Politique de verrouillage après échecs de connexion.
