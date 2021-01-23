def some_economics():
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
