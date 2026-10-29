Skill — Génération des manuels utilisateurs et cahiers de tests
1. Rôle et objectif
Cette Skill définit la méthode à suivre pour produire, à partir des spécifications Markdown, des scripts de tests automatisés, de l’application accessible via Playwright MCP et des modèles fournis, deux livrables professionnels :
1. un manuel utilisateur Word (.docx) qui explique comment utiliser les fonctionnalités de l’application ;
2. un cahier de tests Excel (.xlsx) qui décrit les scénarios à exécuter et permet de consigner les résultats de recette.
Les documents témoins servent de référence pour le ton, la structure rédactionnelle et le niveau de détail. Le document CEPICI fourni séparément sert de référence graphique et de mise en page. Ne pas confondre ces deux rôles.

La priorité des sources est la suivante :
1. modèle Word ou Excel fourni : mise en page, styles, logos, couleurs, dimensions, en-têtes et pieds de page ;
2. spécifications Markdown et règles métier : comportement fonctionnel attendu ;
3. scripts automatisés : parcours, actions, données et assertions déjà définis ;
4. observation directe de l’application via Playwright MCP : libellés et comportements réellement visibles ;
5. documents témoins : conventions de rédaction et organisation, sans reprendre leurs erreurs, données ou fonctionnalités propres à un autre projet.
Ne jamais inventer une fonctionnalité, une règle métier, un champ, un résultat attendu, une valeur de test ou un comportement non étayé par les sources. Si une information manque ou si les sources se contredisent, la signaler dans une liste de points à clarifier plutôt que de trancher arbitrairement.
2. Sources de référence et enseignements tirés des documents témoins
2.1 Manuels utilisateurs
Les manuels YELEN OCI et ANSUT Gestion d’incident présentent des conventions communes :
- une page de couverture avec le nom du projet, la date, la version et l’auteur/rédacteur lorsqu’ils sont connus ;
- un sommaire organisé selon les chapitres et sous-chapitres ;
- un préambule qui précise l’objectif du manuel, le mode d’accès et les prérequis ;
- une présentation synthétique des fonctionnalités ou menus ;
- un chapitre par module ou menu, puis des sous-sections par action ou procédure ;
- des captures d’écran insérées à proximité des instructions qu’elles illustrent ;
- des consignes présentées dans l’ordre réel d’exécution, avec les noms des menus, champs et boutons.
Exemples observés : YELEN OCI détaille l’ajout, le filtrage et la modification de contenus ; le manuel ANSUT décrit la création d’un incident, les cas particuliers et les différentes vues de traitement. Ces exemples guident la structure, mais leur contenu métier ne doit pas être réutilisé pour une autre application.
2.2 Cahiers de tests Excel
Les deux cahiers fournis utilisent une feuille de tests organisée par fonctionnalités. Le cahier BNI fournit une structure de colonnes particulièrement explicite :
- FONCTIONNALITÉS : module ou rubrique testée ;
- ID : identifiant unique du cas de test, par exemple CT0001 ;
- PRÉREQUIS : état initial, droits et données nécessaires ;
- DESCRIPTION : objectif du test formulé en une phrase ;
- ACTIONS : étapes numérotées dans l’ordre d’exécution ;
- RÉSULTATS ATTENDUS : comportement attendu après une action ou à la fin du scénario ;
- STATUT ATTENDU : valeur attendue, généralement OK lorsque le scénario doit fonctionner ;
- RÉSULTAT : résultat constaté pendant la recette ;
- STATUT : statut constaté (OK, NOK, ou valeur explicitement prévue par le modèle) ;
- COMMENTAIRE : précision, anomalie ou question éventuelle.
Le cahier Dashboard présente également une zone de métadonnées : lien de l’application, contact, auteur des tests, date et version du document, période de test et données de test. Conserver les champs du modèle Excel réellement fourni, même si leur libellé diffère légèrement de cette liste.

