from behave import given, when, then
from Models.pokemon import Pokemon
from Models.pokeball import Pokeball


@given('un Pokemon de types {type1} et {type2}')
def step_given_pokemon_types(context, type1, type2):
    context.pokemon = Pokemon("TestPokemon", type1, type2)

@given('une Pokéball contenant ce Pokémon')
def step_given_pokeball_with_pokemon(context):
    context.pokeball = Pokeball(600, context.pokemon)
    context.pokemon.pokeball = context.pokeball

@when("J'affiche le type du Pokémon via la Pokéball")
def step_when_afficher_type(context):
    context.result = context.pokeball.afficher_type_pokemon()

@then('afficher le message "De types {type1} et {type2}."')
def step_then_afficher_types(context, type1, type2):
    expected = f"De types {type1} et {type2}."
    assert context.result == expected

@given('une Pokéball sans Pokémon')
def step_given_empty_pokeball(context):
    context.pokeball = Pokeball(600)

@then('afficher le message "Cette Pokeball est vide. Aucun type à afficher."')
def step_then_afficher_vide(context):
    assert context.result == "Cette Pokeball est vide. Aucun type à afficher."
