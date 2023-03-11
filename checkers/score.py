
import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN, EDGE_SIZE, WIDTH_BOARD, SCORE_BOX_WIDTH, HEIGHT_BOARD, PADDING, OUTLINE, COLS


def draw_scores(win, white_score, red_score):
    SCORE_BOX_LEFT = 2*EDGE_SIZE+WIDTH_BOARD
    SCORE_BOX_CENTER = SCORE_BOX_LEFT+SCORE_BOX_WIDTH//2
    
    font = pygame.font.SysFont("moolboran", 26)
    label = font.render("WHITE PLAYER CAPTURES", 1, WHITE)
    text_rect = label.get_rect(center=(SCORE_BOX_CENTER,2* EDGE_SIZE))
    win.blit(label, text_rect)
    label = font.render("RED PLAYER CAPTURES", 1, WHITE)
    text_rect = label.get_rect(center=(SCORE_BOX_CENTER,2* EDGE_SIZE+HEIGHT_BOARD//2))
    win.blit(label, text_rect)
    
    draw_score(win, RED, red_score)
    draw_score(win, WHITE, white_score)

def draw_score(win, color, score):
    SCORE_BOX_LEFT = 2*EDGE_SIZE+WIDTH_BOARD
    SCORE_BOX_CENTER = SCORE_BOX_LEFT+SCORE_BOX_WIDTH//2

    if color == RED:
        START_POS_Y = 3* EDGE_SIZE
    else: 
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