from http import HTTPStatus
import allure
import pytest
from config.configuration import API_USERNAME, API_KEY
from page_objects_API.api_auth import ApiAuth



@allure.title("Позитивная проверка, валидный API KEY")
@pytest.mark.parametrize("username, key", [(API_USERNAME, API_KEY)])
def test_login_get_api_token_success(base_url_api, username, key):
    client = ApiAuth(base_url_api)
    response = client.post_auth(username, key)
    assert response.status_code == HTTPStatus.OK
    assert response.json()["success"] == "Success: API session successfully started!"
    assert response.json().get("api_token")


@allure.title("Негативная проверка, невалидный API KEY")
@pytest.mark.parametrize("username, key", [(API_USERNAME, "12345")])
def test_login_get_api_token_negative(base_url_api, username, key):
    client = ApiAuth(base_url_api)
    response = client.post_auth(username, key)
    assert response.status_code == HTTPStatus.OK
    assert response.json()["error"] == 'Warning: Incorrect API Key!'

