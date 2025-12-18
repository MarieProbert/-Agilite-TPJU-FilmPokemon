Feature: Mettre un Pokémon dans une Pokéball

  En tant que dresseur Pokemon
  Je veux mettre un Pokémon sauvage dans une Pokéball
  Afin de le capturer

  Scenario: Mettre un Pokémon dans une Pokéball
    Given un Pokémon sauvage
    And une Pokéball vide
    When je mets le Pokémon dans la Pokéball
    Then la Pokéball doit contenir le Pokémon
    And le Pokémon doit référencer la Pokéball
