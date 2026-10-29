# -*- coding: utf-8 -*-
"""Fonctions communes aux outils QA Factory (aucun appel réseau)."""
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
PROJETS = RACINE / "projets"
TEMPLATES = RACINE / "templates"

DOSSIERS = ["01-entrant", "02-a-valider", "03-valide", "04-livrables"]

TYPES_CAS = {"nominal", "negatif", "limite", "securite", "ergonomie"}
TECHNIQUES = {"cas-d-usage", "partitions-equivalence", "valeurs-limites", "table-decision",
              "transition-etats", "devinette-erreurs", "exploratoire"}
CRITICITES = {"CRITICAL", "MAJOR", "MINOR", "UNDEFINED"}
IMPORTANCES = {"LOW", "MEDIUM", "HIGH", "VERY_HIGH"}

RE_EX = re.compile(r"^EX-\d{3,}$")
RE_CT = re.compile(r"^CT\d{4,}$")
RE_Q = re.compile(r"^Q-\d{3,}$")
RE_JDD = re.compile(r"^JDD-\d{3,}$")

# Windows : la console peut être en cp1252 ; on force l'UTF-8 pour les accents.
for flux in (sys.stdout, sys.stderr):
    try:
        flux.reconfigure(encoding="utf-8")
    except Exception:
        pass


def erreur(message, code=1):
    print(f"ERREUR : {message}", file=sys.stderr)
    sys.exit(code)


def dossier_projet(nom):
    d = PROJETS / nom
    if not d.is_dir():
        existants = sorted(p.name for p in PROJETS.iterdir() if p.is_dir() and not p.name.startswith("_")) if PROJETS.is_dir() else []
        erreur(f"projet « {nom} » introuvable dans {PROJETS}. Projets existants : {', '.join(existants) or 'aucun'}")
    return d


def charger_projet(nom):
    d = dossier_projet(nom)
    f = d / "projet.json"
    if not f.exists():
        erreur(f"{f} absent : lancer d'abord outils/nouveau_projet.py")
    return d, json.loads(f.read_text(encoding="utf-8"))


def charger_cas(fichier):
    if not fichier.exists():
        erreur(f"{fichier} introuvable")
    try:
        return json.loads(fichier.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        erreur(f"{fichier} : JSON invalide ({e})")


def empreinte(fichier):
    """Empreinte du JSON normalisé : insensible aux espaces, sensible au contenu."""
    data = json.loads(fichier.read_text(encoding="utf-8"))
    canon = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()[:16]


def _sections(texte, motif):
    """Découpe un fichier Markdown en sections '### <ID> — titre'."""
    parties = re.split(r"^###\s+", texte, flags=re.M)
    res = {}
    for p in parties[1:]:
        entete, _, corps = p.partition("\n")
        m = re.match(rf"({motif})\s*[—–-]\s*(.*)", entete.strip())
        if m:
            res[m.group(1)] = {"titre": m.group(2).strip(), "corps": corps}
    return res


def _champ(corps, nom):
    m = re.search(rf"^\s*-\s*\*\*{nom}\*\*\s*:\s*(.*)$", corps, flags=re.M | re.I)
    return m.group(1).strip() if m else ""


def lire_questions(fichier):
    if not fichier.exists():
        return {}
    res = {}
    for qid, s in _sections(fichier.read_text(encoding="utf-8"), r"Q-\d{3,}").items():
        res[qid] = {
            "titre": s["titre"],
            "type": _champ(s["corps"], "Type"),
            "gravite": _champ(s["corps"], "Gravité").lower(),
            "statut": _champ(s["corps"], "Statut").lower(),
            "question": _champ(s["corps"], "Question"),
            "reponse": _champ(s["corps"], "Réponse"),
            "impact": re.findall(r"(?:EX-\d{3,}|CT\d{4,})", _champ(s["corps"], "Impact")),
        }
    return res


def lire_jeux(fichier):
    if not fichier.exists():
        return {}
    res = {}
    for jid, s in _sections(fichier.read_text(encoding="utf-8"), r"JDD-\d{3,}").items():
        res[jid] = {
            "titre": s["titre"],
            "type": _champ(s["corps"], "Type"),
            "cas": re.findall(r"CT\d{4,}", _champ(s["corps"], "Cas concernés")),
            "corps": s["corps"],
        }
    return res


def journaliser(dossier, commande, resultat, fichiers=()):
    j = dossier / "journal.md"
    if not j.exists():
        j.write_text("# Journal du projet\n\n| Date | Commande | Résultat | Fichiers |\n|---|---|---|---|\n", encoding="utf-8")
    liste = ", ".join(f"`{f}`" for f in fichiers)
    with j.open("a", encoding="utf-8") as f:
        f.write(f"| {date.today().isoformat()} | {commande} | {resultat} | {liste} |\n")


def fonctionnalites(cas_json):
    """Fonctionnalités dans l'ordre de première apparition (exigences puis cas)."""
    vues = []
    for e in cas_json.get("exigences", []) + cas_json.get("cas_de_tests", []):
        f = e.get("fonctionnalite")
        if f and f not in vues:
            vues.append(f)
    return vues


def slug(texte):
    import unicodedata
    t = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "fonctionnalite"
