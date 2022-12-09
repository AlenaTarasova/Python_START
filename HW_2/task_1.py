"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""
num = input("Введите дробное число (целую часть отделить точкой): ")  
x = num.split(".") 
a = int(x[0]) 
b = int(x[1]) 
sum = 0
while (a > 0): 
    sum = sum + (a % 10)
    a = a // 10
while (b > 0): 
    sum = sum + (b % 10)
    b = b // 10
print(sum)