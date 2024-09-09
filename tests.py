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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        assert "Мастер и Маргарита" in collector.get_books_genre()
        assert collector.get_book_genre("Мастер и Маргарита") == ''

    def test_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.add_new_book("Мастер и Маргарита")
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        collector.add_new_book("Ужасный роман")
        collector.set_book_genre("Ужасный роман", "Ужасы")

        assert collector.get_books_with_specific_genre("Фантастика") == ["Мастер и Маргарита"]
        assert collector.get_books_with_specific_genre("Ужасы") == ["Ужасный роман"]

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Детская книга")
        collector.set_book_genre("Детская книга", "Фантастика")
        collector.add_new_book("Детектив для детей")
        collector.set_book_genre("Детектив для детей", "Детективы")

        assert collector.get_books_for_children() == ["Детская книга"]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.add_book_in_favorites("Мастер и Маргарита")
        assert "Мастер и Маргарита" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.add_book_in_favorites("Мастер и Маргарита")
        collector.delete_book_from_favorites("Мастер и Маргарита")
        assert "Мастер и Маргарита" not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("book_name, genre", [
        ("Книга 1", "Фантастика"),
        ("Книга 2", "Ужасы"),
        ("Книга 3", "Детективы"),
    ])
    def test_adding_books_with_various_genres(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        collector.add_new_book("Ужасный роман")
        collector.set_book_genre("Ужасный роман", "Ужасы")

        expected_genre_dict = {
            "Мастер и Маргарита": "Фантастика",
            "Ужасный роман": "Ужасы"
        }
        assert collector.get_books_genre() == expected_genre_dict