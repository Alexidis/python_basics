def my_pow(x, y):
    """Возведение в степень"""

    # в зависимости от знака определяем множитель. для положительных - умножаем, для отрицательной - делим
    factor = x if y > 0 else 1/x
    # получаем модуль степени
    exp = abs(y)
    # инициируем начальное значение
    comp = 1
    # если стпень 0 то в цикл не пойдем
    for i in range(exp):
        comp *= factor
    return comp


def main():
    a = float(input('Введите действительное положительное число '))
    b = int(input('Введите целое отрицательное число '))
    pow_val = my_pow(a, b)
    print(f'При возведении {a} в {b} получается примерно {pow_val:.10f}')