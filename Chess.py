import pygame
pygame.init()

from time import sleep
from abc import abstractmethod
from abc import abstractproperty

from Playground import dictSwapper

class Sounds:
    file_start = 'C:/Users/Elliot/Specific Projects/Python-Games/Chess'
    PIECE_TAKING = pygame.mixer.Sound(f'{file_start}/SOUND_PIECE_TAKING.m4a')

class Convert:
    letter_to_num = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
    num_to_letter = dictSwapper(letter_to_num)
    color_change = {'WHITE' : 'BLACK', 'BLACK' : 'WHITE'}

class BoardImgSizes:
    SQ_SIZE = 54
    TEXT_BUFFER = 39
    BLANK_BUFFER = 23

class Piece:
    def __init__(self,color : str,coord : str):
        self.coord = coord
        self.color = color
        self.image = pygame.image.load(f'C:/Users/Elliot/Specific Projects/Python-Games/Chess/PIECE_{color.upper()}_{self}.png')

    @abstractmethod
    def rules(self,board, last_board):
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
        for letter in Convert.letter_to_num.keys():
            for number in Convert.letter_to_num.values():
                coord = letter + str(number)
                board_dict[coord] = None

        return board_dict 

    def change_board(self,coord, piece : Piece) -> None:
        self.board_dict[coord] = piece

    def set_pawns(self) -> None:
        for letter in Convert.letter_to_num.keys():
            for num,color in {'2':'WHITE','7':'BLACK'}.items():
                coord = letter + num
                self.board_dict[coord] = Pawn(color,coord)

    def set_pieces(self) -> None:
        let_to_piece : dict[str,Piece] = {'a' : Rook, 'b' : Knight, 'c' : Bishop, 'd' : Queen, 
                               'e' : King, 'f' : Bishop, 'g' : Knight, 'h' : Rook}
        for letter in Convert.letter_to_num.keys():
            for num,color in {'1':'WHITE','8':'BLACK'}.items():
                coord = letter + num
                self.board_dict[coord] = let_to_piece[letter](color,coord)

