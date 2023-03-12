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



                
def mini_max1(board_state, max_player, turn_color, depth, depth_limit):
    best_score_for_each_action = []
    actions_pieces = []
    pieces = get_pieces(board_state, turn_color)
    for piece in pieces:
        actions = mv.get_moves(board_state, piece)
        if actions:
            print('Actions: ')
            print(actions)
            for action in actions:
                new_board_state, _ = mv.move(board_state, piece, actions, action)
                actions_pieces.append( (piece, action) )
                
                if  depth < depth_limit:
                    depth +=1
                    score, _ = mini_max(new_board_state, max_player, mv.change_turn(turn_color), depth+1, depth_limit) 
                    best_score_for_each_action.append(score)
                    depth -= 1
                else:
                    best_score_for_each_action.append(utility_function(board_state, max_player))

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
            return (None, None)
        min_action = actions_pieces[min_index]
        return (min_, min_action)



def mini_max(board_state, max_player, turn_color, depth, depth_limit):
    best_scores = {}
    
    if depth == depth_limit or end_of_game(board_state): # Stop condition if won the game
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


def end_of_game(board_state):
    # Not sure if working correctly... before this happens a min() in the minimax is empty and returns error
    if get_pieces(board_state, WHITE) == 0 or get_pieces(board_state, RED) == 0: return True

def utility_function(board_state, turn_color):
    maximizing_player = len( get_pieces(board_state, turn_color) )
    
    if turn_color == RED:
        minimizing_player = len( get_pieces(board_state, WHITE) )
    if turn_color == WHITE:
        minimizing_player = len( get_pieces(board_state, RED) )
        
    return maximizing_player - minimizing_player