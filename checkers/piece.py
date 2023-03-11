import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN, EDGE_SIZE,PADDING,OUTLINE

class Piece:

    def __init__(self, row, col, color, name, king=False):
        self.row = row
        self.col = col
        self.color = color
        self.name = name + '_' + str(row) + str(col)
        self.king = king
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 + EDGE_SIZE
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 + EDGE_SIZE

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.name)