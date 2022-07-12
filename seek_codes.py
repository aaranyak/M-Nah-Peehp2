import numpy as np
from utilfuncs import *

def get_tiles(piece, board):
    """Returns the list of pseudo-legal moves
       that are possble for a certian piece"""

    ptype = get_piece_by_id(piece)
    if ptype[0] == 1:
        return get_rook_tiles(piece, board)
    if ptype[0] == 2:
        return get_knight_tiles(piece, board)
    if ptype[0] == 3:
        return get_bishop_tiles(piece, board)
    if ptype[0] == 4:
        return get_king_tiles(piece, board)
    if ptype[0] == 5:
        return get_queen_tiles(piece, board)
    if ptype[0] == 6:
        return get_pawn_tiles(piece, board)
    else:
        return []

def get_pawn_tiles(piece, board):
    """Return moves for pawn"""
    ptype = get_piece_by_id(piece)
    simple_board = teamify_board(board, not ptype[1])
    y,x = get_position_of_piece(piece, board)
    filtered_tiles = []
    # If piece is a white pawn:
    if ptype[1] and y + 1 in range(0,8): # Check if the piece is at the opposite edge of the board.
        if simple_board[y + 1][x] == 3: # Check if tile in front of pawn is blocked by piece.
            filtered_tiles.append((y + 1, x)) # Add the front tile to the list.
            if y == 1: # If pawn is on second file, ability to move two squares ahead.
                if simple_board[y + 2][x] == 3: # Check if second square in front of pawn is blocked
                    filtered_tiles.append((y + 2, x))
        if x + 1 in range(0,8): # If x in not on edge
            if simple_board[y + 1][x + 1] == 1: # Check if piece is available for capture
                filtered_tiles.append((y + 1, x + 1)) # If yes, add tile to list
        if x - 1 in range(0,8): # If x not on other edge
            if simple_board[y + 1][x - 1] == 1: # Check if piece is available for capture
                filtered_tiles.append((y + 1, x - 1)) # If yes, add tile to list

    # If piece is a black pawn:
    elif y - 1 in range(0,8): # Check if the piece is at the opposite edge of the board.
        if simple_board[y - 1][x] == 3: # Check if tile in front of pawn is blocked by piece.
            filtered_tiles.append((y - 1, x)) # Add the front tile to the list.
            if y == 6: # If pawn is on sixth file, ability to move two squares ahead.
                if simple_board[y - 2][x] == 3:
                    filtered_tiles.append((y - 2, x)) # Check if second square in front of pawn is blocked
        if x + 1 in range(0,8): # If x in not on edge
            if simple_board[y - 1][x + 1] == 1: # Check if piece is available for capture
                filtered_tiles.append((y - 1, x + 1)) # If yes, add tile to list
        if x - 1 in range(0,8): # If x not on other edge
            if simple_board[y - 1][x - 1] == 1: # Check if piece is available for capture
                filtered_tiles.append((y - 1, x - 1)) # If yes, add tile to list

    unfiltered_tiles = []

    return filtered_tiles

def get_knight_tiles(piece, board):
    """Returns moves for knight"""
    ptype = get_piece_by_id(piece)
    simple_board = teamify_board(board, not ptype[1])
    y,x = get_position_of_piece(piece, board)
    unfiltered_pattern = [
        (y + 2, x + 1),
        (y + 1, x + 2),
        (y - 2, x - 1),
        (y - 1, x - 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 2, x + 1),
        (y + 2, x - 1),
    ] # The pattern of squares that a knight jumps to.
    unfiltered_tiles = []
    for ty, tx in unfiltered_pattern: # Filter out the tiles that do not exist.
        if ty in range(0,8) and tx in range(0,8):
            unfiltered_tiles.append((ty,tx))
    filtered_tiles = []
    for ty, tx in unfiltered_tiles: # Filter out the tiles that are blocked by our own pieces.
        if simple_board[ty][tx] != 0:
            filtered_tiles.append((ty,tx))
    return filtered_tiles

def get_king_tiles(piece, board):
    """Returns moves for king"""
    ptype = get_piece_by_id(piece)
    simple_board = teamify_board(board, not ptype[1])
    y,x = get_position_of_piece(piece, board)
    unfiltered_pattern = [
        (y, x + 1),
        (y + 1, x),
        (y, x - 1),
        (y - 1, x),
        (y + 1, x + 1),
        (y - 1, x - 1),
        (y - 1, x + 1),
        (y + 1, x - 1)
    ] # The pattern of squares that a king jumps to.
    unfiltered_tiles = []
    for ty, tx in unfiltered_pattern: # Filter out the tiles that do not exist.
        if ty in range(0,8) and tx in range(0,8):
            unfiltered_tiles.append((ty,tx))
    filtered_tiles = []
    for ty, tx in unfiltered_tiles: # Filter out the tiles that are blocked by our own pieces.
        if simple_board[ty][tx] != 0:
            filtered_tiles.append((ty,tx))
    return filtered_tiles

