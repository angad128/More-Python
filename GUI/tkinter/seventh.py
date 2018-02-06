# Mouse Click Events

# importing our inbuilt tkinter package
from tkinter import *

root  = Tk()


def leftClick(event):
	print("This is Left Click!")

def middleClick(event):
	print("This is Left Click!")

def rightClick(event):
	print("This is Right Click!")

frame = Frame(root, width=300, height= 200, bg="black")
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",rightClick)

frame.pack()

root.mainloop()