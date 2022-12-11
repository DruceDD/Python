# 2. Напишите функцию triangle(a, b, c), которая принимает на вход три длины
# отрезков и определяет, можно ли из этих отрезков составить треугольник.

a, b, c = int(input('Введите сторону треугольника: ')), int(input('Введите сторону треугольника: ')), int(
    input('Введите сторону треугольника: '))


def triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    return False


if triangle(a, b, c) == True:
    print('Это треугольник')
else:
    print('Это не треугольник')
