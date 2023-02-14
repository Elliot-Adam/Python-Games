import pygame
from pygame import mixer
import string
pygame.init()
mixer.init()

class Sounds:
    PIECE_DROP = mixer.Sound('Chess/PIECE_DROPPING.m4a')

class Convert:
    numToLetter = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
    letterNumDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

class Piece:
    selectedCoord = None
    def __init__(self,color,name,coord):
        self.color = color
        self.name = name
        self.coord = coord
        self.image = f'{self.color}_{self.name}'

    def rules(self,coord,chosenColor):
        match self.name:
            case 'PAWN':
                possibleMoves = self.pawnRules(coord,chosenColor)
                                
            case 'KNIGHT':
                possibleMoves = self.knightRules()
            
            case 'BISHOP':
                possibleMoves = self.bishopRules()                    
                
            case 'ROOK':
                possibleMoves = self.rookRules()

            case 'QUEEN':
                possibleMoves = self.queenRules()
        
            case 'KING':
                possibleMoves = self.kingRules()

        return possibleMoves

    def pawnRules(self,coord,chosenColor) -> list:
        #Pawn Logic for taking
        if chosenColor != None:
            if chosenColor != self.color:
                #Can only take if not the same color
                letterNum = Convert.letterNumDict[self.selectedCoord[0]]
                if self.color == 'WHITE':
                    num = int(self.selectedCoord[1]) + 1
                else:
                    num = int(self.selectedCoord[1]) - 1
                try:
                    adjacent = [Convert.numToLetter[letterNum + 1],Convert.numToLetter[letterNum - 1]]
                except KeyError:
                    try:
                        adjacent = [Convert.numToLetter[letterNum + 1]]
                    except KeyError:
                        adjacent = [Convert.numToLetter[letterNum - 1]]

                possibleMoves = [value + str(num) for value in adjacent]
                            
        else:
            #Pawn logic for moving and en passant
            #If on starting square pawn can move two squares
            if self.color == 'WHITE':
                if self.selectedCoord[1] == '2' and board.board_dict[self.selectedCoord[0] + str(int(self.selectedCoord[1]) + 1)] == None:
                    possibleNums = [int(self.selectedCoord[1]) + 1, int(self.selectedCoord[1]) + 2]
                else:
                    possibleNums = [int(self.selectedCoord[1]) + 1]
            else:
                if self.selectedCoord[1] == '7' and board.board_dict[str(self.selectedCoord[0] + str(int(self.selectedCoord[1]) - 1))] == None:
                    possibleNums = [int(self.selectedCoord[1]) - 1, int(self.selectedCoord[1]) - 2]
                else:
                    possibleNums = [int(self.selectedCoord[1]) - 1]

            #En passant stuff - Not completed
            #print(startingPos_dict,board.board_dict)
            if startingPos_dict.values != board.board_dict.values:
                print(lastPiece,lastCoord)
                #If not in starting position because then there will be no previous coordinate or piece
                if lastPiece.split('_')[1] == 'PAWN' and (lastCoord[1] == '7' or lastCoord[1] == '2'):
                    #If last piece was a pawn and pawn was on 7 or 2
                    print(lastPiece, lastCoord)
                    
            #Moving logic for pawns; accounts for opening double move
            letter = self.selectedCoord[0]
            possibleMoves = [letter + str(num) for num in possibleNums]

        return possibleMoves

    def knightRules(self) -> list:
        #Knight Logic
        letterNum = Convert.letterNumDict[self.selectedCoord[0]]
        possibleMoves = [] #List of strings for possible moves
        for possible in [1,2,-1,-2]:
            try:
                letter = Convert.numToLetter[letterNum + possible]
                num = int(3 - abs(possible))
                #    gets inverted(2 to 1, 1 to 2)

                posNum = str(int(self.selectedCoord[1]) + num)
                negNum = str(int(self.selectedCoord[1]) - num)

                legal = [1,2,3,4,5,6,7,8]
                
                if int(posNum) in legal:
                    possibleMoves.append(letter + posNum)
                
                if int(negNum) in legal:
                    possibleMoves.append(letter + negNum)

            except KeyError:
                pass
        
        return possibleMoves
            
    def bishopRules(self) -> list:
        #Logic for bishop moving/taking
        possibleMoves = []
        for letterinc,numinc in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            diagBool = True
            letterNum = Convert.letterNumDict[self.selectedCoord[0]]
            num = int(self.selectedCoord[1])
            while diagBool:
                try:
                    #Move in that diagonal
                    letterNum += letterinc
                    num += numinc
                    if not 1 <= num <= 8:
                        #If diagonal goes off board
                        break

                    newCoord = Convert.numToLetter[letterNum] + str(num)
                    if board.board_dict[newCoord] != None:
                        #If theres a piece in the intended spot
                        diagBool = False
                        

                    possibleMoves.append(newCoord)
                    
                except KeyError:
                    pass

        return possibleMoves

    def rookRules(self) -> list:
        #Logic for rook movement and captures
        possibleMoves = []
        for letterinc,numinc in [(0,1),(1,0),(-1,0),(0,-1)]:
            lineBool = True
            letterNum = Convert.letterNumDict[self.selectedCoord[0]]
            num = int(self.selectedCoord[1])
            while lineBool:
                try:
                    #Move in that direction; straight line
                    letterNum += letterinc
                    num += numinc
                    if not (1 <= num <= 8) or not (1 <= letterNum <= 8):
                        #If straight line goes off board
                        break

                    newCoord = Convert.numToLetter[letterNum] + str(num)
                    if board.board_dict[newCoord] != None:
                        #If theres a piece in the intended spot
                        lineBool = False
                        

                    possibleMoves.append(newCoord)
                    
                except KeyError:
                    pass
        
        return possibleMoves

    def queenRules(self) -> list:
        possibleMoves = []
        possibleMoves.extend(self.bishopRules())
        possibleMoves.extend(self.rookRules())
        return possibleMoves

    def kingRules(self) -> list:
        #King movement
        possibleMoves = []
        letterNum = Convert.letterNumDict[self.selectedCoord[0]]
        num = int(self.selectedCoord[1])
        
        possibleLetters = [letterNum, letterNum + 1,letterNum - 1]
        possibleNums = [num, num + 1,num - 1]
        for letter in possibleLetters:
            if not 1 <= letter <= 8:
                continue
            for num in possibleNums:
                if not 1 <= num <= 8:
                    continue
                possibleMoves.append(str(Convert.numToLetter[letter]) + str(num))

        possibleMoves.remove(selectedCoord)
        return possibleMoves

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
                x = self.textBuffer + ((Convert.letterNumDict[coord[0]] - 1) * self.SQLENGTH) + 5
                y = self.blankBuffer + ((8 - int(coord[1])) * self.SQHEIGHT) + 5
                self.rect_dict[coord] = pygame.Rect(x,y,self.SQLENGTH,self.SQHEIGHT)

    def change(self,coord:str,piece:Piece):
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
            piece = Piece(color,pieceList[iter],coord)
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
            piece = Piece(color,'PAWN',coord)
            self.change(coord,piece)

