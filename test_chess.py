import numpy as np
import utilfuncs as uf
import tkinter as tk
import seek_codes as sk
import chess_functions as cf
class TestingChess():
    """docstring for TestingChess."""

    def __init__(self, board):
        self.mousepos = (0,0)
        self.board = board
        self.selected = 0
        wpieces = ["", "♜", "♞", "♝", "♚", "♛", "♟"]
        bpieces = ["", "♖", "♘", "♗", "♔", "♕", "♙"]
        top = tk.Tk()
        self.display_seek = []
        simplified = uf.simplify_board(board)
        top.title("M-Nah-Peehp 2")
        top.geometry("400x400")
        C = tk.Canvas(top, height=400, width=400,bg="white")
        self.canvas = C
        C.pack()
        for x in range(8):
            for y in range(8):
                if (x + y) % 2: col = "#6f8f72"
                else: col = "#adbd8f"
                C.create_rectangle(x * 50,y * 50, x * 50 + 50,y * 50 + 50,fill=col, outline="")
        for y,row in enumerate(simplified):
            for x,piece in enumerate(row):
                if piece > 6:
                    C.create_text((x * 50) + 25, (y * 50) + 30, text=wpieces[piece - 6] , fill="#36663b",font="Times 40")
                else:
                    C.create_text((x * 50) + 25, (y * 50) + 30,text=wpieces[piece] , fill="#3b8c43", font="Times 40")
        self.canvas.bind('<Motion>', self.updateMousePos)
        self.canvas.bind('<Button-1>', self.select_piece)
        self.canvas.bind('<Button-2>', self.move_piece)
        self.canvas.bind("<Button-3>", self.move_piece)
        top.mainloop()
    def updateMousePos(self, mouse):
        wpieces = ["", "♜", "♞", "♝", "♚", "♛", "♟"]
        bpieces = ["", "♖", "♘", "♗", "♔", "♕", "♙"]
        self.mousepos = (mouse.y, mouse.x)
        simplified = uf.simplify_board(self.board)
        C = self.canvas
        for x in range(8):
            for y in range(8):
                if y == int(mouse.y / 50) and x == int(mouse.x / 50):
                    if (x + y) % 2: col = "#6f708f"
                    else: col = "#918fbd"
                elif (y,x) in self.display_seek:
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
    def select_piece(self, click):
        my, mx = self.mousepos
        self.selected = self.board[int(my / 50)][int(mx / 50)]
        self.display_seek = sk.get_tiles(self.selected, self.board)
        wpieces = ["", "♜", "♞", "♝", "♚", "♛", "♟"]
        bpieces = ["", "♖", "♘", "♗", "♔", "♕", "♙"]
        simplified = uf.simplify_board(self.board)
        C = self.canvas
        for x in range(8):
            for y in range(8):
                if y == int(my / 50) and x == int(mx / 50):
                    if (x + y) % 2: col = "#6f708f"
                    else: col = "#918fbd"
                elif (y,x) in self.display_seek:
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
    def move_piece(self, click):
        if cf.is_check(self.board, True):
            print("White king in check!")
        if cf.is_check(self.board, False):
            print("Black king in check!")
        if self.selected != 0:
            my, mx = self.mousepos
            px, py = int(mx / 50), int(my / 50)
            by, bx = uf.get_position_of_piece(self.selected, self.board)
            self.board[by][bx] = 0
            self.board[py][px] = self.selected
            self.display_seek = sk.get_tiles(self.selected, self.board)
            wpieces = ["", "♜", "♞", "♝", "♚", "♛", "♟"]
            bpieces = ["", "♖", "♘", "♗", "♔", "♕", "♙"]
            simplified = uf.simplify_board(self.board)
            C = self.canvas
            for x in range(8):
                for y in range(8):
                    if y == int(my / 50) and x == int(mx / 50):
                        if (x + y) % 2: col = "#6f708f"
                        else: col = "#918fbd"
                    elif (y,x) in self.display_seek:
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
def test_board(board):
    """Test seek codes"""
    chesstest = TestingChess(board)
