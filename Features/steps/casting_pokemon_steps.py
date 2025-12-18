from behave import when, then
from Models.pokemon_acteur_adapter import PokemonAdapter
from Models.acteur_factory import ActeurFactory

@when('j\'attribue le film au Pokémon')
def step_impl_attribution_film(context):
    context.acteur = PokemonAdapter(context.pokemon)
    context.acteur.set_film(context.film)

@then('le Pokémon est associé au film "{titre_film}"')
def step_impl_verification_association(context, titre_film):
    film_associe = context.acteur.get_film()
    
    assert film_associe is not None, "L'acteur n'a pas de film."
    assert film_associe.titre == titre_film

@then('le nom de l\'acteur est bien "{nom_pokemon}"')
def step_impl_verification_nom(context, nom_pokemon):
    nom_reel = context.acteur.get_nom()
    
    assert nom_reel == nom_pokemon or nom_reel == "Pokemon"