def setup():
    global board,selected,playerVal,startingPos_dict,wKc,wQc,bKc,bQc
    playerVal = 'WHITE'
    board = Board()
    startingPos = Board()
    startingPos_dict = startingPos.board_dict
    selected = False
    wKc = True
    wQc = True
    bKc = True
    bQc = True
    
def draw_board():
    boardImage = pygame.image.load('Chess/ChessBoardWHITE.png').convert_alpha()
    scaled_boardImage = pygame.transform.scale(boardImage,(SCREEN_LENGTH,SCREEN_HEIGHT))
    SCREEN.blit(scaled_boardImage,(0,0))

def draw_pieces():
    """Draws the pieces to the board"""
    for coord,value in board.board_dict.items():
        if value == None:
            continue
        img = pygame.image.load('Chess/{}.png'.format(value.image))
        rect : pygame.Rect = board.rect_dict[coord]
        scaled_img = pygame.transform.scale(img,(rect.width - 10,rect.height - 10))
        SCREEN.blit(scaled_img,(rect.x,rect.y))

    if selected:
        highlightLegalMoves()
        x,y = pygame.mouse.get_pos()
        img = pygame.image.load('Chess/{}.png'.format(selection.image))
        scaled_img = pygame.transform.scale(img,(rect.width - 10,rect.height - 10))
        SCREEN.blit(scaled_img,(x,y))

