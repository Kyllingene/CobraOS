from os.path import isfile
import json
import tkinter as tk

textEditorWindow = tk.Tk()
textEditorWindow.title('Text Editor - CobraOS')

#Main File Editation
enterToFile = tk.Frame(height=300, width=200, master=textEditorWindow)

namelab = tk.Label(text='Enter Filename Here (WITH EXTENSION)', master=enterToFile)
nameent = tk.Entry(master=enterToFile)

textlab = tk.Label(text='Enter Text Here', master=enterToFile)
textwindow = tk.Text(master=enterToFile)

filename = ''
text = ''

namelab.pack()
nameent.pack()

textlab.pack()
textwindow.pack(padx=5,pady=5)

#File Options
optionsFrame = tk.Frame(height=300, width=100, master=textEditorWindow)

option = tk.IntVar(value=1,master=textEditorWindow)
optionslab = tk.Label(text='File Mode:', master=optionsFrame)
O1 = tk.Radiobutton(master=optionsFrame, text='Read', variable=option,value=1)
O2 = tk.Radiobutton(master=optionsFrame, text='Write', variable=option,value=2)
O3 = tk.Radiobutton(master=optionsFrame, text='Append', variable=option,value=3)
optionslab.pack()
O1.pack(anchor=tk.W)
O2.pack(anchor=tk.W)
O3.pack(anchor=tk.W)
O1.invoke()

enterToFile.pack(side=tk.RIGHT)
optionsFrame.pack(side=tk.RIGHT)

f = open(r'TextFiles\Text Editor\instructions.txt')
textwindow.insert('1.0', f.read())
f.close()

def writeFile():
	global filename
	global text
	global textwindow
	filename = nameent.get()
	text = textwindow.get('1.0', tk.END)
	mode = option.get()
	print(mode, '-', option.get())
	
	if mode == 1:
		if isfile(filename):
			textwindow.delete('1.0', tk.END)
			f = open(filename, 'r')
			text = f.read()
			f.close()
			textwindow.insert('1.0', text)
		else:
			textwindow.insert('1.0', "The file does not exist.")
	elif mode == 2:
		f = open(filename, 'w')
		f.write(text)
		f.close()
	elif mode == 3:
		if isfile(filename):
			f = open(filename, 'a')
			f.write(text)
			f.close()
		else:
			textwindow.insert('1.0', "The file does not exist.")

finbut = tk.Button(text='Commit', master=optionsFrame, command=writeFile)
finbut.pack(padx=5,pady=5)

textEditorWindow.mainloop()