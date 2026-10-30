---
description: Temps A — publie dans Squash les exigences et cas validés (simulation, accord, puis publication)
argument-hint: <projet>
---
Publie dans Squash TM le projet « $ARGUMENTS » en suivant **strictement** la skill `publication-squash`.

Rappels non négociables :
- uniquement depuis `projets/$ARGUMENTS/03-valide/cas-de-tests.json` ;
- `python outils/controle.py $ARGUMENTS --dossier 03-valide` à 0 erreur avant tout appel ;
- simulation (`apply: false`) d'abord, plan présenté, puis `apply: true` **seulement** après l'accord explicite du responsable du projet ;
- fichier de correspondance : `projets/$ARGUMENTS/04-livrables/squash/correspondance.json`.
