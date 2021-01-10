from my_utils import get_resource_path
from collections import namedtuple


def count_data(full_file_path):
    """ 
    :param full_file_path: полный путь до файла который надо прочитать
    :return: список словарей с номером строки, количеством слов и самой строкой
    """""
    # создаем кортеж для хранения строк и количества слов в ней
    line_counter = namedtuple('line_counter', ['content', 'word_count'])
    # открываем файл на чтение с поддержкой русских символов
    with open(full_file_path, 'r', encoding='utf-8') as file:
        # заполняем список кортежей строками из файла
        counted_lines = [line_counter(line.replace('\n', ''), len(line.split(' '))) for line in file.readlines()]

    return counted_lines


def file_counter():
    """Подсчет строк и слов в файле"""
    # получаем путь к файлу ресурсов
    file_name = get_resource_path('p2.txt')
    # получаем список посчитанных строк
    counted_lines = count_data(file_name)
    # распечатываем количество строк
    print(f'Всего прочитано строк {len(counted_lines)}')
    # расспечатываем список в удобном формате
    for line in counted_lines:
        print(f'В строке \'{line.content}\' слов {line.word_count}')
