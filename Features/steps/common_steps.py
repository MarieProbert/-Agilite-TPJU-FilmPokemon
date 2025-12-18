from behave import given
from Models.pokemon import Pokemon
from Models.film import Film

@given('un Pokémon nommé "{nom}"')
def step_impl_common_creation_pokemon(context, nom):
    context.pokemon = Pokemon(nom, "Normal", "Normal")

@given('un film intitulé')
def step_impl_common_film(context):
    context.film = Film()
