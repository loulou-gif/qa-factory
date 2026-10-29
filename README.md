# QA Factory

Chaîne de production des livrables de test, pilotée par Claude Code et des serveurs MCP :

**cahier des charges → cas de tests + questions + jeux de données → validation → Squash TM + specs d'automatisation → (lien de la plateforme disponible) → exploration → en parallèle : tests Playwright, cahier de tests, manuel utilisateur.**

Tout passe par un seul fichier validé, `cas-de-tests.json` : Squash, le cahier Excel et les specs en sont générés avec les mêmes identifiants (`EX-001`, `CT0001`). Rien n'est réécrit à la main à côté.

## Installation (une fois)

Prérequis sur le PC : Claude Code, Node.js 20+, Python 3 avec `openpyxl` (`pip install openpyxl`), Pandoc (pour les cahiers des charges en .docx).

1. Copier `.mcp.json.example` en `.mcp.json` et y mettre :
   - le chemin de `squash-tm-mcp\dist\index.js` (le MCP Squash amélioré) ;
   - l'URL de l'API Squash et un **jeton d'API** Squash (Squash → Mon compte → Jetons d'API).
   `.mcp.json` n'est pas versionné (il contient le jeton).
2. Ouvrir Claude Code dans ce dossier : `claude`. Taper `/mcp` : `squash-tm` et `playwright` doivent être connectés.
3. Si Node passe par un proxy d'entreprise : ajouter `"NODE_USE_ENV_PROXY": "1"` dans le bloc `env` de `squash-tm`.

## Utilisation

| Étape | Qui | Commande dans Claude Code | Résultat |
|---|---|---|---|
| 1. Créer le projet | Julius | `/nouveau-projet saucedemo https://www.saucedemo.com 28` | `projets/saucedemo/` et `projet.json` |
| 2. Déposer les documents | Julius | (explorateur de fichiers) | CDC, US, DSF dans `01-entrant/` |
| 3. Analyser | Claude | `/analyser saucedemo` | `02-a-valider/` : cas, questions, jeux de données |
| 4. Relire, corriger | Julius + Claude | `/corriger saucedemo <demande>` | nouvelle version dans `02-a-valider/` |
| 5. **Valider** | **Julius** | **déplacer les 4 fichiers dans `03-valide/`** | validation |
| 6. Publier dans Squash | Claude, accord de Julius | `/publier saucedemo` | exigences + cas liés dans Squash |
| 7. Specs d'automatisation | Claude | `/specs saucedemo` | specs BROUILLON dans `04-livrables/specs/` |
| 8. Explorer la plateforme | Claude | `/explorer saucedemo` | découvertes, écarts, specs CONFIRMÉES |
| 9. Recette, en parallèle | Claude | `/recette saucedemo` | tests Playwright exécutés + cahier Excel + manuel Word, produits ensemble |
| (ou séparément) | Claude | `/generer-tests`, `/cahier`, `/manuel` | un seul de ces livrables |
| Suivi | — | `/statut` | avancement de chaque projet |

Les étapes 1 à 7 forment le **temps A** (réception du cahier des charges, sans besoin de l'application). Les étapes 8 et 9 forment le **temps B** : elles ne démarrent qu'avec le lien de la plateforme, l'environnement et les comptes de test. **Le cahier de tests et le manuel ne sont produits qu'en temps B**, en parallèle de l'écriture des scripts automatisés. Les détails : `CLAUDE.md`.

Les 4 fichiers à déplacer à l'étape 5 : `cas-de-tests.json`, `cas-de-tests.md`, `ambiguites.md`, `jeux-de-donnees.md`.

## Ce que contient le dépôt

```text
qa-factory/
├── CLAUDE.md                 règles et workflow pour Claude (à lire en premier)
├── README.md                 ce guide
├── .mcp.json.example         serveurs MCP : squash-tm, playwright
├── .claude/
│   ├── settings.json         permissions : lecture Squash autorisée, écriture sur demande, suppression interdite
│   ├── commands/             /nouveau-projet, /analyser, /corriger, /publier, /specs, /explorer, /recette,
│   │                         /generer-tests, /cahier, /manuel, /statut
│   └── skills/               analyse-cdc, publication-squash, cahier-de-tests, specs-automatisation,
│                             exploration-application, generation-tests-playwright, manuel-utilisateur
├── docs/
│   ├── FORMAT-CAS-DE-TESTS.md   format des fichiers d'analyse et règles de contrôle
│   └── regles-livrables.md      règles de rédaction du manuel et du cahier (ta skill de documentation)
├── outils/                   scripts Python sans réseau : création de projet, vue de relecture,
│                             contrôle + matrice de traçabilité, cahier Excel, specs, statut
├── templates/
│   ├── cahier/               modèle Excel (Synelia / BNI)
│   ├── manuel/               modèle Word (CEPICI / Synelia) et générateur du manuel
│   ├── specs/                exemples de specs ANSUT et Orange eFacture
│   ├── automatisation/       socle d'un dépôt Playwright (AGENTS.md générique, config, preuves)
│   └── exemples/             découvertes, inventaire, points à confirmer d'Orange eFacture
└── projets/
    └── saucedemo/            projet d'exemple : CDC et analyse produite (02-a-valider)
```

## Outils en ligne de commande

Utilisables sans Claude :

```powershell
python outils/nouveau_projet.py <nom> --url <URL> --squash-id <ID> --libelle "<Nom>"
python outils/rendre_revue.py <projet>                  # vue de relecture depuis le JSON
python outils/controle.py <projet> [--dossier 03-valide] # contrôle + matrice de traçabilité
python outils/build_cahier.py <projet> [--nominaux]      # cahier Excel, temps B (exige l'URL et l'exploration)
python outils/generer_specs.py <projet>                  # specs BROUILLON (depuis 03-valide)
python outils/statut.py [projet]
```

## Garde-fous

- Rien n'est publié ni généré depuis `02-a-valider` : seul ce que Julius a déplacé dans `03-valide` compte.
- Squash : simulation d'abord, publication réelle après accord ; aucune suppression possible (bloquée dans le MCP et dans `.claude/settings.json`).
- Aucune donnée inventée : un manque du cahier des charges devient une question (`ambiguites.md`).
- Aucun secret dans les fichiers : identifiants par variables d'environnement.
- Le cahier de tests et le manuel ne sont jamais produits avant que la plateforme soit accessible et explorée.

## Limites connues

- Claude ne surveille pas les dossiers : chaque étape se lance par une commande.
- Un cas déjà publié et modifié ensuite n'est pas mis à jour dans Squash (à faire à la main ; Claude liste les cas concernés).
- Cahier de tests : version française uniquement pour l'instant.
- Les cahiers des charges sont envoyés au modèle d'IA : vérifier que le client l'autorise.
