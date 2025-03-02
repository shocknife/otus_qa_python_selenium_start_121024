from page_objects_API.api_uri import ApiUri

import requests


class ApiAuth:
    def __init__(self, base_url_api):
        self.base_url_api = base_url_api

    def post_auth(self, username, key):
        response = requests.post(f"{self.base_url_api}{ApiUri.LOGIN}", data={'username': username, 'key': key})
        return response