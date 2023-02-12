import pygame
import string
pygame.init()


    
class Board:
    SCREEN_LENGTH = 500
    SCREEN_HEIGHT = 500
    board_dict = {}
    rect_dict = {}
    blankBuffer = 23
    textBuffer = 39
    BOARD_LENGTH = SCREEN_LENGTH - blankBuffer - textBuffer
    BOARD_HEIGHT = SCREEN_HEIGHT - blankBuffer - textBuffer
    SQLENGTH = BOARD_LENGTH / 8
    SQHEIGHT = BOARD_HEIGHT / 8
    letterNumDict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

    def createBoard(self):   
        """Creates the board dictionary and sets up all the coordinates"""
        letterCoord = string.ascii_lowercase[:8]
        for letter in letterCoord:
            for number in range(1,9):
                snum = str(number)
                coord = letter + snum
                self.board_dict[coord] = None
                x = self.textBuffer + (self.letterNumDict[coord[0]] * self.SQLENGTH) + 5
                y = self.blankBuffer + ((8 - int(coord[1])) * self.SQHEIGHT) + 5
                self.rect_dict[coord] = pygame.Rect(x,y,self.SQLENGTH,self.SQHEIGHT)

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
                num = '2'
            case 'BLACK':
                num = '7'
        letterList = ['a','b','c','d','e','f','g','h']

        for iter in range(8):
            coord = letterList[iter] + num
            piece = color + '_' + 'PAWN'
            self.change(coord,piece)

def setup():
    global board,selected
    board = Board()
    board.createBoard()
    board.setBoardFront()
    selected = False
    
def draw_board():
    boardImage = pygame.image.load('c:/Users/Elliot/Specific Projects/Python-Games/Chess/ChessBoardWHITE.png').convert_alpha()
    scaled_boardImage = pygame.transform.scale(boardImage,(SCREEN_LENGTH,SCREEN_HEIGHT))
    SCREEN.blit(scaled_boardImage,(0,0))

def draw_pieces():
    """Draws the pieces to the board"""
    for coord,value in board.board_dict.items():
        if value == None:
            continue
        img = pygame.image.load('c:/Users/Elliot/Specific Projects/Python-Games/Chess/{}.png'.format(value))
        rect : pygame.Rect = board.rect_dict[coord]
        scaled_img = pygame.transform.scale(img,(rect.width - 10,rect.height - 10))
        SCREEN.blit(scaled_img,(rect.x,rect.y))

    if selected:
        x,y = pygame.mouse.get_pos()
        img = pygame.image.load('c:/Users/Elliot/Specific Projects/Python-Games/Chess/{}.png'.format(selection))
        scaled_img = pygame.transform.scale(img,(rect.width - 10,rect.height - 10))
        SCREEN.blit(scaled_img,(x,y))

def coordClicked(x,y) -> str:
    numToLetter = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
    num = 8 - (((y - board.textBuffer) // board.SQHEIGHT))
    letter = numToLetter[(((x - board.textBuffer) // board.SQLENGTH) + 1)]
    coord = letter + str(int(num))
    print(coord)
    return coord

def playerInputCheck():
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] in range(board.textBuffer,board.BOARD_LENGTH + board.textBuffer + 1):
            global selected,selection
            x,y = pygame.mouse.get_pos()
            coord = coordClicked(x,y)
            if board.board_dict[coord] != None:
                if board.board_dict[coord].split('_')[0] == 'BLACK':
                    selected = True
                    selection = board.board_dict[coord]
                    print(selection)

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
        playerInputCheck()
        draw_board()
        draw_pieces()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()