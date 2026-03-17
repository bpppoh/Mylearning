import math

userInput = input("Enter coefficients a,b,c : ").split(',')
a = float(userInput[0])
b = float(userInput[1])
c = float(userInput[2])

checkNumber = (b**2)-(4*a*c)
if checkNumber >= 0 and a != 0 :
    correct = True
else :
    correct = False

print(f"Can use quadratic formula : {correct}")