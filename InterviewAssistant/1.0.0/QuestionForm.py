from tkinter import *
from eventMethods import *

class QuestionForm:

    def __init__(self, root, title):
        # main title
        header = Label(root, text=title, bg="black", fg="white", width=28)
        header.pack(fill=X)

        # creates 'frame' to seperate the title from questions
        frame = Frame(root, width=400, height=500)
        frame.pack()

        # question 1
        question_1 = Label(frame, text="question 1: ")
        question_1.grid(row=0, column=0, sticky=E)

        entry_1 = Entry(frame)
        entry_1.grid(row=0, column=1)

        # question 2
        question_2 = Label(frame, text="question 2: ")
        question_2.grid(row=1, column=0, sticky=E)

        entry_2 = Entry(frame)
        entry_2.grid(row=1, column=1)

        # COMMENTED THIS OUT FOR NOW (12-15-17)
        # check box test
        # checkBox = Checkbutton(frame, text="Check this?").grid(columnspan=2)

        # submit Button
        submit = Button(frame, text="Submit", fg="black")
        submit.bind("<Button-1>", leftClick)
        submit.bind("<Button-2>", middleClick)
        submit.bind("<Button-3>", rightClick)
        submit.grid(columnspan=2)
