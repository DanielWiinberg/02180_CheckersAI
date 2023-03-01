import pygame
from .constants import GREY, WHITE, BLACK, YELLOW, SQUARE_SIZE

class Piece:
    PADDING = 15
    OUTLINE = 2
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        
        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1
            
        self.calculate_position_on_board()
            
    def calculate_position_on_board(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        
    def make_king(self):
        self.king = True
        
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position_on_board()
        
    def draw_piece(self, window):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.king:
            pygame.draw.circle(window, YELLOW, (self.x, self.y), radius//2)
        
    def __repr__(self):
        return str(self.color) + ' at location: ' + str(self.x, self.y)