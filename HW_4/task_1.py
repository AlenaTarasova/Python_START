"""
Выведите список простых множителей натурального числа N.

Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""
n = int(input("Введите n : "))
factors = []
d = 2
m = n
while d * d <= n:
    if n % d == 0:
        factors.append(d)
        n //= d
    else:
        d += 1
factors.append(n)
print('{} = {}' .format(m, factors))
