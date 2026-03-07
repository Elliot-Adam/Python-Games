import os 

class DBException (Exception):
    message = ''

class EmptyDatabaseException (DBException):
    message = 'The data base is empty\nUnable to remove or change people'

class NoDataException (DBException):
    message = 'No data from person\nUnable to remove or change data'

class Utility:
    @staticmethod
    def get_person_from_db() -> str:
        personsStr = '\n'.join(Utility.get_database(1))
        limiter = '_'
        condList = []
        condList.extend(Utility.get_database(1))
        condList.extend([f'_{x}' for x in range(len(Utility.get_database(1)))])
        personRequested = Utility.assertValidAnswer('Please input the name of the person you want from the database (start with _ to use ID): ', f'Please input someone from the database\nOptions are {personsStr}', 'inp in condList', condList) 
        if personRequested.startswith(limiter):
            personRequested = Utility.get_database(1)[int(personRequested.strip(limiter))]
            print(f'Using ID of {personRequested}')
        
        return personRequested

    @staticmethod
    def dict_to_str(dictToStr : dict) -> str:
        strFromDict = '{'
        for k,v in dictToStr.items():
            strFromDict += f'\'{k}\' : \'{v}\','

        strFromDict = strFromDict.strip(',') + '}'
        return strFromDict

    @staticmethod
    def retrieve_name(modifier : str = ''):
        lName = Utility.assertValidAnswer(f'Please input the person\'s {modifier}last name: ', 'Please input a valid name', 'len(inp) > 2').capitalize()
        fName = Utility.assertValidAnswer(f'Please input the person\'s {modifier}first name: ', 'Please input a valid name', 'len(inp) > 2').capitalize()
        mI = Utility.assertValidAnswer(f'Please input the person\'s {modifier}middle initial: ', 'Please input a valid initial', 'len(inp) == 1').capitalize()
        return f'{fName.strip()} {mI.strip()}. {lName.strip()}'

    @staticmethod
    def present_menu(prompt : str, options : list):
        numList = []
        prompt += '\n'
        for num,option in enumerate(options,1):
           numList += str(num)
           prompt += f'{num}. {option}\n'

        prompt += '\n'
        return int(Utility.assertValidAnswer(prompt, 'Please select a valid answer', 'inp in condList', numList))

    @staticmethod
    def assertValidAnswer(promptMessage : str, failureMessage : str, condition : str, condList : list = []) -> str:
        """Gets input given a certain condition which is defined by the condition parameter.
        If condition not fulfilled, will print failure message until condition is fulfilled"""
        inp = ''
        while True:
            inp = input(promptMessage)
            if inp == ';': quit()
            if eval(condition):
                break
            print(failureMessage)
                
        return inp
    
    @staticmethod
    def get_persons_data(person : str) -> dict[str:str]:
        dataDict = Utility.get_database(2)[Utility.get_person_ID(person)].strip('\n')
        if dataDict: return eval(dataDict)
        raise NoDataException()

    @staticmethod
    def get_database(type : int = 4) -> list[str]:
        """Returns a list denoted by the type parameter\n
        1=All peoples names\n
        2=All people's data as strings\n
        3=Tuples with index 0 being the name and index 1 being the string of data\n
        4=Strings of the name + limiter + data"""
        with open(DATABASE,'r') as database:
            lines = database.readlines()
            if not lines: raise EmptyDatabaseException
            match type:
                case 1:
                    #Gives all names
                    return [x.split('/')[0] for x in lines]
                
                case 2:
                    #Gives all data
                    return [x.split('/')[1] for x in lines]
                
                case 3:
                    #Gives a tuple (names, data)
                    return [(x.split('/')[0],x.split('/')[1]) for x in lines]
                
                case 4:
                    #Gives full string
                    return lines

    @staticmethod
    def get_person_ID(person : str):
        return Utility.get_database(1).index(person)

