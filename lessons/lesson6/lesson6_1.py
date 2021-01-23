from time import sleep
from collections import namedtuple


class TrafficLight:
    """Класс Светофор
        Содержит константы одинаковые для всех светофоров, а также
        набор методов позволяющих переключать сигналы светофора и проверку корректности введеного сигнала
    """
    __TrafficLight = namedtuple('TrafficLight', ['title', 'order', 'next_order'])
    __RED = __TrafficLight('Красный', 1, 2)
    __YELLOW = __TrafficLight('Жёлтый', 2, 3)
    __GREEN = __TrafficLight('Зелёный', 3, 1)
    __colors = {'red': __RED, 'yellow': __YELLOW, 'green': __GREEN}

    def __init__(self, start_color='green', red_duration=7, yellow_duration=2, green_duration=9):
        """
        Конструктор класса
        :param start_color: начальный сигнал
        :param red_duration: длительность красного сигнала
        :param yellow_duration: длительность желтого сигнала
        :param green_duration: длительность зеленого сигнала
        """
        self.__color = TrafficLight.__colors[start_color]
        self.__durations = {'red': red_duration, 'yellow': yellow_duration, 'green': green_duration}

    def order_check(self, new_color):
        """
        Проверяет корректностб последовательности сигналов
        :param new_color: название сигнала
        :return: является ли ведденый сигнал следующим, относительно текущего состояния
        """
        try:
            return self.__color.next_order == TrafficLight.__colors[new_color].order
        except KeyError:
            print('Не существует указаного сигнала')

    def running(self, new_color):
        """
        Переключение сигнала светофора
        :param new_color: цвет на который происходит переключение
        :return: None
        """
        # приводим название сигнала к стандартному формату
        new_color = new_color.lower()
        # если указан корректный сигнал
        if self.order_check(new_color):
            # меняем состояние сигнала
            self.__color = TrafficLight.__colors[new_color]
        else:
            # поднимаем ошибку
            raise Exception('Указан не верный порядок сигналов')
        # сообщаекм состояние пользователю
        print(f'Загорелся {self.__color.title}')

        # удерживаем сигнал в течении заданого времени
        for sec in range(self.__durations[new_color], 0, -1):
            print(f'{self.__color.title} будет гореть ещё {sec} секунд')
            sleep(1)

    def manual_switch(self):
        """
        оплетка для пользователя
        :return: None
        """
        new_color = input('Введите название следующий сигнала светофора на английском')
        self.running(new_color)

    def auto_switch(self):
        """
        Автоматический переключатель сигналов светофора
        :return: None
        """
        print(TrafficLight.__colors)
        for color in TrafficLight.__colors:
            self.running(color)


def main():
    traffic_light = TrafficLight()
    traffic_light.auto_switch()
