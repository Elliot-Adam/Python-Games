<<<<<<< HEAD
#Connect 4
import random
import math
import copy
#Classes
class Colors:
    color_dict = {'1':'31;','2':'34;','3':'32;','4':'33;'}
    color_og_list = ['31;','34;','32;','33;']
    color_list = ['Red','Blue','Green','Yellow']

class Board:
    """Board class includes modules such as printing the BOARD, setting the BOARD, and checking for wins"""
    def __init__(self) -> None:
        self.cont_playing = True
        self.move_list = []
        self.downward_arrow = '\u2193'
        self.blackbg = '40m'
        self.bold = '1;'
        self.set_board()
        
    def set_board(self) -> None:
        """Resetting the BOARD at the beginning of the game and after a win"""
        self.move_list.clear()
        count = 1
        for row in range(6):
            for column in range(7):
                self.move_list.append(count)
                count += 1

    def print_board(self) -> None:
        """The module to print the BOARD to the terminal so the user can see the remaining spots"""
            #Print the numbers and arrows above the BOARD
        print('\n')
        print('  ',end='')
        for num in list(range(1,7)):
            print(num,end= '    ')
        print(7)
        print('  ',end='')
        for _ in range(7):
            print(self.downward_arrow,end= '    ')
            #Actually prints the BOARD while excluding the open spaces
        print()
        row_count = 0    
        for spot in self.move_list[::-1]:
            if isinstance(spot,int):
                choice = ' '
            else:
                choice = spot
            print('| {} |'.format(choice),end='')
            row_count += 1
            if row_count == 7:
                print()
                row_count = 0

    def four_check_test_bot(self,p1,p2) -> bool:
        """Four check that runs during test mode so I dont have to do fulfill inputs while checking tests"""
        global winning_numbers
        winning_numbers = []
        (win1,win2) = (self.four_check_back(p1.color),self.four_check_back(p2.color))
        output:bool = False
        tie:bool = len(self.chosen_check()) == 0
        final_winning_nums_list = []
        for num_list in winning_numbers:
                for num in num_list:
                    self.move_list[num] = '\x1B[{}{}\x1B[0m'.format(self.bold,self.move_list[num].replace('\x1b[',"",1))
                    final_winning_nums_list.append(self.move_list[num])
        if win1 or win2:
            output = True
        if tie:
            output = True
        return output

    def four_check_front(self,p1,p2) -> bool:
        """four check front is the module that handles what happens if there is a win or not. There will be some related modules after"""
        global winning_numbers
        winning_numbers = []
        win1,win2 = self.four_check_back(p1.color),self.four_check_back(p2.color)
        output:bool = False
        tie:bool = len(self.chosen_check()) == 0
        final_winning_nums_list = []
        for num_list in winning_numbers:
                for num in num_list:
                    self.move_list[num] = '\x1B[{}{}\x1B[0m'.format(self.bold,self.move_list[num].replace('\x1b[',"",1))
                    final_winning_nums_list.append(self.move_list[num])
        if win1:
            self.four_check_win_side(p1)
            output = True
        if win2:
            self.four_check_win_side(p2)
            output = True
        if tie:
            self.four_check_tie_side()
            output = True

        return output

    def four_check_back(self,color) -> bool:
        """four check back is the module used to find a win"""
        #Registers all row combinations
        val = False
        for row in range(6):
            for count in range(4):
                row_count = row * 7
                #print('Four Row Check',self.move_list[count + row_count] , self.move_list[count + 1 + row_count] , self.move_list[count + 2 + row_count] , self.move_list[count + 3 + row_count],'row',int(row_count/7 + 1))
                if self.move_list[count + row_count] == self.move_list[count + 1 + row_count] == self.move_list[count + 2 + row_count] == self.move_list[count + 3 + row_count]:
                    if color in self.move_list[count + row_count]:
                        winning_numbers.append([count + row_count , count + 1 + row_count , count + 2 + row_count , count + 3 + row_count])
                        val = True
        #Registers all column combinations
        for column in range(7):
            for count in range(3):
                column_count = count * 7
                if self.move_list[column_count + column] == self.move_list[column_count + 7 + column] == self.move_list[column_count + 14 + column] == self.move_list[column_count + 21 + column]:
                    if color in self.move_list[column + column_count]:
                        winning_numbers.append([column_count + column , column_count + 7 + column , column_count + 14 + column , column_count + 21 + column])
                        val = True
        #Registers all diagonal combinations
        for spots,value in enumerate(self.move_list):
            try:
                #Registers all negative slope diagonal combinations
                if math.floor(spots/7) != math.floor((spots + 8) / 7 ) != math.floor((spots + 16) / 7) != math.floor((spots + 24) / 7):
                    if self.move_list[spots] == self.move_list[spots + 8] == self.move_list[spots + 16] == self.move_list[spots + 24]:
                        print('Values',color)
                        print((value == self.move_list[spots + 8] == self.move_list[spots + 16] == self.move_list[spots + 24]),value , self.move_list[spots + 8] , self.move_list[spots + 16] , self.move_list[spots + 24])
                        print(repr(value))
                        if color in repr(value):
                            print('Winning for color')
                            winning_numbers.append([spots, spots + 8, spots + 16, spots + 24])
                            val = True
                #Registers all positive slope diagonal combinations
                if math.floor(spots/7) != math.floor((spots + 6) / 7 ) != math.floor((spots + 12) / 7) != math.floor((spots + 18) / 7):
                    if value == self.move_list[spots + 6] == self.move_list[spots + 12] == self.move_list[spots + 18]:
                        if color in repr(value):
                            winning_numbers.append([spots, spots + 6, spots + 12, spots + 18])
                            val = True
            except:
                pass
            
            
        if val:
            print('Win')
            return True
        return False
    
    def four_check_win_side(self,player) -> None:
        """Code that runs if there is a win"""
        self.print_board()
        self.set_board()
        print('{} connected 4'.format(player.name))
        player.scorepp()
        self.score_print()
        self.cont_prompt()

    def four_check_tie_side(self) -> None:
        """Code that runs if there is a tie"""
        self.print_BOARD()
        self.set_BOARD()
        print('\nTie Game')
        self.score_print()
        self.cont_prompt()

    def chosen_check(self) -> list:
        """Test for chosen spots on the BOARD. Returns list of unchosen spaces"""
        templist = []
        for spot in self.move_list:
            if isinstance(spot,int):
                templist.append(spot)
        return templist

    def cont_prompt(self) -> None:
        """Asks if the plyer wants to continue playing after a game"""
        while True:
            cont_inp = input('Continue Playing?\n')
            if cont_inp == 'Yes' or cont_inp == 'yes':
                break
            elif cont_inp == 'No' or cont_inp == 'no':
                self.cont_playing = False
                break
            else:
                print('Please input yes, or no\n')

    def score_print(self) -> None:
        """Prints both players score as well as their names next to it"""
        print('{}\'s Score: {}, {}\'s Score: {}'.format(PLAYER1.name,PLAYER1.score,PLAYER2.name,PLAYER2.score))

    def legal_moves(self) -> list[int]:
        legal_moves_list = [1,2,3,4,5,6,7]
        if not isinstance(self.move_list[41],int):
            legal_moves_list.remove(7)
        if not isinstance(self.move_list[40],int):
            legal_moves_list.remove(6)
        if not isinstance(self.move_list[39],int):
            legal_moves_list.remove(5)
        if not isinstance(self.move_list[38],int):
            legal_moves_list.remove(4)
        if not isinstance(self.move_list[37],int):
            legal_moves_list.remove(3)
        if not isinstance(self.move_list[36],int):
            legal_moves_list.remove(2)
        if not isinstance(self.move_list[35],int):
            legal_moves_list.remove(1)
        return legal_moves_list

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
        self.choice = self.choice_flipper(self.choice)
        print('After',self.choice)
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
        BOARD.move_list[self.choice] = '\x1b[{}{}O\x1b[0m'.format(self.color,BOARD.blackbg)

    def choice_flipper(self,num) -> int:
        """Flips choice so it can display neatly(e.g. 1 -> 7, 3 -> 4, etc.)"""
        print('b4',num)
        match num:
            case 1:
                return 7
            case 2:
                return 6
            case 3:
                return 5
            case 4:
                return 4
            case 5:
                return 3
            case 6:
                return 2
            case 7:
                return 1            

