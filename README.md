Рад видеть в моём Pet-project!

Написаны автотесты к сервису http://91.210.171.73:8080/api/docs/:

Запрос ключа с валидными данными в поле username  password
Запрос ключа с невалидными данными в поле username  password
Запрос ключа с пустыми значениями в поле username  password
Получение списка категорий животных с валидным токеном
Получение списка категорий животных без токена
Создание категории животных

Т.к через тесты и через Postman любые запросы (кроме запроса на получение токена) возвращают 400 коды. Дальнейшее написание тестов остановлено. 

Для запуска тестов необходимо установить библиотеки pytest, requests

Запуск тестов производится командой py.test tests/test_pet.py
