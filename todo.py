import argparse
import datetime
def createTask():
    subjectSwitch = False
    todotxt = open("todo.txt", "a")
    for i in range(len(subjectList)):
        if args.cr[0] == subjectList[i]:
            subjectSwitch = True
    if subjectSwitch == False:
        todotxt.close()
        parser.error("Please enter a valid subject: Maths, Physics, Computer Science, N/A, this would be your first argument")
    x = datetime.datetime.now()
    todotxt.write(args.cr[0] + "*" + args.cr[1] + "*" + args.cr[2] + "*" + "Date assigned: " + x.strftime("%d/%m/%Y") + "\n")
    todotxt.close()
    sortTasks()
def deleteTask():
    pass
def viewTasks():
    pass
def searchTask():
    pass
def splitTask():
    pass
def editTask():
    pass
def sortTasks():
    f = open("todo.txt")
    file = f.read()
    f.close()
    file = file.splitlines()
    for i in range(len(file)):
        file[i] = file[i].split("*")
    print(file)
parser = argparse.ArgumentParser()
subjectList = ["Maths", "Physics", "Computer Science", "N/A"]
parser.add_argument ("--cr", nargs = 3, help = "Create a new task")
args = parser.parse_args()
if args.cr:
    createTask()