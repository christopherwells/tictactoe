from random import randint
from sys import exit


class Game:
    """Contains all settings for a new game and game logic."""

    def __init__(self):
        # start with new board
        self.board = [" " for i in range(9)]
        self.player = "O"
        self.computer = "X"

    def draw_board(self):
        print("\n ", self.board[0], " | ", self.board[1], " | ", self.board[2])
        print("-" * 17)
        print(" ", self.board[3], " | ", self.board[4], " | ", self.board[5])
        print("-" * 17)
        print(" ", self.board[6], " | ", self.board[7], " | ", self.board[8])

    def make_move(self, player_move):
        # check for stalemate first
        if " " not in self.board:
            self.draw_board()
            print("Game is tied.")
            exit()
        else:
            pass

        # players turn
        if player_move:
            making_move = True
            while making_move:
                # if position is empty, allow move
                position = int(input())
                if self.board[position] == " ":
                    self.board[position] = self.player
                    return False
                else:
                    continue
        else:
            # computers turn
            making_move = True
            while making_move:
                # pick a random empty position
                position = randint(0, 8)
                if self.board[position] == " ":
                    self.board[position] = self.computer
                    return False
                else:
                    continue

    def check_board(self, char):
        # check for winning line
        win = [
            "012", "345", "678",  # horizontal
            "036", "147", "258",  # vertical
            "048", "246"          # diagonal
        ]
        # if char exists at positions i,j,k its a winning line
        for n in range(len(win)):
            i, j, k = int(win[n][0]), int(win[n][1]), int(win[n][2])
            if self.board[i] == char and self.board[j] == char and self.board[k] == char:
                print(f"Winning line at positions {i} {j} {k}")
                # highlight line
                self.board[i] = i
                self.board[j] = j
                self.board[k] = k
                self.draw_board()
                exit(0)
            else:
                continue

    # game loop
    def loop(self):
        while True:
            self.draw_board()
            self.make_move(True)
            self.check_board(self.player)
            self.draw_board()
            self.make_move(False)
            self.check_board(self.computer)


game = Game()
game.loop()