Les cellules fusionnées et la disposition visuelle des modèles peuvent être importantes : ne pas reconstruire arbitrairement le classeur en supprimant ses regroupements, ses styles ou ses sections. Avant de produire un nouveau cahier, inspecter la structure et les styles du fichier modèle.
3. Règles communes aux deux livrables
- Rédiger en français professionnel, correct et accessible.
- Employer une terminologie stable dans tout le document. Utiliser les libellés exacts visibles dans l’application lorsqu’ils sont disponibles.
- Conserver les noms de menus, champs, boutons, onglets et statuts tels qu’ils apparaissent dans l’interface, entre guillemets si cela améliore la lisibilité.
- Décrire les actions dans leur ordre réel. Une étape doit correspondre à une action claire et réalisable.
- Éviter les formulations vagues comme « faire le nécessaire », « traiter correctement » ou « vérifier que tout fonctionne ».
- Ne pas ajouter de promesses, d’explications métier ou de conseils qui ne sont pas confirmés par les sources.
- Ne pas exposer de vrais mots de passe, secrets, données personnelles ou données de production dans les exemples et captures. Utiliser des données de test autorisées.
- Ne pas modifier le modèle de marque pour le rendre plus « moderne » : respecter le fichier témoin fourni.
- Ne jamais marquer un test comme exécuté ni renseigner un résultat constaté sur la seule base d’une rédaction générée. Le statut réel ne peut être rempli qu’après exécution et observation effective.
- Si un scénario ne peut pas être observé dans l’environnement disponible, le laisser comme scénario à exécuter et indiquer le blocage ; ne pas simuler un résultat.
3.1 Workflow obligatoire avant toute génération
Cette section est prioritaire sur toute consigne plus générale de la Skill. La génération ne doit pas commencer directement par la rédaction.
Phase A — Définir le périmètre et inventorier les sources
1. Confirmer le livrable demandé : manuel Word, cahier de tests Excel, ou les deux.
2. Inspecter les dossiers et fichiers réellement présents. Ne pas supposer qu'un chemin ou un document existe parce qu'il est cité dans une consigne.
3. Repérer les modèles Word/Excel et les documents témoins pertinents.
4. Identifier les spécifications Markdown liées au périmètre, les scripts Playwright, les Page Objects, les données de test et les utilitaires.
5. Établir une matrice de couverture avant la rédaction.
La matrice doit au minimum contenir :
Élément	Source fonctionnelle	Test associé	Observation Playwright	État de vérification	Action
Fonctionnalité ou procédure	Fichier et section	Fichier/scénario	Écran ou capture	Confirmé / partiel / non vérifié / contradictoire	Documenter / vérifier / clarifier


Ne pas confondre « présent dans un test » avec « complètement couvert », ni « présent dans l'interface » avec « règle métier validée ».
Phase B — Distinguer les sources de vérité
Utiliser chaque source pour ce qu'elle peut réellement démontrer :
- Spécifications fonctionnelles : définition du besoin, règles métier, contraintes et comportements attendus.
- Scripts de tests et assertions : scénarios automatisés, actions réalisées, conditions vérifiées et résultats attendus codés.
- Playwright MCP et application réelle : libellés, emplacement des contrôles, état de l'interface, parcours effectivement observés et messages réellement affichés.
- Page Objects et utilitaires : détails techniques utiles pour comprendre les parcours automatisés ; ne pas les exposer dans le manuel utilisateur.
- Modèles documentaires : mise en page et identité visuelle.
- Documents témoins : ton, organisation et niveau de détail, jamais les règles métier d'un autre produit.
Si deux sources se contredisent, ne pas choisir arbitrairement celle qui semble la plus plausible. Consigner l'écart avec les références concernées et suspendre uniquement la partie qui dépend de cette décision.
Phase C — Construire le parcours utilisateur de bout en bout
Pour tout manuel d'une application protégée par authentification, documenter le parcours réel depuis l'état initial jusqu'à la fonctionnalité demandée.

Ordre par défaut :
1. Prérequis et accès à l'application.
2. Authentification, si nécessaire.
3. Résultat observable après connexion.
4. Navigation vers le menu ou module concerné.
5. Accès à la fonctionnalité.
6. Procédures disponibles et résultats observés.
La connexion ne doit jamais être omise au seul motif que les scripts Playwright utilisent storageState, une session persistée ou un global-setup. Ces mécanismes techniques ne remplacent pas le parcours utilisateur. Si l'authentification est un prérequis commun, elle doit être expliquée avant le premier menu protégé, avec les libellés réellement observés. Ne jamais publier les mots de passe, jetons, cookies ou comptes techniques confidentiels.

