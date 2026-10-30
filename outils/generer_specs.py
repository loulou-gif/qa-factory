# -*- coding: utf-8 -*-
"""Génère les specs d'automatisation (une par fonctionnalité) à partir de 03-valide.

Usage : python outils/generer_specs.py <projet> [--forcer]

Format : celui des projets ANSUT / Orange eFacture (FEATURE, DESCRIPTION, CRITÈRES
D'ACCEPTATION, DATA, SCENARIO, OBSERVABILITY, LOCATOR_RULES, POINTS À CONFIRMER).
Les specs produites sont au statut BROUILLON : les blocs INTERACT / ASSERT et les
locators sont complétés par /explorer (temps B), une fois l'application accessible.

Une spec déjà passée au statut CONFIRMÉE n'est jamais écrasée (sauf --forcer).
"""
import argparse
import re
from datetime import date

from qa_commun import charger_cas, charger_projet, fonctionnalites, journaliser, lire_jeux, lire_questions, slug

LOCATOR_RULES = """LOCATOR_RULES

priority

1 : data-testid
2 : id
3 : name
4 : role / label (getByRole, getByLabel)
5 : css stable
6 : xpath (dernier recours)

avoid

- xpath absolu
- sélecteurs positionnels (nth, tr[1], li[2])
- classes CSS générées
- tout locator non observé dans l'application réelle
"""

OBSERVABILITY = """OBSERVABILITY

screenshot

on_success : true
on_failure : true

allure

attach_screenshots : true

logs

navigation : true
interaction : true
assertion : true
"""


def lignes_jdd(jdd):
    res = []
    for ligne in jdd["corps"].splitlines():
        cols = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cols) >= 2 and ligne.strip().startswith("|") and not re.match(r"^-+$", cols[0]) and cols[0].lower() != "champ":
            valeur = cols[1].strip("`")
            secret = "variable" in valeur.lower() or "jamais en clair" in " ".join(cols[2:]).lower()
            m = re.search(r"variable\s+`?([A-Z0-9_]+)`?", cols[1])
            if m:
                valeur = "{{" + m.group(1) + "}}"
            res.append((slug(cols[0]).replace("-", "_"), valeur, secret))
    return res


# Types de test automatisables avec Playwright (interface web). Les autres (performance, fiabilité…)
# relèvent d'une campagne dédiée (Gatling, k6, outils de sécurité…) décrite dans strategie_tests.
TYPES_PLAYWRIGHT = {"fonctionnel", "securite", "utilisabilite", "compatibilite"}


def automatisable(c):
    return c.get("type_test", "fonctionnel") in TYPES_PLAYWRIGHT


