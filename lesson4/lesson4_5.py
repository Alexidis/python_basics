from functools import reduce


def list_production(low_bound, high_bound):
    """Произведение четных элементов списка"""
    origin_list = [i for i in range(low_bound, high_bound+1) if i % 2 == 0]
    return reduce(lambda prev, curr: prev * curr, origin_list)


def main():
    l5_low_bound, l5_high_bound, = input('Введите верхнюю и нижнюю границы ').split()
    print(f'{list_production(int(l5_low_bound), int(l5_high_bound))}')
