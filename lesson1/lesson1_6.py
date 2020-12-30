def fitness_tracker():
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
