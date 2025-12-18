class Pokemon:
    def __init__(self, nom, type1, type2, pokeball=None, capacite=None):
        self.type1 = type1
        self.type2 = type2
        self.pokeball = pokeball
        self.nom = nom
        if capacite is not None:
            self.capacite = capacite
        else:
            self.capacite = None
        if pokeball is not None:
            self.pokeball.pokemon = self
        else:
            self.pokeball = None

    def get_type1(self):
        return self.type1
    
    def set_type1(self, new_type):
        self.type1 = new_type

    def get_type2(self):
        return self.type2

    def set_type2(self, new_type):
        self.type2 = new_type

    def get_pokeball(self):
        return self.pokeball
    
    def utiliser_capacite(self):
        if self.capacite is not None:
            return f"{self.nom} utilise {self.capacite}!"
        else:
            return "Ce Pokémon n'a pas de capacité assignée."
    