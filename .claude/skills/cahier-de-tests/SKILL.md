---
name: cahier-de-tests
description: Temps B — génère le cahier de tests Excel d'un projet (modèle Synelia/BNI) une fois le lien de la plateforme disponible et l'exploration faite, en parallèle de l'écriture des scripts automatisés, avec la feuille de traçabilité et les points à confirmer. À utiliser pour /cahier, /recette ou toute demande de cahier de tests / test book.
---

# Cahier de tests Excel (temps B)

Le cahier est produit **uniquement quand la plateforme à tester est accessible** (lien, environnement, comptes de test) et **après l'exploration**. Il est fait en parallèle de l'écriture des scripts automatisés. Raison : un cahier remis au client doit porter les libellés, enchaînements et messages réels, pas ceux supposés à partir du cahier des charges.

Le cahier reste **généré**, jamais rédigé à la main : son contenu vient de `03-valide/cas-de-tests.json`. Les règles de `docs/regles-livrables.md` (sections 3, 5 et 8.2) s'appliquent.

## Préconditions (bloquantes)

1. `projet.json` → `application.url` renseignée ; comptes de test disponibles.
2. Exploration faite : `04-livrables/exploration/decouvertes.md` existe (le script le vérifie et refuse sinon).
3. Écarts d'exploration (`04-livrables/exploration/ecarts.md`) arbitrés par Julius. Les écarts acceptés (libellés réels notamment) ont été reportés dans le JSON en passant par `02-a-valider` puis revalidés dans `03-valide`. S'il reste des écarts non arbitrés, les lister et demander à Julius s'il veut le cahier maintenant (les cas concernés seront signalés dans les points à confirmer).
4. `python outils/controle.py <projet> --dossier 03-valide` : 0 erreur.

## Déroulé

1. Métadonnées : `projet.json` → `cahier` (titre, version, auteur, contact, description) et `application.url`. Toute valeur inconnue reste « À renseigner ».
2. Générer :
   - cahier complet : `python outils/build_cahier.py <projet>` ;
   - cahier de recette client (parcours nominaux), si demandé ou si `cahier.nominaux_uniquement` vaut `true` : `python outils/build_cahier.py <projet> --nominaux`.
3. Traçabilité vers les tests automatisés : si l'inventaire du dépôt d'automatisation existe (`docs/test-inventory.md`), et que Julius a fait reporter les liens dans le JSON (`"automatisation": {"test": …}`), la feuille « Traçabilité » les reprend. Pendant une `/recette`, régénérer le cahier à la fin, une fois les tests écrits.
4. Vérifier le fichier produit dans `04-livrables/cahier/` : nombre de cas, colonnes RÉSULTAT / STATUT / COMMENTAIRE vides, feuille « Traçabilité », pas de texte manifestement tronqué.
5. Écrire ou mettre à jour `04-livrables/cahier/points_a_confirmer.md` (modèle : `templates/exemples/exemple-points-a-confirmer-cahier-olib.md`) : métadonnées « À renseigner », cas liés à des questions ouvertes ou à des écarts non arbitrés, périmètre retenu.

## Règles

- RÉSULTAT et STATUT ne sont **jamais** remplis sans exécution réelle observée.
- Les identifiants CT sont ceux du JSON (traçabilité avec Squash, les specs et les tests) : ne pas renuméroter.
- Ne pas corriger un libellé directement dans l'Excel : la correction passe par le JSON.
- Modèle client différent : le placer dans `templates/cahier/` et adapter les cellules d'en-tête dans `outils/build_cahier.py`.
- Version anglaise : non automatisée pour l'instant (traduction dans un `cas-de-tests.en.json` de mêmes identifiants, puis option à ajouter au script).
