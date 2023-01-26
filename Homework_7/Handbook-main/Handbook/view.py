def inp_mod():
    mod = input('Введите режим работы (импорт или экспорт): ')
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname

def view_import (result):
    print(result) 

def inp_export():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    sec_name = input('Введите отчество: ')
    phone = int(input('Введите номер телефона: '))
    comment = input('Ведите признак телефона (домашний, рабочий): ')
    return surname, name, sec_name, phone, comment


def view_import_no ():
    print(f'Данные не найдены')