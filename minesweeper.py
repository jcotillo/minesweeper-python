from board import Board
from pyemojify import emojify

class mineSweeper:
    def __init__(self):
        self.board = Board()
        self.won = False
        self.game_over = False

    def play(self):
        while not self.game_over:
            self.board.draw()
            self.user_input()
            self.determine_state()
        self.print_result()

    def determine_state(self):
        if self.board.remainingTiles == 0:
            self.won = True
            self.game_over = True
        elif self.board.state == -1:
            self.game_over = False
        else:
            print "{} tiles left to uncovert to win. {} bomb still out there though".format(self.board.remainingTiles, 10)

    def user_input(self):
        print emojify(":sparkles: :sparkles: input coords :sparkles: :sparkles:")
        try:
            x,y,f = input("(x,y, flag boolean):")
        except ValueError:
            print "woops! forgot an arg there. Probably the flag. Try again."
            x,y,f = input("(x,y, flag boolean):")
        self.board.play(x,y, f)

    def print_result(self):
        if self.won:
            print emojify("YAY YOU WON :sparkles:")
        else:
            print emojify("oh no! You lost...:sparkles:")

mi = mineSweeper()
mi.play()
