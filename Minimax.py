import math
from copy import deepcopy
import numpy as np
from scipy.signal import convolve2d

from Board import COLUMNS, ROWS


def actions(board):
    """
    :param board:
    :return: list of actions (columns that the coin can be dropped)
    """
    action_list = []
    for col in range(COLUMNS):
        if board.__is_valid_drop__(col):
            action_list.append(col)
    return action_list


def result(board, action):
    """
    :param board: Board instance
    :param action: number (column)
    :return: a board with the action applied
    """
    newboard = deepcopy(board)
    newboard.drop_coin(action)
    return newboard


def terminal(board):
    """
    :param board: Board instance
    :return: Tuple (if a player won, which player)
    """
    player = 2 if board.player1turn else 1
    boardcopy = deepcopy(board.board)
    horizontal_kernel = np.array([[1, 1, 1, 1]])
    vertical_kernel = np.transpose(horizontal_kernel)
    diag1_kernel = np.eye(4, dtype=np.uint8)
    diag2_kernel = np.fliplr(diag1_kernel)
    detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]
    # fill the player we are checking with
    np.place(boardcopy, boardcopy != player, 0)
    if player == 2:
        np.place(boardcopy, boardcopy != 0, 1)
    for kernel in detection_kernels:
        if (convolve2d(boardcopy, kernel, mode="valid") == 4).any():
            return True, player
    return False, 0


def minimax(board):
    if terminal(board)[0]:
        return None
    else:
        if not board.player1turn:
            value, move = MAX(board)
            return value, move
        else:
            value, move = MINI(board)
            return value, move


def MINI(boardin):
    v = math.inf
    bottom_node, winner = terminal(boardin)
    moveout = None
    if bottom_node:
        if winner == 1:
            return 1, None
        elif winner == 2:
            return -1, None

    for action in actions(boardin):
        newboard = result(boardin, action)
        aux, act = MAX(result(newboard, action))
        if aux < v:
            v = aux
            moveout = action
            if v == -1:
                return v, moveout
    return v, moveout


def MAX(boardin):
    v = -math.inf
    bottom_node, winner = terminal(boardin)
    moveout = None
    if bottom_node:
        if winner == 1:
            return -1, None
        elif winner == 2:
            return 1, None
    for action in actions(boardin):
        newboard = result(boardin, action)
        aux, act = MINI(result(newboard, action))
        if aux > v:
            v = aux
            moveout = action
            if v == 1:
                return v, moveout
    return v, moveout
