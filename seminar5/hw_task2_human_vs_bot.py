# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход
# можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

candy = int(input('Введите количество конфет: '))

while candy >= 28:
    player = int(input('Введите количество конфет, которое хотите забрать: '))
    while player > 28:
        print('Максимальное количество конфет, которое можно брать - 28шт!')
        player = int(input('Попробуйте снова: '))
    else:
        candy -= player
        print(candy, 'шт конфет осталось', sep='')
        if candy <= 28:
            win = 0
            break
        else:
            if candy <= 57:
                bot = candy - 29
                if bot == 0:
                    bot = random.randint(1, 29)
                    print('Bot решил взять', bot, 'конфету')
                    candy -= bot
                    print(candy, 'шт конфет осталось', sep='')
                    win = 1
                    break
                else:
                    print('Bot решил взять', bot, 'конфет')
                    candy -= bot
                    print(candy, 'шт конфет осталось', sep='')
            else:
                bot = random.randint(1, 29)
                print('Bot решил взять', bot, 'конфет')
                candy -= bot
                print(candy, 'шт конфет осталось', sep='')
                if candy <= 28:
                    win = 1
                    break

if win == 1:
    print('Игрок победил!')
else:
    print('Робот был сильнее (:')