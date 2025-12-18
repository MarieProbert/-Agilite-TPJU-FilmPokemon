import unittest
from film import Film, Categorie
from realisateur import Realisateur

class TestFilm(unittest.TestCase):


    def setUp(self):
        self.kill_bill = Film()
        self.action = Categorie()
        self.real = Realisateur("Quentin Tarantino")
        
        self.action.set_nom("Action")
        self.kill_bill.set_categorie(self.action)

    def tearDown(self):
        pass

    def test_set_duree(self):
        self.kill_bill.set_duree(111)
        self.assertEqual(111, self.kill_bill.get_duree())

    def test_set_realisateur(self):
        self.assertEqual("Quentin Tarantino", self.real.get_nom())

    def test_liste_films_vide(self):
        nouveau_real = Realisateur("Inconnu")
        self.assertEqual(nouveau_real.afficher_stats(), "Le réalisateur Inconnu a produit 0 films pour une durée de 0 min.")

    def test_set_date_sortie(self):
        self.kill_bill.set_date_sortie("2003/10/29")
        self.assertEqual("2003/10/29", self.kill_bill.get_date_sortie())

    def test_description_film(self):
        self.action.set_nom("Thriller")
        attendu = "Je suis un film de catégorie Thriller et de durée 0 sorti en 2001/01/01"
        self.assertEqual(attendu, self.kill_bill.description())

if __name__ == '__main__':
    unittest.main()