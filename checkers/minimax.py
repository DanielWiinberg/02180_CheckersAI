import pygame
from .constants import *
from checkers.board import Board
from checkers.game import Game
import copy

class Minimax:

# White maximizes, red minimizes.
    board = Board()

    def utility_function(self, state):
        value = board.white_left - board.red_left #can add: + C * (Board.white_kings - Board.red_kings)
        print(value)
        return value
    
    def minimax(self, piece):

        game_board = copy.deepcopy(game)


        for move in Game.moves: