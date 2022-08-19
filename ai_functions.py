import numpy as np
from utilfuncs import *
from chess_functions import *
from seek_codes import *
import multiprocessing
import time
def minmax(board, depth, colour):
    """Basic implimentation of minmax search"""
    pieces = get_pieces_from_board(board, colour) # Get all pieces.
    if depth == 0: # If it has reached the end of search,
        return (count_material(board, colour), 0,0) # Return a basic board evauluation by piece material.
    else: # Otherwise, continue search.
        results = []
        moves = []
        for piece in pieces: # Loop through all the pieces
            possible_moves = get_tiles(piece, board) # Get available moves for piece.
            for move in possible_moves: # Loop through all possible moves.
                new_board = move_piece_on_board(piece, move, board) # Play the move.
                if not is_check(new_board, colour): # If move is legal,
                    evaluate = minmax(new_board, depth - 1, not colour) # Search the next part of the tree.

                    results.append(-evaluate[0]) # Add the result to the results.
                    moves.append((piece, move)) # Add the move to the moves.
        if len(results) == 0: # If there are no legal moves,
            if is_check(board, colour): # If in check,
                return (float("-inf"), 0, 0) # Checkmate!
            else:
                return (0, 0, 0) # Stalemate!
        else: # Otherwise, return the greatest result of the search.
            greatest_index = 0
            greatest_evaluation = float("-inf")
            for index, evaluation in enumerate(results): # Loop through the result.
                if evaluation > greatest_evaluation: # If result greater than current greatest,
                    greatest_evaluation = evaluation # Assign that to the greatest.
                    greatest_index = index # Update the index.
            return (greatest_evaluation, moves[greatest_index][0], moves[greatest_index][1]) # Return the result of the search.

def minmax_pruning(board, depth, colour, alpha, beta, multithreading):
    """Implimentation of minmax search with alpha-beta pruning"""
    pieces = get_pieces_from_board(board, colour) # Get all pieces.
    if depth == 0: # If it has reached the end of search,
        return (count_material(board, colour), 0,0) # Return a basic board evauluation by piece material.
    else: # Otherwise, continue search.
        results = []
        moves = []
        for piece in pieces: # Loop through all the pieces
            possible_moves = get_tiles(piece, board) # Get available moves for piece.
            for move in possible_moves: # Loop through all possible moves.
                new_board = move_piece_on_board(piece, move, board) # Play the move.
                if not is_check(new_board, colour): # If move is legal,
                    evaluate = minmax_pruning(new_board, depth - 1, not colour, -beta, -alpha, True) # Search the next part of the tree.
                    results.append(-evaluate[0]) # Add the result to the results.
                    moves.append((piece, move)) # Add the move to the moves.
                    if -evaluate[0] >= beta: # Move was better than the previous best,
                        break # Search discontinued.
                    else:
                        alpha = max(alpha, -evaluate[0])
            else: # If loop wasn't broken,
                continue # Skip to next iteration befor loop breaks.
            break # If inner loop was broken, break
        if len(results) == 0: # If there are no legal moves,
            if is_check(board, colour): # If in check,
                return (float("-inf"), 0, 0) # Checkmate!
            else:
                return (0, 0, 0) # Stalemate!
        else: # Otherwise, return the greatest result of the search.
            greatest_index = 0
            greatest_evaluation = float("-inf")
            for index, evaluation in enumerate(results): # Loop through the result.
                if evaluation > greatest_evaluation: # If result greater than current greatest,
                    greatest_evaluation = evaluation # Assign that to the greatest.
                    greatest_index = index # Update the index.
            return (greatest_evaluation, moves[greatest_index][0], moves[greatest_index][1]) # Return the result of the search.

def minmax_pruning_timed(board, depth, colour, alpha, beta, start_time, close_time, ordering, t_table):
    """Implimentation of minmax search with alpha-beta pruning"""
    available_moves = get_all_pseudo_legal_moves(board, colour)
    if depth == 0: # If it has reached the end of search,
        if time.time() > start_time + close_time: # If time has ecxeeded limit
            return "broken" # Break out of function
        return (count_material(board, colour), 0,0,t_table) # Return a basic board evauluation by piece material.

    else: # Otherwise, continue search.
        ordering_list = [] # List for sorting moves
        # Create ordering list
        for move in available_moves:
            played = move_piece_on_board(move[0], move[1], board)
            if str(played) in ordering:
                if colour:
                    ordering_list.append((move, ordering[str(played)]))
                else:
                    ordering_list.append((move, -ordering[str(played)]))

            else:
                ordering_list.append((move, 0))
        ordering_list.sort(key=lambda e: e, reverse=True)
        ordered_moves = [move[0] for move in ordering_list]
        results = []
        moves = []
        for available in ordered_moves: # Go through
            piece = available[0]
            move = available[1]
            new_board = move_piece_on_board(piece, move, board) # Play the move.
            if not is_check(new_board, colour): # If move is legal,
                evaluate = minmax_pruning_timed(new_board, depth - 1, not colour, -beta, -alpha, start_time, close_time, ordering, t_table) # Search the next part of the tree.
                if evaluate == "broken": # If previous function was broken
                    return "broken" # Break out of function
                t_table = evaluate[3] # Update evaluation table
                results.append(-evaluate[0]) # Add the result to the results.
                moves.append((piece, move)) # Add the move to the moves.
                if -evaluate[0] >= beta: # Move was better than the previous best,
                    break # Search discontinued.
                else:
                    alpha = max(alpha, -evaluate[0])
        if len(results) == 0: # If there are no legal moves,
            if is_check(board, colour): # If in check,
                return (float("-inf"), 0, 0) # Checkmate!
            else:
                return (0, 0, 0) # Stalemate!
        else: # Otherwise, return the greatest result of the search.
            greatest_index = 0
            greatest_evaluation = float("-inf")
            for index, evaluation in enumerate(results): # Loop through the result.
                if evaluation > greatest_evaluation: # If result greater than current greatest,
                    greatest_evaluation = evaluation # Assign that to the greatest.
                    greatest_index = index # Update the index.
            if colour:
                t_table[str(board)] = greatest_evaluation # Add to evluation table
            else:
                t_table[str(board)] = -greatest_evaluation # Add to evaluation table
            return (greatest_evaluation, moves[greatest_index][0], moves[greatest_index][1], t_table) # Return the result of the search.

def iterative_deepening(board, max_time):
    """Minmax with iterative deepening"""
    ordering_table = {} # The table for move ordering
    last_eval = () # Last Evaluation
    timer = max_time # Timer
    depth = 1 # Search Depth
    while True: # Keep searching until time runs out
        curtime = time.time() # The Current Time
        eval1 = minmax_pruning_timed(board,depth, True, float("-inf"), float("inf"), time.time(), timer, ordering_table, {}) # Search, but only to a time limit.
        if eval1 != "broken": # If search was not discontinued.
            timer -= (time.time() - curtime) # Update timer.
            last_eval = (eval1[0], eval1[1], eval1[2]) # Update evaluation.
            ordering_table = eval1[3] # Update ordering table.
            depth += 1 # Increment depth
        else: # If search was discontinued
            break # Return values
    return (depth - 1,last_eval)
