# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))
f1 = not(x or y or z)
f2 = (not x) and (not y) and (not z)
if f1 == f2:
    print("Истина")
else:
    print("Ложь")