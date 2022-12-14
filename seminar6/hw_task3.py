# 3. Задача
# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ),
# применив лямбды, filter, map, zip, enumerate, списочные выражения.
# ________________________________________________________________________________________________

# 7. Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список
# и выведите их в порядке возрастания.
#
# Входные данные
# 1 3 2
# 4 3 2
#
# Выходные данные
# 2 3

sp1 = list(map(int, input().split()))
sp2 = list(map(int, input().split()))

a = set(sp1)
b = set(sp2)

i = a.intersection(b)
res = list(i)
print(*res)

# ________________________________________________________________________________________________

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

#[1.1, 1.2, 3.1, 5.03, 10.01] => 0.19

numb_list = [1.1, 1.2, 3.1, 5.03, 10.01]

dr = list(map(lambda x: (int(x * 100 % 100)), numb_list))
max_dr = max(dr)
min_dr = min(dr)

print(numb_list)
print((max_dr - min_dr) / 100)