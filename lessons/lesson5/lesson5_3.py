from my_utils import get_resource_path
from collections import namedtuple


def oneC_like():
    """Запись в файл которого нет"""
    # получаем путь к файлу ресурсов
    full_path = get_resource_path('p3.txt')
    # создаем кортеж для хранения инормации о сотрудниках
    employee = namedtuple('Employee', ['name', 'salary'])
    # задаем нижний лимит ддохода
    low_limit = 20000

    # читаем данные из файла
    with open(full_path, 'r', encoding='utf-8') as file:
        employees = [employee(i.split()[0], float(i.split()[1])) for i in file.readlines()]
    # расчитываем средний дохож
    avg_salary = sum(employee.salary for employee in employees) / len(employees)
    # определяем список сотрудников с наименьшим доходом
    poorest_empls = [employee for employee in employees if employee.salary < low_limit]

    print(f'Средний доход всех сотрудников {avg_salary:.2f}')
    print(f'Следующие сотрудники получают меньше {low_limit}')
    for empl in poorest_empls:
        print(f'{empl.name} получает {empl.salary}')
