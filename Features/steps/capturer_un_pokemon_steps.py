from behave import given, when, then
from Models.pokemon import Pokemon
from Models.pokeball import Pokeball

@given('un Pokémon sauvage')
def step_given_pokemon_sauvage(context):
    context.pokemon = Pokemon("TestPokemon", "Feu", "Spectre")

@given('une Pokéball vide')
def step_given_pokeball_vide(context):
    context.pokeball = Pokeball(600)

@when('je mets le Pokémon dans la Pokéball')
def step_when_mettre_pokemon(context):
    context.pokeball.pokemon = context.pokemon
    context.pokemon.pokeball = context.pokeball

@then('la Pokéball doit contenir le Pokémon')
def step_then_pokeball_contient(context):
    assert context.pokeball.pokemon == context.pokemon

@then('le Pokémon doit référencer la Pokéball')
def step_then_pokemon_reference(context):
    assert context.pokemon.pokeball == context.pokeball
