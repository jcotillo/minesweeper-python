from tile import Tile
from random import randint
from pyemojify import emojify

# constants
WIDTH = 40
NUM_BOMBS = 10
COLS = 9
ROWS = 9
count_emoji_dictionary = {"1":":one:","2":":two:", "3":":three:", "4": ":four:", "5": ":five:"}

class Board:
    def __init__(self):
        self.grid = [[Tile(x,y) for y in range(COLS)] for x in range(ROWS)]
        self.place_bombs()
        self.state = 0
        self.remaindingTiles = (ROWS * COLS) - NUM_BOMBS

    def play(self,x,y, flag=False):
        # flag a certain tile
        if not self.inbounds(x,y):
            raise ValueError('Coordinates out of bound.')

        if self.inbounds(x,y) and flag:
            self.grid[x][y].flagged = True
            self.grid[x][y].label = emojify(":triangular_flag_on_post:")
            return

        # if not flagging and it is a bomb
        if self.inbounds(x,y) and self.grid[x][y].bomb:
            self.state = -1
            return
        # start recursive call
        self.reveal(x,y)


    def reveal(self, x, y):
            if not self.inbounds(x,y):
                return

            tile = self.grid[x][y]

            if tile.bomb:
                return

            if tile.visible:
                return

            tile.visible = True
            self.remaindingTiles -= 1
            count = self.count_neighbors(x,y)

            if count > 0:
                tile.label = count_emoji_dictionary[str(count)]
                return

            # recursively check the neighbors
            for (dx,dy) in [(0,1), (0,-1), (-1,0), (1,-1), (-1,1), (-1,-1), (1,0), (1,1)]:
                self.reveal(x+dx, y+dy)

    def count_neighbors(self,x,y):
        count = 0
        for (dx,dy) in [(0,1), (0,-1), (-1,0), (1,-1), (-1,1), (-1,-1), (1,0), (1,1)]:
            new_x = x + dx
            new_y = y + dy

            if self.inbounds(new_x, new_y) and self.grid[new_x][new_y].bomb:
                count += 1

        return count

    def inbounds(self,x,y):
        return (x >= 0 and x < COLS) and (y >= 0 and y < ROWS)

    def place_bombs(self):
        for n in range(NUM_BOMBS):
            # ensures that we end up with NUM_BOMBS bombs in the grid
            while True:
                x = randint(0,8)
                y = randint(0,8)
                if self.grid[x][y].bomb == False:
                    self.grid[x][y].bomb = True
                    break

    def draw(self):
        for row in self.grid:
            for tile in row:
                if tile.visible and tile.label not in count_emoji_dictionary.values():
                    print emojify(":white_small_square:"),
                else:
                    print emojify(tile.label),
            print "\n"
