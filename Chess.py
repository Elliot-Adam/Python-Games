import pygame
from pygame import mixer
import string
pygame.init()
mixer.init()

class Sounds:
    PIECE_DROP = mixer.Sound('Chess/SOUND_PIECE_DROPPING.m4a')
    PIECE_TAKE = mixer.Sound('Chess/SOUND_PIECE_TAKEING.m4a')
    PROMOTION = mixer.Sound('Chess/SOUND_PROMOTION.m4a')
    CASTLING = mixer.Sound('Chess/SOUND_CASTLING.m4a')

class Convert:
    numToLetter = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
    letterNumDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

class Piece:
    selectedCoord : str = None
    def __init__(self,color,name,coord):
        self.color : str = color
        self.name : str = name
        self.coord : str = coord
        self.image : str = f'PIECE_{self.color}_{self.name}'
        if self.name == 'ROOK':
            self.castleBool = True
        else:
            self.castleBool = False

    def rules(self,chosenColor : str):
        """Returns list of all the coordinates where the piece can move to; has a match case for all the rules of the pieces"""
        match self.name:
            case 'PAWN':
                possibleMoves = self.pawnRules(chosenColor)
                                
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

    #Functions to determine which piece can move where;
    #Could probably be moved outside of the class,
    #but I think it looks neater
    def pawnRules(self,chosenColor : str) -> list:
        #Pawn Logic for taking
        possibleMoves = []
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

        possibleMoves.remove(self.selectedCoord)
        return possibleMoves


    #All special rules into functions
    def castling(self):
        if self.name == 'KING':
            #You can only run castling if you are a king piece
            possibleMoves = []
            if self.color == 'WHITE':
                for piece in [board.board_dict['a1'],board.board_dict['h1']]:
                    #Checks castling bools and ensures that there is a piece in the spot
                    if piece == None or piece.name != 'ROOK':
                        continue
                    elif piece.castlingBool:
                        #All the white rooks that haven't moved yet
                        if piece.coord[0] > self.coord[0]:
                            #Rook on h1
                            if board.board_dict['f1'] == None and board.board_dict['g1'] == None:
                                possibleMoves.append('g1')
                                board.board_dict['f1'] = piece
                                mixer.Sound.play(Sounds.CASTLING)
                            
                        else:
                            #Rook on a1
                            if board.board_dict['b1'] == None and board.board_dict['c1'] == None and board.board_dict['d1'] == None:
                                possibleMoves.append('c1')
                                board.board_dict['d1'] = piece
                                mixer.Sound.play(Sounds.CASTLING)

    def enPassant(self):
        pass

    def promotion(self):
        rect : pygame.Rect = board.rect_dict[self.coord] 
        pygame.draw.rect(SCREEN,(255,255,255),rect)
        for num,img in enumerate(['QUEEN','ROOK','KNIGHT','BISHOP'],start= 1):
            newimgstr = f'Chess/{self.color}_{img}.png'
            newimg = pygame.image.load(newimgstr)
            scaled_img = pygame.transform.scale(newimg,(rect.width / 2 ,rect.height / 2))
            width , height = (rect.width / 2),(rect.height / 2)
            topLrect = pygame.Rect(rect.x,rect.y,width,height)
            topRrect = pygame.Rect(rect.x + width,rect.y,width,height)
            bottomLrect = pygame.Rect(rect.x,rect.y + height,width,height)
            bottomRrect = pygame.Rect(rect.x + width,rect.y + height,width,height)
            match num:
                case 1:
                #Top Left
                    newRect = topLrect
                case 2:
                #Top Right
                    newRect = topRrect

                case 3:
                #Bottom Left
                    newRect = bottomLrect
                
                case 4:
                #Bottom Right
                    newRect = bottomRrect

            SCREEN.blit(scaled_img,newRect)

    #Other functions
    def opposite(self):
        if self.color == 'WHITE':
            return 'BLACK'
        else:
            return 'WHITE'

    def blockCheck(self):
        if self.name == 'KING' and inCheckcolor == self.color:
            #Can only use it if you are a king in check
            if checkingPiece.name != 'KNIGHT' and checkingPiece != 'PAWN':
                #Can only block if piece isn't a knight or a pawn
                match checkingPiece.name:
                    case 'BISHOP':
                        #Copied from rules; modified a bit
                        for letterinc,numinc in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                            diagMoves = []
                            found = False
                            letterNum = Convert.letterNumDict[checkingPiece.selectedCoord[0]]
                            num = int(checkingPiece.selectedCoord[1])
                            while not found:
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
                                        newPiece = board.board_dict[newCoord]
                                        if newPiece.name == 'KING' and newPiece.color != checkingPiece.color:
                                            #If hitting our king
                                            found = True
                                            break
                                        

                                    diagMoves.append(newCoord)
                                    
                                except KeyError:
                                    pass
                            
                            if found:
                                break

                            else:
                                diagMoves.clear()

                        return diagMoves
                    
                    case 'ROOK':
                        #Logic for rook movement and captures
                        for letterinc,numinc in [(0,1),(1,0),(-1,0),(0,-1)]:
                            lineMoves = []
                            found = False
                            letterNum = Convert.letterNumDict[checkingPiece.selectedCoord[0]]
                            num = int(checkingPiece.selectedCoord[1])
                            while not found:
                                try:
                                    #Move in that direction; straight line
                                    letterNum += letterinc
                                    num += numinc
                                    if not (1 <= num <= 8) or not (1 <= letterNum <= 8):
                                        #If straight line goes off board
                                        break

                                    newCoord = Convert.numToLetter[letterNum] + str(num)
                                    newPiece = board.board_dict[newCoord]
                                    if newPiece.name == 'KING' and newPiece.color != checkingPiece.color:
                                            #If hitting our king
                                            found = True
                                            break
                                        

                                    lineMoves.append(newCoord)
                                    
                                except KeyError:
                                    pass
                                    
                            if found:
                                break

                            else:
                                lineMoves.clear()

                        return lineMoves
                    
                    case 'QUEEN':
                        #Copied from bishop / rook
                        for letterinc,numinc in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                            #Bishop stuff
                            diagMoves = []
                            found = False
                            letterNum = Convert.letterNumDict[checkingPiece.selectedCoord[0]]
                            num = int(checkingPiece.selectedCoord[1])
                            while not found:
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
                                        newPiece = board.board_dict[newCoord]
                                        if newPiece is None:
                                            continue

                                        if newPiece.name == 'KING' and newPiece.color != checkingPiece.color:
                                            #If hitting our king
                                            found = True
                                            break
                                        

                                    diagMoves.append(newCoord)
                                    
                                except KeyError:
                                    pass
                            
                            if found:
                                break

                            else:
                                diagMoves.clear()

                        for letterinc,numinc in [(0,1),(1,0),(-1,0),(0,-1)]:
                                lineMoves = []
                                found = False
                                letterNum = Convert.letterNumDict[checkingPiece.selectedCoord[0]]
                                num = int(checkingPiece.selectedCoord[1])
                                while not found:
                                    try:
                                        #Move in that direction; straight line
                                        letterNum += letterinc
                                        num += numinc
                                        if not (1 <= num <= 8) or not (1 <= letterNum <= 8):
                                            #If straight line goes off board
                                            break

                                        newCoord = Convert.numToLetter[letterNum] + str(num)
                                        newPiece = board.board_dict[newCoord]
                                        if newPiece is None:
                                            continue

                                        if newPiece.name == 'KING' and newPiece.color != checkingPiece.color:
                                                #If hitting our king
                                                found = True
                                                break
                                            

                                        lineMoves.append(newCoord)
                                        
                                    except KeyError:
                                        pass

                                if found:
                                    break
                                
                                else:
                                    lineMoves.clear()

                        moves = diagMoves[:]
                        moves.extend(lineMoves)
                        return moves                            

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
        global promotion,promotingPiece
        if self.board_dict[coord] != None:
            mixer.Sound.play(Sounds.PIECE_TAKE)
        else:
            mixer.Sound.play(Sounds.PIECE_DROP)
        self.board_dict[coord] = piece
        if isinstance(piece,Piece):
            piece.coord = coord
            #Code for promotion
            if piece.name == 'PAWN':
                if piece.coord[1] == '8' or piece.coord[1] == '1':
                    #8 and 1 are impossible to get to if you are the same color
                    promotion = True
                    promotingPiece = piece
                    mixer.Sound.play(Sounds.PROMOTION)

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

