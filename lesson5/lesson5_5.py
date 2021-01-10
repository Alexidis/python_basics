from os import remove, path
from my_utils import get_resource_path


def file_number_writer(file, numbers, separator):
    """
    Писатель чисел в файл
    :param file: полный путь до файла который надо прочитать
    :param numbers: число для записи
    :param separator: разделитель
    :return:
    """
    line_write = numbers + separator
    with open(file, 'a') as f:
        f.write(line_write)


def file_number_reader(file,  separator):
    """
    Читатель чисел из файла
    :param file: полный путь до файла который надо прочитать
    :param separator:  разделитель
    :return: набор прочитанных чисел
    """
    with open(file, 'r') as f:
        # удаляем последний пробел и разбиваем строку по разделителю
        file_numbers = f.readline().rstrip().split(separator)
        numbers = [float(elem) for elem in file_numbers]
    return numbers


def file_num_sum():
    """считатель суммы чисел записанных в файл и прочитанных из него же"""
    # получаем путь к файлу ресурсов
    full_path = get_resource_path('p5.txt')
    # задаем разделитель
    separator = ' '
    # удаляем старый файл если он есть
    if path.exists(full_path):
        remove(full_path)
    print('Вводите текст для записи файл. Для окончания ввода невводя ссимволов нажмите Enter')
    # в цикле записываем числа в файл
    while True:
        # получаем строку ввода
        data = input('')

        # если в строке нет данны, закрываем файл и выходим из программы
        if not data:
            break
        file_number_writer(full_path, data, separator)
    # получаем список чисел и суммируем его
    numbers_sum = sum(file_number_reader(full_path, separator))

    print(f'Сумма ввденых чисел равна {numbers_sum:.2f}')

