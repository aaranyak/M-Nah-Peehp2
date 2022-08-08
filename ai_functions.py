import numpy as np
from utilfuncs import *
from chess_functions import *
from seek_codes import *
import multiprocessing


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

def minmax_pruning_transposition(board, depth, colour, alpha, beta, multithreading):
    """Implimentation of minmax search with alpha-beta pruning and keeping track of transpositions"""
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
