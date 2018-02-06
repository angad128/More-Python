from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Wintow title', 'IT is tkinter messagebox like JS alertbox.')

answer = tkinter.messagebox.askquestion('Question 1', 'Do yo like it?')

if answer == 'yes':
	print(' B==D ' )

root.mainloop()