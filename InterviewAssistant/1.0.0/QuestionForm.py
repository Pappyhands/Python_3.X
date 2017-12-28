from tkinter import *
import eventMethods

class QuestionForm:

    def __init__(self, root, title):

        formatted_title = title + '\n' + ("-"*60)
        error_msg = StringVar()
        # error_msg.set('')

        root.geometry("400x800")

        data = [] # define this, was thinking about using it as a means to organzie information

        # main title
        header = Label(root, text=formatted_title, bg="black", fg="white", width=28, height=2)
        header.pack(fill=X)

        # error message
        error = Label(root, textvariable=error_msg, bg="black", fg="white", width=28)
        error.pack(fill=X)

        # creates 'frame' to seperate the title from questions
        frame = Frame(root)
        frame.pack()

        ########################################
        ########################################
        ########################################

        # First Name Label
        Label(frame, text="First Name: ").grid(row=0, column=0, sticky=E)
        # First Name Entry
        first_name_entry = Text(frame, height=1, width=25)
        first_name_entry.grid(row=0, column=2)
        first_name_entry.focus_set()

        #--------------------------------------------

        # Last Name Label
        Label(frame, text="Last Name: ").grid(row=1, column=0, sticky=E)
        # Last Name Entry
        last_name_entry = Text(frame, height=1, width=25)
        last_name_entry.grid(row=1, column=2)
        last_name_entry.focus_set()

        #--------------------------------------------

        # Location Label
        Label(frame, text="Location: ").grid(row=2, column=0, sticky=E)
        # # Location Entry
        # location_entry = Menu(frame)
        # location_entry.grid(row=1, column=1)

        location_var = StringVar(root)

        location_choices = [  'Main Office',
                                'Bay State',
                                 'Wahconah',
                             'Byron Weston',
                                      'CTC',
                          'Human Resources',
                            'Old Berkshire',
                           'Transportation',
                                  'Pioneer',
                                    'Other' ]

        location_choices.sort()

        location_menu = OptionMenu(frame, location_var, *location_choices)
        location_var.set('Main Office') # set the default option
        location_menu.grid(row = 2, column =2, sticky="ew")

        # on change dropdown value
        def changeDropdown(*args):
            print( location_var.get() )
        #--------------------------------------------

        # would like to look into cleaning these conditional IF statements up
        def checkLocation(location):
            if location == 'Main Office':
                return 'MO'
            elif location == 'Bay State':
                return 'BS'
            elif location == 'Wahconah':
                return 'WAH'
            elif location == 'Byron Weston':
                return 'BW'
            elif location == 'CTC':
                return 'CTC'
            elif location == 'Human Resources':
                return 'HR'
            elif location == 'Old Berkshire':
                return 'OB'
            elif location == 'Transportation':
                return 'TRP'
            elif location == 'Pioneer':
                return 'PIO'
            elif location == 'Other':
                return 'OTH'

        def checkName():
            if len(first_name_entry.get("1.0", "end-1c")) < 1:
                error_msg.set("*ERROR: First Name Required!*")
                return False
            elif len(last_name_entry.get("1.0", "end-1c")) < 1:
                error_msg.set("*ERROR: Last Name Required!*")
                return False
            else:
                error_msg.set("")
                return True

        # THIS IS WHERE THE MAGIC HAPPENS
        def submitData(self):
            fileName = ""
            if checkName():
                NAME = last_name_entry.get("1.0", "end-1c")
                LOCATION = location_var.get()

                fileName += checkLocation(LOCATION)
                temp = NAME.split(" ")
                fileName += "_" + temp[0]
                print(fileName)




        # # question 1
        # question_1 = Label(frame, text="question 1: ")
        # question_1.grid(row=2, column=0, sticky=E)
        #
        # entry_1 = Text(frame, height=2, width=30)
        # entry_1.grid(row=2, column=1)
        #

        # # question 2
        # question_2 = Label(frame, text="question 2: ")
        # question_2.grid(row=3, column=0, sticky=E)
        #
        # entry_2 = Text(frame, height=2, width=30)
        # entry_2.grid(row=3, column=1)

        # COMMENTED THIS OUT FOR NOW (12-15-17)
        # check box test
        # checkBox = Checkbutton(frame, text="Check this?").grid(columnspan=2)

        # submit Button
        submit = Button(root, text="Submit", fg="black")
        submit.pack(side = BOTTOM)
        submit.bind("<Button-1>", submitData)

        tab_order = (first_name_entry, last_name_entry, location_menu)

        for widget in tab_order:
            widget.lower()
