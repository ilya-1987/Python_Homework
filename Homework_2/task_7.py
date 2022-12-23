# Задайте список из n чисел последовательности (1+1/n)**n и выведите 
# на экран их сумму.4

def in_list(n):
    list = []
    for i in range (1, n+1):
        list.append((1+1/i)**i)
    return list

def sum(list):
    sum=0
    for i in range (len(list)):
        sum=sum + list[i]
    return sum

n = int(input('Введите число N: '))

list = in_list(n)
print(list)
result = sum(list)
print(result)