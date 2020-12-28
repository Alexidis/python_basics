def inner_fact(some):
    """Промежуточные значения факториала"""
    # инициируем начальное значение
    cur = 1
    for i in range(1, some+1):
        # вычисляем текущее значение
        cur *= i

        yield cur
