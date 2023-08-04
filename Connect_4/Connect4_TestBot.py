#Test bot for connect 4
from Connect_4 import Player
from Connect_4 import Board
from Connect_4 import board_change
from Connect_4 import win_check

def mult_change(bot : Player,board : Board,*nums):
    for num in nums:
        bot.choice = num
        board_change(bot,board)
    
class Horiz_Tests:
    def ht1(test_bot1 : Player,test_bot2 : Player,board : Board):
        mult_change(test_bot1,board,1,2,3,4)
        board.print_board()
    
    def ht2(test_bot1 : Player,test_bot2 : Player,board : Board):
        mult_change(test_bot2,board,1,2,3)
        mult_change(test_bot1,board,1,2,3,4,4)
        board.print_board()
        
    def ht3(test_bot1 : Player,test_bot2 : Player,board : Board):
        """Meant to fail"""
        mult_change(test_bot1,board,1,5,6,7)
        board.print_board()

class Vert_Tests:
    def vt1(test_bot1 : Player,test_bot2 : Player,board : Board):
        mult_change(test_bot1,board,1,1,1,1)
        board.print_board()
    
    def vt2(test_bot1 : Player,test_bot2 : Player,board : Board):
        mult_change(test_bot2,board,1)
        mult_change(test_bot1,board,1,1,1,1)
        board.print_board()
    
    def vt3(test_bot1 : Player,test_bot2 : Player,board : Board):
        mult_change(test_bot1,board,7,7,7,7)
        board.print_board()

class Pos_Diag_Tests:
    def pdt1(test_bot1 : Player,test_bot2 : Player,board : Board):
        mult_change(test_bot2,board,4,4,4,5,5,6)
        mult_change(test_bot1,board,7,6,5,4)
        board.print_board()

    def pdt2(test_bot1 : Player,test_bot2 : Player,board : Board):
        mult_change(test_bot2,board,4,4,4,4,5,5,5,6,6)
        mult_change(test_bot1,board,7,6,5,4)        
        board.print_board()

    def pdt3(test_bot1 : Player,test_bot2 : Player,board : Board):
        """Meant to fail"""
        mult_change(test_bot2,board,7,6,6,5,5,5)
        mult_change(test_bot1,board,1,7,6,5)
        board.print_board()

class Neg_Diag_Tests:
    def ndt1(test_bot1 : Player,test_bot2 : Player,board : Board):
        mult_change(test_bot2,board,7,7,7,6,6,5)
        mult_change(test_bot1,board,7,6,5,4)
        board.print_board()

    def ndt2(test_bot1 : Player,test_bot2 : Player,board : Board):
        mult_change(test_bot2,board,4,4,4,3,3,2)
        mult_change(test_bot1,board,4,3,2,1)
        board.print_board()

    def ndt3(test_bot1 : Player,test_bot2 : Player,board : Board):
        """Meant to fail"""
        mult_change(test_bot2,board,7,7,6,1,1,1,2,2,2)
        mult_change(test_bot1,board,7,6,1,1,2,2,2)
        board.print_board()

def tie_test(test_bot1 : Player,test_bot2 : Player,board : Board):
    mult_change(test_bot1,board,1,1,1,3,3,3,5,5,5,7,7,7)
    mult_change(test_bot2,board,2,2,2,4,4,4,6,6,6)
    mult_change(test_bot2,board,1,1,1,3,3,3,5,5,5,7,7,7)
    mult_change(test_bot1,board,2,2,2,4,4,4,6,6,6)
    board.print_board()
    if not bool(win_check(board)):
        board.board_list.clear()
        for num in range(42): board.board_list.append(num + 1)
        return True
    return False

def all_horiz(b1 : Player,b2 : Player,board : Board):
    Horiz_Tests.ht1(b1,b2,board)
    if not bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    Horiz_Tests.ht2(b1,b2,board)
    if not bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    Horiz_Tests.ht3(b1,b2,board)
    if bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    return True

def all_vert(b1 : Player,b2 : Player,board : Board):
    Vert_Tests.vt1(b1,b2,board)
    if not bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    Vert_Tests.vt2(b1,b2,board)
    if not bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    Vert_Tests.vt3(b1,b2,board)
    if not bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    return True

def all_pdiags(b1 : Player,b2 : Player,board : Board):
    Pos_Diag_Tests.pdt1(b1,b2,board)
    if not bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    Pos_Diag_Tests.pdt2(b1,b2,board)
    if not bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    Pos_Diag_Tests.pdt3(b1,b2,board)
    if bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    return True

def all_ndiags(b1 : Player,b2 : Player,board : Board):
    Neg_Diag_Tests.ndt1(b1,b2,board)
    if not bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    Neg_Diag_Tests.ndt2(b1,b2,board)
    if not bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    Neg_Diag_Tests.ndt3(b1,b2,board)
    if bool(win_check(board)):
        return False
    board.board_list.clear()
    for num in range(42): board.board_list.append(num + 1)
    return True

def run(b1,b2):
    board = Board()
    assert all_horiz(b1,b2,board) ,'Horizontal tests failed'
    assert all_vert(b1,b2,board) ,'Vertical tests failed'
    assert all_pdiags(b1,b2,board) ,'Positive Diag tests failed'
    assert all_ndiags(b1,b2,board) ,'Negative Diag tests failed'
    assert tie_test(b1,b2,board) ,'Tie Test failed'
    print('\nAll tests passed succesfully')
    


if __name__ == '__main__':
    test_bot1 = Player()
    test_bot1.color = '37;'
    test_bot1.name = 'TB1'
    test_bot2 = Player()
    test_bot2.color = '35;'
    test_bot2.name = 'TB2'
    run(test_bot1,test_bot2)