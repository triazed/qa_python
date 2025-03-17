from main import BooksCollector
import pytest

class TestBooksCollector:

    # Тест метода __init__. Проверяет, что у нового экземпляра класса есть все жанры в списке жанров.
    def test_add_new_object_has_genres_lists_true(self):
        collector = BooksCollector()
        all_genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        for i in all_genres:
            assert i in collector.genre

    # Тест метода add_new_book. Проверяет, что в словарь books_genre добавилось именно 2 книги
    def test_add_new_book_add_two_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    # Тест метода add_new_book. Проверяет, что книга с названием, содержащим < 1 и > 41 символов, не добавилась в словарь books_genre
    @pytest.mark.parametrize('name',['', 'Что делать, если ваш кот хочет вас убить, а собака за вас не заступается'])
    def test_add_new_book_when_name_is_more_than40_less_than_1_book_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre.keys()

    # Тест метода set_book_genre. Проверяет, что если книга есть в books_genre и её жанр входит в список genre, то в словаре books_genre устанавливается жанр книги.
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_when_book_added_and_genre_exists_genre_set(self, genre):
        collector = BooksCollector()
        name = 'Галопом по Вселенной'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    # Тест метода set_book_genre. Проверяет, что если книга есть в books_genre, но её жанр не входит в список genre, то в словаре books_genre не устанавливается жанр книги.
    def test_set_book_genre_when_book_added_and_genre_doesnt_exist_genre_not_set(self):
        collector = BooksCollector()
        name = 'Фантазии Дракулы'
        genre = 'Женский роман'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == ''

    # Тест метода get_book_genre. Проверяет, что если книга есть в books_genre и ей задан жанр, то получаем жанр книги по ее имени.
    def test_get_book_genre_when_book_added_and_genre_set_returns_genre(self):
        collector = BooksCollector()
        name = 'Галопом по Вселенной'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # Тест метода get_book_genre. Проверяет, что если книга есть в books_genre, но ей не задан жанр, то получаем пустую строку.
    def test_get_book_genre_when_book_added_and_genre_not_set_returns_empty_string(self):
        collector = BooksCollector()
        name = 'Книга без жанра'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    # Тест метода get_books_with_specific_genre. Проверяет, что если книга есть в books_genre, ей задан жанр, и её жанр входит в список genre, то в список books_with_specific_genre записывается название книги.
    def test_get_books_with_specific_genre_when_book_added_and_genre_set_book_added_to_list(self):
        collector = BooksCollector()
        name = 'Галопом по Вселенной'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_with_specific_genre(genre)

    # Тест метода get_books_genre. Проверяет, что метод выводит текущий словарь books_genre.
    def test_get_books_genre_when_book_added_and_genre_set_returns_dictionary(self):
        collector = BooksCollector()
        name = 'Галопом по Вселенной'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == {name: genre}

    # Тест метода get_books_for_children. Проверяет, что если книга есть в books_genre, ей задан жанр, который не входит в список genre_age_rating, то в список books_for_children записывается название книги.
    @pytest.mark.parametrize('genre',['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_when_genre_not_in_age_rating_book_added_to_list(self, genre):
        collector = BooksCollector()
        name = 'Детская книга'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_for_children()

    # Тест метода add_book_in_favorites. Проверяет, что если книга есть в books_genre и еще не была добавлена в список favorites, добавляется в список favorites.
    def test_add_book_in_favorites_when_book_not_in_favourites_added_to_list(self):
        collector = BooksCollector()
        name = 'Галопом по Вселенной'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    # Тест метода add_book_in_favorites. Проверяет, что если книга есть в books_genre и уже была добавлена в список favorites, она не добавляется в список favorites повторно.
    def test_add_book_in_favorites_when_book_already_in_favourites_not_added_to_list(self):
        collector = BooksCollector()
        name = 'Галопом по Вселенной'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert collector.favorites == [name]

    # Тест метода delete_book_from_favorites. Проверяет, что если книга есть в favorites, метод delete_book_from_favorites удаляет ее из favorites.
    def test_delete_book_from_favorites_when_book_in_favourites_deleted_from_list(self):
        collector = BooksCollector()
        name = 'Галопом по Вселенной'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    # Тест метода get_list_of_favorites_books. Проверяет, что метод выводит текущий список избранных книг.
    def test_get_list_of_favorites_books_when_book_added_returns_list(self):
        collector = BooksCollector()
        name = 'Галопом по Вселенной'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]
