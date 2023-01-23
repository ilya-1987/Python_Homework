#Пользователь вводит число N. Затем он вводит личные данные
#(имя и возраст) своих N друзей. Создайте список friends и добавьте 
#в него N словарей с ключами name и age. Выведите средний возраст всех 
#друзей и самое длинное имя.

from statistics import mean

friends = {}
a = int(input("Введите количестводрузей: "))
for i in range(a):
    name = input("Имя друга: ")
    age = int(input("Возраст друга: "))
    friends[name] = age
    

print('Самое длинное имя друга ' + str(max(friends, key=len)))
print('Средний возраст друзей ' + str(mean(friends[age] for age in friends)))