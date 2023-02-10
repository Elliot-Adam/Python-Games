import random
from Connect_4 import Board
from Connect_4 import Colors
from Connect_4 import colors
import math
import copy

class Player:
    """Basic logic for either a computer or human player"""
    def __init__(self,name) -> None:
        self.name = name
        self.score = 0
        self.color = self.color_getter()
        self.choice = None
        
    def scorepp(self) -> None:
        """Incrementing score"""
        self.score += 1

    def color_getter(self) -> str:
        """Color getter module gets the selected color to the attribute self.color"""
        while True:
            print('{}, pick a color'.format(self.name))
            for num,color in enumerate(Colors.color_list,start= 1):
                print('{}. {}'.format(num,color))
            color_inp = input('')
            if not color_inp in ['1','2','3','4']:
                print('Please use the number associated with the color')
                continue
            Colors.color_list.remove(Colors.color_list[int(color_inp) - 1])
            break
        #print('color {}'.format(colors(color_inp)))
        return colors(color_inp)
    
    def ai_color_getter(self) -> str:
        """Gets a color for the AI"""
        color_inp = random.choice(['1','2','3'])
        return colors(color_inp)

    def board_change(self) -> None:
        """Board_Change module takes the choice from the Player class and puts it into the Board class"""
        #Accounts for list syntax
        assert self.choice in [1,2,3,4,5,6,7]
        self.choice = self.choice_flipper(self.choice)
        self.choice -= 1
        while True:
            try:
                if not isinstance(BOARD.move_list[self.choice], int):
                    self.choice += 7
                else:
                    break
            except:
                print('Please input a legal move')
                self.choice_getter()
                self.board_change()
                break
        BOARD.move_list[self.choice] = '\x1b[{}{}O\x1b[0m'.format(self.color,BOARD.blackbg)

    def choice_flipper(self,num) -> int:
        """Flips choice so it can display neatly(e.g. 1 -> 7, 3 -> 4, etc.)"""
        return 8 - num         

    def choice_getter(self):
        pass

class HardAI(Player):
    #Used to find the best move 
    win_moves = []
    best_moves_dict = {}
    best_moves = []
    #Used to enact theoretical boards
    temp_board = []
    """Logic for the Hard AI. Uses an algorithm to find the best move"""
    def __init__(self,name) -> None:
        """Only change in overloaded init is that the ai color getter is called"""
        self.name = name
        self.score = 0
        self.color = self.ai_color_getter()
        self.choice = None


    def minimax(self,depth,isMaximizing:bool):
        if depth == 0 or self.recognize_win(self) or self.recognize_win(PLAYER1):
            return #Eval

        if isMaximizing:
            best_score = -1000
            moves = [move for move in self.temp_board.move_list if move >= 35 and isinstance(move,int)]
            for move in moves:
                og = self.temp_board.move_list[move][:]
                self.temp_board.move_list[move] = self.color
                score = self.minimax(depth - 1,False)
                best_score = max(score,best_score)
                self.temp_board.move_list[move] = og
            return best_score

        else:
            worst_score = 1000
            moves = [move for move in self.temp_board.move_list if move >= 35 and isinstance(move,int)]
            for move in moves:
                og = self.temp_board.move_list[move][:]
                self.temp_board.move_list[move] = self.color
                score = self.minimax(depth - 1,True)
                best_score = min(score,worst_score)
                self.temp_board.move_list[move] = og
            return worst_score

    def choice_getter(self):
        """Front end command to get the choice of the hard ai"""
        self.temp_board = copy.deepcopy(BOARD)
        if self.recognize_win(self) or self.recognize_win(PLAYER1):
            print('WIN/LOSS found')
            best_moveKV = (-100000,-1000000)
            #Finds greatest score
            for move,score in self.best_moves_dict.items():
                if score > best_moveKV[1]:
                    best_moveKV = (move,score)
                    print(best_moveKV)
            self.best_moves_dict.clear()
            self.win_moves.clear()
            self.choice = best_moveKV[0]
        else:
            self.choice = random.choice(BOARD.legal_moves())
            
    def weighted_randomizer(self,num,weight):
        """Created 4 randomized lists based on weights from params"""
        weight1 = weight
        weight2 = weight * 2
        weight3 = weight * 3
        weight4 = weight * 4
        if num == 4:
            return [weight1,weight2,weight3,weight4],[weight2,weight3,weight4,weight1],[weight3,weight4,weight1,weight2],[weight4,weight1,weight2,weight3]
        if num == 3:
            return [weight1,weight2,weight3],[weight2,weight3,weight1],[weight3,weight1,weight2]
    
    def win_rows(self,color):
        for row in range(6):
            for count in range(4):
                for num1,num2,num3,num4 in self.weighted_randomizer(4,1):
                    row_count = row * 7
                    value = row_count + count 
                    if math.floor((value + num1)/7) == math.floor((value + num2)/7) == math.floor((value + num3)/7) == math.floor((value + num4)/7):
                        if not BOARD.move_list[value] == BOARD.move_list[value + num1] == BOARD.move_list[value + num2]:
                            continue
                        if not color in repr(BOARD.move_list[value]):
                            print(False,'Dif color')
                            continue
                        if not isinstance(BOARD.move_list[value + num3],int):
                            print(False,'Closed')
                            continue
                        print(True,'row')
                        self.win_moves.append(BOARD.move_list[value + num3])
   
    def win_columns(self,color):
        for column in range(7):
            for count in range(3):
                column_count = count * 7
                value = column_count + column
                for num1,num2,num3 in self.weighted_randomizer(3,7):
                    if (value) % 7 == (value) % 7 == (value + num1) % 7 == (value + num2) % 7:
                        if not BOARD.move_list[value] == BOARD.move_list[value + num1] == BOARD.move_list[value + num2]:
                            continue
                        if not color in repr(BOARD.move_list[value]):
                            continue
                        if not isinstance(BOARD.move_list[value + num3],int):
                            continue
                        self.win_moves.append(BOARD.move_list[value + num3])
   
    def win_diagonals(self,color):
        for spots,value in enumerate(BOARD.move_list):
            for num1, num2, num3 in self.weighted_randomizer(3,8):
                try:
                    #Registers all negative slope diagonal combinations
                    if math.floor(spots/7) != math.floor((spots + num1) / 7 ) != math.floor((spots + num2) / 7) != math.floor((spots + num3) / 7):
                        if not BOARD.move_list[value] == BOARD.move_list[value + num1] == BOARD.move_list[value + num2]:
                            continue
                        if not color in repr(BOARD.move_list[value]):
                            continue
                        if not isinstance(BOARD.move_list[value + num3],int):
                            continue
                        self.win_moves.append(BOARD.move_list[value + num3])
                except:
                    pass
                
            for num1,num2,num3 in self.weighted_randomizer(3,6):
                try:
                    #Registers all positive slope diagonal combinations
                    if math.floor(spots/7) != math.floor((spots + num1) / 7 ) != math.floor((spots + num2) / 7) != math.floor((spots + num3) / 7):
                        if not BOARD.move_list[value] == BOARD.move_list[value + num1] == BOARD.move_list[value + num2]:
                            continue
                        if not color in repr(BOARD.move_list[value]):
                            continue
                        if not isinstance(BOARD.move_list[value + num3],int):
                            continue
                        self.win_moves.append(BOARD.move_list[value + num3])
   
                except:
                    pass
         
    def recognize_win(self,playerObj:Player) -> bool:
        self.win_rows(playerObj.color)
        self.win_columns(playerObj.color)
        self.win_diagonals(playerObj.color)
        if len(self.win_moves) != 0:
            for index,move in enumerate(self.win_moves):
                #Turns raw move into playable move
                print('Moves', move, move%7)
                if (move % 7) == 0:
                    self.win_moves[index] = 1
                else:
                    self.win_moves[index] = self.choice_flipper(move % 7)
                print('After in reco',self.win_moves[index])
                pass                

            for winning_move in self.win_moves:
                #Assigns score to moves
                if isinstance(playerObj,HardAI):
                    self.best_moves_dict[winning_move] = 100
                else:
                    self.best_moves_dict[winning_move] = -100
            return True
        return False

