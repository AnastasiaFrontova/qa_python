import pytest
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
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1. Тесты для метода add_new_book.

    @pytest.mark.parametrize("name, expected", [
        ('', False),
        ('a' * 41, False),
        ('ValidName', True),
    ])
    def test_add_new_book_validation_name(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == expected


    # 2. Тест для метода add_new_book, добавляет новую книгу в словарь books_genre

    @pytest.mark.parametrize("name", [
        'Оно',
        'Гость из Будущего',
        'Гордость и предубеждение',
    ])
    def test_add_new_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # 3. Тест для метода add_new_book, попытка добавления дубликата
    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Тачки')
        collector.add_new_book('Тачки')
        assert len(collector.get_books_genre()) == 1

    # 4. Тест для метода set_book_genre.
    @pytest.mark.parametrize("name, genre", [
        ('Земля будущего', 'Фантастика'),
        ('Оно', 'Ужасы'),
        ('Тачки', 'Мультфильмы'),
    ])
    def test_set_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # 5. Тест для метода get_book_genre, вывод жанра книги по ее имени
    @pytest.mark.parametrize("name, genre", [
        ('Земля будущего', 'Фантастика'),
        ('Оно', 'Ужасы'),
        ('Тачки', 'Мультфильмы'),
    ])
    def test_get_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    #№6. Тест для метода set_book_genre, вывод книги с жанром не из списка
    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Друзья')
        collector.set_book_genre('Друзья', 'Несуществующий жанр Сериал')
        assert collector.get_book_genre('Друзья') == ''

    # 7. Тест для метода get_books_with_specific_genre.
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Побег')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Побег', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно']


    # 8. Тест для метода get_books_genre.
    def test_get_books_genre(self, collector):
        collector.add_new_book("Амфибия")
        collector.set_book_genre("Амфибия", "Фантастика")
        assert collector.get_books_genre() == {"Амфибия": "Фантастика"}


    # 9. Тест для метода get_books_for_children.
    def test_get_books_for_children(self, collector):
        collector.add_new_book("Тачки")
        collector.set_book_genre("Тачки", "Мультфильмы")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        assert collector.get_books_for_children() == ["Тачки"]


    # 10. Тест для метода add_book_in_favorites
    @pytest.mark.parametrize("name", [
        "Тачки",
        "Начало",
        "Гость из будущего"
    ])
    def test_add_book_in_favorites(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]


    # 11. Тест для метода delete_book_from_favorites
    @pytest.mark.parametrize("name", [
        "Тачки",
        "Начало",
        "Гость из Будущего"
    ])
    def test_delete_book_from_favorites(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.get_list_of_favorites_books() == []

    # 12. Тест для метода get_list_of_favorites_books
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Тачки")
        collector.add_book_in_favorites("Тачки")
        assert collector.get_list_of_favorites_books() == ["Тачки"]
















