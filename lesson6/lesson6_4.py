from random import randint, shuffle


class Car:
    """
    Класс "Автомобиль"
    """
    def __init__(self, name, color, acceleration, braking, turning):
        self.speed = 0
        self._acceleration_speed = acceleration
        self._braking_speed = braking
        self._turning_speed = turning
        self.name = name
        self._crime = False
        self.color = color
        self.is_police = False

    def go(self):
        """
        Нажатие на педаль газ
        :return: None
        """
        self.speed += self._acceleration_speed

    def stop(self):
        """
        Нажатие на педаль тормоз
        :return: None
        """
        new_speed = self.speed - self._braking_speed
        self.speed = new_speed if new_speed > 0 else 0

    def turn(self):
        """
        Крутой поворт
        :return: None
        """
        new_speed = self.speed - self._turning_speed
        self.speed = new_speed if new_speed > 0 else 0

    def get_last_distance(self):
        """
        считаем что отрезак проеден за еденицу времени, по этому скорость равна расстоянию
        :return:
        """
        return self.speed

    def is_criminal(self):
        """
        Возращает статус совершения правонарушения
        :return: статус совершения правонарушения
        """
        return self._crime

    def show_speed(self):
        """
        Показывает текущую скорость
        :return: текущая скорость
        """
        msg = f'{self.name} движется со скоростью {self.speed} км/ч'
        return msg


class TownCar(Car):
    """Класс городской автомобиль"""
    def show_speed(self):
        """
        Показываем скорость или фиксируем правонарушение
        :return: статус скоростного режима
        """
        self._crime = self.speed > 60
        return 'Вы превысили скорость' if self._crime else Car.show_speed(self)


class WorkCar(Car):
    """Класс рабочий автомобиль"""
    def show_speed(self):
        """
        Показываем скорость или фиксируем правонарушение
        :return: статус скоростного режима
        """
        self._crime = self.speed > 60
        return 'Вы превысили скорость' if self._crime else Car.show_speed(self)


class PoliceCar(Car):
    """Класс автомобиль полиции"""
    def __init__(self, name, color, acceleration, braking, turning):
        Car.__init__(self, name, color, acceleration, braking, turning)
        self.is_police = True


class SportCar(Car):
    """Класс спортивный автомобиль"""
    pass


class Race:
    """
    Класс гонка
    Учебное хулиганство
    """
    MOTIONS = {1: 'go', 2: 'breaking', 3: 'turn'}

    def __init__(self, racers, distance):
        """
        инициируем участников и длину заезда
        :param distance:
        """
        self.__rating_board = dict.fromkeys(racers, 0)
        self.__distance = distance
        self.__alert = False
        self.__police = PoliceCar('ВАЗ', 'Металик', 32, 8, 3)
        self.__police_dist = 0

    def start_race(self):
        winner = None
        # получаем список участников заезда
        racers = list(self.__rating_board.keys())
        # делаем первый стартовый рывок
        for car in racers:
            car.go()
            self.__rating_board[car] += car.get_last_distance()
        # пока нет победиля
        while not winner:
            # перемешиваем участников что бы у всех были равные шансы
            shuffle(racers)
            for car in racers:
                # все участники двигаются по трассе случайным образом
                motion = randint(1, 3)
                if Race.MOTIONS[motion] == 'go':
                    print(f'{car.name} ускоряется')
                    car.go()
                elif Race.MOTIONS[motion] == 'breaking':
                    print(f'{car.name} тормозит')
                    car.stop()
                else:
                    print(f'{car.name} поворачивает')
                    car.turn()
                # считаем расстояние паройденное участником
                self.__rating_board[car] += car.get_last_distance()
                distance_left = self.__distance - self.__rating_board[car] if self.__distance - self.__rating_board[car] > 0 else 0
                print(f'{car.show_speed()} а до финиша осталось {distance_left}')

                # поднимем тревогу, из если совершенно правонарушение
                if car.is_criminal():
                    self.__alert = True
                # если тревога поднята и гонка не закончена
                if self.__alert and distance_left > 0:
                    # полиция должнга преследовать правонарушителей!
                    self.__police.go()
                    print(f'Полиция преследует преступников со скоростью {self.__police.speed}')
                    self.__police_dist = self.__police.get_last_distance()
                # если кто-нибудь доехал до финиша, завершаем гонку
                if self.__distance <= max(self.__rating_board[car], self.__police_dist):
                    winner = car if self.__rating_board[car] > self.__police_dist else self.__police
                    break
        # и объявляем победителя
        if winner.is_police:
            print(f'Копы на ВАЗике цвета {self.__police.color} всех догнали')
        else:
            print(f'Побеждает {winner.color} {winner.name}')
