from Models.acteur import Acteur

class pokemon_acteur_adapter(Acteur):
    def __init__(self, pokemon):
        nom_acteur = pokemon.__class__.__name__
        super().__init__(nom_acteur)
        self.pokemon = pokemon

    def jouer_scene(self):
        return self.pokemon.utiliser_capacite()