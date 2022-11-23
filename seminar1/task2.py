# 2.	Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

count = 0
num = int(input("Введите число: "))
max_num =   num
while count < 4:
    num = int(input("Введите число: "))
    if num > max_num:
        max_num = num
    count += 1

print(max_num)