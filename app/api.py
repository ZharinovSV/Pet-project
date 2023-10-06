import requests
import json

class PetDemoProject:

    def __init__(self):
        self.base_url = 'http://91.210.171.73:8080/'

    def get_api_token(self, username: str, password: str):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключем пользователя, найденного по указанным username и паролем"""

        data = {
            'username': username,
            'password': password
        }

        res = requests.post(self.base_url + 'api/token/auth/', data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets_categories(self, token):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком всех категорий животных."""

        headers = {'Authorization': token['token']}

        res = requests.get(self.base_url + '/api/category/', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets_categories_whithout_token(self):
        """Метод делает запрос к API сервера без токенаи возвращает статус запроса и результат в формате JSON"""

        res = requests.get(self.base_url + '/api/category/')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def create_pets_categories(self, token: json, name: str):
        """Метод создаёт карточку категории животных возвращает статус запроса и результат в формате JSON
        с созданной категории животных и id."""

        headers = {'Authorization': token['token']}
        data = {
            'name': name
        }

        res = requests.post(self.base_url + '/api/category/', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


