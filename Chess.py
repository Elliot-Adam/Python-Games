import pygame
import string
pygame.init()


    
class Board:
    board_dict = {}

    def createBoard(self):
        """Creates the board dictionary and sets up all the coordinates"""
        letterCoord = string.ascii_lowercase[:8]
        for letter in letterCoord:
            for number in range(1,9):
                snum = str(number)
                coord = letter + snum
                self.board_dict[coord] = None

    def change(self,coord:str,piece:str):
        """The coordinate should be like h4 or e5 while the piece will be the name of the image file so like
        WHITE_PAWN or BLACK_QUEEN"""
        self.board_dict[coord] = piece

    def setBoardFront(self):
        self.setBoardPieces('WHITE')
        self.setBoardPawns('WHITE')

        self.setBoardPieces('BLACK')
        self.setBoardPawns('BLACK')

    def setBoardPieces(self,color):
        """Actually sets up the pieces on the board for the game"""
        letterList = ['a','b','c','d','e','f','g','h']
        pieceList = ['ROOK','BISHOP','KNIGHT','QUEEN','KING','BISHOP','KNIGHT','ROOK']

        match color:
            case 'WHITE':
                num = '1'
            case 'BLACK':
                num = '8'

        for iter in range(8):
            coord = letterList[iter] + num
            piece = color + '_' + pieceList[iter]
            self.change(coord,piece)

    def setBoardPawns(self,color):
        """Sets up all the pawns"""
        match color:
            case 'WHITE':
                num = '1'
            case 'BLACK':
                num = '8'
        letterList = ['a','b','c','d','e','f','g','h']

        for iter in range(8):
            coord = letterList[iter] + num
            piece = color + '_' + 'PAWN'
            self.change(coord,piece)

def setup():
    global board
    board = Board()
    board.createBoard()
    board.setBoardFront()

def draw():
    draw_board()
    draw_pieces()

def draw_board():
    boardImage = pygame.image.load('c:/Users/Elliot/Specific Projects/Python-Games/Chess/ChessBoard.png').convert_alpha()
    scaled_boardImage = pygame.transform.scale(boardImage,(SCREEN_LENGTH,SCREEN_HEIGHT))
    SCREEN.blit(scaled_boardImage,(0,0))

def draw_pieces():
    leftBuffer = 39
    rightBuffer = 23

    HEIGHT = SCREEN_HEIGHT / 8 - 10
    LENGTH = SCREEN_LENGTH - leftBuffer - rightBuffer/ 8 
    letterNumDict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    for coord,value in board.board_dict.items():
        if value == None:
            continue
        x = (letterNumDict[coord[0]] * LENGTH) + leftBuffer
        y = (8 - int(coord[1])) * HEIGHT
        img = pygame.image.load('c:/Users/Elliot/Specific Projects/Python-Games/Chess/{}.png'.format(value)).convert()
        scaled_img = pygame.transform.scale(img,(SCREEN_LENGTH/8 - 25,SCREEN_HEIGHT/8 - 25))
        rect = scaled_img.get_rect()
        rect.x = x
        rect.y = y
        SCREEN.blit(scaled_img,rect)

if __name__ == '__main__':
    CLOCK = pygame.time.Clock()
    FPS = 20

    SCREEN_LENGTH = 500
    SCREEN_HEIGHT = 500
    name = 'Chess'
    icon = pygame.image.load('c:/Users/Elliot/Specific Projects/Python-Games/Chess/WHITE_PAWN.png')

    SCREEN = pygame.display.set_mode((SCREEN_LENGTH,SCREEN_HEIGHT))
    pygame.display.set_caption(name)
    pygame.display.set_icon(icon)
    isRunning = True
    setup()
    while isRunning:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()