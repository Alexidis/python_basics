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