Si l'utilisateur demande uniquement un sous-chapitre et qu'un manuel global documente déjà la connexion, une référence explicite à ce chapitre peut suffire. En l'absence de preuve qu'un tel chapitre existe dans le livrable, ne pas supposer qu'il est présent.
Phase D — Exécuter l'observation sans prendre de risques
1. Réutiliser l'authentification, les fixtures, les Page Objects, les données et les scripts existants lorsque cela est approprié.
2. Ne pas lancer automatiquement toute la suite de tests si elle peut modifier ou supprimer des données partagées.
3. Identifier les actions destructrices (suppression, modification de paramètres partagés, envoi, clôture, etc.) et ne les exécuter que dans un environnement et avec des données autorisés.
4. Pour les scénarios d'ajout ou de modification, privilégier des données de test uniques si le projet prévoit déjà ce mécanisme.
5. Capturer les états réellement observés. Une capture de formulaire vide ne prouve pas le résultat d'un enregistrement.
6. Si une action n'est pas réalisable ou sûre, indiquer « non vérifié » et expliquer le blocage. Ne pas simuler un succès.
Phase E — Rédiger seulement à partir des éléments suffisamment étayés
Pour chaque procédure, confirmer :
- le point de départ ;
- les droits ou prérequis nécessaires, lorsqu'ils sont connus ;
- les contrôles à utiliser et leurs libellés exacts ;
- les données à saisir ou sélectionner ;
- l'action de validation ;
- le résultat attendu issu de la spécification ;
- le résultat réellement observé, s'il a été vérifié ;
- les cas particuliers et limites documentés.
Les informations non confirmées doivent rester dans un registre séparé de points à clarifier. Ne pas remplir les trous avec des hypothèses plausibles. N'affirmer ni « obligatoire », ni « automatiquement », ni « immédiatement », ni « avec succès » sans source suffisante.
Phase F — Contrôle du fond avant contrôle de la forme
Effectuer les contrôles dans cet ordre :
1. Complétude du parcours et du périmètre.
2. Exactitude des actions et libellés.
3. Cohérence entre spécifications, tests et observations.
4. Pertinence et exactitude des captures.
5. Orthographe, clarté et terminologie.
6. Mise en page, pagination et charte graphique.
7. Contrôle final du fichier rendu.
Un document visuellement réussi n'est pas validé tant que les contrôles fonctionnels ne sont pas terminés.
3.2 Registre de preuves et d'écarts
Pendant la génération, tenir un registre interne pour chaque affirmation fonctionnelle importante. Pour chaque point, noter la source, le passage/scénario concerné et le niveau de vérification.

Utiliser ces statuts :
- Confirmé par spécification et observation : règle documentée et comportement visible cohérent.
- Documenté, non observé : la spécification décrit le comportement, mais l'environnement n'a pas permis de le vérifier.
- Observé, règle métier à confirmer : l'interface montre le comportement, mais les sources fonctionnelles ne suffisent pas à valider sa signification.
- Partiellement vérifié : seules certaines étapes ou conditions ont été observées.
- Contradictoire : les sources ne concordent pas.
- Non vérifié : aucune preuve suffisante.
Le registre doit être livré séparément du manuel utilisateur, par exemple dans un fichier Markdown nommé points_a_confirmer_<module>.md, lorsque des écarts ou limites existent. Ne pas inclure les détails techniques internes dans le manuel final sauf s'ils sont nécessaires à l'utilisateur.
3.3 Règles obligatoires pour les captures
Chaque capture utilisée doit être associée à une procédure et à une étape précise. Maintenir une correspondance entre :
- le nom de la fonctionnalité ;
- l'action (consultation, ajout, recherche, modification, suppression, connexion, etc.) ;
- l'état affiché ;
- le texte de la légende ;
- l'étape du manuel qu'elle illustre.
Ne jamais utiliser une capture de modification pour illustrer l'ajout sans l'indiquer explicitement. Si un comportement identique est montré dans un autre contexte, préciser ce contexte dans le texte ou prendre une capture adaptée.

