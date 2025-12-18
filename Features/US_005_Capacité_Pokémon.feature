Feature: US_005 Performance d'acteur contextualisée

  En tant que Réalisateur
  Je veux que le Pokémon joue sa scène en utilisant sa capacité spéciale
  Afin de générer une action spécifique liée au film en cours

  Scenario Outline: Un Pokémon joue sa scène dans un film
    Given un Pokémon nommé "<nom>"
    And sa capacité spéciale est "<capacite>"
    And le Pokémon est casté dans le film "<titre_film>"
    When le Pokémon joue sa scène
    Then l'action produite doit être "<nom> joue dans <titre_film> et utilise <capacite>"

    Examples:
      | nom       | capacite      | titre_film            |
      | Pikachu   | Tonnerre      | Détective Pikachu     |
      | Dracaufeu | Lance-Flammes | Le Seigneur des Ailes |
      | Rondoudou | Berceuse      | Insomnia              |