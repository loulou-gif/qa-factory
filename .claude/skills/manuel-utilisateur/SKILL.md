---
name: manuel-utilisateur
description: Temps B — rédige le manuel utilisateur Word d'un projet à partir de l'application réellement observée, des cas validés et des captures, selon les règles de docs/regles-livrables.md et le modèle templates/manuel. À utiliser pour /manuel.
---

# Manuel utilisateur (temps B uniquement)

Le manuel décrit ce que l'utilisateur voit réellement : il n'est **jamais** rédigé en temps A, à partir du seul cahier des charges.

Règles complètes : `docs/regles-livrables.md` (ta skill de documentation : workflow phases A à F, registre de preuves, captures, structure, mise en page, critères bloquants). Elles s'appliquent intégralement.

## Préconditions

- Exploration faite pour les fonctionnalités du périmètre (`04-livrables/exploration/decouvertes.md`, captures dans `04-livrables/exploration/captures/`).
- Modèle Word : `templates/manuel/modele_manuel.docx` (référence graphique CEPICI/Synelia).
- Générateur : `templates/manuel/generation/` (repris d'Orange eFacture, rendu générique) : `build_manual.py`, `word_finalize.ps1` et l'exemple de contenu complet `exemple_contenu_olib.py`.

## Déroulé

1. Phase A — périmètre et matrice de couverture (fonctionnalité → cas validés → captures → état de vérification), écrite dans `04-livrables/manuel/points_a_confirmer_manuel.md`.
2. Phases B à D — vérifier chaque procédure dans l'application (MCP Playwright), compléter les captures manquantes, sans action destructive non autorisée.
3. Phase E — écrire `04-livrables/manuel/generation/contenu_manuel.py`, sur le modèle de `exemple_contenu_olib.py` :
   - en tête : `PROJET = '<NOM EN MAJUSCULES>'`, `MODULE = '<sous-titre de couverture>'`, `TITRE = 'Manuel d’utilisation – <Nom>'` (et `LANG = 'en'` pour une version anglaise) ;
   - une fonction `build(d)` qui assemble avec `H_UNNUM`, `H`, `P`, `STEPS`, `BULLETS`, `FIG`, `NOTE`, `LABEL` et retourne `''.join(x)` ;
   - plan : préambule, fonctionnalités, authentification, un chapitre par module, une sous-section par procédure ; `FIG('<nom de capture sans .png>', 'Légende')`.
4. Générer : `python templates/manuel/generation/build_manual.py templates/manuel/modele_manuel.docx projets/<projet>/04-livrables/exploration/captures projets/<projet>/04-livrables/manuel/_brouillon.docx projets/<projet>/04-livrables/manuel/generation/contenu_manuel.py`.
5. Finaliser sous Windows (sommaire, champs, PDF) : `powershell -File templates/manuel/generation/word_finalize.ps1 <brouillon> <final.docx> <final.pdf>` (chemins Windows **absolus** : Word est piloté par COM).
6. Phase F — contrôles du fond puis de la forme ; inspecter le rendu PDF avant de dire qu'il est prêt.

Nommage : `Manuel_utilisateur_<Projet>_vX.Y.docx` dans `04-livrables/manuel/`.

## Règles clés (rappel)

- Authentification décrite avant le premier menu protégé, même si les tests utilisent une session enregistrée.
- Une capture = une étape précise, sans secret ni donnée personnelle.
- Distinguer résultat attendu (spécification) et résultat observé.
- Les écarts et éléments non vérifiés vont dans `points_a_confirmer_manuel.md`, pas dans le manuel.
