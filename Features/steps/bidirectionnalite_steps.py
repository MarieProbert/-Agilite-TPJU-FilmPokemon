from behave import given, when, then
from Models.film import Film
from Models.realisateur import Realisateur

@given('un réalisateur nommé "{nom_real}"')
def step_impl_given_real(context, nom_real):
    context.real = Realisateur(nom_real)

@given('un film avec un realisateur')
def step_impl_given_film(context):
    context.film = Film()

@when('j\'ajoute le film à la liste du réalisateur "{nom_real}"')
def step_impl_when_ajoute(context, nom_real):
    if not hasattr(context, 'film'):
        context.film = Film()
    context.real.ajouter_film(context.film)

@then('le film doit apparaître dans la liste des films de "{nom_real}"')
def step_impl_then_liste(context, nom_real):
    films_du_real = context.real.get_films()
    assert context.film in films_du_real

@then('le réalisateur associé au film doit être "{nom_real}"')
def step_impl_then_inverse(context, nom_real):
    real_associe = context.film.get_realisateur() 
    assert real_associe == context.real