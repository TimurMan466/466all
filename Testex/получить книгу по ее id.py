import requests

# Задаем URL для API
url = "http://localhost:5000/api/books/"

# Задаем id книги, информацию о которой мы хотим получить
book_id = 1

# Отправляем GET-запрос на получение информации о книге
response = requests.get(url + str(book_id))

# Проверяем, что код ответа сервера равен 200 (ОК)
assert response.status_code == 200, f"Код ответа сервера не равен 200. Код: {response.status_code}"

# Проверяем, что тело ответа содержит Json объект с полями "id", "name", "author", "year" и "isElectronicBook"
json_data = response.json()
assert set(json_data.keys()) == {"id","name", "author", "year", "isElectronicBook"}, "Тело ответа не содержит Json объекта с полями 'id', 'name', 'author', 'year' и 'isElectronicBook'"

# Проверяем, что значение поля "id" соответствует переданному в запросе book_id
assert json_data["id"] == book_id, f"Значение поля 'id' не соответствует переданному в запросе. Ожидалось: {book_id}. Получено: {json_data['id']}"

print("Тест успешно пройден!")
