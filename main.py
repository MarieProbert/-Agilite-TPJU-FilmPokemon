from Models.pokemon import Pokemon
from Models.pokeball import Pokeball

# Création des instances
funecire = Pokemon("Funecire", "Feu", "Spectre")
super_ball = Pokeball(600, funecire)

# On relie le pokemon à sa pokéball (relation bidirectionnelle)
funecire.pokeball = super_ball

# Utilisation
print(super_ball.afficher_type_pokemon()) 
# Affiche : De types Feu et Spectre.