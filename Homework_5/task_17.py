# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

path = 'fileabv.txt'
with open(path, 'r', encoding='utf8')as file:
    text = file.readline().split()

print(text)
find = 'абв'

for word in text:
    if find in word:
        text.remove(word)

print(text)

