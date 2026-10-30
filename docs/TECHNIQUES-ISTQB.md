# Référentiel ISTQB de conception des tests

Ce document est **le seul référentiel** que l'agent applique pour concevoir les cas de tests (`/analyser`, `/corriger`). Une technique ou un type de test qui n'y figure pas est refusé par `outils/controle.py`.

Références :
- **CTFL v4.0** : ISTQB Certified Tester Foundation Level, syllabus v4.0 (2023), chapitres 2 et 4 ;
- **CTFL v3.1** : syllabus Foundation précédent (2018), pour le test des cas d'utilisation, retiré de la v4.0 mais toujours enseigné au niveau avancé ;
- **CTAL-TA** : ISTQB Advanced Level Test Analyst ;
- **ISO/IEC 25010** : modèle de qualité du produit, auquel le CTFL v4.0 renvoie pour les tests non fonctionnels.

## 1. Techniques de conception autorisées

Chaque cas de test porte **une** technique dans le champ `technique` : celle qui a permis de le dériver.

| Code (`technique`) | Technique | Référence | Quand l'appliquer | Comment dériver les cas |
|---|---|---|---|---|
| `partitions-equivalence` | Partitions d'équivalence | CTFL v4.0 §4.2.1 | Champ, paramètre ou option dont les valeurs se regroupent en classes traitées de la même façon | Identifier les partitions valides et invalides documentées ; un cas par partition invalide (une seule invalide à la fois) ; les partitions valides peuvent être combinées dans un même cas |
| `valeurs-limites` | Analyse des valeurs limites | CTFL v4.0 §4.2.2 | Partition ordonnée avec des bornes **données par le CDC** (longueur, montant, date, quantité) | Méthode à 2 valeurs (borne et voisin hors partition) par défaut, à 3 valeurs pour les règles critiques ; borne absente du CDC = question, jamais une valeur supposée. Cas de nature `limite` |
| `table-decision` | Tables de décision | CTFL v4.0 §4.2.3 | Règle qui combine plusieurs conditions (identifiant × mot de passe, statut × rôle) | Écrire la table (conditions, actions) dans la `description` du premier cas ; un cas par colonne retenue ; colonnes impossibles écartées avec la raison |
| `transition-etats` | Test de transition d'états | CTFL v4.0 §4.2.4 | Objet à statuts **documentés** (commande, compte, session, réclamation) | Couvrir chaque transition valide (couverture des transitions valides) et les transitions invalides significatives ; citer l'état de départ dans les prérequis |
| `cas-d-usage` | Test des cas d'utilisation | CTFL v3.1 §4.2.5, CTAL-TA | Parcours utilisateur de bout en bout décrit dans le CDC ou une US | Un cas pour le scénario principal ; un cas par scénario alternatif ou d'exception documenté |
| `criteres-acceptation` | Test basé sur les critères d'acceptation | CTFL v4.0 §4.5.2 | User Story avec critères d'acceptation, ou règle formulée « doit / ne doit pas » | Un cas au moins par critère ; le résultat attendu reprend le critère sous forme observable |
| `test-combinatoire` | Test combinatoire (par paires) | CTAL-TA | Plusieurs paramètres indépendants à plusieurs valeurs (filtres, options) dont la combinaison exhaustive est trop coûteuse | Couvrir toutes les paires de valeurs ; lister les paramètres et valeurs dans la `description` |
| `arbre-classification` | Arbre de classification | CTAL-TA | Entrées décomposables en classifications et classes (formulaire riche, paramétrage) | Décrire l'arbre dans la `description` ; un cas par combinaison retenue |
| `devinette-erreurs` | Estimation d'erreurs | CTFL v4.0 §4.4.1 | Erreurs plausibles connues du métier ou des projets similaires, non décrites dans le CDC | Cas de nature `negatif`, la `description` dit quelle erreur est visée ; le résultat attendu non documenté devient une question |
| `exploratoire` | Test exploratoire | CTFL v4.0 §4.4.2 | Zone mal spécifiée ou à risque, utile en temps B | Plutôt dans la stratégie (`approche: exploratoire`, avec une charte) qu'en cas détaillé |
| `checklist` | Test basé sur des checklists | CTFL v4.0 §4.4.3 | Contrôles génériques (ergonomie, accessibilité, sécurité de base) | Un cas par point de checklist qui porte une exigence du CDC ; préciser la checklist utilisée |

**Exclues** : les techniques boîte blanche (CTFL v4.0 §4.3 : test des instructions, test des branches). Elles exigent le code source, que l'équipe de test n'a pas. Toute technique hors de ce tableau (« intuition », « happy path », « smoke »…) est une erreur de contrôle.

### Choix de la technique, exigence par exigence

1. L'exigence décrit un parcours → `cas-d-usage` (ou `criteres-acceptation` si elle vient d'une US avec critères).
2. Elle impose des valeurs ou des formats → `partitions-equivalence`, puis `valeurs-limites` si des bornes sont données.
3. Elle combine des conditions → `table-decision` (ou `test-combinatoire` au-delà de 3-4 paramètres indépendants).
4. Elle mentionne des statuts ou un cycle de vie → `transition-etats`.
5. Le métier laisse prévoir des erreurs non décrites → `devinette-erreurs`, résultat attendu à confirmer.

Une exigence fonctionnelle reçoit au minimum un cas nominal ; une exigence qui porte une règle de validation reçoit aussi au moins un cas négatif ou limite (le contrôle le vérifie).

## 2. Types de test

