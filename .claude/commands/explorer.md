---
description: Temps B — explore l'application réelle, consigne découvertes et écarts, confirme les specs
argument-hint: <projet> [fonctionnalité]
---
Explore l'application du projet « $ARGUMENTS » en suivant la skill `exploration-application`, puis complète les specs avec la partie temps B de la skill `specs-automatisation`.

- Périmètre : la fonctionnalité indiquée, sinon toutes les specs BROUILLON ou PARTIELLE, une par une.
- Respecte `projet.json` → `application.actions_autorisees` (lecture seule par défaut) ; en cas de doute sur une action qui écrit des données, demande avant.
- Sorties : `04-livrables/exploration/decouvertes.md`, `ecarts.md`, captures, specs complétées (statut CONFIRMÉE ou PARTIELLE).
- Termine par la liste des écarts à arbitrer par le responsable du projet.
