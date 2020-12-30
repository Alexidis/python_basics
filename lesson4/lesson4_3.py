def twenty_multiples():
    """Генерация списка с помощью гератора списков"""
    return [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]


def main():
    print(f'Список чисел кратных 20 или 21 в интервале от 20 до 240 {twenty_multiples()}')
