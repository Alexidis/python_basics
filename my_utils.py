from os import path, getcwd


def get_resource_path(file_name):
    # файл будет лежать в специальной директории
    resources_abs_path = 'resources/lesson5'
    # делаем относительный путь к файлу
    file_path = path.join(getcwd(), resources_abs_path)
    # делаем полный путь к файлу
    full_path = path.join(file_path, file_name)

    return full_path
