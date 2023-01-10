"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""

float_list = [1.1, 1.2, 3.1, 5, 10.01]
my_list = []
for num in float_list:
    my_list.append(num-int(num))
res = max(my_list) - min(my_list)
print (round(res, 2)*10)