@tag
Feature: US003 : Gestion de la relation bidirectionnelle
  En tant que Gestionnaire de catalogue
  Je veux que l'affectation d'un film à un réalisateur soit automatique dans les deux sens
  Afin de garantir l'intégrité des données sans double saisie

  Scenario Outline: Ajout d'un film à un réalisateur et vérification des liens
    Given un réalisateur nommé "<nom_real>" 
    And un film avec un realisateur
    When j'ajoute le film à la liste du réalisateur "<nom_real>"
    Then le film doit apparaître dans la liste des films de "<nom_real>" And le réalisateur associé au film doit être "<nom_real>"

    Examples:
      | nom_real          |
      | Quentin Tarantino |
      | Christopher Nolan |
      | Stanley Kubrick   |