def turns(firstP) -> None:
    """The turns between players game. Reused code from Tic Tac Toe"""
    t = firstP
    if t == 1:
        nextP = 2
    else:
        nextP = 1
    while BOARD.cont_playing:
        if t == 1:
            PLAYER1.choice_getter()
            PLAYER1.board_change()
            status = BOARD.four_check_front(PLAYER1,PLAYER2)
            t = 2
            if status:
            #if someone won, restart the game with PLAYER2 going first
                t = nextP
                nextP = 1
                continue
        if t == 2:
            PLAYER2.choice_getter()
            PLAYER2.board_change()
            status = BOARD.four_check_front(PLAYER1,PLAYER2)
            if status:
            #if someone won, restart the game with PLAYER2 going first
                t = nextP
                nextP = 2
            else:
                t = 1

class Test(Player):
    """Test bot for test mode. dif 4"""
    def __init__ (self,color,name= 'Testbot') -> None:
        self.color = color
        self.name = name
        self.score = 0
        self.choice = None
        
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

    def choice_getter(self) -> None:
        """Test bot chooses a random legal move from the BOARD"""
        self.choice = random.choice(BOARD.legal_moves())
    
    def choice_and_change(bot ,num : int):
        bot.choice = num
        bot.board_change()

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

        BOARD.set_board()

        self.Diag_Tests.diag_test4()
        BOARD.print_board()

        if BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Diag Test 4 failed')
            return False

        BOARD.set_board()

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

    def hard_ai_check(self) -> bool:
        global PLAYER2
        PLAYER2 = HardAI('Hard Computer')
        turns(1)
        if not BOARD.four_check_test_bot(TESTBOT1,TESTBOT2):
            print('Hard AI check failed')
            return False

        print('Hard AI test passed')
        BOARD.set_board()
        return True


    def run(self) -> None:
        """Runs all checks and asserts that they are correct and gives an assurance statement at the end that everything passed"""
        #assert self.check_vert()
        #assert self.check_horiz()
        #assert self.check_diag()
        #assert self.check_tie()
        assert self.hard_ai_check()
        print('All tests passed')

def test() -> None:
    """Test bot checks if wins and stuff work"""
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
    global BOARD 
    BOARD = Board()
    test()