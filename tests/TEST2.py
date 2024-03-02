from utils.utils import load_schema

import requests
import jsonschema


ISSUER_DN = '/C=RU/ST=Moscow/L=Moscow/O=ÐÐÐ Â«Ð¡Ð¿Ð¾ÑÑÐ¸Ð²Ð½ÑÐµ Ð»Ð¾ÑÐµÑÐµÐ¸Â»/emailAddress=noreply@example.invalid/CN=russian-post-mtls'

def test_create_user_should_be_success(api_url):
    """Получили ответ со статусом кода 200"""
    # GIVEN
    schema = load_schema('../scheme/post_get_product_list/post_get_product_list_101021.json')
    schema2 = load_schema('../scheme/post_get_product_list/post_get_product_list_102041.json')
    product_type = ''
    product_status = 'ACTIVATED'

    # WHEN
    response = requests.post(
        url=f'{api_url}/partner-api/api/v1/partners/getProductList',
        headers={
            "ssl-client-issuer-dn": ISSUER_DN
        },
        json={
            "productType": product_type,
            "productStatus": product_status
        }
    )
    response_json = response.json()

    # THEN
    assert response.status_code == 200
    for element in response_json:
        if element['productCode'] == 101021:
            jsonschema.validate(instance=element, schema=schema)
        if element['productCode'] == 102041:
            jsonschema.validate(instance=element, schema=schema2)
