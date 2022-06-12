from tkinter import *
class mybutton:
    def __init__(self, root1):
        frame = Frame(root1)   #create window
        frame.pack()

        self.printButton = Button(frame, text= "click here", command=self.printMessage)
        self.printButton.pack()

        self.quitButton = Button(frame, text = "Exit ", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Button clicked")

root = Tk()
b = mybutton(root)
root.mainloop()