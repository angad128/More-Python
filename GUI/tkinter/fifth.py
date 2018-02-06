# Binding function to layout

# importing our inbuilt tkinter package
from tkinter import *

root  = Tk()

def printName():
	print("Hello my name is Angad!")

btn1 = Button(root,command=printName , text="Hello", bg="green", fg="white")
btn1.pack()

root.mainloop()