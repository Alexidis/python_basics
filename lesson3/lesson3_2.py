def user_form_printer(**inner_fields):
    """Вывод данных пользователя"""
    for title, value in inner_fields.items():
        # так как ключ массива не может быть с пробелом то заменяем _ на пробел
        spaced_title = title.replace('_', ' ')
        print(f'{spaced_title}: {value}, ', end='')


# можно было и списком но так показалось эстетичней
fields = dict.fromkeys(['Имя', 'Фамилия', 'Год рождения', 'Город проживания', 'Email', 'Телефон'], '')

for field in fields.keys():
    fields[field] = input(f'Заполните графу \'{field}\' ')

user_form_printer(Имя=fields['Имя'], Фамилия=fields['Фамилия'], Год_рождения=fields['Год рождения'],
                  Город_проживания=fields['Город проживания'], Email=fields['Email'], Телефон=fields['Телефон'])
