import allure
import requests


class ApiAuth:
    def __init__(self, base_url_api):
        self.base_url_api = base_url_api

    @allure.title("Аутентификация пользователем")
    def post_auth(self, username, key):
        response = requests.post(
            f"{self.base_url_api}api/account/login",
            data={"username": username, "key": key},
        )
        return response
