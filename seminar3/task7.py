# 7. Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список
# и выведите их в порядке возрастания.
#
# Входные данные
# 1 3 2
# 4 3 2
#
# Выходные данные
# 2 3

sp1 = [1, 3, 2]
sp2 = [4, 3, 2]

# sp1.sort()
# for i in range(len(sp1)):
#     for j in range(len(sp2)):
#         if sp1[i] == sp2[j]:
#             print(sp1[i])

a = set(sp1)
b = set(sp2)

i = a.intersection(b)
res = list(i)
print(*res)