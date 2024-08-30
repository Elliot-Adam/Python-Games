import pygame
pygame.init()

from abc import abstractmethod
from abc import abstractproperty

import os

from screen import Screen

class Sounds:
    def sound_get() -> dict:
        sounds = {}
        sounds['PIECE_TAKING'] = pygame.mixer.Sound(f'{Utility.file_start}/SOUND_PIECE_TAKING.m4a')

class Coord:
    def __init__(self,coord):
        self.coord = coord

    @staticmethod
    def legal_coords():
        legal = []
        for letter in Utility.letter_to_num.keys():
            for number in Utility.letter_to_num.values():
                coord = letter + str(number)
                legal.append(coord)

        return legal
    
    def __add__(self,other : tuple) -> str:
        #Letter
        letter = Utility.letter_to_num[self.coord[0]] + other[0]
        #Number
        number = int(self.coord[1]) + other[1]
        if letter - 1 not in range(8) or number - 1 not in range(8):
            return None
        coord = Utility.num_to_letter[letter] + str(number)
        assert isinstance(coord,str)
        return coord

class Piece:
    def __init__(self,color : str,coord : str):
        self.coord = coord
        assert color in ('WHITE','BLACK'),'Initializing piece without proper color'
        self.color = color
        self.image = pygame.image.load(f'{Utility.file_start}/PIECE_{color.upper()}_{self}.png')

    def block_check(self,board, last_board,checking_pieces : list) -> list:
        """Returns list to block the check"""
        board : Board = board
        last_board : Board = last_board
        assert str(self) != 'KING', "Shouldn't call block_check from king"
        if not checking_pieces: return []
        king : King = Utility.find_king(board,self.color)
        assert king, "Couldn't find your king on board"
        if len(checking_pieces) > 1: return [] #Impossible to block double check
        if str(checking_pieces[0]) == 'KNIGHT': return [] #Impossible to block knight check

        legal_moves = []

        piece : Piece = checking_pieces[0]
        in_common = set(tuple(piece.rules(board,last_board))) & set(tuple(piece.__class__.rules(piece.__class__(king.color,king.coord),board,last_board)))
        #Makes a set of the moves of the checking piece and grabs everything in common with if the king had the checking pieces rules which should grab all the spaces between them

        for move in list(in_common):
            if move in self.rules(board,last_board):
                next_board = board.board_dict.copy()
                next_board[move] = self
                next_board[self.coord] = None
                if next_board[king.coord].in_check(board,last_board): continue
                legal_moves.append(move)

        return legal_moves
    
    @abstractmethod
    def rules(self,board, last_board) -> list:
        ...

    @abstractproperty
    def value(self):
        ...

class Board:
    def __init__(self) -> None:
        self.board_dict : dict[str,Piece] = Board.set_board_dict()
        self.set_pawns()
        self.set_pieces()

    @staticmethod
    def set_board_dict() -> dict:
        board_dict = {}
        for coord in Coord.legal_coords():
            board_dict[coord] = None

        return board_dict 

    def change_board(self,coord, piece : Piece) -> None:
        self.board_dict[coord] = piece

    def set_pawns(self) -> None:
        for letter in Utility.letter_to_num.keys():
            for num,color in {'2':'WHITE','7':'BLACK'}.items():
                coord = letter + num
                self.board_dict[coord] = Pawn(color,coord)

    def set_pieces(self) -> None:
        let_to_piece : dict[str,Piece] = {'a' : Rook, 'b' : Knight, 'c' : Bishop, 'd' : Queen, 
                               'e' : King, 'f' : Bishop, 'g' : Knight, 'h' : Rook}
        for letter in Utility.letter_to_num.keys():
            for num,color in {'1':'WHITE','8':'BLACK'}.items():
                coord = letter + num
                self.board_dict[coord] = let_to_piece[letter](color,coord)

