Feature: Employee Creates Reimbursements

  Scenario Outline: Employee creates a reimbursement
    Given Employee is on the login page
    When Employee enters their <username> into the username field
    And Employee enters their <password> into the password field
    And Employee clicks on login button
    Then Employee is on the View Reports Page
    When Employee clicks on Create Reports button
    Then Employee is on the Create Reports Page
    When Employee enters their <amount> into the amount field
    And Employee enters their <reason> into the description field
    And Employee clicks on the submit button
    And Employee clicks on the logout button
    Then Employee is on the login page




    Examples:
      | username | password | amount | reason       |
      | rtest1   | password | 1000   | Dental       |
      | rtest2   | password | 500    | Bought a ps5 |
      | test2    | test2    | 700    | Laptop       |
      | test4    | test4    | 200    | Uber Eats    |