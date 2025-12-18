Feature: Afficher le type d'un Pokémon dans une Pokéball

  En tant que dresseur Pokemon
  Je veux savoir les types d'un Pokémon via sa Pokéball
  Pour avoir des informations sur le Pokémon contenu

  Scenario Outline: Afficher les types d'un Pokémon dans une Pokéball
    Given un Pokemon de types <type1> et <type2>
    And une Pokéball contenant ce Pokémon
    When J'affiche le type du Pokémon via la Pokéball
    Then afficher le message "De types <type1> et <type2>."

    Examples:
      | type1 | type2   |
      | Feu   | Spectre |
      | Eau   | Vol     |
      | Plante| Poison  |

  Scenario: La Pokéball est vide
    Given une Pokéball sans Pokémon
    When J'affiche le type du Pokémon via la Pokéball
    Then afficher le message "Cette Pokeball est vide. Aucun type à afficher."