# Inventaire de couverture — Front office Orange eFacture

Sources : `agents/features/frontoffice/{login,dashboard,myinvoices,claims}.md`, qui correspondent aux fichiers LOGIN.md, DASHBOARD.md, MY_INVOICE.md et RECLAMATIONS_FRONT_OFFICE.md demandés. Elles sont complétées par l'exploration du 28/10/2026 (`docs/frontoffice-discoveries.md`).
Exécution de référence : suite complète du 28/10/2026, run `evidence/2026-10-28_10-16-48` (manifeste : `evidence/2026-10-28_10-16-48/manifest.md`).
Statuts : PASS, FAIL, BLOCKED, NEEDS_DISCOVERY, NOT_RUN, IMPLEMENTED_NOT_RUN.
Chemins des preuves : relatifs à `evidence/2026-10-28_10-16-48/frontoffice/`. Chaque dossier contient la capture de l'état final (`test-finished-1.png` ou `test-failed-1.png`) et, s'il y en a, les captures d'étape (`step-NN-…png`).

## A. Connexion et récupération — LOGIN.md

Specs : `tests/auth/frontoffice/login.spec.js` et `tests/auth/frontoffice/recovery.spec.js`

| ID | Scénario spec | Test Playwright | Statut | Preuve | Commentaire |
|---|---|---|---|---|---|
| FLOG-01 | S1 Affichage | Front Office - Login - Display the login screen | PASS | `auth-frontoffice-login/front-office-login-display-the-login-screen__PASS/` | |
| FLOG-02 | S2 Identifiants valides | Front Office - Login - Authenticate with valid test credentials | BLOCKED | `…authenticate-with-valid-test-credentials__SKIPPED/` | Test écrit, ignoré : `FRONTOFFICE_TEST_PASSWORD` vide. Assertion post-connexion limitée à `#/accueil` (route lue dans le bundle), à confirmer |
| FLOG-03 | S3 Mauvais mot de passe | Front Office - Login - Reject an incorrect password | PASS | `…reject-an-incorrect-password__PASS/` | 1 tentative sur `QA_REQ_01` |
| FLOG-04 | S4 Identifiant inconnu refusé | Front Office - Login - Reject an unknown account | PASS | `…reject-an-unknown-account__PASS/` | |
| FLOG-05 | S4 / critère 5 : aucune divulgation de l'existence du compte | Front Office - Login - Refuse unknown accounts and wrong passwords with the same message | **FAIL** | `…same-mes__FAILED/` (2 étapes et l'état d'échec) | **Défaut applicatif** : « : connection failed to the platform » (924) contre « login and/or password incorrect(s) » (919). 2e tentative sur `QA_REQ_01` |
| FLOG-06 | S5 Champs vides | Front Office - Login - Block submission with empty fields | PASS | `…block-submission-with-empty-fields__PASS/` | Aucun appel de connexion |
| FLOG-07 | S5 Identifiant seul | Front Office - Login - Block submission with an empty password | PASS | `…with-an-empty-password__PASS/` | |
| FLOG-08 | S5 Mot de passe seul | Front Office - Login - Block submission with an empty username | PASS | `…with-an-empty-username__PASS/` | |
| FLOG-09 | S6 Masquage et contrôle d'affichage | Front Office - Login - Mask the password and reveal it with the eye icon | PASS | `…mask-the-password…__PASS/` (+ étape) | Icône sans nom accessible |
| FLOG-10 | S7 Ouverture de la réinitialisation | Forgot password - Open the reset form from the login screen | PASS | `auth-frontoffice-recovery/forgot-password-open-the-reset-form…__PASS/` | |
| FLOG-11 | S8 Réinitialisation vide | Forgot password - Require the account number | PASS | `…forgot-password-require-the-account-number__PASS/` | Aucun appel OTP |
| FLOG-12 | S8 Réinitialisation, compte inconnu | Forgot password - Refuse an unknown account number | PASS | `…refuse-an-unknown-account-number__PASS/` | Le message confirme l'inexistence du compte (anomalie F2) |
| FLOG-13 | S8 Réinitialisation avec le compte de test | — | BLOCKED | — | Enverrait un code réel au compte partagé : autorisation requise |
| FLOG-14 | S9 Ouverture « identifiant oublié » | Forgotten identifier - Open the support form without account fields | PASS | `…forgotten-identifier-open-the-support-form…__PASS/` | Parcours distinct : formulaire de support |
| FLOG-15 | S10 Identifiant oublié, saisie vide | Forgotten identifier - Keep an empty request unsent | PASS | `…keep-an-empty-request-unsent__PASS/` (+ étape) | Garde réseau : aucune requête |
| FLOG-16 | S10 Identifiant oublié, données valides | — | BLOCKED | — | Créerait une demande réelle : autorisation requise |
| FLOG-17 | S11 Retour depuis la réinitialisation | Forgot password - Return to the login page | PASS | `…return-to-the-login-page__PASS/` | |
| FLOG-18 | S11 Fermeture de « identifiant oublié » | Forgotten identifier - Close the form and return to the login screen | PASS | `…close-the-form…__PASS/` | |
| FLOG-19 | S12 Accès direct sans authentification | Front Office - Login - Redirect protected pages to the login screen | PASS | `…redirect-protected-pages…__PASS/` (4 étapes) | `#/accueil`, `#/factures`, `#/reclamations`, `#/help` |
| FLOG-20 | S13 Déconnexion | — | BLOCKED | — | Nécessite une session authentifiée |
| FLOG-21 | Langue FR / EN (observé) | Front Office - Login - Switch the interface between English and French | PASS | `…switch-the-interface…__PASS/` | |
| FLOG-22 | Première connexion : changement de mot de passe (bundle) | — | NEEDS_DISCOVERY | — | Lu dans le code ; nécessite un compte en première connexion |
| FLOG-23 | Astuce après 2 échecs (bundle) | — | NEEDS_DISCOVERY | — | Non exécuté pour limiter les tentatives |
| FLOG-24 | Identifiant égal au mot de passe → réinitialisation (bundle) | — | NEEDS_DISCOVERY | — | À confirmer avec l'équipe |

