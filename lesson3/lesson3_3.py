def my_func(first, second, third):
    """Сумма двух максимумов"""

    # Соединяем все в tuple
    all_params = (first, second, third)
    # находим минимальный элемент
    min_el = min(all_params)
    # суммируем все что не минимальный элемент
    result = sum(filter(lambda el: el != min_el,  all_params))
    return result


a, b, c = input('Введите через пробел три числа ').split()
print(my_func(int(a), int(b), int(c)))
