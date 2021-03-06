def get_ratings():
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