def inner_fact(some):
    """Промежуточные значения факториала"""
    # инициируем начальное значение
    cur = 1
    for i in range(1, some+1):
        # вычисляем текущее значение
        cur *= i

        yield cur


def main():
    l7_item = int(input('Введите число факториал которого необходимо вычислить '))
    i = 1
    for el in inner_fact(l7_item):
        print(f'На {i}-ом шаге значение факториала равно {el}')
        i += 1
