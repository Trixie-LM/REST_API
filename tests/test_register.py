from utils import load_schema

import requests
import jsonschema


def test_register_success(api_url):
    # GIVEN
    schema = load_schema('scheme/post_register.json')
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    # WHEN
    response = requests.post(f'{api_url}/register', json={
        "email": email,
        "password": password
    })

    # THEN
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=schema)


def test_register_without_password_fail(api_url):
    # GIVEN
    email = 'eve.holt@reqres.in'

    # WHEN
    response = requests.post(f'{api_url}/register', json={
        "email": email
    })

    # THEN
    assert response.status_code == 400


def test_register_not_defined_user_fail(api_url):
    # GIVEN
    email = 'example@gmail.com'
    password = 'example'

    # WHEN
    response = requests.post(f'{api_url}/register', json={
        "email": email,
        "password": password
    })

    # THEN
    assert response.status_code == 400
