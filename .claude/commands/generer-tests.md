---
description: Temps B — génère, exécute et inventorie les tests Playwright à partir des specs confirmées
argument-hint: <projet> [fonctionnalité]
---
Génère les tests Playwright du projet « $ARGUMENTS » en suivant la skill `generation-tests-playwright`.

- Dépôt cible : `projet.json` → `automatisation.depot` (l'initialiser depuis `templates/automatisation/` s'il n'existe pas, après accord du responsable du projet sur l'emplacement).
- Uniquement les specs CONFIRMÉES (ou les scénarios confirmés d'une spec PARTIELLE).
- Exécuter les tests générés, mettre à jour `docs/test-inventory.md` du dépôt, rapporter PASS / FAIL / BLOCKED / NOT_RUN honnêtement.
