---
description: Crée un nouveau projet QA (dossiers 01 à 04 et projet.json)
argument-hint: <nom> [url] [id-squash]
---
Crée le projet QA « $ARGUMENTS ».

1. Déduis du texte : le nom court (minuscules, chiffres, tirets), l'URL de l'application et l'ID du projet Squash s'ils sont donnés. S'il manque le nom, demande-le.
2. Lance `python outils/nouveau_projet.py <nom> [--url URL] [--squash-id ID] [--libelle "Nom lisible"]`.
3. Si un ID Squash est donné, vérifie avec l'outil MCP `get_project` qu'il existe, et reporte son nom exact dans `projet.json` → `squash.projet_nom`.
4. Liste au responsable du projet les champs de `projet.json` restant « À renseigner » et rappelle la suite : déposer les documents dans `projets/<nom>/01-entrant/`, puis `/analyser <nom>`.