## B. Tableau de bord — DASHBOARD.md

| ID | Scénario spec | Test | Statut | Commentaire |
|---|---|---|---|---|
| FDSH-01 à FDSH-12 | S1 Accès, S2 Widget Account, S3 Add account, S4 Validation de l'ajout, S5 Indicateurs, S6 My Latest Invoices / See all, S7 Raccourci réclamation, S8 FAQ, S9 Tutoriels, S10 Liaison des comptes, S11 Retour et session, S12 États vides et erreurs | — | BLOCKED ×12 | Aucune session authentifiée (mot de passe absent). Aucun locator n'a pu être observé, donc aucun test n'a été écrit. FAQ et tutoriels publics : voir la section C |

## C. Aide publique — découverte hors spécification

Spec : `tests/frontoffice/help/open-help.spec.js`

| ID | Cas | Test | Statut | Preuve |
|---|---|---|---|---|
| FHLP-01 | Accès sans connexion aux tutoriels | Help - Public access - Open the tutorials without logging in | PASS | `frontoffice-help-open-help/help-public-access…__PASS/` |
| FHLP-02 | Passage des tutoriels à la FAQ | Help - Navigation - Switch from tutorials to the FAQ | PASS | `…switch-from-tutorials-to-the-faq__PASS/` (+ étape) |
| FHLP-03 | Retour à la connexion | Help - Navigation - Return to the login page | PASS | `…return-to-the-login-page__PASS/` |

## D. My Invoice — MY_INVOICE.md

| ID | Scénario spec | Test | Statut | Commentaire |
|---|---|---|---|---|
| FINV-01 à FINV-19 | S1 Accès, S2 Liste, S3-S5 Recherche, S6-S9 Filtres, S10 My Identifier, S11 Détails, S12 Réclamation depuis facture, S13 Paiement, S14 Orange Money code, S15 QR code, S16 Visa, S17 Archives, S18 Archives par identifiant, S19 Chargement et erreurs | — | BLOCKED ×19 | Session authentifiée requise. Pour S10 et S18, un second identifiant de test est aussi nécessaire ; pour S13 à S16, un environnement de paiement de test. Aucun paiement ne sera jamais confirmé |

## E. Réclamations — RECLAMATIONS_FRONT_OFFICE.md

Spec : `tests/frontoffice/claims/public-claim.spec.js`

| ID | Scénario spec | Test | Statut | Preuve | Commentaire |
|---|---|---|---|---|---|
| FCLM-01 | Liste des réclamations | — | BLOCKED | — | Session requise |
| FCLM-02 | État d'une réclamation | — | BLOCKED | — | Session et réclamation existante requises |
| FCLM-03 | Recherche | — | BLOCKED | — | Session requise |
| FCLM-04 | Recherche sans résultat | — | BLOCKED | — | Session requise |
| FCLM-05 | Ouvrir la création (formulaire public, sans connexion) | Claims - Public form - Open the claim form without logging in | PASS | `frontoffice-claims-public-claim/claims-public-form-open…__PASS/` | |
| FCLM-06 | Champs obligatoires | Claims - Public form - Keep an empty claim unsent | PASS | `…keep-an-empty-claim-unsent__PASS/` (+ étape) | Garde réseau : 0 requête |
| FCLM-07 | Création avec données de test | — | BLOCKED | — | Créerait une réclamation réelle : autorisation explicite requise |
| FCLM-08 | Périmètre par identifiant | — | BLOCKED | — | Session et 2 identifiants requis |
| FCLM-09 | Contact par e-mail (observé) | Claims - Public form - Ask for an email address when contact by email is chosen | PASS | `…ask-for-an-email…__PASS/` | |
| FCLM-10 | Téléphone non numérique (observé) | Claims - Public form - Keep a claim with a non-numeric phone number unsent | PASS | `…non-numeric-phone…__PASS/` (+ étape) | Message générique, aucune requête |
| FCLM-11 | E-mail invalide (observé) | Claims - Public form - Keep a claim with an invalid email unsent | PASS | `…invalid-email-unsent__PASS/` (+ étape) | Message générique, aucune requête |
| FCLM-12 | Types de réclamation BO proposés dans le FO (inter-espaces, = SET-15 du BO) | Claims - Public form - Offer the complaint types configured in the back office | PASS | `…offer-the-complaint-types…__PASS/` (+ capture BO) | Inclut 2 types QA visibles publiquement (anomalie F4) |

## Synthèse (comptée à partir des tableaux ci-dessus)

| Section | Cas | PASS | FAIL | BLOCKED | NEEDS_DISCOVERY | NOT_RUN | IMPLEMENTED_NOT_RUN |
|---|---|---|---|---|---|---|---|
| A. Connexion et récupération | 24 | 16 | 1 | 4 | 3 | 0 | 0 |
| B. Tableau de bord | 12 | 0 | 0 | 12 | 0 | 0 | 0 |
| C. Aide publique | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| D. My Invoice | 19 | 0 | 0 | 19 | 0 | 0 | 0 |
| E. Réclamations | 12 | 6 | 0 | 6 | 0 | 0 | 0 |
| **Total** | **70** | **25** | **1** | **41** | **3** | **0** | **0** |

Tests Playwright Front Office : 27. Résultats : 25 PASS, 1 FAIL (FLOG-05), 1 ignoré (FLOG-02, compté BLOCKED).
