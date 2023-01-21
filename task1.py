class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Страницы могут быть только целочисленными")
        if pages < 0:
            raise ValueError("Количество страниц может быть только положительным числом")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), pages={self.pages!r}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self.pages

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Продолжительность может быть только числом с плавающей запятой")
        if duration < 0:
            raise ValueError("Продолжительность может быть только положительным числом")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), duration={self.duration!r}"

