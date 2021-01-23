def int_func(mini_str):
    """Перевод строки"""
    return mini_str.title()


def main():
    user_string = input('Введите строку ')
    print(int_func(user_string))
