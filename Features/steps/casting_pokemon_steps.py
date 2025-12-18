from behave import when, then
from Models.pokemon_acteur_adapter import PokemonAdapter
from Models.film import Film

@when("j'attribue le film au Pokémon")
def step_impl_attribution_film(context):
    if not hasattr(context, 'film'):
        context.film = Film()
    
    context.acteur = PokemonAdapter(context.pokemon)
    context.acteur.set_film(context.film)

@then("le Pokémon est associé à un film")
def step_impl_verification_association(context):
    film_associe = context.acteur.get_film()
    
    assert film_associe is not None, "L'acteur n'a pas de film."
    assert film_associe == context.film

@then('le nom de l\'acteur est bien "{nom_pokemon}"')
def step_impl_verification_nom(context, nom_pokemon):
    nom_reel = context.acteur.get_nom()
    
    assert nom_reel == nom_pokemon, f"Attendu: {nom_pokemon}, Reçu: {nom_reel}"