@tag
Feature: US_001 Gestion complète des informations d'un film
  En tant que Gestionnaire de films
  Je veux créer un film et modifier tous ses attributs (catégorie, durée, date de sortie)
  Afin de générer une description précise et complète pour mon catalogue

  Scenario Outline: Mise à jour et vérification de tous les détails du film
    Given un nouveau film est créé
    And je définis la catégorie sur "<categorie>"
    When je modifie la durée à <duree> minutes et la date de sortie à "<date>"
    Then la description finale doit être "<resultat>"

    Examples:
      | categorie       | duree | date       | resultat                                                                         |
      | Science-Fiction | 120   | 2023/10/25 | Je suis un film de catégorie Science-Fiction et de durée 120 sorti en 2023/10/25 |
      | Drame           | 95    | 1999/05/12 | Je suis un film de catégorie Drame et de durée 95 sorti en 1999/05/12            |