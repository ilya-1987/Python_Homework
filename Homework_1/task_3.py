a = int(input("Введите номер четверти в которой бы Вы хотели узнать диапазон возможных координат: "))
if a == 1:
    print ("В первой четверти диапазон возможых координат будет X > 0 Y > 0")
elif a == 2:
    print ("Во второй четверти диапазон возможых координат будет X < 0 Y > 0")
elif a == 3:
    print ("В третьей четверти диапазон возможых координат будет X < 0 Y < 0")
elif a == 4:
    print ("В четвертой четверти диапазон возможых координат будет X > 0 Y < 0")
else:
    print ("Такой четверти нет.")