class Person(Player):
    """Logic for the human player. Only difference is how they get their move"""
    def choice_getter(self) -> None:
        """Gets choice for human player"""
        while True:
            BOARD.print_board()
            self.choice = input('\n\n{}, Choose a spot\n'.format(self.name))
            if self.choice == 'quit' or self.choice == 'Quit':
                print ('Quitting...')
                quit()
            try:
                self.choice = int(self.choice)
            except:
                print('\nGive a viable location\n\n')
                continue
            if int(self.choice) not in [1,2,3,4,5,6,7]:
                print('\nGive a viable location\n\n')
                continue
            break

class EasyAI(Player):
    """Logic for the Easy AI. Completely random"""
    def __init__(self,name) -> None:
        """Only change in overloaded init is that the ai color getter is called"""
        self.name = name
        self.score = 0
        self.color = self.ai_color_getter()
        self.choice = None
        

    def choice_getter(self) -> None:
        """Easy AI chooses a random legal move from the BOARD"""
        self.choice = random.choice(BOARD.legal_moves())

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

#Functions

def colors(color) -> str:
    """Turns player choice into unicode for the Player object to turn the O into the specified color"""
    ret_value = Colors.color_dict[color]

    Colors.color_og_list.remove(Colors.color_dict[color])
    Colors.color_dict.clear()
    for key,value in enumerate(Colors.color_og_list,start= 1):
        Colors.color_dict[str(key)] = value
    return ret_value

