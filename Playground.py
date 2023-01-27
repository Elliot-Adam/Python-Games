import time 
import hashlib 
import math 
import random 
import re 
from fractions import Fraction
import sqlite3
import pygame

class Small_Projects:

    def dec_to_frac():
        x = input("Input number ")
        print (Fraction(x))

    def grade_calc():

    #Put in correct out of total and get percent and letter grade

        t=input ("Enter Numerator \n")
        v=input ("Enter Denominator \n")
        try: 
            t=float(t)
            v=float(v)
        except:
            print ("CANNOT DIVIDE WORDS")
        try:
            s=(t/v)
        except:
            print ("CANNOT DIVIDE BY ZERO")
            quit()
        s=(s*100)
        print ("{}{}".format(round(s,2), "%"))
        if s<0:
            print ("INVALID NUMBERS")
            quit ()
        elif s>150:
            print ("INVALID")
            quit () 
        if s   > 100:
            print ("A+")    
        elif s >= 94:
            print ("A")
        elif s >= 90:
            print ("A-")
        elif s >= 86:
            print ("B+")
        elif s >= 84:
            print ("B")
        elif s >= 80:
            print ("B-")
        elif s >= 76:
            print ("C+")
        elif s >= 74:
            print ("C")
        elif s >= 70:
            print ("C-")
        elif s >= 66:
            print ("D+")
        elif s >= 64:
            print ("D")
        elif s >= 60:
            print ("D-")
        elif s  < 60:
            print ("E")
    
    def food_calc():

        #Meal Calc with 15% Tip and 10% Tax 

        m=input ("Cost of meal: ")
        try:
            m=(float(m))
        except:
            print ("INVALID")
            quit()

        if m<=0:
            print ("INVALID")
            quit()
        t=(m*(1/10))
        st=(t+m)
        ti=(st*(15/100))
        to=(m+t+ti) 
        print ("Meal cost:", round(m,2),"Tax cost:",round(t,2), "Tip cost:",round(ti,2),"TOTAL COST:",round(to,2))

    def Interest_Calc():

        #Interest Calc with 7.5% interest rate

        mo=input ("INSERT AMOUNT\n")
        ye=input ("INSERT YEARS FOR CALCULATIONS\n")
        mo=(float(mo))
        ye=(float(ye))
        while ye>0:
            mo=((mo)*1.075)
            print (round(mo,2))
            ye=(ye-1)
            time.sleep (0.2)
    
    def Pass():

        #Password System with my B-day

        x=input ("Enter Password \n")
        x=int(x)
        pas=14623
        x=(x*2+7)
        if x==pas:
            print ("Correct Password")
        else:
            print ("Incorrect Password")
        
    def tax_calc():

    #Sales Tax Calc with Total cost 
    
        c=input("INSERT COST: ") 
        c=float(c)
        ta=(.06*c)
        too=(c+ta)
        print ("Cost:",round(c,2), "Tax Cost:" ,round(ta,2), "Total Cost:",round(too,2))
    
    def rocket():

        #Rocket Blastoff
    
        r=5

        while r>0:
            print (r)
            r=(r-1)
            time.sleep (0.8)

        print ("BLASTOFFFF!")

    def inv_calc() :

        #Invoice Calc with $per minute 1.3, $text message 0.3, $per Gig 2, Customer service 3, VAT of 10%, and if paid within 15 days 5% discount
        
        mi=input ("INSERT NUMBER OF MINUTES \n")
        mi=float(mi)
        mi=(mi*1.3)
        tm=input ("INSERT NUMBER OF TEXT MESSAGES \n")
        tm=float(tm)
        tm=(tm*0.3)
        g=input ("INSERT AMOUNT OF INTERNET USED \n")
        g=float(g)
        g=(g*2)
        
        cs=(3)
        invo=(cs+g+tm+mi)
        VAT=(invo*1/10)
        tinvo=(invo+VAT)
        di=(tinvo*19/20)
        wo=(tinvo)
        print ("WITHIN 15 DAYS:",round(di,2),"WITHOUT 15 DAYS", round(wo,2)) 

    def pay_calc():

        #Pay with adjusted labor costs of 1.5x rate after 40 hours

        rte=input ("Enter Rate:")
        hrs = input("Enter Hours:")
        h = float(hrs)
        r=float(rte)
        if h > 40:
            h=(h-40)
            sr=(r*1.5)
            sh=(h*sr)
            h=40
            p=(h*r+sh)
        else:
            p=(h*r)
        print (p)
    
    def even_calc():

    #Even number Calc in selected range 
        count=0
        min = input ("Enter Minimum \n")
        max= input ("Enter Maximum \n")
        min= int(min)
        max= int(max)
        for x in range(min,max):
            if x % 2 == 0:
                count +=1
        print ("There are", count,"even numbers in between", min, "and",max)

    def Cris_pass():
    
    #Hashing password system Password:Jaraxxus
        

        inputPw = input("Enter password \n" )

        #hashedPassword = hashlib.sha512(password.encode('utf-8')).hexdigest()
        hashedInput = hashlib.sha512(inputPw.encode('utf-8')).hexdigest()

        alsoHashedPassword = "60d1627dee91a47d96c775b4888dd45a0e04fb1ce21c0ab96664d4a02d3c1c74c7a5939b746397b52a7526aed2f2f9155b6ca357526990cb0096f3ec9900dc8c"
        #print("Hashed password: " + hashedPassword)
        #print("Hashed input: " + hashedInput)
    
        #if ( hashedPassword == hashedInput):
            #print("Password Correct")
        if ( hashedInput == alsoHashedPassword):
            print("Password Correct")
            print("also matched saved hash")
        else:
            print("Incorrect password")
        
    def function_pay_calc():
        def computepay(h, r):
            if h > 40:
                h=(h-40)
                sr=(r*1.5)
                sh=(h*sr)
                h=40
                return (h*r+sh)
            else:
                return (h*r)
                
        rte=input ("Enter Rate:")
        hrs = input("Enter Hours:")
        hr = float(hrs)
        ra=float(rte)
            
        p = computepay(hr, ra)
        print("Pay", p)
        
    def prime_calc():
        
        
        #Input a number and get a Prime or Composite
        
        x=input ("Enter Number \n")
        x=int(x)
        y=math.sqrt((x)+1)
        ft=3
        while ft<y:
            if x%ft:
                ft+=1
            else:
                print ("Composite")
                quit()
        print ("Prime")

    def recurs_additive_calc():
        #Insert a number to add up all its predecessors (e.g. insert 3 get 6 because 3 + 2 + 1)

        def total(num):
            if num == 1:
                return 1
            else:
                return num + total(num-1)

        n = input("Enter number ")
        nint = int(n)
        print(total(nint))
        
    def not_recurs_additive_calc():
        n = input('Enter Number ')
        nlist = []
        nint = int(n)
        while nint > 0:
            nlist.append (nint)
            nint = nint - 1
        slist = sum(nlist)
        print (slist)

    def factorial_calc():

    #Finds the factorial of the inputted number
        tota = 1
        n = input("Enter number ")
        nlist = list()
        nint = int(n)
        while nint > 0:
            nlist.append (nint)
            nint = nint - 1
        l = len(nlist)
        l += 1
        for x in range (1,l):
            tota = (tota*x)
        print (tota)
        
    def largest_and_smallest():

    #Repeatedly prompts for number until done is input; Finds the largest and smallest number out of sample size

        largest=None
        smallest=None 

        while True:
            InputS = input("Enter a number: ")
            if InputS == "done":
                break
            try:
                InputI=int(InputS)
            except:
                print ("Invalid input")
                continue
            if largest == None:
                largest =  InputI
            if smallest == None:
                smallest = InputI 
            
            if InputI > largest :
                largest = InputI 
            if InputI < smallest :
                smallest = InputI 
        print("Maximum is", largest)
        print("Minimum is", smallest)
        
    def vowel_count():

    # Continually asks for a string than counts the number of vowels in that string

        count=0
        vowel=set("aeiouAEIOU")
    
        while True:
            x = input ("Enter: ")
            try:
                int(x)
                print("Invalid")
                continue 
            except:
                pass
            if x == "done":
                break
            if x == "Done":
                break
            for letter in x:
                if letter in vowel:
                    count += 1
            print ("Vowel count updated")
        print ("Final vowel count", count)

    def file_up_reader():

    #Read and uppercase a whole file
        fname = input("Enter file name: ")
        fh = open(fname,'r')
        lines = fh.readlines()

        for line in lines:
            strippedAndUpper = line.upper().strip()
            print (strippedAndUpper)
            
    def selective_avg():

    #Have python sort through a file and only looking at numbers after a keyword then adds them up and makes an average
        fname = input("Enter file name: ")
        fhand = open(fname)
        optot = 0
        count = 0
        for line in fhand:
            if line.startswith("X-DSPAM-Confidence:"):
                count += 1 
                op = line.find (":")
                opf = line[op+1:]
                opf = float(opf)
                optot = (optot + opf)
        optavg = optot/count
        print ("Average spam confidence:", optavg)

    def text_analizer():

    #Enter the name of a text file and it will go through every word and sort and print every new word.

        fname = input("Enter file name: ")
        fh = open(fname)
        lst = []
        lstsort = []
        for line in fh:
            wL = line.split()
            for word in wL:
                if word == "\n":
                    continue 
                if word in lst:
                    continue 
                else:
                    lst.append(word)
                    continue
        lstsort = lst[:]
        lstsort.sort()
        print (lstsort)
        fh.close

    def reader():

    #Input a file and it will count and print every line that started with the keyword
        fname = input("Enter file name: ")
        fh = open(fname)
        count = 0
        for line in fh:
            Sline = line.split()
            
            if len(Sline) < 1: 
                continue 
            else:
                SSline = Sline [0]
                if len(Sline) > 1:
                    FSline = Sline [1]
                else:
                    continue
            if SSline == "From":
                print (FSline)
                count += 1

        print("There were", count, "lines in the file with From as the first word")
        fh.close

    def most_common_word():

    #Input a file and it will spit out the most common word and how many times it was said DOES WORK WITH MULTIPLE WORDS WITH THE SAME FREQUENCY
        fname = input("Enter file name: ")
        if len(fname) < 1:
            fname = "textFile.txt"
        lines = open(fname)
        words = {}
        mcw = []
        largestM = None
        for line in lines:
            line = line.split()
            for word in line:
                words[word] = words.get(word,0) + 1
                if largest == None:
                    largest = words[word]
                if words[word] >= largest:
                    largest = words[word]
                    if word in mcw:
                        continue
                    else: 
                        mcw.append(word)
        if len(mcw) > 1:
            print ("Most common words:",mcw,"; Frequencies:",largest)
        else:
            print ("Most common word:",mcw,"; Frequency:",largest)
        lines.close

    def mcw_after_key():

    #Input a file and get the most common word and frequency of words only past a keyword
    
        fname = input("Enter file name: ")
        if len(fname) < 1:
            fname = "textFile.txt"
        lines = open(fname)
        words = {}
        largest = None
        for line in lines:
            line = line.split()
            if len(line) > 1:
                if line[0] == "From":
                    line1 = line[1]
                    words[line1] = words.get(line1,0) + 1
                    if largest == None or words[line1] >= largest:
                        largest = words[line1]
                        mcw = line1 
        try:
            print (mcw)
        except:
            print ("No words with that keyword were found in the file")

    def quadratic_calc():
        #Quadratic Equation
        def assignment(letter):
            letter = input(letter + " = ")
            return letter
        def purification(inputted):
            pure = int(inputted)
            return pure
        def Ready(letter):
            strletter = assignment(letter)
            readyLetter = purification(strletter)
            return readyLetter

        A = Ready('A')
        B = Ready('B')
        C = Ready('C')
        possol = (B*-1 + math.sqrt(B**2 - (4*A*C)))/(2*A)
        negsol = (B*-1 - math.sqrt(B**2 - (4*A*C)))/(2*A)
        print ("x =",round(possol,2),"and x =",round(negsol,2))

    def sockets():
        #Socket Connect Example
        import socket

        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect(('data.pr4e.org', 80))
        cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(),end='')

        mysock.close()

    def jsonparsing():
        from urllib.request import Request
        from urllib.request import urlopen
        import json 
        import ssl
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        url = input('Enter url')
        if (len(url) < 1):
            url = "https://py4e-data.dr-chuck.net/comments_1637310.json"
        raw_request = Request(url)
        raw_request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
        raw_request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
        resp = urlopen(raw_request)
        raw_html = resp.read()
        raw_json = json.loads(raw_html)
        total = 0
        for dict in raw_json['comments']:
            v = dict['count']
            total += v
        print (total)

    def jsonGeoFinder():
        import urllib.request, urllib.parse, urllib.error
        import json
        import ssl

        api_key = False
        # If you have a Google Places API key, enter it here
        # api_key = 'AIzaSy___IDByT70'
        # https://developers.google.com/maps/documentation/geocoding/intro

        if api_key is False:
            api_key = 42
            serviceurl = 'http://py4e-data.dr-chuck.net/json?'
        else :
            serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        while True:
            address = input('Enter location: ')
            if len(address) < 1: break

            parms = dict()
            parms['address'] = address
            if api_key is not False: parms['key'] = api_key
            url = serviceurl + urllib.parse.urlencode(parms)

            print('Retrieving', url)
            uh = urllib.request.urlopen(url, context=ctx)
            data = uh.read().decode()
            print('Retrieved', len(data), 'characters')

            try:
                js = json.loads(data)
            except:
                js = None

            if not js or 'status' not in js or js['status'] != 'OK':
                print('==== Failure To Retrieve ====')
                print(data)
                continue

            #print(json.dumps(js, indent=4))

            #Add a print statement whenever you want
            lat = js['results'][0]['geometry']['location']['lat']
            lng = js['results'][0]['geometry']['location']['lng']
            print('lat', lat, 'lng', lng)
            location = js['results'][0]['formatted_address']
            place_id = js['results'][0]['place_id']

    def sqltables():
        conn = sqlite3.connect('emaildb.sqlite')
        cur = conn.cursor()

        cur.execute('DROP TABLE IF EXISTS Counts')

        cur.execute('''
        CREATE TABLE Counts (org TEXT, count INTEGER)''')

        fname = input('Enter file name: ')
        if (len(fname) < 1): fname = 'Assignment.txt'
        fh = open(fname)
        for line in fh:
            if not line.startswith('From: '): continue
            pieces = line.split()
            email = pieces[1]
            partsOfEmail = email.split('@')
            domain = partsOfEmail[1]
            cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO Counts (org, count)
                        VALUES (?, 1)''', (domain,))
            else:
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                            (domain,))
        conn.commit()

        # https://www.sqlite.org/lang_select.html
        #cur = conn.cursor()
        sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

        for row in cur.execute(sqlstr):
            print(str(row[0]),row [1])

        cur.close()
                
    def ptheorum():
        a = input("Input a ")
        b = input("Input b ")
        c = math.sqrt(float(a)**2 + float(b)**2)
        print("c is {}".format(c))

class Big_Projects:

    def scrabble_helper():

    #Input however many letters and python will find every word in the set dictionary that contains those letters; WORKS WITH DUPLICATE LETTERS    
    
        file1 = open('10Kenglish.txt', 'r')
        text = file1.readlines()
        inputI = input ("Enter Letters ")
        try:
            int(inputI)
            quit()
        except:
            pass 
        inputL = []
        inputL.append(inputI)
        rL = []
        sL = inputL[0]
        for letter in sL:
            rL.append(letter)
        rL.append("_")
        count = 1 
        c = 0
        cc = 0
        rsL = rL[:]
        wlist = []
        clist = []
        swlist = [] 
        
        for line in text:
            count += 1
            line = (line.strip() + "_")
            for x in line: 
                
                if x in rsL:
                
                    if x == ("_"):
                        wlist.append (line)
                        clist.append (count)
                    rsL.remove(x)
                    continue  
                else:
                    rsL = rL[:]
                    break
                
            rsL = rL[:]
        for z in wlist:
            swlist.append(z.strip("_"))
        print ("\n")
        for y in swlist:
                print ("Line:" , clist[cc] ,"; Word:" , y)
                cc += 1
                c += 1
                time.sleep (0.15)
            
        print ("\n", c, "possible words") 
        file1.close()


    def rps():
        #Rock Paper Scisssors
        #Ascii art
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
                    image(rock,rock)
                    return 't'
                case 'rs':
                    image(rock,scissors)
                    return 'w'
                case 'rp':
                    image(rock,paper)
                    return 'l'
                case 'ss':
                    image(scissors,scissors)
                    return 't'
                case 'sp':
                    image(scissors,paper)
                    return 'w'
                case 'sr': 
                    image(scissors,rock)
                    return 'l'
                case 'pp':
                    image(paper,paper)
                    return 't'
                case 'pr':
                    image(paper,rock)
                    return 'w'
                case 'ps':
                    image(paper,scissors)
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


    def TicTacToe():
        #Tic Tac Toe

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
            def choiceGetter(self):
                self.choice = self.optimalMove()
                self.choice -= 1

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
                if len(self.winningMove()) > 0:
                    return random.choice(self.winningMove())
                if len(self.blockWin()) > 0:
                    return random.choice(self.blockWin())
                if len(self.corners()) > 0:
                    return random.choice(self.corners())
                return random.choice(board.repCheck()) 


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


    def Pong():
        #Imports
        pygame.init()

        #Classes
        class Ball:
            def __init__(self,x,y,vx,vy,radius):
                self.x = x
                self.y = y
                self.vx = vx
                self.vy = vy
                self.radius = radius
                self.incrementSpeed = False
                self.accy = 0.3
                self.accx = 0.3
            def move(self):
                self.x += self.vx
                self.y += self.vy
            def direct_distance(self,other):
                return math.sqrt(((self.x - other.x)**2) + ((self.y - other.y)**2))
        class Paddle:
            def __init__(self,x,y,width,height):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
            def paddle_move(self, keyup,keydown):
                allKeys = pygame.key.get_pressed()
                if allKeys[keyup]:
                    if self.y - 7 >= 0:
                        self.y -= 7
                    else:
                        self.y += 5
                if allKeys[keydown]:
                    if self.y + self.height + 7 <= displayHeight:
                        self.y += 7
                    else:
                        self.y -= 5
            def move(self):
                if self.x == 10:
                    self.paddle_move(pygame.K_w,pygame.K_s)   
                else:
                    self.paddle_move(pygame.K_UP,pygame.K_DOWN)

        #Function Defs
        def score_update(ascore,bscore):
            regFont = pygame.font.Font(None,40)
            ascoreprint = regFont.render(str(ascore),True,white)
            ascore_rect = ascoreprint.get_rect(center = (displayWidth/3,displayHeight/5))
            bscoreprint = regFont.render(str(bscore),True,white)
            bscore_rect = bscoreprint.get_rect(center = (displayWidth*(2/3),displayHeight/5))
            SCREEN.blit(ascoreprint,ascore_rect)
            SCREEN.blit(bscoreprint,bscore_rect)
        def hit_paddle(ball,paddle):
            #Check hit corner top right
            if math.sqrt((ball.x - paddle.x + paddle.width)**2 + (ball.y - paddle.y)**2) < ball.radius:
                ball.vy *= -1 
                    
                return True
            #Check hit corner bottom right
            if math.sqrt((ball.x - paddle.x + paddle.width)**2 + (ball.y - paddle.y - paddle.height)**2) < ball.radius:
                ball.vy *= -1 
                return True
            #Check hit
            if ball.vx < 0:
                if ball.x - ball.radius <= paddle.x + paddle.width + 2 and ball.y > paddle.y and ball.y < paddle.y + paddle.height:
                    return True
            else:
                if ball.x + ball.radius >= paddle.x - paddle.width - 2 and ball.y > paddle.y and ball.y < paddle.y + paddle.height:
                    return True
            return False
        def hit_sides(y,dh,radius):
            if (y < radius) or y > (dh - radius):
                return True
        def hit_front(ball):
            if ball.x < ball.radius:
                return True
            return False
        def hit_back(ball):
            if ball.x + ball.radius > displayWidth:
                return True
            return False
        def reset(SINGLEball):
            SINGLEball.x = displayWidth/2
            SINGLEball.y = random.randint(10,displayHeight - 10)
            if random.randint(0,2) % 2 == 0:
                ball.vy *= -1
        def gmode(mode):
            global ball
            global paddle_a
            global paddle_b
            global ball1
            global ball2
            global speed
            paddle_a = Paddle(10,displayHeight/2,3,40)
            paddle_b = Paddle(490,displayHeight/2,3,40)
            if mode == 1:
                speed = 30
                ball = Ball(displayWidth/2,displayHeight/2,6,6,10)
            if mode == 2:
                speed = 30
                ball1 = Ball(displayWidth/2,(3*displayHeight/5),6,6,10)
                ball2 = Ball(displayWidth/2,(2*displayHeight/5),-6,-6,10)
            if mode == 3:
                speed = 45
                ball = Ball(displayWidth/2,displayHeight/2,6,6,20)
                paddle_a.height = 20
                paddle_b.height = 20 
            if mode == 4:
                speed = 35
                ball = Ball(displayWidth/2,displayHeight/2,6,6,10)
                ball.incrementSpeed = True
        def gmode_getter():
            messageprint = []
            pygame.time.set_timer(pygame.USEREVENT,10000)
            timer_active = True
            regFont = pygame.font.Font(None,30)
            message = ['Input Mode ','1. Normal ','2. Multiball ','3. Big Ball, Small Paddle','4.Speed Pong']
            for text in message:
                messageprint.append(regFont.render(text,True,white))
            for line in range(len(messageprint)):
                print(displayHeight/5 - line)
                message_rect = messageprint[line].get_rect(center = (displayWidth/2,displayHeight/6 + line*50))
                SCREEN.blit(messageprint[line],message_rect)
            pygame.display.flip()
            while timer_active:
                
                for event in pygame.event.get():
                    if event.type == pygame.USEREVENT:
                        timer_active = False
                        return 1
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                            print(event.key,pygame.K_1,pygame.K_2,pygame.K_3)
                            timer_active = False
                        if event.key == pygame.K_1:
                            return 1
                        if event.key == pygame.K_2:
                            return 2
                        if event.key == pygame.K_3:
                            return 3
                        if event.key == pygame.K_4:
                            return 4
        def ballCrash(ballUno,ballDos):
            if ballUno.direct_distance(ballDos) < ballUno.radius*2:
                return True
            

        #Variable Defs
        clock = pygame.time.Clock()
        speed = 30
        displayWidth = 500
        displayHeight = 300
        ascore = 0
        bscore = 0
        SCREEN = pygame.display.set_mode((displayWidth,displayHeight))
        black = (0,0,0)
        white = (255,255,255)
        gameIcon = pygame.image.load('Pong_Image.png')
        pygame.display.set_caption("Pong")
        pygame.display.set_icon(gameIcon)
        mode = gmode_getter()
        gmode(mode)
        #Game Loop
        if __name__ == "__main__":
            while True:
                if mode == 1 or mode == 3 or mode == 4:
                    clock.tick(speed)
                    pygame.draw.rect(SCREEN,white,(paddle_a.x,paddle_a.y,paddle_a.width,paddle_a.height))
                    pygame.draw.rect(SCREEN,white,(paddle_b.x,paddle_b.y,paddle_b.width,paddle_b.height))
                    pygame.draw.circle(SCREEN,white,(ball.x,ball.y),ball.radius)
                    ball.move()
                    paddle_a.move()
                    paddle_b.move()
                    if hit_front(ball):
                        bscore += 1
                        reset(ball)
                    if hit_back(ball):
                        ascore += 1
                        reset(ball)
                    if hit_paddle(ball,paddle_a):
                        if ball.incrementSpeed:
                            if ball.vy < 0:
                                ball.vy -= ball.accy
                                ball.accy -= 0.005
                                ball.vx -= ball.accx
                                ball.accx -= 0.005
                            if ball.vy > 0:
                                ball.vy += ball.accy
                                ball.accy += 0.005
                                ball.vx += ball.accx
                                ball.accx -= 0.005
                        ball.vx = abs(ball.vx) 
                    if hit_paddle(ball,paddle_b):
                        ball.vx = abs(ball.vx) * -1
                    if hit_sides(ball.y,displayHeight,ball.radius):
                        ball.vy *= -1
                    score_update(ascore,bscore)
                    pygame.display.update()
                if mode == 2:
                    clock.tick(speed)
                    pygame.draw.rect(SCREEN,white,(paddle_a.x,paddle_a.y,paddle_a.width,paddle_a.height))
                    pygame.draw.rect(SCREEN,white,(paddle_b.x,paddle_b.y,paddle_b.width,paddle_b.height))
                    pygame.draw.circle(SCREEN,white,(ball1.x,ball1.y),ball1.radius)
                    pygame.draw.circle(SCREEN,white,(ball2.x,ball2.y),ball2.radius)
                    ball1.move()
                    ball2.move()
                    paddle_a.move()
                    paddle_b.move()
                    for ball in [ball1,ball2]:
                        if hit_front(ball):
                            bscore += 1
                            reset(ball)
                        if hit_back(ball):
                            ascore += 1
                            reset(ball)
                        if ballCrash(ball1,ball2):
                            ball1.vx *= -1
                            ball2.vx *= -1
                            ball1.vy *= -1
                            ball2.vy *= -1
                        if hit_paddle(ball,paddle_a):
                            ball.vx = abs(ball.vx) 
                        if hit_paddle(ball,paddle_b):
                            ball.vx = abs(ball.vx) * -1
                        if hit_sides(ball.y,displayHeight,ball.radius):
                            ball.vy *= -1
                    score_update(ascore,bscore)
                    pygame.display.update()
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                SCREEN.fill(black)

                
if __name__=="__main__":
#Normal Projects

    #Small_Projects.grade_calc()
    #Small_Projects.food_calc()
    #Small_Projects.Interest_Calc()
    #Small_Projects.Pass()
    #Small_Projects.tax_calc()
    #Small_Projects.rocket()
    #Small_Projects.inv_calc()
    #Small_Projects.pay_calc()
    #Small_Projects.even_calc()
    #Small_Projects.Cris_pass()
    #Small_Projects.function_pay_calc()
    #Small_Projects.prime_calc()
    Small_Projects.recurs_additive_calc()
    Small_Projects.recurs_additive_calc()
    #Small_Projects.factorial_calc()
    #Small_Projects.largest_and_smallest()
    #Small_Projects.vowel_count()
    #Small_Projects.file_up_reader
    #Small_Projects.selective_avg()
    #Small_Projects.text_analizer()
    #Small_Projects.reader()
    #Small_Projects.most_common_word()
    #Small_Projects.mcw_after_key()
    #Small_Projects.quadratic_calc()
    #Small_Projects.dec_to_frac()
    #Small_Projects.sockets()
    #Small_Projects.jsonparsing
    #Small_Projects.jsonGeoFinder()
    #Small_Projects.sqltables()
    #Small_Projects.ptheorum()

#Big Projects

    #Big_Projects.rps()
    #Big_Projects.scrabble_helper()
    #Big_Projects.TicTacToe()
    #Big_Projects.Pong()
    pass