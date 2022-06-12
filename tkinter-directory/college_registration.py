from tkinter import *
root = Tk()
root.geometry("500x300")

def submit_val():
    print("Your information has been saved successfully")


Label(root, text="Registration Form", font="times 15 bold").grid(row=0, column=3)

id_user = Label(root, text="Student ID:")
id_user.grid(row=2, column=2)
name_user = Label(root, text="Student Name:")
name_user.grid(row=3, column=2)
course_user = Label(root, text="Course:")
course_user.grid(row=4, column=2)
fees_user = Label(root, text="Fees:")
fees_user.grid(row=5, column=2)


id_value = IntVar
name_value = StringVar
course_value = StringVar
fees_value = IntVar
check_me = IntVar


id_box = Entry(root, textvariable = id_value)
id_box.grid(row=2, column=3)
name_box = Entry(root, textvariable = name_value)
name_box.grid(row=3, column=3)
course_box = Entry(root, textvariable = course_value)
course_box.grid(row=4, column=3)
fees_box = Entry(root, textvariable = fees_value)
fees_box.grid(row=5, column=3)


checkbox = Checkbutton(text="Remember me?", variable=check_me)
checkbox.grid(row=7, column=3)

Button(text="Submit", command=submit_val).grid(row=8, column=3)



root.mainloop()