class Pawn(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    has_moved = False

    def __str__(self):
        return 'PAWN'
    
    def rules(self, board : Board,last_board : Board) -> list:
        #Movement
        legal_moves = []
        if movement := self.movement_rules(board):
            legal_moves.extend(movement)
        if capture := self.capture_rules(board):
            legal_moves.extend(capture)
        if en_passant := self.en_passant_rules(board,last_board):
            legal_moves.extend(en_passant)

        king : King = Utility.find_king(board,self.color)

        """for move in legal_moves:
            next_board = board.board_dict.copy()
            next_board[move] = self
            next_board[self.coord] = None
            if next_board[king.coord].in_check(board,last_board): continue
            legal_moves.append(move)"""

        return legal_moves
    
    def movement_rules(self,board : Board) -> list:
        legal_moves = []
        coord = Coord(self.coord)
        two_coord = None
        color_dict = {'WHITE': +1 , 'BLACK' : -1}
        one_coord = coord + (0,color_dict[self.color])
        if not self.has_moved:
            two_coord = coord + (0,color_dict[self.color] * 2)

        if board.board_dict[one_coord] == None: legal_moves.append(one_coord)
        if two_coord != None:
            if board.board_dict[two_coord] == None: legal_moves.append(two_coord)
        return legal_moves

    def capture_rules(self,board : Board) -> list:
        legal_moves = []
        coord = Coord(self.coord)
        color_dict = {'WHITE': +1 , 'BLACK' : -1}

        left_attack_coord = coord + (-1,color_dict[self.color])
        right_attack_coord = coord + (1,color_dict[self.color])

        if left_attack_coord:
            if left_attack_coord[1] != 0 and board.board_dict[left_attack_coord] != None and board.board_dict[left_attack_coord].color != self.color: legal_moves.append(left_attack_coord)
        if right_attack_coord: 
            if right_attack_coord[1] != 9 and board.board_dict[right_attack_coord] != None and board.board_dict[right_attack_coord].color != self.color: legal_moves.append(right_attack_coord)
        return legal_moves
    
    def illegal_capture_rules(self,board : Board):
        "Used for en passant"
        legal_moves = []
        coord = Coord(self.coord)
        color_dict = {'WHITE': +1 , 'BLACK' : -1}

        left_attack_coord = coord + (1,color_dict[self.color])
        right_attack_coord = coord + (1,color_dict[self.color])

        legal_moves.append(left_attack_coord) 
        legal_moves.append(right_attack_coord)
        return legal_moves

    def en_passant_rules(self,board : Board,last_board : Board) -> list:
        legal_moves = []
        try:
            moved = Utility.piece_moved(board,last_board)
        except: return legal_moves
        
        if str(moved[0]) == 'PAWN':
            #Last moved was a pawn
            if abs(int(moved[0].coord[1]) - int(moved[1][1])) == 2:
                #Was a pawn double move
                letter = moved[0].coord[0]
                number = (int(moved[0].coord[1]) + int(moved[1][1])) // 2
                coord = letter + str(number)
                if coord in self.illegal_capture_rules(board):
                    legal_moves.append('_' + coord)

        return legal_moves

    @property
    def value(self):
        return 1

class Knight(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    def __str__(self):
        return 'KNIGHT'
    
    def rules(self,board : Board,last_board):
        legal_moves = []
        for x in [2,-2]:
            coord1 = Coord(self.coord) + (x,0)
            coord2 = Coord(self.coord) + (0,x)
            if not (coord1 or coord2):
                continue

            for y in [1,-1]:
                coord3 = None
                coord4 = None
                if coord1:
                    coord3 = Coord(coord1) + (0,y)
                if coord2:
                    coord4 = Coord(coord2) + (y,0)  

                if not (coord3 or coord4):
                    continue

                if coord3:
                    legal_moves.append(coord3)
                if coord4:
                    legal_moves.append(coord4)

        for move in legal_moves:
            if isinstance(board.board_dict[move],Piece) and board.board_dict[move].color == self.color:
                legal_moves.remove(move)

        return legal_moves

    @property
    def value(self):
        return 3

class Bishop(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    def __str__(self):
        return 'BISHOP'
    
    def rules(self,board:Board , last_board):
        legal_moves = []
        for xincr in [1,-1]:
            for yincr in [1,-1]:
                coord = Coord(self.coord)
                diag = True
                while diag:
                    coord = Coord(coord + (xincr,yincr))
                    if not coord.coord:
                        break

                    if board.board_dict[coord.coord] != None:
                        diag = False
                        if board.board_dict[coord.coord].color == self.color:
                            continue

                    legal_moves.append(coord.coord)

        return legal_moves

    @property
    def value(self):
        return 3

class Rook(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    has_moved = False

    def __str__(self):
        return 'ROOK'
    
    def rules(self,board:Board,last_board):
        legal_moves = []
        for xincr, yincr in [(0,1),(0,-1),(1,0),(-1,0)]:
            coord = Coord(self.coord)
            line = True
            while line:
                coord = Coord(coord + (xincr,yincr))
                if not coord.coord:
                    break

                if board.board_dict[coord.coord] != None:
                    line = False
                    if board.board_dict[coord.coord].color == self.color:
                        continue
                   
                legal_moves.append(coord.coord)


        return legal_moves

    @property
    def value(self):
        return 5

class Queen(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    def __str__(self):
        return 'QUEEN'
    
    def rules(self,board : Board,last_board : Board):
        legal_moves = []
        legal_moves.extend(Bishop.rules(self,board,last_board))
        legal_moves.extend(Rook.rules(self,board,last_board))
        return legal_moves

    @property
    def value(self):
        return 9

class King(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    has_moved = False

    def __str__(self):
        return 'KING'
    
    def rules(self,board:Board,last_board):
        legal_moves = []
        legal_moves.extend(self.movement_rules(board,last_board))
        if not self.has_moved:
            legal_moves.extend(self.castling_rules(board,last_board))
        return legal_moves

    def movement_rules(self,board : Board,last_board):
        legal_moves = []
        coord = Coord(self.coord)

        for x in range(3): 
            x -= 1
            coord1 = coord + (x,0)
            coord2 = Coord(coord1) + (0,1)
            coord3 = Coord(coord1) + (0,-1)
            if coord1:
                legal_moves.append(coord1)
            if coord2:
                legal_moves.append(coord2)
            if coord3:
                legal_moves.append(coord3)

        legal_moves.remove(self.coord)
        """covered = Utility.covered_squares(self.color,board,last_board)
        for move in legal_moves:
            if (board.board_dict[move] and board.board_dict[move].color == self.color) or (move in covered):
                legal_moves.remove(move)"""

        return legal_moves
    
    def castling_rules(self,board:Board,last_board : Board):
        legal_moves = []
        if self.has_moved:
            return []
        #if self.in_check(board,last_board):
        #    return []

        king_dict = {'WHITE':('a1','h1'),'BLACK':('a8','h8')}
        for rook_coord in king_dict[self.color]:
            if rook_spot := board.board_dict[rook_coord]:
                if isinstance(rook_spot,Rook) and rook_spot.color == self.color and not rook_spot.has_moved:
                    #Rook of same color is in one of the spots
                    if rook_coord < self.coord:
                        if board.board_dict['b' + rook_coord[1]] is None and board.board_dict['c' + rook_coord[1]] is None and board.board_dict['d' + rook_coord[1]] is None:
                            legal_moves.append('_c' + rook_coord[1])
                    else:
                        if board.board_dict['f' + rook_coord[1]] is None and board.board_dict['g' + rook_coord[1]] is None:
                            legal_moves.append('_g' + rook_coord[1]) 

        return legal_moves

    def in_check(self,board : Board,last_board : Board):
        checking_pieces = []
        for piece in board.board_dict.values():
            if piece and piece.color != self.color:
                #An opponents piece
                if self.coord in piece.rules(board,last_board):
                    #in check
                    checking_pieces.append(piece)

        return checking_pieces

    @property
    def value(self):
        return 0

class Utility:
    def coord_clicked(x,y,screen) -> tuple:
        'Gets the location on the chess board of where you clicked'
        #Letter

        if x not in range(Utility.TEXT_BUFFER, screen.SCREEN_WIDTH - Utility.BLANK_BUFFER):
            return None
        
        letter = -(((Utility.SQ_SIZE * 8) // screen.SCREEN_WIDTH - (x - Utility.TEXT_BUFFER)) // Utility.SQ_SIZE)

        if letter - 1 not in range(8):
            return None

        letter = Utility.num_to_letter[letter]

        #Number

        if y not in range(Utility.BLANK_BUFFER, screen.SCREEN_HEIGHT - Utility.TEXT_BUFFER):
            return None
        
        number = 9 + (((Utility.SQ_SIZE * 8) // screen.SCREEN_HEIGHT - (y - Utility.BLANK_BUFFER)) // Utility.SQ_SIZE)

        if number - 1 not in range(8):
            return None
        
        coord = letter + str(number)
        return coord

    def covered_squares(color : str,board : Board,last_board : Board) -> tuple:
        """Returns all covered squares that are covered by pieces of the opposite color"""
        covered = []
        for piece in board.board_dict.values():
            if piece and piece.color != color:
                covered.append(piece.rules(board,last_board))
        
        return tuple(covered)
    
    def piece_moved(board : Board, last_board : Board) -> tuple[Piece,str]:
        "Returns tuple where [0] is the piece that moved and [1] is where it moved from"
        base_board = Board()
        strbasedict = {}
        strboarddict = {}
        for k,v in base_board.board_dict.items():
            strbasedict[k] = str(v) 
        for k,v in board.board_dict.items():
            strboarddict[k] = str(v) 
        board_set = set(strboarddict.items())
        base_set = set(strbasedict.items())
        if not len(board_set ^ base_set) / 2 <= 1:
            #Not first turn
            board_set = set(board.board_dict.items())
            last_set = set(last_board.board_dict.items())
            moved = []

            changed_set = last_set ^ board_set
            count = {}
            for item in changed_set:count[item[1]] = count.get(item[1],0) + 1
            piece : Piece = Utility.dict_search(count,2)[0]

            coord_list = []
            coord_list.extend(Utility.dict_search(last_board.board_dict,piece))
            coord_list.extend(Utility.dict_search(board.board_dict,piece))
            coord_list.remove(piece.coord)
            from_coord = coord_list[0]

            moved.append(piece)
            moved.append(from_coord)
            assert moved, 'Didn\'t find moved piece'
            assert isinstance(moved[0],Piece) and isinstance(moved[1],str), 'Didn\'t find moved piece' 
            return tuple(moved)
        else:
            raise Exception('First Turn')

    def playerInp(board : Board,held : Piece,color : str,last_board : Board,screen : Screen) -> Piece:
        delay = False
        if pygame.mouse.get_pressed()[0]:
            coord = Utility.coord_clicked(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],screen)
            if coord:
                piece = board.board_dict[coord]
                if piece != None and piece.color == color and not held:
                    #Picking up a piece
                    held = piece
                    delay = True
                    return held,color,delay
                
                if held:
                    #Putting down a piece
                    if coord == held.coord:
                        board.change_board(coord,held)
                        held = None
                        delay = True
                        return held,color,delay
                        
                    if rules := held.rules(board,last_board):
                        if coord in rules:
                            #If clicked on a legal move
                            last_board.board_dict = board.board_dict.copy()
                            last_board.board_dict[held.coord] = held
                            assert str(board.board_dict[coord]) != 'KING', "Shouldn't be able to take king"
                            board.change_board(held.coord,None)
                            board.change_board(coord,held)
                            held.coord = coord
                            if str(held) in ['PAWN','KING','ROOK']:
                                held.has_moved = True
                            held = None
                            delay = True
                            color = Utility.color_change[color]

                        elif isinstance(held,Pawn) and ('_' + coord in held.rules(board,last_board)):
                            #Is an en passant move
                            color_dict = {'WHITE' : -1, 'BLACK' : 1}
                            number = str(int(coord[1]) + color_dict[held.color])
                            letter = coord[0]
                            taken = letter + number
                            board.change_board(taken,None)
                            last_board.board_dict = board.board_dict.copy()
                            last_board.board_dict[held.coord] = held
                            board.change_board(held.coord,None)
                            board.change_board(coord,held)
                            held.coord = coord
                            held = None
                            delay = True
                            color = Utility.color_change[color]

                        elif isinstance(held,King) and ('_' + coord in held.rules(board,last_board)):
                            #Is a castling move
                            #Moving the rook
                            if coord > held.coord:
                                rook : Rook = board.board_dict['h' + held.coord[1]]
                                rook_spot = Coord(coord) + (-1,0)

                            else:
                                rook : Rook = board.board_dict['a' + held.coord[1]]
                                rook_spot = Coord(coord) + (1,0)

                            board.change_board(rook.coord,None)
                            board.change_board(rook_spot,rook)
                            rook.coord = rook_spot        

                            rook.has_moved = False
                            held.has_moved = False

                            #Setting down the king 

                            board.change_board(held.coord,None)
                            board.change_board(coord,held)

                            held = None
                            delay = True
                            color = Utility.color_change[color]

                        else:
                            #Clicked on a non legal move
                            board.change_board(held.coord,held)
                            held = None
                            delay = True
            elif held:
                #Puts back down the piece if you click outside of the board
                board.change_board(held.coord,held)
                held = None
                delay = True
        
        return held,color,delay
    
    def screen_setup() -> Screen:
        bg = Utility.file_start + 'BOARD_WHITE.png'
        icon = Utility.file_start + 'PIECE_WHITE_PAWN.png'
        screen = Screen(500,500,'Chess',icon,bg)
        screen.__setattr__('draw_pieces',draw_pieces)
        screen.__setattr__('draw_held',draw_held)
        screen.__setattr__('screen_run',screen_run)
        screen.__setattr__('draw_possible',draw_possible)
        return screen
    
    def dictSwapper(og : dict):
        "Swaps a dictionary's values and keys into another dictionary"
        empty : dict = {}
        for k,v in og.items():
            empty[v] = k
        return empty
    
    def dict_search(dictionary : dict, keyword) -> list:
        "Gets list of keys from a keyword"
        l : list = []
        for k,v in dictionary.items():
            if v is keyword:
                l.append(k)
        return l
    
    def find_king(board : Board, color: str) -> King:
        king : King = None
        for piece in board.board_dict.values():
            if piece and str(piece) == 'KING':
                if piece.color == color:
                    #piece = your own king
                    king = piece
                    break
        
        return king

    letter_to_num = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
    num_to_letter = dictSwapper(letter_to_num)
    color_change = {'WHITE' : 'BLACK', 'BLACK' : 'WHITE'}

    SQ_SIZE = 54
    TEXT_BUFFER = 39
    BLANK_BUFFER = 23

    file_start = (os.path.dirname(__file__) + '/Chess_Assets/').replace('\\','/')

def draw_pieces(self,board : Board,held) -> None:
        for coord,piece in board.board_dict.items():
            if piece != None and piece != held:
                x = Utility.TEXT_BUFFER + ((Utility.letter_to_num[coord[0]] - 1) * Utility.SQ_SIZE) + (Utility.letter_to_num[coord[0]])
                y = Utility.BLANK_BUFFER + ((8 - int(coord[1])) * Utility.SQ_SIZE) + (8 - int(coord[1])) + 2.5
                rect = pygame.Rect(x,y,Utility.SQ_SIZE,Utility.SQ_SIZE)
                scaled = pygame.transform.scale(piece.image,(Utility.SQ_SIZE - 5,Utility.SQ_SIZE - 5))
                self.SCREEN.blit(scaled,rect)

def draw_held(self,held : Piece):
    if held != None:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        
        buffer = -20

        rect = pygame.Rect(x + buffer,y + buffer,Utility.SQ_SIZE,Utility.SQ_SIZE)
        scaled = pygame.transform.scale(held.image,(Utility.SQ_SIZE - 5,Utility.SQ_SIZE - 5))
        self.SCREEN.blit(scaled,rect)

def draw_possible(self,held : Piece,board : Board,lastBoard : Board):
    if not held: return
    for move in held.rules(board,lastBoard):
        if '_' in move: move = move[1:]
        x = (Utility.letter_to_num[move[0]] - 1) * Utility.SQ_SIZE + Utility.TEXT_BUFFER
        y = (8 - int(move[1])) * Utility.SQ_SIZE + Utility.BLANK_BUFFER

        if board.board_dict[move] is None:
            img = pygame.image.load('Chess_Assets/DOT_SMALL.png')
        else:
            img = pygame.image.load('Chess_Assets/DOT_BIG.png')

        rect = pygame.Rect(x + 5,y + 5,Utility.SQ_SIZE,Utility.SQ_SIZE)
        scaled = pygame.transform.scale(img,(Utility.SQ_SIZE - 5,Utility.SQ_SIZE - 5))
        self.SCREEN.blit(scaled,rect)

def screen_run(self : Screen,board : Board , held : Piece, lastBoard : Board) -> None:
    self.draw_bg()
    self.draw_possible(self,held,board,lastBoard)
    self.draw_pieces(self,board,held)
    self.draw_held(self,held)

def run():
    game_board = Board()
    last_board = Board()
    screen = Utility.screen_setup()
    running = True
    game_clock = pygame.time.Clock()
    FPS = 30
    held = None
    color = 'WHITE'
    delay = False
    delay_count = 0
    while running:
        game_clock.tick(FPS)
        screen.screen_run(screen,game_board,held,last_board)
        if not delay:
            held , color , delay = Utility.playerInp(game_board, held,color, last_board,screen)
        else:
            if delay_count == 5:
                delay = False
                delay_count = -1
            delay_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    run()