Avant insertion :
- vérifier que l'écran est lisible à la taille finale dans le document ;
- recadrer sans enlever les informations nécessaires à la compréhension ;
- éviter les captures redondantes ;
- vérifier que la capture n'affiche pas de mot de passe, jeton, données personnelles non autorisées ou informations de production ;
- vérifier que la légende décrit réellement l'image.
Si la capture ne permet pas de lire les contrôles, refaire la capture plutôt que d'ajouter une explication fondée sur une image illisible.
4. Manuel utilisateur Word
4.1 Objectif et lecteur cible
4.1.1 Parcours d'accès obligatoire
Si l'application nécessite une authentification, inclure une section « Authentification » avant les menus fonctionnels, même lorsque les tests automatisés réutilisent une session persistée. Décrire le parcours depuis la page de connexion jusqu'à l'arrivée sur l'application, avec des captures réelles. Les détails de stockage de session et d'authentification automatisée sont exclus du manuel.

Si la connexion n'est pas requise dans le périmètre considéré, cette exception doit être justifiée par le fonctionnement réel de l'application ou par le périmètre explicitement demandé.
4.1.2 Structure minimale d'une procédure
Chaque procédure doit permettre à un utilisateur qui ne connaît pas l'application de réaliser l'action sans accompagnement oral. Selon la fonctionnalité, inclure :
1. Objectif de l'action.
2. Point de départ et chemin d'accès.
3. Conditions préalables.
4. Étapes numérotées, une action claire par étape.
5. Capture d'écran à proximité de l'étape pertinente.
6. Résultat attendu et/ou résultat observé, avec un vocabulaire qui distingue clairement les deux.
7. Cas particuliers et erreurs connus, uniquement s'ils sont étayés.
Ne pas ajouter artificiellement toutes les sous-sections si elles n'apportent rien à une procédure simple. En revanche, ne pas supprimer une étape nécessaire pour rendre le parcours complet.

Le manuel s’adresse à une personne qui doit utiliser l’application, pas à un développeur qui doit comprendre son code. Il doit permettre à l’utilisateur de réaliser une tâche sans accompagnement oral, en suivant les instructions et les captures d’écran.
4.2 Ton et style d’écriture
Adopter le ton pédagogique, neutre et procédural des manuels témoins :
- privilégier des phrases courtes ou moyennes ;
- expliquer une action à la fois ;
- utiliser une formulation directe, par exemple : « Cliquez sur le menu “Utilisateurs”. La liste des utilisateurs s’affiche. » ;
- utiliser « vous » ou « l’utilisateur » de manière cohérente dans tout le document ; privilégier une seule convention par document ;
- nommer précisément le contrôle à utiliser : menu, onglet, champ, liste déroulante, bouton, icône, case à cocher ;
- expliquer le résultat observable après l’action, si celui-ci est confirmé ;
- éviter le langage promotionnel, les appréciations subjectives et les longues explications techniques.
Ne pas reproduire les fautes, incohérences de temps, répétitions ou formulations maladroites des documents témoins. En conserver la simplicité et le caractère pratique, tout en corrigeant l’orthographe, la grammaire et la ponctuation.
4.3 Structure recommandée
Adapter le plan au périmètre réel de l’application et au modèle Word fourni. En général :
1. Couverture : titre « MANUEL D’UTILISATION », nom du projet/application, logos officiels, date, version et rédacteur si ces informations sont connues.
2. Sommaire : généré à partir des styles de titres Word ; numéros de page actualisables.
3. Préambule : objectif du document, public visé, mode d’accès à l’application et prérequis confirmés.
4. Fonctionnalités : présentation courte des modules principaux, sans décrire encore chaque procédure.
5. Chapitres fonctionnels : un chapitre par menu ou module principal.
6. Sous-sections procédurales : une sous-section par tâche utilisateur (consulter, rechercher, créer, modifier, supprimer, valider, exporter, etc., uniquement si la fonction existe).
7. Fin du document : dernière section utile, sans texte de remplissage.
Numéroter les chapitres et sous-sections de manière cohérente. La profondeur de la numérotation doit rester raisonnable : éviter de multiplier les niveaux lorsque cela n’aide pas l’utilisateur. Le sommaire doit refléter exactement les titres du corps du document.
4.4 Modèle d’une procédure
Pour chaque procédure, suivre autant que possible ce schéma :
1. Titre orienté action : par exemple « Créer un utilisateur ».
2. Contexte bref : à quoi sert l’action, uniquement si nécessaire.
3. Accès : indiquer le menu ou l’écran à ouvrir.
4. Étapes : actions dans l’ordre, avec les libellés exacts de l’interface.
5. Capture(s) : capture lisible montrant l’écran ou l’étape décrite, placée près du texte correspondant.
6. Résultat attendu côté utilisateur : confirmation, élément créé, liste mise à jour, détail affiché, téléchargement lancé, etc., uniquement si observé ou documenté.
7. Cas particulier ou avertissement : seulement si la documentation ou l’application le confirme.
Exemple de style :
« Dans le menu “Utilisateurs”, cliquez sur “Nouvel utilisateur”. Le formulaire de création s’affiche. Renseignez les champs obligatoires, puis cliquez sur “Créer l’utilisateur”. Une demande de confirmation s’affiche. Confirmez l’action si vous souhaitez poursuivre. »

