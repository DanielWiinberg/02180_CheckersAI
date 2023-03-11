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
    print('---' , depth, turn_color, '---')
    best_score_for_each_action = []
    actions_pieces = []
    
    if depth == depth_limit: #TODO: Stop condition if won the game
        best_score_for_each_action.append(utility_function(board_state, max_player))
    else:
        pieces = get_pieces(board_state, turn_color) #Retrieves all pieces
        pieces = [piece for piece in pieces if mv.get_moves(board_state, piece)] #Only keep the pieces that can actually move
        print('all moveable pieces: ', pieces)
        for piece in pieces:
            actions = mv.get_moves(board_state, piece)
            print('Piece: ', piece, 'Actions: ', actions)
            for action in actions:
                new_board_state, _ = mv.move(board_state, piece, actions, action)
                
                if depth == 0: #Only appending the piece and actions at depth 0
                    actions_pieces.append( (piece, action) )
                print('depth: ', depth, 'action pieces - inner: ', actions_pieces)

                score, _ = mini_max(new_board_state, max_player, mv.change_turn(turn_color), depth+1, depth_limit)
                best_score_for_each_action.append(score)
                depth -= 1
    

    print('! best scores: ', best_score_for_each_action)
    print('! action pieces: ', actions_pieces)
    
    if (depth % 2) == 0:
        max_ = max(best_score_for_each_action)
        if depth == 0: # Only looking for index at depth 0...
            actions_pieces.append( (piece, action) )
            max_index = best_score_for_each_action.index(max_)
            max_action = actions_pieces[max_index]
        else:
            max_action = None
        return (max_, max_action)

    else:
        min_ = min(best_score_for_each_action)
        if depth == 0:
            actions_pieces.append( (piece, action) )
            min_index = min(best_score_for_each_action.index(min))
            min_action = actions_pieces[min_index]
        else:
            min_action = None
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