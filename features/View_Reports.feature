Feature: Employee and Manager View Reimbursements

  Scenario Outline: Employee views reimbursements
    Given Employee is on the login page
    When Employee enters their <username> into the username field
    And Employee enters their <password> into the password field
    And Employee clicks on login button
    Then Employee is on the View Reports Page
    When Employee clicks on the logout button
    Then Employee is on the login page


    Examples:
      | username | password |
      | rtest1   | password |
      | bpur     | password |
      | test1    | test1    |
      | test3    | test3    |


  Scenario Outline: Manager views and resolves reimbursements
    Given Employee is on the login page
    When Employee enters their <username> into the username field
    And Employee enters their <password> into the password field
    And Employee clicks on login button
    Then Employee is on the View Reports Page
    When Manager clicks on the resolve btn
    And Manager selects the <status>
    And Manager enters their <comment> into the comment field
    And Manager clicks the submit button
    Then Employee is on the View Reports Page
    When Employee clicks on the logout button
    Then Employee is on the login page


    Examples:
      | username | password | status | comment            |
      | test2    | test2    | 0      | Selenium Comment 1 |
      | test4    | test4    | 1      | Selenium Comment 2 |
