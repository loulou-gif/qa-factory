---
description: Temps B — après l'exploration, produit en parallèle les scripts automatisés, le cahier de tests et le manuel
argument-hint: <projet>
---
Produis les livrables du temps B du projet « $ARGUMENTS », en parallèle.

1. Vérifie les préconditions communes :
   - `projet.json` → `application.url`, environnement et `automatisation.depot` renseignés (si le dépôt n'existe pas encore, demande l'emplacement avant de lancer quoi que ce soit) ;
   - exploration faite (`04-livrables/exploration/decouvertes.md`) et specs CONFIRMÉES ou PARTIELLES ;
   - écarts d'exploration (`ecarts.md`) arbitrés par le responsable du projet. S'il reste des écarts sans décision, liste-les et demande s'il faut attendre.
2. Lance **trois sous-agents en parallèle** (outil Agent, un message avec trois appels), chacun avec une consigne complète et autonome :
   - **Automatisation** : suivre `.claude/skills/generation-tests-playwright/SKILL.md` pour toutes les specs confirmées ; rapporter les fichiers créés, les résultats d'exécution réels et l'inventaire mis à jour ;
   - **Cahier de tests** : suivre `.claude/skills/cahier-de-tests/SKILL.md` ; rapporter le fichier produit, le nombre de cas et les points à confirmer ;
   - **Manuel** : suivre `.claude/skills/manuel-utilisateur/SKILL.md` et `docs/regles-livrables.md` ; rapporter le fichier produit, les contrôles faits et les points à confirmer.
   Chaque sous-agent travaille sur ses propres fichiers (dépôt d'automatisation, `04-livrables/cahier/`, `04-livrables/manuel/`) : aucun ne modifie `03-valide/` ni les specs.
3. Quand les trois ont terminé : régénère le cahier une fois de plus si l'inventaire des tests a été mis à jour (la feuille Traçabilité reprend alors les tests automatisés), puis fais un compte rendu unique : livrables produits, résultats des tests (PASS / FAIL / BLOCKED / NOT_RUN), points à confirmer regroupés.
