class Stationery:
    """
    Базовый класс
    """
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen (Stationery):
    def draw(self):
        print(f'Это {self.title} синего цвета')


class Pencil (Stationery):
    def draw(self):
        print(f'Этот {self.title} не заточек')


class Handle (Stationery):
    def draw(self):
        print(f'{self.title} нужен для выжедения')


def main():
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()
    pencil.draw()
    handle.draw()
