def unique_list(some_list):
    """Список без повторений"""
    return [i for i in some_list if some_list.count(i) == 1]
