import pygame
from pygame import mixer
import string
pygame.init()
mixer.init()

    
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

    def __init__(self):
        self.createBoard()
        self.setBoardFront()
        

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
        pieceList = ['ROOK','KNIGHT','BISHOP','QUEEN','KING','BISHOP','KNIGHT','ROOK']

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
    global board,selected,playerVal,startingPos_dict
    playerVal = 'WHITE'
    board = Board()
    startingPos = Board()
    startingPos_dict = startingPos.board_dict
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
    num = 8 - (((y - board.blankBuffer) // board.SQHEIGHT))
    letter = numToLetter[(((x - board.textBuffer) // board.SQLENGTH) + 1)]
    coord = letter + str(int(num))
    return coord

def sideChange(color):
    global playerVal,selected,lastCoord,lastPiece
    if color == 'WHITE':
        playerVal = 'BLACK'
    else:
        playerVal = 'WHITE'
    lastCoord = selectedCoord
    lastPiece = selection
    selected = False

def playerInputLogic(color):
    global playerVal,selected,selection,selectedCoord,lastCoord,lastPiece
    
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] in range(board.textBuffer,board.BOARD_LENGTH + board.textBuffer + 1) and pygame.mouse.get_pos()[1] in range(board.blankBuffer,board.blankBuffer + board.BOARD_HEIGHT + 1):
            x,y = pygame.mouse.get_pos()
            coord = coordClicked(x,y)
            if selected:
                mixer.music.load('c:/Users/Elliot/Specific Projects/Python-Games/Chess/PIECE_DROPPING.m4a')
                mixer.music.play()
                #Putting down a piece if holding a piece
                numToLetter = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
                letterNumDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
                piece = selection.split('_')[1]
                if coord == selectedCoord:
                    #You can put a piece back without it switching turns
                    board.change(coord,selection)
                    selected = False
                    return

                if piece == 'PAWN':
                    #Pawn Logic for taking
                    if board.board_dict[coord] != None:
                        if board.board_dict[coord].split('_')[0] != color:
                            #Can only take if not the same color
                            letterNum = letterNumDict[selectedCoord[0]]
                            if color == 'WHITE':
                                num = int(selectedCoord[1]) + 1
                            else:
                                num = int(selectedCoord[1]) - 1

                            if letterNum != 1 or letterNum != 8:
                                adjacent = [numToLetter[letterNum + 1],numToLetter[letterNum - 1]]
                            else:
                                if letterNum == 1:
                                    adjacent = [numToLetter[2],None]
                                else:
                                    adjacent = [numToLetter[7],None]
                                
                            for possible in adjacent:
                                if possible != None:
                                    if coord == f'{possible}{num}':
                                        board.change(coord,selection)
                                        sideChange(color)
                                        return
                            
                    else:
                        #Pawn logic for moving and en passant
                        #If on starting square pawn can move two squares
                        if color == 'WHITE':
                            if selectedCoord[1] == '2':
                                possibleNums = [int(selectedCoord[1]) + 1, int(selectedCoord[1]) + 2]
                            else:
                                possibleNums = [int(selectedCoord[1]) + 1,None]
                        else:
                            if selectedCoord[1] == '7':
                                possibleNums = [int(selectedCoord[1]) - 1, int(selectedCoord[1]) - 2]
                            else:
                                possibleNums = [int(selectedCoord[1]) - 1,None]

                        #En passant stuff - Not completed
                        #print(startingPos_dict,board.board_dict)
                        if startingPos_dict.values != board.board_dict.values:
                            print(lastCoord,lastPiece)
                            #If not in starting position because then there will be no previous coordinate or piece
                            if lastPiece.split('_')[1] == 'PAWN' and (lastCoord[1] == '7' or lastCoord[1] == '2'):
                                 #If last piece was a pawn and pawn was on 7 or 2
                                 print(lastPiece, lastCoord)
                                 return 

                        #Moving logic for pawns; accounts for opening double move
                        letter = selectedCoord[0]
                        for possible in possibleNums:
                            if possible != None:
                                if coord == f'{letter}{possible}':
                                    board.change(coord,selection)
                                    sideChange(color)
                                    return
            
                if piece == 'KNIGHT':
                    #Knight Logic
                    letterNum = letterNumDict[selectedCoord[0]]
                    possibleMoves = [] #List of strings for possible moves
                    for possible in [1,2,-1,-2]:
                        try:
                            letter = numToLetter[letterNum + possible]
                            num = int(((possible / possible) * (3 - abs(possible))) + int(selectedCoord[1])) 
                            #    gets positivity of possible     gets inverted(2 to 1, 1 to 2)
                            possibleMoves.append(letter + str(num))
                        except KeyError:
                            pass
                    print(possibleMoves)

                    for move in possibleMoves:
                        if coord == move:
                            if board.board_dict[coord] == None or board.board_dict[coord].split('_')[0] != color:
                                board.change(coord,selection)
                                sideChange(color)
                                return
                    return

            if board.board_dict[coord] != None:
                #Grabbing a piece; only runs if there is a piece in that square
                if board.board_dict[coord].split('_')[0] == color:
                    selected = True
                    selection = board.board_dict[coord]
                    selectedCoord = coord
                    board.change(coord,None)
                    

            
                

if __name__ == '__main__':
    CLOCK = pygame.time.Clock()
    FPS = 10

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
        playerInputLogic(playerVal)
        draw_board()
        draw_pieces()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()