from utils import load_schema

import requests
import jsonschema


def test_create_user_should_be_success(api_url):
    # GIVEN
    schema = load_schema('scheme/post_create_user.json')
    name = 'morpheus'
    job = 'leader'

    # WHEN
    response = requests.post(f'{api_url}/users', json={
        "name": name,
        "job": job
    })

    # THEN
    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    jsonschema.validate(instance=response.json(), schema=schema)
