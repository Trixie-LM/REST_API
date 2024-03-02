from utils.utils import load_schema

import requests
import jsonschema


def successful_response(api_url, issuer_dn, product_type, product_status):
    """Получение успешного ответа с кодом статуса 200"""
    with step(f"Отправление запроса c product_type='{product_type}' и product_status='{product_status}'"):
    # WHEN
        response = requests.post(
            url=f'{api_url}/partner-api/api/v1/partners/getProductList',
            headers={
                "ssl-client-issuer-dn": issuer_dn
            },
            json={
                "productType": product_type,
                "productStatus": product_status
            }
        )
    return response
