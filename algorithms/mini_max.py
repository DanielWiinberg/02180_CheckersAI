from checkers.constants import ROWS, COLS, WHITE, RED
from checkers import moves as mv
from copy import deepcopy
import numpy as np


'''SIMPLE MINIMAX GRAPH SEARCH CODE'''
                
def mini_max_graph(board_state, board_state_explored, max_player, turn_color, depth, depth_limit):
    board_state_explored = [(turn_color,board_state)]
    best_scores,board_state_explored = min_func_graph(board_state, board_state_explored, max_player, turn_color, depth, depth_limit)
    max_score = max(best_scores.values())
    max_actions = [action for action, score in best_scores.items() if score == max_score]
    if not max_actions:
        return None, None, board_state_explored
    max_action = max_actions[0]
    # print('! max_score: ', max_score)
    # print('! max_action: ', max_action)
    return max_score, max_action, board_state_explored

def max_func_graph(board_state, board_state_explored, max_player, turn_color, depth, depth_limit):
    best_scores = {}
    if depth == depth_limit or end_of_game(board_state, turn_color): # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
        return best_scores,board_state_explored
    
    pieces = get_pieces(board_state, turn_color)
    pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
    for piece in pieces:
        actions = mv.get_moves(board_state, piece)
        for action in actions:
            # print("HERE MAX!!!!")
            # print(board_state)
            new_board_state = deepcopy(board_state)
            new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
            
            if (turn_color,new_board_state) in board_state_explored:
                continue
            board_state_explored.append((turn_color,new_board_state))
            #print(new_board_state)
            b_score,board_state_explored = min_func_graph(new_board_state, board_state_explored, max_player, mv.change_turn(turn_color), depth + 1, depth_limit) 
            if b_score:
                min_score = max(b_score.values())
                best_scores[(piece, action)] = min_score
                
    return best_scores,board_state_explored


        
def min_func_graph(board_state, board_state_explored, max_player, turn_color, depth, depth_limit):
    best_scores = {}
    if depth == depth_limit or end_of_game(board_state, turn_color): # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
        return best_scores,board_state_explored
    
    pieces = get_pieces(board_state, turn_color)
    pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
    for piece in pieces:
        actions = mv.get_moves(board_state, piece)
        for action in actions:
            # print("HERE MIN!!!!")
            # print(board_state)
            new_board_state = deepcopy(board_state)
            new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
            
            if (turn_color,new_board_state) in board_state_explored:
                continue
            board_state_explored.append((turn_color,new_board_state))
            #print(new_board_state)
            b_score,board_state_explored = max_func_graph(new_board_state, board_state_explored, max_player, mv.change_turn(turn_color), depth + 1, depth_limit) 
            if b_score:
                min_score = min(b_score.values())
                best_scores[(piece, action)] = min_score
                
    return best_scores,board_state_explored



'''ALPHA-BETA MINIMAX CODE'''

def mini_max_alpha_beta(board_state, max_player, turn_color, depth, depth_limit):
    best_scores = min_alpha_beta_func(board_state, max_player, turn_color, depth, depth_limit, -np.inf, np.inf)
    max_score = max(best_scores.values())
    max_actions = [action for action, score in best_scores.items() if score == max_score]
    if not max_actions:
        return None, None
    max_action = max_actions[0]
    # print('! max_score: ', max_score)
    # print('! max_action: ', max_action)
    return max_score, max_action

def max_alpha_beta_func(board_state, max_player, turn_color, depth, depth_limit, alpha, beta):
    best_scores = {}
    if depth == depth_limit: # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
    else:
        pieces = get_pieces(board_state, turn_color)
        pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
        for piece in pieces:
            actions = mv.get_moves(board_state, piece)
            for action in actions:
                # print("HERE MAX!!!!")
                # print(board_state)
                new_board_state = deepcopy(board_state)
                new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
                #print(new_board_state)
                b_score = min_alpha_beta_func(new_board_state, max_player, mv.change_turn(turn_color), depth + 1, depth_limit, alpha, beta) 
                #if b_score:
                max_score = max(b_score.values())  
                best_scores[(piece, action)] = max_score
                if max_score >= beta:
                    return best_scores
                alpha = max(alpha, max_score)
                    
    return best_scores

        
