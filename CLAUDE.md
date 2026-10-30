# CLAUDE.md — QA Factory

Les règles du dépôt sont dans `AGENTS.md`, partagé avec OpenCode :

@AGENTS.md

## Spécificités Claude Code

- Commandes : `.claude/commands/`. Après toute modification d'une commande, lancer `python outils/synchroniser_opencode.py` pour mettre à jour la version OpenCode.
- `/recette` : lancer les trois sous-agents avec l'outil Agent, en un seul message (trois appels), pour qu'ils travaillent en parallèle.
- Permissions : `.claude/settings.json` (lecture Squash autorisée, écritures sur demande, suppressions interdites).
- MCP : `.mcp.json` (variables d'environnement `SQUASH_MCP_INDEX`, `SQUASH_TM_BASE_URL`, `SQUASH_TM_API_TOKEN`).
