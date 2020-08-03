#Imports
from runpy import run_module
import json 
from random import randint
from os.path import isfile

#Checking and loading users file
if isfile(r'TextFiles\users.json'):
    f = open(r'TextFiles\users.json', 'r')
    users = json.loads(f.read())
    f.close()
else:
    raise FileNotFoundError(r"File 'TextFiles\users.json', file containing user data, was not found.")

#Loading dictionary file (used for wotd)
f = open('TextFiles\dictionary.json')
dictionary = json.loads(f.read())
f.close()
wordNum = randint(0, len(dictionary)-1)
wotd = dictionary[wordNum]

end = False

#Run cycle:
while end == False:

    end = False
    stop = False
    login = False

    #Login
    while login == False:
        username = input('Username: ')
        #If user inputs 'new':
        if username == 'new':
            username = input('Username: ')
            password = input('Password: ')
            #If the username doesn't currently exist:
            if users.get(username) == None:
                #Login, and add the user info to the users.json file, and edit the user.json file (used for games)
                login = True
                users.update({username: password})
                f = open(r'TextFiles\users.json', 'w')
                f.write(json.dumps(users))
                f.close()
                f = open(r'TextFiles\user.json', 'w')
                f.write(json.dumps('{"username":"%s"}' % username))
                f.close()
            else:
                print('')
                print('User already exists. Please sign in.')
        #If user enters 'exit':
        elif username == 'exit':
            end = True
            login = True
        #If the user types in a valid username:
        else:
            password = input('Password: ')
            if username in users:
                #If user exists, and password is correct:
                if users.get(username) == password:
                    login = True
                    f = open(r'TextFiles\user.json', 'w')
                    f.write(json.dumps('{"username":"%s"}' % username))
                    f.close()
                else:
                    print('')
                    print('Incorrect password or username. Please try again.')
            else:
                print('')
                print('No user by that name.')
    
    #Checks to see if 'end' is true, and ends the loop if it is:
    if end == True:
        continue
                
    print('')
    print('Welcome to Cobra OS')
    print('')
    print('Loading OS. . .')
    print('')
    print('')
    print('-------')

    print('   Cobra OS: Silent But Deadly'   )
    print('')
    print('---')
    print('The word of the day is:')
    print(wotd)
    print('---')
    print('')

    print('- Open Notepad')
    print('- Open Torus Typer')
    print('- Open Cards')
    print('- Open Credits')
    print('- Sign Out')
    print('-------')

    #Loop for input:
    while stop == False:
        print('')
        action = input(">> ")
        action = action.lower()
        notImplemented = ['open credits', 'open cards']
        #If the action does not exist yet:
        if action in notImplemented:
            print('')
            print('Feature not yet implemented. Please select a new action.')

    #If the action exists, then:
        #If action is 'sign out':
        elif action == 'sign out':
            print('')
            print('Signing out...')
            stop = True

        #If action is 'open notepad':
        elif action == 'open notepad':
            run_module('textEditor')
            
        #If action is 'open torus typer':
        elif action == 'open torus typer':
            run_module('tautyp')
            
        #If none of the above:
        else:
            print('')
            print('Command not recongized. Try rephrasing or respelling it.')

#Write the users dictionary to 'users.json' (for if you make a new user):
f = open(r'TextFiles\users.json', 'w')
f.write(json.dumps(users))
f.close()