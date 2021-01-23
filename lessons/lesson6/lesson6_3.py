class Worker:
    """
    Недоумеваю почему, но это базовый класс Сотрудник
    """
    def __init__(self, surname: str, name: str, position: str, wage, bonus):
        """
        Конструктор базового класса
        :param surname: фамилия
        :param name: имя
        :param position: должность
        :param wage: оклад
        :param bonus: премия
        """
        self.surname = surname
        self.name = name
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """
    Дочерний класс "Должность"
    """
    def get_full_name(self):
        """
        Получение имени сотрудника
        :return: полное имя сотрудника
        """
        return ' '.join((self.surname, self.name))

    def get_total_income(self):
        """
        Получения полной ЗП сотрудника
        :return: полная ЗП сотрудника
        """
        return self._income['wage'] + self._income['bonus']


def main():
    new_worker = Position('Филиппов', 'Артем', 'Специалист', 15100, 35700)
    print(f'Приняли сотрудника {new_worker.get_full_name()}, на должность {new_worker.position}'
          f' с ЗП {new_worker.get_total_income()}')
