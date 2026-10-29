# Ambiguïtés et questions — SauceDemo

Questions issues de l'analyse de `01-entrant/cahier-des-charges.md`. Les réponses sont à renseigner par Julius ou le client ; tant qu'une question bloquante est ouverte, les cas liés restent à confirmer.

### Q-001 — Libellés de l'écran de connexion et textes des messages d'erreur
- **Type** : manque
- **Gravité** : importante
- **Source** : CDC §2.1, §2.2, §2.3, §2.4, §5.1
- **Constat** : le CDC parle d'« un message d'erreur » sans en donner le texte, et ne nomme ni les champs ni le bouton de l'écran de connexion.
- **Question** : quels sont les libellés exacts des champs et du bouton de connexion, et le texte de chaque message d'erreur (champ manquant, identifiants incorrects, compte bloqué, champ manquant du formulaire de commande) ?
- **Impact** : EX-002, EX-003, EX-004, EX-012, CT0002, CT0003, CT0004, CT0005, CT0006, CT0007, CT0022, CT0023, CT0024
- **Proposition** : relever les libellés et textes réels lors de l'exploration (temps B) et compléter les specs ; les cas restent rédigés sur le sens du message.
- **Réponse** :
- **Statut** : ouverte

### Q-002 — Compte verrouillé disponible pour les tests
- **Type** : risque
- **Gravité** : bloquante
- **Source** : CDC §2.4
- **Constat** : le verrouillage est fait par l'administrateur, mais le CDC ne fournit ni compte verrouillé de test ni accès administrateur.
- **Question** : un compte verrouillé dédié aux tests peut-il être fourni (identifiant et mot de passe, par variables d'environnement) ?
- **Impact** : EX-004, CT0007
- **Proposition** : demander au client un compte verrouillé permanent réservé à la recette.
- **Réponse** :
- **Statut** : ouverte

### Q-003 — Règle de calcul des taxes
- **Type** : manque
- **Gravité** : importante
- **Source** : CDC §5.2
- **Constat** : le CDC impose « total = somme des prix + taxes » sans donner le taux ni le mode de calcul des taxes.
- **Question** : quel est le taux de taxe applicable et comment est-il arrondi ?
- **Impact** : EX-013, CT0025
- **Proposition** : vérifier pour l'instant la cohérence total = total hors taxes + taxes affichées ; ajouter un contrôle du montant des taxes une fois le taux connu.
- **Réponse** :
- **Statut** : ouverte

### Q-004 — Seuil de performance attendu
- **Type** : ambiguïté
- **Gravité** : importante
- **Source** : CDC §6.1
- **Constat** : « l'application doit être rapide » n'est pas mesurable.
- **Question** : quels temps de réponse maximaux sont attendus, pour quelles pages et sous quelle charge ?
- **Impact** : EX-016
- **Proposition** : aucun cas de test fonctionnel tant que le seuil n'est pas défini ; prévoir une campagne de performance (Gatling) dédiée.
- **Réponse** :
- **Statut** : ouverte

### Q-005 — Comportement attendu avec un panier vide
- **Type** : ambiguïté
- **Gravité** : bloquante
- **Source** : CDC §5.4
- **Constat** : le CDC interdit la commande avec un panier vide sans dire comment : bouton « Checkout » absent, désactivé, ou message d'erreur.
- **Question** : quel est le comportement attendu quand l'utilisateur tente de commander avec un panier vide ?
- **Impact** : EX-015, CT0027
- **Proposition** : le bouton « Checkout » est inactif ou un message empêche de continuer ; le cas vérifie seulement que le récapitulatif n'est pas accessible.
- **Réponse** :
- **Statut** : ouverte

### Q-006 — Portée de la conservation du panier
- **Type** : ambiguïté
- **Gravité** : mineure
- **Source** : CDC §4.3
- **Constat** : « conservé pendant la navigation » ne précise pas si le panier survit à une déconnexion ou à la fermeture du navigateur.
- **Question** : le panier doit-il être conservé après une déconnexion puis une reconnexion ?
- **Impact** : EX-011, CT0020
- **Proposition** : tester d'abord la navigation dans une même session ; ajouter un cas après reconnexion si la règle est confirmée.
- **Réponse** :
- **Statut** : ouverte

### Q-007 — Paiement et livraison lors de la commande
- **Type** : risque
- **Gravité** : importante
- **Source** : CDC §5.2, §5.3
- **Constat** : le récapitulatif affiche un moyen de paiement et un mode de livraison, sans dire lesquels ni si « Finish » déclenche un paiement ou une expédition réels.
- **Question** : la validation d'une commande en recette déclenche-t-elle un paiement ou une livraison réels ? Quelles valeurs de paiement et de livraison doivent s'afficher ?
- **Impact** : EX-013, EX-014, CT0021
- **Proposition** : n'exécuter CT0021 qu'après confirmation écrite qu'aucun paiement réel n'est déclenché ; vérifier la présence des informations sans imposer leurs valeurs.
- **Réponse** :
- **Statut** : ouverte

### Q-008 — Format du code postal
- **Type** : manque
- **Gravité** : mineure
- **Source** : CDC §5.1
- **Constat** : aucun format ni longueur n'est donné pour le code postal ; les valeurs limites ne peuvent pas être conçues.
- **Question** : le code postal a-t-il un format imposé (chiffres uniquement, longueur) ?
- **Impact** : EX-012, CT0024
- **Proposition** : ne tester que l'obligation du champ ; ajouter des cas limites si un format est défini.
- **Réponse** :
- **Statut** : ouverte

### Q-009 — Modification de la quantité dans le panier
- **Type** : hors périmètre
- **Gravité** : mineure
- **Source** : CDC §4.2
- **Constat** : le panier affiche une quantité, mais le CDC ne décrit ni augmentation ni diminution de quantité.
- **Question** : l'utilisateur peut-il modifier la quantité d'un article dans le panier, ou seulement le retirer ?
- **Impact** : EX-010, CT0019
- **Proposition** : considérer que seul le retrait est possible, conformément au CDC.
- **Réponse** :
- **Statut** : ouverte
