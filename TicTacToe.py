#Tic Tac Toe
#Imports 
import random
import copy

#Classes
class Board:
    def __init__(self):
        self.strstart = '\x1b['
        self.strred = '31'
        self.strgreen = '32'
        self.strwhite = '37'
        self.strblackbg = ';40m'
        self.strundline = '4;'
        self.strbold = '1;'
        self.strclose = '0m'
        self.spotlist = []
        self.donePlaying = False
        global wcx
        global wco
        self.winner = None
        wcx = False
        wco = False

    def donePrompt(self):
        while True:
            dp = input('Do you want to play again.  ')
            if dp == 'Yes' or dp == 'yes':
                self.donePlaying = False
                break
            elif dp == 'No' or dp == 'no':
                self.donePlaying = True
                break
            else:
                print('\nPlease input "Yes" or "No".\n')
        
    def setBoard(self):
        self.spotlist = []
        for num in range(1,10):
            self.spotlist.append(num)

    def repCheck(self):
        tempspotlist = list(set(self.spotlist))
        if '0' in tempspotlist:
            tempspotlist.remove('0')
        if 'X' in tempspotlist:
            tempspotlist.remove('X')
        return tempspotlist

    def change(self,num,letter):
        if num + 1 in self.spotlist:
            self.spotlist[num] = letter

    def printBoard(self):
        print('\n')
        count = 0
        for numindex in range(9):
            listval = self.spotlist[numindex]
            if not count == 2:
                end = True
            else:
                end = False
            if not wcx or wco:
                #Check if spot has been chosen or not
                if type(listval) == int:
                    if end:
                        #Check mid of line
                        print(self.strstart + self.strundline + self.strwhite + self.strblackbg + str(listval) + self.strstart + self.strclose,end='_|_')
                    else:
                        #Check end of line
                        print(self.strstart + self.strundline + self.strwhite + self.strblackbg + str(listval) + self.strstart + self.strclose)
                else:
                    #Prints red and bolded if prints letter
                    if end:
                        #Checks mid of line
                        print(self.strstart + self.strundline + self.strbold + self.strred + self.strblackbg + str(listval) + self.strstart + self.strclose, end= '_|_')
                    else:
                        #Checks end of line
                        print(self.strstart + self.strundline + self.strbold + self.strred + self.strblackbg + str(listval) + self.strstart + self.strclose)
            else:
                #prints green letters on win because direct list has already been changed to the green letters 
                if end:
                    print(listval,end='_|_')
                else:
                    print(listval)
            if end:                
                count += 1
            else:
                count = 0

    def endCheck_front(self,playerX,playerO):
        wcx,wco = self.winCheck_back_main()
        if len(winningNums) > 1:
            for winningNum in winningNums:
                self.spotlist[winningNum] = self.strstart + self.strundline + self.strbold + self.strgreen + self.strblackbg + self.spotlist[winningNum] + self.strstart + self.strclose
            if wcx:
                self.winCheck_wrapup('X',playerX)
                wcx = False
                return self.donePlaying

            if wco:
                self.winCheck_wrapup('0',playerO)
                wco = False
                return self.donePlaying
        
        if self.tieCheck():
            self.printBoard()
            self.setBoard()
            print('\nTie Game\n')
            scorePrint()
            self.donePrompt()
            return self.donePlaying
        return None

    def winCheck_wrapup(self,letter,player):
        self.winner = letter
        self.printBoard()
        self.setBoard()
        print('\n{} has won this round\n'.format(player.name))
        player.scoreIncrement()
        scorePrint()
        self.donePrompt()
            
    def winCheck_back_main(self):
        global winningNums
        winx = False
        wino = False
        winningNums = []
        #Row Check
        for row in range(3): 
            if self.spotlist[row*3] == self.spotlist[row*3+1] == self.spotlist[row*3+2]: 
                if self.spotlist[row*3+1] == 'X':
                    winx = True
                    wino = False
                    winningNums = [row*3, row*3+1, row*3+2]
                    break
                if self.spotlist[row*3+1] == '0':
                    winx = False
                    wino = True
                    winningNums = [row*3, row*3+1, row*3+2]
                    break
        #Column Check
        for column in range(3):
            if self.spotlist[column] == self.spotlist[column+3] == self.spotlist[column+6]:
                if self.spotlist[column] == 'X':
                    winx = True
                    wino = False
                    winningNums = [column,column+3,column+6]
                    break
                if self.spotlist[column] == '0':                    
                    winx = False
                    wino = True
                    winningNums = [column,column+3,column+6]
                    break
        #Diagonal top left to bottom right check        
        if self.spotlist[0] == self.spotlist[4] == self.spotlist[8]:
            if self.spotlist[0] == 'X':
                winx = True
                wino = False
            if self.spotlist[0] == '0':
                winx = False
                wino = True
            winningNums = [0,4,8]
        #Diagonal top right to bottom left check
        if self.spotlist[2] == self.spotlist[4] == self.spotlist[6]:
            if self.spotlist[2] == 'X':
                winx = True
                wino = False
            if self.spotlist[2] == '0':
                winx = False
                wino = True
            winningNums = [2,4,6]
        return winx,wino     
                    
    def tieCheck(self):
        if len(self.repCheck()) == 0:
        #If tie
            return True
        return False

    def __del__(self):
        print('\nThanks for playing')

