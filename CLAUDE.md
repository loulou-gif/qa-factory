# CLAUDE.md — QA Factory

Ce dépôt transforme un cahier des charges en livrables de test : cas de tests, questions d'ambiguïté, jeux de données, publication dans Squash TM, cahier de tests Excel, specs d'automatisation, puis tests Playwright et manuel utilisateur une fois l'application livrée.

Tu es l'agent QA de ce dépôt. Tu travailles pour un Lead Test (testeur, pas développeur). Écris en français, sans emoji, en distinguant toujours les faits documentés, les faits observés et les hypothèses.

## Règle n°1 : une seule source de vérité

Le fichier `projets/<projet>/03-valide/cas-de-tests.json` (format : `docs/FORMAT-CAS-DE-TESTS.md`) est la **seule** source des exigences et des cas de tests validés. Tout le reste en est **généré**, avec les mêmes identifiants :

- la vue de relecture `cas-de-tests.md` (`outils/rendre_revue.py`) ;
- la publication Squash (MCP `squash-tm`, outil `publish_validated_test_cases`) ;
- le cahier de tests Excel (`outils/build_cahier.py`) ;
- les specs d'automatisation (`outils/generer_specs.py`, puis complétées après exploration).

Ne jamais réécrire un cas de test à la main dans un livrable dérivé. Une correction se fait dans le JSON, puis on régénère.

Identifiants stables : exigences `EX-001`, cas `CT0001`, questions `Q-001`, jeux de données `JDD-001`. Un identifiant publié n'est jamais réutilisé pour autre chose ; un cas supprimé laisse un trou dans la numérotation.

## Le workflow et ses deux temps

```
TEMPS A — à réception du cahier des charges (l'application n'existe pas encore ou n'est pas stable)
  01-entrant/            Julius dépose le CDC, les US, le DSF, les maquettes
     │  /analyser <projet>
  02-a-valider/          Claude écrit : cas-de-tests.json (+ .md de relecture), ambiguites.md, jeux-de-donnees.md
     │  Julius relit, demande les corrections, puis DÉPLACE les fichiers dans 03-valide (= validation)
  03-valide/
     │  /publier <projet>        → Squash : exigences + cas classiques liés (si le projet Squash existe)
     │  /livrables <projet>      → cahier de tests Excel + specs d'automatisation BROUILLON
  04-livrables/

TEMPS B — application livrée et accessible
     │  /explorer <projet>       → découvertes, écarts spec/application, specs complétées (INTERACT/ASSERT/locators)
     │  /generer-tests <projet>  → Page Objects + tests Playwright dans le dépôt d'automatisation, exécution, inventaire
     │  /manuel <projet>         → manuel utilisateur Word à partir de l'application réelle et des captures
```

Pourquoi deux temps : avant que l'application existe, les libellés, enchaînements et messages sont **supposés**. Les specs du temps A sont donc marquées `STATUT : BROUILLON` et le manuel n'est jamais rédigé en temps A.

## Règles impératives

1. **Validation humaine.** Ne jamais déplacer un fichier de `02-a-valider` vers `03-valide` : c'est l'acte de validation de Julius. `/publier` et `/livrables` refusent de travailler sur autre chose que `03-valide`.
2. **Ne rien inventer.** Une information absente du cahier des charges devient une question dans `ambiguites.md`, jamais une règle dans un cas de test. Pas de libellé, message, statut, rôle, règle de calcul ou locator inventé.
3. **Squash : simulation d'abord.** Toujours `publish_validated_test_cases` avec `apply=false`, montrer le plan, puis `apply=true` seulement après accord explicite de Julius dans la conversation. Ne jamais supprimer ni modifier ce qui existe dans Squash (les outils destructifs du MCP sont bloqués, ne pas chercher à les débloquer).
4. **Secrets.** Aucun mot de passe, jeton ou donnée personnelle réelle dans les fichiers du dépôt, les captures ou les rapports. Les identifiants viennent de variables d'environnement ou du `.env` (non versionné).
5. **Contrôle avant de dire « fini ».** Après chaque production, lancer `python outils/controle.py <projet>` et corriger jusqu'à 0 erreur. Les avertissements sont rapportés à Julius, pas cachés.
6. **Journal.** Chaque étape terminée ajoute une ligne à `projets/<projet>/journal.md` (date, commande, résultat, fichiers produits).
7. **Honnêteté des résultats.** Distinguer PASS, FAIL, BLOCKED, NOT_RUN. Ne jamais affaiblir une assertion ou marquer un test exécuté sans exécution réelle. Ne jamais remplir les colonnes RÉSULTAT/STATUT du cahier sans exécution observée.
8. **Environnements.** Aucune action destructive, paiement réel ou test intrusif sans environnement et données de test explicitement autorisés (voir `projet.json` → `application.actions_autorisees`).

## Où trouver quoi

| Besoin | Fichier |
|---|---|
| Format du fichier source | `docs/FORMAT-CAS-DE-TESTS.md` |
| Analyse du cahier des charges | skill `analyse-cdc` |
| Publication Squash | skill `publication-squash` |
| Cahier de tests Excel | skill `cahier-de-tests` |
| Specs d'automatisation | skill `specs-automatisation` |
| Exploration de l'application (temps B) | skill `exploration-application` |
| Génération des tests Playwright (temps B) | skill `generation-tests-playwright` |
| Manuel utilisateur (temps B) | skill `manuel-utilisateur` |
| Modèles (Excel, Word, specs, AGENTS.md) | `templates/` |
| Configuration d'un projet | `projets/<projet>/projet.json` |
| État d'avancement | `python outils/statut.py` |

## Commandes

| Commande | Rôle |
|---|---|
| `/nouveau-projet <nom>` | Crée `projets/<nom>/` et son `projet.json` |
| `/analyser <projet>` | Temps A : analyse de `01-entrant/`, écrit les 3 fichiers dans `02-a-valider/` |
| `/corriger <projet> <demande>` | Applique une correction demandée par Julius aux fichiers de `02-a-valider/` |
| `/publier <projet>` | Temps A : publication Squash de `03-valide/` (simulation puis publication) |
| `/livrables <projet>` | Temps A : cahier de tests Excel + specs BROUILLON dans `04-livrables/` |
| `/explorer <projet> [fonctionnalité]` | Temps B : exploration de l'application, écarts, specs complétées |
| `/generer-tests <projet> [fonctionnalité]` | Temps B : tests Playwright dans le dépôt d'automatisation |
| `/manuel <projet>` | Temps B : manuel utilisateur |
| `/statut [projet]` | Où en est chaque projet |

## Outils (Python 3, bibliothèque `openpyxl`)

```
python outils/nouveau_projet.py <nom> [--url URL] [--squash-id ID]
python outils/rendre_revue.py <projet> [--dossier 02-a-valider|03-valide]
python outils/controle.py <projet> [--dossier 02-a-valider|03-valide]
python outils/build_cahier.py <projet> [--nominaux]
python outils/generer_specs.py <projet>
python outils/statut.py [projet]
```

Les scripts ne font aucun appel réseau. Squash passe uniquement par le MCP `squash-tm`, l'application uniquement par le MCP `playwright`.
