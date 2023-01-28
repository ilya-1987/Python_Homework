import os.path
import datetime


def log_cash(rezhim):
     
    if rezhim == 'импорт':
        with open('/home/userpc/Документы/Python_Homework/Homework_7/log.txt', 'a', encoding='utf-8') as file:
            file.write(f'Чтение из файла: {str(datetime.datetime.now())} \n')
    else:
        with open('/home/userpc/Документы/Python_Homework/Homework_7/log.txt', 'a', encoding='utf-8') as file:
            file.write(f'Запись в файл: {str(datetime.datetime.now())} \n')
    