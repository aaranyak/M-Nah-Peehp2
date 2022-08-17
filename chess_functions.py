from seek_codes import *
from utilfuncs import *

def is_check(board, colour):
    """Checks if the king of a certian colour is in check"""
    opponent_pieces = get_pieces_from_board(board, not colour) # Get the id's of all the opponent's pieces.
    attacked_squares = []
    for piece in opponent_pieces: # Loop through every piece in the opponent's team.
        piece_squares = get_tiles(piece, board) # Get all the squares this piece can move to.
        attacked_squares.extend(piece_squares) # Add these to the list of all threatned squares.
    if colour: # If colour is white,
        king_position = get_position_of_piece(4, board) # Get the position of the white king.
    else: # If colour is black,
        king_position = get_position_of_piece(20, board) # Get the position of the black king.
    if king_position in attacked_squares: # If the king's square is attacked,
        return True # Means king is in check.
    else:
        return False # King not in check
def move_piece_on_board(piece, tile, board):
    """Return board with a moved piece"""
    board = np.copy(board)
    cy,cx = get_position_of_piece(piece, board)
    if piece == 4 and tile == (0,1): # If white king is castling on king's side
        move_piece_on_board(33, (0,2), board) # Move rook behind king
    if piece == 4 and tile == (0,5): # If white king is castling on queen's side
        move_piece_on_board(34, (0,6), board) # Move rook behind king
    if piece == 20 and tile == (7,1): # If black king is castling on king's side
        move_piece_on_board(36, (7,2), board) # Move rook behind king
    if piece == 20 and tile == (7,5): # If black king is castling on queen's side
        move_piece_on_board(35, (7,6), board) # Move rook behind king
    dy,dx = tile
    board[cy][cx] = 0
    board[dy][dx] = piece
    if piece == 33: # If rook is moved
        board[tile[0]][tile[1]] = 1 # Loses right to castle on that side.
    if piece == 34: # If rook is moved
        board[tile[0]][tile[1]] = 8 # Loses right to castle on that side.
    if piece == 35: # If rook is moved
        board[tile[0]][tile[1]] = 17 # Loses right to castle on that side.
    if piece == 36: # If rook is moved
        board[tile[0]][tile[1]] = 24 # Loses right to castle on that side.
    if piece == 4: # If white king is moved.
        pieces_on_board = get_pieces_from_board(board)
        if 33 in pieces_on_board: # If rook has not moved
            y1, x1 = get_position_of_piece(33, board)
            board[y1][x1] = 1 # Loses right to castle on one side.
        if 34 in pieces_on_board:
            y2, x2 = get_position_of_piece(34, board)
            board[y2][x2] = 8 # Loses right to castle on the other side.
    if piece == 20: # If black king is moved.
        pieces_on_board = get_pieces_from_board(board)
        if 35 in pieces_on_board: # If rook has not moved
            y1, x1 = get_position_of_piece(35, board)
            board[y1][x1] = 17 # Loses right to castle on one side.
        if 36 in pieces_on_board:
            y2, x2 = get_position_of_piece(36, board)
            board[y2][x2] = 24 # Loses right to castle on the other side.
    return board
def is_legal(piece, tile, board):
    """Checks if move is legal"""
    col = get_piece_by_id(piece)[1] # Colour of piece.
    board = move_piece_on_board(piece, tile, board) # Make move on separate board.
    if is_check(board, col): # If results in check, move is illegal.
        return False
    else: # Otherwise, move is legal.
        return True

def is_checkmate(board, colour):
    """Checks if it is checkmate."""
    is_checkmate = True
    legal_moves = get_all_moves(board, colour) # Get all legal moves.
    if len(legal_moves) != 0:
        is_checkmate = False
    if is_check(board, colour):
        if is_checkmate:
            return -1 # Checkmate!
        else:
            return 1 # Not Checkmate.
    else:
        if is_checkmate:
            return 0 # Stalemate!
        else:
            return 1 # Not Stalemate.
def get_all_moves(board, colour):
    """Returns all possible moves to play"""
    pieces = get_pieces_from_board(board, colour)
    moves = []
    for piece in pieces: # Loop through all the pieces.
        for move in get_tiles(piece, board): # Play all moves.
            if is_legal(piece, move, board): # If move is legal.
                moves.append((piece, move)) # Add the move
    return moves

def count_material(board, colour):
    """Counts the material of pieces on the board."""
    material = 0
    my_pieces = get_pieces_from_board(board,colour)
    opponent_pieces = get_pieces_from_board(board,not colour)
    for piece in my_pieces:
        ptype = get_piece_by_id(piece)[0]
        if ptype == 6: # Piece is a pawn.
            material += 10
        if ptype == 1: # Piece is a rook.
            material += 70
        if ptype == 3: # Piece is a bishop.
            material += 40
        if ptype == 2: # Piece is knight.
            material += 65
        if ptype == 5: # Piece is queen.
            material += 100
        if ptype == 4: # Piece is king.
            material += 0
    for piece in opponent_pieces:
        ptype = get_piece_by_id(piece)[0]
        if ptype == 6: # Piece is a pawn.
            material -= 10
        if ptype == 1: # Piece is a rook.
            material -= 70
        if ptype == 3: # Piece is a bishop.
            material -= 40
        if ptype == 2: # Piece is knight.
            material -= 65
        if ptype == 5: # Piece is queen.
            material -= 100
        if ptype == 4: # Piece is king.
            material -= 0
    return material
