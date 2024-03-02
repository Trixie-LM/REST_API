from utils.utils import load_schema
import requests
import jsonschema
from utils.partner_api import get_product_list


ISSUER_DN = '/C=RU/ST=Moscow/L=Moscow/O=ÐÐÐ Â«Ð¡Ð¿Ð¾ÑÑÐ¸Ð²Ð½ÑÐµ Ð»Ð¾ÑÐµÑÐµÐ¸Â»/emailAddress=noreply@example.invalid/CN=russian-post-mtls'

def test_successful_response(api_url):
    """Получили ответ со статусом кода 200"""
    response = get_product_list.successful_response(api_url, ISSUER_DN, '', 'ACTIVATED')
    assert response.status_code == 200
