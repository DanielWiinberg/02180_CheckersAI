import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN, PADDING,OUTLINE

class Piece:

    def __init__(self, row, col, color, name, king = False):
        self.row = row
        self.col = col
        self.color = color
        if color == RED:
            name="RED"
        else:
            name="WHITE"
        self.name = name + '_' + str(row) + str(col)
        self.king = king
        self.x = 0
        self.y = 0

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))


    def __repr__(self):
        return str(self.name)