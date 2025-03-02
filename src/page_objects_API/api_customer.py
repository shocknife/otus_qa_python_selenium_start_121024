class ApiCustomer:
    def __init__(self, client):
        self.client = client

    def post_add_customer(self,
                             firstname: str,
                             lastname: str,
                             email: str,
                             telephone: str):
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'telephone': telephone
        }
        response = self.client.session.post(f"{self.client.base_url_api}api/sale/customer",
                                            data=data)
        return response
