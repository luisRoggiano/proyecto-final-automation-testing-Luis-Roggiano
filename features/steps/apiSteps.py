from behave import when, then, given
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
#check Connection
@given('API Connected OK')
def step_api_available(context):
    context.base_url = BASE_URL
#check Get method
@when('GET a "{endpoint}"')
def step_get_request(context, endpoint):
    context.response = requests.get(f"{context.base_url}{endpoint}")
#Check test POST Method
@when('POST to "{endpoint}" with:')
def step_post_with_table(context, endpoint):
    # table to dict
    data = {}
    for row in context.table:
        data[row[0]] = row[1]
    
    context.response = requests.post(f"{context.base_url}{endpoint}", json=data)
#check status code
@then('Status Code should be {status:d}')
def step_check_status(context, status):
    assert context.response.status_code == status