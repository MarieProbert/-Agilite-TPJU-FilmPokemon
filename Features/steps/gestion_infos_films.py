from behave import given, when, then
from film import Film
from categorie import Categorie

@given('un nouveau film est créé')
def step_impl_creation(context):
    context.mon_film = Film()

@given('je définis la catégorie sur "{nom_categorie}"')
def step_impl_categorie(context, nom_categorie):
    ma_categorie = Categorie()
    ma_categorie.set_nom(nom_categorie)
    context.mon_film.set_categorie(ma_categorie)

@when('je modifie la durée à {duree:d} minutes et la date de sortie à "{date_sortie}"')
def step_impl_modification(context, duree, date_sortie):
    context.mon_film.set_duree(duree)
    context.mon_film.set_date_sortie(date_sortie)

@then('la description finale doit être "{description_attendue}"')
def step_impl_verification(context, description_attendue):
    resultat_reel = context.mon_film.description()
    
    assert resultat_reel == description_attendue, \
        f"Erreur description: \nAttendu: {description_attendue}\nObtenu : {resultat_reel}"