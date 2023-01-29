def inp_mod():
    mod = input('Введите режим работы импорт/экспорт: ')
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname


def inp_export():
    name = input('Введите фамилию: ')
    surname = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    description = input('Введите описание телефона (пример: мобильный, домашний, рабочий...): ')
    return '\n', name, surname, phone, description


def view_import(result):
    print(*result, sep='\n')


def view_import_no():
    print('Данные не найдены!')


def view_export():
    print('Ваши данные успешно сохранены!')

def view_data(result):
    print(result)