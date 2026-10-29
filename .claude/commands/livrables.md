---
description: Temps A — génère le cahier de tests Excel et les specs d'automatisation BROUILLON depuis les cas validés
argument-hint: <projet> [nominaux]
---
Génère les livrables du temps A pour « $ARGUMENTS » à partir de `03-valide/` uniquement.

1. `python outils/controle.py <projet> --dossier 03-valide` : 0 erreur, sinon s'arrêter.
2. Cahier de tests : skill `cahier-de-tests` (`python outils/build_cahier.py <projet>`, avec `--nominaux` si demandé), puis `04-livrables/cahier/points_a_confirmer.md`.
3. Specs : skill `specs-automatisation`, partie temps A (`python outils/generer_specs.py <projet>`, puis USER STORY, CONTRAINTES MÉTIER et `particular` complétés depuis les fichiers validés uniquement). Statut BROUILLON.
4. Compte rendu : fichiers produits, nombre de cas, points à confirmer, et rappel que les specs devront être confirmées par `/explorer` quand l'application sera disponible.
