# -*- coding: utf-8 -*-
"""Génère la vue de relecture cas-de-tests.md à partir de cas-de-tests.json.

Usage : python outils/rendre_revue.py <projet> [--dossier 02-a-valider|03-valide]

Le fichier produit porte l'empreinte du JSON : le contrôle détecte ainsi une vue
modifiée à la main ou non régénérée après une correction du JSON.
"""
import argparse
from collections import Counter

from qa_commun import charger_cas, charger_projet, empreinte, fonctionnalites, lire_questions

TYPES = {"nominal": "Nominal", "negatif": "Négatif", "limite": "Limite", "securite": "Sécurité", "ergonomie": "Ergonomie"}


def cellule(t):
    return str(t or "").replace("|", "\\|").replace("\n", "<br>")


def rendre(projet_nom, dossier):
    d, projet = charger_projet(projet_nom)
    base = d / dossier
    fjson = base / "cas-de-tests.json"
    data = charger_cas(fjson)
    questions = lire_questions(base / "ambiguites.md")
    exigences = data.get("exigences", [])
    cas = data.get("cas_de_tests", [])
    meta = data.get("meta", {})

    lignes = [
        f"<!-- Fichier généré par outils/rendre_revue.py à partir de cas-de-tests.json — NE PAS MODIFIER. empreinte: {empreinte(fjson)} -->",
        f"# Cas de tests — {projet.get('nom', projet_nom)} (version {meta.get('version', '?')})",
        "",
        "Vue de relecture. Pour corriger : `/corriger " + projet_nom + " <demande>` (le JSON est modifié, puis cette vue est régénérée).",
        "",
        f"Sources analysées : {', '.join(meta.get('sources', [])) or 'non renseignées'}",
        "",
        "## Synthèse",
        "",
        "| Indicateur | Valeur |",
        "|---|---|",
        f"| Fonctionnalités | {len(fonctionnalites(data))} |",
        f"| Exigences | {len(exigences)} |",
        f"| Cas de tests | {len(cas)} |",
    ]
    for t, n in sorted(Counter(c.get("type", "?") for c in cas).items()):
        lignes.append(f"| Cas {TYPES.get(t, t).lower()} | {n} |")
    ouvertes = [q for q in questions.values() if q["statut"] == "ouverte"]
    bloquantes = [qid for qid, q in questions.items() if q["statut"] == "ouverte" and q["gravite"] == "bloquante"]
    lignes += [
        f"| Questions ouvertes | {len(ouvertes)} (dont bloquantes : {len(bloquantes)}) |",
        "",
    ]

    for f in fonctionnalites(data):
        lignes += [f"## {f}", "", "### Exigences", "", "| ID | Exigence | Criticité | Source | Questions |", "|---|---|---|---|---|"]
        for e in (x for x in exigences if x.get("fonctionnalite") == f):
            lignes.append(f"| {e['id']} | **{cellule(e.get('titre'))}**<br>{cellule(e.get('description'))} | "
                          f"{e.get('criticite', 'MAJOR')} | {cellule(e.get('source'))} | {', '.join(e.get('questions', []))} |")
        lignes += ["", "### Cas de tests", ""]
        for c in (x for x in cas if x.get("fonctionnalite") == f):
            alerte = ""
            if any(q in bloquantes for q in c.get("questions", [])):
                alerte = " — **suspendu à une question bloquante**"
            lignes += [
                f"#### {c['id']} — {c.get('titre', '')}{alerte}",
                "",
                f"- **Exigences** : {', '.join(c.get('exigences', []))}",
                f"- **Type** : {TYPES.get(c.get('type'), c.get('type'))} — **Technique** : {c.get('technique', '')} — **Importance** : {c.get('importance', 'MEDIUM')}",
                f"- **Prérequis** : {cellule(c.get('prerequis'))}",
            ]
            if c.get("description"):
                lignes.append(f"- **Objectif** : {cellule(c['description'])}")
            if c.get("jeux_de_donnees"):
                lignes.append(f"- **Jeux de données** : {', '.join(c['jeux_de_donnees'])}")
            if c.get("questions"):
                lignes.append(f"- **Questions liées** : {', '.join(c['questions'])}")
            lignes += ["", "| # | Action | Résultat attendu |", "|---|---|---|"]
            for i, s in enumerate(c.get("etapes", []), start=1):
                lignes.append(f"| {i} | {cellule(s.get('action'))} | {cellule(s.get('resultat_attendu'))} |")
            lignes.append("")

    sortie = base / "cas-de-tests.md"
    sortie.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return sortie, len(exigences), len(cas)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("projet")
    p.add_argument("--dossier", default="02-a-valider", choices=["02-a-valider", "03-valide"])
    a = p.parse_args()
    sortie, ne, nc = rendre(a.projet, a.dossier)
    print(f"{sortie} : {ne} exigences, {nc} cas de tests")


if __name__ == "__main__":
    main()
