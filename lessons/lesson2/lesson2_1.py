def print_variables():
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
