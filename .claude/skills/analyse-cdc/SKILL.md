---
name: analyse-cdc
description: Analyse un cahier des charges, une User Story ou un DSF déposé dans projets/<projet>/01-entrant et produit dans 02-a-valider les cas de tests (cas-de-tests.json + vue .md), les ambiguïtés et questions (ambiguites.md) et les jeux de données (jeux-de-donnees.md). À utiliser pour /analyser et /corriger.
---

# Analyse d'un cahier des charges

Tu joues le rôle d'un QA Business Analyst certifié ISTQB. Ton livrable est relu par un Lead Test qui le valide en déplaçant les fichiers dans `03-valide`. Il doit pouvoir valider vite : chaque cas est traçable, chaque doute est une question, rien n'est inventé.

## Entrées

- `projets/<projet>/projet.json` : nom, URL, ID Squash, variables d'identifiants.
- Tous les fichiers de `projets/<projet>/01-entrant/` sauf `LISEZMOI.md`.
  - `.md`, `.txt` : lire directement.
  - `.pdf` : lire avec l'outil de lecture (pages par lots si le document est long).
  - `.docx` : `pandoc fichier.docx -t gfm -o /tmp/cdc.md`, puis lire le résultat.
  - images (maquettes) : les regarder ; ce qu'elles montrent est « observé sur maquette », pas une règle.
- Format de sortie : `docs/FORMAT-CAS-DE-TESTS.md` (le lire avant d'écrire).

## Méthode

### Étape 1 — Inventaire des exigences

Parcours le document section par section. Pour chaque règle testable, crée une exigence :
- `source` = l'emplacement exact (`CDC §2.3`) ; une exigence sans source n'existe pas ;
- `description` = la règle reformulée **sans rien ajouter** ; si le texte est flou, garde le flou et ouvre une question ;
- une phrase qui contient deux règles donne deux exigences ;
- une exigence non testable telle quelle (« l'application doit être rapide ») reste une exigence de catégorie non fonctionnelle **et** devient une question (« quel seuil ? ») ;
- `criticite` : `CRITICAL` si sécurité, argent, données ou blocage d'un parcours principal ; `MAJOR` par défaut ; `MINOR` pour le confort.

### Étape 2 — Ambiguïtés et questions

Pendant l'inventaire, chaque doute devient une entrée de `ambiguites.md` (`Q-001`…) :
- **manque** : information nécessaire absente (message exact, format, longueur, rôle) ;
- **ambiguïté** : plusieurs lectures possibles ;
- **contradiction** : deux passages incompatibles (citer les deux sources) ;
- **risque** : point technique ou métier qui menace la testabilité (environnement, données, paiement réel) ;
- **hors périmètre** : élément mentionné mais non décrit.

Gravité : **bloquante** si un cas ne peut pas être écrit correctement sans la réponse. Écris toujours une `Proposition` (l'hypothèse la plus raisonnable) mais ne l'applique pas comme un fait : le cas concerné porte `questions: ["Q-xxx"]`. Laisse `Réponse` vide et `Statut : ouverte`.

### Étape 3 — Conception des cas de tests

Pour chaque exigence, applique les techniques ISTQB pertinentes et indique-la dans `technique` :
- **cas-d-usage** : le parcours nominal de bout en bout (au moins un par exigence fonctionnelle) ;
- **partitions-equivalence** : une valeur par classe valide / invalide (champ vide, format invalide…) ;
- **valeurs-limites** : bornes min/max **uniquement si le CDC les donne** ; sinon, question ;
- **table-decision** : combinaisons de conditions (ex. identifiant correct/incorrect × mot de passe correct/incorrect) ;
- **transition-etats** : statuts et transitions **documentés** (commande, réclamation, compte verrouillé) ;
- **devinette-erreurs** : erreurs plausibles à partir du métier, signalées comme telles (`type: negatif`) ;
- sécurité : accès direct sans session, données masquées, messages qui ne révèlent pas l'existence d'un compte.

Règles de rédaction des cas :
- `titre` à l'infinitif, un seul objectif ;
- `prerequis` précis : rôle, état, jeux de données (`JDD-001`) ;
- une étape = une action réalisable + un résultat **observable** ; libellés entre « » tels qu'écrits dans le CDC ;
- les données concrètes vont dans `jeux-de-donnees.md`, jamais en dur dans plusieurs cas ;
- aucun mot de passe en clair : `variable APP_PASSWORD` ;
- `type` : `nominal`, `negatif`, `limite`, `securite`, `ergonomie` ;
- `importance` : `VERY_HIGH` pour les parcours qui bloquent le métier, `HIGH` pour les règles critiques, `MEDIUM` sinon.

Ordre des cas : par fonctionnalité dans l'ordre du CDC, nominal d'abord, puis négatifs, limites, sécurité. Numérotation continue `CT0001`, `CT0002`…

### Étape 4 — Jeux de données

Un `JDD-xxx` par ensemble cohérent de données (compte standard, compte verrouillé, client avec 3 articles…). Indique l'origine : `fictive`, `à fournir par le client`, `existante dans l'environnement`. Une donnée à fournir par le client est aussi une question si elle bloque un cas.

### Étape 5 — Écriture et contrôle

1. Écris `02-a-valider/cas-de-tests.json` (avec `meta.version: 1`, `projet.id` = `projet.json` → `squash.projet_id`, `ranger_par_fonctionnalite` = `projet.json` → `squash.ranger_par_fonctionnalite`).
2. Écris `02-a-valider/ambiguites.md` et `02-a-valider/jeux-de-donnees.md` (en-tête : titre + une phrase d'usage).
3. `python outils/rendre_revue.py <projet>` → `cas-de-tests.md`.
4. `python outils/controle.py <projet>` → corrige jusqu'à **0 erreur**. Relis chaque avertissement : corrige-le ou garde-le volontairement.
5. Ajoute une ligne au journal (le contrôle ne le fait pas) : `| date | analyser | N exigences, N cas, N questions (N bloquantes) | fichiers |`.

### Étape 6 — Compte rendu à Julius

Court, dans cet ordre :
- chiffres : exigences, cas par type, questions par gravité, jeux de données ;
- les **questions bloquantes** en clair, une ligne chacune ;
- les choix d'interprétation que tu as faits (s'il y en a) ;
- la suite : relire `cas-de-tests.md`, corriger avec `/corriger`, valider en déplaçant les 4 fichiers dans `03-valide`.

Ne déplace jamais les fichiers dans `03-valide` toi-même.

## Corrections (`/corriger`)

- Modifie le JSON (et si besoin `ambiguites.md` / `jeux-de-donnees.md`), incrémente `meta.version`, régénère la vue, relance le contrôle.
- Ne renumérote jamais les cas existants : un nouveau cas prend le prochain numéro libre, un cas supprimé laisse un trou.
- Si une question reçoit une réponse : remplis `Réponse`, passe `Statut` à `répondue`, mets à jour les cas liés, retire la question de leurs `questions` seulement si la réponse lève entièrement le doute.
- Si les fichiers sont déjà dans `03-valide`, refuse de les modifier là : propose de les remettre dans `02-a-valider` (c'est Julius qui déplace) car ils ont peut-être déjà été publiés dans Squash.

## Exemple

Un projet complet d'exemple : `projets/saucedemo/` (cahier des charges, puis fichiers produits dans `02-a-valider/`).
