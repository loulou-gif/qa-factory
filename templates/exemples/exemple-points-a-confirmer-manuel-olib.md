# Points à confirmer — Manuel utilisateur OLIB (My Facture) v1.0

Livrables :
- `docs/manuel/Manuel_utilisateur_OLIB_v1.0.docx` ;
- `docs/manuel/Manuel_utilisateur_OLIB_v1.0.pdf` (export Word, pour relecture) ;
- `docs/manuel/User_manual_OLIB_v1.0_EN.docx` et `.pdf` : version anglaise, mêmes captures, générée avec `content_olib_en.py`. Les points ci-dessous s'appliquent aussi à cette version (sur la couverture, « to be completed » remplace « à renseigner »).

Ils sont générés par `docs/manuel/generation/build_manual_olib.py` et `content_olib.py`, à partir du modèle `Mode_emploi_Cepici - administration.docx`. Les captures (`docs/manuel/captures/`) ont été prises en recette le 28/10/2026 avec le compte de test QA_REQ_01 et le compte administrateur du back office.

## 1. Métadonnées de couverture

| Champ | Valeur actuelle | Action |
|---|---|---|
| Date | « à renseigner » | Fournir la date de diffusion |
| Version | « à renseigner » (fichier nommé v1.0) | Valider la numérotation |
| Rédaction | Synelia Group Afrique (repris du modèle) | Confirmer ou fournir le nom du rédacteur |
| Logo client | Absent (seuls les logos Synelia du modèle) | Fournir le logo officiel Orange si souhaité |
| Nom du projet | « PROJET : OLIB » / « MY FACTURE » | Confirmer l'intitulé officiel |

## 2. Fonctionnalités non observées (décrites sans résultat constaté)

| Procédure du manuel | Raison | À confirmer |
|---|---|---|
| Connexion LDAP (BO) | Aucun compte LDAP de test | Comportement réel |
| Reset d'un compte client | Non autorisé sur un compte réel | Effet de la réinitialisation |
| Bulk import, Delete invoices, Delete customer accounts | Non exécutés | Format attendu ; le lien du Bulk import est libellé « Download the customer account deletion template » (libellé probablement erroné) |
| Create User | Non exécuté | Communication du mot de passe initial |
| Check now (Payment check) | Modifie l'état payé / impayé | Effet et message de retour |
| Run Simulation (Cron) | Non exécuté | Résultat affiché |
| Mot de passe oublié (FO) | Enverrait un code réel | Suite de la procédure |
| Identifiant oublié / réclamation sans connexion (FO) | reCAPTCHA en erreur (ANO-02) | Message de confirmation après envoi |
| Bind an account (FO) | Aucun second compte de test | Étapes après **Next** |
| Paiement Mobile Money (« Pay with Mobile Money », « I pay my invoice ») | Aucun environnement de paiement de test | Parcours complet |
| Envoi d'une réclamation authentifiée (FO) | Formulaire capturé sans envoi pour le manuel (l'envoi a été testé en E2E) | — |

## 3. Écarts et incertitudes de l'interface

- **Customer Center (FO)** : menu affiché mais inactif (non cliquable). Il est documenté comme tel. Destination prévue à confirmer.
- **Onglets F.A.Q et Tutorials du BO** (ajout du 29/10/2026) : Settings compte désormais 13 onglets. Les captures des autres onglets (figures 26 à 38 et 45 à 48) datent du 28/10 et montrent encore 11 onglets.
- **Tutoriel : suppression impossible** : un tutoriel doit avoir au moins une étape, mais la suppression d'un tutoriel avec étape est refusée par l'API (« this data cannot be deleted because it is used ») sans message à l'écran. Le tutoriel de test `QA_E2E TUTORIAL 672631` (id 1) n'a pas pu être supprimé : il a été passé au statut Disabled et doit être supprimé côté serveur.
- **Tutoriel : statut Disabled ignoré** : un tutoriel Disabled reste affiché dans l'aide de l'espace client.
- **Tutoriel : détail non chargé (FO)** : un clic sur un tutoriel laisse le panneau de droite en chargement (erreur Angular NG03402 dans la console). Les étapes ne sont jamais affichées.
- **Tutoriel : libellés** : dans la fenêtre d'étape, la liste de position est libellée « Segment » ; la position s'affiche « droite » dans l'interface anglaise ; le titre reste « Create Tutorial » en modification ; la vidéo est obligatoire et une URL dont la valeur de paramètre contient « _ » est refusée.
- **Actualités (FO)** : aucune actualité affichée (ANO-08). Le contenu de la fenêtre n'est pas décrit.
- **Tutorials and FAQ (FO)** : les figures de l'aide publique montrent un tutoriel et une question de test (QA_E2E) publiés le 29/10/2026. La figure de l'aide authentifiée (espace client) montre encore l'état vide du 28/10.
- **Connexion FO** : le 29/10/2026, la page de connexion affiche un reCAPTCHA « I'm not a robot » absent de la figure 49 (capture du 28/10). La connexion automatisée n'est plus possible.
- **Libellés** : le manuel cite l'interface anglaise. Des libellés mixtes existent (filtres en français dans l'interface anglaise, ANO-04 ; colonne « Libelle » dans Complaint Type ; « Search an customer »). Ils sont cités tels qu'affichés.
- **Statuts des réclamations** : New / In progress / Closed, observés sur une réclamation de test (QA_E2E).
- **Accès par profil** : le manuel suppose un profil administrateur. Les droits nécessaires à chaque menu sont à préciser.

## 4. Captures

- Masquage appliqué : noms, e-mails, téléphones, URL et identifiants TIMM. Dans « Invoice Details » (figure 6), toutes les valeurs sont masquées ; seuls les libellés restent lisibles.
- Les figures 7 et 8 (liste des clients) affichent le message « Operation completed successfully » d'une action précédente.
- Les données visibles sont des données de test (QA_REQ_01, QA_E2E…, facture fictive 00000000000123456789 dont le PDF contient un document de démonstration).
- Les pages contenant de grandes captures laissent parfois un espace blanc en bas de page : chaque capture est maintenue avec sa légende et l'étape qui la précède.

## 5. Régénération

```
python build_manual_olib.py "../Mode_emploi_Cepici - administration.docx" ../captures <brouillon.docx> content_olib.py
powershell -File word_finalize.ps1 -Src <brouillon.docx> -Dst ../Manuel_utilisateur_OLIB_v1.0.docx -Pdf ../Manuel_utilisateur_OLIB_v1.0.pdf
```

Le brouillon doit se trouver hors du dossier Temp : Word refuse de l'ouvrir depuis ce dossier.
