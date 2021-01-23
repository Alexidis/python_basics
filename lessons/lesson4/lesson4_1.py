import sys


def calc_salary():
    """Расчет ЗП"""
    # получаем параметры из вне
    work_time, rate, bonus = sys.argv
    # производим расчет
    salary = (float(work_time) * float(rate)) + float(bonus)
    return salary


def main():
    sys.argv = input('Введите выработку в часах, ставку за час и премию сотрудника ').split()
    print(f'Зарплата с бонусом составляет: {calc_salary()}')
