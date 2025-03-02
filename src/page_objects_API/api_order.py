import allure


class ApiOrder:
    def __init__(self, client):
        self.client = client

    @allure.title("Загрузка заказа")
    def get_order_load(self):
        response = self.client.session.get(
            f"{self.client.base_url_api}api/sale/order.load"
        )
        return response

    @allure.title("Подтверждение заказа")
    def post_order_confirm(self):
        response = self.client.session.post(
            f"{self.client.base_url_api}api/sale/order.confirm"
        )
        return response
