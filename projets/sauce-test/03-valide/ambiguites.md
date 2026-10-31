# Ambiguïtés et questions — sauce-test

Questions issues de l'analyse de `01-entrant/Cahier_des_charges_SauceDemo.pdf` (version 1.0 du 30 octobre 2026). Les réponses sont à renseigner par le responsable du projet ou le client ; tant qu'une question bloquante est ouverte, les cas liés restent à confirmer.

### Q-001 — Libellés de l'interface et textes des messages
- **Type** : manque
- **Gravité** : importante
- **Source** : CDC §5.1 EF-AUTH-01 à 04, §5.4 EF-CMD-03 et EF-CMD-06, §4
- **Constat** : le CDC parle d'« un message de validation », d'« un message d'erreur compréhensible », d'« un message explicite » et d'« un message confirmant la fin du parcours » sans en donner le texte. Il ne nomme ni les champs, ni les boutons, ni les options du menu.
- **Question** : quels sont les libellés exacts des champs, boutons et options de menu, et le texte de chaque message (champs de connexion vides, identifiants incorrects, profil verrouillé, champ de commande manquant, succès de commande) ? Un message distinct est-il attendu pour chaque champ vide ?
- **Impact** : EX-001, EX-003, EX-004, EX-005, EX-019, EX-023, CT0001, CT0003, CT0004, CT0005, CT0006, CT0007, CT0008, CT0024, CT0025, CT0026, CT0027, CT0028
- **Proposition** : relever les libellés et textes réels pendant l'exploration (temps B) et les reporter dans les specs ; les cas restent rédigés sur le sens du message.
- **Réponse** :
- **Statut** : ouverte

### Q-002 — Mot de passe commun des profils de démonstration
- **Type** : risque
- **Gravité** : importante
- **Source** : CDC §10 (note sous le tableau des profils)
- **Constat** : le CDC indique qu'un mot de passe commun aux profils de test est documenté par l'application, à confirmer sur la page de connexion au moment de la campagne, car il peut évoluer.
- **Question** : le mot de passe affiché sur la page de connexion est-il bien celui à utiliser, et qui le renseigne dans la variable `APP_PASSWORD` du `.env` de chaque testeur ?
- **Impact** : EX-002, EX-005, EX-032, CT0002, CT0008, CT0042
- **Proposition** : relever le mot de passe sur la page de connexion au début de chaque campagne et le placer dans `APP_PASSWORD` (jamais dans le dépôt).
- **Réponse** :
- **Statut** : ouverte

### Q-003 — « État du produit » après ajout au panier
- **Type** : ambiguïté
- **Gravité** : importante
- **Source** : CDC §5.3 EF-CART-02, §5.5 EF-NAV-03
- **Constat** : « l'interface doit refléter l'état du produit » ne dit pas comment : changement du libellé du bouton (ajout devient retrait), marqueur visuel, autre.
- **Question** : comment l'interface montre-t-elle qu'un produit est dans le panier, sur le catalogue et sur la fiche détaillée ?
- **Impact** : EX-012, CT0017, CT0018, CT0021
- **Proposition** : le bouton d'ajout est remplacé par un bouton de retrait ; à confirmer en exploration.
- **Réponse** :
- **Statut** : ouverte

### Q-004 — Mode de comptage de l'indicateur et quantités du panier
- **Type** : ambiguïté
- **Gravité** : importante
- **Source** : CDC §6 RG-03, §5.3 EF-CART-03, §6 note sur les « éventuelles règles de quantité », §7 Fiabilité
- **Constat** : l'indicateur représente « le nombre d'articles ajoutés selon le fonctionnement de l'application ». Le CDC ne dit pas si un même produit peut être ajouté plusieurs fois, si la quantité est modifiable, ni ce qu'affiche l'indicateur quand le panier est vide.
- **Question** : un produit peut-il être ajouté plusieurs fois (quantité supérieure à 1) ? L'indicateur compte-t-il les produits distincts ou la somme des quantités ? Qu'affiche-t-il pour un panier vide (rien, 0) ?
- **Impact** : EX-012, EX-013, EX-033, CT0017, CT0018, CT0019, CT0021, CT0023, CT0037
- **Proposition** : un produit ne peut être ajouté qu'une fois (quantité 1), l'indicateur compte les produits et disparaît quand le panier est vide ; à confirmer en exploration.
- **Réponse** :
- **Statut** : ouverte

### Q-005 — Règle de calcul des taxes et du total
- **Type** : manque
- **Gravité** : importante
- **Source** : CDC §6 RG-07 et note, §11 Risques
- **Constat** : le total doit être « cohérent » avec le sous-total et les taxes ; le taux, l'arrondi et le lien entre sous-total et prix des articles ne sont pas donnés, et le CDC demande de les vérifier sur l'environnement cible.
- **Question** : quel est le taux de taxe et la règle d'arrondi ? Le sous-total est-il la somme des prix des articles ? « Cohérent » signifie-t-il total = sous-total + taxes ?
- **Impact** : EX-021, CT0030
- **Proposition** : vérifier total = sous-total + taxes affichées et sous-total = somme des prix ; ajouter le contrôle du montant des taxes une fois le taux confirmé.
- **Réponse** :
- **Statut** : ouverte

