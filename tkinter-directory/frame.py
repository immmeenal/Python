from tkinter import *

root = Tk()

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="Click", fg="red")
button2 = Button(otherframe, text="Click", fg="green")

button1.pack()
button2.pack()


root.mainloop()