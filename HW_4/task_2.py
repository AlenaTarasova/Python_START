"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""
A = [1, 2, 3, 2, 5, 1]
found = set()
found_again = set()

for a in A:
    if a in found_again:
        continue
    if a in found:
        found.remove(a)
        found_again.add(a)
    else:
        found.add(a)

print(list(found))
