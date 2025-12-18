class Pokemon:
    def __init__(self, nom, type1, type2, pokeball=None):
        self.type1 = type1
        self.type2 = type2
        self.pokeball = pokeball
        self.nom = nom
        if pokeball is not None:
            self.pokeball.pokemon = self

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
    