def greatest_prev(sub_list):
    """Фильтрация значений относительно предыдущих"""
    # значения индексов списка
    list_indices = range(1, len(sub_list))
    # генерируем новый список в котором остались только элементы со значением большим чем у соседа слева
    new_list = [sub_list[i] for i in list_indices if float(sub_list[i]) > float(sub_list[i - 1])]
    return new_list
