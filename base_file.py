import numpy as np
from utilfuncs import *
from seek_codes import *
from test_chess import *
from game_types import *
from chess_functions import *
from ai_functions import *
from ai_game_alg import AiVsHumanSimple
board_init_state = [
    [1,2,3,4,5,6,7,8],
    [9,10,11,12,13,14,15,16],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [32,31,30,29,28,27,26,25],
    [24,23,22,20,21,19,18,17]
]
board = np.array(board_init_state)
game = AiVsHumanSimple(False)
game.play()