def min_alpha_beta_func(board_state, max_player, turn_color, depth, depth_limit, alpha, beta):
    best_scores = {}
    if depth == depth_limit: # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
    else:  
        pieces = get_pieces(board_state, turn_color)
        pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
        for piece in pieces:
            actions = mv.get_moves(board_state, piece)
            for action in actions:
                # print("HERE MIN!!!!")
                # print(board_state)
                new_board_state = deepcopy(board_state)
                new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
                #print(new_board_state)
                b_score = max_alpha_beta_func(new_board_state, max_player, mv.change_turn(turn_color), depth + 1, depth_limit, alpha, beta) 
                #if b_score:
                min_score = min(b_score.values())
                best_scores[(piece, action)] = min_score
                if min_score <= alpha:
                    return best_scores
                beta = min(beta, min_score)
    return best_scores


'''SIMPLE MINIMAX TREE SEARCH CODE'''
                
def mini_max(board_state, max_player, turn_color, depth, depth_limit):
    best_scores = min_func(board_state, max_player, turn_color, depth, depth_limit)
    max_score = max(best_scores.values())
    max_actions = [action for action, score in best_scores.items() if score == max_score]
    if not max_actions:
        return None, None
    max_action = max_actions[0]
    # print('! max_score: ', max_score)
    # print('! max_action: ', max_action)
    return max_score, max_action

def max_func(board_state, max_player, turn_color, depth, depth_limit):
    best_scores = {}
    if depth == depth_limit or end_of_game(board_state, turn_color): # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
        return best_scores
    
    pieces = get_pieces(board_state, turn_color)
    pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
    for piece in pieces:
        actions = mv.get_moves(board_state, piece)
        for action in actions:
            # print("HERE MAX!!!!")
            # print(board_state)
            new_board_state = deepcopy(board_state)
            new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
            #print(new_board_state)
            b_score = min_func(new_board_state, max_player, mv.change_turn(turn_color), depth + 1, depth_limit) 
            if b_score:
                min_score = max(b_score.values())
                best_scores[(piece, action)] = min_score
    return best_scores


        
def min_func(board_state, max_player, turn_color, depth, depth_limit):
    best_scores = {}
    if depth == depth_limit or end_of_game(board_state, turn_color): # Stop condition if won the game
        best_scores[None] = utility_function(board_state, max_player)
        return best_scores
    
    pieces = get_pieces(board_state, turn_color)
    pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] # Only keep the pieces that can actually move
    for piece in pieces:
        actions = mv.get_moves(board_state, piece)
        for action in actions:
            # print("HERE MIN!!!!")
            # print(board_state)
            new_board_state = deepcopy(board_state)
            new_board_state, _ = list(mv.move(new_board_state, piece, actions, action))
            #print(new_board_state)
            b_score = max_func(new_board_state, max_player, mv.change_turn(turn_color), depth + 1, depth_limit) 
            if b_score:
                min_score = min(b_score.values())
                best_scores[(piece, action)] = min_score
                
    return best_scores




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
    

#print(recursive_loop(s_init, 0, 2))
    

def get_pieces(board_state, turn_color):
    pieces = []
    for row in range(ROWS):
        for col in range(COLS):
            piece = board_state[row][col]
            if piece != 0 and piece.color == turn_color:
                pieces.append(piece)
    return pieces


def end_of_game(board_state, turn_color):
    # Not sure if working correctly... before this happens a min() in the minimax is empty and returns error
    if get_pieces(board_state, WHITE) == 0:
        print("RED WIN")
        return True
    if get_pieces(board_state, RED) == 0:
        print("WHITE WIN")
        return True
    
    pieces = get_pieces(board_state, turn_color)
    pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] 
    if not pieces:
        print("No actions")
        return True
    
    return False

def utility_function(board_state, turn_color):
    maximizing_player = len( get_pieces(board_state, turn_color) )
    
    if turn_color == RED:
        minimizing_player = len( get_pieces(board_state, WHITE) )
    if turn_color == WHITE:
        minimizing_player = len( get_pieces(board_state, RED) )
        
    return maximizing_player - minimizing_player