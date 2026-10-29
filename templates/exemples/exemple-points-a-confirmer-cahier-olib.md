# Points à confirmer — Cahier de tests Orange eFacture v1.0

Livrables :
- `docs/cahier/Cahier_de_tests_OrangeEFacture_v1.0.xlsx` (français) ;
- `docs/cahier/Test_book_OrangeEFacture_v1.0_EN.xlsx` (anglais, mêmes cas et même numérotation).

Ils sont générés par `docs/cahier/generation/build_cahier.py` (option `en` pour l'anglais), à partir du modèle `CAHIER DE TESTS BNI GESTION DES HABILITATIONS (3) BONITA (2).xlsx`.

## 1. Périmètre : cahier de recette des parties prenantes

- **Parcours nominaux uniquement** : 138 cas (CT0001–CT0138), répartis en 19 fonctionnalités.
- **Cas négatifs retirés** : 39 cas. Ce sont par exemple des identifiants invalides, des champs vides, des recherches sans résultat, des annulations ou des contrôles de sécurité. Ils restent couverts par les tests automatisés et le rapport E2E.
- **Cas raccourcis** : 6 cas de Settings (Users, Profiles, Actions, Notifications, Complaint Type, Status) perdent leur étape de validation d'un formulaire vide.
- **Où modifier la sélection** : `generation/parcours_nominaux.py`.
- **Colonnes laissées vides pour le client** : RÉSULTAT OLIB / OLIB RESULT, STATUT OLIB / OLIB STATUS et COMMENTAIRE.
- **STATUT ATTENDU** : il reste à « OK » pour chaque résultat attendu.
- **Feuille « Traçabilité » / « Traceability »** : elle relie chaque cas à sa spec et à son test Playwright, sans résultat d'exécution.
- **Ajout du 29/10/2026 (onglets F.A.Q et Tutorials du back office)** : 11 cas observés manuellement, sans test automatisé (« — » dans la traçabilité) : CT0053 à CT0059 (Settings), CT0080 (aide publique) et CT0127 à CT0129 (tutoriels BO → FO). Les 4 cas de validation de formulaire vide créés en même temps sont retirés (parcours non nominaux).
- **Résultats de la campagne automatisée du 28/10/2026** : ils ne figurent plus dans le cahier. Voir `docs/rapport/Rapport_tests_E2E_OrangeEFacture_2026-10-28.xlsx`.

## 2. Métadonnées à renseigner ou valider

| Champ | Valeur actuelle | Action |
|---|---|---|
| Personne à contacter | À renseigner | Fournir le nom ou le contact |
| Auteur des tests | À renseigner | Fournir le nom |
| Version | V1.0 | Valider la numérotation |
| Date de début et de fin des tests | À renseigner | À compléter lors de la recette OLIB |
| Logo client (à gauche du titre) | Vide | Fournir le logo officiel Orange. Le logo BNI du modèle a été retiré |
| Logo prestataire (à droite du titre) | Synelia, repris du modèle CEPICI (`docs/manuel`) | Confirmer qu'il remplace le logo Agora du modèle |

## 3. Adaptations du modèle

- **Ligne « Description »** : les cellules B16:E16 sont fusionnées, comme la ligne « Lien » (B17:E17), pour que le texte soit lisible.
- **Ligne « Personne à contacter »** : le modèle fusionne B18:B19, ce qui laisse « Auteur des tests » sans cellule de valeur. La fusion a été supprimée.
- **En-têtes H et I** : « RÉSULTAT » et « STATUT » du modèle sont renommés « RÉSULTAT OLIB » et « STATUT OLIB » (« OLIB RESULT » et « OLIB STATUS » en anglais).
- **Saisie du client** : la liste OK / NOK du modèle est conservée sur STATUT OLIB, et la mise en couleur OK / NOK sur RÉSULTAT OLIB.

## 4. Parcours nominaux dont le résultat attendu n'est pas confirmé

Ces parcours n'ont pas pu être observés pendant la campagne automatisée. Leur résultat attendu, marqué « À confirmer », doit être validé avant la recette.

| ID | Parcours | Raison |
|---|---|---|
| CT0006 | Connexion avec un compte LDAP | Aucun compte LDAP de test fourni |
| CT0026 | Réinitialisation (« Reset ») d'un client | Effet non documenté |
| CT0029 | Import d'un fichier de clients | Format et retours d'import à confirmer |
| CT0043 | Création d'un utilisateur du back office | Effets de la création (envoi d'identifiants) non documentés |
| CT0063 | « Check now » (vérification des paiements) | Modifie le statut payé / impayé des factures |
| CT0069 | Changement de mot de passe à la première connexion | Aucun compte en première connexion |
| CT0073 | Réinitialisation du mot de passe | Envoie un code réel (OTP) |
| CT0076 | Demande d'identifiant oublié | reCAPTCHA en erreur (ANO-02) |
| CT0091 | Liaison d'un second compte | Aucun second compte de test |
| CT0101 | Factures d'un autre identifiant | Aucun second identifiant de test |
| CT0102 | Parcours de paiement | Aucun environnement de paiement de test |
| CT0136 | Accès FO d'un client désactivé | Règle métier à confirmer |
| CT0128 | Tutoriel dans l'aide client (connecté) | Connexion FO bloquée par un reCAPTCHA le 29/10/2026 |

Comportements observés le 29/10/2026 qui contredisent le résultat attendu (à arbitrer avant la recette) :

| ID | Parcours | Constat |
|---|---|---|
| CT0059 | Suppression d'un tutoriel | Refusée par l'API (code 921 « this data cannot be deleted because it is used ») dès qu'il a une étape, sans message à l'écran. Or un tutoriel doit avoir au moins une étape : aucun tutoriel ne peut être supprimé |
| CT0080 | Consultation d'un tutoriel (FO) | Le panneau de détail reste en chargement (erreur Angular NG03402) ; les étapes ne s'affichent pas |
| CT0129 | Tutoriel désactivé | Il reste affiché dans l'aide publique |

Donnée de test restante : le tutoriel `QA_E2E TUTORIAL 672631` (id 1), impossible à supprimer, a été passé au statut Disabled. Il reste visible dans l'aide publique et doit être supprimé côté serveur.

## 5. Sources contradictoires ou incomplètes

- **`agents/project-overview.md`** : il décrit « BNI Agora », pas Orange eFacture. Il semble copié d'un autre projet.
- **Onglets de « Settings »** : depuis le 29/10/2026, ils sont 13 (ajout de F.A.Q et Tutorials). Le test automatisé « Navigation - Display the eleven administration tabs » (CT0041) attend encore 11 onglets et doit être mis à jour.
- **Fenêtre d'étape d'un tutoriel** : la liste de position est libellée « Segment », la position s'affiche « droite » dans l'interface anglaise, la vidéo est obligatoire et une URL dont la valeur de paramètre contient « _ » est refusée. Le titre de la page reste « Create Tutorial » en modification.
- **Fenêtre « Bulk import »** : le lien de modèle est libellé « Download the customer account deletion template ». Le modèle est au format `.xls`, alors que les fenêtres de fichier acceptent `.csv,.xlsx`.
- **Menu « Customer Center » du front office** : il est inactif. Sa destination est à confirmer.
- **Tuile « Monthly invoice »** : elle affiche 0 alors qu'une facture du mois a été reçue. Règle de calcul à confirmer (ANO-09).
- **Libellés français conservés dans la version anglaise** : trois cas de changement de langue (CT0004, CT0068, CT0095) citent volontairement les libellés français de l'interface.
