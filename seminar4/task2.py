# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1. с помощью математических формул нахождения корней квадратного уравнения
# 2. с помощью дополнительных библиотек Python

a, b, c = float(input()), float(input()), float(input())

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(' x1 =', x1, '\n', 'x2 =', x2)
elif d == 0:
    x = (-b) // (2 * a)
    print('x =', x)
else:
    print('корней нет')