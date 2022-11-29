# 4. Напишите программу, которая проверяет пятизначное число на палиндром.

num = input("Введите число: ")

# count = 0
# for i in range(len(num) // 2):
#     if num[i] == num[-1 - i]:
#         count += 1
# if count == len(num) // 2:
#     print("Число - палиндром")
# else:
#     print("Число - не палиндром")

rev_num = num[::-1]
if rev_num == num:
    print("Число - палиндром")
else:
    print("Число - не палиндром")