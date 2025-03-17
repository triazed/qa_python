# qa_python

Файл main.py содержит тестируемый класс BooksCollector.

Файл tests.py содержит тесты класса BooksCollector: 

    1. test_add_new_object_has_genres_lists_true
    # Тест метода __init__. Проверяет, что у нового экземпляра класса есть все жанры в списке жанров.
    
    2. test_add_new_book_add_two_books_added
    # Тест метода add_new_book. Проверяет, что в словарь books_genre добавилось именно 2 книги
    
    3. test_add_new_book_when_name_is_more_than40_less_than_1_book_not_added
    # Тест метода add_new_book. Проверяет, что книга с названием, содержащим < 1 и > 41 символов, не добавилась в словарь books_genre

    4. test_set_book_genre_when_book_added_and_genre_exists_genre_set
    # Тест метода set_book_genre. Проверяет, что если книга есть в books_genre и её жанр входит в список genre, то в словаре books_genre устанавливается жанр книги.
    
    5. test_set_book_genre_when_book_added_and_genre_doesnt_exist_genre_not_set
    # Тест метода set_book_genre. Проверяет, что если книга есть в books_genre, но её жанр не входит в список genre, то в словаре books_genre не устанавливается жанр книги.

    6. test_get_book_genre_when_book_added_and_genre_set_returns_genre
    # Тест метода get_book_genre. Проверяет, что если книга есть в books_genre и ей задан жанр, то получаем жанр книги по ее имени.
    
    7. test_get_book_genre_when_book_added_and_genre_not_set_returns_empty_string
    # Тест метода get_book_genre. Проверяет, что если книга есть в books_genre, но ей не задан жанр, то получаем пустую строку.

    8. test_get_books_with_specific_genre_when_book_added_and_genre_set_book_added_to_list
    # Тест метода get_books_with_specific_genre. Проверяет, что если книга есть в books_genre, ей задан жанр, и её жанр входит в список genre, то в список books_with_specific_genre записывается название книги.

    9. test_get_books_genre_when_book_added_and_genre_set_returns_dictionary
    # Тест метода get_books_genre. Проверяет, что метод выводит текущий словарь books_genre.
    
    10. test_get_books_for_children_when_genre_not_in_age_rating_book_added_to_list
    # Тест метода get_books_for_children. Проверяет, что если книга есть в books_genre, ей задан жанр, который не входит в список genre_age_rating, то в список books_for_children записывается название книги.
    
    11. test_add_book_in_favorites_when_book_not_in_favourites_added_to_list
    # Тест метода add_book_in_favorites. Проверяет, что если книга есть в books_genre и еще не была добавлена в список favorites, добавляется в список favorites.

    12. test_add_book_in_favorites_when_book_already_in_favourites_not_added_to_list
    # Тест метода add_book_in_favorites. Проверяет, что если книга есть в books_genre и уже была добавлена в список favorites, она не добавляется в список favorites повторно.
    
    13. test_delete_book_from_favorites_when_book_in_favourites_deleted_from_list
    # Тест метода delete_book_from_favorites. Проверяет, что если книга есть в favorites, метод delete_book_from_favorites удаляет ее из favorites.

    14. test_get_list_of_favorites_books_when_book_added_returns_list
    # Тест метода get_list_of_favorites_books. Проверяет, что метод выводит текущий список избранных книг.    
    

