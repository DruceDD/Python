# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное (встроенными методами пользоваться нельзя).

# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите целое число: '))
system = int(input('Введите основание системы счисления(2, 3, 8): '))

new_num = []
while num != 0:
    ost = num % system
    new_num.append(ost)
    num //= system

new_num.reverse()
print(*new_num, sep='')