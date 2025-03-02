import requests


class ApiAuth:
    def __init__(self, base_url_api):
        self.base_url_api = base_url_api

    def post_auth(self, username, key):
        response = requests.post(
            f"{self.base_url_api}api/account/login",
            data={"username": username, "key": key},
        )
        return response
