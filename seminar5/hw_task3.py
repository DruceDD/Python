# 3. Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))

def draw_board(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-' * 13)

def take_input(player):
    valid = False
    while not valid:
        player_input = input('Выберите ячейку для установки символа "' + player + '": ')
        try:
            player_input = int(player_input)
        except:
            print("Некорректный ввод! Введите число!")
            continue
        if player_input >= 1 and player_input <= 9:
            if (str(board[player_input - 1]) not in 'XO'):
                board[player_input - 1] = player
                valid = True
            else:
                print('Клетка уже занята! Попробуйте снова!')
        else:
            print('Некорректный ввод! Введите число от 1 до 9, чтобы сделать ход!')

def check_win(board):
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for win_cond in win:
        if board[win_cond[0]] == board[win_cond[1]] == board[win_cond[2]]:
            return board[win_cond[0]]
    return False

def game(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        count += 1
        if count > 4:
            tmp = check_win(board)
            if tmp:
                print('Игрок за "', tmp, '" - выиграл!', sep='')
                win = True
                break
        if count == 9:
            print('Ничья!')
            break
    draw_board(board)

game(board)