def generer(d, projet, data, f, questions, jeux, version):
    cas = [c for c in data["cas_de_tests"] if c.get("fonctionnalite") == f and automatisable(c)]
    exigences = [e for e in data["exigences"] if e.get("fonctionnalite") == f]
    code = slug(f).upper().replace("-", "_")
    tags = {slug(f), "regression"}
    if any(c.get("type") == "nominal" and c.get("importance") in ("HIGH", "VERY_HIGH") for c in cas):
        tags.add("smoke")
    qs = sorted({q for x in exigences + cas for q in x.get("questions", [])})
    jdd_ids = sorted({j for c in cas for j in c.get("jeux_de_donnees", [])})
    app = projet.get("application", {})
    variables = app.get("variables_identifiants") or ["APP_USERNAME", "APP_PASSWORD"]

    L = [
        f"FEATURE : {code}",
        "NAME",
        f,
        "APPLICATION",
        projet.get("nom", ""),
        "MODULE",
        f,
        "STATUT",
        f"BROUILLON — généré le {date.today().isoformat()} depuis 03-valide/cas-de-tests.json (version {version}).",
        "Les libellés, enchaînements, messages et locators sont ceux du cahier des charges : ils doivent être",
        "confirmés par /explorer sur l'application réelle avant toute génération de test.",
        "TAGS",
        " ".join(f"@{t}" for t in sorted(tags)),
        "SOURCES",
    ]
    L += [f"- {e['id']} : {e.get('source', '')}" for e in exigences]
    L += ["DESCRIPTION", ""]
    L += [f"- {e['id']} {e.get('titre', '')} : {e.get('description', '')}" for e in exigences]
    L += ["", "USER STORY",
          "<!-- À rédiger par /specs à partir des exigences ci-dessus uniquement : En tant que <rôle documenté>, "
          "je veux <action>, afin de <valeur métier>. Rôle inconnu = point à confirmer. -->",
          "CRITÈRES D'ACCEPTATION"]
    L += [f"{i}. {e.get('titre', '')} ({e['id']})" for i, e in enumerate(exigences, start=1)]
    L += ["", "DATA", "", "base_url", 'value       : "{{BASE_URL}}"', "",
          "session", f'value       : "{{{{{variables[0]}}}}} / {{{{{variables[-1]}}}}}"', "secret      : true", ""]
    for jid in jdd_ids:
        j = jeux.get(jid)
        if not j:
            continue
        L += [slug(jid).replace("-", "_"), f'label       : "{j["titre"]}"', f'type        : "{j["type"]}"']
        for cle, valeur, secret in lignes_jdd(j):
            L.append(f'{cle:<12}: "{valeur}"' + ("  # secret" if secret else ""))
        L.append("")

    for c in cas:
        L += [f"SCENARIO {c['id']} — {c.get('titre', '')}", "",
              f"id        : {c['id']}",
              f"tags      : [{', '.join(sorted({slug(f), c.get('type', '')}))}]",
              f"exigences : [{', '.join(c.get('exigences', []))}]",
              f"type      : {c.get('type', '')}",
              f"type_test : {c.get('type_test', 'fonctionnel')}",
              f"technique : {c.get('technique', '')}",
              f"importance: {c.get('importance', 'MEDIUM')}"]
        if c.get("jeux_de_donnees"):
            L.append(f"data      : [{', '.join(slug(j).replace('-', '_') for j in c['jeux_de_donnees'])}]")
        if c.get("questions"):
            L.append(f"questions : [{', '.join(c['questions'])}]")
        L += ["", f"GIVEN {c.get('prerequis', '')}", "", 'CONNECT url="{{BASE_URL}}"', "  session=reuse", ""]
        for i, s in enumerate(c.get("etapes", []), start=1):
            L += [f"STEP {i}", f"WHEN {s.get('action', '')}",
                  "<!-- INTERACT : à écrire après exploration (élément réel, locator validé) -->",
                  f"THEN {s.get('resultat_attendu', '')}",
                  "<!-- ASSERT : à écrire après exploration (fait observable, texte réel) -->", ""]
    L += [OBSERVABILITY, LOCATOR_RULES, "POINTS À CONFIRMER", ""]
    if qs:
        for q in qs:
            info = questions.get(q, {})
            L.append(f"- {q} [{info.get('gravite', '?')}, {info.get('statut', '?')}] {info.get('question', '')}"
                     + (f" — Réponse : {info['reponse']}" if info.get("reponse") else ""))
    else:
        L.append("- Aucune question liée dans ambiguites.md.")
    L += ["- Tous les libellés, messages et enchaînements : à confirmer par exploration (statut BROUILLON).", ""]
    return "\n".join(L)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("projet")
    p.add_argument("--forcer", action="store_true", help="écraser aussi les specs CONFIRMÉES")
    a = p.parse_args()
    d, projet = charger_projet(a.projet)
    base = d / "03-valide"
    data = charger_cas(base / "cas-de-tests.json")
    questions = lire_questions(base / "ambiguites.md")
    jeux = lire_jeux(base / "jeux-de-donnees.md")
    version = data.get("meta", {}).get("version", "?")
    out_dir = d / "04-livrables" / "specs"
    out_dir.mkdir(parents=True, exist_ok=True)
    ecrits, ignores = [], []
    sans_cas = []
    hors = [c for c in data["cas_de_tests"] if not automatisable(c)]
    for f in fonctionnalites(data):
        if not any(c.get("fonctionnalite") == f and automatisable(c) for c in data["cas_de_tests"]):
            sans_cas.append(f)
            continue
        cible = out_dir / f"{slug(f)}.md"
        if cible.exists() and not a.forcer and "STATUT\nCONFIRM" in cible.read_text(encoding="utf-8"):
            ignores.append(cible.name)
            continue
        cible.write_text(generer(d, projet, data, f, questions, jeux, version), encoding="utf-8")
        ecrits.append(cible.name)
    journaliser(d, "specs", f"{len(ecrits)} spec(s) BROUILLON", [f"04-livrables/specs/{n}" for n in ecrits])
    for n in ecrits:
        print(f"écrit   : 04-livrables/specs/{n}")
    for n in ignores:
        print(f"conservé (CONFIRMÉE) : 04-livrables/specs/{n}")
    for f in sans_cas:
        print(f"pas de spec : « {f} » n'a aucun cas automatisable avec Playwright")
    for c in hors:
        print(f"hors Playwright : {c['id']} ({c.get('type_test')}) → campagne dédiée, voir strategie_tests")


if __name__ == "__main__":
    main()
