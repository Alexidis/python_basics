def greatest_digit():
    """Поиск наибольшей цифры в числе."""
    custom_int = int(input('Введите целое положительное число '))

    # заносим делитель в переменную
    divider = 10
    # получаем значение едениц
    greatest_num = custom_int % divider

    # проверяем все разряды
    while custom_int >= divider:
        # сокращаем введенное число на делитель
        custom_int //= divider
        # находим "еденицу" текущего ранга
        curr_num = custom_int % divider
        greatest_num = max(curr_num, greatest_num)

    print(f'Наибольшая цифра в веденом числе {greatest_num}')
