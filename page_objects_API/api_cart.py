class ApiCart:
    def __init__(self, client):
        self.client = client

    def get_item_cart(self):
        response = self.client.session.post(f"{self.client.base_url_api}api/sale/cart")
        return response

    def post_cart_add(self, product_id: str, quantity:str):
        data = {'product_id':product_id,
                'quantity': quantity}
        response = self.client.session.post(f"{self.client.base_url_api}api/sale/cart.add",
                                           data=data)
        return response


    def post_cart_edit(self, key_id: str, quantity:str):
        data = {'key': key_id,
                'quantity': quantity}
        response = self.client.session.post(f"{self.client.base_url_api}api/sale/cart.edit",
                                           data=data)
        return response

    def post_cart_remove(self, key_id: str):
        data = {'key': key_id}
        response = self.client.session.post(f"{self.client.base_url_api}api/sale/cart.remove",
                                           data=data)
        return response

    def find_cart_id_of_product_id(self, client, product_id):
        response_add = client.cart_api.get_item_cart()
        product_id_to_find = product_id
        cart_id = None
        for product in response_add.json().get("products", []):
            if product.get("product_id") == product_id_to_find:
                cart_id = product.get("cart_id")
                break
        return cart_id