from categorie import Categorie

class Film:
    def __init__(self):
        self._duree = 0
        self._date_sortie = "2001/01/01"
        self._categorie = None 
        self._realisateur = None

    def get_duree(self) -> int:
        return self._duree

    def set_duree(self, duree: int):
        self._duree = duree

    def get_date_sortie(self) -> str:
        return self._date_sortie

    def set_date_sortie(self, date_sortie: str):
        self._date_sortie = date_sortie

    def set_categorie(self, categorie: Categorie):
        self._categorie = categorie

    def get_categorie(self) -> Categorie:
        return self._categorie
    
    def set_realisateur(self, realisateur: "Realisateur"):
        self._realisateur = realisateur

    def get_realisateur(self) -> "Realisateur":
        return self._realisateur

    def description(self) -> str:
        if self._categorie:
            nom_cat = self._categorie.get_nom()
        else:
            nom_cat = "Inconnue"
            
        return f"Je suis un film de catégorie {nom_cat} et de durée {self._duree} sorti en {self._date_sortie}"