def startup() -> int:
    """Gets the mode/difficulty user input. Reused code from Tic Tac Toe"""
    while True:
        try:
            dif = int(input('Modes\n1.Player vs Player\n2.Player vs Easy AI\n3.Player vs Hard AI\n'))
        except:
            print('\nPlease input 1, 2, or 3')
            continue
        if dif not in [1,2,3]:
            print('Please input a 1, 2, or 3')
            continue
        return dif

def starterRequest() -> int:
    """Gets who the player wants to start"""
    while True:
        starter = input('Who goes first\n1.Player\n2.AI\n3.Random\n')
        try:
            starter = int(starter)
        except:
            print('Please input 1, 2, or 3')
        if starter not in [1,2,3]:
            print('Please input 1, 2, or 3')
            continue
        break
    return starter

def name_getter(num) -> str:
    """Gets name for Person object. Reused code from Tic Tac Toe"""
    while True:
        name = input('Player {}, input your name. '.format(num))
        if len(name) < 1:
            print('Insert a name please')
            continue
        break
    return name

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

#Level Functions
def game_modes() -> None:
    """Runs different mode level functions"""
    dif = startup()
    match int(dif):
        case 1:
            player_VS_player()
        case 2:
            player_VS_ezai()
        case 3:
            player_VS_hardai()

def player_VS_player() -> None:
    """Player vs player code. Dif 1"""
    global PLAYER1
    global PLAYER2
    p1name = name_getter('1')
    p2name = name_getter('2')
    PLAYER1 = Person(p1name)
    PLAYER2 = Person(p2name)
    turns(1)

