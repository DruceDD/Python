# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите чиисло n: '))
sp = []

d = 2
while d <= n:
    if n % d == 0:
        n /= d
        sp.append(d)
    else:
        d += 1
print(sp)