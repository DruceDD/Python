# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

#[1.1, 1.2, 3.1, 5.03, 10.01] => 0.19

numb_list = [1.1, 1.2, 3.1, 5.03, 10.01]
dr_list = []

for i in range(len(numb_list)):
    dr = (int(numb_list[i]*100)) % 100
    dr_list.append(dr)

max_dr = max(dr_list)
min_dr = min(dr_list)

print(numb_list)
print(' минимальная дробная часть', min_dr, '\n', 'максимальная дробная часть', max_dr)
print((max_dr - min_dr) / 100)