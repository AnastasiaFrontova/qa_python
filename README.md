Провела покрытие тестами приложение BooksCollector. Реализованы тесты:
1. Проверка ограничения на длину символов в названии книги - test_add_new_book_validation_name
2. Добавление новой книги в список - test_add_new_book
3. Добавление дубликата в список - test_add_new_book_duplicate_not_added
4. Устанавливаем жанр книги - test_set_book_genre
5. Вывод жанра книги по ее названию - test_get_book_genre
6. Вывод книги с жанром не из списка - test_set_book_genre_invalid_genre_not_set
7. Получение списка книг с определенным жанром - test_get_books_with_specific_genre
8. Вывод текущего словаря - test_get_books_genre
9. Вывод книг, подходящих для детей (без возрастного рейтинга) - test_get_books_for_children
10. Добавление книги в избранное - test_add_book_in_favorites
11. Удаление книги из избранного - test_delete_book_from_favorites
12. Получение списка избранных книг - test_get_list_of_favorites_books