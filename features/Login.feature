Feature: Employee Logs in

  Scenario Outline: Employee logs in
    Given Employee is on the login page
    When Employee enters their <username> into the username field
    And Employee enters their <password> into the password field
    And Employee clicks on login button
    Then Employee is on the View Reports Page
    And Employee's manager status is <isManager>


    Examples:
      | username | password | isManager |
      | rtest1   | password | 0         |
      | rtest2   | password | 0         |
      | test2    | test2    | 1         |
      | test4    | test4    | 1         |