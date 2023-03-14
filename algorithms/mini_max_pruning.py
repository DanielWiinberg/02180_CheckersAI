from checkers.constants import ROWS, COLS, WHITE, RED
from checkers import moves as mv
from copy import deepcopy
import numpy as np
from algorithms.helper_functions import *

def mini_max_alpha_beta(board_state, max_player, turn_color, depth, depth_limit):
    nodes_explored = 0
    best_scores, nodes_explored = min_alpha_beta_func(board_state, max_player, turn_color, depth, depth_limit, -np.inf, np.inf, nodes_explored)
    max_score = max(best_scores.values())
    max_actions = [action for action, score in best_scores.items() if score == max_score]
    if not max_actions:
        return None, None, nodes_explored
    max_action = max_actions[0]
    # print('! max_score: ', max_score)
    # print('! max_action: ', max_action)
    return max_score, max_action, nodes_explored

def max_alpha_beta_func(board_state, max_player, turn_color, depth, depth_limit, alpha, beta, nodes_explored):
    best_scores = {}
    if depth == depth_limit or end_of_game(board_state, turn_color): # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
    else:
        pieces = get_pieces(board_state, turn_color)
        pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
        for piece in pieces:
            actions = mv.get_moves(board_state, piece)
            for action in actions:
                nodes_explored += 1
                # print("HERE MAX!!!!")
                # print(board_state)
                new_board_state = deepcopy(board_state)
                new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
                #print(new_board_state)
                b_score, nodes_explored = min_alpha_beta_func(new_board_state, max_player, mv.change_turn(turn_color), depth + 1, depth_limit, alpha, beta, nodes_explored) 
                #if b_score:
                max_score = max(b_score.values())  
                best_scores[(piece, action)] = max_score
                if max_score >= beta:
                    return best_scores, nodes_explored
                alpha = max(alpha, max_score)
                    
    return best_scores, nodes_explored

        
def min_alpha_beta_func(board_state, max_player, turn_color, depth, depth_limit, alpha, beta, nodes_explored):
    best_scores = {}
    if depth == depth_limit or end_of_game(board_state, turn_color): # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
    else:  
        pieces = get_pieces(board_state, turn_color)
        pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
        for piece in pieces:
            actions = mv.get_moves(board_state, piece)
            for action in actions:
                nodes_explored += 1
                # print("HERE MIN!!!!")
                # print(board_state)
                new_board_state = deepcopy(board_state)
                new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
                #print(new_board_state)
                b_score, nodes_explored = max_alpha_beta_func(new_board_state, max_player, mv.change_turn(turn_color), depth + 1, depth_limit, alpha, beta, nodes_explored) 
                #if b_score:
                min_score = min(b_score.values())
                best_scores[(piece, action)] = min_score
                if min_score <= alpha:
                    return best_scores, nodes_explored
                beta = min(beta, min_score)
    return best_scores, nodes_explored