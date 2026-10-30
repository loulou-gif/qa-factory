---
description: Temps A — génère les specs d'automatisation BROUILLON depuis les cas validés
---
Génère les specs d'automatisation du projet « $ARGUMENTS » à partir de `03-valide/` uniquement.

1. `python outils/controle.py $ARGUMENTS --dossier 03-valide` : 0 erreur, sinon s'arrêter.
2. Skill `specs-automatisation`, partie temps A : `python outils/generer_specs.py $ARGUMENTS`, puis USER STORY, CONTRAINTES MÉTIER et `particular` complétés depuis les fichiers validés uniquement. Statut BROUILLON.
3. Compte rendu : specs produites, points à confirmer, et rappel que le cahier de tests, le manuel et les scripts se feront en temps B, quand le lien de la plateforme et les accès de test seront disponibles (`/explorer` puis `/recette`).

Ne génère ni cahier de tests ni manuel ici.
