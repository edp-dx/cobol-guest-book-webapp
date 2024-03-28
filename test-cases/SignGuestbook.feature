Feature: Sign the Guest Book

  Background:
    Given the COBOL Guest Book Webapp is running

  Scenario: Successfully sign the guest book
    Given I have the following signer details
      | name    | John Doe       |
      | message | Great service! |
    When I submit a request to sign the guest book
    Then the response should indicate the signing was successful
    And the response should contain "Thank you, John Doe, for your message!"

  Scenario: Attempt to sign with missing name
    Given I have the following signer details
      | message | Missing name! |
    When I submit a request to sign the guest book
    Then the response should indicate a failure due to missing name
    And the response status code should be 400

  Scenario: Attempt to sign with missing message
    Given I have the following signer details
      | name | Jane Doe |
    When I submit a request to sign the guest book
    Then the response should indicate a failure due to missing message
    And the response status code should be 400
