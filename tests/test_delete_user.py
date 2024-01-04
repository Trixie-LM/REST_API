import requests


def test_delete_user_should_be_success(api_url):
    # GIVEN
    user_id = 2

    # WHEN
    response = requests.delete(f'{api_url}/users/{user_id}')

    # THEN
    assert response.status_code == 204
