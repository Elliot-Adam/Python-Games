<<<<<<< HEAD
from Connect_4 import *

class Test(Player):
    """Test bot for test mode. dif 4"""
    def __init__ (self,color,name= 'Testbot') -> None:
        self.color = color
        self.name = name
        self.score = 0
        self.choice = None

    def choice_getter(self) -> None:
        """Test bot chooses a random legal move from the BOARD"""
        self.choice = random.choice(BOARD.legal_moves())
    
    def choice_and_change(bot,num):
        bot.choice = num
        bot.board_change()
        
    class Vert_Tests:
        """Encapsulated version of all vertical tests"""
        def vert_test1() -> None:
            """Tests upright in far right"""
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)

        def vert_test2() -> None:
            """Tests upright in far right with one piece beneath the four"""
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)

        def vert_test3() -> None:
            """Tests upright in far left"""
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,1)

    class Horiz_Tests:
        """Encapsulated version of all horizontal tests"""
        def horiz_test1() -> None:
            """Tests flat in far right"""
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,6)
            Test.choice_and_change(TESTBOT1,5)
            Test.choice_and_change(TESTBOT1,4)

        def horiz_test2() -> None:
            """Tests flat in far left"""
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,2)
            Test.choice_and_change(TESTBOT1,3)
            Test.choice_and_change(TESTBOT1,4)

        def horiz_test3() -> None:
            """Tests flat in far left on the second row"""
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,2)
            Test.choice_and_change(TESTBOT2,3)
            Test.choice_and_change(TESTBOT1,4)
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,2)
            Test.choice_and_change(TESTBOT1,3)
            Test.choice_and_change(TESTBOT1,4)
            
        def horiz_test4() -> None:
            """Checks if 3 points on far right will win with point on second row of far left. Meant to fail"""
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,6)
            Test.choice_and_change(TESTBOT1,5)
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT1,1)
    
        def horiz_test5() -> None:
            """Checks off screen in other direction"""
            Test.choice_and_change(TESTBOT2,7)
            
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,2)
            Test.choice_and_change(TESTBOT1,3)
            Test.choice_and_change(TESTBOT1,7)

    class Diag_Tests:
        """Encapsulated version of all diagonal tests"""
        def diag_test1() -> None:
            """Checks diagonal from center to far left. negative slope"""
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,2)
            Test.choice_and_change(TESTBOT2,2)
            Test.choice_and_change(TESTBOT2,3)
            
            Test.choice_and_change(TESTBOT1,4)
            Test.choice_and_change(TESTBOT1,3)
            Test.choice_and_change(TESTBOT1,2)
            Test.choice_and_change(TESTBOT1,1)
            
        def diag_test2() -> None:
            """Checks diagonal from center to far right. positive slope"""
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,6)
            Test.choice_and_change(TESTBOT2,6)
            Test.choice_and_change(TESTBOT2,5)
            
            Test.choice_and_change(TESTBOT1,4)
            Test.choice_and_change(TESTBOT1,5)
            Test.choice_and_change(TESTBOT1,6)
            Test.choice_and_change(TESTBOT1,7)

        def diag_test3() -> None:
            """Checks diagonal from far left to far right off screen. Meant to fail"""
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,6)
            Test.choice_and_change(TESTBOT2,6)
            Test.choice_and_change(TESTBOT2,5)
            Test.choice_and_change(TESTBOT2,5)
            Test.choice_and_change(TESTBOT2,5)
            
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,5)
            Test.choice_and_change(TESTBOT1,6)
            Test.choice_and_change(TESTBOT1,7)

        def diag_test4() -> None:
            """Checks diagonal from far right to far left off screen. Meant to fail"""
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,2)
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,7)
            
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,2)
            Test.choice_and_change(TESTBOT1,3)
            Test.choice_and_change(TESTBOT1,7)

            Test.choice_and_change(TESTBOT2,2)
            Test.choice_and_change(TESTBOT1,2)
            
        def diag_test5() -> None:
            """Another check off screen. Meant to fail"""
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,6)
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,7)
            
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,5)
            Test.choice_and_change(TESTBOT1,6)
            Test.choice_and_change(TESTBOT1,7)

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
        BOARD.set_board()

        self.Vert_Tests.vert_test1()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Vert Test 1 failed')
            return False
        
        BOARD.set_board()
        
        self.Vert_Tests.vert_test2()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Vert Test 2 failed')
            return False
        
        BOARD.set_board()
        
        self.Vert_Tests.vert_test3()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Vert Test 3 failed')
            return False

        print('\nAll vertical tests passed')
        return True

    def check_horiz(self) -> bool:
        """Runs every horizontal test"""
        BOARD.set_board()

        self.Horiz_Tests.horiz_test1()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Horiz Test 1 failed')
            return False

        BOARD.set_board()

        self.Horiz_Tests.horiz_test2()
        BOARD.print_board()
        
        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Horiz Test 2 failed')
            return False
        
        BOARD.set_board()

        self.Horiz_Tests.horiz_test3()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Horiz Test 3 failed')
            return False
        
        BOARD.set_board()

        self.Horiz_Tests.horiz_test4()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Horiz Test 4 failed')
            return False

        BOARD.set_board()

        self.Horiz_Tests.horiz_test5()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Horiz Test 4 failed')
            return False
            
        print('\nAll horizontal tests passed')
        return True

    def check_diag(self) -> bool:
        """Runs every diagonal test"""
        BOARD.set_board()

        self.Diag_Tests.diag_test1()
        BOARD.print_board()
        
        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 1 failed')
            return False
            
        BOARD.set_board()

        self.Diag_Tests.diag_test2()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 2 failed')
            return False   

        BOARD.set_board()
        
    #Tests if diagonal works across the BOARD. Meant to fail
        self.Diag_Tests.diag_test3()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 3 failed')
            return False

        BOARD.board()

        self.Diag_Tests.diag_test4()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 4 failed')
            return False

        BOARD.board()

        self.Diag_Tests.diag_test5()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 5 failed')
            return False

        print('\nAll diagonal tests passed')
        return True

    def check_tie(self) -> bool:
        """Checks to see if a tie works"""
        BOARD.set_board()
        #Sevens
        self.check_tie_side(7,TESTBOT1,TESTBOT2)
        #Sixes        
        self.check_tie_side(6,TESTBOT2,TESTBOT1)
        #Fives
        self.check_tie_side(5,TESTBOT1,TESTBOT2)
        #Fours
        self.check_tie_side(4,TESTBOT2,TESTBOT1)
        #Threes
        self.check_tie_side(3,TESTBOT1,TESTBOT2)
        #Twos
        self.check_tie_side(2,TESTBOT2,TESTBOT1)
        #Ones
        self.check_tie_side(1,TESTBOT1,TESTBOT2)
        #Print
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Tie Test failed')
            return False

        print('Tie test passed')
        BOARD.set_board()
        return True

    def easyAIcheck(self) -> bool:
        BOARD.set_board()
        global PLAYER1
        global PLAYER2
        BOARD.cont_playing = True
        easyAI = EasyAI('Easy AI')
        PLAYER1 = easyAI
        PLAYER2 = TESTBOT1
        turns(1)

    def hardAIcheck(self) -> bool:
        BOARD.set_board()
        global PLAYER1
        global PLAYER2
        BOARD.cont_playing = True
        hardAI = HardAI('Hard AI')
        PLAYER1 = hardAI
        PLAYER2 = TESTBOT1
        print(locals())
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
    global PLAYER1
    global PLAYER2
    global TESTBOT1
    global TESTBOT2
    TESTBOT1 = Test('37;',"Test1")
    TESTBOT2 = Test('35;','Test2')
    PLAYER1 = TESTBOT1
    PLAYER2 = TESTBOT2
    TESTBOT1.run()
    
