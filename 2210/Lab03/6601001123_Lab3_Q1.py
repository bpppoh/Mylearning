import math

try :
    print("--- Circle Overlap Detector ---")
    x1 , y1 , r1 = input("Enter x , y and radius for Circle 1 : ").split()
    x1 = float(x1)
    y1 = float(y1)
    r1 = float(r1)
    
    x2 , y2 , r2 = input("Enter x , y and radius for Circle 2 : ").split()
    x2 = float(x2)
    y2 = float(y2)
    r2 = float(r2)

    d = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    # print(d)
    sumOfRadius = r1 + r2
    if (d == sumOfRadius) :
        print("Touch")
    elif ( d < sumOfRadius) :
        print("Overlap")
    else :
        print("Free")
except :
    print("========================")
    print("Error occured")
    print("========================")