import numpy as np
import tkinter as tk
import time
def draw_board(board):
    """Displays the state of the board on the terminal."""
    wpieces = ["__", "♜", "♞", "♝", "♚", "♛", "♟"]
    bpieces = ["__", "♖", "♘", "♗", "♔", "♕", "♙"]
    rendered = []
    for row in board:
        pr = []
        for tile in row:
            ptype, pteam = get_piece_by_id(tile)
            if pteam:
                pr.append(wpieces[ptype])
            else:
                pr.append(bpieces[ptype])
        rendered.append(pr)
    image = ""
    image += " __ __ __ __ __ __ __ __\n"
    for row in rendered:
        image += "|"
        for piece in row:
            image += piece
            if piece != "__": image += " "
            image += "|"
        image += "\n"
    return image
def get_piece_by_id(id):
    """Returns piece type and colour"""
    type = 0
    if id in [1,8,24,17]:
        type = 1
    if id in [2,7,23,18]:
        type = 2
    if id in [3,6,22,19]:
        type = 3
    if id in [4,20]:
        type = 4
    if id in [5,21]:
        type = 5
    if id in range(9,17) or id in range(25,33):
        type = 6
    team = id < 17
    return (type, team)
def teamify_board(board, inv = False):
    """Returns a simplified version of the board
       Which only has the colour of the pieces."""
    result = []
    for row in board:
        tr = []
        for tile in row:
            pc = get_piece_by_id(tile)
            if pc[0] != 0:
                if not inv:
                    if not pc[1]: tr.append(1)
                    else: tr.append(0)
                else:
                    if not pc[1]: tr.append(0)
                    else: tr.append(1)
            else:
                tr.append(3)
        result.append(tr)
    return np.array(result)
def simplify_board(board, inv=False):
    """Returns a simplified version of the board
       which only shows piece type and colour"""
    result = []
    for row in board:
        sr = []
        for tile in row:
            if tile == 0:
                sr.append(0)
            else:
                pd = get_piece_by_id(tile)
                num = pd[0]
                if pd[1] == inv:
                    num += 6
                sr.append(num)
        result.append(sr)
    return np.array(result)
def turn_board(board):
    """Shows the board from the perspective of another player"""
    reslist = []
    for row in board:
        fr = []
        for tile in row:
            if tile == 0: fr.append(0)
            else:
                if tile > 16:
                    fr.append(tile - 16)
                else:
                    fr.append(tile + 16)
        reslist.append(fr)
    resray = np.array(reslist)
    result = np.rot90(resray,2)
    return result
def get_position_of_piece(piece, board):
    """Returns the position of the piece on the board"""
    posarr = np.where(board == piece)
    if len(posarr[0]) == 0 or len(posarr[1]) == 0:
        return(-1,-1)
    else:
        y = posarr[0][0]
        x = posarr[1][0]
        return y,x
def display_pattern(tiles):
    """Marks specific tiles on an empty board"""
    display = np.zeros((8,8))
    for y,x in tiles:
        display[y][x] = 1
    return display
def render_board(*args):
    """Displays the state of the board on a separate window"""
    wpieces = ["", "♜", "♞", "♝", "♚", "♛", "♟"]
    bpieces = ["", "♖", "♘", "♗", "♔", "♕", "♙"]
    rendered = []
    board = args[0]
    if len(args) == 2:
        display_pattern = args[1]
    else:
        display_pattern = []
    top = tk.Tk()
    simplified = simplify_board(board)
    top.title("M-Nah-Peehp 2")
    top.geometry("400x400")
    C = tk.Canvas(top, height=400, width=400,bg="white")
    C.pack()
    for x in range(8):
        for y in range(8):
            if (y,x) in display_pattern:
                if (x + y) % 2: col = "#8f6f6f"
                else: col = "#bd8f8f"
            else:
                if (x + y) % 2: col = "#6f8f72"
                else: col = "#adbd8f"
            C.create_rectangle(x * 50,y * 50, x * 50 + 50,y * 50 + 50,fill=col, outline="")
    for y,row in enumerate(simplified):
        for x,piece in enumerate(row):
            if piece > 6:
                C.create_text((x * 50) + 25, (y * 50) + 30, text=wpieces[piece - 6] , fill="#36663b",font="Times 40")
            else:
                C.create_text((x * 50) + 25, (y * 50) + 30,text=wpieces[piece] , fill="#3b8c43", font="Times 40")
    top.mainloop()

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
                filtered_tiles.append((y - 1, x - 1)) # If yes, add tile to list

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
    return tiles