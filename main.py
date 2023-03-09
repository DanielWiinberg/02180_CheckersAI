import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, EDGE_SIZE
from checkers.game import Game
from checkers.board import Board
pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')



def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y- EDGE_SIZE) // SQUARE_SIZE
    col = (x-EDGE_SIZE) // SQUARE_SIZE 
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    board = Board()

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print('Winner: ', game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                
                #print(board.board) # loop igennem
                #piece = board.get_piece(row,col)
                #print(board.get_valid_moves(piece))

        game.update()
    
    pygame.quit()


main()