#Imports
import tkinter as tk
from runpy import run_module
import json 
from random import randint
from os.path import isfile

#Trying to load the users file


users = None

def writeUsers():
	f = open(r'TextFiles\users.json', 'w')
	f.write(json.dumps(users))
	f.close()

def getUsers():
	global users
	f=open(r'TextFiles\users.json', 'r')
	users=json.loads(f.read())
	f.close()

def makeUsers():
	global users
	f=open(r'TextFiles\users.json', 'x')
	f.close()
	users={'cobraos':'admin'}
	writeUsers()

if isfile(r'TextFiles\users.json'):
	getUsers()
else:
	makeUsers()

#Loading dictionary file (used for wotd)
f = open(r'TextFiles\dictionary.json')
dictionary = json.loads(f.read())
f.close()
wordNum = randint(0, len(dictionary)-1)
wotd = dictionary[wordNum]

end = False

#Sets up the tkinter interface
windowMain = tk.Tk()
windowMain.title(f"Cobra OS - {wotd}")

	#Sets up the login stuff
padX, padY = 3, 3 
loginFrame = tk.Frame(master = windowMain)

username = None
password = None
new = tk.BooleanVar()

def login():
	global username
	global password
	global new
	username = user_ent.get()
	password = pass_ent.get()

	if new.get() != True:
		if username in users:
			if users.get(username) == password:
				loginFrame.pack_forget()
				mainFrame.pack()
			else:
				failnew_lab.pack_forget()
				fail_lab.pack_forget()
				fail_lab.pack(padx=6,pady=6)
		else:
			failnew_lab.pack_forget()
			fail_lab.pack_forget()
			fail_lab.pack(padx=6,pady=6)
	else:
		if username not in users:
			users.update({username:password})
			writeUsers()
			loginFrame.pack_forget()
			mainFrame.pack()
		else:
			fail_lab.pack_forget()
			failnew_lab.pack_forget()
			failnew_lab.pack(padx=6,pady=6)

user_lab = tk.Label(master = loginFrame, text = "Username:")
user_ent = tk.Entry(master = loginFrame)

pass_lab = tk.Label(master = loginFrame, text = "Password:")
pass_ent = tk.Entry(master = loginFrame)

ent_but = tk.Button(text="Enter", command=login, master=loginFrame)

new_lab = tk.Label(text='Create new user?', master=loginFrame)
new_cbut = tk.Checkbutton(variable=new, onvalue=True,offvalue=False, master=loginFrame)

fail_lab = tk.Label(text = 'Username or password was incorrect. Please try again.', master = loginFrame)
failnew_lab = tk.Label(text='User already exists.', master = loginFrame)

user_lab.pack()
user_ent.pack()
pass_lab.pack()
pass_ent.pack()
ent_but.pack()
new_lab.pack(pady=8)
new_cbut.pack(pady=8)



	#Sets up the main pages stuff:
	
def logout():
	global username
	global password
	username = None
	password = None
	mainFrame.pack_forget()
	loginFrame.pack()
	
def runTors():
	run_module('totyp')
	
def runText():
	run_module('textEditor')

mainFrame = tk.Frame(master = windowMain)
padx, pady = 4, 4

title_lab = tk.Label(text = 'Cobra OS', master = mainFrame, padx=padx, pady=pady)
usershow_lab = tk.Label(text=username, master=mainFrame)
text_but = tk.Button(text='Text Editor', command=runText, master=mainFrame, padx=padx, pady=pady)
tors_but = tk.Button(text='Torus Typer', command=runTors, master=mainFrame, padx=padx, pady=pady)

sign_but = tk.Button(text='Sign Out', command=logout, master=mainFrame, padx=padX, pady=padY)

title_lab.pack()
usershow_lab.pack()
text_but.pack()
tors_but.pack()

sign_but.pack()


logout()
#Loop
windowMain.mainloop()
