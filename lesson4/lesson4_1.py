from sys import argv


def calc_salary():
    """Расчет ЗП"""
    # получаем параметры из вне
    work_time, rate, bonus = argv
    # производим расчет
    salary = (float(work_time) * float(rate)) + float(bonus)
    return salary