Cet exemple illustre le style et ne doit pas être présenté comme une fonctionnalité réelle sans confirmation dans les sources du projet.
4.5 Captures d’écran
- Utiliser Playwright MCP pour capturer l’interface réelle de l’application dans l’environnement de test.
- Capturer l’écran pertinent au bon moment du parcours ; éviter les captures génériques qui ne prouvent pas l’étape décrite.
- Préserver la lisibilité : taille suffisante, cadrage utile, absence de menus superflus et de zones vides excessives.
- Ne pas utiliser une capture d’un autre projet pour illustrer l’application courante.
- Ne pas inventer ou reconstituer une interface par génération d’image.
- Si une annotation est nécessaire, utiliser des flèches ou encadrés sobres et cohérents, sans masquer les libellés importants.
- Placer la capture immédiatement après le passage qu’elle illustre et ajouter une légende courte si cela aide à l’identifier.
- Vérifier que les captures ne contiennent pas de secrets, données personnelles non autorisées ou informations sensibles.
- Ne pas affirmer qu’une capture illustre un résultat final si ce résultat n’a pas été réellement observé.
4.6 Mise en page Word et identité visuelle
Le document CEPICI fourni est la référence graphique principale. Avant de générer le manuel :
- inspecter le modèle réel et reprendre ses logos, couleurs, polices, tailles, espacements, en-têtes, pieds de page, pagination, marges et style de couverture ;
- privilégier les styles Word natifs (Titre 1, Titre 2, etc.) afin de maintenir un document cohérent et un sommaire actualisable ;
- reprendre les couleurs à partir du modèle plutôt que de les estimer visuellement ; si nécessaire, lire les valeurs RGB/HEX dans le fichier ;
- conserver le ratio des logos et leur positionnement sans les déformer ;
- utiliser des styles cohérents pour les titres de chapitres, les sous-titres, le corps de texte, les légendes et les avertissements ;
- éviter les changements de couleur décoratifs et les polices non présentes dans le modèle ;
- garder des marges, espacements et sauts de page homogènes ;
- éviter les titres isolés en bas de page, les images coupées, les tableaux débordants et les grands espaces vides injustifiés ;
- ajouter les informations de version et de date seulement lorsqu’elles sont fournies ou validées.
Ne pas déduire une couleur exacte d’une capture d’écran compressée si le modèle Word peut être inspecté directement. Le modèle fourni prime sur toute valeur approximative.
5. Cahier de tests Excel
5.1 Objectif et lecteur cible
Le cahier de tests est un support de préparation et d’exécution de la recette fonctionnelle. Il doit permettre à un testeur de comprendre le but du cas, de préparer l’état initial, de réaliser les actions et de comparer le comportement observé au résultat attendu.

