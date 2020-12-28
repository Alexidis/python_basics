from collections import Counter


def unique_list(some_list):
    """Список без повторений"""
    # создаем словарь с расчитанныым количеством вхождений каждого элемента введеного списка
    list_counter = Counter(some_list)
    return [item for item in some_list if list_counter[item] == 1]