def player_VS_ezai() -> None:
    """Player vs an easy/random AI. Dif 2"""
    global PLAYER1
    global PLAYER2
    p1name = name_getter('1')
    p2name = 'Easy Computer'
    PLAYER1 = Person(p1name)
    PLAYER2 = EasyAI(p2name)
    starter = starterRequest()
    #Randomnly making variable starter 1 or 2 if the user chose random
    if starter == 3:
        starter = random.choice([1,2])
    if starter == 1:
        pfirst = 1
    if starter == 2:
        pfirst = 2
    turns(pfirst)

def player_VS_hardai() -> None:
    """Player vs Hard/Smart AI. Dif 3"""
    global PLAYER1
    global PLAYER2
    p1name = name_getter('1')
    p2name = 'Hard Computer'
    PLAYER1 = Person(p1name)
    PLAYER2 = HardAI(p2name)
    starter = starterRequest()
    #Randomnly making variable starter 1 or 2 if the user chose random
    if starter == 3:
        starter = random.choice([1,2])
    if starter == 1:
        pfirst = 1
    if starter == 2:
        pfirst = 2
    turns(pfirst)

def testVars():
    global BOARD 
    BOARD = Board()
#Main Game Code




if __name__ == '__main__':
    global BOARD 
    BOARD = Board()
    game_modes()

=======
#Connect 4
import random
import math
#Classes
class Colors:
    color_dict = {'1':'31;','2':'34;','3':'32;','4':'33;'}
    color_og_list = ['31;','34;','32;','33;']
    color_list = ['Red','Blue','Green','Yellow']

