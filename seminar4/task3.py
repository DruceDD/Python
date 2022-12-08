# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input())
b = int(input())

if a > b:
    high = a
else:
    high = b
while(True):
    if high % a == 0 and high % b == 0:
        nok = high
        break
    high += 1
print("Для чисел", a, "и", b, "НОК -", nok)


# a = int(input())
# b = int(input())
#
# p = a * b
#
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# nod = a + b
# nok = p // nod
# print(nok)