from Models.acteur import Acteur

class PokemonAdapter(Acteur):
    def __init__(self, pokemon):
        super().__init__(pokemon.get_nom()) 
        self._pokemon = pokemon

    def jouer_scene(self):
        action_base = self._pokemon.utiliser_capacite()
        
        film = self.get_film()
        capacite = self._pokemon.get_capacite() if self._pokemon.get_capacite() else "rien"
        
        return f"{self._pokemon.get_nom()} utilise {capacite}"