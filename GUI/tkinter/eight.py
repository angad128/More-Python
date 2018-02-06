# Using Classes
from tkinter import *

class MyButtons:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.btn_1 = Button(frame, text="Print", command= self.printMessage)
		self.btn_1.pack(side=LEFT)
		self.btn_2 = Button(frame, text="Exit",command= frame.quit)
		self.btn_2.pack(side=LEFT)

	def printMessage(slef):
		print("Hello World Message!")



root = Tk()
ob = MyButtons(root)
root.mainloop()