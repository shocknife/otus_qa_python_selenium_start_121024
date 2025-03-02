class ApiShipMethod:
    def __init__(self, client):
        self.client = client

    def get_shipping_method(self):
        response = self.client.session.get(f"{self.client.base_url_api}api/sale/shipping_method")
        return response

    def post_shipping_method_save(self, shipping_method):
        data = {'shipping_method': shipping_method}
        response = self.client.session.post(f"{self.client.base_url_api}api/sale/shipping_method.save", data=data)
        return response

    def post_shipping_address(self,
                             firstname: str,
                             lastname: str,
                             address_1: str,
                             city: str,
                             country_id: str,
                             zone_id: int):
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'address_1': address_1,
            'city': city,
            'country_id': country_id,
            'zone_id': zone_id
        }
        response = self.client.session.post(f"{self.client.base_url_api}api/sale/shipping_address",
                                            data=data)
        return response