from tkinter import *
from os.path import *

class QuestionForm:

    def __init__(self, root, title):

        formatted_title = title + '\n' + ("-"*60)
        error_msg = StringVar()
        # error_msg.set('')

        root.geometry("700x800")

        data = [] # define this, was thinking about using it as a means to organzie information

        # main title
        header = Label(root, text=formatted_title, bg="black", fg="white", width=28, height=2)
        header.pack(fill=X)

        # error message
        error = Label(root, textvariable=error_msg, bg="black", fg="red", width=28)
        error.pack(fill=X)

        # creates 'frame' to seperate the title from questions
        frame = Frame(root)
        frame.pack()

        ########################################
        ########################################
        ########################################

        #--------------------------------------------

        Label(frame).grid(row=0, column=0)

        # First Name Label
        Label(frame, text="First Name: ").grid(row=1, column=0, sticky=E)
        # First Name Entry
        first_name_entry = Text(frame, height=1, width=25)
        first_name_entry.grid(row=1, column=1)
        first_name_entry.focus_set()

        Label(frame).grid(row=2, column=0)

        #--------------------------------------------

        # Last Name Label
        Label(frame, text="Last Name: ").grid(row=3, column=0, sticky=E)
        # Last Name Entry
        last_name_entry = Text(frame, height=1, width=25)
        last_name_entry.grid(row=3, column=1)

        Label(frame).grid(row=4, column=0)



        # THIS IS OUT OF ORDER ON PURPOSE BECAUSE THE FUNCTION CALL ISN'T DESIGNED THE BEST
        #--------------------------------------------

        Label(frame, text="Other: ").grid(row=6, column=0, sticky=E)
        # Other Location Entry
        other_location_entry = Text(frame, height=1, width=25, bg='light grey', state=DISABLED)
        other_location_entry.grid(row=6, column=1)

        def otherCheck(location):
            if location == "Other":
                other_location_entry.config(bg='white')
                other_location_entry.config(state=NORMAL)
            else:
                other_location_entry.config(bg='light grey')
                other_location_entry.config(state=DISABLED)

        #--------------------------------------------

        # OUT OF ORDER ON PURPOSE, SEE ABOVE COMMENT
        # Location Label
        Label(frame, text="Location: ").grid(row=5, column=0, sticky=E)
        location_var = StringVar(root)

        location_choices = ['Main Office',
                            'Bay State',
                            'Wahconah',
                            'Byron Weston',
                            'CTC',
                            'Human Resources',
                            'Old Berkshire',
                            'Transportation',
                            'Pioneer',
                            'Other']

        location_choices.sort()

        location_menu = OptionMenu(frame, location_var, *location_choices, command=otherCheck)

        location_menu.config(bg = "LIGHT GREY")
        location_var.set('Main Office') # set the default option
        location_menu.grid(row =5, column =1, sticky="ew")
        location_menu.update()

        #--------------------------------------------
        Label(frame).grid(row=7, column=0)

        # Applications  Label
        Label(frame, text="Applications: ").grid(row=8, column=0)

        # Applications Entry
        apps_entry = Text(frame, height=3, width=40)
        apps_entry.grid(row=8, column=1)
        Label(frame).grid(row=9, column=0)


        #--------------------------------------------
        # Computer Admin(s) Label
        Label(frame, text="Admin User(s): ").grid(row=15, column=0, sticky=E)
        # Computer Admins(s) Entry
        admins_entry = Text(frame, height=3, width=40)
        admins_entry.grid(row=15, column=1)
        Label(frame).grid(row=16, column=0)


        #--------------------------------------------
        # Printer(s) Label
        Label(frame, text="Printer(s): ").grid(row=17, column=0, sticky=E)
        # Printer(s) Entry
        printers_entry = Text(frame, height=3, width=40)
        printers_entry.grid(row=17, column=1)
        Label(frame).grid(row=18, column=0)

        #--------------------------------------------

        # Notes Label
        Label(frame, text="Notes: ").grid(row=19, column=0, sticky=E)
        # Notes Entry
        notes_entry = Text(frame, height=5, width=40)
        notes_entry.grid(row=19, column=1)


        #--------------------------------------------
        def saveFile(fileName, data):
            # this is saving all output files to the 'output' directory within the program
            fullPath = join('output/', fileName + ".txt")
            # 'w+' implements the creation of a new file (ie. You are WRITING to a NEW file)
            with open(fullPath, "w+") as text_file:
                text_file.write(data)

            error_msg.set("*SUCCESS: Text File Created.*")


        #--------------------------------------------
        # THIS IS WHERE THE MAGIC HAPPENS
        def submitData(self):
            fileName = ""
            # NAME = ""
            # LOCATION = ""

            if checkName() and checkLocation():
                NAME = last_name_entry.get("1.0", "end-1c")
                LOCATION = location_var.get()
                fileName += getLocation(LOCATION)
                temp = NAME.split(" ")
                fileName += "_" + temp[0]

                # print(fileName)
            data = "NAME:\n-----------------\n %s %s \n\nLOCATION:\n-----------------\n %s\n\nAPPLICATIONS:\n-----------------\n %s\n\nADMIN USER(S):\n-----------------\n %s\n\nPRINTER(S):\n-----------------\n %s\n\nNOTES:\n-----------------\n%s" % (first_name_entry.get("1.0", "end-1c"), last_name_entry.get("1.0", "end-1c"), LOCATION, apps_entry.get("1.0", "end-1c"), admins_entry.get("1.0", "end-1c"), printers_entry.get("1.0", "end-1c"), notes_entry.get("1.0", "end-1c"))

            saveFile(fileName, data)



        #--------------------------------------------

        # submit Button
        submit = Button(root, text="Submit", fg="black")
        submit.pack(side = BOTTOM, padx=20, pady=20)
        submit.bind("<Button-1>", submitData)
        #Test

        #--------------------------------------------
        def checkLocation():
            if location_var.get() == 'Other':
                if len(other_location_entry.get("1.0", "end-1c")) < 1:
                    error_msg.set("*ERROR: Location Required!*")
                    return False
                else:
                    error_msg.set("")
                    return True
            else:
                error_msg.set("")
                return True

        #--------------------------------------------

        # would like to look into cleaning these conditional IF statements up
        def getLocation(location):
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
                return other_location_entry.get("1.0", "end-1c")

        #--------------------------------------------

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

        #--------------------------------------------
