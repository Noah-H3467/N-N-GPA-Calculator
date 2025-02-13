import tkinter as tk
from tkinter import *
class Weighted:
  def __init__(self, gradeRaw, credit, weight):
    self.gradeRaw = gradeRaw
    self.credit = credit
    self.weight = weight
  def addWeight(self):
    if self.gradeRaw != 0:
      if self.weight == "Honors":
        self.gradeRaw += 1
      elif self.weight == "AP":
        self.gradeRaw += 2
  def getGradePoint(self):
    global GP
    if self.gradeRaw == 14:
      GP = 5
    elif self.gradeRaw == 13:
      GP = 4.67
    elif self.gradeRaw == 12:
      GP = 4.33
    elif self.gradeRaw == 11:
      GP = 4
    elif self.gradeRaw == 10:
      GP = 3.67
    elif self.gradeRaw == 9:
      GP = 3.33
    elif self.gradeRaw == 8:
      GP = 3
    elif self.gradeRaw == 7:
      GP = 2.67
    elif self.gradeRaw == 6:
      GP = 2.33
    elif self.gradeRaw == 5:
      GP = 2
    elif self.gradeRaw == 4:
      GP = 1.67
    elif self.gradeRaw == 3:
      GP = 1.33
    elif self.gradeRaw == 2:
      GP = 1.00
    elif self.gradeRaw == 1:
      GP = 0.67
    else:
      GP = 0
  def GPtimesCredits(self, credit):
    self.gradePoint = GP * credit
    return self.gradePoint
class Unweighted:
  def __init__(self, uGP, credit):
    self.credit = credit
    self.uGP = uGP
  def GPtimesCredits(self, credit):
    self.gradePoint = self.uGP * credit
    return self.gradePoint

class Ready:
  def __init__(self, isGrade, isWeight, isCredit):
    self.grade = isGrade
    self.weight = isWeight
    self.credits = isCredit
    self.isCalculated = False

  def setGrade(self):
    self.grade = True

  def setWeight(self):
    self.weight = True

  def setCredits(self):
    self.credits = True

  def isReady(self):
    return (self.grade and self.weight and self.credits)

  def setCalculated(self):
    canMoveOn.isCalculated = True

def promptUser():
  global numCourses
  global canMoveOn
  numCourses += 1
  canMoveOn = Ready(False, False, False)
  print()
  print("Class #" + str(numCourses) + ": ")
  print("Use the bottons to enter the grade, number of credits, and Weight -'AP', 'Honors', 'Normal'- of your course.")
  print("If you are done entering information for that course, press DONE to move on.")
  print("Or, if you finished entering all your classes, press CALCULATE GPA. ")

def calculateGPA():
  global wGradePointList
  global creditsAggregation
  global gradePointList
  global canMoveOn
  global disp_Weighted
  global disp_Unweighted

  if (canMoveOn.isReady()):
    creditsAggregation += courseCredits
    c_weighted = Weighted(courseRaw, courseCredits, courseWeight)
    c_weighted.addWeight()
    c_weighted.getGradePoint()
    c_weighted.GPtimesCredits(courseCredits)
    wGradePointList.append(c_weighted.gradePoint)
    c_unweighted = Unweighted(uGP, courseCredits)
    c_unweighted.GPtimesCredits(courseCredits)
    gradePointList.append(c_unweighted.gradePoint)
    weights.set("")
    credits.set("")
    grades.set("")
    wGradePointSum = 0.0
    uGradePointSum = 0.0
    for i in range(len(wGradePointList)):
      wGradePointSum += wGradePointList[i]
    wGPA = wGradePointSum/creditsAggregation
    wGPA = round(wGPA*100)/100
    for i in range(numCourses):
      uGradePointSum += gradePointList[i]
    uGPA = uGradePointSum/creditsAggregation
    uGPA = round(uGPA*100)/100
    print()
    print("Your weighted GPA is " + str(wGPA))
    print("Your unweighted GPA is " + str(uGPA))
    disp_Weighted.set(str(wGPA))
    disp_Unweighted.set(str(uGPA))
    del wGPA
    del uGPA
    del c_weighted
    del c_unweighted

def grader(gradeDisp, wGradeRaw, uGradePoint):
  global courseRaw
  global uGP
  global canMoveOn
  grades.set(gradeDisp)
  courseRaw = wGradeRaw
  uGP = uGradePoint
  canMoveOn.setGrade()

def crediter(credit):
  global courseCredits
  global canMoveOn
  credits.set(credit)
  courseCredits = credit
  canMoveOn.setCredits()

def weighter(weight):
  global courseWeight
  global canMoveOn
  weights.set(weight)
  courseWeight = weight
  canMoveOn.setWeight()

def storeData():
  global canMoveOn
  global creditsAggregation
  global courseCredits
  global c_weighted
  global c_unweighted
  global gradePointList
  global wGradePointList
  if canMoveOn.isReady():
    creditsAggregation += courseCredits
    c_weighted = Weighted(courseRaw, courseCredits, courseWeight)
    c_weighted.addWeight()
    c_weighted.getGradePoint()
    c_weighted.GPtimesCredits(courseCredits)
    wGradePointList.append(c_weighted.gradePoint)
    c_unweighted = Unweighted(uGP, courseCredits)
    c_unweighted.GPtimesCredits(courseCredits)
    gradePointList.append(c_unweighted.gradePoint)
    del c_weighted
    del c_unweighted
    del canMoveOn
    weights.set("")
    credits.set("")
    grades.set("")
    promptUser()
  else:
    print("You must click all required buttons before moving on.")