Il ne s’agit pas d’un manuel utilisateur : le style est plus compact, structuré et vérifiable. Éviter les paragraphes explicatifs longs dans les cellules.
5.2 Métadonnées du document
Reprendre les champs présents dans le modèle Excel, par exemple :
- nom du projet ;
- description ou périmètre ;
- lien d’accès à l’application ;
- personne à contacter ;
- auteur des tests ;
- date de rédaction et version ;
- date de début et de fin des tests ;
- données de test ou jeu de données.
Ne pas inventer les noms, dates, contacts, versions ou URL. Laisser les champs non connus vides ou les marquer explicitement « À renseigner », selon la convention du modèle.
5.3 Organisation des tests
- Regrouper les cas par fonctionnalité ou module, dans un ordre logique correspondant à la navigation dans l’application ou au découpage des spécifications.
- Attribuer un identifiant unique et stable à chaque cas : CT0001, CT0002, etc. Ne pas réutiliser un ID pour un scénario différent.
- Décrire un objectif principal par cas de test. Si plusieurs résultats indépendants doivent être validés, scinder le scénario lorsque cela améliore la traçabilité.
- Prévoir des cas positifs, négatifs, limites et contrôles de droits uniquement lorsque les spécifications, les scripts ou l’application fournissent une base pour les définir.
- Inclure les prérequis nécessaires : connexion, rôle/droits, données existantes, état d’un objet ou disponibilité d’une fonctionnalité.
- Garder les cas de test indépendants autant que possible. Si un cas dépend d’un autre, l’indiquer explicitement.
5.4 Rédaction des colonnes
FONCTIONNALITÉS
Nom du module ou de la rubrique, avec une terminologie identique à celle de l’application et des spécifications. Les lignes suivantes peuvent rester dans le même groupe visuel si le modèle utilise des cellules fusionnées.

ID
Identifiant unique et séquentiel, par exemple CT0001. Vérifier l’absence de doublons.

PRÉREQUIS
Décrire l’état nécessaire avant l’exécution. Être précis : « Être connecté avec un compte disposant du droit de création d’utilisateur » plutôt que « Avoir accès » si le droit spécifique est connu. Mentionner les données nécessaires.

DESCRIPTION
Formuler l’objectif du scénario en une phrase courte, par exemple « Accéder au menu Utilisateurs » ou « Créer un nouvel utilisateur ». Éviter de mettre toutes les étapes dans cette colonne.

ACTIONS
Décomposer en étapes numérotées et ordonnées. Chaque étape doit préciser une action concrète et, si utile, le contrôle exact :
1. Cliquer sur le menu « Utilisateurs ».
2. Cliquer sur « Nouvel utilisateur ».
3. Renseigner les champs obligatoires avec des données de test valides.
4. Cliquer sur « Créer l’utilisateur ».
Les libellés doivent être vérifiés dans l’interface. Éviter les icônes décrites de façon ambiguë : nommer leur fonction si elle est connue, sinon indiquer qu’elle doit être identifiée.

RÉSULTATS ATTENDUS
Décrire des résultats observables et vérifiables, liés aux étapes. Exemples de formulation : « L’application affiche la liste des utilisateurs » ; « Une boîte de confirmation s’affiche » ; « Le compte est ajouté à la liste ». Ne pas écrire seulement « Ça fonctionne » ou « L’action est réussie ». Pour un scénario comportant plusieurs étapes déterminantes, détailler le résultat associé à chaque étape si le modèle le permet.

STATUT ATTENDU
Utiliser les valeurs prévues par le modèle. Dans les cahiers témoins, OK sert de valeur attendue pour les cas fonctionnels. Ne pas ajouter d’autres valeurs sans vérifier la convention du projet.

RÉSULTAT
Champ destiné au constat de l’exécution réelle. Le laisser vide avant l’exécution, sauf si le modèle prévoit explicitement une autre convention.

STATUT
Renseigner uniquement après exécution, selon les valeurs admises par le modèle, par exemple OK ou NOK. Ne pas préremplir les statuts réels à partir d’une hypothèse.