### Q-006 — Règles exactes des tris
- **Type** : manque
- **Gravité** : mineure
- **Source** : CDC §5.2 EF-CAT-03
- **Constat** : les quatre options de tri sont listées, mais ni le tri appliqué par défaut à l'arrivée sur le catalogue, ni le traitement des égalités de prix, ni la sensibilité à la casse du tri par nom.
- **Question** : quel tri est appliqué par défaut ? Comment sont ordonnés deux produits de même prix ?
- **Impact** : EX-009, CT0012, CT0013, CT0014, CT0015
- **Proposition** : vérifier uniquement l'ordre sur le critère choisi ; relever le tri par défaut en exploration.
- **Réponse** :
- **Statut** : ouverte

### Q-007 — Formats et longueurs des informations client
- **Type** : manque
- **Gravité** : bloquante
- **Source** : CDC §5.4 EF-CMD-02, §10 Jeu de données de commande
- **Constat** : le CDC demande des jeux « contenant des caractères inhabituels » pour les tests négatifs mais ne donne aucune règle de format ni de longueur pour le prénom, le nom et le code postal. Le résultat attendu de ces saisies est inconnu.
- **Question** : quels caractères et quelles longueurs sont acceptés pour le prénom, le nom et le code postal ? Une saisie avec caractères spéciaux ou un code postal non numérique doit-il être refusé ?
- **Impact** : EX-018, EX-019, CT0029
- **Proposition** : sans règle documentée, considérer le seul contrôle « champ renseigné » et consigner le comportement observé en exploration comme fait observé, pas comme attendu.
- **Réponse** :
- **Statut** : ouverte

### Q-008 — Accès direct aux étapes de commande sans validation
- **Type** : manque
- **Gravité** : bloquante
- **Source** : CDC §6 RG-08
- **Constat** : « la confirmation n'est possible qu'après validation des étapes précédentes », mais le CDC ne dit pas ce qui se passe si l'utilisateur atteint le récapitulatif ou la confirmation sans avoir validé les informations client (adresse ouverte directement, retour navigateur).
- **Question** : quel est le comportement attendu dans ce cas : redirection vers l'étape des informations client, message, blocage du bouton de confirmation ?
- **Impact** : EX-024, CT0031
- **Proposition** : retour à l'étape des informations client sans confirmation possible.
- **Réponse** :
- **Statut** : ouverte

### Q-009 — Options du menu et commandes de navigation
- **Type** : ambiguïté
- **Gravité** : importante
- **Source** : CDC §5.5 EF-NAV-01 et EF-NAV-04, §5.3 EF-CART-05
- **Constat** : le menu propose « notamment » la déconnexion et la réinitialisation ; la liste complète n'est pas donnée. « Sans incohérence d'état » n'est pas défini, ni les commandes de retour disponibles (retour au catalogue, annulation de la commande).
- **Question** : quelles options le menu doit-il contenir ? Quelles commandes de retour existent dans le panier et la commande, et vers quel écran mènent-elles ?
- **Impact** : EX-025, EX-029, CT0032, CT0036
- **Proposition** : relever les options et commandes réelles en exploration ; « sans incohérence » = l'écran annoncé s'affiche et le panier est inchangé.
- **Réponse** :
- **Statut** : ouverte

### Q-010 — Périmètre exact de la réinitialisation
- **Type** : ambiguïté
- **Gravité** : importante
- **Source** : CDC §5.5 EF-NAV-03, §6 RG-09
- **Constat** : la réinitialisation remet à zéro « les éléments de démonstration concernés, notamment » le panier et les boutons. La liste complète, le tri après réinitialisation et l'écran affiché ensuite ne sont pas précisés.
- **Question** : quels éléments la réinitialisation restaure-t-elle (panier, boutons, tri, commande en cours) et l'utilisateur reste-t-il sur l'écran courant ?
- **Impact** : EX-028, CT0035
- **Proposition** : vérifier le panier et les boutons d'ajout/retrait (seuls cités) ; relever le reste en exploration.
- **Réponse** :
- **Statut** : ouverte

### Q-011 — Comportement en cas d'accès sans session
- **Type** : manque
- **Gravité** : importante
- **Source** : CDC §4 Visiteur non connecté, §6 RG-01
- **Constat** : l'accès au catalogue nécessite une authentification, mais le CDC ne dit pas ce qui se passe si un visiteur ouvre directement l'adresse d'une page interne.
- **Question** : redirection vers l'écran de connexion, message d'erreur, autre ?
- **Impact** : EX-006, CT0009
- **Proposition** : retour à l'écran de connexion avec un message indiquant que l'authentification est nécessaire.
- **Réponse** :
- **Statut** : ouverte

