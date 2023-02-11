if __name__ == "__main__":
    import doctest


    class Liquids:
        """Базовый класс жидкостей"""
        def __init__(self, brand: str, volume: int):
            """
            Создание и подготовка к работе объекта "Жидкости"

            :param brand: Название производящей компании
            :param volume: Объём жидкости
            """
            self._brand = brand  # уникален для данного класса, поэтому должен использоваться только внутри класса
            self._volume = volume  # для избежания искажений значений

        @property
        def brand(self):
            return self._brand

        @property
        def volume(self):
            return self._volume

        @volume.setter
        def volume(self, new_volume: int):
            if not isinstance(new_volume, int):
                raise TypeError("Новое значение должно быть только целым числом")
            if new_volume <= 0:
                raise ValueError("Новое значение может быть только положительным числом")
            self._volume = new_volume

        def __str__(self):
            return f"Имя компании {self.brand}. Объём {self.volume}"

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r}, volume={self.volume!r})"

        def add_water(self, water: int) -> int:
            """
            Разбавление водой
            :param water: Объём воды
            :return: Новый объём жидкости

            Примеры:
            >>> coffee = Liquids("Nescafe", 40)
            >>> coffee.add_water(20)
            """
            if not isinstance(water, int):
                raise TypeError("Количество воды должно быть только целым числом")
            if water <= 0:
                raise ValueError("Количество воды может быть только положительным числом")
            ...

    class Drinks(Liquids):
        """Напитки"""
        def __init__(self, brand: str, volume: int, sugar: float):
            """
            Создание и подготовка к работе объекта "Напитки"
            :param sugar: Количество сахара

            Примеры:
            >>> hot_chocolate = Drinks("Красный Октябрь", 50, 4.2)
            """
            super().__init__(brand, volume)
            self.sugar = sugar

        @property
        def sugar(self):
            return self.sugar

        @sugar.setter
        def sugar(self, sugar: float):
            if not isinstance(sugar, float):
                raise TypeError("Количество сахара может быть только числом с плавающей запятой")
            if sugar < 0:
                raise ValueError("Количество сахара может быть только положительным числом")

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r}, volume={self.volume!r}), sugar={self.sugar!r}"

    class Paints(Liquids):
        """Краски"""
        def __init__(self, brand: str, volume: int, material: float):
            """
            Создание и подготовка к работе объекта "Напитки"
            :param material: Материал

            Примеры:
            >>> red_paint = Paints("Tikkurila", 23, "Акрил")
            """
            super().__init__(brand, volume)
            self.material = material

        @property
        def material(self):
            return self.material

        @material.setter
        def material(self, material: str):
            if not isinstance(material, str):
                raise TypeError("Материал может быть только строкой")

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r}, volume={self.volume!r}), material={self.material!r}"

        doctest.testmod()