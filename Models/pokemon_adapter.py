from Models.pokemon import Pokemon
from Models.film import Film

class PokemonAdapter:
    def __init__(self, pokemon: Pokemon):
        self._pokemon = pokemon
        self._film = None
        self._dialogue = None

    def get_nom(self) -> str:
        return self._pokemon.nom

    def set_nom(self, nom: str):
        self._pokemon.nom = nom

    def get_film(self) -> Film:
        return self._film

    def set_nom(self, film: Film):
        self._film = film

    def jouer_scene(self):
        # On peut faire parler le Pokémon ou utiliser sa capacité comme "scène"
        if self._dialogue:
            return f"{self._pokemon.nom} dit : {self._dialogue}"
        return self._pokemon.utiliser_capacite()

    def set_dialogue(self, dialogue: str):
        self._dialogue = dialogue