def coordClicked(x,y) -> str:
    num = 8 - ((y - board.blankBuffer) // board.SQHEIGHT)
    #Get the number by reversing the distance from the start of the board to the end of the board and dividing
    #By the square size to end up with the number between 1 and 8
    letter = Convert.numToLetter[(((x - board.textBuffer) // board.SQLENGTH) + 1)]
    #Pretty much same thing down here except it gets converted back into a letter
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
        xrange = range(board.textBuffer,board.BOARD_LENGTH + board.textBuffer + 1)
        yrange = range(board.blankBuffer,board.blankBuffer + board.BOARD_HEIGHT + 1)
        if pygame.mouse.get_pos()[0] in xrange and pygame.mouse.get_pos()[1] in yrange:
            x,y = pygame.mouse.get_pos()
            coord = coordClicked(x,y)
            if board.board_dict[coord] != None:
                #If the chosen spot isn't empty, grab the color of the piece you clicked
                chosenColor = board.board_dict[coord].color

            else:
                chosenColor = None


            if selected:
                #Putting down a piece if holding a piece
                if coord == selectedCoord:
                    #You can put a piece back without it switching turns
                    board.change(coord,selection)
                    selected = False
                    return   
                #Selection is the piece object that the player is currently holding
                possibleMoves = selection.rules(coord,chosenColor)
                for possible in possibleMoves:
                    if chosenColor != color:
                        if coord == possible:
                            mixer.Sound.play(Sounds.PIECE_DROP)
                            board.change(coord,selection)
                            sideChange(color)    
                            break
                else:
                    #Code for what happens if the chosen spot isn't legal
                    pass
            
            else:
                if board.board_dict[coord] != None:
                    #Grabbing a piece, when you don't have one; only runs if there is a piece in that square
                    if chosenColor == color:
                        selected = True
                        selection = board.board_dict[coord]
                        board.board_dict[coord].selectedCoord = coord 
                        selectedCoord = coord
                        board.change(coord,None)

def highlightLegalMoves():
    possibleMoves : list = selection.rules(selection.color,selection.selectedCoord)
    if selection.name == 'PAWN': 
        possibleMoves.extend(selection.pawnRules(None,None))
    dot = pygame.image.load('Chess/dot.png')
    for move in possibleMoves:
        #Move = coordinate like h3
        if board.board_dict[move] == None or board.board_dict[move].color != selection.color:
            rect : pygame.Rect = board.rect_dict[move]
            dot = pygame.transform.scale(dot,(rect.width - 10,rect.height - 10))
            SCREEN.blit(dot,rect)

def checked():
    for coord,piece in board.board_dict.items():
        possibleMoves : list = piece.rules(piece.color,coord)
        if selection.name == 'PAWN': 
            possibleMoves.extend(piece.pawnRules(None,None))
        #Now we have a list of all the possible moves this piece could make
        for move in possibleMoves:
            if board.board_dict[move] == None:
                continue

            if board.board_dict[move].color == piece.color:
                continue

            if board.board_dict[move].name != 'KING':
                continue

            #Now we have all the moves that could take the king next turn
            print('Checked')


if __name__ == '__main__':
    CLOCK = pygame.time.Clock()
    FPS = 13

    clientCount = 0

    SCREEN_LENGTH = 500
    SCREEN_HEIGHT = 500
    name = 'Chess'
    icon = pygame.image.load('Chess/WHITE_PAWN.png')

    SCREEN = pygame.display.set_mode((SCREEN_LENGTH,SCREEN_HEIGHT))
    pygame.display.set_caption(name)
    pygame.display.set_icon(icon)
    isRunning = True
    setup()
    while isRunning:
        playerInputLogic(playerVal)
        draw_board()
        draw_pieces()
        checked()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()