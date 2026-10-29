---
name: cahier-de-tests
description: Génère le cahier de tests Excel d'un projet à partir du JSON validé (modèle Synelia/BNI), avec la feuille de traçabilité et le fichier de points à confirmer. À utiliser pour /livrables ou toute demande de cahier de tests / test book.
---

# Cahier de tests Excel

Le cahier est **généré**, jamais rédigé à la main : son contenu vient de `03-valide/cas-de-tests.json`. Les règles de fond et de forme de `docs/regles-livrables.md` (sections 3, 5 et 8.2) s'appliquent.

## Déroulé

1. Préconditions : `03-valide/cas-de-tests.json` existe et `python outils/controle.py <projet> --dossier 03-valide` donne 0 erreur.
2. Métadonnées : lire `projet.json` → `cahier` (titre, version, auteur, contact, description) et `application.url`. Toute valeur inconnue reste « À renseigner » : ne jamais inventer un nom, une date de recette ou une version.
3. Générer :
   - cahier complet : `python outils/build_cahier.py <projet>` ;
   - cahier de recette client (parcours nominaux seulement), si Julius le demande ou si `cahier.nominaux_uniquement` vaut `true` : `python outils/build_cahier.py <projet> --nominaux`.
4. Vérifier le fichier produit dans `04-livrables/cahier/` : l'ouvrir avec `openpyxl`, contrôler le nombre de cas, l'absence de cellule tronquée évidente, les colonnes RÉSULTAT / STATUT / COMMENTAIRE vides, la feuille « Traçabilité ».
5. Écrire ou mettre à jour `04-livrables/cahier/points_a_confirmer.md` :
   - métadonnées encore « À renseigner » ;
   - cas liés à des questions ouvertes (liste depuis `ambiguites.md`) ;
   - périmètre retenu (complet ou nominaux, nombre de cas retirés).
6. Journal (déjà ajouté par le script) ; compte rendu court à Julius.

## Règles

- Les colonnes RÉSULTAT et STATUT ne sont **jamais** remplies sans exécution réelle observée.
- Les identifiants CT sont ceux du JSON (traçabilité avec Squash et les specs) : ne pas renumérer.
- Le modèle `templates/cahier/modele_cahier.xlsx` n'est pas modifié ; s'il faut un autre modèle client, le placer dans `templates/cahier/` et adapter `outils/build_cahier.py` (cellules d'en-tête) plutôt que de bricoler le fichier généré.
- Version anglaise : pas encore générée automatiquement. Si demandée, traduire dans un fichier `cas-de-tests.en.json` de même structure et mêmes identifiants, puis adapter le script (option à ajouter), comme pour le projet Orange eFacture.
