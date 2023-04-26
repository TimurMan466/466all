import requests

# Отправляем GET запрос
response = requests.get("http://localhost:5000/api/books")

# Проверяем, что код ответа равен 200 (ОК)
assert response.status_code == 200, f"Ошибка: код ответа сервера не 200, а {response.status_code}"

# Проверяем, что ответ содержит JSON
try:
    json_data = response.json()
except ValueError:
    assert False, "Ошибка: ответ сервера не содержит JSON"

# Проверяем, что каждая книга содержит поля "id", "name", "author", "year" и "isElectronicBook"
for book in json_data:
    assert "id" in book, "Ошибка: книга не содержит поля 'id'"
    assert "name" in book, "Ошибка: книга не содержит поля 'name'"
    assert "author" in book, "Ошибка: книга не содержит поля 'author'"
    assert "year" in book, "Ошибка: книга не содержит поля 'year'"
    assert "isElectronicBook" in book, "Ошибка: книга не содержит поля 'isElectronicBook'"

# Проверяем, что количество книг в ответе соответствует количеству книг в базе данных
books_count = len(json_data)
assert books_count > 0, "Ошибка: список книг пуст"
assert books_count == 1, f"Ошибка: количество книг в ответе ({books_count}) не соответствует количеству книг в базе данных (1)"

print("Тест успешно пройден!")