---
description: Applique une correction demandée par le responsable du projet aux fichiers d'analyse en attente de validation
---
Correction demandée : « $ARGUMENTS » (le premier mot est le projet).

Suis la section « Corrections » de la skill `analyse-cdc` :
1. Travaille uniquement dans `projets/<projet>/02-a-valider/`. Si les fichiers ne sont que dans `03-valide/`, explique qu'il faut d'abord les remettre dans `02-a-valider/` (c'est le responsable du projet qui déplace) et arrête-toi.
2. Applique la demande au JSON (et à `ambiguites.md` / `jeux-de-donnees.md` si besoin), sans renuméroter, en incrémentant `meta.version`.
3. `python outils/rendre_revue.py <projet>` puis `python outils/controle.py <projet>` jusqu'à 0 erreur.
4. Journal, puis compte rendu : ce qui a changé (ids concernés), nouveaux avertissements éventuels.