class Board:
    """Board class includes modules such as printing the BOARD, setting the BOARD, and checking for wins"""
    def __init__(self) -> None:
        self.cont_playing = True
        self.move_list = []
        self.downward_arrow = '\u2193'
        self.blackbg = '40m'
        self.bold = '1;'
        self.set_board()
        
    def set_board(self) -> None:
        """Resetting the BOARD at the beginning of the game and after a win"""
        self.move_list.clear()
        count = 1
        for row in range(6):
            for column in range(7):
                self.move_list.append(count)
                count += 1

    def print_board(self) -> None:
        """The module to print the BOARD to the terminal so the user can see the remaining spots"""
            #Print the numbers and arrows above the BOARD
        print('\n')
        print('  ',end='')
        for num in list(range(1,7)):
            print(num,end= '    ')
        print(7)
        print('  ',end='')
        for _ in range(7):
            print(self.downward_arrow,end= '    ')
            #Actually prints the BOARD while excluding the open spaces
        print()
        row_count = 0    
        for spot in self.move_list[::-1]:
            if isinstance(spot,int):
                choice = ' '
            else:
                choice = spot
            print('| {} |'.format(choice),end='')
            row_count += 1
            if row_count == 7:
                print()
                row_count = 0

    def four_check_test_bot(self,p1,p2) -> bool:
        """Four check that runs during test mode so I dont have to do fulfill inputs while checking tests"""
        global winning_numbers
        winning_numbers = []
        (win1,win2) = (self.four_check_back(p1.color),self.four_check_back(p2.color))
        output:bool = False
        tie:bool = len(self.chosen_check()) == 0
        final_winning_nums_list = []
        for num_list in winning_numbers:
                for num in num_list:
                    self.move_list[num] = '\x1B[{}{}\x1B[0m'.format(self.bold,self.move_list[num].replace('\x1b[',"",1))
                    final_winning_nums_list.append(self.move_list[num])
        if win1 or win2:
            output = True
        if tie:
            output = True
        return output

    def four_check_front(self,p1,p2) -> bool:
        """four check front is the module that handles what happens if there is a win or not. There will be some related modules after"""
        global winning_numbers
        winning_numbers = []
        win1,win2 = self.four_check_back(p1.color),self.four_check_back(p2.color)
        output:bool = False
        tie:bool = len(self.chosen_check()) == 0
        final_winning_nums_list = []
        for num_list in winning_numbers:
                for num in num_list:
                    self.move_list[num] = '\x1B[{}{}\x1B[0m'.format(self.bold,self.move_list[num].replace('\x1b[',"",1))
                    final_winning_nums_list.append(self.move_list[num])
        if win1:
            self.four_check_win_side(p1)
            output = True
        if win2:
            self.four_check_win_side(p2)
            output = True
        if tie:
            self.four_check_tie_side()
            output = True

        return output

    def four_check_back(self,color) -> bool:
        """four check back is the module used to find a win"""
        #Registers all row combinations
        val = False
        for row in range(6):
            for count in range(4):
                row_count = row * 7
                #print('Four Row Check',self.move_list[count + row_count] , self.move_list[count + 1 + row_count] , self.move_list[count + 2 + row_count] , self.move_list[count + 3 + row_count],'row',int(row_count/7 + 1))
                if self.move_list[count + row_count] == self.move_list[count + 1 + row_count] == self.move_list[count + 2 + row_count] == self.move_list[count + 3 + row_count]:
                    if color in self.move_list[count + row_count]:
                        winning_numbers.append([count + row_count , count + 1 + row_count , count + 2 + row_count , count + 3 + row_count])
                        val = True
        #Registers all column combinations
        for column in range(7):
            for count in range(3):
                column_count = count * 7
                if self.move_list[column_count + column] == self.move_list[column_count + 7 + column] == self.move_list[column_count + 14 + column] == self.move_list[column_count + 21 + column]:
                    if color in self.move_list[column + column_count]:
                        winning_numbers.append([column_count + column , column_count + 7 + column , column_count + 14 + column , column_count + 21 + column])
                        val = True
        #Registers all diagonal combinations
        for spots,value in enumerate(self.move_list):
            try:
                #Registers all negative slope diagonal combinations
                if math.floor(spots/7) != math.floor((spots + 8) / 7 ) != math.floor((spots + 16) / 7) != math.floor((spots + 24) / 7):
                    if self.move_list[spots] == self.move_list[spots + 8] == self.move_list[spots + 16] == self.move_list[spots + 24]:
                        print('Values',color)
                        print((value == self.move_list[spots + 8] == self.move_list[spots + 16] == self.move_list[spots + 24]),value , self.move_list[spots + 8] , self.move_list[spots + 16] , self.move_list[spots + 24])
                        print(repr(value))
                        if color in repr(value):
                            print('Winning for color')
                            winning_numbers.append([spots, spots + 8, spots + 16, spots + 24])
                            val = True
                #Registers all positive slope diagonal combinations
                if math.floor(spots/7) != math.floor((spots + 6) / 7 ) != math.floor((spots + 12) / 7) != math.floor((spots + 18) / 7):
                    if value == self.move_list[spots + 6] == self.move_list[spots + 12] == self.move_list[spots + 18]:
                        if color in repr(value):
                            winning_numbers.append([spots, spots + 6, spots + 12, spots + 18])
                            val = True
            except:
                pass
            
            
        if val:
            print('Win')
            return True
        return False
    
    def four_check_win_side(self,player) -> None:
        """Code that runs if there is a win"""
        self.print_board()
        self.set_board()
        print('{} connected 4'.format(player.name))
        player.scorepp()
        self.score_print()
        self.cont_prompt()

    def four_check_tie_side(self) -> None:
        """Code that runs if there is a tie"""
        self.print_BOARD()
        self.set_BOARD()
        print('\nTie Game')
        self.score_print()
        self.cont_prompt()

    def chosen_check(self) -> list:
        """Test for chosen spots on the BOARD. Returns list of unchosen spaces"""
        templist = []
        for spot in self.move_list:
            if isinstance(spot,int):
                templist.append(spot)
        return templist

    def cont_prompt(self) -> None:
        """Asks if the plyer wants to continue playing after a game"""
        while True:
            cont_inp = input('Continue Playing?\n')
            if cont_inp == 'Yes' or cont_inp == 'yes':
                break
            elif cont_inp == 'No' or cont_inp == 'no':
                self.cont_playing = False
                break
            else:
                print('Please input yes, or no\n')

    def score_print(self) -> None:
        """Prints both players score as well as their names next to it"""
        print('{}\'s Score: {}, {}\'s Score: {}'.format(PLAYER1.name,PLAYER1.score,PLAYER2.name,PLAYER2.score))

    def legal_moves(self) -> list[int]:
        legal_moves_list = [1,2,3,4,5,6,7]
        if not isinstance(self.move_list[41],int):
            legal_moves_list.remove(7)
        if not isinstance(self.move_list[40],int):
            legal_moves_list.remove(6)
        if not isinstance(self.move_list[39],int):
            legal_moves_list.remove(5)
        if not isinstance(self.move_list[38],int):
            legal_moves_list.remove(4)
        if not isinstance(self.move_list[37],int):
            legal_moves_list.remove(3)
        if not isinstance(self.move_list[36],int):
            legal_moves_list.remove(2)
        if not isinstance(self.move_list[35],int):
            legal_moves_list.remove(1)
        return legal_moves_list

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

    def BOARD_change(self) -> None:
        """Board_Change module takes the choice from the Player class and puts it into the Board class"""
        #Accounts for list syntax
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
                self.BOARD_change()
        BOARD.move_list[self.choice] = '\x1b[{}{}O\x1b[0m'.format(self.color,BOARD.blackbg)

    def choice_flipper(self,num) -> int:
        """Flips choice so it can display neatly(e.g. 1 -> 7, 3 -> 4, etc.)"""
        match num:
            case 1:
                return 7
            case 2:
                return 6
            case 3:
                return 5
            case 4:
                return 4
            case 5:
                return 3
            case 6:
                return 2
            case 7:
                return 1            