class DatabaseMethods:
    #Person Methods
    @staticmethod
    def add_to_database():
        fullName = Utility.retrieve_name()
        try:
            if fullName in Utility.get_database(1):
                print('Name already in database')
                wait()
                return
            
        except EmptyDatabaseException:
            pass
        
        with open(DATABASE, 'a') as database:
            database.write(f'{fullName}/\n')
            print(f'{fullName} added successfully')
            wait()

    @staticmethod
    def remove_from_database():
        try:
            personRequested = Utility.get_person_from_db()
            lines = Utility.get_database()
            lines.pop(Utility.get_person_ID(personRequested))
            print(f'{personRequested} successfully removed')

            with open(DATABASE,'w') as database:
                database.writelines(lines)
                wait()

        except DBException as e:
            print(e.message)
            wait()           

    @staticmethod
    def change_name_in_database():
        try:
            personRequested = Utility.get_person_from_db()
            newName = Utility.retrieve_name('new ')
            lines = Utility.get_database()
            id = Utility.get_person_ID(personRequested)
            lines[id] = f'{newName}/{Utility.get_database(2)[id]}'

            with open(DATABASE,'w') as database:
                database.writelines(lines)
                print(f'Name changed from {personRequested} to {newName} successfully')
                wait()
            
        except DBException as e:
            print(e.message)
            wait()   

    #Data Methods
    @staticmethod
    def get_from_database():
        personRequested = Utility.get_person_from_db()
        data : dict = Utility.get_persons_data(personRequested)
        if data != NO_DATA:
            dataStr = '\n'.join(data.keys())
            dataRequested = Utility.assertValidAnswer('Please input the data type you want to retrieve: ', f'Please input a piece of data from the database\nOptions are {dataStr}', 'inp in condList', data.keys()) 
            dataRetrieved = data[dataRequested]

        else:
            dataRetrieved = data

        print(dataRetrieved)
        wait()
        
    @staticmethod    
    def add_data():
        lines = Utility.get_database()
        personsStr = '\n'.join(Utility.get_database(1))
        if personsStr == NO_DATA:
            print('Noone in database')
            wait()
            return
        
        personRequested = Utility.get_person_from_db()
        try: dataDict : dict = Utility.get_persons_data(personRequested)
        except: dataDict = NO_DATA

        if dataDict != NO_DATA:
            dataType = Utility.assertValidAnswer('Please input the type of data you want to add: ', f'Please input a data type not currently available\nOptions are {dataDict.keys()}', 'inp.capitalize() not in condList', dataDict.keys()).capitalize()
            dataValue = Utility.assertValidAnswer('Please input the value you want to populate this data type with: ', '', 'True')
            
            dataDict[dataType] = dataValue
            
            dataStr = '{' + ','.join([f'\'{k}\' : \'{v}\'' for k,v in dataDict.items()]) + '}'

        else:
            dataType = Utility.assertValidAnswer('Please input the type of data you want to add: ', '', 'True').capitalize()
            dataValue = Utility.assertValidAnswer('Please input the value you want to populate this data type with: ', '', 'True')

            dataStr = '{' + f'\'{dataType}\' : \'{dataValue}\'' + '}'            
        
        index = Utility.get_person_ID(personRequested)
        lines[index] = f'{personRequested}/{dataStr}\n'

        with open(DATABASE,'w') as database:
            database.writelines(lines)
            print(f'{dataType} with a value of {dataValue} was added to {personRequested} successfully')
            wait()
            
    @staticmethod
    def remove_data():
        try:
            personRequested = Utility.get_person_from_db()
            dataDict : dict = Utility.get_persons_data(personRequested)
            dataType = Utility.assertValidAnswer('Please input the type of data you want to remove: ', f'Please input a data type currently available\nOptions are {dataDict.keys()}', 'inp.capitalize() in condList', dataDict.keys()).capitalize()
            
            dataDict.pop(dataType)
            lines = Utility.get_database()
            dataAsStr = Utility.dict_to_str(dataDict)
            if dataAsStr == '{}': dataAsStr = ''
            lines[Utility.get_person_ID(personRequested)] = f'{personRequested}/{dataAsStr}\n'

            with open(DATABASE,'w') as database:
                database.writelines(lines)

        except DBException as e:
            print(e.message)
            wait()   

    @staticmethod
    def change_data():
        try:
            personRequested = Utility.get_person_from_db()
            dataDict : dict = Utility.get_persons_data(personRequested)
            dataType = Utility.assertValidAnswer('Please input the type of data you want to change: ', f'Please input a data type currently available\nOptions are {dataDict.keys()}', 'inp.capitalize() in condList', dataDict.keys()).capitalize()
            newVal = Utility.assertValidAnswer('Please input the value you want to change the data to: ', '', 'True')
            dataDict[dataType] = newVal
            print(dataDict)
            lines = Utility.get_database()
            dataAsStr = Utility.dict_to_str(dataDict)
            lines[Utility.get_person_ID(personRequested)] = f'{personRequested}/{dataAsStr}\n'

            with open(DATABASE,'w') as database:
                database.writelines(lines)

        except DBException as e:
            print(e.message)
            wait()   

    @staticmethod
    def retrieve_data():
        try:
            personRequested = Utility.get_person_from_db()
            dataDict : dict = Utility.get_persons_data(personRequested)
            dataType = Utility.assertValidAnswer('Please input the type of data you want to retrieve: ', f'Please input a data type currently available\nOptions are {dataDict.keys()}', 'inp.capitalize() in condList', dataDict.keys()).capitalize()
            
            print(f'Requested data from category {dataType} has value {dataDict[dataType]}')
            wait()

        except DBException as e:
            print(e.message)
            wait()   

    #Utility methods
    @staticmethod
    def print_database():
        names : list[str]= Utility.get_database(1)
        for name in names:
            try: data : dict = Utility.get_persons_data(name)
            except NoDataException: data = NO_DATA
            print('-' * 20)
            print(f'Name {name}\nData: ')
            if data != NO_DATA:
                for k,v in data.items():
                    print(f'{k} : {v}')
            
            else: print(NO_DATA)
            print('-' * 20)

        wait()    

    @staticmethod
    def clear_database():
        with open(DATABASE,'w') as database:
                pass

