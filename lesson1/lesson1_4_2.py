def greatest_digit():
    """Поиск наибольшей цифры в числе."""
    custom_int = int(input('Введите целое положительное число '))

    # разряд цифры в числе
    rank = 1
    greatest_num = 0

    # определяем максимальный разряд
    while custom_int // rank > 10:
        rank *= 10

    # проверяем все разряды
    while rank >= 1:
        # находим цифру соотвествующую разряду
        curr_num = custom_int // rank
        # определяем текущий максимум
        greatest_num = max(curr_num, greatest_num)
        # убираем последний разряд из числа
        custom_int -= curr_num * rank
        # переходим на младший разряд
        rank //= 10

    print(f'Наибольшая цифра в веденом числе {greatest_num}')
