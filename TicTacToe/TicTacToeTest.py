from TicTacToe import Board
from TicTacToe import HardAI

def test():
    #Board setup
    board = Board()
    player1 = HardAI('Computer','X') 
    board.change(1,'O')
    board.change(2,'O')
    board.change(player1.optimalMove(),'X')
    board.printBoard()

test()