import pygame
pygame.init()

from abc import abstractmethod
from abc import abstractproperty
from Playground import dictSwapper

class Convert:
    letter_to_num = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
    num_to_letter = dictSwapper(letter_to_num)

class Piece:
    def __init__(self,color : str,coord : str):
        self.coord = coord
        self.color = color
        self.image = f'PIECE_{color.upper}_{self}'

    @abstractmethod
    def rules(self):
        ...

    @abstractproperty
    def value(self):
        ...

class Board:
    def __init__(self) -> None:
        self.board_dict = Board.set_board_dict()
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

    def change_board(self,piece : Piece) -> None:
        self.board_dict[piece.coord]

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

    def __str__(self):
        return 'PAWN'
    
    def rules(self, board : Board):
        pass

class Knight(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

class Bishop(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

class Rook(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

class Queen(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

class King(Piece):
    def __init__(self, color: str, coord: str):
        super().__init__(color, coord)

class Screen:
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 500

    SCREEN = pygame.display.set_mode((self.SCREEN_HEIGHT,self.SCREEN_WIDTH))

    name = 'Chess'
    file_root = 'C:/Users/Elliot/Specific Projects/Python-Games/Chess/'

    bg = pygame.image.load(file_root + 'BOARD_WHITE.png').convert_alpha()
    icon = pygame.image.load(file_root + 'PIECE_WHITE_PAWN.png').convert_alpha()

    pygame.display.set_caption(name)
    pygame.display.set_icon(icon)

    def draw_bg(self):
        scaled_bg = pygame.transform.scale(self.bg,(self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.SCREEN.blit(scaled_bg,(0,0))
        
    def draw_pieces(board : Board):
        pass

def run():
    game_board = Board()
    running = True
    game_clock = pygame.time.Clock()
    FPS = 30
    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
        game_clock.tick(FPS)
    
if __name__ == '__main__':
    run()