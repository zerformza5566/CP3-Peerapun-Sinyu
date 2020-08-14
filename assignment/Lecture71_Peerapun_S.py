menuList = []
menuPriceList = []

def showBill():
    totalPrice = 0
    print("---- Food ----")
    for number in range(len(menuList)):
        print("Menu :", menuList[number], "| Price :", menuPriceList[number])
        totalPrice += menuPriceList[number]
    print("Total :", totalPrice)

while True:
    menuInput = input("Please Enter Menu : ")
    if menuInput.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuInput)
        menuPriceList.append(menuPrice)

showBill()