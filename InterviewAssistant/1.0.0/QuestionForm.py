from tkinter import *
import eventMethods

class QuestionForm:

    def __init__(self, root, title):

        root.geometry("300x800")

        data = [] # define this, was thinking about using it as a means to organzie information

        # main title
        header = Label(root, text=title, bg="black", fg="white", width=28)
        header.pack(fill=X)

        # creates 'frame' to seperate the title from questions
        frame = Frame(root)
        frame.pack()

        ########################################
        ########################################
        ########################################

        # Name Label
        name_label = Label(frame, text="Name: ")
        name_label.grid(row=0, column=0, sticky=E)
        # Name Entry
        name_entry = Text(frame, height=1, width=25)
        name_entry.grid(row=0, column=1)
        name_entry.focus_set()

        #--------------------------------------------

        # Location Label
        location_label = Label(frame, text="Location: ")
        location_label.grid(row=1, column=0, sticky=E)
        # Location Entry
        location_entry = Text(frame, height=1, width=25)
        location_entry.grid(row=1, column=1)

        #--------------------------------------------

        # question 1
        question_1 = Label(frame, text="question 1: ")
        question_1.grid(row=2, column=0, sticky=E)

        entry_1 = Text(frame, height=2, width=30)
        entry_1.grid(row=2, column=1)


        def submitData(self):
            one = name_entry.get("1.0", "end-1c")
            two = location_entry.get("1.0", "end-1c")
            print(one + " " + two)

        # question 2
        question_2 = Label(frame, text="question 2: ")
        question_2.grid(row=3, column=0, sticky=E)

        entry_2 = Text(frame, height=2, width=30)
        entry_2.grid(row=3, column=1)

        # COMMENTED THIS OUT FOR NOW (12-15-17)
        # check box test
        # checkBox = Checkbutton(frame, text="Check this?").grid(columnspan=2)

        # submit Button
        submit = Button(frame, text="Submit", fg="black")
        submit.bind("<Button-1>", submitData)

        submit.grid(columnspan=2)
