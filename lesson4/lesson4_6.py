from itertools import count, cycle


def count_iter_creator(start_elem, repeats=5):
    """Не бесконечный итератор последовательности"""
    # вычисляем максимальное количество повторений
    max_repeats = start_elem + repeats
    for i in count(start_elem):
        # т.к. идем с шагом 1 то дополнительный счетчик не вводим
        if i < max_repeats:
            yield i
        else:
            break


def cycle_iter_creator(some_list, repeats=5):
    """Не бесконечный итератор повторений списка"""
    # инициализируем счетчик
    repeat = 0
    # вычисляем сколько потребуется повторений для прокрутки всего спика repeats раз
    max_repeats = len(some_list) * repeats
    for i in cycle(some_list):
        if repeat < max_repeats:
            # перед выдачей значения увеличиваем счетчик, чтобы не уйти в бесконечность
            repeat += 1
            yield i
        else:
            break


def main():
    l6_low_bound = int(input('Введите начальное значение итератора '))
    count_itr = count_iter_creator(l6_low_bound)
    print(f'Из итератора получился список {list(count_itr)}')

    l6_list = input('Введите список для повторения ').split()
    cycle_itr = cycle_iter_creator(l6_list)
    print(f'Из итератора получился список {list(cycle_itr)}')
