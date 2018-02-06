from tkinter import *

def doNothing():
	print("Okay, I wont..")


root = Tk()

# ** Main Menu ** # 
menu = Menu(root)

root.config(menu=menu) # configuring menu with root

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


# *** The Toolbar *** #
toolbar = Frame(root, bg="blue")

btn_1 = Button(toolbar,text="Insert Image",command=doNothing)
btn_1.pack(side=LEFT, padx=2, pady=2)
btn_2 = Button(toolbar,text="Print",command=doNothing)
btn_2.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


root.mainloop()