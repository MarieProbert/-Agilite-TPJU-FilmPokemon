from Models.acteur import Acteur
from Models.pokemon import Pokemon
from Models.pokemon_acteur_adapter import PokemonAdapter

class ActeurFactory:
    @staticmethod
    def creer_acteur(type_source, nom, dialogue, film=None): 
        
        if type_source == "humain":
            acteur = Acteur(nom)
            acteur.set_dialogue(dialogue)
            if film:
                acteur.set_film(film)
            return acteur
        elif type_source == "pokemon":
            

            pokemon = Pokemon(nom=nom, type1="Inconnu", type2="Inconnu", capacite=dialogue)
            acteur_adapter = PokemonAdapter(pokemon)
            if film:
                acteur_adapter.set_nom(film)
            return acteur_adapter
        
        else:
            raise ValueError("Type de source inconnu pour créer un acteur")