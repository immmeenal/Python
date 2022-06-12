from tkinter import *


root = Tk()

def yo():
    print("you clicked the button")

button1 = Button(root, text = "Click here" , command= yo)
button1.pack()






root.mainloop()