from tkinter import *

def doNothing():
	print("Okay, I wont..")


root = Tk()
menu = Menu(root)
# configuring menu with root
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New",command=doNothing)
subMenu.add_command(label="Open",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command= doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)
editMenu.add_command(label="Exit",command= doNothing)

root.mainloop()