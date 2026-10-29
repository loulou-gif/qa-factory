# Contenu du manuel utilisateur OLIB - My Facture (back office et espace client).
# Sources : application observee en recette le 28/10/2026 (captures Playwright),
# completee le 29/10/2026 (onglets F.A.Q et Tutorials du back office),
# tests E2E et cahier de tests v1.0. Les libelles sont ceux reellement affiches
# (interface en anglais). Les elements non verifies sont signales dans
# points_a_confirmer_OLIB.md.

def build(d):
    P, STEPS, BULLETS, FIG, NOTE, LABEL, H, H_UNNUM = (d[k] for k in
        ('P', 'STEPS', 'BULLETS', 'FIG', 'NOTE', 'LABEL', 'H', 'H_UNNUM'))
    x = []
    add = x.append
    MODAL = 11

    # ------------------------------------------------------------------ PREAMBULE
    add(H_UNNUM('PREAMBULE'))
    add(P("Le présent document a pour but de guider les utilisateurs dans l’utilisation de la "
          "plateforme **My Facture** (projet OLIB), solution de mise à disposition des factures "
          "électroniques des clients d’Orange Liberia."))
    add(P("La plateforme comprend deux espaces :", keep_next=True))
    add(BULLETS([
        "le **back office** (« My Facture Backoffice »), réservé au personnel habilité, qui permet "
        "de gérer les comptes clients, les factures, les réclamations, les indicateurs et le paramétrage ;",
        "l’**espace client** (« My Facture »), qui permet aux clients de consulter et télécharger leurs "
        "factures, de suivre leurs réclamations et d’en déposer de nouvelles.",
    ]))
    add(P("Pour chaque menu, le manuel décrit le chemin d’accès, les éléments affichés et les procédures "
          "disponibles, dans l’ordre réel d’exécution."))
    add(P("Les deux espaces sont accessibles depuis un navigateur web, aux adresses communiquées par "
          "l’administrateur de la plateforme. Vous devez disposer d’un compte : un compte utilisateur du back "
          "office, ou un numéro de compte client (ou numéro de ligne) et un mot de passe pour l’espace client."))
    add(P("Les menus et boutons visibles dans le back office dépendent du profil du compte connecté. "
          "L’interface est disponible en anglais (**EN**) et en français (**FR**) ; les libellés cités dans ce "
          "manuel sont ceux de l’interface anglaise."))
    add(NOTE('Remarque', "Dans les captures, les noms, adresses e-mail, numéros de téléphone et paramètres "
             "techniques sont volontairement masqués. Les données visibles sont des données de test."))

    # ------------------------------------------------------------------ FONCTIONNALITES
    add(H_UNNUM('FONCTIONNALITES'))
    add(LABEL('Back office'))
    add(P("La barre de menus, à gauche de l’écran, regroupe les fonctionnalités suivantes :", keep_next=True))
    add(BULLETS([
        "**Home** : synthèse des factures déposées, réclamations à traiter et liste des factures.",
        "**Customers** : comptes clients, envoi et consultation de factures, imports.",
        "**Claims** : suivi et traitement des réclamations des clients.",
        "**KPI** : indicateurs d’activité, de factures et de réclamations.",
        "**Settings** : utilisateurs, profils, notifications, contenus (F.A.Q, tutoriels) et tâches planifiées.",
    ]))
    add(P("Le bandeau supérieur propose le choix de la langue (**EN** / **FR**), les notifications "
          "(cloche), le nom du compte connecté et le bouton de déconnexion."))
    add(LABEL('Espace client'))
    add(P("Le bandeau supérieur de l’espace client propose les menus suivants :", keep_next=True))
    add(BULLETS([
        "**Home** : accueil personnalisé, dernière facture, tuiles de synthèse et raccourcis.",
        "**My invoice** : liste, détail, téléchargement et archives des factures.",
        "**My claims** : historique des réclamations et dépôt d’une réclamation.",
        "**Customer Center** : menu affiché mais inactif lors de la rédaction de ce manuel.",
    ]))
    add(P("Il propose également les actualités (icône mégaphone), le changement de thème clair/sombre, "
          "le choix de la langue et le menu du profil."))

    # ================================================================== BACK OFFICE
    # ------------------------------------------------------------------ I. AUTHENTIFICATION BO
    add(H(0, 'BACK OFFICE – AUTHENTIFICATION', page_break=True))
    add(H(1, 'Se connecter'))
    add(P("Pour accéder au back office, vous devez d’abord vous connecter avec votre compte utilisateur."))
    add(STEPS(["Ouvrez votre navigateur web et saisissez l’adresse du back office. La page de connexion s’affiche."]))
    add(FIG('bo_01_connexion', 'Page de connexion du back office'))
    add(STEPS([
        "Renseignez le champ **Username** avec votre identifiant.",
        "Renseignez le champ **Password**. L’icône en forme d’œil permet d’afficher ou de masquer la saisie.",
        "Si votre compte est un compte Windows, activez l’option **Windows account (LDAP)** "
        "(« Same password as your Windows session »).",
        "Cliquez sur le bouton **Log in**.",
    ]))
    add(LABEL('Résultat'))
    add(P("La page **Home** du back office s’affiche, avec la barre de menus à gauche."))
    add(LABEL('Cas particuliers'))
    add(P("Si l’identifiant ou le mot de passe est incorrect, la connexion est refusée et la page de "
          "connexion reste affichée. Vérifiez votre saisie, puis cliquez de nouveau sur **Log in**."))
    add(H(1, 'Changer la langue'))
    add(P("Cliquez sur **EN** ou **FR**, en haut de l’écran (sur la page de connexion comme dans "
          "l’application). Les libellés s’affichent dans la langue choisie."))
    add(H(1, 'Se déconnecter'))
    add(STEPS([
        "Cliquez sur l’icône de déconnexion, à droite du nom du compte, en haut de l’écran. "
        "Le message « You are about to log out. Continue? » s’affiche.",
    ]))
    add(FIG('bo_06_deconnexion', 'Confirmation de la déconnexion'))
    add(STEPS(["Cliquez sur **Yes** pour confirmer, ou sur **No** pour rester connecté."]))
    add(LABEL('Résultat'))
    add(P("La session est fermée et la page de connexion s’affiche de nouveau."))

    # ------------------------------------------------------------------ II. HOME
    add(H(0, 'MENU HOME', page_break=True))
    add(P("*Prérequis : être connecté au back office.*"))
    add(H(1, 'Présentation de la page d’accueil'))
    add(P("Cliquez sur **Home** dans la barre de menus. La page d’accueil s’affiche.", keep_next=True))
    add(FIG('bo_02_home', 'Page « Home » du back office'))
    add(P("La page présente :", keep_next=True))
    add(BULLETS([
        "les boutons **B2C** / **B2B** (segment de clientèle) et **Month** / **Quarter** / **Semester** (période) ;",
        "le bloc **INVOICES FILED** : nombre de clients, factures lues (**Read**), non lues (**Not read yet**) "
        "et téléchargées (**Downloaded**), avec les boutons **Export invoices** et **Export non-readers** ;",
        "le bloc **TO PROCESS** : réclamations en attente, avec le bouton **Open claims** qui ouvre le menu Claims ;",
        "des cartes d’indicateurs, chacune accompagnée d’une icône de téléchargement.",
    ]))
    add(H(1, 'Consulter la répartition des clients et les dernières réclamations'))
    add(P("Faites défiler la page. Le bloc **Customers by universe** présente la répartition des clients par "
          "univers (**Landline**, **Mobile**, **Internet**, **Other**). Le lien **Open KPIs** ouvre le menu KPI. "
          "Le bloc **Latest claims** liste les dernières réclamations ; le lien **See all** ouvre le menu Claims.", keep_next=True))
    add(FIG('bo_03_home_univers', 'Blocs « Customers by universe » et « Latest claims »'))
    add(H(1, 'Rechercher une facture déposée'))
    add(P("Le tableau **Filed invoices**, en bas de la page, liste les factures déposées."))
    add(STEPS([
        "Renseignez un ou plusieurs critères : **Search customer**, **Search for an invoice number**, "
        "**Invoice status**, univers (**All universes**).",
        "Cliquez sur **Search**. La liste est filtrée selon les critères saisis.",
    ]))
    add(FIG('bo_04_home_factures', 'Tableau « Filed invoices »'))
    add(P("Le tableau affiche les colonnes **Customer**, **Invoice No**, **Universe**, **Issue date**, "
          "**Amount** et **Action**. Utilisez **Rows per page**, **Previous** et **Next** pour naviguer entre les pages."))
    add(H(1, 'Consulter le détail d’une facture'))
    add(STEPS([
        "Dans la colonne **Action** du tableau **Filed invoices**, cliquez sur **See details**. "
        "La fenêtre **Invoice Details** s’affiche.",
    ]))
    add(FIG('bo_05_home_detail_facture', 'Fenêtre « Invoice Details » (valeurs masquées)', width_cm=MODAL))
    add(P("La fenêtre indique si la facture a été téléchargée (**Has it been downloaded**) et lue "
          "(**Has it been read**), puis affiche ses informations : **Invoice Number**, **Period**, **Issue Date**, "
          "**Due Date**, **Amount**, **User name**, **universes**, **Invoice status**, **Subject** et **Description**."))
    add(STEPS(["Cliquez sur **Close** pour fermer la fenêtre."]))

    # ------------------------------------------------------------------ III. CUSTOMERS
    add(H(0, 'MENU CUSTOMERS', page_break=True))
    add(P("*Prérequis : être connecté au back office avec un profil autorisé à gérer les clients.*"))
    add(H(1, 'Consulter et rechercher un compte client'))
    add(P("Cliquez sur **Customers** dans la barre de menus. La page « Customers. Customer accounts, contacts "
          "and access to the customer area. » s’affiche.", keep_next=True))
    add(FIG('bo_10_customers_liste', 'Liste des comptes clients'))
    add(P("La liste affiche les colonnes **Customers account**, **Customer**, **contact**, **Email**, "
          "**Main account**, **Connected at least once**, **Status** et **Action**."))
    add(STEPS([
        "Saisissez un numéro de compte ou un nom dans le champ de recherche.",
        "Sélectionnez au besoin un statut dans la liste **customer status**.",
        "Cliquez sur **Search**. La liste est filtrée.",
    ]))
    add(P("Pour agir sur un compte, cliquez sur **Actions** dans la colonne **Action**. Le menu propose : "
          "**View details**, **Edit**, **Change status**, **Send an invoice**, **View invoices**, **Reset** et **Delete**.", keep_next=True))
    add(FIG('bo_11_customers_actions', 'Menu « Actions » d’un compte client'))

    add(H(1, 'Créer un compte client'))
    add(STEPS([
        "Cliquez sur **Create a customer account**. La fenêtre **Customer account creation** s’affiche.",
    ]))
    add(FIG('bo_12_customers_creation', 'Fenêtre « Customer account creation »', width_cm=MODAL))
    add(STEPS([
        "Indiquez s’il s’agit d’un compte principal (**Is it a main account?**). Pour un compte secondaire, "
        "sélectionnez le compte parent dans **Parent Account**.",
        "Sélectionnez le **Segment** et la langue des notifications (**Notification language**).",
        "Renseignez **Customer Name** et **N° Customer Account**.",
        "Saisissez l’adresse e-mail dans **Email**, puis appuyez sur la touche **Entrée** pour la valider. "
        "Procédez de même pour le numéro de téléphone dans **Contact**.",
        "Cliquez sur **Save** pour enregistrer, ou sur **Close** pour abandonner.",
    ]))
    add(LABEL('Résultat'))
    add(P("Le message « Operation completed successfully » s’affiche et le compte apparaît dans la liste."))

    add(H(1, 'Consulter le détail d’un compte client'))
    add(STEPS([
        "Dans le menu **Actions** du compte, cliquez sur **View details**.",
    ]))
    add(FIG('bo_13_customers_detail', 'Détail d’un compte client', width_cm=MODAL))
    add(P("La fenêtre affiche la date de dernière connexion, les compteurs de factures consultées, "
          "téléchargées et reçues, ainsi que les informations du compte."))

    add(H(1, 'Modifier un compte client'))
    add(STEPS([
        "Dans le menu **Actions** du compte, cliquez sur **Edit**. La fenêtre **Customer account edit** s’affiche, "
        "pré-remplie avec les informations du compte.",
    ]))
    add(FIG('bo_14_customers_modification', 'Fenêtre « Customer account edit »', width_cm=MODAL))
    add(STEPS([
        "Modifiez les champs souhaités.",
        "Cliquez sur **Save**.",
    ]))

    add(H(1, 'Changer le statut d’un compte client'))
    add(STEPS([
        "Dans le menu **Actions** du compte, cliquez sur **Change status**. La fenêtre affiche le nom du client "
        "(**Client name**), son identifiant (**Username**) et son adresse e-mail.",
    ]))
    add(FIG('bo_15_customers_statut', 'Changement de statut d’un compte client', width_cm=MODAL))
    add(STEPS([
        "Dans la liste **Select a status**, recherchez et sélectionnez le nouveau statut. Ce champ est obligatoire "
        "(« This field is required »).",
        "Cliquez sur **Save**.",
    ]))

    add(H(1, 'Envoyer une facture à un client'))
    add(STEPS([
        "Dans le menu **Actions** du compte, cliquez sur **Send an invoice**. Le formulaire d’envoi s’affiche ; "
        "le champ **Customer Account** est pré-rempli.",
    ]))
    add(FIG('bo_16_customers_envoi_facture', 'Formulaire d’envoi d’une facture (exemple de saisie)', width_cm=MODAL))
    add(STEPS([
        "Renseignez **Invoice Number**, **Invoice Amount**, **Universe**, **Issue Date**, **Due Date**, "
        "**Month**, **Year** et **Subject**.",
        "Cliquez sur le bouton **No invoice** pour joindre le fichier de la facture.",
        "Saisissez au besoin un message dans la zone de texte.",
        "Cliquez sur **Save** pour envoyer la facture.",
    ]))
    add(LABEL('Résultat'))
    add(P("La facture est mise à disposition du client dans son espace (menu **My invoice**)."))

    add(H(1, 'Consulter les factures d’un client'))
    add(STEPS([
        "Dans le menu **Actions** du compte, cliquez sur **View invoices**. La liste des factures du client s’affiche.",
    ]))
    add(FIG('bo_17_customers_factures', 'Factures d’un client', width_cm=MODAL))
    add(P("La liste affiche les colonnes **Number**, **Amount**, **Issued on** et **Is open?** (facture "
          "consultée ou non). Vous pouvez :", keep_next=True))
    add(BULLETS([
        "filtrer par **Invoice status** ou par numéro (**Search an invoice number**), puis cliquer sur **Search** ;",
        "télécharger une facture avec l’icône de téléchargement de sa ligne ;",
        "cocher des factures, puis cliquer sur **Download** ou sur **Delete selection**.",
    ]))
    add(STEPS(["Cliquez sur **Close** pour fermer la fenêtre."]))

    add(H(1, 'Réinitialiser un compte client'))
    add(STEPS([
        "Dans le menu **Actions** du compte, cliquez sur **Reset**. Le message « You are about to reset this "
        "customer. Continue? » s’affiche.",
    ]))
    add(FIG('bo_18_customers_reset', 'Confirmation de la réinitialisation'))
    add(STEPS(["Cliquez sur **Yes** pour confirmer, ou sur **No** pour annuler."]))
    add(NOTE('Attention', "L’effet exact de la réinitialisation sur le compte du client n’a pas été observé "
             "lors de la rédaction de ce manuel. Utilisez cette action avec prudence."))

    add(H(1, 'Importer des comptes clients'))
    add(STEPS([
        "Cliquez sur **Bulk import**. La fenêtre **Account import** s’affiche.",
    ]))
    add(FIG('bo_19_customers_import', 'Fenêtre « Account import »', width_cm=MODAL))
    add(STEPS([
        "Cliquez sur le lien de téléchargement du modèle pour obtenir le fichier à compléter.",
        "Cliquez sur la zone **Choose your…** et sélectionnez le fichier complété.",
        "Cliquez sur **Save**.",
    ]))

    add(H(1, 'Supprimer des factures ou des comptes clients en masse'))
    add(P("Les boutons **Delete invoices** et **Delete customer accounts** ouvrent une fenêtre d’import "
          "identique, qui permet de supprimer en masse les éléments listés dans un fichier.", keep_next=True))
    add(FIG('bo_20_customers_suppression_factures', 'Fenêtre de suppression de factures par fichier', width_cm=MODAL))
    add(STEPS([
        "Cliquez sur **Delete invoices** (ou **Delete customer accounts**).",
        "Téléchargez le modèle avec le lien proposé, puis complétez-le.",
        "Sélectionnez le fichier dans la zone **Choose your…**, puis cliquez sur **Save**.",
    ]))
    add(P("Pour supprimer des comptes depuis la liste, cochez-les, puis cliquez sur **Delete selected**. "
          "Pour un seul compte, utilisez **Delete** dans son menu **Actions**."))
    add(NOTE('Attention', "Les suppressions n’ont pas été exécutées lors de la rédaction de ce manuel. "
             "Vérifiez le contenu du fichier avant de valider."))

    # ------------------------------------------------------------------ IV. CLAIMS
    add(H(0, 'MENU CLAIMS', page_break=True))
    add(P("*Prérequis : être connecté au back office avec un profil autorisé à traiter les réclamations.*"))
    add(H(1, 'Consulter les réclamations'))
    add(P("Cliquez sur **Claims** dans la barre de menus. La page « Claims. Customer requests and how they are "
          "being handled. » s’affiche.", keep_next=True))
    add(FIG('bo_30_claims_liste', 'Liste des réclamations'))
    add(P("Les compteurs **Claims created**, **Claims being processed** et **Resolved complaints** présentent "
          "l’état des réclamations. Les boutons **B2C** / **B2B** sélectionnent le segment de clientèle. "
          "La liste affiche les colonnes **Customer**, **Reason for complaint**, **Subject**, **Channel**, "
          "**Status**, **Date created** et **Action**."))
    add(P("Une réclamation passe successivement par les statuts **New**, **In progress** et **Closed**."))
    add(H(1, 'Rechercher une réclamation'))
    add(STEPS([
        "Sélectionnez un statut dans la liste **Status** et/ou saisissez un client dans **Search an customer**.",
        "Cliquez sur **Search**.",
    ]))
    add(H(1, 'Consulter le détail d’une réclamation'))
    add(STEPS([
        "Cliquez sur **Actions** sur la ligne de la réclamation. Le menu propose **See details**, "
        "**Mark in progress** et **Mark Completed**.",
    ]))
    add(FIG('bo_31_claims_actions', 'Menu « Actions » d’une réclamation'))
    add(STEPS(["Cliquez sur **See details**. La fenêtre de détail s’affiche."]))
    add(FIG('bo_32_claims_detail', 'Détail d’une réclamation', width_cm=MODAL))
    add(P("La fenêtre affiche le compte client, le numéro de réclamation (au format REC2026-10-INT-…), "
          "le nom, le motif, le statut, l’univers, le contact, le titre et la description."))
    add(H(1, 'Prendre en charge une réclamation'))
    add(STEPS([
        "Dans le menu **Actions** d’une réclamation au statut **New**, cliquez sur **Mark in progress**. "
        "Le message « You are about to change the status of this claim. Continue? » s’affiche.",
        "Saisissez un commentaire dans la zone de texte.",
    ]))
    add(FIG('bo_33_claims_en_cours', 'Prise en charge d’une réclamation (commentaire de test)'))
    add(STEPS(["Cliquez sur **Yes**."]))
    add(LABEL('Résultat'))
    add(P("Le message « Operation completed successfully » s’affiche et le statut de la réclamation devient "
          "**In progress**.", keep_next=True))
    add(FIG('bo_34_claims_statut_en_cours', 'Réclamation au statut « In progress »'))
    add(H(1, 'Clôturer une réclamation'))
    add(STEPS([
        "Dans le menu **Actions** d’une réclamation au statut **In progress**, cliquez sur **Mark Completed**. "
        "Le message « You are about to process this claim. Continue? » s’affiche.",
        "Saisissez la réponse destinée au client dans la zone de texte.",
    ]))
    add(FIG('bo_35_claims_cloture', 'Clôture d’une réclamation (réponse de test)'))
    add(STEPS(["Cliquez sur **Yes**."]))
    add(LABEL('Résultat'))
    add(P("Le statut de la réclamation devient **Closed**. Le client voit la réponse dans la colonne "
          "**Reply comment** de son menu **My claims**."))

    # ------------------------------------------------------------------ V. KPI
    add(H(0, 'MENU KPI', page_break=True))
    add(P("*Prérequis : être connecté au back office.*"))
    add(H(1, 'Consulter les indicateurs'))
    add(P("Cliquez sur **KPI** dans la barre de menus. La page « KPI. Customer activity, invoices and claims. » "
          "s’affiche.", keep_next=True))
    add(FIG('bo_40_kpi', 'Page « KPI »'))
    add(P("Les cartes présentent notamment le nombre total de clients (avec la répartition **B2B** / **B2C**), "
          "les nouveaux comptes, les factures disponibles et les clients ayant reçu ou téléchargé leurs factures."))
    add(H(1, 'Filtrer les indicateurs'))
    add(STEPS([
        "Dans le bloc **FILTERS**, renseignez la période (**Start date**, **End date**).",
        "Renseignez au besoin **Customer e-mail**, **Universe** et **Segment**.",
        "Cliquez sur **Refresh KPIs**. Les indicateurs et graphiques sont recalculés.",
    ]))
    add(H(1, 'Consulter les graphiques'))
    add(P("Faites défiler la page pour afficher les graphiques (disponibilité des factures, évolution des "
          "connexions, taux de consultation des factures, taux d’échec de connexion, etc.). Les boutons "
          "**Week**, **Month** et **Year** modifient la granularité de certains graphiques.", keep_next=True))
    add(FIG('bo_41_kpi_graphiques', 'Graphiques de la page « KPI »'))

    # ------------------------------------------------------------------ VI. SETTINGS
    add(H(0, 'MENU SETTINGS', page_break=True))
    add(P("*Prérequis : être connecté au back office avec un profil d’administration.*"))
    add(P("Cliquez sur **Settings** dans la barre de menus. La page « Settings. Users, permissions, "
          "notifications, content and scheduled jobs. » s’affiche. Elle comprend les onglets **Users**, "
          "**Profiles**, **Actions**, **F.A.Q**, **Tutorials**, **Notifications**, **Complaint Type**, **Status**, "
          "**Public Campaign**, **Cron collect**, **Cron details**, **Payment check** et **TIMM connection**."))
    add(P("Dans les onglets présentant une liste, la recherche s’effectue en renseignant les critères puis en "
          "cliquant sur **Search**, et les actions d’une ligne sont accessibles dans la colonne **Action**."))

    add(H(1, 'Users (utilisateurs du back office)'))
    add(P("Cliquez sur l’onglet **Users**. La liste des utilisateurs s’affiche avec les colonnes **No.**, "
          "**Login**, **Last Name**, **First Name**, **Email**, **Group**, **Status** et **Action**. "
          "La recherche porte sur le login, le nom et le prénom.", keep_next=True))
    add(FIG('bo_50_settings_users', 'Onglet « Users »'))
    add(LABEL('Créer un utilisateur'))
    add(STEPS([
        "Cliquez sur **Create User**. Le formulaire de création s’affiche.",
    ]))
    add(FIG('bo_51_settings_user_form', 'Formulaire de création d’un utilisateur', width_cm=MODAL))
    add(STEPS([
        "Renseignez **Last Name**, **First Name**, **Email**, **Phone** et **Login**.",
        "Sélectionnez le **Profile** de l’utilisateur.",
        "Cochez **LDAP account** si l’utilisateur se connecte avec son compte Windows.",
        "Cliquez sur **Save**.",
    ]))
    add(NOTE('Remarque', "La création effective d’un utilisateur n’a pas été réalisée lors de la rédaction "
             "de ce manuel ; le mode de communication du mot de passe initial reste à confirmer."))

    add(H(1, 'Profiles (profils et habilitations)'))
    add(P("Cliquez sur l’onglet **Profiles**. La liste des profils s’affiche avec les colonnes **Code**, "
          "**Label**, **Status** et **Action**.", keep_next=True))
    add(FIG('bo_52_settings_profiles', 'Onglet « Profiles »'))
    add(STEPS([
        "Cliquez sur **Create a profile**.",
        "Renseignez **Code** et **Label**.",
        "Cochez, dans l’arborescence, les droits accordés au profil.",
    ]))
    add(FIG('bo_53_settings_profile_form', 'Formulaire d’un profil et arborescence des droits', width_cm=MODAL))
    add(STEPS(["Cliquez sur **Save**."]))

    add(H(1, 'Actions (droits de l’application)'))
    add(P("Cliquez sur l’onglet **Actions**. La liste des actions (droits) s’affiche avec les colonnes "
          "**Code**, **Label**, **Parent** et **Action**. Le bouton **Create an action** permet d’en ajouter une.", keep_next=True))
    add(FIG('bo_54_settings_actions', 'Onglet « Actions »'))

    add(H(1, 'Notifications (modèles de messages)'))
    add(P("Cliquez sur l’onglet **Notifications**. La liste des modèles de messages s’affiche avec les colonnes "
          "**Subject**, **Step**, **Channel**, **Language**, **Body**, **Status** et **Action**. "
          "Pour rechercher un modèle, renseignez **Search a template** puis cliquez sur **Research**.", keep_next=True))
    add(FIG('bo_55_settings_notifications', 'Onglet « Notifications »'))
    add(STEPS([
        "Cliquez sur **Create a notification**.",
        "Renseignez **Code**, **Message subject**, **Language** et **Notification type**.",
        "Rédigez le message dans l’éditeur de texte.",
    ]))
    add(FIG('bo_56_settings_notification_form', 'Formulaire d’un modèle de notification', width_cm=MODAL))
    add(STEPS(["Cliquez sur **Save**."]))

    add(H(1, 'Complaint Type (motifs de réclamation)'))
    add(P("Cliquez sur l’onglet **Complaint Type**. La liste des motifs s’affiche avec les colonnes "
          "**Libelle**, **Date** et **Action**.", keep_next=True))
    add(FIG('bo_57_settings_complaint_type', 'Onglet « Complaint Type »'))
    add(STEPS([
        "Cliquez sur **Create a type of complaint**.",
        "Renseignez **Label** (obligatoire) et, au besoin, **Comment**.",
    ]))
    add(FIG('bo_58_settings_complaint_type_form', 'Formulaire d’un motif de réclamation', width_cm=MODAL))
    add(STEPS(["Cliquez sur **Save**."]))
    add(P("Si le libellé n’est pas renseigné, le message « The label field is required! » s’affiche."))

    add(H(1, 'Status (statuts)'))
    add(P("Cliquez sur l’onglet **Status**. La liste des statuts s’affiche ; la recherche porte sur la source "
          "et le libellé.", keep_next=True))
    add(FIG('bo_59_settings_status', 'Onglet « Status »'))
    add(STEPS([
        "Cliquez sur **Create Status**.",
        "Renseignez **Source**, **Label** et, au besoin, **Comment**.",
    ]))
    add(FIG('bo_60_settings_status_form', 'Formulaire d’un statut', width_cm=MODAL))
    add(STEPS(["Cliquez sur **Save**."]))

    add(H(1, 'Public Campaign (campagnes publicitaires)'))
    add(P("Cliquez sur l’onglet **Public Campaign**. La liste des campagnes s’affiche avec les colonnes "
          "**Name**, **Segment**, **Message**, **Number of people clicked**, **Start date**, **End date** et "
          "**Action**. Vous pouvez filtrer par période et par nom avant de cliquer sur **Search**.", keep_next=True))
    add(FIG('bo_61_settings_campaigns', 'Onglet « Public Campaign »'))
    add(STEPS([
        "Cliquez sur **Create an advertising campaign**. La fenêtre **Advertising Campaign** s’affiche.",
        "Sélectionnez la langue du contenu (**English** ou **French**) avec les onglets **Content language**.",
        "Renseignez **Title**, **Segment**, **Start date**, **End date** et **Message**.",
        "Laissez l’option **Active** sur **Yes** pour activer la campagne.",
    ]))
    add(FIG('bo_62_settings_campaign_form', 'Fenêtre « Advertising Campaign »', width_cm=8))
    add(STEPS(["Cliquez sur **Save**."]))

    add(H(1, 'F.A.Q (questions fréquentes)'))
    add(P("Cliquez sur l’onglet **F.A.Q**. La page de gestion de la F.A.Q permet de publier les questions "
          "affichées dans l’onglet **Frequently asked questions** de la rubrique **Tutorials and FAQ** de "
          "l’espace client. Elle présente les colonnes **Title**, **Detail**, **Segment**, **Date** et **Action**. "
          "Pour retrouver une question, renseignez **Search by title** puis cliquez sur **Search**.", keep_next=True))
    add(FIG('bo_63_settings_faq', 'Onglet « F.A.Q » (question de test)'))
    add(LABEL('Créer une question'))
    add(STEPS([
        "Cliquez sur **Create a F.A.Q**. La fenêtre **F.A.Q** s’affiche.",
        "Sélectionnez la langue du contenu (**English** ou **French**).",
        "Renseignez **Title**, sélectionnez le ou les **Segment** (**B2B**, **B2C**), puis rédigez la réponse "
        "dans **Response**.",
    ]))
    add(FIG('bo_64_settings_faq_form', 'Fenêtre « F.A.Q »', width_cm=MODAL))
    add(STEPS(["Cliquez sur **Save**."]))
    add(LABEL('Résultat'))
    add(P("Le message « Operation completed successfully » s’affiche et la question apparaît dans la liste. "
          "Elle est aussitôt visible dans l’onglet **Frequently asked questions** de l’espace client, y compris "
          "dans la rubrique d’aide accessible sans connexion."))
    add(P("Si aucun segment n’est sélectionné, le message « Please select at least one segment » s’affiche et "
          "la question n’est pas enregistrée."))
    add(LABEL('Modifier ou supprimer une question'))
    add(BULLETS([
        "Pour modifier une question, cliquez sur l’icône crayon de sa ligne, modifiez les champs, puis cliquez sur **Save**.",
        "Pour supprimer une question, cliquez sur l’icône corbeille de sa ligne. Le message « You are about to "
        "delete this item. Continue? » s’affiche ; cliquez sur **delete** pour confirmer ou sur **No** pour "
        "annuler. La question n’est plus affichée dans l’espace client.",
    ]))

    add(H(1, 'Tutorials (tutoriels)'))
    add(P("Cliquez sur l’onglet **Tutorials**. La page de gestion des tutoriels permet de publier les tutoriels "
          "affichés dans l’onglet **Tutorials** de la rubrique **Tutorials and FAQ** de l’espace client. Elle "
          "présente les colonnes **Title**, **Description**, **Date** et **Action**. Pour retrouver un tutoriel, "
          "renseignez **Search by title** puis cliquez sur **Search**.", keep_next=True))
    add(FIG('bo_69_settings_tutorials', 'Onglet « Tutorials » (tutoriel de test)'))
    add(P("Un tutoriel est composé d’un titre, d’une description et d’une ou plusieurs étapes. Chaque étape "
          "comprend un titre, un message, une adresse de vidéo et, si besoin, une image."))
    add(LABEL('Créer un tutoriel'))
    add(STEPS([
        "Cliquez sur **Create tutorial**. La page **Create Tutorial** s’affiche.",
        "Sélectionnez la langue du contenu (**English** ou **French**) avec les onglets **Content language**.",
        "Renseignez **Title**.",
        "Sélectionnez le ou les **Segment** (**B2B**, **B2C**) auxquels le tutoriel est destiné.",
        "Sélectionnez le **Status** (**Active**, **Disabled** ou **Suspended**).",
        "Rédigez la présentation du tutoriel dans **Description**.",
    ]))
    add(FIG('bo_70_settings_tutorial_form', 'Page « Create Tutorial »'))
    add(LABEL('Ajouter une étape'))
    add(STEPS([
        "Dans la partie droite de la page, cliquez sur **Add step**. La fenêtre de l’étape s’affiche.",
        "Renseignez **Title**.",
        "Choisissez la position du texte (**Right** ou **Left**) dans la liste « Please select the position » "
        "(ce champ est libellé **Segment** dans l’interface).",
        "Sélectionnez le **Status** de l’étape.",
        "Au besoin, cliquez sur **Choose an image** pour joindre une image.",
        "Renseignez l’adresse de la vidéo dans **Video** (par exemple une adresse YouTube).",
        "Rédigez le contenu de l’étape dans **Message**.",
    ]))
    add(FIG('bo_71_settings_tutorial_step', 'Fenêtre d’ajout d’une étape', width_cm=MODAL))
    add(STEPS([
        "Cliquez sur **Save**. L’étape apparaît dans le tableau des étapes (colonnes **No.**, **Title**, "
        "**Position**, **Image**, **Video**). Répétez l’opération pour chaque étape.",
    ]))
    add(FIG('bo_72_settings_tutorial_steps', 'Tutoriel et tableau de ses étapes'))
    add(P("Dans le tableau des étapes, l’icône crayon permet de modifier une étape et l’icône « – » de la retirer."))
    add(LABEL('Enregistrer le tutoriel'))
    add(STEPS([
        "Cliquez sur **Save**, en bas du formulaire du tutoriel, ou sur **Cancel** pour abandonner.",
    ]))
    add(LABEL('Résultat'))
    add(P("Le message « Operation completed successfully » s’affiche, la liste des tutoriels est de nouveau "
          "affichée et le tutoriel apparaît dans l’onglet **Tutorials** de l’espace client."))
    add(LABEL('Cas particuliers'))
    add(BULLETS([
        "Sans segment ni statut, les messages « At least one segment must be selected » et « Status field is "
        "required » s’affichent.",
        "Sans étape, le message « Warning, please add at least one step » s’affiche : un tutoriel doit comporter "
        "au moins une étape.",
        "Dans la fenêtre d’une étape, les messages « Position field is required », « Status field is required » et "
        "« Please enter a valid URL! » signalent un champ manquant ou une adresse de vidéo invalide.",
    ]))
    add(LABEL('Modifier ou supprimer un tutoriel'))
    add(BULLETS([
        "Pour modifier un tutoriel, cliquez sur l’icône crayon de sa ligne. Le formulaire s’affiche avec les "
        "valeurs et les étapes enregistrées ; modifiez-les, puis cliquez sur **Save**.",
        "Pour supprimer un tutoriel, cliquez sur l’icône corbeille de sa ligne, puis sur **Delete** dans le "
        "message de confirmation.",
    ]))
    add(NOTE('Remarque', "Lors de la rédaction de ce manuel, la suppression d’un tutoriel comportant des étapes "
             "était refusée par l’application sans message d’erreur, et un tutoriel au statut **Disabled** "
             "restait affiché dans l’espace client. Ces comportements sont à confirmer."))

    add(H(1, 'Cron collect et Cron details (tâches planifiées)'))
    add(P("Les onglets **Cron collect** (« Collection totals ») et **Cron details** (« Details + PDF + Email ») "
          "paramètrent les tâches planifiées de collecte des factures."))
    add(FIG('bo_65_settings_cron_collect', 'Onglet « Cron collect »'))
    add(LABEL('Modifier la planification'))
    add(STEPS([
        "Renseignez le jour du mois (**Day of month**) et sélectionnez l’heure (**Hour**).",
        "Activez ou désactivez la tâche avec l’option **Enable**. L’expression **CRON expression** est "
        "mise à jour automatiquement.",
        "Cliquez sur **Save**, ou sur **Cancel** pour abandonner.",
    ]))
    add(LABEL('Lancer une simulation'))
    add(STEPS([
        "Dans le bloc **Collect Simulation** (ou **Detail Simulation**), sélectionnez la période (**Period**) "
        "et le type de document (**Document type**).",
        "Cliquez sur **Run Simulation**. La simulation est exécutée pour la période et le type de document choisis.",
    ]))
    add(FIG('bo_66_settings_cron_details', 'Onglet « Cron details »'))

    add(H(1, 'Payment check (vérification des paiements)'))
    add(P("L’onglet **Payment check** (« Orange Money payment check ») paramètre l’interrogation périodique du "
          "système TIMM pour chaque paiement en attente : la facture passe à l’état payé (TS) ou de nouveau impayé (TF).", keep_next=True))
    add(FIG('bo_67_settings_payment_check', 'Onglet « Payment check »'))
    add(STEPS([
        "Sélectionnez la fréquence dans **Frequency**.",
        "Activez ou désactivez l’option **Automatic check enabled**.",
        "Cliquez sur **Save**.",
    ]))
    add(P("Le bouton **Check now** lance immédiatement la vérification de tous les paiements en attente."))
    add(NOTE('Attention', "**Check now** modifie l’état payé / impayé des factures. Il n’a pas été exécuté lors "
             "de la rédaction de ce manuel."))

    add(H(1, 'TIMM connection'))
    add(P("L’onglet **TIMM connection** contient les adresses de l’API TIMM (**Totals URL**, **Details URL**, "
          "**Orange Money payment URL (PayStart)**, **Orange Money payment status URL (Transaction/Status)**, "
          "**Customer record URL (CRM)**, etc.) et les identifiants associés. Le mot de passe est chiffré et "
          "n’est jamais réaffiché.", keep_next=True))
    add(FIG('bo_68_settings_timm', 'Onglet « TIMM connection » (valeurs masquées)'))
    add(NOTE('Attention', "Ces paramètres conditionnent la récupération des factures et des paiements. "
             "Ne les modifiez qu’à la demande de l’équipe technique."))

    # ================================================================== ESPACE CLIENT
    # ------------------------------------------------------------------ VII. AUTHENTIFICATION FO
    add(H(0, 'ESPACE CLIENT – AUTHENTIFICATION', page_break=True))
    add(H(1, 'Se connecter'))
    add(STEPS(["Ouvrez votre navigateur web et saisissez l’adresse de l’espace client. La page de connexion s’affiche."]))
    add(FIG('fo_01_connexion', 'Page de connexion de l’espace client'))
    add(STEPS([
        "Renseignez le champ **Account number or line number** avec votre numéro de compte client ou votre "
        "numéro de ligne.",
        "Renseignez le champ **Password**.",
        "Cliquez sur **Login**.",
    ]))
    add(LABEL('Résultat'))
    add(P("La page d’accueil (**Home**) de l’espace client s’affiche."))
    add(P("Les boutons **FR** / **EN** et l’icône de thème, en haut à droite, permettent de changer la langue "
          "et l’affichage clair/sombre avant même la connexion."))

    add(H(1, 'Mot de passe oublié'))
    add(STEPS([
        "Sur la page de connexion, cliquez sur **Forgot password ?**. La page « Forgotten your password ? » s’affiche.",
    ]))
    add(FIG('fo_02_mot_de_passe_oublie', 'Page « Forgotten your password ? »'))
    add(STEPS([
        "Renseignez **Account number or line number**.",
        "Cliquez sur **Submit**. Un code de réinitialisation vous est envoyé.",
    ]))
    add(P("Le lien **Go back to the login page** permet de revenir à la page de connexion."))
    add(NOTE('Remarque', "L’envoi du code et la suite de la procédure n’ont pas été exécutés lors de la "
             "rédaction de ce manuel."))

    add(H(1, 'Identifiant oublié'))
    add(STEPS([
        "Sur la page de connexion, cliquez sur la tuile **Forgotten identifier**. Le formulaire « Welcome to your "
        "online support form » s’affiche.",
    ]))
    add(FIG('fo_03_identifiant_oublie', 'Formulaire « Forgotten identifier »'))
    add(STEPS([
        "Choisissez le mode de contact (**By Phone** ou **By Email**) et renseignez le numéro ou l’adresse.",
        "Sélectionnez l’univers concerné (**Other**, **Internet**, **Mobile**, **Landline**).",
        "Sélectionnez le motif dans **Reason of claim** et saisissez la **Description**.",
        "Cliquez sur **Send**.",
    ]))
    add(P("Le bouton **Close** ferme le formulaire sans l’envoyer."))

    add(H(1, 'Déposer une réclamation sans être connecté'))
    add(STEPS([
        "Sur la page de connexion, cliquez sur la tuile **Make a new claim** (« No login needed »).",
    ]))
    add(FIG('fo_04_reclamation_sans_connexion', 'Formulaire de réclamation sans connexion'))
    add(STEPS([
        "Renseignez **Full name** et, si vous le connaissez, **Customer account**.",
        "Choisissez le mode de contact (**By Phone** ou **By Email**) et renseignez le numéro ou l’adresse.",
        "Sélectionnez l’**Universe** et le motif (**Reason of claim**), puis saisissez la **Description**.",
        "Validez la vérification de sécurité affichée en bas du formulaire, puis envoyez le formulaire.",
    ]))
    add(NOTE('Remarque', "Lors de la rédaction de ce manuel, la vérification de sécurité du formulaire était "
             "en erreur ; l’envoi n’a pas pu être observé."))

    add(H(1, 'Consulter l’aide sans être connecté'))
    add(P("La rubrique **Tutorials and FAQ** est accessible depuis la page de connexion. Elle comprend un champ "
          "de recherche par mots-clés (**Search using keywords**) et deux onglets : **Tutorials** et "
          "**Frequently asked questions**.", keep_next=True))
    add(FIG('fo_07_aide_publique_tutoriel', 'Rubrique « Tutorials and FAQ » – onglet « Tutorials » (tutoriel de test)'))
    add(STEPS([
        "Dans l’onglet **Tutorials**, cliquez sur un tutoriel de la liste. Son contenu s’affiche dans la partie "
        "droite (« Select a tutorial from the list. » tant qu’aucun tutoriel n’est sélectionné).",
        "Cliquez sur l’onglet **Frequently asked questions**. Les questions publiées s’affichent ; cliquez sur "
        "une question pour afficher ou masquer sa réponse.",
    ]))
    add(FIG('fo_08_aide_publique_faq_contenu', 'Onglet « Frequently asked questions » (question de test)'))
    add(P("Le bouton **Go back to the login page** permet de revenir à la page de connexion. Les tutoriels et "
          "les questions sont publiés depuis le back office (onglets **Tutorials** et **F.A.Q** du menu "
          "**Settings**). Lorsqu’aucun contenu n’est publié, les messages « No tutorials available. » et "
          "« No question available. » s’affichent."))
    add(NOTE('Remarque', "Lors de la rédaction de ce manuel, le contenu d’un tutoriel sélectionné restait en "
             "cours de chargement : les étapes n’ont pas pu être observées dans l’espace client."))

    # ------------------------------------------------------------------ VIII. HOME FO
    add(H(0, 'ESPACE CLIENT – MENU HOME', page_break=True))
    add(P("*Prérequis : être connecté à l’espace client.*"))
    add(H(1, 'Présentation de la page d’accueil'))
    add(P("Après la connexion, ou en cliquant sur **Home**, la page d’accueil s’affiche.", keep_next=True))
    add(FIG('fo_10_accueil', 'Page d’accueil de l’espace client'))
    add(P("La page présente :", keep_next=True))
    add(BULLETS([
        "un bandeau orange invitant à donner votre avis sur la facturation (**Answer in 2 minutes**), que la croix permet de fermer ;",
        "votre dernière facture disponible : montant (**INVOICE AMOUNT**), date d’échéance, compte, et les boutons "
        "**Pay with Mobile Money** et **View invoice** ;",
        "les tuiles **Account** (nombre de comptes, avec le lien **+ Add**), **Monthly invoice**, **Unread invoice** "
        "et **Unpaid invoice** ;",
        "le bloc **My latest invoices**, filtrable avec **All**, **Unread** et **Unpaid**, et le lien **See all my invoices**.",
    ]))
    add(H(1, 'Utiliser les raccourcis'))
    add(P("Faites défiler la page. Le bloc **Shortcuts** propose :", keep_next=True))
    add(BULLETS([
        "**Make a claim** : suivre vos demandes ou déposer une réclamation ;",
        "**Link an account** : regrouper toutes vos lignes ;",
        "**Tutorials and FAQ** : aide sur le paiement, le téléchargement et la compréhension de votre facture.",
    ]))
    add(FIG('fo_12_accueil_raccourcis', 'Bloc « Shortcuts » de la page d’accueil'))
    add(H(1, 'Menu du profil'))
    add(P("Cliquez sur l’icône du profil, en haut à droite. Le menu affiche votre identifiant et propose "
          "**Bind an account**, **Change my password** et **Logout**.", keep_next=True))
    add(FIG('fo_13_menu_profil', 'Menu du profil'))
    add(H(1, 'Lier un autre compte'))
    add(STEPS([
        "Dans le menu du profil, cliquez sur **Bind an account** (ou sur **+ Add** dans la tuile **Account**). "
        "La fenêtre **Bind another account** s’affiche.",
        "Renseignez **Account to be binded** avec l’identifiant du compte à rattacher.",
        "Cliquez sur **Next** et suivez les instructions affichées.",
    ]))
    add(FIG('fo_14_lier_compte', 'Fenêtre « Bind another account »'))
    add(NOTE('Remarque', "Les étapes suivant **Next** n’ont pas été observées lors de la rédaction de ce manuel."))
    add(H(1, 'Changer votre mot de passe'))
    add(STEPS([
        "Dans le menu du profil, cliquez sur **Change my password**. La fenêtre **Change my password** s’affiche.",
        "Renseignez **Current password**.",
        "Renseignez **New password**. Un indicateur affiche la robustesse du mot de passe (de **Weak** à **Strong**).",
        "Renseignez **Confirm password** avec le même mot de passe.",
    ]))
    add(FIG('fo_15_changer_mot_de_passe', 'Fenêtre « Change my password »'))
    add(P("Le mot de passe doit contenir au moins 10 caractères, au moins 1 chiffre, au moins 1 caractère "
          "spécial et au moins 1 lettre majuscule."))
    add(STEPS(["Cliquez sur **Submit**."]))
    add(H(1, 'Consulter les actualités'))
    add(P("Cliquez sur l’icône en forme de mégaphone, dans le bandeau supérieur, pour afficher les actualités.", keep_next=True))
    add(FIG('fo_16_actualites', 'Accès aux actualités (icône mégaphone)'))
    add(NOTE('Remarque', "Lors de la rédaction de ce manuel, aucune actualité n’était affichée."))
    add(H(1, 'Changer la langue'))
    add(P("Cliquez sur **FR** ou **EN** dans le bandeau supérieur. Les menus et libellés s’affichent dans la "
          "langue choisie (par exemple **Accueil**, **Mes Factures**, **Mes Réclamations** en français).", keep_next=True))
    add(FIG('fo_18_accueil_fr', 'Espace client affiché en français'))
    add(H(1, 'Se déconnecter'))
    add(P("Dans le menu du profil, cliquez sur **Logout**. La page de connexion s’affiche."))

    # ------------------------------------------------------------------ IX. MY INVOICE
    add(H(0, 'ESPACE CLIENT – MENU MY INVOICE', page_break=True))
    add(P("*Prérequis : être connecté à l’espace client.*"))
    add(H(1, 'Consulter la liste de vos factures'))
    add(P("Cliquez sur **My invoice** dans le bandeau supérieur. La page « My invoice. Manage your invoices "
          "with ease. » s’affiche.", keep_next=True))
    add(FIG('fo_20_factures_liste', 'Page « My invoice »'))
    add(P("La partie gauche affiche le nombre de factures et leur liste (univers, numéro, période). "
          "Si plusieurs comptes sont liés, sélectionnez le compte dans la liste **My identifier**."))
    add(H(1, 'Rechercher et filtrer vos factures'))
    add(STEPS([
        "Saisissez un numéro de facture dans le champ **Search by invoice’s number**, puis cliquez sur l’icône loupe.",
        "Ou utilisez les **Filter options** : **Filter by universe**, **Filter by period** et **Filter by status**.",
    ]))
    add(FIG('fo_21_factures_filtre', 'Options de filtrage des factures'))
    add(H(1, 'Consulter et télécharger une facture'))
    add(STEPS([
        "Cliquez sur une facture de la liste. Son détail s’affiche dans la partie droite, avec un aperçu du document.",
    ]))
    add(FIG('fo_22_facture_detail', 'Détail d’une facture (document de test)'))
    add(STEPS([
        "Cliquez sur **Download** pour télécharger la facture.",
    ]))
    add(P("Depuis le détail, le bouton **Make a claim** ouvre le formulaire de réclamation et le bouton "
          "**I pay my invoice** lance le paiement."))
    add(NOTE('Remarque', "Le parcours de paiement (Mobile Money) n’a pas été exécuté lors de la rédaction de ce manuel."))
    add(H(1, 'Consulter vos factures archivées'))
    add(STEPS([
        "Cliquez sur l’onglet **archived invoices**. La liste des factures archivées s’affiche.",
        "Cliquez sur le bouton de téléchargement d’une facture pour la télécharger et la consulter.",
    ]))
    add(FIG('fo_23_factures_archives', 'Onglet « archived invoices »'))
    add(P("Si aucune facture n’est archivée, le message « no archived invoice were found. » s’affiche."))

    # ------------------------------------------------------------------ X. MY CLAIMS
    add(H(0, 'ESPACE CLIENT – MENU MY CLAIMS', page_break=True))
    add(P("*Prérequis : être connecté à l’espace client.*"))
    add(H(1, 'Consulter vos réclamations'))
    add(P("Cliquez sur **My claims** dans le bandeau supérieur. La page « Track your claims » s’affiche.", keep_next=True))
    add(FIG('fo_30_reclamations_liste', 'Page « My claims »'))
    add(P("Le tableau **My claims history** affiche les colonnes **N°**, **DATE OF ISSUE**, **ACCOUNT**, "
          "**TITLE**, **DESCRIPTION**, **REPLY COMMENT** et **STATUS**. Le champ **Search a claims** permet "
          "de rechercher une réclamation."))
    add(H(1, 'Déposer une réclamation'))
    add(STEPS([
        "Cliquez sur **Make a claim**. Le formulaire « Welcome to your online support form » s’affiche.",
        "Choisissez le mode de contact (**By Phone** ou **By Email**) et vérifiez le numéro ou l’adresse.",
        "Sélectionnez le **Customer account** et, si la réclamation porte sur une facture, l’**Invoice concerned**.",
        "Sélectionnez l’**Universe** et le motif (**Reason of claim**).",
        "Saisissez la **Description** de votre demande.",
    ]))
    add(FIG('fo_31_reclamation_formulaire', 'Formulaire de réclamation (exemple non envoyé)'))
    add(STEPS(["Envoyez le formulaire avec le bouton situé en bas de la fenêtre."]))
    add(P("Pour contester une facture, utilisez le lien **HERE** affiché sous le motif de réclamation."))
    add(LABEL('Résultat'))
    add(P("La réclamation apparaît dans **My claims history**. Elle est traitée depuis le back office "
          "(voir le chapitre **Menu Claims**)."))
    add(H(1, 'Consulter le détail d’une réclamation'))
    add(STEPS([
        "Sur la ligne de la réclamation, cliquez sur **details**.",
    ]))
    add(FIG('fo_32_reclamation_detail', 'Détail d’une réclamation clôturée'))
    add(P("La fenêtre affiche le numéro, les dates de création et de clôture, le statut, le titre, la "
          "description et, une fois la réclamation traitée, la réponse (**Reply comment**). "
          "Cliquez sur **Close** pour la fermer."))

    # ------------------------------------------------------------------ XI. AIDE
    add(H(0, 'ESPACE CLIENT – TUTORIALS AND FAQ', page_break=True))
    add(P("*Prérequis : être connecté à l’espace client.*"))
    add(P("Cliquez sur le raccourci **Tutorials and FAQ** de la page d’accueil. La rubrique d’aide s’affiche.", keep_next=True))
    add(FIG('fo_40_aide_client', 'Rubrique « Tutorials and FAQ » depuis l’espace client'))
    add(STEPS([
        "Saisissez un mot-clé dans **Search using keywords** pour rechercher un contenu.",
        "Cliquez sur l’onglet **Tutorials** ou **Frequently asked questions** pour afficher le contenu correspondant.",
    ]))
    add(P("Les tutoriels et les questions affichés sont ceux publiés depuis le back office pour votre segment "
          "(voir **Tutorials** et **F.A.Q** dans le chapitre **Menu Settings**)."))

    return ''.join(x)
