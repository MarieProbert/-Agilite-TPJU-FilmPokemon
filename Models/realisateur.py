from typing import List
from film import Film

class Realisateur:
    def __init__(self, nom: str):
        self._nom = nom
        self._films: List[Film] = []

    def get_nom(self) -> str:
        return self._nom

    def set_nom(self, nom: str):
        self._nom = nom

    def get_films(self):
        return self._films

    def ajouter_film(self, film: Film):
        if film not in self._films:
            self._films.append(film)
            film.set_realisateur(self)

    def afficher_stats(self):
        t = self.calcul_stats()
        res = f"Le réalisateur {self._nom} a produit {len(self._films)} films pour une durée de {t} min."
        return res

    def calcul_stats(self):
        t = 0
        for f in self._films:
            t += f.get_duree()
        return t