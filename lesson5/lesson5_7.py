from my_utils import get_resource_path
from json import dumps


def profit_calculator():
    """расчет прибыли"""
    # получаем путь к файлу ресурсов
    import_file_name = get_resource_path('p7.txt')
    # получаем путь к файлу в который будем писать
    export_file_name = get_resource_path('p7_json.txt')
    # инициализируем начальные значения
    average_profit = 0
    sep = ','
    firms = {}
    # читаем строки из файла, чтобы не держать файл сразу выходим
    with open(import_file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    firms_count = len(lines)
    # подсчет средний прибыти и формирования списка фирм
    for line in lines:
        # разбиваем строку на отдельные поля
        fields = line.split(sep)
        # получаем данные из соотвествующих полей
        name = fields[0]
        proceeds = float(fields[2])
        costs = float(fields[3])
        # считаем прибыли
        profit = proceeds - costs
        # если прибыль есть добавляем сумму к расчету средней
        if profit > 0:
            average_profit += profit
        # сохраняем информацию о прибыли
        firms[name] = profit
    # получаем итоговое значений средней прибыли
    average_profit /= firms_count
    # формируем итоговый список
    firms_budget = [firms, {'average_profit': average_profit}]

    # формируем данные для записи
    export_data = dumps(firms_budget)

    # сохраняем данные в файл
    with open(export_file_name, 'w', encoding='utf-8') as file:
        file.write(export_data)