COMMENTAIRE
Noter une anomalie, une précision utile, un blocage, une question ou une référence de ticket. Laisser vide lorsqu’il n’y a rien à signaler.
5.5 Qualité des scénarios
Chaque cas de test doit répondre aux questions suivantes :
- Le prérequis permet-il de préparer l’état initial ?
- Les actions sont-elles exécutables sans interprétation personnelle ?
- Le résultat attendu est-il observable et suffisamment précis ?
- Le scénario correspond-il à une spécification, une règle métier ou un comportement confirmé ?
- Les données de test sont-elles disponibles et non sensibles ?
- Le cas est-il distinct des autres cas ou son doublon est-il justifié ?
Éviter les résultats attendus trop génériques. Si le scénario porte sur une recherche, préciser que les résultats correspondent aux critères saisis lorsque cette règle est confirmée. Si le scénario porte sur une création, préciser le retour observable attendu (formulaire fermé, message, nouvelle ligne, détail, etc.) uniquement si ce comportement est documenté ou observé.
5.6 Mise en forme Excel
- Utiliser le cahier Excel témoin comme base et préserver sa structure, ses cellules fusionnées, sa hiérarchie visuelle, ses couleurs, ses bordures, ses alignements, ses hauteurs de ligne et ses largeurs de colonnes.
- Ne pas transformer automatiquement le classeur en tableau plat si le modèle utilise une mise en page structurée.
- Reprendre les styles d’en-têtes et de sections du modèle ; ne pas choisir de nouvelles couleurs arbitrairement.
- Activer le retour à la ligne pour les cellules longues et ajuster les hauteurs de ligne afin que les actions et résultats restent lisibles.
- Maintenir les identifiants et statuts visibles et cohérents.
- Préserver les formules, validations de données, liens et autres éléments présents dans le modèle, après les avoir inspectés.
- Vérifier qu’aucun contenu n’est tronqué, masqué, décalé ou placé hors de la zone utile.
- Ne pas utiliser de couleurs comme seul moyen de transmettre un statut si le libellé textuel peut aussi être affiché.
- Ne pas ajouter des colonnes sans nécessité fonctionnelle ; si le modèle doit être adapté, expliquer le changement.
6. Utilisation de Playwright MCP et des scripts automatisés
1. Lire les spécifications Markdown pertinentes et identifier les modules, règles métier, prérequis et résultats attendus.
2. Lire les scripts automatisés concernés afin de réutiliser les parcours et assertions déjà établis.
3. Utiliser Playwright MCP pour observer les parcours réellement accessibles dans l’environnement de test.
4. Comparer les libellés et comportements observés aux spécifications et aux scripts.
5. Capturer les écrans utiles pour le manuel utilisateur ; conserver les captures dans un répertoire identifié par projet et fonctionnalité.
6. Préparer les scénarios de tests à partir des exigences et des scripts, sans considérer qu’un script existant prouve automatiquement que toutes les exigences sont couvertes.
7. Générer les documents à partir des modèles Word et Excel existants.
8. Contrôler les documents générés et signaler les incertitudes.
Ne pas exécuter d’action destructive (suppression, désactivation, envoi réel, paiement, publication, modification de données critiques) sans environnement et données de test autorisés. Si l’action est nécessaire au scénario, vérifier les consignes du projet et utiliser des données dédiées.
7. Traçabilité et traitement des incertitudes
- Relier chaque procédure du manuel à une fonctionnalité documentée et observée.
- Relier chaque cas de test à une spécification, une exigence, un scénario automatisé ou un comportement confirmé.
- Si une référence stable existe (nom du fichier Markdown, section, identifiant de test), la conserver dans les sources de travail ou dans le document lorsque le modèle le prévoit.
- Si les sources se contredisent, ne pas les harmoniser silencieusement. Produire une liste de points à confirmer.
- Distinguer clairement : documenté, observé dans l’application, déduit et à confirmer. Éviter de présenter une déduction comme un fait.
- Ne pas affirmer qu’une fonctionnalité est absente simplement parce qu’elle n’a pas été trouvée lors d’une seule navigation.
8. Contrôle qualité avant livraison
8.1 Manuel Word
- Le titre, le projet, la date, la version et le rédacteur sont corrects ou laissés à renseigner.
- Le sommaire correspond aux titres et peut être actualisé.
- Les chapitres suivent une logique de navigation compréhensible.
- Chaque procédure est dans le bon ordre et contient des actions précises.
- Les noms des champs et boutons correspondent à l’interface observée.
- Les captures sont réelles, lisibles, pertinentes et placées près des instructions.
- Les logos, couleurs, polices, marges, en-têtes, pieds de page et pagination suivent le modèle.
- Aucune image n’est coupée, aucun titre n’est isolé et aucune page ne contient de grand espace vide injustifié.
- L’orthographe, la grammaire, la ponctuation et la terminologie sont cohérentes.
- Aucun contenu confidentiel ou donnée réelle non autorisée n’est exposé.
8.2 Cahier Excel
- Les métadonnées du projet sont exactes ou identifiées comme à renseigner.
- Les fonctionnalités sont regroupées de manière logique.
- Les identifiants sont uniques et séquentiels.
- Chaque scénario a un prérequis, une description, des actions et des résultats attendus exploitables.
- Les actions sont numérotées et les résultats sont vérifiables.
- Les statuts réels ne sont pas renseignés sans exécution effective.
- Les cellules longues sont lisibles et aucun texte important n’est tronqué.
- Les couleurs, bordures, cellules fusionnées, dimensions et validations respectent le modèle.
- Les formules, liens et fonctionnalités du classeur sont préservés.
8.3 Vérification technique
- Ouvrir les fichiers générés avec une bibliothèque adaptée et vérifier qu’ils ne sont pas corrompus.
- Pour Word, contrôler les sauts de page, images, styles et sommaire ; si possible, convertir en PDF pour une vérification visuelle finale.
- Pour Excel, vérifier les feuilles, les dimensions, les cellules fusionnées, les formules, les validations, les liens et l’absence de contenu en dehors de la zone attendue.
- Ne pas déclarer la validation visuelle terminée si aucun rendu n’a été inspecté.
8.4 Critères bloquants de validation du manuel utilisateur
Ne pas déclarer le manuel prêt à diffuser si l'un des points suivants est vrai :
- le parcours commence par un menu protégé sans expliquer l'authentification ou référencer explicitement une procédure de connexion existante ;
- une procédure critique est absente ou ne peut pas être exécutée à partir des instructions ;
- des champs, règles métier, messages ou résultats sont inventés ou contredisent les sources ;
- une capture illustre une autre action ou un autre écran que celui décrit sans contextualisation ;
- les fonctionnalités annoncées dans le périmètre ne correspondent pas au contenu réellement documenté ;
- le sommaire, la pagination ou la mise en page empêchent la lecture ;
- des secrets ou données sensibles apparaissent dans le document.
Dans le compte rendu final, distinguer explicitement :
- les fonctionnalités documentées ;
- les parcours effectivement observés ;
- les informations uniquement issues des spécifications ;
- les éléments non vérifiés ;
- les écarts qui nécessitent une décision humaine ;
- les contrôles de rendu réellement effectués.
Ne jamais dire que le document a été « validé visuellement » si aucun rendu final (Word ou PDF) n'a été inspecté.
9. Livrables attendus
Pour chaque demande, produire uniquement le ou les livrables demandés, accompagnés si nécessaire d’une courte liste de points à confirmer.

