def elem_replacement():
    """Перемена мест элментов в массиве"""
    list_len = int(input('Введите длину списка '))
    changing_list = [input('Введите элемент амаршрута ') for i in range(list_len)]
    print(f'Ваш список выглядит так {changing_list}')
    for i, value in enumerate(changing_list):
        # находим индекс жоемент с которым будем обменивать элемент i
        next_i = i + 1
        # меняем только на четных элементах и если существует индекс замещения
        if i % 2 == 0 and next_i <= list_len - 1:
            changing_list[i], changing_list[next_i] = changing_list[next_i], changing_list[i]
    print(f'Список после изменения {changing_list}')
