class NonNumericListError(Exception):
    """
    Иаключение принадлежности элемента списка к числам
    """
    pass


def main():
    my_list = []
    while True:
        num_to_add = input('Введите число ')
        try:
            # Если введено стоп слово выходим цикла
            if num_to_add == 'stop':
                break
            # Если введено не число поднимаем исключение
            if not num_to_add.isdigit():
                raise NonNumericListError

            # если исключения не было и не введено сто слово расширяем список
            my_list.append(float(num_to_add))
        # Если поймали исключение выводим сообщение
        except NonNumericListError:
            print('Вывели не число')
    # Принтим итоговой список
    print(f'Итоговы список {my_list}')
