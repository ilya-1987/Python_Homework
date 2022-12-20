# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6,782 -> 23
# - 0,56 -> 11

def sum (number):
    sum = 0
    for i in number:
        if i != '.':
            sum = sum + int(i)
    return sum


number = input('Введите вещественное число: ')

print (sum(number))