class Person(Player):
    """Logic for the human player. Only difference is how they get their move"""
    def choice_getter(self) -> None:
        """Gets choice for human player"""
        while True:
            BOARD.print_board()
            self.choice = input('\n\n{}, Choose a spot\n'.format(self.name))
            if self.choice == 'quit' or self.choice == 'Quit':
                print ('Quitting...')
                quit()
            try:
                self.choice = int(self.choice)
            except:
                print('\nGive a viable location\n\n')
                continue
            if int(self.choice) not in [1,2,3,4,5,6,7]:
                print('\nGive a viable location\n\n')
                continue
            break

class EasyAI(Player):
    """Logic for the Easy AI. Completely random"""
    def __init__(self,name) -> None:
        """Only change in overloaded init is that the ai color getter is called"""
        self.name = name
        self.score = 0
        self.color = self.ai_color_getter()
        self.choice = None
        

    def choice_getter(self) -> None:
        """Easy AI chooses a random legal move from the BOARD"""
        self.choice = random.choice(BOARD.legal_moves())

class HardAI(Player):
    #Used to find the best move 
    win_moves = []
    best_moves_dict = {}
    best_moves = []
    #Used to enact theoretical BOARDs
    temp_board = []
    """Logic for the Hard AI. Uses an algorithm to find the best move"""
    def __init__(self,name) -> None:
        """Only change in overloaded init is that the ai color getter is called"""
        self.name = name
        self.score = 0
        self.color = self.ai_color_getter()
        self.choice = None
        self.temp_board = BOARD.move_list.copy()

    def choice_getter(self):
        """Front end command to get the choice of the hard ai"""
        if self.recognize_win(self) or self.recognize_win(PLAYER1):
            best_moveKV = (0,0)
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
                self.win_moves[index] = self.choice_flipper((move % 7))
                pass                

            for winning_move in self.win_moves:
                #Assigns score to moves
                if isinstance(playerObj,HardAI):
                    self.best_moves_dict[winning_move] = 100
                else:
                    self.best_moves_dict[winning_move] = 99
            return True
        return False

#Functions

