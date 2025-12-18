import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from Models.pokemon import Pokemon
from Models.pokeball import Pokeball
from Models.dresseur import Dresseur

class TestPokemon(unittest.TestCase):
    """Traduction de PokemonTest.java"""

    def setUp(self):
        # Équivalent des engagements (@BeforeEach)
        self.f_valeur1 = 2.0
        self.f_valeur2 = 3.0

    def test_get_type1(self):
        dracaufeu = Pokemon("Dracaufeu", "Feu", "Vol")
        self.assertEqual("Feu", dracaufeu.get_type1())

    def test_get_type2(self):
        dracaufeu = Pokemon("Dracaufeu", "Feu", "Vol")
        self.assertEqual("Vol", dracaufeu.get_type2())

    def test_set_type1(self):
        dracaufeu = Pokemon("Dracaufeu", "Eau", "Vol")
        dracaufeu.set_type1("Feu")
        self.assertEqual("Feu", dracaufeu.get_type1())

    def test_set_type2(self):
        dracaufeu = Pokemon("Dracaufeu", "Feu", "Spectre")
        dracaufeu.set_type2("Vol")
        self.assertEqual("Vol", dracaufeu.get_type2())

    def test_get_pokeball(self):
        funecire = Pokemon("Funecire", "Feu", "Spectre")
        super_ball = Pokeball(600)
        super_ball.capturer_pokemon(funecire)
        self.assertEqual(super_ball, funecire.get_pokeball())


class TestPokeball(unittest.TestCase):
    """Traduction de PokeballTest.java"""

    def setUp(self):
        # Équivalent des engagements (@BeforeEach)
        self.funecire = Pokemon("Funecire", "Feu", "Spectre")
        self.super_ball = Pokeball(600)
        self.super_ball.capturer_pokemon(self.funecire)

    def test_afficher_pokeball(self):
        # Vérifie le message renvoyé par la pokéball
        attendu = "De types Feu et Spectre."
        self.assertEqual(attendu, self.super_ball.afficher_type_pokemon())

    def test_capturer_pokemon(self):
        pikachu = Pokemon("Pikachu", "Electrik", "Normal")
        pokeball = Pokeball(300)
        pokeball.capturer_pokemon(pikachu)
        self.assertEqual(pikachu, pokeball.pokemon)
        self.assertEqual(pokeball, pikachu.pokeball)

class TestDresseur(unittest.TestCase):
    def setUp(self):
        self.dresseur = Dresseur("Sacha")
        self.pokemon = Pokemon("Pikachu", "Électrik", None)
        self.pokeball = Pokeball(prix=200)

    def test_modification_nom(self):
        self.dresseur.nom = "Régis"
        self.assertEqual(self.dresseur.nom, "Régis")

    def test_get_nom(self):
        self.assertEqual(self.dresseur.get_nom(), "Sacha")

    def test_get_inventaire(self):
        self.dresseur.ajouter_pokeball(self.pokeball)
        self.assertIn(self.pokeball, self.dresseur.get_inventaire())
        self.assertEqual(len(self.dresseur.get_inventaire()), 1)

    def test_nettoyer_lien_pokemon_pokeball(self):
        self.dresseur.capturer_pokemon(self.pokemon, self.pokeball)
        self.dresseur.nettoyer_lien_pokemon_pokeball(self.pokeball)
        self.assertIsNone(self.pokeball.pokemon)
        self.assertIsNone(self.pokemon.pokeball)

    def test_ajouter_pokeball(self):
        self.dresseur.ajouter_pokeball(self.pokeball)
        self.assertIn(self.pokeball, self.dresseur.inventaire)
        self.assertEqual(len(self.dresseur.inventaire), 1)

    def test_capturer_pokemon_succes(self):
        self.dresseur.capturer_pokemon(self.pokemon, self.pokeball)
        self.assertEqual(self.pokeball.pokemon, self.pokemon)
        self.assertEqual(self.pokemon.pokeball, self.pokeball)

    def test_liberer_pokemon(self):
        self.dresseur.capturer_pokemon(self.pokemon, self.pokeball)
        
        self.dresseur.liberer_pokemon(self.pokeball)
        self.assertIsNone(self.pokeball.pokemon)
        self.assertIsNone(self.pokemon.pokeball)

if __name__ == '__main__':
    unittest.main()