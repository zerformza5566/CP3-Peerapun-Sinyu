class Customer:
    customerName = ""
    customerLastName = ""
    customerAge = 0

    def addCart(self):
        print("Added product to", self.customerName.capitalize(), self.customerLastName.capitalize(), "'s Cart")

customer1 = Customer()
customer1.customerName = "peerapun"
customer1.customerLastName = "sinyu"
customer1.addCart()

customer2 = Customer()
customer2.customerName = "peerapong"
customer2.customerLastName = "sinyu"
customer2.addCart()

customer3 = Customer()
customer3.customerName = "annika"
customer3.customerLastName = "ma-in"
customer3.addCart()

customer4 = Customer()
customer4.customerName = "Tom"
customer4.customerLastName = "CHUTIMAN"
customer4.addCart()