class Pawn(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    moved = False

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
        return legal_moves
    
    def movement_rules(self,board : Board) -> list:
        legal_moves = []
        two_coord = None
        if self.color == 'WHITE':
            one_coord = self.coord[0] + str(int(self.coord[1]) + 1)
            if not self.moved:
                two_coord = self.coord[0] + str(int(self.coord[1]) + 2)

        elif self.color == 'BLACK':
            one_coord = self.coord[0] + str(int(self.coord[1]) - 1)
            if not self.moved:
                two_coord = self.coord[0] + str(int(self.coord[1]) - 2)

        if board.board_dict[one_coord] == None: legal_moves.append(one_coord)
        if two_coord != None:
            if board.board_dict[two_coord] == None: legal_moves.append(two_coord)
        return legal_moves

    def capture_rules(self,board : Board) -> list:
        legal_moves = []
        if self.color == 'WHITE':
            one_coord = self.coord[0] + str(int(self.coord[1]) + 1)

        elif self.color == 'BLACK':
            one_coord = self.coord[0] + str(int(self.coord[1]) - 1)

        left_attack_coord = (Convert.num_to_letter[Convert.letter_to_num[self.coord[0]] - 1]) + one_coord[1]
        right_attack_coord = (Convert.num_to_letter[Convert.letter_to_num[self.coord[0]] + 1]) + one_coord[1]

        if left_attack_coord[1] != 0 and board.board_dict[left_attack_coord] != None and board.board_dict[left_attack_coord].color != self.color: legal_moves.append(left_attack_coord) 
        if right_attack_coord[1] != 8 and board.board_dict[right_attack_coord] != None and board.board_dict[right_attack_coord].color != self.color: legal_moves.append(right_attack_coord)
        return legal_moves

    def en_passant_rules(self,board : Board,last_board : Board) -> list:
        legal_moves = []
        try:
            moved = piece_moved(board,last_board)
        except:
            return legal_moves
        if str(moved[0]) == 'PAWN':
            if abs(Convert.letter_to_num[moved[0].coord[0]] - Convert.letter_to_num[moved[1][0]]) == 2:
                #Last move was a pawn double move
                letter = moved[0].coord[0]
                number = str((moved[0].coord[1] + moved[1]) // 2)
                legal_moves.append(letter + number)
                return legal_moves

class Knight(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    def __str__(self):
        return 'KNIGHT'
    
    def rules(self):
        pass

class Bishop(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    def __str__(self):
        return 'BISHOP'
    
    def rules(self):
        pass

class Rook(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    def __str__(self):
        return 'ROOK'
    
    def rules(self):
        pass

class Queen(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    def __str__(self):
        return 'QUEEN'
    
    def rules(self,board : Board,last_board : Board):
        pass

class King(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

    def __str__(self):
        return 'KING'
    
    def rules(self):
        pass

class Screen:
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 500

    SCREEN = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

    name = 'Chess'
    file_root = 'C:/Users/Elliot/Specific Projects/Python-Games/Chess/'

    bg = pygame.image.load(file_root + 'BOARD_WHITE.png').convert_alpha()
    icon = pygame.image.load(file_root + 'PIECE_WHITE_PAWN.png').convert_alpha()

    pygame.display.set_caption(name)
    pygame.display.set_icon(icon)

    def draw_bg(self) -> None:
        scaled_bg = pygame.transform.scale(self.bg,(self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.SCREEN.blit(scaled_bg,(0,0))
        
    def draw_pieces(self,board : Board) -> None:
        for coord,piece in board.board_dict.items():
            if piece != None:
                x = BoardImgSizes.TEXT_BUFFER + ((Convert.letter_to_num[coord[0]] - 1) * BoardImgSizes.SQ_SIZE) + (Convert.letter_to_num[coord[0]])
                y = BoardImgSizes.BLANK_BUFFER + ((8 - int(coord[1])) * BoardImgSizes.SQ_SIZE) + (8 - int(coord[1])) + 2.5
                rect = pygame.Rect(x,y,BoardImgSizes.SQ_SIZE,BoardImgSizes.SQ_SIZE)
                scaled = pygame.transform.scale(piece.image,(BoardImgSizes.SQ_SIZE - 5,BoardImgSizes.SQ_SIZE - 5))
                self.SCREEN.blit(scaled,rect)

    def draw_held(self,held : Piece):
        if held != None:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            
            rect = pygame.Rect(x,y,BoardImgSizes.SQ_SIZE,BoardImgSizes.SQ_SIZE)
            scaled = pygame.transform.scale(held.image,(BoardImgSizes.SQ_SIZE - 5,BoardImgSizes.SQ_SIZE - 5))
            self.SCREEN.blit(scaled,rect)

    def screen_run(self,board : Board , held : Piece) -> None:
        self.draw_bg()
        self.draw_pieces(board)
        self.draw_held(held)
            
def coord_clicked(x,y) -> tuple:
    'Gets the location on the chess board of where you clicked'
    #Letter

    if x not in range(BoardImgSizes.TEXT_BUFFER, Screen.SCREEN_WIDTH - BoardImgSizes.BLANK_BUFFER):
        return None
    
    letter = -(((BoardImgSizes.SQ_SIZE * 8) // Screen.SCREEN_WIDTH - (x - BoardImgSizes.TEXT_BUFFER)) // BoardImgSizes.SQ_SIZE)

    if letter - 1 not in range(8):
        return None

    letter = Convert.num_to_letter[letter]

    #Number

    if y not in range(BoardImgSizes.BLANK_BUFFER, Screen.SCREEN_HEIGHT - BoardImgSizes.TEXT_BUFFER):
        return None
    
    number = 9 + (((BoardImgSizes.SQ_SIZE * 8) // Screen.SCREEN_HEIGHT - (y - BoardImgSizes.BLANK_BUFFER)) // BoardImgSizes.SQ_SIZE)

    if number - 1 not in range(8):
        return None
    
    coord = letter + str(number)
    return coord

def playerInp(board : Board,held : Piece,color : str,last_board : Board) -> Piece:
    delay = False
    if pygame.mouse.get_pressed()[0]:
        coord = coord_clicked(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        piece = board.board_dict[coord]
        if piece != None and piece.color == color:
            #Picking up a piece
            held = piece
            board.change_board(coord,None)
        
        if held:
            #Putting down a piece
            if rules := held.rules(board,last_board):
                if coord in rules:
                    board.change_board(coord,held)
                    held.coord = coord
                    if str(held) == 'PAWN':
                        held.moved = True
                    held = None
                    delay = True
                    color = Convert.color_change[color]
    
    return held,color,delay

def piece_moved(board : Board, last_board : Board):
    coords = []
    for spot, piece in board.board_dict.items():
        if str(last_board.board_dict[spot]) != str(piece):
            coords.append(spot)

    assert len(coords) == 2, 'Didn\'t find moved piece'
    return coords

def run():
    game_board = Board()
    last_board = Board()
    screen = Screen()
    running = True
    game_clock = pygame.time.Clock()
    FPS = 30
    held = None
    color = 'WHITE'
    delay = False
    delay_count = 0
    while running:
        game_clock.tick(FPS)
        screen.screen_run(game_board,held)
        if not delay:
            held , color , delay = playerInp(game_board, held,color, last_board)
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