#Rock Paper Scisssors
#Imports
import random
import time

#Ascii art
class Shapes:
    def rock():
        return'''
               ,--.--._     
        ------" _, \___)    
                / _/____)   
                \ /(____)   
        ------\     (__)    
                `-----"     
        '''

    def scissors():
        return'''
                            
         __       ,/'        
        (__).  ,/'           
         __  ::              
        (__)'  `\.           
                  `\.        
        '''    

    def paper():
        return'''
                _________          
               /        /          
              /        /           
             /        /            
            /________/             
                                
        '''
#Prints
def countdown():
    for i in [3,2,1]:
        Delay(0.5)
        print(i)

def errormes():
    print("\nPlease input your selection of 1, 2 ,or 3\n")

def Delay(amount):
    time.sleep(amount)

def Chose(parameter):
    print(parameter,'chose\n')
    Delay(0.25)
    
def Score(score1,score2):
    print('Player Score: {} Computer Score: {}'.format(score1,(score2 * -1)))

def Winner(winner):
    print (winner, ("wins"))

def image(image1,image2):
    splitimageleft = image1().split('\n')
    splitimageright = invert(image2()).split('\n')
    smallerImage = min(len(splitimageleft),len(splitimageright))
    for i,_ in enumerate(range(0,smallerImage)):
        print(splitimageleft[i] + splitimageright[i])


#Invert Ascii Art
def turnAround(strng:str):
    return strng[::-1]

def invert(shape:str):
    splitShape = shape.split('\n')
    newShapeList = []
    for line in splitShape:
        revline = turnAround(line)
        checkedRevLine = invertCharc(revline)
        newShapeList.append(checkedRevLine)
        finalShapeList = "\n".join(newShapeList)
    return finalShapeList

def invertCharc(string:str):
    table = string.maketrans(r'()[]{}<>/\\',r')(][}{><\\/')
    string = string.translate(table)
    return string


#Inputs
def scoreGetter():
    while True:
        breaker = False
        scoreGoalValid = [1,3,5]
        scoreGoalInput = input("Best of 1 , 3 , 5\n")
        try:
            int(scoreGoalInput)
        except ValueError:
            print("\nCannot use letters\n")
            continue
        if int(scoreGoalInput) in scoreGoalValid:
            intscoreGoalInput = int(scoreGoalInput)
            breaker = True 
        else:
            print("\nInvalid\n")
        if breaker:
            return [intscoreGoalInput,(intscoreGoalInput * -1)]

def Player_choice():
    while True:
        pc = input("Choose\n1. Rock\n2. Paper\n3. Scissors\n")
        print ("\n")
        if len(pc) > 1:
            errormes()
            continue
        try:
            pci = int(pc)
        except:
            errormes()
            continue
        if not pci in [1,2,3]:
            errormes()
            continue

        if pci == 1: 
            return 'pcr'
        elif pci == 2:
            return 'pcp'
        elif pci == 3:
            return 'pcs'

def AI_choice(numa):
    ac = random.choice(numa)
    Delay(0.75)
    if ac == 1:
        return 'acr'
    if ac == 2:
        return 'acp'
    if ac == 3:
        return 'acs'

def finishvars(search):
    match search:
        case 'rr':
            image(Shapes.rock,Shapes.rock)
            return 't'
        case 'rs':
            image(Shapes.rock,Shapes.scissors)
            return 'w'
        case 'rp':
            image(Shapes.rock,Shapes.paper)
            return 'l'
        case 'ss':
            image(Shapes.scissors,Shapes.scissors)
            return 't'
        case 'sp':
            image(Shapes.scissors,Shapes.paper)
            return 'w'
        case 'sr': 
            image(Shapes.scissors,Shapes.rock)
            return 'l'
        case 'pp':
            image(Shapes.paper,Shapes.paper)
            return 't'
        case 'pr':
            image(Shapes.paper,Shapes.rock)
            return 'w'
        case 'ps':
            image(Shapes.paper,Shapes.scissors)
            return 'l'

def doneprompt():
    z = input("Do you want to play again\nYes\nNo\n")
    if z == "Yes" or z == "yes":
        return False
    if z == "No" or z == "no":
        print ("Thanks for Playing")
        return True
    print("Invalid\n")

def combinations(pchoice,achoice):
    countdown()
    outcome = finishvars(pchoice[2] + achoice[2])
    if outcome == 'w':
        Winner('Player')
        return 'p'
    if outcome == 'l':
        Winner('Computer')
        return 'a'
    if outcome == 't':
        print('Tie Game')
        return 't'

def scoreCheck(score):
    if score in scoreGoal:
        if score > 0:
            return setWinner('Player')
        elif score < 0:
            return setWinner('Computer')
    else:
        return 'f'
    
def setWinner(setwinner):
    print (setwinner, "wins the set")
    dp = doneprompt()
    return dp

if __name__ == '__main__':
    donePlaying = False
    while not donePlaying:
        pscore = 0
        ascore = 0
        scoreGoal = scoreGetter()
        while True:
            player_decision = Player_choice()
            Chose('Player')
            AI_decision = AI_choice([1,2,3])
            Chose('Computer')
            finalOutcome = combinations(player_decision,AI_decision)
            if finalOutcome == 't':
                continue
            if finalOutcome == 'p':
                pscore += 1
            if finalOutcome == 'a':
                ascore -= 1
            Score(pscore,ascore)
            Delay(0.7)
            donePlaying = scoreCheck(ascore)
            donePlaying = scoreCheck(pscore)
            if not donePlaying == 'f':
                if not donePlaying:
                    pscore = 0
                    ascore = 0
                else:
                    break