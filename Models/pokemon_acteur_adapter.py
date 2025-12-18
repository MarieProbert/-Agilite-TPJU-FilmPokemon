from Models.acteur import Acteur

class PokemonAdapter(Acteur):
    def __init__(self, pokemon):
        # CORRECTION : On prend le nom du Pokémon (ex: "Pikachu"), pas le nom de la classe
        super().__init__(pokemon.nom) 
        self.pokemon = pokemon

    def jouer_scene(self):
        # On récupère le résultat brut ("Pikachu utilise Tonnerre!")
        action_base = self.pokemon.utiliser_capacite()
        
        # On récupère le film via la classe mère Acteur
        film = self.get_film()
        titre_film = film.titre if film and hasattr(film, 'titre') else "un film inconnu"

        # On reformate pour coller à l'US : "Pikachu joue dans X et utilise Y"
        # Note : On doit parser un peu car utiliser_capacite renvoie déjà une phrase
        capacite = self.pokemon.capacite if self.pokemon.capacite else "rien"
        
        return f"{self.pokemon.nom} joue dans {titre_film} et utilise {capacite}"