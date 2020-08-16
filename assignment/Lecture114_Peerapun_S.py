from forex_python.converter import *
from tkinter import *
from tkinter import ttk
import math

currencyRate = CurrencyRates()
currencyCode = CurrencyCodes()

mainWindow = Tk()
mainWindow.iconbitmap("coin_icon.ico")
mainWindow.title("Currency Exchange.")
mainWindow.geometry("500x200")
mainWindow.resizable(width=False, height=False)

def currencyConvert(event):
    result = currencyRate.convert(currencyBox1.get(), currencyBox2.get(), float(moneyInput.get()))
    labelResult.configure(text=result)

labelFirstCurrency = Label(mainWindow, text="From : ")
labelFirstCurrency.place(x=20, y=20)
currencyBox1 = ttk.Combobox(mainWindow)
currencyBox1['values'] = list(currencyRate.get_rates("").keys())
currencyBox1.current(29)
currencyBox1.bind("<<ComboboxSelected>>")
currencyBox1.place(x=60, y=20)

labelSecondCurrency = Label(mainWindow, text="  To : ")
labelSecondCurrency.place(x=28, y=64)
currencyBox2 = ttk.Combobox(mainWindow)
currencyBox2['values'] = list(currencyRate.get_rates("").keys())
currencyBox2.current(10)
currencyBox2.bind("<<ComboboxSelected>>")
currencyBox2.place(x=60, y=64)

labelMoneyInput = Label(mainWindow, text="Amount of money : ")
labelMoneyInput.place(x=210, y=40)
moneyInput = Entry(mainWindow, width="15")
moneyInput.place(x=320, y=42)

convertButton = Button(mainWindow, text="Convert", height=2)
convertButton.place(x=420, y=32)
convertButton.bind("<Button-1>", currencyConvert)

labelText = Label(mainWindow, text="Result : ", font=("Times", 36), fg="black", bg="#FFFF66")
labelText.place(x=20, y=120)
labelResult = Label(mainWindow, text="", font=("Times", 36), fg="black", bg="#FFFF66")
labelResult.place(x=175, y=120)

mainWindow.mainloop()