Chaque cas porte un `type_test` : la caractéristique de qualité qu'il vérifie (CTFL v4.0 §2.2.2, ISO/IEC 25010). La `nature` Squash en découle et doit correspondre (vérifié par le contrôle).

| Code (`type_test`) | Type de test | Ce qui est vérifié | `nature` Squash | Automatisable Playwright | Outillage habituel |
|---|---|---|---|---|---|
| `fonctionnel` | Test fonctionnel | Complétude, exactitude, pertinence des fonctions | `NAT_FUNCTIONAL_TESTING` | Oui | Squash, Playwright |
| `performance` | Test de performance | Temps de réponse, débit, consommation des ressources, capacité (charge, stress, endurance) | `NAT_PERFORMANCE_TESTING` | Non (campagne dédiée) | Gatling, JMeter, k6 |
| `securite` | Test de sécurité | Confidentialité, intégrité, authentification, contrôle d'accès, traçabilité | `NAT_SECURITY_TESTING` | En partie (contrôles fonctionnels de sécurité) | Playwright ; OWASP ZAP, Burp uniquement avec autorisation écrite |
| `utilisabilite` | Test d'utilisabilité | Facilité d'apprentissage et d'usage, protection contre les erreurs, accessibilité | `NAT_USER_TESTING` | En partie (axe, contrôles d'accessibilité) | Checklists RGAA / WCAG, axe |
| `compatibilite` | Test de compatibilité | Coexistence, interopérabilité ; navigateurs et appareils | `NAT_NON_FUNCTIONAL_TESTING` | Oui (projets Playwright multi-navigateurs) | Playwright, BrowserStack |
| `fiabilite` | Test de fiabilité | Maturité, disponibilité, tolérance aux pannes, récupération | `NAT_NON_FUNCTIONAL_TESTING` | Non | Tests d'endurance, scénarios de reprise |
| `maintenabilite` | Test de maintenabilité | Modularité, analysabilité, modifiabilité | `NAT_NON_FUNCTIONAL_TESTING` | Non | Revue, analyse statique (équipe de développement) |
| `portabilite` | Test de portabilité | Adaptabilité, installabilité, remplaçabilité | `NAT_NON_FUNCTIONAL_TESTING` | Non | Installation sur les environnements cibles |

Nature du cas (`type`), indépendante du type de test : `nominal` (comportement attendu), `negatif` (entrée ou situation refusée), `limite` (borne d'une partition).

Les cas dont le type de test n'est pas automatisable avec Playwright (performance, fiabilité, maintenabilité, portabilité) restent dans Squash et le cahier, mais `outils/generer_specs.py` ne produit pas de spec Playwright pour eux : ils relèvent de la campagne dédiée décrite dans la stratégie.

## 3. Stratégie de types de tests (`strategie_tests`)

L'analyse ne s'arrête pas aux cas fonctionnels : elle dit **quels types de tests effectuer** sur le projet. Le JSON contient une entrée par type examiné, et **les 10 types doivent tous être examinés** (le contrôle refuse un oubli) :

- les 8 types du §2 ;
- les tests liés aux changements (CTFL v4.0 §2.2.3) : `confirmation` (re-test d'une anomalie corrigée) et `regression`.

Pour chaque type, une décision :

| `decision` | Quand | Obligatoire |
|---|---|---|
| `retenu` | Le CDC contient une exigence de ce type, ou le type est une pratique standard de la recette (fonctionnel, confirmation, régression) | `objectif`, `niveau`, `approche`, `justification` (source CDC) |
| `a-confirmer` | Le type est pertinent pour ce produit mais le CDC ne donne pas de quoi le tester (seuil, navigateurs, référentiel) | `justification` et au moins une question dans `ambiguites.md` |
| `non-retenu` | Aucune exigence et pas de risque identifié, ou hors de portée de l'équipe de test | `justification` (la raison de l'exclusion) |

Champs : `niveau` de test (CTFL v4.0 §2.2.1 : `composant`, `integration-composants`, `systeme`, `integration-systemes`, `acceptation`) ; `approche` : `cas` (cas de tests de ce fichier), `campagne-dediee` (performance, sécurité intrusive…), `checklist`, `exploratoire` ; `exigences`, `cas`, `questions` (identifiants) ; `outil` et `priorite` (`haute`, `moyenne`, `basse`), facultatifs.

Règle d'honnêteté : un type n'est jamais `retenu` sur la base d'un seuil ou d'une contrainte inventés. « L'application doit être rapide » donne un type `performance` **à confirmer**, avec la question « quels temps de réponse, pour quelles pages, sous quelle charge ? ». Les tests intrusifs (injection, force brute, scan de vulnérabilités) ne sont proposés qu'en campagne dédiée, sous réserve d'une autorisation écrite et d'un environnement dédié (règle 8 de `AGENTS.md`).

## 4. Ce que vérifie `outils/controle.py`

Erreurs :
- `technique` hors du tableau du §1 ; `type_test` hors du tableau du §2 ; `type` différent de `nominal`, `negatif`, `limite` ;
- `nature` incohérente avec `type_test` ;
- `strategie_tests` absente, type non examiné parmi les 10, décision invalide, justification manquante, champs obligatoires d'un type retenu absents, type « à confirmer » sans question, référence inconnue.

Avertissements :
- cas `limite` conçu sans `valeurs-limites` ;
- exigence `CAT_PERFORMANCE`, `CAT_SECURITY` ou `CAT_ERGONOMIC` absente des types retenus ou à confirmer correspondants ;
- cas non fonctionnel non rattaché à la stratégie ;
- campagne dédiée sans question (seuils, environnement, outillage).
