from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()



    def test_add_new_book_add_book(self): # тест проверяет, что новая книга добавляется в коллекцию
        books_collector = BooksCollector()  # Создаем экземпляр класса

        book_name = "To Kill a Mockingbird"

        # Проверяем, что книга еще не добавлена
        assert book_name not in books_collector.books_genre

        # Добавляем новую книгу
        books_collector.add_new_book(book_name)

        # Проверяем, что книга добавлена
        assert book_name in books_collector.books_genre




    def test_add_new_book_add_repeat_book(self): # Одну и ту же книгу можно добавить только один раз
        books_collector = BooksCollector()  # Создаем экземпляр класса

        book_name = "To Kill a Mockingbird"

        # Добавляем новую книгу
        books_collector.add_new_book(book_name)

        # Проверяем, что книга добавлена
        assert book_name in books_collector.books_genre

        # Пытаемся добавить ту же книгу повторно
        books_collector.add_new_book(book_name)

        # Проверяем, что книга не добавляется повторно
        assert books_collector.books_genre.count(book_name) == 1

