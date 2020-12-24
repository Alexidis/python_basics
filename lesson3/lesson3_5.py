def sum_quit(numbers):
    """Сумма и выход"""

    # инициируем начальные значения суммы и выхода
    s = 0
    # суммируем все числа
    for number in numbers:
        # если они числа
        if number.isdigit():
            s += float(number)
        # иначе выходим, и передаем сигнад о выходе во вне
        else:
            break
    return s


print('Введите через пробел три числа ')
total_sum = 0
while True:
    # получаем список чисел
    current_numbers = input().split()
    # сумму текущего набора прибавляем к общей сумме
    total_sum += sum_quit(current_numbers)
    print(f'Сумма всех чисел равна {total_sum}')
    esc = list(filter(lambda x: not x.isdigit(), current_numbers))
    # выходим при получении надлежащего сигнала
    if esc:
        break