Nommage recommandé :
- Manuel_utilisateur_<Projet>_vX.Y.docx
- Cahier_de_tests_<Projet>_vX.Y.xlsx
- captures : captures/<module>/<procedure>_<etape>.png
Adapter le nommage à la convention interne lorsqu’elle est fournie. Ne pas inventer la version ou la date officielle.
10. Instruction finale pour l’agent
Avant de générer un document, suivre obligatoirement le workflow détaillé en section 3.1. Ne jamais sauter directement à la rédaction.
1. Inspecter le modèle correspondant et les sources réellement présentes.
2. Construire une matrice de couverture et un registre de preuves.
3. Pour un manuel, vérifier le parcours d'accès complet, y compris la connexion lorsqu'elle est nécessaire.
4. Observer l'application avec Playwright MCP et prendre des captures réelles lorsque cela est nécessaire et sûr.
5. Rédiger uniquement les éléments étayés ; isoler les incertitudes et contradictions.
6. Générer le document en respectant strictement le modèle.
7. Contrôler le fond avant la forme, puis inspecter le rendu final.
8. Livrer le fichier, le compte rendu de vérification et les points à confirmer.
Principe directeur : un livrable doit être exact, complet dans le périmètre annoncé, traçable à ses sources, compréhensible par son lecteur et conforme au modèle interne. La qualité visuelle ne compense jamais un contenu non vérifié.