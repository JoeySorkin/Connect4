import time

from Board import *
from Minimax import *
import pygame


# game loop
# for i in range (COLUMNS):
#     for j in range(i):
#         board.drop_coin(i)
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([520, 500])
        self.board = Board()

        for i in range(COLUMNS):
            for j in range(i):
                self.board.drop_coin(j)
        self.gameover = False
        self.winner = None

    def start(self):
        self.screen.fill((255, 255, 255))
        while not self.gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover = True

            # Ask p1 input
            self.board.print()
            if self.board.player1turn:
                col = int(input("Player 1 choose a column:  "))
                self.board.drop_coin(col)
                print("TERMINAL", terminal(self.board))
                self.gameover, self.winner = terminal(self.board)
            # Ask p2 input
            else:
                print("Player 2 choose a column:  ")
                v, mov = minimax(self.board)
                self.board.drop_coin(mov)
            for cols in range(0, COLUMNS):
                for rows in range(0, ROWS):
                    print("RC", cols, rows)
                    coef = 50
                    col = cols + 1
                    row = rows + 1
                    loc = (20 + col * 60, 20 + row * 60)
                    color = (0, 0, 0)
                    if self.board.board[rows, cols] == 2:
                        color = (255, 0, 0)
                    elif self.board.board[rows, cols] == 1:
                        color = (0, 0, 255)
                    pygame.draw.circle(self.screen, color, loc, 20)
            pygame.display.flip()
            time.sleep(1)
        print(self.winner, "Wins!")

    pygame.quit()
