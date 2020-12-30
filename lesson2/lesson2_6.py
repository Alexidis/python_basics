def pivot_table():
    """
        Сводная по товарам
        по хорошему это надо разделить на две функции,
        а можно все сделать в одном цикле
    """
    products_qnt = int(input('Введите количество товаров '))
    # инициализируем список товаров
    products = []
    # создаем шаблон словаря характеристик и сводной
    characteristics = ['название', 'цена', 'количество', 'еденицы измерения']
    # заполняем список продуктов и их характеристик
    for i in range(products_qnt):
        product_specification = dict.fromkeys(characteristics)
        for characteristic in characteristics:
            product_specification[characteristic] = input(f'Введите {characteristic} товара ')
        products.append((i + 1, product_specification))

    # инициализируем сводную
    pivot = dict.fromkeys(characteristics, [])
    # заполняем сводную
    for characteristic in characteristics:
        sub_car = []
        for product in products:
            sub_car.append(product[-1][characteristic])
        pivot[characteristic] = sub_car

    print(pivot)
