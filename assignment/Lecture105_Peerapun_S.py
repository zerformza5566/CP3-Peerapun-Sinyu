class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirCondition(self):
        print("Turn On : Air")

class Cars(Vehicle):
    pass

class Pickup(Vehicle):
    pass

class Van(Vehicle):
    pass

van1 = Van()
van1.turnOnAirCondition()


car1 = Cars()
car1.turnOnAirCondition()


pickup1 = Pickup()
pickup1.turnOnAirCondition()
