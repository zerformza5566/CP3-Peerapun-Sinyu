menuList = []

def showBill():
    totalPrice = 0
    print("---- Food ----")
    for number in range(len(menuList)):
        print(menuList[number])
        totalPrice += menuList[number][1]
    print("Total :", totalPrice)

while True:
    menuName = input("Plese Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append([menuName,menuPrice])


showBill()