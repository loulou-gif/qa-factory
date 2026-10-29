---
description: Temps B — génère le cahier de tests Excel (lien de la plateforme et exploration requis)
argument-hint: <projet> [nominaux]
---
Génère le cahier de tests du projet « $ARGUMENTS » en suivant la skill `cahier-de-tests`.

Préconditions bloquantes (sinon, s'arrêter et dire ce qui manque) :
- `projet.json` → `application.url` renseignée et comptes de test disponibles ;
- exploration faite (`04-livrables/exploration/decouvertes.md`) ;
- écarts d'exploration arbitrés par Julius et, s'il en a accepté, JSON corrigé et revalidé dans `03-valide/`.
