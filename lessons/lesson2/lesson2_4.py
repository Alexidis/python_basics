def separate_string():
    """Биение строки"""
    separator = ' '
    user_string = input('Ведите сроку ')
    for string_idx, word in enumerate(user_string.split(separator)):
        print(f'№{string_idx + 1} {word[:10]}')
