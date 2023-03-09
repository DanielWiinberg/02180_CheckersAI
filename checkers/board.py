import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, GREY, WHITE, BROWN, BEIGE, DARK_BLUE, EDGE_SIZE, WIDTH_BOARD, HEIGHT_BOARD, HEIGHT, WIDTH, SCORE_BOX_WIDTH,PADDING,OUTLINE
from .piece import Piece
from .score import Score

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_score = self.white_score = 0
        self.red_kings = self.white_kings = 0
        self.create_board()
    
    def draw_squares(self, win):
        win.fill(DARK_BLUE)
        pygame.draw.rect(win, BROWN, (EDGE_SIZE,EDGE_SIZE,WIDTH_BOARD, HEIGHT_BOARD))
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BEIGE, (row*SQUARE_SIZE+EDGE_SIZE, col *SQUARE_SIZE+EDGE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
    def draw_scores(self, win):
        SCORE_BOX_LEFT = 2*EDGE_SIZE+WIDTH_BOARD
        SCORE_BOX_CENTER = SCORE_BOX_LEFT+SCORE_BOX_WIDTH//2
        
        font = pygame.font.SysFont("moolboran", 26)
        label = font.render("WHITE PLAYER CAPTURES", 1, WHITE)
        text_rect = label.get_rect(center=(SCORE_BOX_CENTER,2* EDGE_SIZE))
        win.blit(label, text_rect)
        label = font.render("RED PLAYER CAPTURES", 1, WHITE)
        text_rect = label.get_rect(center=(SCORE_BOX_CENTER,2* EDGE_SIZE+HEIGHT_BOARD//2))
        win.blit(label, text_rect)
        
        Score.draw_scores(self, win, RED)
        Score.draw_scores(self, win, WHITE)
        
        # radius = SQUARE_SIZE//2 - PADDING
        # pygame.draw.circle(win, GREY, (self.x, self.y), radius + OUTLINE)
        # pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1 

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    def draw(self, win):
        self.draw_squares(win)
        self.draw_scores(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                    self.white_score += 1
                else:
                    self.white_left -= 1
                    self.red_score += 1
    
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        
        return None 
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves