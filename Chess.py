import pygame
from pygame import mixer
import string
import copy

pygame.init()
mixer.init()

#Encapsulations of variables
class InputVars:
    #Probably going to implement a drag feature later
    held = False

class Sounds:
    PIECE_DROP = mixer.Sound('Chess/SOUND_PIECE_DROPPING.m4a')
    PIECE_PICK_UP = mixer.Sound('Chess/SOUND_PIECE_TAKEING.m4a')
    PROMOTION = mixer.Sound('Chess/SOUND_PROMOTION.m4a')
    CASTLING = mixer.Sound('Chess/SOUND_CASTLING.m4a')

    @staticmethod
    def s_volume_change(soundFromSelf : pygame.mixer.Sound, volume : float):
        soundFromSelf.set_volume(volume)

class Convert:
    numToLetter = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
    letterNumDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

#Game Related Classes
class Piece:
    selectedCoord : str = None
    def __init__(self,color,name,coord):
        self.color : str = color
        self.name : str = name
        self.coord : str = coord
        self.image : str = f'PIECE_{self.color}_{self.name}'
        if self.name == 'ROOK' or self.name == 'KING':
            self.castleBool = True
        else:
            self.castleBool = False

    def rules(self,chosenPiece):
        """Returns list of all the coordinates where the piece can move to; has a match case for all the rules of the pieces"""
        match self.name:
            case 'PAWN':
                possibleMoves = self.pawnRules(chosenPiece)
                                
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
    def pawnRules(self,chosenPiece) -> list:
        #Pawn Logic for taking
        possibleMoves = []
        if chosenPiece is not None:
            pawnTake = self.pawnTaking()
            if pawnTake:
                possibleMoves.extend(pawnTake)
                            
        else:
            #Pawn logic for moving and en passant
            #If on starting square pawn can move two squares
            pawnMove = self.pawnMoving()
            if pawnMove:
                possibleNums = pawnMove.copy()

            #En passant stuff
            enPassant = self.enPassant()
            if enPassant:
                possibleMoves.extend(enPassant)
                    
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
                    if board.board_dict[newCoord] is not None:
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
                    if board.board_dict[newCoord] is not None:
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
        if len(self.castling()) > 0:
            possibleMoves.extend(self.castling())

        return possibleMoves


    #All special rules into functions
    def castling(self) -> list:
        if self.name == 'KING':
            #You can only run castling if you are a king piece
            possibleMoves = []
            for num in ['1','8']:
                #First runs through the white rooks on a1 and h1 and then the black rooks on a8 and h8
                for piece in [board.board_dict['a' + num],board.board_dict['h' + num]]:
                    #Checks castling bools and ensures that there is a piece in the spot
                    if piece == None or piece.name != 'ROOK':
                        #print('PIECE NOT RECOGNIZED')
                        continue

                    elif piece.castleBool:
                        #All the white rooks that haven't moved yet
                        if piece.coord[0] > self.coord[0]:
                            #Rook on h1
                            if board.board_dict['f' + num] == None and board.board_dict['g' + num] == None:
                                #Ensuring f and g squares are open for short castling
                                possibleMoves.append('g' + num)
                    
                        else:
                            #Rook on a1
                            if board.board_dict['b' + num] == None and board.board_dict['c' + num] == None and board.board_dict['d' + num] == None:
                                #Ensuring d and c and b squares are open for long castling
                                possibleMoves.append('c' + num)

            return possibleMoves

    def enPassant(self) -> list:
        #Should probably return a string as you can only ever have one en passant at a time but
        #I like keeping the convention of having the functions return a list
        possibleMoves = []
        if not checkStartingPos():
            #ensures that this isn't the first move
            #GUARD CLAUSES
            if lastPiece.name != 'PAWN':
                return

            if not (abs(int(lastCoord[1]) - int(lastPiece.coord[1])) == 2):
                #If piece didn't move 2 spaces
                return

            if not selected:
                return

            if not (abs(Convert.letterNumDict[selection.selectedCoord[0]] - Convert.letterNumDict[lastPiece.coord[0]]) == 1):
                #If piece isn't next to my current held piece
                return
            
            if not (selection.selectedCoord[1] == lastPiece.coord[1]):
                return

            #Guard clause summary
            #If there was an enemy pawn that just moved 2 spaces and is now right next to my pawn
            #...  that I have selected , then do all the code in here
            letter = lastPiece.coord[0]
            if lastPiece.color == 'WHITE':
                num = int(lastPiece.coord[1]) - 1

            else:
                num = int(lastPiece.coord[1]) + 1

            coord = letter + str(num)
            possibleMoves.append(coord)
        return possibleMoves
                 
    def promotion(self) -> None:
        """Blits to the screen the promotion window"""
        rect : pygame.Rect = copy.deepcopy(board.rect_dict[self.coord])
        rectoffset = -3
        rect.x = copy.deepcopy(board.rect_dict[self.coord].x) + rectoffset
        rect.y = copy.deepcopy(board.rect_dict[self.coord].y) + rectoffset
        pygame.draw.rect(SCREEN,(255,255,255),rect)
        imgsizeoffset = 5
        for num,img in enumerate(['QUEEN','ROOK','KNIGHT','BISHOP'],start= 1):
            newimgstr = f'Chess/PIECE_{self.color}_{img}.png'
            newimg = pygame.image.load(newimgstr)
            scaled_img = pygame.transform.scale(newimg,(rect.width / 2 - imgsizeoffset ,rect.height / 2 - imgsizeoffset))
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
                                    if board.board_dict[newCoord] is not None:
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

    #Pawn logic functions
    def pawnTaking(self) -> list:
        """All possible taking moves for pawns"""
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
        for possible in possibleMoves:
            if board.board_dict[possible] is None:
                #Removes the taking moves where there is nothing; cant take nothing
                possibleMoves.remove(possible)
                
        print('RETURNING FROM TAKE',possibleMoves)
        return possibleMoves

    def pawnMoving(self) -> list:
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

        return possibleNums

    #Static functions
    @staticmethod
    def s_castleCorres(coord):
        """Grabs which rook to change and which rook to make from the new king coordinate"""
        if coord[0] == 'g':
            #Short castle
            newRook = Piece(selection.color,'ROOK','f' + coord[1])
            newRook.castleBool = False
            board.board_dict['f' + coord[1]] = newRook
            #Make a new rook that cant castle in the correct place
            del board.board_dict['h' + coord[1]]
            board.board_dict['h' + coord[1]] = None
            #Delete the old rook

        if coord[0] == 'c':
            #Long castle
            newRook = Piece(selection.color,'ROOK','d' + coord[1])
            newRook.castleBool = False
            board.board_dict['d' + coord[1]] = newRook
            #Make a new rook that cant castle in the correct place
            del board.board_dict['a' + coord[1]]
            board.board_dict['a' + coord[1]] = None
            #Delete the old rook

        mixer.Sound.play(Sounds.CASTLING)

    @staticmethod
    def s_enPassantCorres(coord):
        """Deletes the above or behind pawn"""
        letter = coord[0]
        if selection.color == 'WHITE':
            num = int(coord[1]) - 1
        else:
            num = int(coord[1]) + 1
        
        deletedCoord = letter + str(num)
        del board.board_dict[deletedCoord]
        board.board_dict[deletedCoord] = None

