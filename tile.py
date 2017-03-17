from pyemojify import emojify

class Tile:
    def __init__(self,x,y):
        self.bomb = False
        self.label = emojify(":black_small_square:")
        self.visible = False
        self.flagged = False
