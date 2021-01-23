def div_func(dividend, divider):
    """Деление с нулем"""
    # Если делитель будет 0 вернем None
    if not divider:
        return None
    else:
        return dividend / divider


def main():
    user_dividend = int(input('Введите делимое '))
    user_divider = int(input('Введите делитель'))
    quotient = div_func(user_dividend, user_divider)

    print(f'Результат деления {user_dividend} на {user_divider} равен {quotient}')
