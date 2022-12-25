# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите количество элементов списка: '))
numbers = list(n)
print(f'Cозданный список {numbers}')

def sum(list1):
    sum = 0
    for i in range (1, len(list1), 2):
        sum += list1[i]
    return sum

list = numbers
result = sum(list)
oddnumbers = []
count = 0
for i in numbers:
    if count % 2 == 1:
        oddnumbers.append(i)
    count += 1

print(f'Элементы стоящии на нечтной позиции списка {oddnumbers}')

print(f'Сумма элементов, стоящих на нечетной позиции списка равна {result}')