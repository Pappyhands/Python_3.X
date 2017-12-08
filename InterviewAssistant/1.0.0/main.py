from tkinter import *

# main window
root = Tk()

# main title
header = Label(root, text="Interview Assistant v1.0.0", bg="black", fg="white", width=28)
header.pack(fill=X)

frame = Frame(root)
frame.pack()

question_1 = Label(frame, text="question 1: ").grid(row=0, column=0, sticky=E)
entry_1 = Entry(frame).grid(row=0, column=1)

question_2 = Label(frame, text="question 2: ").grid(row=1, column=0, sticky=E)
entry_2 = Entry(frame).grid(row=1, column=1)

checkBox = Checkbutton(frame, text="Check this?").grid(columnspan=2)

submit = Button(frame, text="Submit", fg="black").grid(columnspan=2)

# displays main window
root.mainloop()
