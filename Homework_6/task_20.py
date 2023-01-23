#Создайте список из случайных чисел. Найдите количество различных 
# элементов в нем.

from random import randint
 
array=[]
for i in range(5):
    array.append(randint(1,30))
print ('Список из случайных чисел:')
print(' '.join(map(str, array)))

count = 0
unique_array = []
for x in array:
    if x not in unique_array:
        count += 1
        unique_array.append(x)
print ('Количество неповторяющихся элементов в списке:')
print(len(unique_array))