import conftest


class ApiPayAddress:
    def __init__(self, client):
        self.client = client

    def get_payment_method(self):
        response = self.client.session.get(
            f"{self.client.base_url_api}api/sale/payment_method"
        )
        return response

    def post_add_method_payment(self, payment_method):
        data = {"payment_method": payment_method}
        response = self.client.session.post(
            f"{self.client.base_url_api}api/sale/payment_method.save", data=data
        )
        return response

    def post_payment_address(
        self,
        firstname: str,
        lastname: str,
        address_1: str,
        city: str,
        country_id: str,
        zone_id: int,
    ):
        data = {
            "firstname": firstname,
            "lastname": lastname,
            "address_1": address_1,
            "city": city,
            "country_id": country_id,
            "zone_id": zone_id,
        }
        response = self.client.session.post(
            f"{self.client.base_url_api}api/sale/payment_address", data=data
        )
        return response
