import allure
import pytest


@allure.step("Проверка смены валюты")
@pytest.mark.parametrize(
    "product_id, quantity_add, currency, currency_symbol, results",
    [
        ("40", "1", "GBP", "£", 200),
        ("40", "1", "USD", "$", 200),
        ("40", "1", "EUR", "€", 200),
        ("40", "1", "invalid", None, 400),
        ("40", "1", " ", None, 400),
        ("40", "1", 44, None, 400),
    ],
)
def test_post_currency(
    client, currency, currency_symbol, product_id, quantity_add, results
):
    client.cart_api.post_cart_add(product_id=product_id, quantity=quantity_add)
    response = client.currency_api.post_currency(currency=currency)
    assert response.status_code == 200
    if currency_symbol is not None:
        assert response.json()["success"] == "Success: Your currency has been changed!"
        response_item = client.cart_api.get_item_cart()
        cart_id = client.cart_api.find_cart_id_of_product_id(
            client=client, product_id=product_id
        )

        price_value = None
        total_value = None

        for product in response_item.json()["products"]:
            if product["cart_id"] == cart_id:
                price_value = product["price"]
                total_value = product["total"]
                break

        totals_texts = [item["text"] for item in response_item.json()["totals"]]

        assert currency_symbol in price_value
        assert currency_symbol in total_value
        assert all(
            currency_symbol in text for text in totals_texts
        ), "Не все элементы содержат символ $"
    else:
        assert response.json()["error"] == "Warning: Currency could not be found!"