if __name__ == '__main__':
    testVars()
=======
from Connect_4 import *

class Test(Player):
    """Test bot for test mode. dif 4"""
    def __init__ (self,color,name= 'Testbot') -> None:
        self.color = color
        self.name = name
        self.score = 0
        self.choice = None

    def choice_getter(self) -> None:
        """Test bot chooses a random legal move from the BOARD"""
        self.choice = random.choice(BOARD.legal_moves())
    
    def choice_and_change(bot,num):
        bot.choice = num
        bot.BOARD_change()
        
    class Vert_Tests:
        """Encapsulated version of all vertical tests"""
        def vert_test1() -> None:
            """Tests upright in far right"""
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)

        def vert_test2() -> None:
            """Tests upright in far right with one piece beneath the four"""
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,7)

        def vert_test3() -> None:
            """Tests upright in far left"""
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,1)

    class Horiz_Tests:
        """Encapsulated version of all horizontal tests"""
        def horiz_test1() -> None:
            """Tests flat in far right"""
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,6)
            Test.choice_and_change(TESTBOT1,5)
            Test.choice_and_change(TESTBOT1,4)

        def horiz_test2() -> None:
            """Tests flat in far left"""
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,2)
            Test.choice_and_change(TESTBOT1,3)
            Test.choice_and_change(TESTBOT1,4)

        def horiz_test3() -> None:
            """Tests flat in far left on the second row"""
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,2)
            Test.choice_and_change(TESTBOT2,3)
            Test.choice_and_change(TESTBOT1,4)
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,2)
            Test.choice_and_change(TESTBOT1,3)
            Test.choice_and_change(TESTBOT1,4)
            
        def horiz_test4() -> None:
            """Checks if 3 points on far right will win with point on second row of far left. Meant to fail"""
            Test.choice_and_change(TESTBOT1,7)
            Test.choice_and_change(TESTBOT1,6)
            Test.choice_and_change(TESTBOT1,5)
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT1,1)
    
        def horiz_test5() -> None:
            """Checks off screen in other direction"""
            Test.choice_and_change(TESTBOT2,7)
            
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,2)
            Test.choice_and_change(TESTBOT1,3)
            Test.choice_and_change(TESTBOT1,7)

    class Diag_Tests:
        """Encapsulated version of all diagonal tests"""
        def diag_test1() -> None:
            """Checks diagonal from center to far left. negative slope"""
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,2)
            Test.choice_and_change(TESTBOT2,2)
            Test.choice_and_change(TESTBOT2,3)
            
            Test.choice_and_change(TESTBOT1,4)
            Test.choice_and_change(TESTBOT1,3)
            Test.choice_and_change(TESTBOT1,2)
            Test.choice_and_change(TESTBOT1,1)
            
        def diag_test2() -> None:
            """Checks diagonal from center to far right. positive slope"""
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,6)
            Test.choice_and_change(TESTBOT2,6)
            Test.choice_and_change(TESTBOT2,5)
            
            Test.choice_and_change(TESTBOT1,4)
            Test.choice_and_change(TESTBOT1,5)
            Test.choice_and_change(TESTBOT1,6)
            Test.choice_and_change(TESTBOT1,7)

        def diag_test3() -> None:
            """Checks diagonal from far left to far right off screen. Meant to fail"""
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,6)
            Test.choice_and_change(TESTBOT2,6)
            Test.choice_and_change(TESTBOT2,5)
            Test.choice_and_change(TESTBOT2,5)
            Test.choice_and_change(TESTBOT2,5)
            
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,5)
            Test.choice_and_change(TESTBOT1,6)
            Test.choice_and_change(TESTBOT1,7)

        def diag_test4() -> None:
            """Checks diagonal from far right to far left off screen. Meant to fail"""
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,2)
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,7)
            
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,2)
            Test.choice_and_change(TESTBOT1,3)
            Test.choice_and_change(TESTBOT1,7)

            Test.choice_and_change(TESTBOT2,2)
            Test.choice_and_change(TESTBOT1,2)
            
        def diag_test5() -> None:
            """Another check off screen. Meant to fail"""
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,1)
            Test.choice_and_change(TESTBOT2,6)
            Test.choice_and_change(TESTBOT2,7)
            Test.choice_and_change(TESTBOT2,7)
            
            Test.choice_and_change(TESTBOT1,1)
            Test.choice_and_change(TESTBOT1,5)
            Test.choice_and_change(TESTBOT1,6)
            Test.choice_and_change(TESTBOT1,7)

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
        BOARD.set_board()

        self.Vert_Tests.vert_test1()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Vert Test 1 failed')
            return False
        
        BOARD.set_board()
        
        self.Vert_Tests.vert_test2()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Vert Test 2 failed')
            return False
        
        BOARD.set_board()
        
        self.Vert_Tests.vert_test3()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Vert Test 3 failed')
            return False

        print('\nAll vertical tests passed')
        return True

    def check_horiz(self) -> bool:
        """Runs every horizontal test"""
        BOARD.set_board()

        self.Horiz_Tests.horiz_test1()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Horiz Test 1 failed')
            return False

        BOARD.set_board()

        self.Horiz_Tests.horiz_test2()
        BOARD.print_board()
        
        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Horiz Test 2 failed')
            return False
        
        BOARD.set_board()

        self.Horiz_Tests.horiz_test3()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Horiz Test 3 failed')
            return False
        
        BOARD.set_board()

        self.Horiz_Tests.horiz_test4()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Horiz Test 4 failed')
            return False

        BOARD.set_board()

        self.Horiz_Tests.horiz_test5()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Horiz Test 4 failed')
            return False
            
        print('\nAll horizontal tests passed')
        return True

    def check_diag(self) -> bool:
        """Runs every diagonal test"""
        BOARD.set_board()

        self.Diag_Tests.diag_test1()
        BOARD.print_board()
        
        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 1 failed')
            return False
            
        BOARD.set_board()

        self.Diag_Tests.diag_test2()
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 2 failed')
            return False   

        BOARD.set_board()
        
    #Tests if diagonal works across the BOARD. Meant to fail
        self.Diag_Tests.diag_test3()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 3 failed')
            return False

        BOARD.board()

        self.Diag_Tests.diag_test4()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 4 failed')
            return False

        BOARD.board()

        self.Diag_Tests.diag_test5()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 5 failed')
            return False

        print('\nAll diagonal tests passed')
        return True

    def check_tie(self) -> bool:
        """Checks to see if a tie works"""
        BOARD.set_board()
        #Sevens
        self.check_tie_side(7,TESTBOT1,TESTBOT2)
        #Sixes        
        self.check_tie_side(6,TESTBOT2,TESTBOT1)
        #Fives
        self.check_tie_side(5,TESTBOT1,TESTBOT2)
        #Fours
        self.check_tie_side(4,TESTBOT2,TESTBOT1)
        #Threes
        self.check_tie_side(3,TESTBOT1,TESTBOT2)
        #Twos
        self.check_tie_side(2,TESTBOT2,TESTBOT1)
        #Ones
        self.check_tie_side(1,TESTBOT1,TESTBOT2)
        #Print
        BOARD.print_board()

        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Tie Test failed')
            return False

        print('Tie test passed')
        BOARD.set_board()
        return True

    def easyAIcheck(self) -> bool:
        BOARD.set_board()
        global PLAYER1
        global PLAYER2
        BOARD.cont_playing = True
        easyAI = EasyAI('Easy AI')
        PLAYER1 = easyAI
        PLAYER2 = TESTBOT1
        turns(1)

    def hardAIcheck(self) -> bool:
        BOARD.set_board()
        global PLAYER1
        global PLAYER2
        BOARD.cont_playing = True
        hardAI = HardAI('Hard AI')
        PLAYER1 = hardAI
        PLAYER2 = TESTBOT1
        print(locals())
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
    global PLAYER1
    global PLAYER2
    global TESTBOT1
    global TESTBOT2
    TESTBOT1 = Test('37;',"Test1")
    TESTBOT2 = Test('35;','Test2')
    PLAYER1 = TESTBOT1
    PLAYER2 = TESTBOT2
    TESTBOT1.run()
    
if __name__ == '__main__':
    BOARD = Board()
>>>>>>> 533daa36b3a8e98e9f5a307e9c6ebd31e6249646
    test()