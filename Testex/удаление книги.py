import requests

# Отправляем запрос для получения списка книг
response = requests.get('http://localhost:5000/api/books')
assert response.status_code == 200, 'Ошибка при получении списка книг'

# Выбираем  книгу из списка для удаления
books = response.json()
if not books:
    raise AssertionError('Список книг пуст')
book_id = books[0]['id']

# Отправляем запрос для удаления книги
response = requests.delete(f'http://localhost:5000/api/books/{book_id}')
assert response.status_code == 200, 'Ошибка при удалении книги'

# Отправляем запрос, чтобы проверить, что книга была удалена
response = requests.get('http://localhost:5000/api/books')
assert response.status_code == 200, 'Ошибка при получении списка книг после удаления'

books = response.json()
assert not any(book['id'] == book_id for book in books), 'Книга не была удалена из списка'

print("Тест успешно пройден!")
