import pygame
import numpy as np
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, EDGE_SIZE, ROWS, COLS, WHITE, N_PIECES
import checkers.board as board
import checkers.moves as mv
import checkers.score as score
from checkers.piece import Piece
pygame.init()

from timeit import default_timer as timer
from algorithms.mini_max import *
from algorithms.mini_max_pruning import *
from algorithms.helper_functions import *



FPS = 60
RECURSION_LIMIT = 2
RECURSION_LIMIT2 = 3 

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

def ai_move(board_state, board_state_explored, turn, termination, ai_method='minimax'):
    n_white_pieces = len( get_pieces(board_state, WHITE) )
    n_red_pieces = len( get_pieces(board_state, RED) )

    if ai_method == 'minimax':
        max_score, max_action = mini_max(board_state, turn, turn, 0, termination)
        board_state_explored = []
    if ai_method == 'minimax_graph':
        max_score, max_action, board_state_explored = mini_max_graph(board_state, board_state_explored, turn, turn, 0, termination)
    if ai_method == 'alpha_beta':
        max_score, max_action = mini_max_alpha_beta(board_state, turn, turn, 0, termination)
        board_state_explored = []

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
    return board_state, moves, n_white_pieces, n_red_pieces, turn, board_state_explored



def main():
    run = True
    clock = pygame.time.Clock()
    
    board.draw_checker_board(WIN)
    board_state = board.create_pieces_board() 
    board_state_explored = []

    moves = []
    select = []
    n_white_pieces = N_PIECES
    n_red_pieces = N_PIECES
    turn = RED
    AI = WHITE
    AI2 = RED
    search_time1 = 0
    search_time2 = 0
    game_mode = 'AI2'

    while run:
        clock.tick(FPS) 
        pygame.time.wait(500)
        update(board_state, moves, n_white_pieces, n_red_pieces)
        
        if end_of_game(board_state, turn):
            print("WE HAVE A WINNER!!!")
            pygame.time.wait(2000)
            print(get_pieces(board_state, RED))
            
            print(get_pieces(board_state, WHITE))
            if len(get_pieces(board_state, RED))>len(get_pieces(board_state, WHITE)):
                print("RED WINS!!!")
            else:
                print("WHITE WINS!!!")
                
            run_winner = True
            while run_winner:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        run_winner = False
        else:   
            if turn == AI:
                start_time1 = timer()
                board_state, moves, n_white_pieces, n_red_pieces, turn, board_state_explored = ai_move(board_state, board_state_explored, turn, RECURSION_LIMIT)

                search_time1 += timer() - start_time1
                
                print(f'time to move(1): {timer() - start_time1}    total search time(1): {search_time1}')
                continue

            if game_mode == 'AI2':
                if turn == AI2:
                    start_time2 = timer()
                    board_state, moves, n_white_pieces, n_red_pieces, turn, board_state_explored = ai_move(board_state, board_state_explored, turn, RECURSION_LIMIT2)
                    search_time2 += timer() - start_time2
                    print(f'time to move(2): {timer() - start_time2}    total search time(2): {search_time2}')
                    #continue
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN and not game_mode == 'AI2':
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
                                    
                                # print(piece)
                                # print(row, col)
                                # print(moves)
                    
    pygame.quit()

main()