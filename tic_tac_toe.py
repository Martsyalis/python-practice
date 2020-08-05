board = [" " for i in range(9)]


def printBoard():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)

    print()


def player_move(icon):
    printBoard()
    print('Your Turn player {}'.format(icon))
    choice = int(input("Enter your move (1-9): ").strip()) - 1
    if board[choice] == " ":
        board[choice] = icon
    else:
        print()
        print('THat space is taken!')
        player_move(icon)


def is_draw():
    if " " not in board:
        return True
    else:
        return False


def is_victory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


while True:
    player_move("X")
    if (is_victory("X")):
        printBoard()
        print("X Wins! CONGRATULATIONS!")
        break
    elif is_draw():
        printBoard()
        print("Its a Draw!")
        break

    player_move("O")
    if (is_victory("O")):
        printBoard()
        print("X Wins! CONGRATULATIONS!")
        break
