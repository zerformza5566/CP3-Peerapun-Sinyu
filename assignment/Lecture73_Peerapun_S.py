systemMenu = {
    "ข้าวมันไก่": 40,
    "ข้าวไก่ทอด": 45,
    "ข้าวผสม": 60
}
menuList = []

def showBill():
    totalPrice = 0
    print("---- Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0], "| Price: ", menuList[number][1])
        totalPrice += menuList[number][1]
    print("Total :", totalPrice)

while True:
    menuName = input("Plese Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])


showBill()
print(menuList)
