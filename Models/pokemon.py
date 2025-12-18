class Pokemon:
    def __init__(self, nom, type1, type2, pokeball=None, capacite=None):
        self._type1 = type1
        self._type2 = type2
        self._pokeball = pokeball
        self._nom = nom
        if capacite is not None:
            self.capacite = capacite
        else:
            self.capacite = None
        if pokeball is not None:
            self._pokeball.pokemon = self
        else:
            self._pokeball = None

    def get_type1(self):
        return self._type1
    
    def set_type1(self, new_type):
        self._type1 = new_type

    def get_type2(self):
        return self._type2

    def set_type2(self, new_type):
        self._type2 = new_type

    def get_pokeball(self):
        return self._pokeball
    
    def set_pokeball(self, pokeball):
        self._pokeball = pokeball
        if pokeball is not None:
            pokeball.pokemon = self
    def get_nom(self):
        return self._nom
    def set_nom(self, nom):
        self._nom = nom
    
    def set_capacite(self, capacite):
        self.capacite = capacite
    
    def get_capacite(self):
        return self.capacite
    
    def utiliser_capacite(self):
        if self.capacite is not None:
            return f"{self._nom} utilise {self.capacite}!"
        else:
            return "Ce Pokémon n'a pas de capacité assignée."
    