def people_in_database():
    prompt = 'Please pick an option'
    options = [('Add person in database','DatabaseMethods.add_to_database()'),
               ('Remove person in database','DatabaseMethods.remove_from_database()'),
               ('Change name of person in database','DatabaseMethods.change_name_in_database()')]
    
    mode = Utility.present_menu(prompt,[x[0] for x in options])
    exec(options[mode - 1][1])

def data_in_database():
    prompt = 'Please pick an option'
    options = [('Add data to a person in database','DatabaseMethods.add_data()'),
               ('Remove data from a person in database', 'DatabaseMethods.remove_data()'),
               ('Retrieve data from a person in database', 'DatabaseMethods.retrieve_data()'),
               ('Change data from a person in database','DatabaseMethods.change_data()')]
    
    mode = Utility.present_menu(prompt,[x[0] for x in options])
    exec(options[mode - 1][1])

def wait():
    input('Press Enter to continue')

def main():
    global DATABASE
    global NO_DATA
    NO_DATA = 'No Data'
    cwd = os.getcwd() 
    DATABASE = cwd + '\database.txt'
    print('Elliot\'s database')
    while True:
        prompt = '\nChoose your preferred action (input ; to exit at any time)'
        modes = [('Add/Remove/Change people from database','people_in_database()'),
                 ('Add/Remove/Retrieve/Change data from a person in the database', 'data_in_database()'),
                 ('Print database','DatabaseMethods.print_database()'),
                 ('Clear database','DatabaseMethods.clear_database()\nquit()'),
                 ('Leave database','quit()')]
        
        mode = Utility.present_menu(prompt,[x[0] for x in modes])
        #print(modes[mode-1])
        exec(modes[mode - 1][1])

if __name__ == '__main__':
    main()