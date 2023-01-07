from typing import Optional


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_:int, name:str, pages:int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'



class Library:
    BOOKS_DATABASE = [
        {
            "id": 1,
            "name": "test_name_1",
            "pages": 200,
        },
        {
            "id": 2,
            "name": "test_name_2",
            "pages": 400,
        }
    ]

    class Book:
        def __init__(self, id_: int, name: str, pages: int):
            self.id = id_
            self.name = name
            self.pages = pages

        def str(self):
            return f'Книга "{self.name}"'

        def repr(self):
            return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'

    class Library:

        def __init__(self, books: Optional[list] = None):
            self.books = [] if books is None else books

        def get_next_book_id(self):
            if self.books == []:
                return 1
            else:
                last_book_id = self.books[-1].id
                return last_book_id + 1

        def get_index_by_book_id(self, book_id: int):
            counter = 0
            for _ in self.books:
                if _.id == book_id:
                    return counter
                counter += 1
            raise ValueError("Книги с запрашиваемым id не существует")

    if __name__ == '__main__':
        empty_library = Library()  # инициализируем пустую библиотеку
        print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

        list_books = [
            Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
        ]
        library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
        print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

        print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
