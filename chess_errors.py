import numpy as np
from utilfuncs import *
class ChessException(Exception):
    """Base exception for all chess exceptions"""
    pass

class IllegalMove(ChessException):
    def __init__(self, piece, tile):
        super(IllegalMove, self).__init__()
        self.message = "Sorry, you cannot move your " + name_piece(piece) + " to this square."
