class PhoneBattery :
    def __init__(self) :
        self.__percent = 100
    
    def use_battery(self,amount) :
        if amount > self.__percent :
            self.__percent = 0
        else :
            self.__percent -= amount
    
    def charge_battery(self,amount) :
        if amount + self.__percent > 100 :
            self.__percent = 100
        else :
            self.__percent += amount
            
    def getPercent(self) :
        return self.__percent

myBattery = PhoneBattery()
print(f"Now myBattery is : {myBattery.getPercent()}\n")

print("Trying to use battery....")
myBattery.use_battery(53)
print(f"Now myBattery is : {myBattery.getPercent()}\n")
print("Trying to use battery....")
myBattery.use_battery(70)
print(f"Now myBattery is : {myBattery.getPercent()}\n")

print("Trying to charge battery....")
myBattery.charge_battery(32)
print(f"Now myBattery is : {myBattery.getPercent()}\n")

print("Trying to charge battery....")
myBattery.charge_battery(49)
print(f"Now myBattery is : {myBattery.getPercent()}\n")

print("Trying to charge battery....")
myBattery.charge_battery(50)
print(f"Now myBattery is : {myBattery.getPercent()}\n")
print(f"{myBattery.__percent}")
