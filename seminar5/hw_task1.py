# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]

n = int(input('Введите количество слов: '))
sp = []

for i in range(1, n + 1):
    sp.append(input())
print(sp)

sp = list(filter(lambda x: 'абв' not in x, sp))

print(', '.join(sp))