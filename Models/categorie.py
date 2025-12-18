class Categorie:
    def __init__(self):
        self._nom = None

    def get_nom(self) -> str:
        return self._nom

    def set_nom(self, nom: str):
        self._nom = nom