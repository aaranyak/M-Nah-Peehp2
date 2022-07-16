import numpy as np
from utilfuncs import *
from seek_codes import *
from chess_functions import *
from chess_errors import *
from chess_game import *
import time
import random
import tkinter as tk
from tkinter import messagebox
from ai_functions import *
class AiVsHumanSimple(ChessGame):
    """Just a test where an Ai plays random moves against a human."""
    def __init__(self, color):
        super(AiVsHumanSimple, self).__init__()
        self.display = tk.Tk()
        self.color = color
        self.selected = 0
        self.mouse_position = (0,0)
        self.show_tiles = []
        self.display.title("Ai vs Human Showdown")
        self.display.geometry("400x400")
        self.canvas = tk.Canvas(self.display, height=400, width=400,bg="white")
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.select_piece)
        self.canvas.bind('<Motion>', self.move_mouse)
        self.canvas.bind('<Button-2>', self.human_move)
        self.canvas.bind("<Button-3>", self.human_move)
    def move_mouse(self, m_pos):
        self.mouse_position = (m_pos.y, m_pos.x)
    def select_piece(self, event):
        if self.turn == self.color:
            my, mx = self.mouse_position
            ty, tx = int(my / 50), int(mx / 50)
            ptype = get_piece_by_id(self.board[ty][tx])
            if ptype[0] == 0:
                self.selected = 0
            else:
                if ptype[1] == self.color:
                    self.selected = self.board[ty][tx]
                    self.show_tiles = get_tiles(self.board[ty][tx], self.board)
            self.update_canvas()

    def play(self):
        self.update_canvas()
        self.playing = True
        while self.playing:
            if self.turn != self.color:
                time.sleep(0.2)
                if get_pieces_from_board(self.board) in ([4,20], [20,4]): # Checks if it is a draw
                    print("Ended in a draw!")
                    break
                white_state = is_checkmate(self.board, True)
                black_state = is_checkmate(self.board, False)
                if white_state == -1:
                    print("Black Checkmates White!")
                    break
                elif black_state == -1:
                    print("White Checkmates Black!")
                    break
                elif black_state == 0 or white_state == 0:
                    print("Stalemate!")
                    break
                self.play_move()
                if get_pieces_from_board(self.board) in ([4,20], [20,4]):
                    print("Ended in a draw!")
                    break
                white_state = is_checkmate(self.board, True)
                black_state = is_checkmate(self.board, False)
                if white_state == -1:
                    print("Black Checkmates White!")
                    break
                elif black_state == -1:
                    print("White Checkmates Black!")
                    break
                elif black_state == 0 or white_state == 0:
                    print("Stalemate!")
                    break
            self.update_canvas()
        self.update_canvas()
        self.display.mainloop()
    def human_move(self, click):
        if self.selected != 0 and self.turn == self.color:
            my, mx = self.mouse_position
            ty, tx = int(my / 50), int(mx / 50)
            try:
                self.make_move(self.selected, (ty,tx))
            except ChessException as error:
                messagebox.showwarning(title="Illegal Move", message=error)
            else:
                self.selected = 0
                self.show_tiles = []
                self.update_canvas()
    def play_move(self):
        evaluation = minmax_pruning(self.board,3, not self.color, float("-inf"), float("inf"), True)
        self.make_move(evaluation[1], evaluation[2])
    def update_canvas(self):
        self.canvas.delete("all")
        piece_icons = ["", "♜", "♞", "♝", "♚", "♛", "♟"]
        # Create the board
        for y in range(8): # All the squares on x axis.
            for x in range(8): # All the squares on y axis.
                if (y,x) in self.show_tiles:
                    if (x + y) % 2: col = "#8f6f6f"
                    else: col = "#bd8f8f"
                else:
                    if (x + y) % 2: col = "#6f8f72" # If square is black, set colour
                    else: col = "#adbd8f" # If square is white, set colour
                self.canvas.create_rectangle(x * 50,y * 50, x * 50 + 50,y * 50 + 50,fill=col, outline="") # Add the chessboard square.
        simplified = simplify_board(self.board)
        # Draw the pieces.
        for y,row in enumerate(simplified):
            for x,piece in enumerate(row):
                if piece > 6:
                    self.canvas.create_text((x * 50) + 25, (y * 50) + 30, text=piece_icons[piece - 6] , fill="#36663b",font="Times 40") # Draw a black piece.
                else:
                    self.canvas.create_text((x * 50) + 25, (y * 50) + 30,text=piece_icons[piece] , fill="#3b8c43", font="Times 40") # Draw a white piece.
        self.display.update()
