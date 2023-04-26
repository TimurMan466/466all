import requests

# Определяем данные для новой книги
new_book = {
    "name": "Анна Каренина",
    "author": "Лев Толстой",
    "year": 1877,
    "isElectronicBook": False
}

# Отправляем POST-запрос для создания новой книги
response = requests.post("http://localhost:5000/api/books", json=new_book)

# Проверяем код ответа на запрос
assert response.status_code in (200, 201), f"Ошибка: получен код {response.status_code}"

# Получаем список всех книг после добавления новой
response = requests.get("http://localhost:5000/api/books")

# Проверяем, что добавленная книга присутствует в списке книг
assert new_book in response.json(), "Ошибка: добавленная книга отсутствует в списке книг"

# Проверяем, что добавленная книга содержит корректные данные
added_book = response.json()[response.json().index(new_book)]
assert added_book["name"] == new_book["name"], "Ошибка: некорректное название книги"
assert added_book["author"] == new_book["author"], "Ошибка: некорректный автор книги"
assert added_book["year"] == new_book["year"], "Ошибка: некорректный год издания книги"
assert added_book["isElectronicBook"] == new_book["isElectronicBook"], "Ошибка: некорректный тип издания книги"


print("Тест успешно пройден!")