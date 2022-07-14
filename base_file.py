import numpy as np
from utilfuncs import *
from seek_codes import *
from test_chess import *
from game_types import *
from chess_functions import *
board_init_state = [
    [1,2,3,4,5,6,7,8],
    [30,0,11,12,13,14,15,16],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,10,0,0,0,0,0,0],
    [32,31,9,29,28,27,26,25],
    [24,23,22,20,21,19,18,17]
]
game = RandomChessGame()
game.play()
