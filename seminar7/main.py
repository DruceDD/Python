# Задача: Создать калькулятор для вычисления математических примеров (с помощью функции eval),
# организовать меню, добавить систему логирования.
# Расширить функционал калькулятора. Например, добавив в него перевод величин (масс, валют и т.д.),
# или перевод чисел из одной системы счисления в другую.

# import logging
# # если хотим, чтобы логи выводились в консоль
# logging.basicConfig(level=logging.INFO)
# # если хотим, чтобы логи записывались в файл
# logging.basicConfig(filename='log.txt',
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.INFO)
# def main():
#     …
#     logging.info("Данные от пользователя получены")
#     …
#     logging.warning("Ошибка обработки данных")

from controller import main_function

main_function()
