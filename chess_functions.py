from seek_codes import *
from utilfuncs import *

def is_check(board, colour):
    """Checks if the king of a certian colour is in check"""
    opponent_pieces = get_pieces_from_board(board, not colour) # Get the id's of all the opponent's pieces.
    attacked_squares = []
    for piece in opponent_pieces: # Loop through every piece in the opponent's team.
        piece_squares = get_tiles(piece) # Get all the squares this piece can move to.
        attacked_squares.extend(piece_squares) # Add these to the list of all threatned squares.
    if colour: # If colour is white,
        king_position = get_position_of_piece(4, board) # Get the position of the white king.
    else: # If colour is black,
        king_position = get_position_of_piece(20, board) # Get the position of the black king.
    if king_position in attacked_squares: # If the king's square is attacked,
        return True # Means king is in check.
    else:
        return False # King not in check