def get_rook_tiles(piece, board):
    """Returns moves for rook"""
    ptype = get_piece_by_id(piece)
    simple_board = teamify_board(board, not ptype[1])
    y,x = get_position_of_piece(piece, board)
    tiles = []

    for ty in reversed(range(0,y)): # Loop through every square above the rook.
        if simple_board[ty][x] == 0: # If square containes friendly piece, break.
                break
        elif simple_board[ty][x] == 1: # If square contains friendly piece, capture then break.
            tiles.append((ty,x))
            break
        else: # If square is empty, add square to list.
            tiles.append((ty,x))

    for ty in range(y + 1, 8): # Loop through every square below the rook.
        if simple_board[ty][x] == 0: # If square containes friendly piece, break.
                break
        elif simple_board[ty][x] == 1: # If square contains friendly piece, capture then break.
            tiles.append((ty,x))
            break
        else: # If square is empty, add square to list.
            tiles.append((ty,x))

    for tx in reversed(range(0,x)): # Loop through every square to the left of the rook.
        if simple_board[y][tx] == 0: # If square containes friendly piece, break.
                break
        elif simple_board[y][tx] == 1: # If square contains friendly piece, capture then break.
            tiles.append((y,tx))
            break
        else: # If square is empty, add square to list.
            tiles.append((y,tx))

    for tx in range(x + 1,8): # Loop through every square to the right of the rook.
        if simple_board[y][tx] == 0: # If square containes friendly piece, break.
                break
        elif simple_board[y][tx] == 1: # If square contains friendly piece, capture then break.
            tiles.append((y,tx))
            break
        else: # If square is empty, add square to list.
            tiles.append((y,tx))
    return tiles

def get_bishop_tiles(piece, board):
    """Returns moves for bishop"""
    ptype = get_piece_by_id(piece)
    simple_board = teamify_board(board, not ptype[1])
    y,x = get_position_of_piece(piece, board)
    tiles = []
    for d in range(1,min(8 - y,8 - x)): # Loop through every square to the bottom-right of the bishop.
        if simple_board[y + d][x + d] == 0: # If square contains friendly piece, break.
            break
        elif simple_board[y + d][x + d] == 1: # If square contains enemy piece, capture then break/
            tiles.append((y + d,x + d))
            break
        else: # If square is empty, add square to list.
            tiles.append((y + d,x + d))

    for d in range(1,min(y + 1,x + 1)): # Loop through every square to the top-left of the bishop.
        if simple_board[y - d][x - d] == 0: # If square contains friendly piece, break.
            break
        elif simple_board[y - d][x - d] == 1: # If square contains enemy piece, capture then break/
            tiles.append((y - d,x - d))
            break
        else: # If square is empty, add square to list.
            tiles.append((y - d,x - d))

    for d in range(1,min(y + 1,8 - x)): # Loop through every square to the top-right of the bishop.
        if simple_board[y - d][x + d] == 0: # If square contains friendly piece, break.
            break
        elif simple_board[y - d][x + d] == 1: # If square contains enemy piece, capture then break/
            tiles.append((y - d,x + d))
            break
        else: # If square is empty, add square to list.
            tiles.append((y - d,x + d))

    for d in range(1,min(8 - y,x + 1)): # Loop through every square to the top-left of the bishop.
        if simple_board[y + d][x - d] == 0: # If square contains friendly piece, break.
            break
        elif simple_board[y + d][x - d] == 1: # If square contains enemy piece, capture then break/
            tiles.append((y + d,x - d))
            break
        else: # If square is empty, add square to list.
            tiles.append((y + d,x - d))
    return tiles

def get_queen_tiles(piece, board):
    """Get the available moves for a queen"""
    tiles = []
    rook_moves = get_rook_tiles(piece, board) # Moves the queen like a rook.
    bishop_moves = get_bishop_tiles(piece, board) # Moves the queen like a bishop.
    tiles.extend(rook_moves) # Combine the rook moves into the queen moves.
    tiles.extend(bishop_moves) # Combine the bishop moves into the queen moves.

    return tiles
