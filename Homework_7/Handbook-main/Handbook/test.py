import csv

#def search ():
surname=input('Введите фамилию: ')
csv_file=csv.reader(open('/home/userpc/Документы/Python_Homework/classmates.csv', 'r'))
for row in csv_file:
    if surname == row[0]:
        print(row)
          
