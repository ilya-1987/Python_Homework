# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.

num = int(input("Введите натуральное число N: "))
i = 2  # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители для числа {old} будут равны: {lst}")