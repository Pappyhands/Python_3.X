from tkinter import *
from QuestionForm import *

# main window
root = Tk()
root.title("INTERVIEW ASSISTANT v1.0.0")
root.wm_iconbitmap('favicon.ico')

b = QuestionForm(root, "INTERVIEW ASSISTANT v1.0.0")


# displays main window
root.mainloop()
