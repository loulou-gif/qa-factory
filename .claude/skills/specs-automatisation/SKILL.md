---
name: specs-automatisation
description: Produit et maintient les specs d'automatisation Markdown (format FEATURE/SCENARIO/INTERACT/ASSERT/LOCATOR_RULES des projets ANSUT et Orange eFacture) à partir des cas validés, au statut BROUILLON en temps A puis CONFIRMÉE après exploration. À utiliser pour /specs et /explorer.
---

# Specs d'automatisation

Une spec par fonctionnalité, dans `projets/<projet>/04-livrables/specs/<fonctionnalite>.md`. Elle doit suffire à l'agent (Claude Code ou OpenCode) pour générer un test Playwright de qualité **en allant sur l'application**, en suivant le modèle `templates/automatisation/agents/AGENTS.md`.

Formats de référence : `templates/specs/exemple-spec-ansut-section.md` (syntaxe DATA / SCENARIO / INTERACT / ASSERT / LOCATOR_RULES d'ANSUT) et `templates/specs/exemple-spec-olib-login.md` (en-tête, user story, critères d'acceptation et contraintes métier d'Orange eFacture). Ce sont des exemples de **forme** : leur contenu métier appartient à d'autres projets.

## Temps A — génération du brouillon (/specs)

1. `python outils/generer_specs.py <projet>` : écrit un squelette par fonctionnalité depuis `03-valide` (en-tête, sources, description, critères d'acceptation, DATA depuis les jeux de données, un SCENARIO par cas avec GIVEN / STEP / WHEN / THEN, OBSERVABILITY, LOCATOR_RULES, points à confirmer). Les specs `CONFIRMÉE` ne sont pas écrasées.
2. Compléter à la main, **uniquement à partir des fichiers validés** :
   - `USER STORY` : « En tant que <rôle documenté>, je veux…, afin de… ». Rôle absent du CDC → écrire « <rôle à confirmer> » et l'ajouter aux points à confirmer ;
   - `CONTRAINTES MÉTIER` (nouvelle section après CRITÈRES D'ACCEPTATION) : règles du CDC utiles à l'automatisation (unicité, données partagées, actions destructives, données à ne pas modifier) ;
   - `particular` dans LOCATOR_RULES : ce que le CDC ou les maquettes laissent prévoir (listes déroulantes, popups de confirmation), formulé comme « à vérifier ».
3. Ne rien écrire dans les commentaires `INTERACT` / `ASSERT` : ils restent à compléter.
4. Le statut reste `BROUILLON`.

## Temps B — confirmation (/explorer)

Pour chaque scénario, après observation réelle via le MCP Playwright (skill `exploration-application`) :

1. Remplacer chaque commentaire `<!-- INTERACT … -->` par les instructions réelles, dans la syntaxe des projets existants :
   ```
   NAVIGATE menu="Paramètres > Section"
   INTERACT click button="Ajouter une section"
   INTERACT fill field="Désignation"
     value="{{data.section.label}}"
   INTERACT select field="Maintenancier"
     value="RAKALL"
   ```
2. Remplacer chaque `<!-- ASSERT … -->` par des assertions observables :
   ```
   ASSERT notification visible=true
     text="La section a été créé avec succès"
   ASSERT element="ligne de la section créée"
     visible=true
   ```
3. Ajouter sous le scénario les **locators validés** (tableau « Élément | Locator | Type | Vérifié ») et les écarts observés (`<!-- écart : CDC « Enregistrer », réel « Valider » -->`).
4. Si l'application contredit la spec : ne pas « corriger » le cas validé en silence. Consigner l'écart dans `04-livrables/exploration/ecarts.md` (voir skill `exploration-application`) ; la décision revient au responsable du projet.
5. Passer `STATUT` à `CONFIRMÉE — exploré le <date> sur <environnement>` quand **tous** les scénarios ont leurs INTERACT et ASSERT, ou `PARTIELLE` en listant les scénarios restants.

## Règles

- Jamais de locator inventé ou recopié d'une autre application.
- Jamais de secret : `{{APP_USERNAME}}`, `{{APP_PASSWORD}}`, `{{BASE_URL}}`.
- L'identifiant du scénario (`CT0001`) est conservé : il relie la spec au cas Squash, au cahier et au test Playwright (titre du test : `[CT0001] <titre>`).
- Une spec par fonctionnalité ; ne pas fusionner ni scinder sans demande.
