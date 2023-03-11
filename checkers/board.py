import pygame
from .constants import BLACK, ROWS, RED, GREEN, SQUARE_SIZE, COLS, GREY, WHITE, BROWN, BEIGE, DARK_BLUE, EDGE_SIZE, WIDTH_BOARD, HEIGHT_BOARD, HEIGHT, WIDTH, SCORE_BOX_WIDTH,PADDING,OUTLINE
from .piece import Piece


    
def draw_checker_board(win):
    #print(self.board)
    win.fill(DARK_BLUE)
    pygame.draw.rect(win, BROWN, (EDGE_SIZE,EDGE_SIZE,WIDTH_BOARD, HEIGHT_BOARD))
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, BEIGE, (row*SQUARE_SIZE+EDGE_SIZE, col *SQUARE_SIZE+EDGE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                
def draw_scores(win):
    SCORE_BOX_LEFT = 2*EDGE_SIZE+WIDTH_BOARD
    SCORE_BOX_CENTER = SCORE_BOX_LEFT+SCORE_BOX_WIDTH//2
    
    font = pygame.font.SysFont("moolboran", 26)
    label = font.render("WHITE PLAYER CAPTURES", 1, WHITE)
    text_rect = label.get_rect(center=(SCORE_BOX_CENTER,2* EDGE_SIZE))
    win.blit(label, text_rect)
    label = font.render("RED PLAYER CAPTURES", 1, WHITE)
    text_rect = label.get_rect(center=(SCORE_BOX_CENTER,2* EDGE_SIZE+HEIGHT_BOARD//2))
    win.blit(label, text_rect)
    
    Score.draw_scores(win, RED)
    Score.draw_scores(win, WHITE)
    

def create_pieces_board():
    board_matrix = [[0] * (COLS) for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            if col % 2 == ((row +  1) % 2):
                if row < 3:
                    board_matrix[row][col] = Piece(row, col, WHITE, 'WHITE')
                elif row > 4:
                    #print(Piece(row, col, RED, 'RED'))
                    board_matrix[row][col] = Piece(row, col, RED, 'RED')
                else:
                    board_matrix[row][col] = 0
            else:
                board_matrix[row][col] = 0
    return board_matrix

def draw_pieces(win, board_matrix):
    for row in range(ROWS):
        for col in range(COLS):
            piece = board_matrix[row][col]
            if piece != 0:
                piece.draw(win)
                



