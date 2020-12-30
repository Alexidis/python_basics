def print_simple():
    """Работа  с переменными."""
    simple_string = 'simple_string'
    simple_int = 123
    simple_float = 123.123
    simple_bool = True

    print(f'simple_string: {simple_string},\n'
          f'simple_int: {simple_int},\n'
          f'simple_float: {simple_float}, \n'
          f'simple_bool: {simple_bool}')

    custom_string = input('Введите строку ')
    print(f'Вы ввели {custom_string}')

    custom_int = int(input('Введите целое число '))
    print(f'Вы ввели {custom_int}')

    custom_float = float(input('Введите число с плавабщей точкой '))
    print(f'Вы ввели {custom_float}')
