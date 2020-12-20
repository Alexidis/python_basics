def first_paragraph():
    """Работа  с переменными."""
    common_list = [
        123,
        123.123,
        complex(1, 2),
        'simple_string',
        [1, 2, 3],
        (1, 2, 3),
        {1, 2, 3},
        {'a': 1, 'b': 2, 'c': 3},
        b'123',
        True,
        None]
    for el in common_list:
        print(f'{el} is type of ', type(el))


def second_paragraph():
    """Перемена мест елментов в массиве"""
    list_len = int(input('Введите длину списка '))
    changing_list = [input('Введите элемент амаршрута ') for i in range(list_len)]
    print(f'Ваш список выглядит так {changing_list}')
    for i, value in enumerate(changing_list):
        # находим индекс жоемент с которым будем обменивать элемент i
        next_i = i + 1
        # меняем только на четных элементах и если существует индекс замещения
        if i % 2 == 0 and next_i <= list_len - 1:
            changing_list[i], changing_list[next_i] = changing_list[next_i], changing_list[i]
    print(f'Список после изменения {changing_list}')


def third_paragraph_list():
    """Времена года в списке"""
    mouths = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето',
              'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    current_month_idx = int(input('Ведите номер текущего месяца ')) - 1
    print(f'Сейчас {mouths[current_month_idx]}')


def third_paragraph_dict():
    """Времена года в словаре"""
    mouths = {'1': 'Зима', '2': 'Зима', '3': 'Весна', '4': 'Весна', '5': 'Весна', '6': 'Лето',
              '7': 'Лето', '8': 'Лето', '9': 'Осень', '10': 'Осень', '11': 'Осень', '12': 'Зима'}
    current_month_num = input('Ведите номер текущего месяца ')
    print(f'Сейчас {mouths.get(current_month_num)}')


def fourth_paragraph():
    """Биение строки"""
    separator = ' '
    user_string = input('Ведите сроку ')
    for string_idx, word in enumerate(user_string.split(separator)):
        print(f'№{string_idx + 1} {word[:10]}')


def fifth_paragraph():
    """Рейтинги"""
    # инициализируем рейтинг
    rating = [6, 4, 4, 2]
    # получаем значение нового рейтинга
    new_rate = int(input('Введите новый рейтинг '))

    # если рейтинг уже существуе в списке
    if new_rate in rating:
        # находим индекс последнего вхождения елемента
        idx = rating.index(new_rate) + rating.count(new_rate)
    # оставил три случая потому что для большого списка быстрее проверить края чем перебирать всю колекцию
    # когда индекса не существуе
    # если значение нового рейтинга превышает значение первого рейтинга в списке
    elif new_rate > rating[0]:
        # то добавлять будем в начало списка
        idx = 0
    # # если значение нового рейтинга меньше значение последнего рейтинга в списке
    elif new_rate < rating[-1]:
        idx = len(rating)
    # новый рейтинг необходимо вставить в внутрь списка
    else:
        # получаем минимальное значение со значением превышающим новый рейтинг
        # так как мы знаем что новый рейтинг внутри диапазано, то генератор не будет пустым
        prev_val = min([val for val in rating if val > new_rate])
        # находим индекс последнего вхождения предыдущего елемента
        idx = rating.index(prev_val) + rating.count(prev_val)

    # добавляем новый элемент в исходный массив
    rating.insert(idx, new_rate)

    print(f'Новые значения рейтинга {rating} новый элемент имеет индекс {idx}')


def sixth_paragraph():
    """
        Сводная по товарам
        по хорошему это надо разделить на две функции,
        а можно все сделать в одном цикле
    """
    products_qnt = int(input('Введите количество товаров '))
    # инициализируем список товаров
    products = []
    # создаем шаблон словаря характеристик и сводной
    tmpl = dict.fromkeys(['название', 'цена', 'количество', 'ед'])
    # заполняем список продуктов и их характеристик
    for i in range(products_qnt):
        product_specification = tmpl.copy()
        product_specification['название'] = input('Введите навазние товара ')
        product_specification['цена'] = input('Введите цену товара ')
        product_specification['количество'] = input('Введите количество товара ')
        product_specification['ед'] = input('Введите еденицы измерения товара ')
        products.append((i + 1, product_specification))

    # инициализируем сводную
    pivot = tmpl.copy()
    pivot['название'] = []
    pivot['цена'] = []
    pivot['количество'] = []
    pivot['ед'] = []

    # заполняем сводную
    for product in products:
        pivot['название'].append(product[-1]['название'])
        pivot['цена'].append(product[-1]['цена'])
        pivot['количество'].append(product[-1]['количество'])
        pivot['ед'].append(product[-1]['ед'])

    print(pivot)


if __name__ == '__main__':
    first_paragraph()
    second_paragraph()
    third_paragraph_list()
    third_paragraph_dict()
    fourth_paragraph()
    fifth_paragraph()
    sixth_paragraph()
