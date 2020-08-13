userName = input("Id : ")
password = input("Password : ")

if userName == "admin" and password == "1234":
    print("Login completed.")
    print("----FPStore----")
    print("-------Product list--------")
    print("1. Leather bag      : 150 THB")
    print("2. Backpack         : 199 THB")
    print("3. Wallet           : 220 THB")
    print("---------------------------")
    userSelectedProduct = int(input("ระบุสินค้าที่ต้องการ : "))
    if userSelectedProduct == 1:
        print("1. Leather bag")
        userQuantityProduct = int(input("จำนวนสินค้าที่ต้องการ : "))
        print("Leather bag", userQuantityProduct, "ชื้น เป็นเงิน:", 150 * userQuantityProduct)
    elif userSelectedProduct == 2:
        print("2. Backpack")
        userQuantityProduct = int(input("จำนวนสินค้าที่ต้องการ : "))
        print("Backpack", userQuantityProduct, "ชื้น เป็นเงิน:", 199 * userQuantityProduct)
    elif userSelectedProduct == 3:
        print("3. Wallet")
        userQuantityProduct = int(input("จำนวนสินค้าที่ต้องการ : "))
        print("Wallet", userQuantityProduct, "ชื้น เป็นเงิน:", 220 * userQuantityProduct)
    print("----ขอบคุณ----")
else:
    print("Incorrect Id/Password.")