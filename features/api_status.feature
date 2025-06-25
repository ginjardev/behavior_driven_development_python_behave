Feature: Public API - Post Retrival

    @Chrome
    Scenario Outline:
        Given the API endpoint is "https://jsonplaceholder.typicode.com/<endpoint>"
        When I make a GET request
        Then the response status should be "<status_code>"
        And the response should contain the field "<field>"

        Examples:
            | endpoint       | status_code | field   |
            | posts/1        | 200         | userId  |
            | posts/2        | 200         | title   |
            | posts/100      | 200         | body    |
            | posts/101      | 404         | error   |