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
                index = col * 7 + row 
                #print(index)
                if ((index) // 7) == ((index + 1) // 7) == \
                ((index + 2) // 7) ==  ((index + 3) // 7):
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
        print()
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

        #Printing the colored chip or the empty space
            if isinstance(spot, int): print(' ',end='')
            else: print(spot,end='')

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
        self.choice = None
        self.color = None

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
    def __init__(self):
        self.color = choice(Colors.color_og_list)
        self.score = 0

    name = 'Computer'

    @abstractmethod
    def choice_getter(self,board : Board):
        ...
    
class EasyAI(AI):
    def choice_getter(self, board: Board):
        self.choice = choice(board.legal_moves)

class HardAI(AI):
    def __init__(self,other : Player):
        self.color = choice(Colors.color_og_list)
        self.score = 0
        self.other = other

    def choice_getter(self,board: Board):
        print(self.other.color)
        self.choice = self.minimax(board,5,True)

    def minimax(self,board : Board,depth : int, maxPlayer : bool):
        if depth == 0 or bool(win_check(board)):
            print('WIN OR LOSS FOUND\nNOT A REAL BOARD')
            board.print_board()
            print('NOT A REAL BOARD')
            return pos_eval(self,board)
        
        best_move = None
        if maxPlayer:
            best_pos = -1000
            for move in board.legal_moves:
                self.choice = move + 1
                child = Board()
                child.board_list = board.board_list[:]
                board_change(self,child)
                pos = self.minimax(child, depth - 1, False)
                if pos > best_pos:
                    best_pos = pos
                    best_move = move

            return best_move

        else:
            best_pos = 1000

            for move in board.legal_moves:
                self.other.choice = move + 1
                child = Board()
                child.board_list = board.board_list[:]
                board_change(self.other,child)
                pos = self.minimax(child, depth - 1, True)
                if pos < best_pos:
                    best_pos = pos
                    best_move = move

            return best_move

#General functions
def board_change(player : Player,board : Board) -> None:
    player.choice -= 1
    try:
        while True:
            if isinstance(board.board_list[player.choice],str):
                #Spot is taken
                player.choice += 7
                continue

            board.board_list[player.choice] = f'\x1b[{player.color}40mO\x1b[0m'
            break
    except:
        pass

def get_color(s : str):
    """Used to get the color unicode from the string"""
    start = s.index('40m')
    return s[start - 3:start]

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
        try:
            starter = int(input('Who goes first\n1.Player\n2.AI\n3.Random\n'))
        except:
            print('Please input 1, 2, or 3')
        if starter not in [1,2,3]:
            print('Please input 1, 2, or 3')
            continue
        break
    return starter

def win_check(board : Board):
    #Initializations
    wins = []
    rows = Get_Indexes.get_rows()
    cols = Get_Indexes.get_cols()
    neg_diags = Get_Indexes.get_neg_diags()
    pos_diags = Get_Indexes.get_pos_diags()

    #Finding if it is a win
    row_wins = [i for i in rows if len(set(list(map(lambda a: board.board_list[a],i)))) == 1]
    col_wins = [i for i in cols if len(set(list(map(lambda a: board.board_list[a],i)))) == 1]
    neg_diag_wins = [i for i in neg_diags if len(set(list(map(lambda a: board.board_list[a],i)))) == 1]
    pos_diag_wins = [i for i in pos_diags if len(set(list(map(lambda a: board.board_list[a],i)))) == 1]

    #Adding it all to the wins list
    wins.extend(row_wins)
    wins.extend(col_wins)
    wins.extend(neg_diag_wins)
    wins.extend(pos_diag_wins)

    return wins

def done_playing() -> bool:
    viable_responses = {'1' : True, '2' : False, 'Yes' : True, 'No' : False}
    while True:
        inp = input('Would you like to keep playing?\n1. Yes\n2. No\n')
        ret = viable_responses.get(inp.title(),None)
        if ret != None:
            return ret
        
        print('Please choose one of the given options')

def pos_eval(p : Player,board : Board):
    """Evalutation of a position for hard AI"""
    if wins := win_check(board):
        i = board.board_list[wins[0][0]]
        if get_color(i) == p.color: return 100
        else: return -100

    score = 0
    rows = Get_Indexes.get_rows()
    cols = Get_Indexes.get_cols()
    pos_diags = Get_Indexes.get_pos_diags()
    neg_diags = Get_Indexes.get_neg_diags()

    count = 0
    chip = '\x1b[' + p.color + '40m\x1b[0m'
    for row in rows:
        row = list(map(lambda a:board.board_list[a],row))
        if row.count(chip) == 3:
            return 99
        
        for foo in row:
            if isinstance(foo,str) and foo != chip:
                count += 1

        if count == 3:
            return -99
     
        count = 0

    return score

#Level and turn functions
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
    p2 = HardAI(p1)
    
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
            if run:
                run,winner = turn_checks(p1,board)
            if run:
                run,winner = turn_checks(p2,board)
        else:
            if run:
                run,winner = turn_checks(p2,board)
            if run:
                run,winner = turn_checks(p1,board)

    if isinstance(winner,Player):
        winner.score += 1
        print(f'{winner.name} won the game')
        print(f'Score\n{p1.name}: {p1.score}, {p2.name}: {p2.score}')
    else:
        assert winner != None, 'Escaped loop with no winner'
        print('Tie Game')
        print(f'Score\n{p1.name}: {p1.score}, {p2.name}: {p2.score}')

    dp = done_playing()
    if dp:
        board1 = Board()
        turns(p1,p2,board1,first)

def turn_checks(p : Player,board : Board):
    p.choice_getter(board)
    winner = None
    assert p.choice,f'Problem initializing player.choice in choice getter in the {p.__class__} class'
    board_change(p,board)
    wins = win_check(board)
    state = not bool(wins)
    #if true win has not been found
    if not state or len(board.legal_moves) == 0:
        for win in wins:
            for index in win:
                start = board.board_list[index].index(';40m')
                tempstr = [c for c in board.board_list[index]]
                tempstr.insert(start - 2, '1;')
                board.board_list[index] = ''.join(tempstr)

                winner = p

        if not winner:
            winner = 'Tie'
            
    board.print_board()
    return state,winner

def game_modes():
    board = Board()
    viable_responses = {
    '1' : player_vs_player, 
    '2' : player_vs_ezai,
    '3' : player_vs_hardai
    }

    while True:
        inp = input('Choose game mode\n1. Player vs Player\n2. Player vs Easy AI\n3. Player vs Hard AI\n')
        ret = viable_responses.get(inp,None)
        if ret == None:
            print('Please from the given options')
        else:
            ret(board)
            break

#Main Game Code

if __name__ == '__main__':
    game_modes()
    

