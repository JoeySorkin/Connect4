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

    def drop_coin(self, col):
        valid_drop = self.board[0][col] == 0  # is that column full?
        if valid_drop:
            row = self.__get_drop_row__(col)
            self.board[row][col] = 1 if self.player1turn else 2
            self.player1turn = not self.player1turn

    def print(self):
        print(self.board)

    def terminal(self, player):
        boardcopy = deepcopy(self.board)
        horizontal_kernel = np.array([[1, 1, 1, 1]])
        vertical_kernel = np.transpose(horizontal_kernel)
        diag1_kernel = np.eye(4, dtype=np.uint8)
        diag2_kernel = np.fliplr(diag1_kernel)
        detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]
        # fill the player we are checking with
        np.place(boardcopy, boardcopy != player, 0)
        if(player == 2):
            np.place(boardcopy, boardcopy != 0, 1)
        print("COPY",boardcopy)
        for kernel in detection_kernels:
            if (convolve2d(boardcopy, kernel, mode="valid") == 4).any():
                return True, player
        return False, None


    # minimax helpers

    pass

# inits for game loop
