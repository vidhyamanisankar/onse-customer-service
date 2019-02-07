from behave import when, then


@when('changes surname to "{surname}" with ID "{customer_id:d}"')
def change_surname(context, surname, customer_id):
    context.response = context.web_client.put(f'/customers/{customer_id}',
                                              json={'surname': surname})

    assert context.response.status_code == 200, context.response.status_code
    context.customer_id = context.response.get_json()['customerId']


@then('I should see customer with new name "{surname}"')
def updated_name(context, surname):
    response = context.response

    assert response.status_code == 200, response.status_code
    assert response.is_json
    body = response.get_json()
    assert f"{body['surname']}" == surname
