from os.path import isfile
import json

file = input('File name (.txt, .json, .py): ')
mode = input('Input mode (w, a, r, r+, x): ')
stop = False

def writeToFile(filename, mode):
    file = open(filename, mode)
    stop = False
    while stop == False:
        text = input('>')
        if text == ':stop:':
            stop = True
        else:
            file.write('\n' + text)
    file.close()

if isfile(file) and mode == 'x':
    print('File already exists.')
else:
    f = open(file, mode)
if mode == 'r':
    print(f.read())
elif mode == 'w' or mode == 'a':
    while stop == False:
        text = input('>')
        if text == ':stop:':
            stop = True
        else:
            f.write('\n' + text)  
elif mode == 'r+':
    end = False
    while end == False:
        mode2 = input('Read, write or stop: ')
        mode2.lower()
        if mode2 == 'stop':
            end == True
        elif mode2 == 'read':
            print(f.read())
        else:
            writeToFile(file, 'w')
elif mode == 'x':
    if not isfile(file):  
        print('New file created.')
    write = input("Would you like to change the file? If so, type 'w' or 'a', depending on edit mode: ")
    if write == 'a':
        mode = 'a'
        writeToFile(file, mode)
    elif mode == 'w':
        mode = 'w'
        writeToFile(file, mode)