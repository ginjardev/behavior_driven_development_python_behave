Feature: LambdaTest E-commerce Playground user login functionality

    @Chrome
    Scenario: Successful login with valid email and password
      Given the LambdaTest e-commerce login page is open "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
      When check if page title is "Account Login"
      When I enter valid email and password
      And I click the Login button
      Then I should be redirected to the dashboard
