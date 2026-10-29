# section.md

FEATURE
name        : "Gestion des sections"
application : "ANSUT"
module      : "Paramétrage > Sections"
tags        : [parametrage, section, smoke, regression]

DESCRIPTION

Valider qu'un utilisateur peut :

* créer une section (libellé, code, maintenancier)
* rechercher une section par filtre
* modifier une section existante
* supprimer une section

Navigation observée : menu latéral « Paramétrage » puis 1er onglet « Sections ».
Chaque opération est un scénario distinct ; dans le framework Selenium, les opérations
s'enchaînent dans une même session (création → recherche → modification → suppression).

DATA

base_url
value       : "{{BASE_URL}}"

session
value       : "{{ADMIN_LOGIN}} / {{ADMIN_PASSWORD}}"
secret      : true

section
label       : "Test"
code        : "TST"
maintainer  : "RAKALL"

section_updated
label       : "Test modify"
code        : "MODTEST"

filter
value       : "Test"
criterion   : "premier critère proposé par le panneau de filtre"
note        : "Selenium sélectionne la 1re option sans en lire le libellé"

SCENARIO Créer une section

tags : [parametrage, section, smoke]

GIVEN l'utilisateur est connecté et le menu Paramétrage est accessible

CONNECT url="{{BASE_URL}}"
  session=reuse

NAVIGATE menu="Paramétrage > Sections"

WHEN je crée une section

INTERACT click button="Ajouter"

INTERACT fill field="Libellé"
  value="Test"

INTERACT fill field="Code"
  value="TST"

INTERACT select field="Maintenancier"
  value="RAKALL"

INTERACT click button="Enregistrer"

THEN une confirmation de création s'affiche

ASSERT notification visible=true

AND je confirme la confirmation

INTERACT click button="Confirmer"

<!-- source Selenium : SectionTest.testCreateSection → CreateSection.GoToMenu()
     libellés de boutons non lus par Selenium (classes .btn-user, .btn-primary,
     .swal2-confirm) : à confirmer par inspection de l'application réelle -->

OBSERVABILITY

screenshot

on_success : true
on_failure : true

allure

attach_screenshots : true

logs

navigation : true
interaction : true
assertion : true

SCENARIO Rechercher une section par libellé

tags : [parametrage, section, regression]

GIVEN l'utilisateur est connecté et se trouve dans l'écran des sections

CONNECT url="{{BASE_URL}}"
  session=reuse

NAVIGATE menu="Paramétrage > Sections"

WHEN je recherche une section

INTERACT click button="Filtrer"

INTERACT select field="Critère de recherche"
  value="premier critère"

INTERACT fill field="Valeur recherchée"
  value="Test"

INTERACT click button="Appliquer le filtre"

THEN la liste affiche les sections correspondant au filtre

ASSERT element="tableau des sections"
  visible=true

BUT aucun message d'erreur ne s'affiche

ASSERT notification absent=true

<!-- source Selenium : SectionTest.testSearchSection → CreateSection.search()
     Selenium ne vérifiait aucun contenu de résultat (absence d'exception uniquement)
     libellé exact du critère non déterminé : 1re option cliquée sans lecture -->

OBSERVABILITY

screenshot

on_success : true
on_failure : true

allure

attach_screenshots : true

logs

navigation : true
interaction : true
assertion : true

SCENARIO Modifier une section existante

tags : [parametrage, section, regression]

GIVEN l'utilisateur est connecté et une section est affichée dans la liste

CONNECT url="{{BASE_URL}}"
  session=reuse

NAVIGATE menu="Paramétrage > Sections"

WHEN je modifie la première section de la liste

INTERACT click button="Modifier"

INTERACT fill field="Libellé"
  value="Test modify"

INTERACT fill field="Code"
  value="MODTEST"

INTERACT click button="Enregistrer"

THEN une confirmation de modification s'affiche

ASSERT notification visible=true

AND je confirme la confirmation

INTERACT click button="Confirmer"

<!-- source Selenium : SectionTest.testModifySection → CreateSection.Modify()
     ciblage historique : première ligne du tableau (index de colonne td[3]) -->

OBSERVABILITY

screenshot

on_success : true
on_failure : true

allure

attach_screenshots : true

logs

navigation : true
interaction : true
assertion : true

SCENARIO Supprimer une section

tags : [parametrage, section, regression]

GIVEN l'utilisateur est connecté et une section est affichée dans la liste

CONNECT url="{{BASE_URL}}"
  session=reuse

NAVIGATE menu="Paramétrage > Sections"

WHEN je supprime la première section de la liste

INTERACT click button="Supprimer"

THEN une première confirmation s'affiche

INTERACT click button="Confirmer"

AND une seconde confirmation s'affiche

INTERACT click button="Confirmer"

AND l'application demande une validation clavier

INTERACT press key="Enter"

AND une confirmation finale s'affiche

INTERACT click button="Confirmer"

THEN la suppression est confirmée

ASSERT notification visible=true

AND la section n'apparaît plus dans la liste

ASSERT element="ligne supprimée"
  absent=true

<!-- source Selenium : SectionTest.testDeleteSection → CreateSection.Deleted()
     enchaînement exact observé : swal2-confirm ×2, ENTER ×4 (pauses intercalées),
     swal2-confirm ×1
     AND "la section n'apparaît plus" : attente fonctionnelle, non vérifiée par Selenium -->

OBSERVABILITY

screenshot

on_success : true
on_failure : true

allure

attach_screenshots : true

logs

navigation : true
interaction : true
assertion : true

LOCATOR_RULES

priority

1 : data-testid
2 : id
3 : name
4 : role
5 : css
6 : xpath

avoid

- absolute xpath
- dynamic xpath
- positional selectors

particular

- popups de confirmation SweetAlert2 : historiquement classe `.swal2-confirm` ; préférer un rôle bouton après inspection
- liste déroulante maintenancier : widget `ng-select` (recherche par texte, puis option)
- navigation par onglet : l'ancien framework cible des index (`li[1]`) ; dans Playwright cibler le **libellé** de l'onglet « Sections »
- actions de ligne : ancien framework cible `tr[1]/td[3]/button[n]` (index de colonne propre à ce module) ; éviter tout sélecteur positionnel
- suppression : enchaînement multi-confirmations (2 confirmations, validation clavier, confirmation finale)
