from Models.film import Film

class Acteur:
    def __init__(self, nom: str):
        self._nom = nom
        self._film = None
        self._dialogue = None

    def get_nom(self) -> str:
        return self._nom

    def set_nom(self, nom: str):
        self._nom = nom

    def get_film(self) -> Film:
        return self._film

    def set_film(self, film: Film):
        self._film = film

    def jouer_scene(self):
        return self._dialogue
    
    def set_dialogue(self, dialogue: str):
        self._dialogue = dialogue
    