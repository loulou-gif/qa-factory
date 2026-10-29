# -*- coding: utf-8 -*-
"""Affiche l'avancement des projets.

Usage : python outils/statut.py [projet]
"""
import json
import sys

from qa_commun import PROJETS, lire_questions


def etat(d):
    def a(p):
        return (d / p).exists()
    entrants = [f for f in (d / "01-entrant").glob("*") if f.name != "LISEZMOI.md"] if a("01-entrant") else []
    questions = lire_questions(d / "03-valide" / "ambiguites.md") or lire_questions(d / "02-a-valider" / "ambiguites.md")
    ouvertes = sum(1 for q in questions.values() if q["statut"] == "ouverte")
    squash = list((d / "04-livrables" / "squash").glob("*correspondance*.json")) if a("04-livrables/squash") else []
    publie = ""
    if squash:
        c = json.loads(squash[0].read_text(encoding="utf-8"))
        publie = f"{len(c.get('exigences', {}))} exigences, {len(c.get('cas_de_tests', {}))} cas"
    specs = list((d / "04-livrables" / "specs").glob("*.md")) if a("04-livrables/specs") else []
    confirmees = sum(1 for s in specs if "STATUT\nCONFIRM" in s.read_text(encoding="utf-8"))
    cahier = list((d / "04-livrables" / "cahier").glob("*.xlsx")) if a("04-livrables/cahier") else []
    manuel = list((d / "04-livrables" / "manuel").glob("*.docx")) if a("04-livrables/manuel") else []
    lignes = [
        ("Documents d'entrée", f"{len(entrants)} fichier(s)" if entrants else "à déposer dans 01-entrant/"),
        ("Analyse (02-a-valider)", "faite" if a("02-a-valider/cas-de-tests.json") else "à lancer : /analyser"),
        ("Validation (03-valide)", "validée" if a("03-valide/cas-de-tests.json") else "en attente de Julius"),
        ("Questions ouvertes", str(ouvertes)),
        ("Publication Squash", publie or "non faite : /publier"),
        ("Specs d'automatisation", f"{len(specs)} ({confirmees} confirmée(s))" if specs else "non faites : /specs"),
        ("Cahier de tests", ", ".join(c.name for c in cahier) or "temps B : /cahier ou /recette"),
        ("Manuel utilisateur", ", ".join(m.name for m in manuel) or "temps B : /manuel ou /recette"),
    ]
    return lignes


def main():
    cible = sys.argv[1] if len(sys.argv) > 1 else None
    projets = [PROJETS / cible] if cible else sorted(p for p in PROJETS.iterdir() if p.is_dir() and not p.name.startswith("_"))
    if not projets:
        print("Aucun projet. Créer : python outils/nouveau_projet.py <nom>")
    for d in projets:
        if not d.is_dir():
            print(f"Projet introuvable : {d.name}")
            continue
        print(f"\n== {d.name}")
        for k, v in etat(d):
            print(f"  {k:<26} {v}")


if __name__ == "__main__":
    main()
