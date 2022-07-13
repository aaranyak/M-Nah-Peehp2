import numpy as np
from utilfuncs import *
from seek_codes import *
class ChessGame():
    """This represents a basic game of chess
       It provides basic functions for playing a game
    """

    def __init__(self):
        self.board_init_state = [
            [1,2,3,4,5,6,7,8],
            [9,10,11,12,13,14,15,16],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [32,31,30,29,28,27,26,25],
            [24,23,22,20,21,19,18,17]
        ] # Create the state of the board when game begins.
        self.board = np.array(self.board_init_state)
        self.turn = True
    def move_piece(self, piece, tile):
        """Move a piece to another tile"""
        cy,cx = get_position_of_piece(piece, self.board)
        dy,dx = tile
        self.board[cy][cx] = 0
        self.board[dy][dx] = piece
    def make_move(self, piece, tile):
        avail = get_tiles
