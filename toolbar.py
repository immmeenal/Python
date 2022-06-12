from tkinter import *
def function1():
    print("Menu item  clicked")

root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Project",command=function1)
submenu.add_command(label="Save As",command=function1)

submenu.add_separator()

submenu.add_command(label="Exit",command=function1)

newmenu = Menu(mymenu)

mymenu.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="undo",command=function1)
#TOOLBAR
toolbar = Frame(root, bg = "pink")
insertbutton = Button(toolbar, text = "Insert Files", command = function1)
insertbutton.pack(side=LEFT, padx=7,pady=0)
printbutton = Button(toolbar, text = "Print", command = function1)
printbutton.pack(side=LEFT, padx=7,pady=9)
toolbar.pack(side= TOP,fill=X)

root.mainloop()