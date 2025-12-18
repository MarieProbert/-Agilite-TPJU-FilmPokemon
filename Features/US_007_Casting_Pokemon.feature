Feature: US_004 Casting d'un Pokémon pour un film

  En tant que Agent de Casting
  Je veux attribuer un film à un Pokémon (considéré comme un Acteur)
  Pour l'enregistrer officiellement dans la distribution du projet

  Scenario Outline: Enregistrer un Pokémon dans un film
    Given un Pokémon nommé "<nom_pokemon>"
    And un film
    When j'attribue le film au Pokémon
    Then le Pokémon est associé à un film
    And le nom de l'acteur est bien "<nom_pokemon>"

    Examples:
      | nom_pokemon | 
      | Pikachu     |
      | Psykokwak   |
      | Mewtwo      |