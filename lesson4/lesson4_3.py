def twenty_multiples():
    """Генерация списка с помощью гератора списков"""
    return [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
