def greatest_prev(sub_list):
    """Фильтрация значений относительно предыдущих"""
    # генерируем новый список в котором остались только элементы со значением большим чем у соседа слева
    new_list = [i for i in sub_list if sub_list.index(i) > 0 and float(i) > float(sub_list[sub_list.index(i)-1])]
    return new_list
