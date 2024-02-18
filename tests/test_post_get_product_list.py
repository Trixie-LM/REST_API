import json
import pprint

from utils import load_schema

import requests
import jsonschema


ISSUER_DN = '/C=RU/ST=Moscow/L=Moscow/O=ÐÐÐ Â«Ð¡Ð¿Ð¾ÑÑÐ¸Ð²Ð½ÑÐµ Ð»Ð¾ÑÐµÑÐµÐ¸Â»/emailAddress=noreply@example.invalid/CN=russian-post-mtls'

def test_create_user_should_be_success(api_url):
    # GIVEN
    # schema = load_schema('scheme/post_create_user.json')
    product_type = ''
    product_status = 'ACTIVATED'

    # WHEN
    response = requests.post(
        url=f'{api_url}/partner-api/api/v1/partners/getProductList',
        headers={
            "ssl-client-issuer-dn": ISSUER_DN
        },
        json={"productType": product_type, "productStatus": product_status}
    )

    response_json = response.json()

    # JSON Path
    print('\n')
    pprint.pprint(response_json[0])
    print('Вывод ключа: ' + response_json[0]['productCode'])
    print('Вывод количества элементов в массиве: ' + str(len(json.loads(response.text))))
    # Вывод ключа во всех элементах массива
    for index, qqq in enumerate(response_json):
        print(f"{index}. {qqq['productCode']}")

    # THEN
    assert response.status_code == 200

    # jsonschema.validate(instance=response.json(), schema=schema)
