import allure
import pytest



@pytest.mark.parametrize(
    "firstname, lastname, email, telephone",
    [
        ("Dear", "Shinchan", "barakuda@abra.com", "+1 879 2548022"),
        ("", "Marcopolo", "shinchan@example.com", "+2 905 2548022"),
        ("Oleg", "", "Oleg@abra.com", "+3 911 2548022"),
        ("Petr", "Changan", "", "+4 855 2548022"),
        ("Александр", "Omoda", "Omoda@abra.com", "")
    ]
)
@allure.step("Проверка добавления адреса доставки")
def test_add_customer(client, firstname, lastname, email, telephone):
    response = client.customer_api.post_add_customer(
        firstname=firstname,
        lastname=lastname,
        email=email,
        telephone=telephone
    )
    if not firstname:
        assert response.json()['error']['firstname']  == 'First Name must be between 1 and 32 characters!'
    if not lastname:
        assert response.json()['error']['lastname']  == 'Last Name must be between 1 and 32 characters!'
    if not email:
        assert response.json()['error']['email'] == 'E-Mail Address does not appear to be valid!'
    assert response.status_code == 200