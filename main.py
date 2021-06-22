
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def printBoard(board_game):
    print("Positions")
    print("1, 2, 3 ")
    print("4, 5, 6 ")
    print("7, 8, 9 ")
    print("\n")
    print(board_game[1] + ' | ' + board_game[2] + ' | ' + board_game[3])
    print('---------')
    print(board_game[4] + ' | ' + board_game[5] + ' | ' + board_game[6])
    print('---------')
    print(board_game[7] + ' | ' + board_game[8] + ' | ' + board_game[9])


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Computer wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return


def checkForWin():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] == mark:
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def playerMove():
    print("\n")
    position = int(input("Enter the position for player 'O':  "))
    insertLetter(player, position)
    return


def compMove():
    best_score = -100
    best_move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key

    insertLetter(computer, best_move)
    return


def minimax(board_game, depth, isMaximizing):
    if checkWhichMarkWon(computer):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        best_score = -100
        for key in board_game.keys():
            if board_game[key] == ' ':
                board_game[key] = computer
                score = minimax(board_game, depth, False)
                board_game[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = 100
        for key in board_game.keys():
            if board_game[key] == ' ':
                board_game[key] = player
                score = minimax(board_game, depth, True)
                board_game[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score


printBoard(board)
player = 'O'
computer = 'X'


while not checkForWin():
    compMove()
    playerMove()
