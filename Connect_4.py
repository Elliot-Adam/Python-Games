#Connect 4

#Imports
from abc import abstractmethod
from random import choice

#Classes

class Colors:
    color_dict = {'1':'31;','2':'34;','3':'32;','4':'33;'}
    color_og_list = ['31;','34;','32;','33;']
    color_list = ['Red','Blue','Green','Yellow']

class Get_Indexes:
    def get_rows():
        row_list = []
        for col in range(6):
            for row in range(4):
                index = (col + 1) * 7 + row 
                if ((index) % 7) == ((index + 1) % 7) == \
                ((index + 2) % 7) ==  ((index + 3) % 7):
                    row_list.append([index,index + 1,index + 2,index + 3])

        return row_list
    
    def get_cols():
        col_list = []
        for index in range(21):
            col_list.append([index,index + 7, index + 14, index + 21])

        return col_list
    
    def get_neg_diags():
        diag_list = []
        for index in range(18):
            if (index // 7 == ((index + 8) // 7 - 1) == \
                ((index + 16) // 7 - 2) == ((index + 24) // 7 - 3)):
                diag_list.append([index,index + 8, index + 16, index + 24])
                
        return diag_list
    
    def get_pos_diags():
        diag_list = []
        for index in range(21):
            if (index // 7 == ((index + 6) // 7 - 1) == \
                ((index + 12) // 7 - 2) == ((index + 18) // 7 - 3)):
                diag_list.append([index,index + 6, index + 12, index + 18])
                
        return diag_list

class Board:
    def __init__(self):
        self.board_list : list = []
        for num in range(42): self.board_list.append(num + 1)

    def print_board(self):
        print('  ',end='')
        for i in range(7): print(i + 1,end='   ')
        print()
        print('  ',end='')
        for _ in range(7): print('\u2193',end='   ')
        print()

        ldone = 0
        for spot in self.board_list[::-1]:
            if ldone == 0:
                print('| ',end='')
                ldone += 1

            if isinstance(spot, int):
                print(' ',end='')
            
            else:
                print(spot,end='')

            if ldone == 7:
                print(' | ')
                ldone = 0

            else:
                print(' | ',end='')
                ldone += 1    

    @property
    def legal_moves(self):
        return [8 - ((i % 7) + 1) for i in [41,40,39,38,37,36,35] if isinstance(self.board_list[i],int)]

class Player:
    def __init__(self):
        self.score = 0

    @abstractmethod
    def choice_getter(self,board : Board):
        ...

class Person(Player):
    def __init__(self,num):
        self.score = 0
        self.name = self.name_getter(num)
        self.color = self.color_getter()

    def choice_getter(self, board: Board):
        while True:
            inp = input(f'\n{self.name}, Choose a spot ')
            try:
                if int(inp) not in board.legal_moves:
                    print('Please choose a legal move')
                
                else:
                    break
            except: pass

        self.choice = 8 - int(inp)

    def name_getter(self,num) -> str:
        """Gets name for Person object. Reused code from Tic Tac Toe"""
        while True:
            name = input('Player {}, input your name. '.format(num))
            if len(name) < 1:
                print('Insert a name please')
                continue
            break
        return name

    def color_getter(self):
        while True:
            print(f'{self.name}, Please choose a color')
            for key,value in enumerate(Colors.color_list):
                print(f'{key + 1}. {value}')
            col = input()
            if Colors.color_dict.get(col,None) == None:
                #col not in color dict
                print('Please choose one of the given options')
                
            else:
                break
        return colors(col)

class AI(Player):
    name = 'Computer'

    @abstractmethod
    def choice_getter(self,board : Board):
        ...
    
class EasyAI(AI):
    def choice_getter(self, board: Board):
        self.choice = choice(board.legal_moves)

class HardAI(AI):
    def choice_getter(self, board: Board):
        self.choice = self.best_move(board)
    
    def best_move(board : Board):
        pass

#Functions
def board_change(player : Player,spot : int,board : Board) -> None:
    spot -= 1
    try:
        while True:
            if isinstance(board.board_list[spot],str):
                #Spot is taken
                spot += 7
                continue

            board.board_list[spot] = f'\x1b[{player.color}40mO\x1b[0m'
            break
    except:
        pass

def colors(color) -> str:
    """Turns player choice into unicode for the Player object to turn the O into the specified color"""
    ret_value = Colors.color_dict[color]

    Colors.color_og_list.remove(Colors.color_dict[color])
    Colors.color_list.pop(int(color) - 1)
    Colors.color_dict.clear()
    for key,value in enumerate(Colors.color_og_list,start= 1): Colors.color_dict[str(key)] = value
    return ret_value

def startup() -> int:
    """Gets the mode/difficulty user input. Reused code from Tic Tac Toe"""
    while True:
        try:
            dif = int(input('Modes\n1.Player vs Player\n2.Player vs Easy AI\n3.Player vs Hard AI\n'))
        except:
            print('\nPlease input 1, 2, or 3')
            continue
        if dif not in range(1,5):
            print('\nPlease input a 1, 2, or 3')
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

def end_check(board : Board):
    #Initializations
    wins = []
    rows = Get_Indexes.get_rows()
    cols = Get_Indexes.get_cols()
    neg_diags = Get_Indexes.get_neg_diags()
    pos_diags = Get_Indexes.get_pos_diags()

    #Finding if it is a win
    row_wins = [i for i in rows if len(set(list(map(lambda a: board.board_list[a]),i))) == 1]
    col_wins = [i for i in cols if len(set(list(map(lambda a: board.board_list[a]),i))) == 1]
    neg_diag_wins = [i for i in neg_diags if len(set(list(map(lambda a: board.board_list[a]),i))) == 1]
    pos_diag_wins = [i for i in pos_diags if len(set(list(map(lambda a: board.board_list[a]),i))) == 1]

    #Adding it all to the wins list
    wins.extend(row_wins)
    wins.extend(col_wins)
    wins.extend(neg_diag_wins)
    wins.extend(pos_diag_wins)

    return wins

#Level functions
def player_vs_player(board : Board):
    p1 = Person('1')
    p2 = Person('2')

    turns(p1,p2,board,1)

def player_vs_ezai(board : Board):
    p1 = Person('1')
    p2 = EasyAI()
    
    first = starterRequest()
    if first in [1,2]:
        turns(p1,p2,board,first)

    else:
        turns(p1,p2,board,choice([1,2]))

def player_vs_hardai(board : Board):
    p1 = Person('1')
    p2 = HardAI()

    p1.name_getter('1')
    
    first = starterRequest()
    if first in [1,2]:
        turns(p1,p2,board,first)

    else:
        turns(p1,p2,board,choice([1,2]))

def turns(p1 : Player, p2 : Player, board : Board, first : int) -> None:
    run = True
    board.print_board()
    while run:
        if first == 1:
            run = turn_checks(p1,board)
            run = turn_checks(p2,board)
        else:
            run = turn_checks(p2,board)
            run = turn_checks(p1,board)

def turn_checks(p : Player,board : Board):
    p.choice_getter(board)
    assert p.choice,f'Problem initializing player.choice in choice getter in the {p.__class__} class'
    board_change(p,p.choice,board)
    board.print_board()
    wins = end_check(board)
    state = bool(len(wins))
    return state

def game_modes():
    board = Board()
    viable_responses = {
    '1' : player_vs_player, 
    '2' : player_vs_ezai,
    '3' : player_vs_hardai}

    while True:
        inp = input('Choose game mode\n1. Player vs Player\n2. Player vs Easy AI\n3. Player vs Hard AI\n')
        ret = viable_responses.get(inp,None)
        if ret == None:
            print('Please from the given options')
        else:
            ret(board)

#Main Game Code

if __name__ == '__main__':
    game_modes()
    

