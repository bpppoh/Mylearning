sides = [float(x) for x in input("Length of 3 sides : ").split(',')]
sides.sort()
# print(sides)
a = sides[0]
b = sides[1]
c = sides[2]
triangleCheck = (((a**2) + (b**2)) == (c**2))
print(f"Right triangle : {triangleCheck}")