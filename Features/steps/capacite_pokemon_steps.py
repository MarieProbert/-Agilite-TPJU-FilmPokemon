from behave import given, when, then
from Models.pokemon_acteur_adapter import PokemonAdapter

@given('sa capacité spéciale est "{capacite}"')
def step_impl_set_capacite(context, capacite):
    context.pokemon.set_capacite(capacite)

@given('le Pokémon est casté dans un film ')
def step_impl_casting_contextualise(context):
    from Models.film import Film
    context.film = Film()
    
    context.acteur = PokemonAdapter(context.pokemon)
    context.acteur.set_film(context.film)

@when('le Pokémon joue sa scène')
def step_impl_action(context):
    if not hasattr(context, 'acteur'):
        context.acteur = PokemonAdapter(context.pokemon)
        
    context.resultat_reel = context.acteur.jouer_scene()

@then('l\'action produite doit être "{phrase_attendue}"')
def step_impl_verification(context, phrase_attendue):
    assert context.resultat_reel == phrase_attendue, \
        f"Erreur : \nAttendu : {phrase_attendue}\nObtenu  : {context.resultat_reel}"