from tkinter import *

obj = Tk()

lable1 = Label(obj, text="Enter first name : ")
lable2 = Label(obj, text="Enter first name : ")


entery1 = Entry(obj)
entery2 = Entry(obj)

lable1.grid(row = 0, column = 0)
lable2.grid(row = 1, column = 0)

entery1.grid(row = 0, column = 1)
entery2.grid(row = 1, column = 1)

obj.mainloop()