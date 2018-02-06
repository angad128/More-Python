# Introduction

# importing our inbuilt tkinter package
from tkinter import *

# defining screen to dislpay our GUI
root  = Tk()


#setting some label
name = Label(root, text="My name is in label")
# displaying it randomly in screen.
name.pack()

# hold a screen continues to print out GUI
root.mainloop()