from copy import deepcopy

import numpy as np
from scipy.signal import convolve2d

ROWS = 6
COLUMNS = 7


class Board:
    def __init__(self):
        self.board = np.zeros((ROWS, COLUMNS))  # create new empty board, 0s represent empty
        self.player1turn = True

    # drop functions
    def __get_drop_row__(self, col):
        for row in reversed(range(ROWS)):
            if self.board[row][col] == 0:
                return row  # traverses up the board, the first empty cell from the bottom is returned

    def __is_valid_drop__(self, col):
        return self.board[0][col] == 0  # is that column full?

    def drop_coin(self, col):
        valid_drop = self.__is_valid_drop__(col)
        if valid_drop:
            row = self.__get_drop_row__(col)
            self.board[row][col] = 1 if self.player1turn else 2
            self.player1turn = not self.player1turn

    def print(self):
        print(self.board)
