"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""

from random import randint

number = int (input("Введите натуральное число: "))
spisok = [randint(-number, number) for _ in range(number)]
print (spisok)

res = 1
with open ('indexes.txt', 'r') as file:
    for line in file:
        index = int(line)
        if number > index >= -number:
            res *= spisok[index]
print (res)