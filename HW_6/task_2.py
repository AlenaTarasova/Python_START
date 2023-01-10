"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""
from collections import Counter
A = [1, 2, 3, 5, 1, 5, 3, 10]
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
dup = {a for a in A if A.count(a) > 1}
print(dup)
counter = Counter(A)
print(list(counter))
