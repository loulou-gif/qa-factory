# Format des fichiers d'analyse

L'analyse d'un cahier des charges produit trois fichiers, plus une vue de relecture générée :

| Fichier | Rôle | Qui l'écrit |
|---|---|---|
| `cas-de-tests.json` | **Source unique** : exigences et cas de tests | Claude (`/analyser`, `/corriger`) |
| `cas-de-tests.md` | Vue de relecture lisible du JSON | Généré par `outils/rendre_revue.py`, ne pas modifier |
| `ambiguites.md` | Ambiguïtés, contradictions, manques, questions | Claude, puis réponses de Julius ou du client |
| `jeux-de-donnees.md` | Jeux de données nécessaires aux cas | Claude |

Le JSON est un sur-ensemble du format attendu par le MCP Squash (`publish_validated_test_cases`, voir `docs/FORMAT.md` du dépôt `squash-tm-mcp`). Les champs supplémentaires (`type`, `technique`, `questions`, `meta`…) sont ignorés par Squash et servent au cahier, aux specs et au contrôle.

## 1. `cas-de-tests.json`

```json
{
  "meta": {
    "projet": "SauceDemo",
    "sources": ["01-entrant/cahier-des-charges.md"],
    "version": 1,
    "genere_le": "2026-10-29"
  },
  "projet": { "id": 28 },
  "ranger_par_fonctionnalite": true,
  "exigences": [ ... ],
  "cas_de_tests": [ ... ]
}
```

| Champ | Obligatoire | Description |
|---|---|---|
| `meta.projet` | Oui | Nom du projet (celui de `projet.json`) |
| `meta.sources` | Oui | Fichiers de `01-entrant/` analysés |
| `meta.version` | Oui | Incrémentée à chaque correction après relecture |
| `projet.id` | Pour publier | ID du projet Squash (repris de `projet.json`) |
| `ranger_par_fonctionnalite` | Non | Un dossier Squash par fonctionnalité (défaut conseillé : `true`) |

### Exigence

| Champ | Obligatoire | Description |
|---|---|---|
| `id` | Oui | `EX-001`, unique, jamais réutilisé |
| `titre` | Oui | Intitulé court, à l'infinitif ou sous forme de règle |
| `fonctionnalite` | Oui | Nom de la fonctionnalité (sert de dossier Squash, de section du cahier et de fichier de spec) |
| `description` | Oui | Règle reformulée fidèlement, sans ajout |
| `source` | Oui | Emplacement exact dans le CDC : `CDC §3.2.1`, `US-12`, `DSF p. 14` |
| `criticite` | Non | `CRITICAL`, `MAJOR` (défaut), `MINOR`, `UNDEFINED` |
| `categorie` | Non | Code Squash, défaut `CAT_FUNCTIONAL` (`CAT_NON_FUNCTIONAL`, `CAT_SECURITY`, `CAT_PERFORMANCE`, `CAT_USER_STORY`…) |
| `questions` | Non | Ids des questions de `ambiguites.md` qui concernent l'exigence |

### Cas de test

| Champ | Obligatoire | Description |
|---|---|---|
| `id` | Oui | `CT0001`, unique, jamais réutilisé |
| `titre` | Oui | Objectif en une phrase, à l'infinitif : « Créer une section avec des données valides » |
| `fonctionnalite` | Oui | Même valeur que l'exigence couverte |
| `exigences` | Oui | Ids des exigences vérifiées (au moins une) |
| `type` | Oui | `nominal`, `negatif`, `limite`, `securite`, `ergonomie` |
| `technique` | Oui | Technique ISTQB : `cas-d-usage`, `partitions-equivalence`, `valeurs-limites`, `table-decision`, `transition-etats`, `devinette-erreurs`, `exploratoire` |
| `prerequis` | Oui | État initial : rôle, droits, données (avec ids `JDD-xxx`) |
| `description` | Non | Précision sur l'objectif |
| `importance` | Non | `LOW`, `MEDIUM` (défaut), `HIGH`, `VERY_HIGH` |
| `etapes` | Oui | Liste ordonnée de `{ "action", "resultat_attendu" }` ; un résultat observable par étape |
| `jeux_de_donnees` | Non | Ids `JDD-xxx` de `jeux-de-donnees.md` (deviennent les jeux de données Squash) |
| `questions` | Non | Ids `Q-xxx` qui conditionnent ce cas. Un cas lié à une question **bloquante** ouverte est signalé par le contrôle |
| `nature`, `statut` | Non | Codes Squash (`NAT_FUNCTIONAL_TESTING`, `WORK_IN_PROGRESS`…) |

Règles de rédaction :
- une action = un geste réalisable ; un résultat attendu = un fait observable (élément affiché, message, valeur, URL, ligne dans une liste) ;
- libellés de l'interface entre guillemets français « », tels qu'écrits dans le CDC ; s'ils sont inconnus, l'écrire (« le bouton de validation ») et ouvrir une question ;
- pas de « vérifier que tout fonctionne », « traiter correctement », « avec succès » sans fait observable ;
- les données concrètes sont dans `jeux-de-donnees.md`, référencées par leur id.

## 2. `ambiguites.md`

Une section par question, dans cet ordre de champs :

```markdown
### Q-001 — Unicité du code de section
- **Type** : manque | ambiguïté | contradiction | risque | hors périmètre
- **Gravité** : bloquante | importante | mineure
- **Source** : CDC §3.2.1
- **Constat** : le CDC impose un code mais ne dit pas s'il est unique.
- **Question** : le code d'une section doit-il être unique dans l'application ?
- **Impact** : EX-002, CT0004 (cas négatif suspendu à la réponse)
- **Proposition** : considérer le code unique et prévoir un cas négatif.
- **Réponse** :
- **Statut** : ouverte
```

- **bloquante** : un ou plusieurs cas ne peuvent pas être finalisés sans la réponse ;
- `Statut` : `ouverte`, `répondue`, `close` ; la `Réponse` est remplie par Julius ou le client, jamais inventée.

## 3. `jeux-de-donnees.md`

Une section par jeu :

```markdown
### JDD-001 — Compte utilisateur standard
- **Type** : valide | invalide | limite
- **Cas concernés** : CT0001, CT0003
- **Origine** : fictive | à fournir par le client | existante dans l'environnement
- **Sensibilité** : aucune | identifiants (variables d'environnement) | données personnelles (à anonymiser)
- **Prérequis** : le compte existe et est actif.

| Champ | Valeur | Remarque |
|---|---|---|
| Identifiant | `standard_user` | |
| Mot de passe | variable `APP_PASSWORD` | jamais en clair |
```

## 4. Contrôles automatiques (`outils/controle.py`)

Bloquant (erreur) :
- structure ou champ obligatoire manquant, id en double, mauvais format d'id ;
- valeur hors liste (`type`, `technique`, `criticite`, `importance`) ;
- cas sans étape, étape sans action ou sans résultat attendu ;
- cas qui cite une exigence, un jeu de données ou une question absents ;
- `cas-de-tests.md` désynchronisé du JSON (modifié à la main ou non régénéré).

Avertissement :
- exigence couverte par aucun cas ; exigence sans cas négatif alors qu'elle porte une règle de validation ;
- cas lié à une question bloquante encore ouverte ;
- jeu de données non utilisé ; question sans exigence ni cas impacté ;
- formulation vague dans un résultat attendu (« correctement », « fonctionne », « avec succès »…).

Le contrôle écrit aussi `matrice-tracabilite.md` (exigence → cas) dans le dossier contrôlé.
