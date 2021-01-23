from my_utils import get_resource_path


def school_scheduler():
    """Планировщик школьных занятий"""
    # получаем путь к файлу ресурсов
    file_name = get_resource_path('p6.txt')
    # инициализируем начальные значения
    lessons = {}
    sep = '   '
    empty_type = '—'
    # читаем строки из файла, чтобы не держать файл сразу выходим
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        fields = line.replace('\n', '').split(sep)
        name = fields[0].replace(':', '')
        # отчищаем поля от строковых значений
        lec_count = int(fields[1].replace('(л)', '').replace(empty_type, '') or 0)
        lab_count = int(fields[2].replace('(пр)', '').replace(empty_type, '') or 0)
        practical_count = int(fields[3].replace('(лаб)', '').replace(empty_type, '') or 0)
        # получаем итоговую сумму по уроку
        total_lesson_count = lec_count + lab_count + practical_count
        # формирум словарь
        lessons[name] = total_lesson_count

    print(lessons)

