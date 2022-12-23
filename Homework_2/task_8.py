# Реализуйте алгоритм перемешивания списка.

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите количество элементов списка: '))
numbers = list(n)
print('Случайно созданный список из ' + str (n)+ ' элементов ' + str(numbers))
for i in range (len(numbers)):
    random_num = randint(i, n-1)
    temp = numbers[i]
    numbers[i] = numbers[random_num]
    numbers[random_num] = temp

print('Перемешаный список '+ str(numbers))