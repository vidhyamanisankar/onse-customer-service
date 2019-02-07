Feature: Update an existing customer on id
  As a service I want to update an existing customer's details.

  Scenario: Update surname
    Given customer "Nicole Forsgren" with ID "12345" exists
    When changes surname to "Bloggs" with ID "12345"
    Then I should see customer with new name "Bloggs"
