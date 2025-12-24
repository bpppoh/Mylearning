try :
    distance = float(input("Enter travel distance (km.): "))
    carType = int(input("Enter the type of car : "))
    drivingPattern = int(input("Enter driving pattern : "))
    
    def fuelCalculation(carType,drivingPattern,distance) :
        if carType == 1 :
            if drivingPattern == 1 :
                return distance / 12
            else :
                return distance / 10
        elif carType == 2 :
            if drivingPattern == 1 :
                return distance / 10
            else :
                return distance / 8
        elif carType == 3 :
            if drivingPattern == 1 :
                return distance / 9
            else :
                return distance / 7
    
    print(f"Fuel required: {fuelCalculation(carType,drivingPattern,distance):.2f}")
            
except:
    print("========================")
    print("Error occured")
    print("========================")