from my_utils import get_resource_path
from collections import namedtuple


def numbers_translator():
    """Запись в файл которого нет"""
    # получаем путь к файлу ресурсов
    full_path = get_resource_path('p4.txt')
    full_path_rus = get_resource_path('p4_rus.txt')
    # создаем кортеж для хранения инормации о сотрудниках
    i_nums = namedtuple('International_nums', ['digit', 'name'])
    # упрощенное решение
    translator = ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
    sep = ' — '
    # читаем исходный файл
    with open(full_path, 'r', encoding='utf-8') as file:
        eng_num = [i_nums(line.split(sep)[1].replace('\n', ''), line.split(sep)[0]) for line in file.readlines()]

    # записываем данные в новый файл
    with open(full_path_rus, 'w', encoding='utf-8') as file:
        rus_nums = [translator[int(num.digit)] + sep + num.digit + '\n' for num in eng_num]
        file.writelines(rus_nums)


