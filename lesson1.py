def first_paragraph():
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


def second_paragraph():
    """Первод секунд в часы, минуты секунды с использованием арифметических операций."""
    custom_seconds = int(input('Введите время в секундах '))

    # целочисленное деление на 3600 дает часы
    hours = custom_seconds // 3600
    # целочисленное деление на 60 остатка от деления на 3600 дает минуты
    minutes = (custom_seconds % 3600) // 60
    seconds = (custom_seconds % 3600) % 60
    # печатаем отформатированую строку
    print(f'Вы ввели время {hours:02d}:{minutes:02d}:{seconds:02d}')


def third_paragraph():
    """Не знаю что это, но я назвал это "Дикое сложение"."""
    custom_nn = input('Введите число n ')
    wild_sum = int(custom_nn) + int(custom_nn * 2) + int(custom_nn * 3)
    print(f'Дикаое сложение дало {wild_sum}')


def fourth_paragraph():
    """Поиск наибольшей цифры в числе."""
    custom_int = input('Введите целое положительное число ')

    # индекс цифры в строке
    i = 0
    # инициализация макисмума
    greatest_num = 0

    # цикл по числу
    while i < len(custom_int):
        # получаем текущую цифру
        curr_num = int(custom_int[i])
        greatest_num = max(curr_num, greatest_num)
        i += 1
    print(f'Наибольшая цифра в веденом числе {greatest_num}')

    
def fourth_paragraph2():
    """Поиск наибольшей цифры в числе."""
    custom_int = int(input('Введите целое положительное число '))

    # разряд цифры в числе
    rank = 1
    greatest_num = 0

    # определяем максимальный разряд
    while custom_int // rank > 10:
        rank *= 10

    # проверяем все разряды
    while rank >= 1:
        # находим цифру соотвествующую разряду
        curr_num = custom_int // rank
        # определяем текущий максимум
        greatest_num = max(curr_num, greatest_num)
        # убираем последний разряд из числа
        custom_int -= curr_num * rank
        # переходим на младший разряд
        rank //= 10

    print(f'Наибольшая цифра в веденом числе {greatest_num}')


def fourth_paragraph3():
    """Поиск наибольшей цифры в числе."""
    custom_int = int(input('Введите целое положительное число '))

    # разряд цифры в числе
    rank = 10
    # получаем значение едениц
    greatest_num = custom_int % 10

    # проверяем все разряды
    while rank <= custom_int:
        # находим "еденицу" текущего ранга
        curr_num = custom_int // rank % 10
        greatest_num = max(curr_num, greatest_num)
        # увеличиваем ранг
        rank *= 10
        
    print(f'Наибольшая цифра в веденом числе {greatest_num}')

def fifth_paragraph():
    """Сложная экономическая задача"""
    proceed = float(input('Введите сумму прибыли '))
    costs = float(input('Введите сумму издержек '))
    # получаем доход
    income = proceed - costs
    if income > 0:
        # тут я возможно не понял условие задачи, но по логике выглядит верно
        print('Фирма отработала с прибылью')
        employee_count = int(input('Введите количество сотрудников '))
        # расчитываем выручку на каждого сотрудника
        employee_proceed = income / employee_count
        # расчитываем рентабильность
        profitability = income / proceed
        print(f'Рентабильность выручки составила {profitability:.4f} '
              f'Прибыль на каждого сотрудника составила {employee_proceed:.4f}')
    elif income < 0:
        print('Фирма отработала с убытком')
    else:
        print('У Вас стагнация')


def sixth_paragraph():
    """Фитнесс трекер"""
    f_day_distance = float(input('Введите количество километров пройденое в первый день '))
    desirable_distance = float(input('Введите количество километров которое нужно пробежать за все время '))
    # текущий результат
    current_result = f_day_distance
    # текущий день
    current_day_num = 1

    # если результат не достигнут, продолжаем бегать
    while current_result < desirable_distance:
        current_result += current_result * 0.1
        current_day_num += 1

    # возвращаем количество дней сколько пришлось бегать для получения результата
    return current_day_num


if __name__ == '__main__':
    first_paragraph()
    second_paragraph()
    third_paragraph()
    fourth_paragraph()
    fourth_paragraph2()
    fourth_paragraph3()
    fifth_paragraph()
    print(sixth_paragraph())



