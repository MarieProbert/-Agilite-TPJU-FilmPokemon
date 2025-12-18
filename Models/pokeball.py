class Pokeball:
    def __init__(self, prix, pokemon=None, dresseur=None):
        self._prix = prix
        self._pokemon = pokemon
        if pokemon is not None:
                pokemon.pokeball = self
        if dresseur is not None:
                self._dresseur = dresseur
        else:
            self._dresseur = None

    def afficher_type_pokemon(self):
        if self._pokemon is None:
            return "Cette Pokeball est vide. Aucun type à afficher."

        t1 = self._pokemon.get_type1()
        t2 = self._pokemon.get_type2()

        if t1 and t2:
            return f"De types {t1} et {t2}."
        elif t1:
            return f"De type {t1}."
        else:
            return "Le Pokémon dans cette Pokeball n'a pas de type défini."
        
    def capturer_pokemon(self, pokemon):
        if self._pokemon is not None:
            raise Exception("La Pokeball contient déjà un Pokémon.")
        if pokemon.pokeball is not None:
            raise Exception("Le Pokémon est déjà dans une Pokeball.")
        self._pokemon = pokemon
        pokemon.pokeball = self
        return True