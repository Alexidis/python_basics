from abc import ABC, abstractmethod


class Clothes(ABC):
    """Абстрактный класс Одежда"""
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def fabric_consumption(self):
        pass


class Suit(Clothes):
    def __init__(self, title, size):
        """Переопределяем конструктов"""
        Clothes.__init__(self, title)
        self.__size = size

    # getter и setter
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def fabric_consumption(self):
        # создаем реализацию абстрактного метода
        return 2 * self.size + 0.3


class Coat(Clothes):
    def __init__(self, title, height):
        """Переопределяем конструктов"""
        Clothes.__init__(self, title)
        self.__height = height

    # getter и setter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, size):
        self.__height = size

    def fabric_consumption(self):
        # создаем реализацию абстрактного метода
        return self.height * 6.5 + 0.5
