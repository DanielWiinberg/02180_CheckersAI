from checkers.constants import ROWS, COLS, WHITE, RED
from checkers import moves as mv
from copy import deepcopy
import numpy as np


def get_pieces(board_state, turn_color):
    pieces = []
    for row in range(ROWS):
        for col in range(COLS):
            piece = board_state[row][col]
            if piece != 0 and piece.color == turn_color:
                pieces.append(piece)
    return pieces


def end_of_game(board_state, turn_color):
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

def get_kings(board_state, turn_color):
    kings = 0
    for row in range(ROWS):
        for col in range(COLS):
            piece = board_state[row][col]
            if piece != 0 and piece.color == turn_color and piece.king:
                kings += 1
    return kings


def get_backline_pieces(board_state, turn_color):
    if turn_color == RED:
        return np.shape([column for column in board_state[ROWS - 1] if column != 0 and column.color == RED])[0]
    if turn_color == WHITE:
        return np.shape([column for column in board_state[0] if column != 0 and column.color == WHITE])[0]


def utility_function(board_state, turn_color):
    # Weights, normal pieces are weight 1
    king_weight = 0.5
    backline_weight = 100
    
    kings_red = get_kings(board_state, RED)
    backline_pieces_red = get_backline_pieces(board_state, RED)
    pieces_red = np.shape(get_pieces(board_state, RED))[0]

    kings_white = get_kings(board_state, WHITE)
    backline_pieces_white = get_backline_pieces(board_state, WHITE)
    pieces_white = np.shape(get_pieces(board_state, WHITE))[0]

    util_value_red = ((kings_red - kings_white) * king_weight +
                      (pieces_red - pieces_white))
    
    util_value_white = ((kings_white - kings_red) * king_weight + 
                        (pieces_white - pieces_red))
    
    if turn_color == RED:
        return util_value_red
    else:
        return util_value_white



def get_board_signature(board_state):
    signature = ''
    for row in range(ROWS):
        for col in range(COLS):
            element = board_state[row][col]
            if board_state[row][col] !=0:
                signature += board_state[row][col].name
                if board_state[row][col].king:
                    signature += "_king"
                signature += ","
            else:
                signature += '0,'
    signature = signature[:-1] 
    #print(signature)        
    return signature