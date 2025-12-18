from behave import given
from Models.pokemon import Pokemon
from Models.film import Film

@given('un Pokémon nommé "{nom}"')
def step_impl_common_creation_pokemon(context, nom):
    # On crée le Pokémon "brut"
    context.pokemon = Pokemon(nom, "Normal", "Normal")

@given('un film intitulé "{titre_film}"')
def step_impl_common_film(context, titre_film):
    context.film = Film()
    # Ajout dynamique de l'attribut titre (car absent de votre classe Film fournie)
    context.film.titre = titre_film