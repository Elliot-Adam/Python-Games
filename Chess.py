import pygame
pygame.init()

from abc import abstractmethod
from abc import abstractproperty

class Board:
    board_dict = {}

class Convert:
    letter_to_num = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
    num_to_letter = {}
    for k,v in letter_to_num.values():
        num_to_letter[v] = k

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

class Pawn(Piece):
    def __str__(self):
        return 'PAWN'
    
    def rules(self, board : Board)

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Rook(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

    



def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
    
if __name__ == '__main__':
    run()