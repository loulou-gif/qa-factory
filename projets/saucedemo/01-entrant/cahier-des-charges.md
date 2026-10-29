# Cahier des charges — Boutique en ligne SauceDemo (exemple de démonstration)

Document d'exemple rédigé pour tester la chaîne QA Factory. Il imite un cahier des charges client court, avec volontairement quelques zones floues.

## 1. Contexte

La société Swag Labs vend des articles en ligne. L'application web permet à un client authentifié de consulter le catalogue, de remplir un panier et de passer commande. Environnement de recette : https://www.saucedemo.com

## 2. Authentification

2.1 L'utilisateur se connecte avec un nom d'utilisateur et un mot de passe. Après connexion, il arrive sur la page « Products » qui affiche le catalogue.

2.2 Les deux champs sont obligatoires. Si l'un d'eux est vide, un message d'erreur indique le champ manquant.

2.3 Si le couple identifiant / mot de passe est incorrect, la connexion est refusée avec un message d'erreur.

2.4 Un compte peut être verrouillé par l'administrateur. Un utilisateur verrouillé ne peut pas se connecter et un message lui indique que son compte est bloqué.

2.5 L'utilisateur peut se déconnecter depuis le menu latéral. Après déconnexion, il revient sur la page de connexion et ne peut plus accéder aux pages internes sans se reconnecter.

## 3. Catalogue

3.1 La page « Products » affiche la liste des articles avec, pour chacun : image, nom, description, prix et un bouton « Add to cart ».

3.2 L'utilisateur peut trier la liste par nom (A à Z, Z à A) et par prix (croissant, décroissant). Le tri par défaut est par nom de A à Z.

3.3 Un clic sur le nom d'un article ouvre sa fiche détaillée, avec un bouton de retour vers le catalogue.

## 4. Panier

4.1 Le bouton « Add to cart » ajoute l'article au panier ; il devient alors « Remove ». L'icône du panier affiche le nombre d'articles.

4.2 Le panier liste les articles ajoutés avec leur quantité, leur nom et leur prix. L'utilisateur peut retirer un article depuis le panier.

4.3 Le contenu du panier est conservé pendant la navigation dans l'application.

## 5. Commande

5.1 Depuis le panier, le bouton « Checkout » ouvre le formulaire d'informations : prénom, nom et code postal. Les trois champs sont obligatoires.

5.2 L'étape suivante présente un récapitulatif : articles, moyen de paiement, mode de livraison, total hors taxes, taxes et total. Le total doit être égal à la somme des prix des articles plus les taxes.

5.3 Le bouton « Finish » valide la commande et affiche un message de confirmation. Le panier est alors vidé.

5.4 Une commande ne doit pas pouvoir être passée avec un panier vide.

## 6. Exigences non fonctionnelles

6.1 L'application doit être rapide.

6.2 Les mots de passe ne doivent jamais apparaître en clair à l'écran.
