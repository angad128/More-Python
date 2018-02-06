# Organizing our Layout

from tkinter import *

root = Tk()

# creating invisible window in our main screen
topframe = Frame(root)
topframe.pack()
# creating another invisible window in our main screen and putting it in bottom.
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

btn1 = Button(topframe, text="Button 1", fg="red")
btn2 = Button(topframe, text="Button 2", fg="green")
btn3 = Button(topframe, text="Button 3", fg="blue")
btn4 = Button(bottomframe, text="Button 4", fg="green")

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack()

root.mainloop()