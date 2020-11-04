from Connect4 import *

board = Board()
gameover = False
winner = None


# game loop
# for i in range (COLUMNS):
#     for j in range(i):
#         board.drop_coin(i)
def start():
    global gameover
    global winner
    while not gameover:
        # Ask p1 input
        board.print()
        if board.player1turn:
            col = int(input("Player 1 choose a column:  "))
            board.drop_coin(col)
            gameover, winner = board.terminal(1)
        # Ask p2 input
        else:
            col = int(input("Player 2 choose a column:  "))
            board.drop_coin(col)
            gameover, winner = board.terminal(2)

    print(winner, "Wins!")
