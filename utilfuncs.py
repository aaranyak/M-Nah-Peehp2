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
def name_piece(piece):
    ptype = get_piece_by_id(piece)
    if ptype[0] == 1:
        return "Rook"
    if ptype[0] == 2:
        return "Knight"
    if ptype[0] == 3:
        return "Bishop"
    if ptype[0] == 4:
        return "King"
    if ptype[0] == 5:
        return "Queen"
    if ptype[0] == 6:
        return "Pawn"
    else:
        return "Empty"

def get_pieces_from_board(*args):
    """Returns all the pieces from a board"""
    board = args[0]
    if len(args) == 2:
        team = args[1]
    else:
        team = None
    line_board = board.reshape(64)
    if team is None:
        pieces = filter(lambda num:num, line_board)
    else:
        if team:
            pieces = filter(lambda num:num and num < 17, line_board)
        else:
            pieces = filter(lambda num:num and num > 16, line_board)
    return list(pieces)

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