def colors(color) -> str:
    """Turns player choice into unicode for the Player object to turn the O into the specified color"""
    ret_value = Colors.color_dict[color]

    Colors.color_og_list.remove(Colors.color_dict[color])
    Colors.color_dict.clear()
    for key,value in enumerate(Colors.color_og_list,start= 1):
        Colors.color_dict[str(key)] = value
    return ret_value

def startup() -> int:
    """Gets the mode/difficulty user input. Reused code from Tic Tac Toe"""
    while True:
        try:
            dif = int(input('Modes\n1.Player vs Player\n2.Player vs Easy AI\n3.Player vs Hard AI\n'))
        except:
            print('\nPlease input 1, 2, or 3')
            continue
        if dif not in [1,2,3]:
            print('Please input a 1, 2, or 3')
            continue
        return dif

def starterRequest() -> int:
    """Gets who the player wants to start"""
    while True:
        starter = input('Who goes first\n1.Player\n2.AI\n3.Random\n')
        try:
            starter = int(starter)
        except:
            print('Please input 1, 2, or 3')
        if starter not in [1,2,3]:
            print('Please input 1, 2, or 3')
            continue
        break
    return starter

def name_getter(num) -> str:
    """Gets name for Person object. Reused code from Tic Tac Toe"""
    while True:
        name = input('Player {}, input your name. '.format(num))
        if len(name) < 1:
            print('Insert a name please')
            continue
        break
    return name

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
            PLAYER1.BOARD_change()
            status = BOARD.four_check_front(PLAYER1,PLAYER2)
            t = 2
            if status:
            #if someone won, restart the game with PLAYER2 going first
                t = nextP
                nextP = 1
                continue
        if t == 2:
            PLAYER2.choice_getter()
            PLAYER2.BOARD_change()
            status = BOARD.four_check_front(PLAYER1,PLAYER2)
            if status:
            #if someone won, restart the game with PLAYER2 going first
                t = nextP
                nextP = 2
            else:
                t = 1

#Level Functions
def game_modes() -> None:
    """Runs different mode level functions"""
    dif = startup()
    match int(dif):
        case 1:
            player_VS_player()
        case 2:
            player_VS_ezai()
        case 3:
            player_VS_hardai()

def player_VS_player() -> None:
    """Player vs player code. Dif 1"""
    global PLAYER1
    global PLAYER2
    p1name = name_getter('1')
    p2name = name_getter('2')
    PLAYER1 = Person(p1name)
    PLAYER2 = Person(p2name)
    turns(1)

def player_VS_ezai() -> None:
    """Player vs an easy/random AI. Dif 2"""
    global PLAYER1
    global PLAYER2
    p1name = name_getter('1')
    p2name = 'Easy Computer'
    PLAYER1 = Person(p1name)
    PLAYER2 = EasyAI(p2name)
    starter = starterRequest()
    #Randomnly making variable starter 1 or 2 if the user chose random
    if starter == 3:
        starter = random.choice([1,2])
    if starter == 1:
        pfirst = 1
    if starter == 2:
        pfirst = 2
    turns(pfirst)

def player_VS_hardai() -> None:
    """Player vs Hard/Smart AI. Dif 3"""
    global PLAYER1
    global PLAYER2
    p1name = name_getter('1')
    p2name = 'Hard Computer'
    PLAYER1 = Person(p1name)
    PLAYER2 = HardAI(p2name)
    starter = starterRequest()
    #Randomnly making variable starter 1 or 2 if the user chose random
    if starter == 3:
        starter = random.choice([1,2])
    if starter == 1:
        pfirst = 1
    if starter == 2:
        pfirst = 2
    turns(pfirst)



#Main Game Code

if __name__ == '__main__':
    print('Main run')
    global BOARD 
    BOARD = Board()
    game_modes()

>>>>>>> 533daa36b3a8e98e9f5a307e9c6ebd31e6249646
