from tkinter import *
import math

def leftClickButton(event):
    bmiResult = round(float(weightInput.get()) / math.pow(float(heightInput.get())/100, 2), 2)
    if bmiResult >= 30:
        labelResult.configure(text="อ้วนมาก")
    elif bmiResult >= 25:
        labelResult.configure(text="อ้วน")
    elif bmiResult >= 23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif bmiResult >= 18.6:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif bmiResult <= 18.5:
        labelResult.configure(text="ผอมเกินไป")
    bmiInfo.configure(text="BMI : " + str(bmiResult))

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่่วนสูง (cm.):")
labelHeight.grid(row=0, column=0)
heightInput = Entry(MainWindow)
heightInput.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (Kg.):")
labelWeight.grid(row=1, column=0)
weightInput = Entry(MainWindow)
weightInput.grid(row=1, column=1)
calButton = Button(MainWindow, text="คำนวณ")
calButton.bind("<Button-1>", leftClickButton)
calButton.grid(row=2, column=0)
bmiInfo = Label(MainWindow, text="BMI : ")
bmiInfo.grid(row=2, column=1)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=2)

MainWindow.mainloop()