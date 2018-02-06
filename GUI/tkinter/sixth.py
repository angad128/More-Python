# Binding function to layout

# importing our inbuilt tkinter package
from tkinter import *

root  = Tk()

def printName(event):
	print("Hello my name is Angad!")

btn1 = Button(root, text="Hello", bg="green", fg="white")
# binding our printName function on event of left-mouse-click
btn1.bind("<Button-1>",printName)
btn1.pack()

root.mainloop()