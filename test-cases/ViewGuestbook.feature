Feature: View the Guest Book

  Background:
    Given the COBOL Guest Book Webapp is running

  Scenario: View all guest book entries
    When I submit a request to view the guest book
    Then the response should be successful
    And the response should contain a list of all guest book entries

  Scenario: View guest book when it's empty
    Given the guest book currently has no entries
    When I submit a request to view the guest book
    Then the response should be successful
    And the response should indicate the guest book is empty
