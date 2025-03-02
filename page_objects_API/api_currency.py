class ApiCurrency:
    def __init__(self, client):
        self.client = client

    def post_currency(self, currency: str):
        data = {'currency':currency}
        response = self.client.session.post(f"{self.client.base_url_api}api/localisation/currency",
                                           data=data)
        return response
