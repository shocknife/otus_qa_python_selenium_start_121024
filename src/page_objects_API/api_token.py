from http import HTTPStatus

import requests
import logging
from src.page_objects_API.api_cart import ApiCart
from src.page_objects_API.api_currency import ApiCurrency
from src.page_objects_API.api_customer import ApiCustomer
from src.page_objects_API.api_order import ApiOrder
from src.page_objects_API.api_payment_address import ApiPayAddress
from src.page_objects_API.api_ship_address import ApiShipMethod


logger = logging.getLogger(__name__)

class ApiToken:
    def __init__(self, base_url_api, username, key):

        self.base_url_api = base_url_api
        self.session = requests.Session()
        params = {'username': username,
                  'key': key}
        response = requests.post(f"{self.base_url_api}api/account/login", data=params)
        json_response = response.json()
        assert response.status_code == HTTPStatus.OK
        assert response.json().get("api_token")
        logger.debug(f"Ответ JSON: {json_response}")
        token = json_response['api_token']
        self.session.params = {'api_token': token}


    @property
    def currency_api(self) -> callable:
        return ApiCurrency(self)

    @property
    def cart_api(self) -> callable:
        return ApiCart(self)

    @property
    def order_api(self) -> callable:
        return ApiOrder(self)

    @property
    def payment_addr_api(self) -> callable:
        return ApiPayAddress(self)

    @property
    def ship_method_api(self) -> callable:
        return ApiShipMethod(self)

    @property
    def customer_api(self) -> callable:
        return ApiCustomer(self)