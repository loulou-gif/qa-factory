---
description: Temps A — analyse le cahier des charges d'un projet et produit cas de tests, ambiguïtés et jeux de données dans 02-a-valider
argument-hint: <projet>
---
Analyse les documents d'entrée du projet « $ARGUMENTS » en suivant **strictement** la skill `analyse-cdc` et le format `docs/FORMAT-CAS-DE-TESTS.md`.

- Entrées : `projets/$ARGUMENTS/01-entrant/` et `projets/$ARGUMENTS/projet.json`.
- Sorties : `projets/$ARGUMENTS/02-a-valider/` → `cas-de-tests.json`, `cas-de-tests.md` (généré), `ambiguites.md`, `jeux-de-donnees.md`, `matrice-tracabilite.md` (généré).
- Si `02-a-valider/cas-de-tests.json` existe déjà, ne l'écrase pas : demande au responsable du projet s'il veut une nouvelle analyse complète ou une correction (`/corriger`).
- Termine par `python outils/controle.py $ARGUMENTS` à 0 erreur, une ligne de journal, et le compte rendu prévu par la skill.
- Ne déplace jamais les fichiers dans `03-valide`.
