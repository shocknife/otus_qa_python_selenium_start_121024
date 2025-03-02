import pytest
import allure


@allure.step(
    "Проверка, что без добавления адреса доставки, не доступен список способов доставки"
)
def test_get_shipping_method(client_function):
    response = client_function.ship_method_api.get_shipping_method()
    assert response.status_code == 200
    assert (
        response.json()["error"]
        == "Warning: There are no products that require shipping"
    )
    client_function.cart_api.post_cart_add(product_id="40", quantity="1")
    response_add = client_function.ship_method_api.get_shipping_method()
    assert response.status_code == 200
    assert response_add.json()["error"] == "Warning: Shipping address required!"


@allure.step(
    "Проверка, что без добавления продукта, не доступен список способов доставки"
)
@pytest.mark.parametrize("shipping_method", [("flat.flat")])
def test_post_shipping_method_save(client_function, shipping_method):
    response = client_function.ship_method_api.post_shipping_method_save(
        shipping_method
    )
    assert response.status_code == 200
    assert (
        response.json()["error"]
        == "Warning: There are no products that require shipping"
    )
