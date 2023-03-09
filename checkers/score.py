
import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN, EDGE_SIZE, WIDTH_BOARD, SCORE_BOX_WIDTH, HEIGHT_BOARD, PADDING, OUTLINE, COLS


class Score:
    def __init__(self, white_score,red_score):
        self.white_score = white_score
        self.red_score = red_score
        # self.white_line = 0
        # self.red_line = 0
    
    
    def draw_scores(self, win, color):
        SCORE_BOX_LEFT = 2*EDGE_SIZE+WIDTH_BOARD
        SCORE_BOX_CENTER = SCORE_BOX_LEFT+SCORE_BOX_WIDTH//2

        if color == RED:
            score = self.white_score
            START_POS_Y = 3* EDGE_SIZE
        else: 
            score = self.red_score
            START_POS_Y = 3* EDGE_SIZE + HEIGHT_BOARD//2
        
        radius = SQUARE_SIZE//2 - PADDING
        piece_row = 0
        for i_piece in range(score):
            n_piece =  i_piece         
            if i_piece+1>(COLS):
                piece_row = 2
                n_piece =  i_piece - COLS
            elif i_piece+1>(COLS//2):
                piece_row = 1
                n_piece =  i_piece - COLS//2
            pos_y = START_POS_Y + radius + (SQUARE_SIZE- PADDING)*piece_row
            pos_x = SCORE_BOX_CENTER - 2*(SQUARE_SIZE- PADDING) + SQUARE_SIZE//2 + n_piece*(SQUARE_SIZE- PADDING)
                
            pygame.draw.circle(win, GREY, (pos_x, pos_y), radius + OUTLINE)
            pygame.draw.circle(win, color, (pos_x, pos_y), radius)