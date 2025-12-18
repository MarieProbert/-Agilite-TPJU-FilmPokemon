from behave import given, when, then
from film import Film
from realisateur import Realisateur

@given('un réalisateur nommé "{nom_real}"')
def step_impl(context, nom_real):
    context.real = Realisateur(nom_real)

@given('un film intitulé "{titre_film}"')
def step_impl(context, titre_film):
    context.film = Film()

@when('j\'ajoute le film "{titre_film}" à la liste du réalisateur "{nom_real}"')
def step_impl(context, titre_film, nom_real):
    context.real.ajouter_film(context.film)

@then('le film doit apparaître dans la liste des films de "{nom_real}"')
def step_impl(context, nom_real):
    films_du_real = context.real.get_films()
    assert context.film in films_du_real, f"Erreur : Le film n'est pas dans la liste de {nom_real}"

@then('le réalisateur associé au film doit être "{nom_real}"')
def step_impl(context, nom_real):
    real_associe = context.film.get_realisateur()
    assert real_associe == context.real, "Erreur : Le lien inverse vers le réalisateur n'a pas été mis à jour"