#"Пора учить английский язык", - сказал себе Степа и решил написать 
# программу для изучения английского языка. Программа получает на вход 
# слово на английском языке и несколько его переводов на русском языке. 
# Составьте словарь, в котором ключ - это английское слово, а значение - 
# это список русских слов.

dictonari = {}
    
 
for i in range (int(input('Введите количество слов: '))):
    
    word = input('Введите слово на английском с переводом: ').split( sep = ' - ', maxsplit=1)
    dictonari[word[0]] = word[1]
 
print (dictonari)