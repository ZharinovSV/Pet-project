from app.api import PetDemoProject
from app.settings import valid_username, valid_password, invalid_username, invalid_password, empty_username, empty_password

pd = PetDemoProject()

def test_get_api_token_with_valid_data(username = valid_username, password = valid_password):
    """ Проверяем что запрос api ключа с валидными данными возвращает статус 200 и в результате содержится слово token"""

    status, result = pd.get_api_token(username, password)
    assert status == 200
    assert 'token' in result

def test_get_api_token_with_invalid_data(username = invalid_username, password = invalid_password):
    """ Проверяем что запрос api ключа с невалидными данными возвращает статус 400"""

    status, result = pd.get_api_token(username, password)
    assert status == 400

def test_get_api_token_with_empty_data(username = empty_username, password = empty_password):
    """ Проверяем что запрос api ключа с пустыми данными данными возвращает статус 400"""

    status, result = pd.get_api_token(username, password)
    assert status == 400

def test_get_pet_categories_with_valid_token():
    """ Проверяем что запрос всех категорий животных возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную token. Далее используя этого ключ
    запрашиваем список всех категорий животных и проверяем что список не пустой."""

    _, token = pd.get_api_token(valid_username, valid_password)
    status, result = pd.get_list_of_pets_categories(token)

    assert status == 200
    assert len(result['id']) > 0

def test_get_pet_categories_without_token():
    """ Проверяем что запрос всех категорий животных без отправки токена возвращает ошибку"""

    status, result = pd.get_list_of_pets_categories_whithout_token()

    assert status != 200


def test_create_pet_categories(name = 'cats'):
    """ Проверяем что запрос на создание категории животных возвращает id созданной категори и статус 201."""

    _, token = pd.get_api_token(valid_username, valid_password)
    status, result = pd.create_pets_categories(token, name)

    assert status == 201
    assert 'id' in result


