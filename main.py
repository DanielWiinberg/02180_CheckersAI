import pygame
import numpy as np
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, EDGE_SIZE, ROWS, COLS, WHITE, N_PIECES
#from checkers.game import Game
import checkers.board as board
import checkers.moves as mv
import checkers.score as score
pygame.init()
from algorithms.mini_max import mini_max

from checkers.piece import Piece


FPS = 60
RECURSION_LIMIT = 6

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y- EDGE_SIZE) // SQUARE_SIZE
    col = (x-EDGE_SIZE) // SQUARE_SIZE 
    return row, col

def update(board_matrix, moves, n_white_pieces, n_red_pieces):
    board.draw_checker_board(WIN)
    board.draw_pieces(WIN, board_matrix)
    score.draw_scores(WIN, N_PIECES - n_white_pieces, N_PIECES - n_red_pieces)
    #print(board_matrix)
    if moves:
      mv.draw_posible_moves(WIN,moves) 
    pygame.display.update()




def main():
    run = True
    clock = pygame.time.Clock()
    
    board.draw_checker_board(WIN)
    board_state = board.create_pieces_board() 
    moves = []
    select = []
    #print(board_matrix) 
    n_white_pieces = N_PIECES
    n_red_pieces = N_PIECES
    turn = RED
    while run:
        clock.tick(FPS)                
        #board.draw_pieces(WIN, board_matrix)     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                
                print(mini_max(board_state, turn, turn, 0, RECURSION_LIMIT))
                
                if moves:
                    if (row,col) in moves:
                        piece = board_state[select[0]][select[1]]
                        move = (row,col)
                        board_state,n_captures = mv.move(board_state, piece, moves, move) 
                        if turn == RED:
                            n_white_pieces = n_white_pieces - n_captures
                        else: 
                            n_red_pieces = n_red_pieces - n_captures
                        print(board_state) 
                        turn = mv.change_turn(turn)
                        moves = []
                        select = []
                        continue
                           
                if board_state[row][col]:
                    piece = board_state[row][col]
                    
                    if piece.color == turn:
                    
                        moves = mv.get_moves(board_state, piece)
                        if moves:
                            select = [row,col]
                        print(piece)
                        print(row, col)
                        print(moves)
                
        
        
        update(board_state, moves, n_white_pieces, n_red_pieces)
        
    pygame.quit()


main()