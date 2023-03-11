from checkers.constants import ROWS, COLS, WHITE, RED
from checkers import moves as mv
from copy import deepcopy

s_3 = [4, 1]
s_4 = [8, 5]

s_5 = [1, 2]
s_6 = [7, 6]


s_1 = [s_3, s_4]
s_2 = [s_5, s_6]

s_init = [s_1, s_2]


def mini_max(board_state, max_player, turn_color, depth, depth_limit):
    best_score_for_each_action = []
    actions_pieces = []
    
    if depth == depth_limit: #TODO: Stop condition if won the game
        best_score_for_each_action.append(utility_function(board_state, max_player))
    else:
        pieces = get_pieces(board_state, turn_color)
        
        for piece in pieces:
            actions = mv.get_moves(board_state, piece)
            print('Actions: ')
            print(actions)
            for action in actions:
                new_board_state, _ = mv.move(board_state, piece, actions, action)
                
                actions_pieces.append( (piece, action) )
                
                score, _ = mini_max(new_board_state, max_player, mv.change_turn(turn_color), depth+1, depth_limit) 
                best_score_for_each_action.append(score)
                depth -= 1
    

    
    print('best scores: ')
    print(best_score_for_each_action)
    
    if (depth % 2) == 0:
        max_ = max(best_score_for_each_action)
        max_index = best_score_for_each_action.index(max_)
        
        print('actions_pieces: ')            
        print(actions_pieces)
        
        max_action = actions_pieces[max_index]
        return (max_, max_action)

    else:
        min_ = min(best_score_for_each_action)
        min_index = min(best_score_for_each_action.index(min))
        
        print('actions_pieces: ')            
        print(actions_pieces)
        
        if len( actions_pieces ) == 0:
            return (0, None)
        min_action = actions_pieces[min_index]
        return (min_, min_action)
    

#print(recursive_loop(s_init, 0, 2))
    

def get_pieces(board_state, turn_color):
    pieces = []
    for row in range(ROWS):
        for col in range(COLS):
            piece = board_state[row][col]
            if piece != 0 and piece.color == turn_color:
                pieces.append(piece)
    return pieces

def utility_function(board_state, turn_color):
    maximizing_player = len( get_pieces(board_state, turn_color) )
    
    if turn_color == RED:
        minimizing_player = len( get_pieces(board_state, WHITE) )
    if turn_color == WHITE:
        minimizing_player = len( get_pieces(board_state, RED) )
        
    return maximizing_player - minimizing_player