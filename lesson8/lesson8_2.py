class ZeroDivisionException(ZeroDivisionError):
    """Новое исключение деления на ноль"""
    pass


def main():
    (dividend, divisor) = input('Введите делимое и делитель через проьел ').split(' ')
    try:
        if not float(divisor):
            raise ZeroDivisionException
        quotient = float(dividend) / float(divisor)
        print('Вы не смогли сломать програму')
    except ZeroDivisionException:
        print('На ноль делить нельзя')