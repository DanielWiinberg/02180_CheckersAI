from checkers.constants import ROWS, COLS, WHITE, RED
from algorithms.helper_functions import *
from checkers import moves as mv
from copy import deepcopy
import numpy as np

''' MINIMAX TREE SEARCH '''            
def mini_max(board_state, max_player, turn_color, depth, depth_limit):
    nodes_explored = 0
    best_scores, nodes_explored = min_func(board_state, max_player, turn_color, depth, depth_limit, nodes_explored)
    max_score = max(best_scores.values())
    max_actions = [action for action, score in best_scores.items() if score == max_score]
    if not max_actions:
        return None, None, nodes_explored
    max_action = max_actions[0]
    print('! max_score: ', max_score)
    print('! max_action: ', max_action)
    return max_score, max_action, nodes_explored

def max_func(board_state, max_player, turn_color, depth, depth_limit, nodes_explored):
    best_scores = {}
    if depth == depth_limit or end_of_game(board_state, turn_color): # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
        return best_scores, nodes_explored
    
    pieces = get_pieces(board_state, turn_color)
    pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
    for piece in pieces:
        actions = mv.get_moves(board_state, piece)
        for action in actions:
            nodes_explored += 1
            new_board_state = deepcopy(board_state)
            new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
            b_score, nodes_explored = min_func(new_board_state, max_player, mv.change_turn(turn_color), depth + 1, depth_limit, nodes_explored) 
            if b_score:
                min_score = max(b_score.values())
                best_scores[(piece, action)] = min_score
    return best_scores, nodes_explored


        
def min_func(board_state, max_player, turn_color, depth, depth_limit, nodes_explored):
    best_scores = {}
    if depth == depth_limit or end_of_game(board_state, turn_color): # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
        return best_scores, nodes_explored
    
    pieces = get_pieces(board_state, turn_color)
    pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
    for piece in pieces:
        actions = mv.get_moves(board_state, piece)
        for action in actions:
            nodes_explored += 1
            new_board_state = deepcopy(board_state)
            new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
            b_score, nodes_explored = max_func(new_board_state, max_player, mv.change_turn(turn_color), depth + 1, depth_limit, nodes_explored) 
            if b_score:
                min_score = min(b_score.values())
                best_scores[(piece, action)] = min_score
                
    return best_scores, nodes_explored






''' MINIMAX GRAPH SEARCH '''
                
def mini_max_graph(board_state, board_state_explored, max_player, turn_color, depth, depth_limit):
    nodes_explored = 0
    best_scores, nodes_explored = min_func_graph(board_state, board_state_explored, max_player, turn_color, depth, depth_limit, nodes_explored)
    max_score = max(best_scores.values())
    max_actions = [action for action, score in best_scores.items() if score == max_score]
    if not max_actions:
        return None, None, nodes_explored
    max_action = max_actions[0]
    # print('! max_score: ', max_score)
    # print('! max_action: ', max_action)
    return max_score, max_action, nodes_explored

def max_func_graph(board_state, board_state_explored, max_player, turn_color, depth, depth_limit, nodes_explored):
    best_scores = {}
    if depth == depth_limit or end_of_game(board_state, turn_color):
        best_scores[None] = utility_function(board_state, max_player)
        return best_scores, nodes_explored
    
    pieces = get_pieces(board_state, turn_color)
    pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)]
    for piece in pieces:
        actions = mv.get_moves(board_state, piece)
        for action in actions:
            nodes_explored += 1
            new_board_state = deepcopy(board_state)
            new_board_state, _ = mv.move(new_board_state, piece, actions, action)
            
            if get_board_signature(new_board_state) in board_state_explored:
                #print("HERE MIN!!!!!!!!!!!!")
                #print(new_board_state)
                continue
            b_score, nodes_explored = min_func_graph(new_board_state, board_state_explored, max_player, mv.change_turn(turn_color), depth + 1, depth_limit, nodes_explored) 
            if b_score:
                min_score = max(b_score.values())
                best_scores[(piece, action)] = min_score
                
    return best_scores, nodes_explored


        
def min_func_graph(board_state, board_state_explored, max_player, turn_color, depth, depth_limit, nodes_explored):
    best_scores = {}
    if depth == depth_limit or end_of_game(board_state, turn_color):
        best_scores[None] = utility_function(board_state, max_player)
        return best_scores, nodes_explored
    
    pieces = get_pieces(board_state, turn_color)
    pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)]
    for piece in pieces:
        actions = mv.get_moves(board_state, piece)
        for action in actions:
            nodes_explored += 1
            new_board_state = deepcopy(board_state)
            new_board_state, _ = mv.move(new_board_state, piece, actions, action)
            
            if get_board_signature(new_board_state) in board_state_explored:
                #print("HERE MIN!!!!!!!!!!!!")
                #print(new_board_state)
                continue
            b_score, nodes_explored = max_func_graph(new_board_state, board_state_explored, max_player, mv.change_turn(turn_color), depth + 1, depth_limit, nodes_explored) 
            if b_score:
                min_score = min(b_score.values())
                best_scores[(piece, action)] = min_score
                
    return best_scores, nodes_explored



    



















'''OLD MINIMAX FUNCTION'''
def mini_max_old(board_state, max_player, turn_color, depth, depth_limit):
    best_scores = {}
    
    if depth == depth_limit or end_of_game(board_state, turn_color): # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
        
    else:
        pieces = get_pieces(board_state, turn_color)
        
        pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
        for piece in pieces:
            actions = mv.get_moves(board_state, piece)
            for action in actions:
                # print("HERE!!!!")
                # print(board_state)
                new_board_state = deepcopy(board_state)
                new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
                # print(new_board_state)
                score, _ = mini_max(new_board_state, max_player, mv.change_turn(turn_color), depth + 1, depth_limit) 
                best_scores[(piece, action)] = score

    if (depth % 2) == 0:
        max_score = max(best_scores.values())
        max_actions = [action for action, score in best_scores.items() if score == max_score]
        if not max_actions:
            return None, None
        max_action = max_actions[0]
        
        # print('! max_score: ', max_score)
        # print('! max_action: ', max_action)
        return max_score, max_action

    else:
        min_score = min(best_scores.values())
        min_actions = [action for action, score in best_scores.items() if score == min_score]
        if not min_actions:
            return None, None
        min_action = min_actions[0]
        # print('! min_score: ', min_score)
        # print('! min_action: ', min_action)
        return min_score, min_action