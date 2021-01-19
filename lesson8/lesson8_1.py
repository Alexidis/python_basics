class Date:
    """
    Класс дата нашей эры (видимо ээто будет синглтон)
    """
    day = 1
    month = 1
    year = 1970

    def __init__(self, str_date):
        """
        делаем из строки числа и заводим свойства класа
        :param str_date: сторка с датой
        """""
        (day, month, year) = str_date.split('.')
        Date.day = int(day)
        Date.month = int(month)
        Date.year = int(year)

    @classmethod
    def to_int(cls, scale):
        """
        перевод шкалы в int
        :param scale: шкала интовое значение которой хотим получить
        :return: щкала привденая в int
        """
        if scale.lower() == 'day':
            result = Date.day
        elif scale.lower() == 'month':
            result =  Date.month
        elif scale.lower() == 'year':
            result = Date.year
        else:
            result = -1
        return result

    @staticmethod
    def validate(str_date):
        """
        Валидатор
        :param str_date: строка для валидации
        :return: результат проверки валидности
        """
        try:
            (day, month, year) = str_date.split('.')
            if int(year) > 0:
                if 1 <= int(month) <= 12:
                    if int(month) in (1, 3, 5, 7, 8, 10, 12):
                        max_day = 31
                    elif int(month) in (4, 6, 9, 11):
                        max_day = 30
                    elif int(year) % 4:
                        max_day = 29
                    else:
                        max_day = 28
                    if 1 <= int(day) <= max_day:
                        return True
        except (TypeError, ValueError):
            pass
        return False
