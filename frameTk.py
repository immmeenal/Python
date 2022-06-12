from tkinter import *
obj = Tk()
myframe = Frame(obj) #to add widgets it acts like container / rectangular area which organize the widgets
#widgets are objects which represent buttons and frames
myframe.pack()
otherframe = Frame(obj)
otherframe.pack(side=BOTTOM)
button1 = Button(myframe, text= "click here", fg="Red") #foreground-color
button2 = Button(otherframe, text= "click here", fg="Blue")
button1.pack()
button2.pack()
obj.mainloop()