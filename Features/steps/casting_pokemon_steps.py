from behave import when, then
from Models.pokemon_acteur_adapter import PokemonAdapter
from Models.film import Film

@when("j'attribue le film au Pokémon")
def step_impl_attribution_film(context):
    # Sécurité : si 'un film' n'a pas été stocké correctement dans context.film
    if not hasattr(context, 'film'):
        context.film = Film()
    
    # Initialisation de l'adaptateur avec le pokemon du contexte
    context.acteur = PokemonAdapter(context.pokemon)
    # Association du film
    context.acteur.set_film(context.film)

@then("le Pokémon est associé à un film")
def step_impl_verification_association(context):
    # On récupère le film via l'adaptateur
    film_associe = context.acteur.get_film()
    
    assert film_associe is not None, "L'acteur n'a pas de film."
    assert film_associe == context.film

@then('le nom de l\'acteur est bien "{nom_pokemon}"')
def step_impl_verification_nom(context, nom_pokemon):
    # L'adapter récupère le nom depuis l'objet Pokemon source
    nom_reel = context.acteur.get_nom()
    
    # Vérification du nom
    assert nom_reel == nom_pokemon, f"Attendu: {nom_pokemon}, Reçu: {nom_reel}"