Feature: Manager views statistics page

  Scenario Outline: Manager views statistics page
    Given Employee is on the login page
    When Employee enters their <username> into the username field
    And Employee enters their <password> into the password field
    And Employee clicks on login button
    Then Employee is on the View Reports Page
    And Employee's manager status is <isManager>
    When Employee clicks on the statistics button
    Then Employee is on statistics page


    Examples:
      | username | password | isManager |
      | test2    | test2    | 1         |
      | test4    | test4    | 1         |