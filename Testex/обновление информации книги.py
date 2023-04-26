import requests
import json


def test_put_book():
    # Отправляем POST запрос для создания книги
    book_data = {"name": "Тестовая книга", "author": "Тестер", "year": 2022, "isElectronicBook": True}
    create_response = requests.post("http://localhost:5000/api/books", json=book_data)
    assert create_response.status_code == 200, "Ошибка создания книги"
    book_id = create_response.json()["id"]

    # Отправляем PUT запрос с измененными данными книги
    updated_data = {"name": "Три товарища", "author": "Эрих Мария Ремарк", "year": 1936, "isElectronicBook": False}
    put_response = requests.put(f"http://localhost:5000/api/books/{book_id}", json=updated_data)
    assert put_response.status_code == 200, "Ошибка при изменении книги"

    # Отправляем GET запрос и проверяем, что данные соответствуют измененным данным
    get_response = requests.get(f"http://localhost:5000/api/books/{book_id}")
    assert get_response.status_code == 200, "Ошибка при получении данных книги"
    book_info = get_response.json()
    assert book_info["name"] == updated_data["name"], "Неверное название книги"
    assert book_info["author"] == updated_data["author"], "Неверный автор книги"
    assert book_info["year"] == updated_data["year"], "Неверный год издания книги"
    assert book_info["isElectronicBook"] == updated_data["isElectronicBook"], "Неверный тип книги"

print("Тест успешно пройден!")