def setup() -> None:
    global board,selected,playerVal,startingPos_dict,inCheckbool,inCheckcolor,checkingPiece
    global promotion,promotingPiece, checkedKing
    playerVal = 'WHITE'
    board = Board()
    startingPos = Board()
    startingPos_dict = startingPos.board_dict
    selected = False
    inCheckbool = False
    inCheckcolor = None
    checkingPiece = None
    checkedKing = None
    promotion = False
    promotingPiece = None
    
def draw_board() -> None:
    boardImage = pygame.image.load('Chess/BOARD_WHITE.png').convert_alpha()
    scaled_boardImage = pygame.transform.scale(boardImage,(SCREEN_LENGTH,SCREEN_HEIGHT))
    SCREEN.blit(scaled_boardImage,(0,0))

def draw_pieces() -> None:
    """Draws the pieces to the board"""
    for coord,value in board.board_dict.items():
        if value == None:
            continue
        img = pygame.image.load('Chess/{}.png'.format(value.image))
        rect : pygame.Rect = board.rect_dict[coord]
        scaled_img = pygame.transform.scale(img,(rect.width - 10,rect.height - 10))
        SCREEN.blit(scaled_img,(rect.x,rect.y))

    if selected:
        x,y = pygame.mouse.get_pos()
        img = pygame.image.load('Chess/{}.png'.format(selection.image))
        scaled_img = pygame.transform.scale(img,(rect.width - 10,rect.height - 10))
        SCREEN.blit(scaled_img,(x,y))

