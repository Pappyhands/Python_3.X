# Description: This is a program being designed to streamline the pre-build
# interview process.
#
# Version: 1.0 (7/22/2017)
#
# Bug Fix(es): N/A
#
# Created by Austin Thompson
# Started on July 22nd, 2017

# import all used libraries
from functions import *
from os.path import *
# be sure to format data before writing it. This might not be the best to way
# to actually do this but I think it is a good way to break apart the functionality
def saveFile(fileName, data):
    # this is saving all output files to the 'output' directory within the program
    fullPath = join('output/', fileName + ".txt")
    # 'w+' implements the creation of a new file (ie. You are WRITING to a NEW file)
    with open(fullPath, "w+") as text_file:
        text_file.write(data)

# opening dialogue
def openingPrompt():
    # cleaner way of doing this has to exist.
    print("Welcome to Interview Assistant v1.0")

# only supports first & last names
def getValidName():
    nameTest = False
    while not nameTest:
        name = userString("Name?: ").title()
        firstLast = name.split(" ")
        if len(firstLast) == 2:
            nameTest = True
    return firstLast

def checkLocation():
    locTest = False
    while not locTest:
        location = userString("Location?: ").upper()
        if len(location) == 2:
            locTest = True

    return location


def addList(msg, error):
    stuff = []
    keepGoing = True
    while keepGoing:
        stuff.append(userString(msg))
        keepGoing = False if userString(error).upper() == 'N' else True
    return stuff


# changed this to return a dictonary
def questions():
    data = {}
    data.update({"Location" : checkLocation()})
    data.update({"Programs" : addList("Additional Program(s)?: ", "Add another program? (Y/N)")})
    data.update({"Printers" : addList("Additional Printer(s)?: ", "Add another printer? (Y/N)")})
    data.update({"Notes" : userString("Additional Notes: ")})
    return data

# THIS IS THE FULL PROGRAM MY DUDE
def runProgram():
    openingPrompt()
    fullName = getValidName()
    answers = questions()
    fileName = answers["Location"] + "_" + fullName[1]
    data = formatData(fullName, answers)
    return fileName, data

#
def formatData(fullName, answers):
    return "Name: %s \nLocation: %s\nPrograms Needed: %s\nPrinters: %s\nAdditional Notes: %s" % (fullName, answers["Location"], answers["Programs"], answers["Printers"], answers["Notes"])

# main function, currently building the prompt in here.
def main():
    fileName, data = runProgram()
    saveFile(fileName,data)

main()