##Singleton
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
    global board,selected,playerVal,inCheckbool,inCheckcolor,checkingPiece
    global promotion,promotingPiece, checkedKing
    playerVal = 'WHITE'
    board = Board()
    selected = False
    inCheckbool = False
    inCheckcolor = None
    checkingPiece = None
    checkedKing = None
    promotion = False
    promotingPiece = None
    Sounds.s_volume_change(Sounds.PIECE_DROP,0.5)
    Sounds.s_volume_change(Sounds.PIECE_PICK_UP,0.2)
    
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
    num = int(8 - ((y - board.blankBuffer) // board.SQHEIGHT))
    #Get the number by reversing the distance from the start of the board to the end of the board and dividing
    #By the square size to end up with the number between 1 and 8
    letter = Convert.numToLetter[(((x - board.textBuffer) // board.SQLENGTH) + 1)]
    #Pretty much same thing down here except it gets converted back into a letter
    
    coord = letter + str(num)
    return coord

def quarterCoordClicked(x : int,y : int, coord: str) -> str:
    """Used to find what portion of the square the player clicked during a promotion"""
    rect : pygame.Rect = board.rect_dict[coord]
    possible = ['QUEEN','KNIGHT','ROOK','BISHOP']
    if x > (rect.x + (rect.width / 2)):
        #In second half of rectangle
        possible.remove('QUEEN')
        possible.remove('KNIGHT')
        if y > (rect.y + (rect.height / 2)):
            #Bottom Right
            possible.remove('ROOK')

        else:
            #Top Right
            possible.remove('BISHOP')

    else:
        #In first half of rectangle
        possible.remove('ROOK')
        possible.remove('BISHOP')
        if y > (rect.y + (rect.height / 2)):
            #Bottom Left
            possible.remove('QUEEN')

        else:
            #Top Left
            possible.remove('KNIGHT')

    assert len(possible) == 1, 'More than one option legal'
    return possible[0]

def sideChange(color : str) -> None:
    global playerVal,selected,lastCoord,lastPiece
    if color == 'WHITE':
        playerVal = 'BLACK'
    else:
        playerVal = 'WHITE'
    lastCoord = selection.selectedCoord
    lastPiece = selection
    selection.selectedCoord = None
    selected = False

def playerInputLogic(color : str) -> None:
    global playerVal,selected,selection,lastCoord,lastPiece, promotion, promotingPiece
    #selection gets defined in here
    #selection = Piece object of the piece that the player is currently holding
    if pygame.mouse.get_pressed()[0] and not InputVars.held:
        #Picks up a piece when you either press down or lift up the mouse button 
        InputVars.held = True
        xrange = range(board.textBuffer,board.BOARD_LENGTH + board.textBuffer + 1)
        yrange = range(board.blankBuffer,board.blankBuffer + board.BOARD_HEIGHT + 1)
        if pygame.mouse.get_pos()[0] in xrange and pygame.mouse.get_pos()[1] in yrange:
            x,y = pygame.mouse.get_pos()
            coord = coordClicked(x,y)
            if int(coord[1]) not in range(1,9):
                return

            if promotion:
                if coord == promotingPiece.coord:
                    selectedPiece = quarterCoordClicked(x,y,coord)
                    del board.board_dict[coord]
                    board.board_dict[coord] = Piece(board.board_dict[coord].color,selectedPiece,coord)
                    promotion = False
                    promotingPiece = None

            chosenPiece = board.board_dict[coord]

            if selected:
                #Putting down a piece if holding a piece
                if coord == selection.selectedCoord:
                    #You can put a piece back without it switching turns
                    board.change(coord,selection)
                    selected = False
                    return   
                #Selection is the piece object that the player is currently holding
                possibleMoves = legalMoves(color,board.board_dict[coord])
                if selection.name == 'PAWN':
                    possibleMoves.extend(legalMoves(color,None))
                for possible in possibleMoves:
                    if chosenPiece == None or chosenPiece.color != color:
                        if coord == possible:
                            #Castling stuff
                            if selection.name == 'KING' and (coord in selection.castling()):
                                #If player chose to castle, move the king and rook accordingly
                                Piece.s_castleCorres(possible)

                            #En passant stuff
                            if selection.name == 'PAWN' and selection.enPassant() and (coord in selection.enPassant()):
                                #If player chose to en passant, remember to delete the piece
                                Piece.s_castleCorres(possible)

                            #Makes it so that a moved rook/king can't castle
                            if selection.name == 'ROOK' or selection.name == 'KING':
                                selection.castleBool = False
                            mixer.Sound.play(Sounds.PIECE_DROP)
                            board.change(coord,selection)
                            sideChange(color)    
                            break
                else:
                    #Code for what happens if the chosen spot isn't legal
                    #Puts back the piece
                    mixer.Sound.play(Sounds.PIECE_PICK_UP)
                    board.change(selection.selectedCoord,selection)
                    selected = False
                    selection = None
            else:
                if board.board_dict[coord] is not None:
                    #Grabbing a piece, when you don't have one; only runs if there is a piece in that square
                    if chosenPiece.color == color:
                        selected = True
                        selection = chosenPiece
                        chosenPiece.selectedCoord = coord 
                        board.change(coord,None)

    if selected:
        moves = legalMoves(color,None)
        if selection.name == 'PAWN':
            moves.extend(legalMoves(selection.color,selection.opposite()))
        highlightMoves(moves)

def legalMoves(color : str,chosenPiece : Piece) -> list:
    global inCheckbool,inCheckcolor,checkingPiece
    if not inCheckbool:
        checkInfo = checked()
        if checkInfo[0]:
            inCheckbool = True
            checkingPiece = checkInfo[1]
            inCheckcolor = checkingPiece.opposite()


    if not (inCheckbool and inCheckcolor == color):
        possibleMoves = selection.rules(chosenPiece)

    else:
        #Code for what happens if you are in check
        possibleMoves = []
        for coord,piece in board.board_dict.items():
            if piece == None or piece.color == checkingPiece.color:
                continue

            piece.selectedCoord = coord
            movesOfPieceTake : list = piece.rules(Piece(color,None,None))
            movesOfPieceMove : list = piece.rules(Piece(None,None,None))
            #Now we have a list of all the possible moves this piece could make
            for move in movesOfPieceTake:
                if move == checkingPiece.coord:
                    #See if you can take the piece
                    possibleMoves.append(move)
                
            for move in movesOfPieceMove:
                #See if you can get in the way of the check
                moves = checkedKing.blockCheck()
                if move in moves:
                    #print('APPENDING',piece.name + piece.coord, move)
                    possibleMoves.append(move)
                    
    return possibleMoves        
                
def highlightMoves(inputList : list) -> None:
    smalldotimg = pygame.image.load('Chess/DOT_SMALL.png')
    bigdotimg = pygame.image.load('Chess/DOT_BIG.png')
    for move in inputList:
        #Move = coordinate like h3
        if board.board_dict[move] is None:
            if selection.name == 'PAWN':
                assert move[1] == selection.selectedCoord[1], 'PRINTING ILLEGAL TAKES'
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
                if board.board_dict[move] is None:
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

def checkStartingPos() -> bool:
    startingPos = True
    for letter in string.ascii_lowercase[:8]:
        for num in string.digits[4:7]:
            coord = letter + num
            if board.board_dict[coord] is not None:
                startingPos = False

    return startingPos

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
    
    assert pygame.get_init(), 'ERROR INITIATING MODULES'
    setup()
    while isRunning:
        draw_board()
        playerInputLogic(playerVal)
        draw_pieces()
        if selected:
            print(legalMoves(selection.opposite(),selection))
        if promotion:
            promotingPiece.promotion()
        
        if not pygame.mouse.get_pressed()[0]:
            InputVars.held = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()