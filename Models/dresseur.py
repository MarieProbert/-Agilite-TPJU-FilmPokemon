class Dresseur:
    def __init__(self, nom):
        self._nom = nom
        self._inventaire = []

    def get_nom(self):
        return self._nom

    def get_inventaire(self):
        return self._inventaire

    def ajouter_pokeball(self, pokeball):
        self._inventaire.append(pokeball)

    def capturer_pokemon(self, pokemon, pokeball):
        pokeball.capturer_pokemon(pokemon)

    def liberer_pokemon(self, pokeball):
        if pokeball.pokemon is not None:
            self.nettoyer_lien_pokemon_pokeball(pokeball)

    def nettoyer_lien_pokemon_pokeball(self, pokeball):
        pokeball.pokemon.pokeball = None
        pokeball.pokemon = None