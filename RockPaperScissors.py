#Rock Paper Scisssors
#Imports
import random
import time
from abc import abstractmethod
class Shape:
    class Rock:
        image = '''
       ,--.--._  
------" _, \___) 
        / _/____)
        \ /(____)
------\     (__) 
       `-----"   
'''

        def __gt__(self,other):
            if isinstance(other,Shape.Scissors):
                return True
            
            return False
        
        def __lt__(self,other):
            if isinstance(other,Shape.Paper):
                return True
            
            return False
        
        def __str__(self):
            return 'Rock'
        
    class Scissors:
        image = '''
             
 __       ,/'
(__).  ,/'   
 __  ::      
(__)'  `\.   
          `\.
''' 

        def __gt__(self,other):
            if isinstance(other,Shape.Paper):
                return True
            
            return False
        
        def __lt__(self,other):
            if isinstance(other,Shape.Rock):
                return True
            
            return False
        
        def __str__(self):
            return 'Scissors'
        
    class Paper:
        image = '''
     _________
    /        /
   /        / 
  /        /  
 /        /   
/________/    
''' 

        def __gt__(self,other):
            if isinstance(other,Shape.Rock):
                return True
            
            return False
        
        def __lt__(self,other):
            if isinstance(other,Shape.Scissors):
                return True
            
            return False
        
        def __str__(self):
            return 'Paper'

class Player:
    score = 0
    shape = None

    @abstractmethod
    def choice_getter(self):
        ...

    @property
    def invertedShape(self):
        return invShape(self.shape)

class Person(Player):
    name = 'Player'
    responseDict = {'1' : Shape.Rock(), '2' : Shape.Paper(), '3' : Shape.Scissors()}
    def choice_getter(self):
        while True:
            pc = input('Choose\n1. Rock\n2. Paper\n3. Scissors\n')
            self.shape = self.responseDict.get(pc,None)
            if self.shape != None:
                break

            if pc.title() in ['Rock', 'Scissors', 'Paper']:
                self.shape = eval('Shape.' + pc.title() + '()')
                assert (isinstance(self.shape, Shape.Rock)
                         or isinstance(self.shape,Shape.Paper) 
                          or isinstance(self.shape,Shape.Scissors)), f'EVAL SHAPE INITIALIZING not initializing properly, self.shape is type {type(self.shape)}, Shape.{pc.title()}()'
                break

            print('Please input a given option')

class AI(Player):
    name = 'Computer'
    def choice_getter(self):
        self.shape = random.choice([Shape.Rock(),Shape.Paper(),Shape.Scissors()])

def invChars(string : str):
    table = string.maketrans(r'()[]{}<>/\\',r')(][}{><\\/')
    string = string.translate(table)
    return string

def invShape(shape : str):
    splitShape = shape.image.split('\n')
    newShapeList = []
    for line in splitShape:
        newShapeList.append(invChars(line[::-1]))
    finalShapeList = '\n'.join(newShapeList)
    return finalShapeList

def combShapes(s1 : str,s2 : str):
    s1list = s1.split('\n')
    s2list = s2.split('\n')
    flist = []
    for index in range(min(len(s1list), len(s2list))):
        flist.append(s1list[index] + '     ' + s2list[index])

    return '\n'.join(flist) 

def doneAsk():
    viable_responses = {'Yes' : True, '1' : True, '2' : False, 'No' : False}
    while True:
        inp = input('Would you like to keep playing\n1. Yes\n2. No\n')
        ret = viable_responses.get(inp.title(),None)
        if ret != None:
            return ret
        print('Please choose a valid option')

def gLoop():
    p1 = Person()
    p2 = AI()
    run = True
    while run:
        state = turn(p1,p2)
        if not state:
            run = False

def turn(p1 : Player, p2 : Player):
    p1.choice_getter()
    p2.choice_getter()
    for i in range(3): print(abs(3-i)) , time.sleep(0.5)
    print(combShapes(p1.shape.image,p2.invertedShape))
    defeat_dict = {Shape.Rock : 'crushes' , Shape.Paper : 'covers' , Shape.Scissors : 'cuts'}
    if p1.shape.__class__ != p2.shape.__class__:
        print(max(p1.shape,p2.shape), defeat_dict[max(p1.shape,p2.shape).__class__] , min(p1.shape,p2.shape))
        if max(p1.shape,p2.shape) == p1.shape: 
            print('Player won')
            p1.score += 1
        else: 
            print('Computer won')
            p2.score += 1

    else:
        print('Tie')

    #Score
    print(f'Player Score: {p1.score}, Computer Score: {p2.score}')
    return doneAsk()
    
if __name__ == '__main__':
    gLoop()