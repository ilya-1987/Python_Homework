# Пользователь вводит число N. Затем он вводит личные данные 
# (имя и возраст) своих N друзей. Создайте список friends и добавьте 
# в него N словарей с ключами name и age. Найдите самого младшего из 
# друзей и выведите его имя.

friends = []
n = int(input("Введите количестводрузей: "))
for i in range (n):
    name = input('Введите имя друга: ')
    age = int(input('Введите возраст друга: '))
    friends.append(dict(name=name, age=age))

min_age = min(friends, key=lambda x: x['age'])
print('Самый младший из друзей', min_age['name'])