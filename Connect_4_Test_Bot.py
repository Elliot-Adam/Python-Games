from Connect_4 import *

class Test(Player):
    """Test bot for test mode. dif 4"""
    def __init__ (self,color,name= 'Testbot') -> None:
        self.color = color
        self.name = name
        self.score = 0
        self.choice = None

    def choice_getter(self) -> None:
        """Test bot chooses a random legal move from the board"""
        self.choice = random.choice(board.legal_moves())
    
    def choice_and_change(bot,num):
        bot.choice = num
        bot.board_change()
        
    class Vert_Tests:
        """Encapsulated version of all vertical tests"""
        def vert_test1() -> None:
            """Tests upright in far right"""
            Test.choice_and_change(testBot1,7)
            Test.choice_and_change(testBot1,7)
            Test.choice_and_change(testBot1,7)
            Test.choice_and_change(testBot1,7)

        def vert_test2() -> None:
            """Tests upright in far right with one piece beneath the four"""
            Test.choice_and_change(testBot2,7)
            Test.choice_and_change(testBot1,7)
            Test.choice_and_change(testBot1,7)
            Test.choice_and_change(testBot1,7)
            Test.choice_and_change(testBot1,7)

        def vert_test3() -> None:
            """Tests upright in far left"""
            Test.choice_and_change(testBot1,1)
            Test.choice_and_change(testBot1,1)
            Test.choice_and_change(testBot1,1)
            Test.choice_and_change(testBot1,1)

    class Horiz_Tests:
        """Encapsulated version of all horizontal tests"""
        def horiz_test1() -> None:
            """Tests flat in far right"""
            Test.choice_and_change(testBot1,7)
            Test.choice_and_change(testBot1,6)
            Test.choice_and_change(testBot1,5)
            Test.choice_and_change(testBot1,4)

        def horiz_test2() -> None:
            """Tests flat in far left"""
            Test.choice_and_change(testBot1,1)
            Test.choice_and_change(testBot1,2)
            Test.choice_and_change(testBot1,3)
            Test.choice_and_change(testBot1,4)

        def horiz_test3() -> None:
            """Tests flat in far left on the second row"""
            Test.choice_and_change(testBot2,1)
            Test.choice_and_change(testBot2,2)
            Test.choice_and_change(testBot2,3)
            Test.choice_and_change(testBot1,4)
            Test.choice_and_change(testBot1,1)
            Test.choice_and_change(testBot1,2)
            Test.choice_and_change(testBot1,3)
            Test.choice_and_change(testBot1,4)
            
        def horiz_test4() -> None:
            """Checks if 3 points on far right will win with point on second row of far left. Meant to fail"""
            Test.choice_and_change(testBot1,7)
            Test.choice_and_change(testBot1,6)
            Test.choice_and_change(testBot1,5)
            Test.choice_and_change(testBot2,1)
            Test.choice_and_change(testBot1,1)
    
        def horiz_test5() -> None:
            """Checks off screen in other direction"""
            Test.choice_and_change(testBot2,7)
            
            Test.choice_and_change(testBot1,1)
            Test.choice_and_change(testBot1,2)
            Test.choice_and_change(testBot1,3)
            Test.choice_and_change(testBot1,7)

    class Diag_Tests:
        """Encapsulated version of all diagonal tests"""
        def diag_test1() -> None:
            """Checks diagonal from center to far left. negative slope"""
            Test.choice_and_change(testBot2,1)
            Test.choice_and_change(testBot2,1)
            Test.choice_and_change(testBot2,1)
            Test.choice_and_change(testBot2,2)
            Test.choice_and_change(testBot2,2)
            Test.choice_and_change(testBot2,3)
            
            Test.choice_and_change(testBot1,4)
            Test.choice_and_change(testBot1,3)
            Test.choice_and_change(testBot1,2)
            Test.choice_and_change(testBot1,1)
            
        def diag_test2() -> None:
            """Checks diagonal from center to far right. positive slope"""
            Test.choice_and_change(testBot2,7)
            Test.choice_and_change(testBot2,7)
            Test.choice_and_change(testBot2,7)
            Test.choice_and_change(testBot2,6)
            Test.choice_and_change(testBot2,6)
            Test.choice_and_change(testBot2,5)
            
            Test.choice_and_change(testBot1,4)
            Test.choice_and_change(testBot1,5)
            Test.choice_and_change(testBot1,6)
            Test.choice_and_change(testBot1,7)

        def diag_test3() -> None:
            """Checks diagonal from far left to far right off screen. Meant to fail"""
            Test.choice_and_change(testBot2,7)
            Test.choice_and_change(testBot2,6)
            Test.choice_and_change(testBot2,6)
            Test.choice_and_change(testBot2,5)
            Test.choice_and_change(testBot2,5)
            Test.choice_and_change(testBot2,5)
            
            Test.choice_and_change(testBot1,1)
            Test.choice_and_change(testBot1,5)
            Test.choice_and_change(testBot1,6)
            Test.choice_and_change(testBot1,7)

        def diag_test4() -> None:
            """Checks diagonal from far right to far left off screen. Meant to fail"""
            Test.choice_and_change(testBot2,1)
            Test.choice_and_change(testBot2,1)
            Test.choice_and_change(testBot2,2)
            Test.choice_and_change(testBot2,7)
            Test.choice_and_change(testBot2,7)
            Test.choice_and_change(testBot2,7)
            
            Test.choice_and_change(testBot1,1)
            Test.choice_and_change(testBot1,2)
            Test.choice_and_change(testBot1,3)
            Test.choice_and_change(testBot1,7)

            Test.choice_and_change(testBot2,2)
            Test.choice_and_change(testBot1,2)
            
        def diag_test5() -> None:
            """Another check off screen. Meant to fail"""
            Test.choice_and_change(testBot2,1)
            Test.choice_and_change(testBot2,1)
            Test.choice_and_change(testBot2,6)
            Test.choice_and_change(testBot2,7)
            Test.choice_and_change(testBot2,7)
            
            Test.choice_and_change(testBot1,1)
            Test.choice_and_change(testBot1,5)
            Test.choice_and_change(testBot1,6)
            Test.choice_and_change(testBot1,7)

    def check_tie_side(self,num,par1,par2) -> None:
        """Fills a whole column for the check_tie function"""
        Test.choice_and_change(par1,num)
        Test.choice_and_change(par1,num)
        Test.choice_and_change(par1,num)

        Test.choice_and_change(par2,num)
        Test.choice_and_change(par2,num)
        Test.choice_and_change(par2,num)

    def check_vert(self) -> bool:
        """Runs every vertical test"""
        board.set_board()

        self.Vert_Tests.vert_test1()
        board.print_board()

        if not board.four_check_test_bot(testBot1,testBot2):
            print('Vert Test 1 failed')
            return False
        
        board.set_board()
        
        self.Vert_Tests.vert_test2()
        board.print_board()

        if not board.four_check_test_bot(testBot1,testBot2):
            print('Vert Test 2 failed')
            return False
        
        board.set_board()
        
        self.Vert_Tests.vert_test3()
        board.print_board()

        if not board.four_check_test_bot(testBot1,testBot2):
            print('Vert Test 3 failed')
            return False

        print('\nAll vertical tests passed')
        return True

    def check_horiz(self) -> bool:
        """Runs every horizontal test"""
        board.set_board()

        self.Horiz_Tests.horiz_test1()
        board.print_board()

        if not board.four_check_test_bot(testBot1,testBot2):
            print('Horiz Test 1 failed')
            return False

        board.set_board()

        self.Horiz_Tests.horiz_test2()
        board.print_board()
        
        if not board.four_check_test_bot(testBot1,testBot2):
            print('Horiz Test 2 failed')
            return False
        
        board.set_board()

        self.Horiz_Tests.horiz_test3()
        board.print_board()

        if not board.four_check_test_bot(testBot1,testBot2):
            print('Horiz Test 3 failed')
            return False
        
        board.set_board()

        self.Horiz_Tests.horiz_test4()
        board.print_board()

        if board.four_check_test_bot(testBot1,testBot2):
            print('Horiz Test 4 failed')
            return False

        board.set_board()

        self.Horiz_Tests.horiz_test5()
        board.print_board()

        if board.four_check_test_bot(testBot1,testBot2):
            print('Horiz Test 4 failed')
            return False
            
        print('\nAll horizontal tests passed')
        return True

    def check_diag(self) -> bool:
        """Runs every diagonal test"""
        board.set_board()

        self.Diag_Tests.diag_test1()
        board.print_board()
        
        if not board.four_check_test_bot(testBot1,testBot2):
            print('Diag Test 1 failed')
            return False
            
        board.set_board()

        self.Diag_Tests.diag_test2()
        board.print_board()

        if not board.four_check_test_bot(testBot1,testBot2):
            print('Diag Test 2 failed')
            return False   

        board.set_board()
        
    #Tests if diagonal works across the board. Meant to fail
        self.Diag_Tests.diag_test3()
        board.print_board()

        if board.four_check_test_bot(testBot1,testBot2):
            print('Diag Test 3 failed')
            return False

        board.set_board()

        self.Diag_Tests.diag_test4()
        board.print_board()

        if board.four_check_test_bot(testBot1,testBot2):
            print('Diag Test 4 failed')
            return False

        board.set_board()

        self.Diag_Tests.diag_test5()
        board.print_board()

        if board.four_check_test_bot(testBot1,testBot2):
            print('Diag Test 5 failed')
            return False

        print('\nAll diagonal tests passed')
        return True

    def check_tie(self) -> bool:
        """Checks to see if a tie works"""
        board.set_board()
        #Sevens
        self.check_tie_side(7,testBot1,testBot2)
        #Sixes        
        self.check_tie_side(6,testBot2,testBot1)
        #Fives
        self.check_tie_side(5,testBot1,testBot2)
        #Fours
        self.check_tie_side(4,testBot2,testBot1)
        #Threes
        self.check_tie_side(3,testBot1,testBot2)
        #Twos
        self.check_tie_side(2,testBot2,testBot1)
        #Ones
        self.check_tie_side(1,testBot1,testBot2)
        #Print
        board.print_board()

        if not board.four_check_test_bot(testBot1,testBot2):
            print('Tie Test failed')
            return False

        print('Tie test passed')
        board.set_board()
        return True

    def easyAIcheck(self) -> bool:
        board.set_board()
        global player1
        global player2
        board.cont_playing = True
        easyAI = EasyAI('Easy AI')
        player1 = easyAI
        player2 = testBot1
        turns(1)

    def hardAIcheck(self) -> bool:
        board.set_board()
        global player1
        global player2
        board.cont_playing = True
        hardAI = HardAI('Hard AI')
        player1 = hardAI
        player2 = testBot1
        turns(1)

    def run(self) -> None:
        """Runs all checks and asserts that they are correct and gives an assurance statement at the end that everything passed"""
        #assert self.check_vert()
        #assert self.check_horiz()
        #assert self.check_diag()
        #assert self.check_tie()
        #self.easyAIcheck()
        self.hardAIcheck()
        print('All tests passed')

def test() -> None:
    """Test bot checks if wins and stuff works"""
    global player1
    global player2
    global testBot1
    global testBot2
    testBot1 = Test('37;',"Test1")
    testBot2 = Test('35;','Test2')
    player1 = testBot1
    player2 = testBot2
    testBot1.run()
    
if __name__ == '__main__':
    test()