class Player:
    def __init__(self,name,letter):
        self.score = 0
        self.name = name
        self.letter = letter
        self.choice = None

    def choiceToBoard(self):
        board.change(self.choice,self.letter)
    
    def scoreIncrement(self):
        if board.winner == self.letter:
            self.score += 1
            board.winner = None

class Person(Player):
    def choiceGetter(self):
        while True:
            board.printBoard()
            self.choice = input('\n\n{}, Choose a spot\n'.format(self.name))
            try:
                self.choice = int(self.choice)
            except:
                print('\nGive a viable number\n\n')
                continue
            if self.choice not in board.repCheck():
                print('\nGive a viable number\n\n')
                continue
            self.choice -= 1
            break
        
class EasyAI(Player):
    def choiceGetter(self):
        self.choice = random.choice(board.repCheck())
        self.choice -= 1

class HardAI(Player):
    temp_board = None
    def choiceGetter(self):
        self.choice = self.optimalMove()
        self.choice -= 1

    def minimax(self,depth : int,isMaximizing : bool):
        if depth == 0 or self.winningMove() or self.blockWin():
            scores_result = {'tie':0,'win':1,'loss':-1}
            if self.tieCheck():
                return scores_result['tie']

            elif self.winningMove():
                return scores_result['win']

            elif self.blockWin():
                return scores_result['loss']


        if isMaximizing:
            best_score = -1000
            moves = [move for move in self.temp_board if isinstance(move,int)]
            print(moves)
            for move in moves:
                print(move)
                og = copy.copy(self.temp_board[move])
                self.temp_board[move] = self.letter
                score = self.minimax(depth - 1,False)
                best_score = max(score,best_score)
                self.temp_board[move] = og
            return best_score

        else:
            worst_score = 1000
            moves = [move for move in self.temp_board if isinstance(move,int)]
            print(moves,'Not maximizing')
            for move in moves:
                print(move)
                og = copy.copy(self.temp_board[move])
                self.temp_board[move] = self.letter
                score = self.minimax(depth - 1,True)
                worst_score = min(score,worst_score)
                self.temp_board[move] = og
            return worst_score

    def winningMove(self):
        #check rows
        winningMoves = []
        for row in range(3):
                row *= 3
                #checks every combination
                for num1,num2,num3 in [0,1,2],[1,2,0],[2,0,1]:
                    if board.spotlist[row + num1] == board.spotlist[row + num2] == self.letter and type(board.spotlist[row + num3]) == int:
                        winningMoves.append(board.spotlist[row + num3])
        #checks columns
        for column in range(3):
            #checks every combination
            for num1,num2,num3 in [0,3,6],[3,6,0],[6,0,3]:
                    if board.spotlist[column + num1] == board.spotlist[column + num2] == self.letter and type(board.spotlist[column + num3]) == int:
                        winningMoves.append(board.spotlist[column + num3])
        #checks diagonals
    
        #checks first diagonal
        for num1,num2,num3 in [0,4,8],[4,8,0],[8,0,4]:
            if board.spotlist[num1] == board.spotlist[num2] == self.letter and type(board.spotlist[num3]) == int:
                        winningMoves.append(board.spotlist[num3])
        #checks second diagonal
        for num1,num2,num3 in [2,4,6],[4,6,2],[6,2,4]:
            if board.spotlist[num1] == board.spotlist[num2] == self.letter and type(board.spotlist[num3]) == int:
                        winningMoves.append(board.spotlist[num3])
                        
        return winningMoves
    
    def blockWin(self):
        blockMoves = []
        for row in range(3):
                row *= 3
                #checks every combination
                for num1,num2,num3 in [0,1,2],[1,2,0],[2,0,1]:
                    if board.spotlist[row + num1] == board.spotlist[row + num2] != self.letter and type(board.spotlist[row + num3]) == int:
                        blockMoves.append(board.spotlist[row + num3])
        #checks columns
        for column in range(3):
            #checks every combination
            for num1,num2,num3 in [0,3,6],[3,6,0],[6,0,3]:
                    if board.spotlist[column + num1] == board.spotlist[column + num2] != self.letter and type(board.spotlist[column + num3]) == int:
                        blockMoves.append(board.spotlist[column + num3])
        #checks diagonals
    
        #checks first diagonal
        for num1,num2,num3 in [0,4,8],[4,8,0],[8,0,4]:
            if board.spotlist[num1] == board.spotlist[num2] != self.letter and type(board.spotlist[num3]) == int:
                        blockMoves.append(board.spotlist[num3])
        #checks second diagonal
        for num1,num2,num3 in [2,4,6],[4,6,2],[6,2,4]:
            if board.spotlist[num1] == board.spotlist[num2] != self.letter and type(board.spotlist[num3]) == int:
                        blockMoves.append(board.spotlist[num3])
                        
        return blockMoves                        

    def corners(self):
        cornerList = []
        count = 0
        for spot in board.spotlist:
            if count in [0,2,6,8]:
                if type(spot) is int:
                    cornerList.append(spot)
            count += 1
        return cornerList

    def optimalMove(self):
        self.temp_board = board.spotlist.copy()
        best_score = -1000
        moves = [move for move in self.temp_board if isinstance(move,int)]
        for move in moves:
            og = copy.copy(self.temp_board[move])
            self.temp_board[move] = self.letter
            score = self.minimax(20,False)
            best_score = max(score,best_score)
            if best_score != -1000:
                best_move = move
            self.temp_board[move] = og
        return best_move

    def tieCheck(self):
        if not self.temp_board:
            return

        tempspotlist = list(set(self.temp_board))
        if '0' in tempspotlist:
            tempspotlist.remove('0')
        if 'X' in tempspotlist:
            print(tempspotlist)
            tempspotlist.remove('X')
        return tempspotlist


