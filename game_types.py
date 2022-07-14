import numpy as np
from utilfuncs import *
from seek_codes import *
from chess_functions import *
from chess_errors import *
from chess_game import *
import random
import tkinter as tk
class RandomChessGame(ChessGame):
    """Just a test where an Ai plays random moves against itself."""

    def __init__(self, time=0.2):
        super(ChessGame, self).__init__()
        self.display = tk.Tk()
        self.display.title("Random Game")
        self.display.geometry("400x400")
        self.canvas = tk.Canvas(top, height=400, width=400,bg="white")
    def play(self):
        playing = True
        self.display.mainloop()
        while playing:
            self.on_move()
            white_state = is_checkmate(True)
            black_state = is_checkmate(False)
            if white_state == -1:
                print("Black Checkmates White!")
                break
            elif black_state == -1:
                print("White Checkmates Black!")
                break
            elif black_state == 0 or white_state == 0:
                print("Stalemate!")
                break

    def on_move(self):
        moves = get_all_moves(self.board, self.turn)
        if moves != []:
            move_to_play = random.choice(moves)
            self.make_move(move)
    def update_canvas(self):
        self.canvas.delete("all")
        piece_icons = ["", "♜", "♞", "♝", "♚", "♛", "♟"]
        # Create the board
        for y in range(8): # All the squares on x axis.
            for x in range(8): # All the squares on y axis.
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
