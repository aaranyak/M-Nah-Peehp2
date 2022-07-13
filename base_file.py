import numpy as np
from utilfuncs import *
from seek_codes import *
from test_chess import *
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
# board_init_state = [
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,31,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,1,0,0,9],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0],
# ]
board = np.array(board_init_state)
display_seek = get_tiles(1,board)
test_board(board)
