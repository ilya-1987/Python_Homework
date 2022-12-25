# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите количество элементов списка: '))
numbers = list(n)
print(f'Cозданный список {numbers}')


def pari(list):
    list1 = []
    count = -1
    i = 0
    lenf = len(list) / 2
    while i < lenf:
        list1.append(list[i]*list[count])
        count -= 1
        i += 1
    return list1



productlist = pari(numbers)
print(f'Список произведений пар чисел {productlist}')