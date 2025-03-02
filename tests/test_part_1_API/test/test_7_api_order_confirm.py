import allure

import pytest
from faker import Faker

fake = Faker()


test_data = (
    fake.first_name(),
    fake.last_name(),
    fake.street_address(),
    fake.city(),
    fake.random_int(min=100, max=999),
    fake.random_int(min=100, max=999),
    fake.email(),
    fake.phone_number(),
    "40",
    "1",
    "cod.cod",
    "flat.flat",
)


@allure.step("Проверка подтверждения заказа")
@pytest.mark.parametrize(
    "firstname, lastname,street_address_1, city, country_code, area_code, email, telephone, product_id, quantity, payment_method, shipping_method",
    [test_data],
)
def test_post_order_add(
    client,
    firstname,
    lastname,
    street_address_1,
    city,
    country_code,
    area_code,
    email,
    telephone,
    product_id,
    quantity,
    payment_method,
    shipping_method,
):
    client.customer_api.post_add_customer(
        firstname=firstname, lastname=lastname, email=email, telephone=telephone
    )
    client.cart_api.post_cart_add(product_id=product_id, quantity=1)
    client.payment_addr_api.post_payment_address(
        firstname=firstname,
        lastname=lastname,
        address_1=street_address_1,
        city=city,
        country_id=country_code,
        zone_id=area_code,
    )
    client.ship_method_api.post_shipping_address(
        firstname=firstname,
        lastname=lastname,
        address_1=street_address_1,
        city=city,
        country_id=country_code,
        zone_id=area_code,
    )
    client.payment_addr_api.get_payment_method()
    client.payment_addr_api.post_add_method_payment(payment_method)
    client.ship_method_api.get_shipping_method()
    client.ship_method_api.post_shipping_method_save(shipping_method)
    response = client.order_api.post_order_confirm()
    assert response.json()["success"] == "Success: You have modified orders!"
    assert response.status_code == 200
    assert response.json().get("order_id")
