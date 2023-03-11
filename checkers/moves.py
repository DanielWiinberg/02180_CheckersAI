import pygame
from .constants import BLACK, ROWS, RED, GREEN, SQUARE_SIZE, COLS, GREY, WHITE, BROWN, BEIGE, DARK_BLUE, EDGE_SIZE, WIDTH_BOARD, HEIGHT_BOARD, HEIGHT, WIDTH, SCORE_BOX_WIDTH,PADDING,OUTLINE
from .piece import Piece


def get_moves(board_matrix, piece):
    row = piece.row
    col = piece.col
    turn = piece.color
    
    moves = {}
    if piece.color == RED or piece.king:
        direction=-1
        moves.update(get_left(board_matrix,row,col, direction, piece, []))
        moves.update(get_right(board_matrix,row,col, direction, piece, []))
        
    if piece.color == WHITE or piece.king:
        direction=1
        moves.update(get_left(board_matrix,row,col, direction, piece, [])) 
        moves.update(get_right(board_matrix,row,col, direction, piece, [])) 
          
    return moves


 
def get_left(board_matrix, row, col, dir, piece, captured):
    moves = {}
    if col-1>=0 and 0<=row+dir<COLS:

        # If not in dictionary, create the value and set it         
        if not board_matrix[row+dir][col-1] and piece.row == row and piece.col == col: 
            moves.update({(row+dir, col-1):[]})
            
        # 1. Check bounds of boards
        # 2. Check element is there
        # 3. Check adjacent piece color is different
        # 4. Check space to jump a piece
        elif (col-2>=0 
              and 0<=row+dir*2<COLS 
              and board_matrix[row+dir][col-1] != 0
              and board_matrix[row+dir][col-1].color != piece.color 
              and not board_matrix[row+dir*2][col-2]):
            new_captured = list(captured)
            new_captured.append(board_matrix[row+dir][col-1])
            
            # Possibility to jump a piece more than once
            moves.update(get_right(board_matrix, row+dir*2, col-2, dir, piece, new_captured))
            moves.update(get_left(board_matrix, row+dir*2, col-2, dir, piece, new_captured))
            
            new_captured = list(set(new_captured))
            moves.update({(row+dir*2, col-2): new_captured})
            
    return moves


def get_right(board_matrix, row, col, dir, piece, captured):
    moves = {}
    if col+1<COLS and 0<=row+dir<COLS:
        
        if not board_matrix[row+dir][col+1] and piece.row == row and piece.col == col: 
            moves.update({(row+dir, col+1):[]})
            
        elif (col+2<COLS 
              and 0<=row+dir*2<COLS 
              and board_matrix[row+dir][col+1] != 0 
              and board_matrix[row+dir][col+1].color != piece.color 
              and not board_matrix[row+dir*2][col+2]):
            new_captured = list(captured)
            new_captured.append(board_matrix[row+dir][col+1])
            
            moves.update(get_right(board_matrix, row+dir*2, col+2, dir, piece, new_captured))
            moves.update(get_left(board_matrix, row+dir*2, col+2, dir, piece, new_captured))
            
            new_captured = list(set(new_captured))
            moves.update({(row+dir*2, col+2): new_captured})
            
    return moves

    

              
def move(board_state, piece, moves ,move):
    row, col = piece.row, piece.col
    new_row, new_col = move[0], move[1]
    captures = moves[move]
    
    king = board_state[row][col].king
    if new_row == ROWS - 1 or new_row == 0:
        king = True
    
    board_state[new_row][new_col] = Piece(new_row, new_col, board_state[row][col].color, board_state[row][col].name, king) 
    board_state[row][col] = 0
    n_captures = 0
    for capture in captures:
        print("captured")
        print(capture)
        n_captures += 1
        board_state[capture.row][capture.col] = 0        
    

                
    return board_state, n_captures
  
def draw_posible_moves(win,moves):
    for move in list(moves.keys()):
        row, col = move
        pygame.draw.circle(win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE//2 + EDGE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE//2 + EDGE_SIZE), 15) 


def change_turn(turn):
    if turn == RED:
        turn = WHITE
    else:
        turn = RED
    return turn