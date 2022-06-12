from tkinter import *

root = Tk()

label1 = Label(root, text="Learn More", bg="red", fg="white")
label1.pack(fill=X)
label2 = Label(root, text="Learn More", bg="blue", fg="white")
label2.pack(side =LEFT,fill=Y)
root.mainloop()