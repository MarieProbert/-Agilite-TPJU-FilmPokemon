from behave import given, when, then
from Models.pokemon_acteur_adapter import PokemonAdapter

@given('sa capacité spéciale est "{capacite}"')
def step_impl_set_capacite(context, capacite):
    # On configure le Pokémon brut
    context.pokemon.capacite = capacite

@given('le Pokémon est casté dans le film "{titre_film}"')
def step_impl_casting_contextualise(context, titre_film):
    # Réutilisation de la logique de casting
    from Models.film import Film
    context.film = Film()
    context.film.titre = titre_film
    
    # On crée l'adapter pour lier le tout
    context.acteur = PokemonAdapter(context.pokemon)
    context.acteur.set_film(context.film)

@when('le Pokémon joue sa scène')
def step_impl_action(context):
    # Si l'acteur n'a pas été créé dans le Given précédent (cas sans film), on le crée
    if not hasattr(context, 'acteur'):
        context.acteur = PokemonAdapter(context.pokemon)
        
    context.resultat_reel = context.acteur.jouer_scene()

@then('l\'action produite doit être "{phrase_attendue}"')
def step_impl_verification(context, phrase_attendue):
    assert context.resultat_reel == phrase_attendue, \
        f"Erreur : \nAttendu : {phrase_attendue}\nObtenu  : {context.resultat_reel}"