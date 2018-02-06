from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100 )
canvas.pack()

blackLine = canvas.create_line(0,0, 200,50)
redLine = canvas.create_line(0,100, 200,50, fill="red")

greenBox = canvas.create_rectangle(25,45, 100,40, fill="green")

#canvas.delete(greenBox)
#canvas.delete(ALL)

root.mainloop()