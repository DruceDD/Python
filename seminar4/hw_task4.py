# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите натуральную степень k: '))

ratio = []
m = []
for i in range(k + 1):
    n = random.randint(0, 9)
    ratio.append(n)
print('Список всех коэффицентов:', ratio)

def create(k, ratio):
    for i in range(len(ratio) - 2):
        if ratio[i] == 0:
            continue
        elif ratio[i] == 1:
            x = f'x^{k - i}'
        else:
            x = f'{ratio[i]}x^{k - i}'
        m.append(x)
    for i in range(len(ratio) - 2, len(ratio) - 1):
        if ratio[i] == 0:
            continue
        elif ratio[i] == 1:
            x = 'x'
        else:
            x = f'{ratio[i]}x'
        m.append(x)
    for i in range(len(ratio) - 1, len(ratio)):
        if ratio[i] == 0:
            continue
        else:
            x = f'{ratio[i]}'
        m.append(x)
    return m

mnogoch = ' + '.join(create(k, ratio)) + ' = 0'
print(mnogoch)

with open('hw_task4.txt', 'w') as file:
    file.write(mnogoch)