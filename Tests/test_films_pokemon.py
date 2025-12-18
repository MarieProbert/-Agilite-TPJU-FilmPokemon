import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from Models.pokemon import Pokemon
from Models.pokeball import Pokeball
from Models.dresseur import Dresseur
from Models.realisateur import Realisateur
from Models.film import Film
from Models.acteur import Acteur
from Models.acteur_factory import ActeurFactory
from Models.pokemon_acteur_adapter import PokemonAdapter

class TestCoverageComplementaire(unittest.TestCase):

    def setUp(self):
        self.pikachu = Pokemon("Pikachu", "Electrik", None)
        self.pokeball = Pokeball(prix=200)

    # --- Section Pokemon ---
    def test_utiliser_capacite_avec_succes(self):
        # Couvre la branche 'if self.capacite is not None'
        pika = Pokemon("Pika", "Electrik", None, capacite="Tonnerre")
        pika.capacite = "Tonnerre" # S'assurer que la capacité est là
        self.assertEqual(pika.utiliser_capacite(), "Pika utilise Tonnerre!")

    def test_utiliser_capacite_sans_capacite(self):
        # Couvre la branche 'else'
        self.assertEqual(self.pikachu.utiliser_capacite(), "Ce Pokémon n'a pas de capacité assignée.")

    def test_pokemon_init_with_pokeball(self):
        # Couvre l'assignation automatique de la pokeball dans __init__
        pball = Pokeball(100)
        pika = Pokemon("Pika", "Electrik", None, pokeball=pball)
        self.assertEqual(pika.pokeball, pball)
        self.assertEqual(pball.pokemon, pika)

    # --- Section Pokeball ---
    def test_afficher_type_pokemon_vide(self):
        # Couvre le cas 'if self.pokemon is None'
        pball = Pokeball(100)
        self.assertEqual(pball.afficher_type_pokemon(), "Cette Pokeball est vide. Aucun type à afficher.")

    def test_afficher_type_un_seul_type(self):
        # Couvre la branche 'elif t1'
        pball = Pokeball(100)
        pika = Pokemon("Pika", "Electrik", None)
        pball.capturer_pokemon(pika)
        self.assertEqual(pball.afficher_type_pokemon(), "De type Electrik.")

    def test_capturer_pokemon_erreurs(self):
        # Couvre les exceptions levées dans capturer_pokemon
        pball1 = Pokeball(100)
        pball2 = Pokeball(200)
        pika = Pokemon("Pika", "Electrik", None)
        
        pball1.capturer_pokemon(pika)
        
        # Cas 1: Pokeball déjà occupée
        with self.assertRaises(Exception) as context:
            pball1.capturer_pokemon(Pokemon("Salameche", "Feu", None))
        self.assertTrue("La Pokeball contient déjà un Pokémon." in str(context.exception))
        
        # Cas 2: Pokémon déjà capturé
        with self.assertRaises(Exception) as context:
            pball2.capturer_pokemon(pika)
        self.assertTrue("Le Pokémon est déjà dans une Pokeball." in str(context.exception))

    # --- Section Dresseur ---
    def test_liberer_pokemon_vide(self):
        # Couvre le cas où on essaie de libérer une pokeball vide (ne fait rien)
        dresseur = Dresseur("Sacha")
        pball = Pokeball(100)
        dresseur.liberer_pokemon(pball) # Ne doit pas planter
        self.assertIsNone(pball.pokemon)

    # --- Section Realisateur & Film ---
    def test_realisateur_gestion_films(self):
        # Couvre ajouter_film et le calcul des stats
        spielberg = Realisateur("Spielberg")
        f1 = Film()
        f1.set_duree(120)
        f2 = Film()
        f2.set_duree(90)
        
        spielberg.ajouter_film(f1)
        spielberg.ajouter_film(f1) # Teste le 'if film not in self._films'
        spielberg.ajouter_film(f2)
        
        self.assertEqual(len(spielberg.get_films()), 2)
        self.assertEqual(spielberg.calcul_stats(), 210)
        self.assertIn("210 min", spielberg.afficher_stats())

    # --- Section Adapter & Factory ---
    def test_PokemonAdapter(self):
        # Teste l'adapter spécifique
        pika = Pokemon("Pikachu", "Electrik", None, capacite="Eclair")
        adapter = PokemonAdapter(pika)
        # Le nom dans l'adapter est le nom de la classe 'Pokemon'
        self.assertEqual(adapter.get_nom(), "Pokemon")
        self.assertEqual(adapter.jouer_scene(), "Pikachu utilise Eclair!")

    def test_acteur_factory_humain(self):
        acteur = ActeurFactory.creer_acteur("humain", "Tom Hanks", "Bonjour", Film())
        self.assertIsInstance(acteur, Acteur)
        self.assertEqual(acteur.jouer_scene(), "Bonjour")

    def test_acteur_factory_erreur(self):
        # Couvre l'exception du type source inconnu
        with self.assertRaises(ValueError):
            ActeurFactory.creer_acteur("alien", "Zog", "Gloup")

if __name__ == '__main__':
    unittest.main()