#Functions
def turns(firstP):
    if player1.letter == 'X':
        playerX = player1
        playerO = player2
    else:
        playerX = player2
        playerO = player1 

    t = firstP
    if t == 1:
        nextP = 2
    else:
        nextP = 1
    while not board.donePlaying:
        if t == 1:
            player1.choiceGetter()
            player1.choiceToBoard()
            status = board.endCheck_front(playerX,playerO)
            t = 2
            if not status is None:
            #if someone won, restart the game with player2 going first
                t = nextP
                nextP = 1
                continue
        if t == 2:
            player2.choiceGetter()
            player2.choiceToBoard()
            status = board.endCheck_front(playerX,playerO)
            if not status is None:
            #if someone won, restart the game with player2 going first
                t = nextP
                nextP = 2
            else:
                t = 1
                
def intro():
    print('Tic Tac Toe\nby Elliot Adam\n\n')
    while True:
        try:
            dif = int(input('Would you like to go play\n1.Player vs Player\n2.Player vs Easy AI\n3.Player vs Hard AI\n'))
        except:
            print('\nPlease input 1, 2, or 3')
            continue
        if dif not in [1,2,3]:
            print('Please input a 1, 2, or 3')
            continue
        return dif

def starterRequest():
    while True:
        starter = input('Who goes first\n1.Player\n2.AI\n3.Random\n')
        try:
            starter = int(starter)
        except:
            print('Please input 1, 2, or 3')
        if starter not in [1,2,3]:
            print('Please input 1, 2, or 3')
            continue
        break
    return starter
    
def scorePrint():
    print("{}'s Score: {} , {}'s Score: {}\n\n".format(player1.name,player1.score,player2.name,player2.score))

#Game Mode Functions
def playerVPlayer():
    global player1
    global player2
    while True:
        p1name = input('Player 1, input your name. ')
        if len(p1name) < 1:
            print('Insert a name please')
            continue
        break

    while True:
        p2name = input('Player 2, input your name. ')
        if len(p1name) < 1:
            print('Insert a name please')
            continue
        break

    player1 = Person(p1name,'X')
    player2 = Person(p2name,'0')
    turns(1)

def playerVEasyAI():
    global player1
    global player2
    while True:
        p1name = input('Player 1, input your name. ')
        if len(p1name) < 1:
            print('Insert a name please')
            continue
        break
    
    p2name = 'Computer'
    
    pfirst = 0
    starter = starterRequest()
    #Randomnly making variable starter 1 or 2 if the user chose random
    if starter == 3:
        starter = random.choice([1,2])
    if starter == 1:
        p1letter = 'X'
        p2letter = '0'
        pfirst = 1
    if starter == 2:
        p1letter = '0'
        p2letter = 'X'
        pfirst = 2
    
    player1 = Person(p1name,p1letter)
    player2 = EasyAI(p2name,p2letter)
    turns(pfirst)
        
def playerVHardAI():
    global player1
    global player2
    while True:
        p1name = input('Player 1, input your name. ')
        if len(p1name) < 1:
            print('Insert a name please')
            continue
        break
    
    p2name = 'Hard Computer'
    
    pfirst = 0
    starter = starterRequest()
    #Randomnly making variable starter 1 or 2 if the user chose random
    
    if starter == 3:
        starter = random.choice([1,2])
    if starter == 1:
        p1letter = 'X'
        p2letter = '0'
        pfirst = 1
    if starter == 2:
        p1letter = '0'
        p2letter = 'X'
        pfirst = 2
    
    player1 = Person(p1name,p1letter)
    player2 = HardAI(p2name,p2letter)
    turns(pfirst)
        
#Main Game Code
if __name__ == '__main__':
    global board
    board = Board()
    board.setBoard()
    dif = intro()
    if dif == 1:
        playerVPlayer()
    if dif == 2:
        playerVEasyAI()
    if dif == 3:
        playerVHardAI()