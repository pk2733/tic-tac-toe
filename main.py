import os

os.system("cls")


class Board:
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("--------------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("--------------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))
        print("--------------")

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):
        for combo in [[1, 2, 3], [3, 4, 5], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False

            if result:
                return True

        return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


board = Board()


def print_header():
    print("Welcome to Tic-Tac-Toe\n")


def refresh_screen():
    os.system("cls")
    print_header()
    board.display()


refresh_screen()

while True:
    refresh_screen()
    x_choice = int(input("\nX) Please choose 1 - 9. > "))

    board.update_cell(x_choice, "X")

    refresh_screen()

    if board.is_winner("X"):
        print("\nX wins\n")
        play_again = input("Would you like to play again? (y/n) > ")
        if play_again == "y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\nTie game\n")
        play_again = input("Would you like to play again? (y/n) > ")
        if play_again == "y":
            board.reset()
            continue
        else:
            break

    o_choice = int(input("\nO) Please choose 1 - 9. > "))

    board.update_cell(o_choice, "O")

    if board.is_winner("O"):
        print("\nO wins\n")
        play_again = input("Would you like to play again? (y/n) > ")
        if play_again == "y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\nTie game\n")
        play_again = input("Would you like to play again? (y/n) > ")
        if play_again == "y":
            board.reset()
            continue
        else:
            break
