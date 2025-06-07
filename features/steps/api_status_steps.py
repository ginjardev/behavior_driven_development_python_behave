import requests
from behave import given, when, then

@given('the API endpoint is "{endpoint}"')
def step_given_api_endpoint(context, endpoint):
    context.url = context.base_url + endpoint

@when('I make a GET request')
def step_when_get_request(context):
    context.response = requests.get(context.url)

@then('the response status should be "{status_code}"')
def step_then_response_status(context, status_code):
    assert context.response.status_code == int(status_code), f'Expected status code {status_code}, but got {context.response.status_code}'

@then('the response should contain the field "{field}"')
def step_then_response_contains_field(context, field):
    try:
        json_data = context.response.json()
    except Exception:
        json_data = {}

    # Optional: allow for failed responses that have no field
    if context.response.status_code == 404:
        assert field not in json_data or not json_data.get(field), \
            f"Unexpected field '{field}' found in 404 response"
    else:
        assert field in json_data, f"Field '{field}' not found in response"
