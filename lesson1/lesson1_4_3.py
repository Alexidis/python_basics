def greatest_digit():
    """Поиск наибольшей цифры в числе."""
    custom_int = int(input('Введите целое положительное число '))

    # разряд цифры в числе
    rank = 10
    # получаем значение едениц
    greatest_num = custom_int % 10

    # проверяем все разряды
    while rank <= custom_int:
        # находим "еденицу" текущего ранга
        curr_num = custom_int // rank % 10
        greatest_num = max(curr_num, greatest_num)
        # увеличиваем ранг
        rank *= 10

    print(f'Наибольшая цифра в веденом числе {greatest_num}')
