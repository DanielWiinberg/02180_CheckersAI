import pygame
import numpy as np
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, EDGE_SIZE, ROWS, COLS, WHITE, N_PIECES
#from checkers.game import Game
import checkers.board as board
import checkers.moves as mv
import checkers.score as score
pygame.init()
import algorithms.mini_max as minimax
# from algorithms.mini_max import mini_max
# from algorithms.mini_max import get_pieces

from timeit import default_timer as timer

from checkers.piece import Piece


FPS = 60
RECURSION_LIMIT = 3
RECURSION_LIMIT2 = 4 

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

def ai_move(board_state, turn, termination, ai_method='minimax'):
    n_white_pieces = len( minimax.get_pieces(board_state, WHITE) )
    n_red_pieces = len( minimax.get_pieces(board_state, RED) )

    if ai_method == 'minimax':
        max_score, max_action = minimax.mini_max(board_state, turn, turn, 0, termination)
    
    piece = max_action[0]
    move = max_action[1]
    moves = mv.get_moves(board_state, piece)
    board_state,n_captures = mv.move(board_state, piece, moves, move) 
    if turn == RED:
        n_white_pieces = n_white_pieces - n_captures
    else: 
        n_red_pieces = n_red_pieces - n_captures
    moves = []
    select = []
    turn = mv.change_turn(turn)
    return board_state, moves, n_white_pieces, n_red_pieces, turn



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
    AI = WHITE
    AI2 = RED
    search_time1 = 0
    search_time2 = 0

    update(board_state, moves, n_white_pieces, n_red_pieces)

    while run:
        clock.tick(FPS)                
        #board.draw_pieces(WIN, board_matrix)     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if turn == AI:
                start_time1 = timer()

                board_state, moves, n_white_pieces, n_red_pieces, turn = ai_move(board_state, turn, RECURSION_LIMIT)
                update(board_state, moves, n_white_pieces, n_red_pieces)

                search_time1 += timer() - start_time1
                print(f'time to move(1): {timer() - start_time1}    total search time(1): {search_time1}')
                continue

            if turn == AI2:
                start_time2 = timer()

                board_state, moves, n_white_pieces, n_red_pieces, turn = ai_move(board_state, turn, RECURSION_LIMIT2)
                update(board_state, moves, n_white_pieces, n_red_pieces)

                search_time2 += timer() - start_time2
                print(f'time to move(2): {timer() - start_time2}    total search time(2): {search_time2}')
                continue

            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    
                    
                    if moves:
                        if (row,col) in moves:
                            piece = board_state[select[0]][select[1]]
                            move = (row,col)
                            board_state,n_captures = mv.move(board_state, piece, moves, move) 
                            if turn == RED:
                                n_white_pieces = n_white_pieces - n_captures
                            else: 
                                n_red_pieces = n_red_pieces - n_captures
                            
                            #print(board_state) 
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
                            #print(piece)
                            #print(row, col)
                            #print(moves)

        
        update(board_state, moves, n_white_pieces, n_red_pieces)
        
    pygame.quit()


main()





                # start = timer()
                # max_score, max_action = mini_max(board_state, turn, turn, 0, RECURSION_LIMIT)
                # piece = max_action[0]
                # move = max_action[1]
                # moves = mv.get_moves(board_state, piece)
                # board_state,n_captures = mv.move(board_state, piece, moves, move) 
                # if turn == RED:
                #     n_white_pieces = n_white_pieces - n_captures
                # else: 
                #     n_red_pieces = n_red_pieces - n_captures
                # #print(board_state) 
                # turn = mv.change_turn(turn)
                # moves = []
                # select = []
                # end = timer()
                # print(f'time to move: {end - start}')
                # update(board_state, moves, n_white_pieces, n_red_pieces)