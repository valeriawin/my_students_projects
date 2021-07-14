# само поле
board = list(range(1, 10))

# вывод текущего поля
def draw_board(board):
    for i in range(3):
        print(board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3])
        if i < 2:
            print("--+---+--")

# обрабатывает, правильно пользователь походил или нет
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        # обработка нечислового ввода
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        # вдруг эта клетка не существует
        if player_answer >= 1 and player_answer <= 9:
            # вдруг она УЖЕ занята крестиком или ноликом
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# анализ победы крестика или нолика
def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

# все происходит с помощью этой функции
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


# не забываем запустить главную функцию, а то ничего не произойдет
main(board)
