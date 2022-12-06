# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class RedBook:
    def __init__(self, animal: str, population: int):
        """
        Создание и подготовка к работе объекта "Красная книга"

        :param animal: Название животного
        :param population: Численность оставшихся животных

        Примеры:
        >>> redbook = RedBook("Панда", 45000)
        """
        if not isinstance(animal, str):
            raise TypeError("Название животного имеет только тип str")
        self.animal = animal

        if not isinstance(population, int):
            raise TypeError("Численность животных имеет только тип int")
        if population < 0:
            raise ValueError("Численность животных может быть только положительным числом")
        self.population = population

    def is_animal_extinct(self) -> bool:
        """
        Метод проверяет, является ли животное вымершим

        :return: Является ли животное вымершим

        Примеры:
        >>> redbook = RedBook("Сумчатый волк", 0)
        >>> redbook.is_animal_extinct()
        """
        ...

    def animal_population_increasing(self, add_population: int) -> None:
        """
        Увеличение численности животного
        :param add_population: Число животных, которое прибавилось

        :return: Увеличенная численность

        Примеры:
        >>> redbook = RedBook("Амурский Тигр", 5000)
        >>> redbook.animal_population_increasing(735)
        """
        if not isinstance(add_population, int):
            raise TypeError("Значение увеличения численности имеет только тип int")
        if add_population < 0:
            raise ValueError("Значение увеличения численности может быть только положительным числом")
        ...

    def animal_population_decreasing(self, substract_population: int) -> None:
        """
        Уменьшение численности животного
        :param substract_population: Число животных, которое убавилось
        :raise ValueError: Если число уменьшения численности превышает количество животных, то вызываем ошибку

        :return: Уменьшенная численность

        Примеры:
        >>> redbook = RedBook("Белый медведь", 20)
        >>> redbook.animal_population_decreasing(10)
        """
        if not isinstance(substract_population, int):
            raise TypeError("Значение уменьшения численности имеет только тип int")
        if substract_population < 0:
            raise ValueError("Значение уменьшения численности может быть только положительным числом")
        ...


class Chocolate:
    def __init__(self, bar: int, cacao: float):
        """
        Создание и подготовка объекта "Шоколад"

        :param bar: Количество шоколадных плиток
        :param cacao: Количество горячего шоколада

        Примеры:
        >>> chocolate = Chocolate(40, 123.7)
        """
        if not isinstance(bar, int):
            raise TypeError("Количество шоколадных плиток должно быть типа int")
        if bar < 0:
            raise ValueError("Количество шоколадных плиток не может быть отрицательным числом")
        self.bar = bar

        if not isinstance(cacao, (int, float)):
            raise TypeError("Количество горячего шоколада должно быть типа int или float")
        if cacao < 0:
            raise ValueError("Количество горячего шоколада не может быть отрицательным числом")
        self.cacao = cacao

    def eat_chocolate(self, eated: int) -> None:
        """
        Поедание шоколада

        :param eated: Количество съеденного шоколада
        :raise ValueError: Если число съеденного шоколада превышает количество шоколадных плиток, то вызываем ошибку
        :return: Оставшиеся плитки

        Примеры:
        >>> chocolate = Chocolate(50, 98.2)
        >>> chocolate.eat_chocolate(2)
        """
        if not isinstance(eated, int):
            raise TypeError("Количество съеденного шоколада должно быть типа int")
        if eated < 0:
            raise ValueError("Количество съеденного шоколада не может быть отрицательным числом")
        ...

    def drink_chocolate(self, drunk: int) -> None:
        """
        Питьё шоколада

        :param drunk: Количество выпитого шоколада
        :raise ValueError: Если число выпитого шоколада превышает количество горячего шоколада, то вызываем ошибку
        :return: Оставшийся объём горячего шоколада

        Примеры:
        >>> chocolate = Chocolate(50, 98.2)
        >>> chocolate.drink_chocolate(3.2)
        """
        if not isinstance(drunk, (int, float)):
            raise TypeError("Количество выпитого шоколада должно быть типа int или float")
        if drunk < 0:
            raise ValueError("Количество выпитого шоколада не может быть отрицательным числом")
        ...


class SantaClausBag:
    def __init__(self, presents: int, bag_capacity: int):
        """
        Список подарков, которые должен раздать Дед Мороз

        :param presents: Количество подарков
        :param bag_capacity: Вместимость мешка
        """
        if not isinstance(presents, int):
            raise TypeError("Количество подарков должно быть только типа int")
        if presents < 0:
            raise ValueError("Количество подарков может быть только положительным числом")
        if presents > bag_capacity:
            raise ValueError("Количество подарков не может превышать вместимость мешка")
        self.presents = presents

        if not isinstance(bag_capacity, int):
            raise TypeError("Вместимость мешка имеет только тип int")
        self.bag_capacity = bag_capacity

    def give_presents(self, given_to_children: int):
        """
        Раздача подарков

        :param given_to_children: Количество подарков, которые раздали
        :ValueError:  Если количество подарков, которые раздали, превышает количество подарков в мешке,
        то вызываем ошибку

        :return: Оставшееся число подарков

        Примеры:
        >>> bag = SantaClausBag(20, 50)
        >>> bag.give_presents(12)
        """
        if not isinstance(given_to_children, int):
            raise TypeError("Количество подарков, которые раздали, должно быть только типа int")
        if given_to_children < 0:
            raise ValueError("Количество подарков, которые раздали, не может быть отрицательным числом")
        ...

    def add_presents(self, gifts):
        """
        Загрузка подарков в мешок

        :param gifts: Количество загружаемых подарков
        :raise ValueError: Если количество подарков превышает вместимость мешка, то вызываем ошибку

        :return: Новое количество подарков в мешке

        Примеры:
        >>> bag = SantaClausBag(20, 50)
        >>> bag.add_presents(29)
        """
        if not isinstance(gifts, int):
            raise TypeError("Количество загружаемых подарков должно быть только типа int")
        if gifts < 0:
            raise ValueError("Количество загружаемых подарков не может быть отрицательным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()
