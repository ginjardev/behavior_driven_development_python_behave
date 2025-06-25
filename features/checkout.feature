Feature: E-commerce checkout process

    @Chrome
    Scenario: Successful checkout with valid user details 
        Given the user is on the product page link "https://ecommerce-playground.lambdatest.io/index.php?route=product/product&path=33&product_id=47"
        When the user clicks the "Buy Now" button
        And the user fills in billing and payment details
        And the user confirms the order
        Then the order should be successfully placed
       
