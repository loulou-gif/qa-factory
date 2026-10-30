# -*- coding: utf-8 -*-
"""Génère les commandes OpenCode (.opencode/commands/) à partir des commandes Claude Code.

Usage : python outils/synchroniser_opencode.py

- .claude/commands/<nom>.md est la source : le corps est repris tel quel, seule la
  description est conservée dans l'en-tête (OpenCode n'utilise pas argument-hint).
- Les commandes qui diffèrent vraiment entre les deux outils ont une version dédiée
  dans outils/opencode/<nom>.md, copiée telle quelle (ex. recette.md : sous-agents
  OpenCode appelés avec l'outil task).
"""
import re

from qa_commun import RACINE

SOURCE = RACINE / ".claude" / "commands"
DEDIEES = RACINE / "outils" / "opencode"
CIBLE = RACINE / ".opencode" / "commands"


def convertir(texte):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", texte, flags=re.S)
    if not m:
        return texte
    entete, corps = m.groups()
    desc = re.search(r"^description:\s*(.*)$", entete, flags=re.M)
    lignes = ["---", f"description: {desc.group(1).strip()}" if desc else "description: commande QA Factory", "---"]
    return "\n".join(lignes) + "\n" + corps


def main():
    CIBLE.mkdir(parents=True, exist_ok=True)
    dediees = {p.name for p in DEDIEES.glob("*.md")}
    ecrites = []
    for src in sorted(SOURCE.glob("*.md")):
        texte = (DEDIEES / src.name).read_text(encoding="utf-8") if src.name in dediees else convertir(src.read_text(encoding="utf-8"))
        (CIBLE / src.name).write_text(texte, encoding="utf-8")
        ecrites.append(src.name + (" (version dédiée)" if src.name in dediees else ""))
    connues = {p.name for p in SOURCE.glob("*.md")}
    orphelines = [p.name for p in CIBLE.glob("*.md") if p.name not in connues]
    for n in ecrites:
        print(f"écrit : .opencode/commands/{n}")
    for n in orphelines:
        print(f"ATTENTION : .opencode/commands/{n} n'a plus d'équivalent Claude Code (à supprimer à la main)")


if __name__ == "__main__":
    main()