### Q-012 — Portée de la sécurité de session après déconnexion
- **Type** : manque
- **Gravité** : importante
- **Source** : CDC §7 Sécurité de session
- **Constat** : la déconnexion doit empêcher « la poursuite normale » d'une session « via les parcours applicatifs ». Le CDC ne dit pas si le bouton Précédent du navigateur fait partie de ces parcours.
- **Question** : après déconnexion, le retour arrière du navigateur doit-il lui aussi être bloqué, ou seul l'accès par les commandes de l'application est-il concerné ?
- **Impact** : EX-027, CT0034
- **Proposition** : tester les deux voies (retour arrière et adresse directe) et rapporter le retour arrière comme écart à qualifier s'il réaffiche le catalogue.
- **Réponse** :
- **Statut** : ouverte

### Q-013 — Seuil de temps de réponse
- **Type** : ambiguïté
- **Gravité** : importante
- **Source** : CDC §4 Utilisateur à latence, §7 Performance
- **Constat** : « un délai acceptable » n'est pas mesurable ; le profil à latence doit être « évalué séparément » sans critère.
- **Question** : quel temps de réponse maximal est acceptable, pour quels écrans, avec le profil standard et avec le profil à latence ?
- **Impact** : EX-032, CT0042
- **Proposition** : relever les temps sans verdict tant que le seuil n'est pas fixé ; pas de test de charge sur une application publique.
- **Réponse** :
- **Statut** : ouverte

### Q-014 — Navigateurs et tailles d'écran retenus
- **Type** : manque
- **Gravité** : importante
- **Source** : CDC §7 Compatibilité, §10 Configuration à consigner
- **Constat** : les navigateurs et tailles d'écran « retenus pour la campagne de test » ne sont pas listés.
- **Question** : quels navigateurs (et versions) et quelles tailles d'écran (ordinateur, tablette, mobile) faut-il couvrir ?
- **Impact** : EX-031, CT0043
- **Proposition** : Chromium, Firefox et WebKit en résolution ordinateur, plus une taille mobile ; à valider.
- **Réponse** :
- **Statut** : ouverte

### Q-015 — Référentiel d'accessibilité
- **Type** : manque
- **Gravité** : importante
- **Source** : CDC §7 Accessibilité
- **Constat** : trois exigences d'accessibilité sont données (champs identifiables, clavier, messages perceptibles) sans référentiel ni niveau de conformité.
- **Question** : faut-il se référer au RGAA ou aux WCAG, et à quel niveau (A, AA) ? Les trois points du CDC suffisent-ils ?
- **Impact** : EX-034, CT0039, CT0040
- **Proposition** : limiter la campagne aux trois points du CDC, contrôlés avec axe et une vérification manuelle au clavier.
- **Réponse** :
- **Statut** : ouverte

### Q-016 — Critères d'ergonomie
- **Type** : ambiguïté
- **Gravité** : mineure
- **Source** : CDC §7 Ergonomie
- **Constat** : « compréhensibles et cohérents » n'a pas de critère vérifiable (langue attendue, glossaire, charte).
- **Question** : existe-t-il une charte ou un glossaire de référence ? L'interface en anglais est-elle acceptée ?
- **Impact** : EX-030, CT0041
- **Proposition** : vérifier la cohérence d'un écran à l'autre (une même action, un même libellé).
- **Réponse** :
- **Statut** : ouverte

### Q-017 — Critère d'identification stable des éléments
- **Type** : ambiguïté
- **Gravité** : mineure
- **Source** : CDC §7 Maintenabilité des tests
- **Constat** : « identifiés de manière stable » n'est pas défini.
- **Question** : un attribut dédié aux tests (par exemple `data-test`) est-il attendu sur chaque élément interactif ?
- **Impact** : EX-035, CT0044
- **Proposition** : considérer stable un identifiant indépendant de la position et du texte affiché ; relever l'existant en exploration.
- **Réponse** :
- **Statut** : ouverte

### Q-018 — Traitement des profils à comportement dégradé et à latence
- **Type** : risque
- **Gravité** : importante
- **Source** : CDC §4, §10, §11 Hypothèses et Risques
- **Constat** : les profils `problem_user` et `performance_glitch_user` produisent volontairement des résultats différents du parcours nominal ; le CDC ne dit pas comment qualifier ces écarts (anomalie à signaler ou comportement attendu).
- **Question** : les écarts observés avec ces profils doivent-ils être signalés comme anomalies, ou seulement consignés dans une charte exploratoire ?
- **Impact** : CT0042 ; stratégie TT-01 (session exploratoire avec `problem_user`) et TT-03
- **Proposition** : les traiter en session exploratoire (temps B), consigner les écarts sans les compter comme échecs des cas nominaux.
- **Réponse** :
- **Statut** : ouverte
