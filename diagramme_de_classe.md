---
config:
  layout: dagre
---
classDiagram
    class Pokemon {
        -nom: str
        -type1: str
        -type2: str
        -pokeball: Pokeball
        -capacite: str
        +get_type1(): str
        +set_type1(new_type: str)
        +get_type2(): str
        +set_type2(new_type: str)
        +get_pokeball(): Pokeball
        +utiliser_capacite(): str
    }

    class Film {
        -_duree: int
        -_date_sortie: str
        -_categorie: Categorie
        -_realisateur: Realisateur
        +get_duree(): int
        +set_duree(duree: int)
        +get_date_sortie(): str
        +set_date_sortie(date_sortie: str)
        +set_categorie(categorie: Categorie)
        +get_categorie(): Categorie
        +set_realisateur(realisateur: Realisateur)
        +get_realisateur(): Realisateur
        +description(): str
    }

    class Acteur {
        -_nom: str
        -_film: Film
        -_dialogue: str
        +get_nom(): str
        +set_nom(nom: str)
        +get_film(): Film
        +set_film(film: Film)
        +jouer_scene(): str
        +set_dialogue(dialogue: str)
    }

    class Realisateur {
        -_nom: str
        -_films: List~Film~
        +get_nom(): str
        +set_nom(nom: str)
        +get_films(): List~Film~
        +ajouter_film(film: Film)
        +afficher_stats(): str
        +calcul_stats(): int
    }

    class Categorie {
        -_nom: str
        +get_nom(): str
        +set_nom(nom: str)
    }

    class Dresseur {
        -nom: str
        -inventaire: List~Pokeball~
        +get_nom(): str
        +get_inventaire(): List~Pokeball~
        +ajouter_pokeball(pokeball: Pokeball)
        +capturer_pokemon(pokemon: Pokemon, pokeball: Pokeball)
        +liberer_pokemon(pokeball: Pokeball)
        +nettoyer_lien_pokemon_pokeball(pokeball: Pokeball)
    }

    class Pokeball {
        -prix: float
        -pokemon: Pokemon
        -dresseur: Dresseur
        +afficher_type_pokemon(): str
        +capturer_pokemon(pokemon: Pokemon): bool
    }

    class PokemonAdapter {
        -pokemon: Pokemon
        +jouer_scene(): str
    }

    class ActeurFactory {
        +creer_acteur(type_source: str, nom: str, dialogue: str, film: Film)* Acteur
    }
    Film --> Categorie : possède une
    Film --> Realisateur : est réalisé par
    Realisateur --> Film : réalise
    Acteur --> Film : joue dnas
    Pokemon --> Pokeball : est contenu dans
    Pokeball --> Pokemon : contient
    Dresseur --> Pokeball : possède
    Pokeball --> Dresseur : appartient à
    PokemonAdapter --> Pokemon : enveloppe
    ActeurFactory ..> Acteur : crée
    ActeurFactory ..> PokemonAdapter : crée
    PokemonAdapter --|> Acteur : adapte
```