def reset():
  global canMoveOn
  if canMoveOn.isCalculated:
    global c_weighted
    global c_unweighted
    del c_weighted
    del c_unweighted
  del canMoveOn
  global wGradePointList
  global creditsAggregation
  global gradePointList
  global globe
  weights.set("")
  credits.set("")
  grades.set("")
  globe = ''
  disp_Unweighted.set(globe)
  disp_Weighted.set(globe)
  wGradePointList = []
  gradePointList = []
  creditsAggregation = 0
  global courseGrade 
  global numCourses
  numCourses = 0
  global courseCredits
  courseCredits = 0
  global courseWeight
  courseWeight = "null"
  global courseRaw 
  courseRaw = 0
  global uGP
  uGP = 0.0
  for line in range(5):
    print()
  print("Welcome to the GPA Calculator with TKINTER.")
  promptUser()

gpawindow = Tk()
gpawindow.title('GPA Calculator')
gpawindow.geometry('550x300')
topFrame = Frame(gpawindow)
topFrame.grid(rowspan = 5, columnspan = 10)
topFrame.configure(bg = "black")
grades = StringVar()
output = Entry(topFrame, width = 6, justify = CENTER, font = ('Arial', 16, 'bold'), textvariable = grades)
output.grid(row = 1, column = 7)

credits = StringVar()
output = Entry(topFrame, width = 6, justify = CENTER, font = ('Arial', 16, 'bold'), textvariable = credits)
output.grid(row = 2, column = 7)

weights = StringVar()
output = Entry(topFrame, width = 6, justify = CENTER, font = ('Arial', 16, 'bold'), textvariable = weights)
output.grid(row = 3, column = 7)

disp_Weighted = StringVar()
output = Entry(topFrame, width = 5, justify = CENTER, font = ('Arial', 16, 'bold'), textvariable = disp_Weighted)
output.grid(row = 5, column = 2)

disp_Unweighted = StringVar()
output = Entry(topFrame, width = 5, justify = CENTER, font = ('Arial', 16, 'bold'), textvariable = disp_Unweighted)
output.grid(row = 5, column = 3)

aplus = Button(topFrame, text = 'A+', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('A+', 12, 4.0))
aplus.grid(row = 1, column = 1)

abutton = Button(topFrame, text = 'A', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('A', 11, 4.0))
abutton.grid(row = 1, column = 2)

aminus = Button(topFrame, text = 'A-', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('A-', 10, 3.67))
aminus.grid(row = 1, column = 3)

bplus = Button(topFrame, text = 'B+', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('B+', 9, 3.33))
bplus.grid(row = 2, column = 1)

bbutton = Button(topFrame, text = 'B', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('B', 8, 3.0))
bbutton.grid(row = 2, column = 2)

bminus = Button(topFrame, text = 'B-', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('B-', 7, 2.67))
bminus.grid(row = 2, column = 3)

cplus = Button(topFrame, text = 'C+', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('C+', 6, 2.33))
cplus.grid(row = 3, column = 1)

cbutton = Button(topFrame, text = 'C', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('C', 5, 2.0))
cbutton.grid(row = 3, column = 2)

cminus = Button(topFrame, text = 'C-', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('C-', 4, 1.67))
cminus.grid(row = 3, column = 3)

dplus = Button(topFrame, text = 'D+', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('D+', 3, 1.33))
dplus.grid(row = 4, column = 1)
dbutton = Button(topFrame, text = 'D', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('D', 2, 1.00))
dbutton.grid(row = 4, column = 2)
dminus = Button(topFrame, text = 'D-', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('D-', 1, 0.67))
dminus.grid(row = 4, column = 3)
fbutton = Button(topFrame, text = 'F', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: grader('F', 0, 0.0))
fbutton.grid(row = 4, column = 4)
twobutton = Button(topFrame, text = '2', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: crediter(2))
twobutton.grid(row = 1, column = 4)
onebutton = Button(topFrame, text = '1', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: crediter(1))
onebutton.grid(row = 2, column = 4)
halfbutton = Button(topFrame, text = '1/2', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: crediter(0.5))
halfbutton.grid(row = 3, column = 4)
apbutton = Button(topFrame, text = 'AP', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: weighter('AP'))
apbutton.grid(row = 1, column = 5)
honorsbutton = Button(topFrame, text = 'Honors', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: weighter('Honors'))
honorsbutton.grid(row = 2, column = 5)
cpbutton = Button(topFrame, text = 'Normal', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: weighter('Normal'))
cpbutton.grid(row = 3, column = 5)
calcGPA = Button(topFrame,text = 'Calculate GPA', fg = 'white', bg = 'black', width = 10, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = lambda: calculateGPA())
calcGPA.grid(row = 4, column = 7)
doneButton = Button(topFrame,text = 'Done', fg = 'white', bg = 'black', width = 4, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = storeData)
doneButton.grid(row = 4, column = 5)
restart = Button(topFrame,text = 'Restart', fg = 'white', bg = 'black', width = 10, height = 2, borderwidth = 5, font = ('Arial', 12, 'bold'), command = reset)
restart.grid(row = 5, column = 7)
weightedGPAlabel = tk.Label(text= 'Weighted', foreground = 'white', background = 'black', font=('Arial', 7, 'bold'))
unweightedGPAlabel = tk.Label(text= 'Unweighted', foreground = "white", background = 'black', font=('Arial', 7, 'bold', ))
weightedGPAlabel.grid(row = 4, column = 0)
unweightedGPAlabel.grid(row = 4, column = 4)
wGradePointList = []
gradePointList = []
creditsAggregation = 0
global courseGrade 
numCourses = 0
courseCredits = 0
courseWeight = "null"
global courseRaw 
courseRaw = 0
global uGP
uGP = 0.0
print("Welcome to the GPA Calculator with TKINTER.")
promptUser()
gpawindow.mainloop()