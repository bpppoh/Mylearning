import math

try :
    userInput = input("Enter coefficients a,b,c : ").split(',')
    a = float(userInput[0])
    b = float(userInput[1])
    c = float(userInput[2])

    sqrtPart = math.sqrt((b**2) - (4*a*c))
    # print(sqrtPart)
    firstPossible = (-b + sqrtPart)/(2*a)
    secondPossible = (-b - sqrtPart)/(2*a)
    print(f"x = {firstPossible} , {secondPossible}")
except :
    print("Programme Error Please try again")