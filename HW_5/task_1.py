"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""
"""oldstr = str(input("ВВедите слова: "))
newstr = str.replace('а') 
print(newstr)"""

str = str(input("ВВедите слова: "))
print(str.translate({ord(i): None for i in 'абв'}))
