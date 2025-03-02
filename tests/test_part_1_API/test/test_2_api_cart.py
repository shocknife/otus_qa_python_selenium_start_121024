import pytest
import allure


@pytest.mark.parametrize(
    "product_id, quantity, expected_status",
    [
        ("40", "1", 'success'),
        ("40", "0", 'success'),
        ("", "1", 'error'),
        ("9999", "1", 'error'),
        ("invalid", "1", 'error'),
    ]
)
@allure.step("Проверка добавления добавления продукта в корзину product_id={product_id} and quantity={quantity}")
def test_cart_add(client, product_id, quantity, expected_status):
    response = client.cart_api.post_cart_add(product_id=product_id, quantity=quantity)
    assert response.status_code == 200
    if response.json().get('success'):
        assert response.json()[expected_status] == 'Success: You have modified your shopping cart!'
    else:
        assert response.json()[expected_status]['warning'] == 'Warning: Product could not be found!'


@pytest.mark.parametrize(
    "product_id, quantity_add, quantity_edit",
    [
        ("40", '1', '5'),
        ("40", '10', '1'),
    ]
)
@allure.step("Тестирование изменения количества продукта в корзине")
def test_cart_edit(client, product_id, quantity_add, quantity_edit):
    client.cart_api.post_cart_add(product_id=product_id, quantity=quantity_add)
    product_id_to_find = product_id
    cart_id = client.cart_api.find_cart_id_of_product_id(client=client, product_id=product_id)
    response = client.cart_api.post_cart_edit(key_id=cart_id, quantity=quantity_edit)
    assert response.status_code == 200
    assert response.json()['success'] == 'Success: You have modified your shopping cart!'
    response_edit = client.cart_api.get_item_cart()
    quantity_find = None
    for product_edit in response_edit.json().get("products", []):
        if product_edit.get("product_id") == product_id_to_find:
            quantity_find = product_edit.get("quantity")
            break
    assert quantity_find == quantity_edit


@pytest.mark.parametrize(
    "product_id, quantity_add, use_correct_cart_id, results",
    [
        ("40", '1', True, False),
        ("40", '10', False, True),
    ]
)
@allure.step("Тестирование удаления продукта из корзины")
def test_cart_remove(client, product_id, quantity_add, use_correct_cart_id, results):
    client.cart_api.post_cart_add(product_id=product_id, quantity=quantity_add)
    cart_id = client.cart_api.find_cart_id_of_product_id(client=client, product_id=product_id)
    cart_id_to_remove = cart_id if use_correct_cart_id else "test"
    response_remove = client.cart_api.post_cart_remove(key_id=cart_id_to_remove)
    assert response_remove.status_code == 200
    assert response_remove.json()['success'] == 'Success: You have modified your shopping cart!'
    response_edit = client.cart_api.get_item_cart()
    product_exists = any(product.get("product_id") == product_id for product in response_edit.json().get("products", []))
    assert product_exists == results
