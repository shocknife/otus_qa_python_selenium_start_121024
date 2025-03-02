import allure
import pytest



@pytest.mark.parametrize(
    "firstname, lastname, address_1, city, country_id, zone_id",
    [
        ("Dear", "Shinchan", "123 Main St", "Anytown", 223, 1),
        ("", "Shinchan", "123 Main St", "Anytown", "RUS", 3),
        ("Dear", "", "123 Main St", "Anytown", 10, "KGD"),
        ("Dear", "Shinchan", "", "KLD", "RUS", 123),
        ("Dear", "Shinchan", "123 Main St", "", "RUS", 99),
        ("Dear", "Shinchan", "123 Main St", "Anytown", "", "KGD"),
        ("Dear", "Shinchan", "123 Main St", "Anytown", 55, ""),
        ("", "", "", "", "", ""),
        ("John", "Doe", "Street 123", "NY", "USA", 1056),
        ("123", "456", "789", "000", "AAA", "BBB"),
    ]
)
@allure.step("Проверка добавления адреса доставки")
def test_post_payment_address(client, firstname, lastname, address_1, city, country_id, zone_id):
    response = client.payment_addr_api.post_payment_address(
        firstname=firstname,
        lastname=lastname,
        address_1=address_1,
        city=city,
        country_id=country_id,
        zone_id=zone_id
    )
    if not firstname:
        assert response.json()['error']['firstname']  == 'First Name must be between 1 and 32 characters!'
    if not lastname:
        assert response.json()['error']['lastname']  == 'Last Name must be between 1 and 32 characters!'
    if not address_1:
        assert response.json()['error']['address_1'] == 'Address 1 must be between 3 and 128 characters!'
    if not city:
        assert response.json()['error']['city'] == 'City must be between 3 and 128 characters!'
    if not country_id:
        assert response.json()['error']['country'] == 'Please select a country!'
    if not zone_id:
        assert response.json()['error']['zone'] == 'Please select a region / state!'
    assert response.status_code == 200



