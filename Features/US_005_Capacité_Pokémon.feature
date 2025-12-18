Feature: US_005 Performance d'acteur Pokemon

  En tant que Réalisateur
  Je veux que le Pokémon joue sa scène en utilisant sa capacité spéciale
  Afin de générer une action spécifique liée au film en cours

  Scenario Outline: Un Pokémon joue sa scène dans un film
    Given un Pokémon nommé "<nom>"
    And sa capacité spéciale est "<capacite>"
    When le Pokémon joue sa scène
    Then l'action produite doit être "<nom> utilise <capacite>"

    Examples:
      | nom       | capacite      |
      | Pikachu   | Tonnerre      |
      | Dracaufeu | Lance-Flammes |
      | Rondoudou | Berceuse      |