def coordClicked(x : int,y : int) -> str:
    """Grabs the coordinate on the chess board based on the input"""
    num = 8 - ((y - board.blankBuffer) // board.SQHEIGHT)
    #Get the number by reversing the distance from the start of the board to the end of the board and dividing
    #By the square size to end up with the number between 1 and 8
    letter = Convert.numToLetter[(((x - board.textBuffer) // board.SQLENGTH) + 1)]
    #Pretty much same thing down here except it gets converted back into a letter
    coord = letter + str(int(num))
    return coord

def sideChange(color : str) -> None:
    global playerVal,selected,lastCoord,lastPiece
    if color == 'WHITE':
        playerVal = 'BLACK'
    else:
        playerVal = 'WHITE'
    lastCoord = selection.selectedCoord
    lastPiece = selection
    selected = False

def playerInputLogic(color : str) -> None:
    global playerVal,selected,selection,lastCoord,lastPiece
    #selection gets defined in here
    #selection = Piece object of the piece that the player is currently holding
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
                if coord == selection.selectedCoord:
                    #You can put a piece back without it switching turns
                    board.change(coord,selection)
                    selected = False
                    return   
                #Selection is the piece object that the player is currently holding
                possibleMoves = legalMoves(color,chosenColor)
                for possible in possibleMoves:
                    if possible in selection.rules(None) or possible in selection.rules(color):
                        if chosenColor != color:
                            if coord == possible:
                                board.change(coord,selection)
                                sideChange(color)    
                                break
                else:
                    #Code for what happens if the chosen spot isn't legal
                    #Puts back the piece
                    selected = False
                    board.change(selection.selectedCoord,selection)
                    selection = None
            else:
                if board.board_dict[coord] != None:
                    #Grabbing a piece, when you don't have one; only runs if there is a piece in that square
                    if chosenColor == color:
                        selected = True
                        selection = board.board_dict[coord]
                        board.board_dict[coord].selectedCoord = coord 
                        board.change(coord,None)

    if selected:
        moves = legalMoves(color,None)
        if selection.name == 'PAWN':
            moves.extend(legalMoves(selection.color,selection.opposite()))
        highlightMoves(moves)

def legalMoves(color : str,chosenColor : str) -> list:
    global inCheckbool,inCheckcolor,checkingPiece
    if not inCheckbool:
        checkInfo = checked()
        if checkInfo[0]:
            inCheckbool = True
            checkingPiece = checkInfo[1]
            inCheckcolor = checkingPiece.opposite()


    if not (inCheckbool and inCheckcolor == color):
        possibleMoves = selection.rules(chosenColor)
        

    else:
        #Code for what happens if you are in check
        possibleMoves = []
        for coord,piece in board.board_dict.items():
            if piece == None or piece.color == checkingPiece.color:
                continue

            piece.selectedCoord = coord
            movesOfPieceTake : list = piece.rules(color)
            movesOfPieceMove : list = piece.rules(None)
            #Now we have a list of all the possible moves this piece could make
            for move in movesOfPieceTake:
                if move == checkingPiece.coord:
                    #See if you can take the piece
                    possibleMoves.append(move)
                
            for move in movesOfPieceMove:
                #See if you can get in the way of the check
                moves = checkedKing.blockCheck()
                if move in moves:
                    print('APPENDING',piece.name + piece.coord, move)
                    possibleMoves.append(move)
                    
    return possibleMoves        
                
def highlightMoves(inputList : list) -> None:
    smalldotimg = pygame.image.load('Chess/DOT_SMALL.png')
    bigdotimg = pygame.image.load('Chess/DOT_BIG.png')
    for move in inputList:
        #Move = coordinate like h3
        if board.board_dict[move] == None:
            rect : pygame.Rect = board.rect_dict[move]
            smalldot = pygame.transform.scale(smalldotimg,(rect.width - 10,rect.height - 10))
            SCREEN.blit(smalldot,rect)
        
        elif board.board_dict[move].color != selection.color:
            offset = 5
            rect : pygame.Rect = board.rect_dict[move].copy()
            rect.x -= offset
            rect.y -= offset
            bigdot = pygame.transform.scale(bigdotimg,(rect.width,rect.height))
            SCREEN.blit(bigdot,rect)

def checked() -> tuple:
    global checkedKing
    for coord,piece in board.board_dict.items():
        if piece != None:
            piece.selectedCoord = coord
            possibleMoves : list = piece.rules(piece.color)
            if piece.name == 'PAWN': 
                possibleMoves.extend(piece.pawnRules(None))
            #Now we have a list of all the possible moves this piece could make
            for move in possibleMoves:
                if board.board_dict[move] == None:
                    continue

                if board.board_dict[move].color == piece.color:
                    continue

                if board.board_dict[move].name != 'KING':
                    continue
                
                #Now we have all the moves that could take the king next turn
                checkedKing = board.board_dict[move]
                return (True,piece)
    return (False,Piece(None,None,None))
        
def coveredMoves(color) -> list:
    possibleMoves = []
    for piece in board.board_dict.values():
        if piece.color == color:
            possibleMoves.extend(piece.rules(None))

    return possibleMoves

if __name__ == '__main__':
    CLOCK = pygame.time.Clock()
    FPS = 14

    clientCount = 0

    SCREEN_LENGTH = 500
    SCREEN_HEIGHT = 500
    name = 'Chess'
    icon = pygame.image.load('Chess/PIECE_WHITE_PAWN.png')

    SCREEN = pygame.display.set_mode((SCREEN_LENGTH,SCREEN_HEIGHT))
    pygame.display.set_caption(name)
    pygame.display.set_icon(icon)
    isRunning = True
    setup()
    while isRunning:
        draw_board()
        playerInputLogic(playerVal)
        draw_pieces()
        if promotion:
            promotingPiece.promotion()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()