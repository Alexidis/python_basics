def sum_quit(numbers):
    """Сумма и выход"""

    # инициируем начальные значения суммы и выхода
    s = 0
    q = False
    # суммируем все числа
    for number in numbers:
        # если они числа
        if number.isdigit():
            s += float(number)
        # иначе выходим, и передаем сигнад о выходе во вне
        else:
            q = True
            break
    return s, q


print('Введите через пробел три числа ')
total_sum = 0
while True:
    # получаем список чисел
    current_numbers = input().split()
    # получаем сумму текущего набора и сигнал о выходе
    current_sum, esc = sum_quit(current_numbers)
    # расчитываем общую сумму
    total_sum += current_sum
    print(f'Сумма всех чисел равна {total_sum}')

    # выходим при получении надлежащего сигнала
    if esc:
        break
