Feature: US_001 Modifier la durée du film

  En tant que Administrateur
  Je veux modifier la durée d'un film
  Afin de corriger une erreur de saisie ou  mettre à jour

  Scenario Outline: Mise à jour de la durée
    Given un film
    When je modifie la durée en <duree>
    Then la durée du film est <duree>

    Examples:
      | duree |
      | 93    |
