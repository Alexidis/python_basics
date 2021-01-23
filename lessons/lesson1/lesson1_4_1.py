def greatest_digit():
    """Поиск наибольшей цифры в числе."""
    custom_int = input('Введите целое положительное число ')

    # индекс цифры в строке
    i = 0
    # инициализация макисмума
    greatest_num = 0

    # цикл по числу
    while i < len(custom_int):
        # получаем текущую цифру
        curr_num = int(custom_int[i])
        greatest_num = max(curr_num, greatest_num)
        i += 1
    print(f'Наибольшая цифра в веденом числе {greatest_num}')
