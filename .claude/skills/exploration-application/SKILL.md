---
name: exploration-application
description: Temps B — explore l'application réelle avec le MCP Playwright pour confirmer libellés, enchaînements, messages et locators, consigner les découvertes et les écarts avec les cas validés, et compléter les specs. À utiliser pour /explorer.
---

# Exploration de l'application (temps B)

Modèle suivi : `templates/exemples/exemple-decouvertes-olib.md` (découvertes du front office Orange eFacture), dans l'esprit des rapports `browser-validation` d'ANSUT.

## Préconditions

- `projet.json` → `application.url` et `application.environnement` renseignés.
- Identifiants dans les variables d'environnement nommées dans `application.variables_identifiants` (jamais dans un fichier versionné).
- `projet.json` → `application.actions_autorisees` : relire ce qui est permis. Par défaut : **lecture seule**. Ne jamais créer, modifier, supprimer, payer ou envoyer sans autorisation écrite dans ce champ ou donnée par Julius dans la conversation.
- Specs BROUILLON présentes dans `04-livrables/specs/`.

## Déroulé, par fonctionnalité

1. Lire la spec, les cas du JSON validé et les questions liées.
2. Avec le MCP Playwright : ouvrir l'URL, se connecter (saisir les identifiants depuis les variables, ne jamais les afficher), naviguer jusqu'à la fonctionnalité.
3. Pour chaque scénario : relever routes, titres, champs (libellé, id, `name`, rôle), boutons, messages, popups, listes, états vides ; tester les validations sans envoyer de données quand c'est possible.
4. Locators : appliquer la priorité de LOCATOR_RULES ; vérifier l'unicité de chaque locator dans le DOM.
5. Captures utiles : `04-livrables/exploration/captures/<fonctionnalite>_<NN>_<etat>.png` (sans données sensibles). Elles serviront au manuel.
6. Compléter la spec (skill `specs-automatisation`, temps B).

## Fichiers à écrire

`04-livrables/exploration/decouvertes.md` — une section par fonctionnalité :
- environnement, date, compte utilisé (identifiant seulement), méthode ;
- légende : **[Observé]** constaté, **[Bundle]** lu dans le code livré non exécuté, **[À confirmer]** hypothèse ;
- routes, écrans, champs, messages, comportements ;
- ce qui n'a pas pu être exploré et pourquoi (compte manquant, action non autorisée).

`04-livrables/exploration/ecarts.md` — tableau :

| Cas | Élément | Cas validé / CDC | Application observée | Nature | Décision |
|---|---|---|---|---|---|
| CT0003 | Bouton de validation | « Enregistrer » | « Valider » | libellé | à décider par Julius |

Nature : `libellé`, `enchaînement`, `message`, `règle`, `donnée`, `anomalie probable`. Une différence de règle (ex. une seule confirmation au lieu de deux) est une **anomalie probable** ou une évolution non documentée : ne pas trancher.

## Après l'exploration

- Proposer à Julius les corrections du JSON validé qui découlent des écarts **qu'il accepte** (libellés notamment). Elles passent par `02-a-valider` → validation → `03-valide`, comme une analyse. Squash n'est pas mis à jour automatiquement pour un cas déjà publié : lister les cas à corriger dans Squash.
- Journal : `| date | explorer <fonctionnalité> | N scénarios confirmés, N écarts | fichiers |`.
