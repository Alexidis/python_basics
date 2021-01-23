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


def main():
    men_coat = Coat('Мужское пальто', 12)
    print(f'На пальто для мужчины ростом {men_coat.height} необходимо {men_coat.fabric_consumption()} метров ткани')
    men_coat.height += 5
    print(f'А на пальто для мужчины ростом {men_coat.height} необходимо {men_coat.fabric_consumption()} метров ткани')

    kid_suit = Suit('Детский костюм', 30)
    print(f'На костюм размером {kid_suit.size} для ребенка необходимо {kid_suit.fabric_consumption()} метров ткани')
    kid_suit.size += 5
    print(f'А на костюм размером {kid_suit.size} для ребенка необходимо {kid_suit.fabric_consumption()} метров ткани')
