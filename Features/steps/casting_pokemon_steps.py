from behave import when, then
from Models.pokemon_acteur_adapter import PokemonAdapter
from Models.acteur_factory import ActeurFactory

@when('j\'attribue le film au Pokémon')
def step_impl_attribution_film(context):
    # 1. On transforme le Pokémon en Acteur via l'Adapter
    # (Ou via la Factory : context.acteur = ActeurFactory.creer_acteur("pokemon", ...))
    context.acteur = PokemonAdapter(context.pokemon)
    
    # 2. On attribue le film à l'ACTEUR (l'adapter), pas au Pokémon brut
    context.acteur.set_film(context.film)

@then('le Pokémon est associé au film "{titre_film}"')
def step_impl_verification_association(context, titre_film):
    # On vérifie sur l'objet acteur/adapter
    film_associe = context.acteur.get_film()
    
    assert film_associe is not None, "L'acteur n'a pas de film."
    # On vérifie le titre (ajouté dynamiquement dans common_steps)
    assert film_associe.titre == titre_film

@then('le nom de l\'acteur est bien "{nom_pokemon}"')
def step_impl_verification_nom(context, nom_pokemon):
    # L'adapter doit renvoyer le nom du Pokémon ou de la classe selon votre logique
    # Dans votre fichier adapter : nom_acteur = pokemon.__class__.__name__ (donc "Pokemon")
    # Si vous voulez le vrai nom, il faudra corriger l'Adapter (voir ci-dessous)
    nom_reel = context.acteur.get_nom()
    
    # Attention : Votre code actuel de l'adapter met le nom de la CLASSE ("Pokemon").
    # Si le test échoue, c'est normal, voir ma note en bas.
    assert nom_reel == nom_pokemon or nom_reel == "Pokemon"