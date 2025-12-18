import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from Models.pokemon import Pokemon
from Models.pokeball import Pokeball
from Models.dresseur import Dresseur
from Models.realisateur import Realisateur
from Models.film import Film
from Models.categorie import Categorie
from Models.acteur import Acteur
from Models.acteur_factory import ActeurFactory
from Models.pokemon_acteur_adapter import PokemonAdapter

class TestActeur(unittest.TestCase):
    def setUp(self):
        self.acteur = Acteur("Tom Cruise")

    def test_get_set_nom(self):
        self.acteur.set_nom("Brad Pitt")
        self.assertEqual(self.acteur.get_nom(), "Brad Pitt")

    def test_get_set_film(self):
        film = Film()
        self.acteur.set_film(film)
        self.assertEqual(self.acteur.get_film(), film)

    def test_set_dialogue(self): 
        self.acteur.set_dialogue("Maverick au rapport")
        self.assertEqual(self.acteur.jouer_scene(), "Maverick au rapport")

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.pika = Pokemon("Pikachu", "Electrik", None)

    def test_get_type1(self):
        dracaufeu = Pokemon("Dracaufeu", "Feu", "Vol")
        self.assertEqual("Feu", dracaufeu.get_type1())

    def test_get_type2(self):
        dracaufeu = Pokemon("Dracaufeu", "Feu", "Vol")
        self.assertEqual("Vol", dracaufeu.get_type2())

    def test_set_type1(self):
        self.pika.set_type1("Feu")
        self.assertEqual("Feu", self.pika.get_type1())

    def test_set_type2(self):
        self.pika.set_type2("Vol")
        self.assertEqual("Vol", self.pika.get_type2())

    def test_get_pokeball(self):
        super_ball = Pokeball(600)
        super_ball.capturer_pokemon(self.pika)
        self.assertEqual(super_ball, self.pika.get_pokeball())

    def test_utiliser_capacite_complet(self):
        self.assertEqual(self.pika.utiliser_capacite(), "Ce Pokémon n'a pas de capacité assignée.")
        self.pika.capacite = "Eclair"
        self.assertEqual(self.pika.utiliser_capacite(), "Pikachu utilise Eclair!")

class TestActeurFactory(unittest.TestCase):
    def test_creer_acteur_humain(self):
        acteur = ActeurFactory.creer_acteur("humain", "Tom Hanks", "Salut", Film())
        self.assertEqual(acteur.get_nom(), "Tom Hanks")

    def test_creer_acteur_pokemon_nom(self): 
        acteur_pika = ActeurFactory.creer_acteur("pokemon", "Pikachu", "Pika!")
        self.assertEqual(acteur_pika.get_nom(), "Pokemon")

    def test_creer_acteur_erreur(self):
        with self.assertRaises(ValueError):
            ActeurFactory.creer_acteur("alien", "Zog", "Gloup")

class TestPokeball(unittest.TestCase):
    def test_init_avec_objets(self): 
        pika = Pokemon("Pika", "Elec", None)
        pball = Pokeball(200, pika)
        self.assertEqual(pball.pokemon, pika)

    def test_afficher_types_complet(self): 
        pb = Pokeball(100)
        self.assertEqual(pb.afficher_type_pokemon(), "Cette Pokeball est vide. Aucun type à afficher.")
        
        p1 = Pokemon("P1", "Eau", None)
        pb.capturer_pokemon(p1)
        self.assertEqual(pb.afficher_type_pokemon(), "De type Eau.")
        
        p2 = Pokemon("P2", "Feu", "Vol")
        pb2 = Pokeball(100, p2)
        self.assertEqual(pb2.afficher_type_pokemon(), "De types Feu et Vol.")

class TestDresseur(unittest.TestCase):
    def setUp(self):
        self.dresseur = Dresseur("Sacha")
        self.pokemon = Pokemon("Pikachu", "Électrik", None)
        self.pokeball = Pokeball(prix=200)

    def test_gestion_pokemon(self):
        self.dresseur.capturer_pokemon(self.pokemon, self.pokeball)
        self.assertEqual(self.pokeball.pokemon, self.pokemon)
        self.dresseur.liberer_pokemon(self.pokeball)
        self.assertIsNone(self.pokeball.pokemon)

class TestFilm(unittest.TestCase):
    def setUp(self):
        self.film_test = Film()
        
        self.kill_bill = Film()
        self.action = Categorie()
        self.action.set_nom("Action")
        self.kill_bill.set_categorie(self.action)
        
        self.real = Realisateur("Quentin Tarantino")

    def test_description_sans_categorie(self):
        self.assertEqual(self.film_test.get_duree(), 0)
        self.assertIn("Inconnue", self.film_test.description())

    def test_description_film_avec_categorie(self):
        self.action.set_nom("Thriller")
        attendu = "Je suis un film de catégorie Thriller et de durée 0 sorti en 2001/01/01"
        self.assertEqual(attendu, self.kill_bill.description())

    def test_get_set_complet(self):
        self.film_test.set_duree(120)
        self.film_test.set_date_sortie("2023/10/25")
        self.assertEqual(self.film_test.get_duree(), 120)
        self.assertEqual(self.film_test.get_date_sortie(), "2023/10/25")

class TestRealisateur(unittest.TestCase):
    def setUp(self):
        self.real = Realisateur("Spielberg")

    def test_stats_realisateur(self):
        f1 = Film(); f1.set_duree(100)
        self.real.ajouter_film(f1)
        self.assertEqual(self.real.calcul_stats(), 100)
        self.assertIn("100 min", self.real.afficher_stats())

if __name__ == '__main__':
    unittest.main()