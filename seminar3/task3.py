# 3. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# Подсказка: можно использовать модуль datetime

import time

def randomize (n):
    str_time = str(time.time())
    str_time = str_time.replace('.', '')
    return int(str_time) % n

print(randomize(100))