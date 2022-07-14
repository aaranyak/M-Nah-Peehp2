import numpy as np
from utilfuncs import *
class ChessException(Exception):
    """Base exception for all chess exceptions"""
    pass

class IllegalMove(ChessException):
    def __init__(self, piece, tile):
        self.message = "Sorry, you cannot move your " + name_piece(piece) + " to this square."
        super(ChessException, self).__init__(self.message)


class KilledPiece(ChessException):
    def __init__(self, piece):
        self.message = "Sorry, your " + name_piece(piece) + " has been eaten"
        super(ChessException, self).__init__(self.message)
