---
description: Temps B — après l'exploration, produit en parallèle les scripts automatisés, le cahier de tests et le manuel
---
Produis les livrables du temps B du projet « $ARGUMENTS ».

1. Vérifie les préconditions communes :
   - `projet.json` → `application.url`, environnement et `automatisation.depot` renseignés (si le dépôt n'existe pas encore, demande l'emplacement avant de lancer quoi que ce soit) ;
   - exploration faite (`04-livrables/exploration/decouvertes.md`) et specs CONFIRMÉES ou PARTIELLES ;
   - écarts d'exploration (`ecarts.md`) arbitrés par le responsable du projet. S'il reste des écarts sans décision, liste-les et demande s'il faut attendre.
2. Délègue aux trois sous-agents du projet avec l'outil **task**, en lançant les trois appels dans le même message pour qu'ils travaillent en parallèle (si ta version d'OpenCode les exécute l'un après l'autre, le résultat reste le même, seulement plus long). Donne à chacun le nom du projet et le chemin du dépôt d'automatisation :
   - `qa-automatisation` : scripts Playwright à partir des specs confirmées, exécution, inventaire ;
   - `qa-cahier` : cahier de tests Excel et points à confirmer ;
   - `qa-manuel` : manuel utilisateur Word et points à confirmer.
   Aucun d'eux ne modifie `03-valide/` ni les specs.
3. Quand les trois ont rendu leur compte rendu : relance `python outils/build_cahier.py <projet>` si l'inventaire des tests a été mis à jour (la feuille Traçabilité reprend alors les tests automatisés), puis fais un compte rendu unique : livrables produits, résultats des tests (PASS / FAIL / BLOCKED / NOT_RUN), points à confirmer regroupés.
