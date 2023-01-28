import os.path
from csv import writer
import csv

def search (sn):
    csv_file = csv.reader(open('/home/userpc/Документы/Python_Homework/Homework_7/classmates.csv', 'r'))
    for row in csv_file:
        if sn == row[0]:
            print(row)
        #else:
            #print(f'Данные не найдены')
    

def export (res):
    if os.path.exists('Homework_7/classmates.csv') == False:
        with open('Homework_7/classmates.csv', mode="w", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow(["Фамилия", "Имя", "Отчество", "Номер телефона", "Телефон"])
            file_writer.writerow(res)
    else:
        with open('Homework_7/classmates.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(res)
            f_object.close()