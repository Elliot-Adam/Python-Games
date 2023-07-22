import time 
import hashlib 
import math 
from fractions import Fraction
import sqlite3

"""All of my tiny projects over my coding career
If on vscode press (Ctrl + K) and then (Ctrl + 1)  to fold the functions
"""
def test():
    print(set(list([1,2,3])))

def dec_to_frac():
    x = input("Input number ")
    print(Fraction(x))

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
     
def d_formula():
    x1,y1 = input('input coord of first node\n').split()
    x2,y2 = input('input coord of second node\n').split()

    x = (int(x1) - int(x2))**2
    y = (int(y1) - int(y2))**2

    d = math.sqrt(x + y)
    print('DISTANCE IS' , d)

def dictSwapper(og : dict):
    "Swaps a dictionary's values and keys into another dictionary"
    empty : dict = {}
    for k,v in og.items():
        empty[v] = k
    return empty
    
def dict_search(dictionary : dict, keyword) -> list:
    "Gets list of keys from a keyword"
    l : list = []
    for k,v in dictionary.items():
        if v is keyword:
            l.append(k)
    return l

#All projects
if __name__=="__main__":
    test()
    #grade_calc()
    #food_calc()
    #Interest_Calc()
    #Pass()
    #tax_calc()
    #rocket()
    #inv_calc()
    #pay_calc()
    #even_calc()
    #Cris_pass()
    #function_pay_calc()
    #prime_calc()
    #recurs_additive_calc()
    #recurs_additive_calc()
    #factorial_calc()
    #largest_and_smallest()
    #vowel_count()
    #file_up_reader
    #selective_avg()
    #text_analizer()
    #reader()
    #most_common_word()
    #mcw_after_key()
    #quadratic_calc()
    #dec_to_frac()
    #sockets()
    #jsonparsing
    #jsonGeoFinder()
    #sqltables()
    #ptheorum()
    #scrabble_helper()
    #d_formula()
    #print(dictSwapper({'a' : 1 ,'b' : 2, 'c' : 3}))
    #print(dict_search({'a':1,'b':2,'c':1},1))
    pass