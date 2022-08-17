import numpy as np
from utilfuncs import *
from seek_codes import *
from chess_functions import *
from chess_errors import *
class ChessGame():
    """This represents a basic game of chess
       It provides basic functions for playing a game
    """

    def __init__(self):
        self.board_init_state = [
            [33,2,3,4,5,6,7,34],
            [9,10,11,12,13,14,15,16],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [32,31,30,29,28,27,26,25],
            [36,23,22,20,21,19,18,35]
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
        """Make a move on the chessboard"""
        ptype = get_piece_by_id(piece)[0]
        ptype = get_piece_by_id(piece)[0]
        if ptype != 0 and piece in get_pieces_from_board(self.board): # Check if piece is on board.
            if tile in get_tiles(piece, self.board): # If move is pseudo legal check if it is legal.
                if is_legal(piece, tile, self.board): # If move is legal, play move.
                    if piece == 4 and tile == (0,1): # If white king is castling on king's side
                        self.move_piece(33, (0,2)) # Move rook behind king
                    if piece == 4 and tile == (0,5): # If white king is castling on queen's side
                        self.move_piece(34, (0,4)) # Move rook behind king
                    if piece == 20 and tile == (7,1): # If black king is castling on king's side
                        self.move_piece(36, (7,2)) # Move rook behind king
                    if piece == 20 and tile == (7,5): # If black king is castling on queen's side
                        self.move_piece(35, (7,4)) # Move rook behind king
                    self.move_piece(piece, tile)
                    if piece == 33: # If rook is moved
                        self.board[tile[0]][tile[1]] = 1 # Loses right to castle on that side.
                    if piece == 34: # If rook is moved
                        self.board[tile[0]][tile[1]] = 8 # Loses right to castle on that side.
                    if piece == 35: # If rook is moved
                        self.board[tile[0]][tile[1]] = 17 # Loses right to castle on that side.
                    if piece == 36: # If rook is moved
                        self.board[tile[0]][tile[1]] = 24 # Loses right to castle on that side.
                    if piece == 4: # If white king is moved.
                        pieces_on_board = get_pieces_from_board(self.board)
                        if 33 in pieces_on_board: # If rook has not moved
                            y1, x1 = get_position_of_piece(33, self.board)
                            self.board[y1][x1] = 1 # Loses right to castle on one side.
                        if 34 in pieces_on_board:
                            y2, x2 = get_position_of_piece(34, self.board)
                            self.board[y2][x2] = 8 # Loses right to castle on the other side.
                    if piece == 20: # If black king is moved.
                        pieces_on_board = get_pieces_from_board(self.board)
                        if 35 in pieces_on_board: # If rook has not moved
                            y1, x1 = get_position_of_piece(35, self.board)
                            self.board[y1][x1] = 17 # Loses right to castle on one side.
                        if 36 in pieces_on_board:
                            y2, x2 = get_position_of_piece(36, self.board)
                            self.board[y2][x2] = 24 # Loses right to castle on the other side.
                else:
                    raise IllegalMove(piece, tile)
            else: # If move is not pseudo-legal, raise an error.
                raise IllegalMove(piece, tile)

        else: # If not, raise an error.
            raise KilledPiece(piece)
        self.turn = not self.turn
