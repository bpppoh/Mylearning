points = [(5, 2), (3, 8), (4, 4), (3, 9), (25, 5), (10, 1), (2, 4), (9, 3)]
print(f"Original Data : {points}")
print()

swappedPoint = []
for i in range(len(points)) :
    swappedPoint.append((points[i][1],points[i][0]))
print(f"a. Swapped (y,x): {swappedPoint}")

xMoreThanY = []
for i in range(len(points)) :
    item = points[i]
    if item[0] > item[1] :
        xMoreThanY.append(item)
print(f"b. Where x > y : {xMoreThanY}")

xLessThanY = []
for i in range(len(points)) :
    item = points[i]
    if item[0] < item[1] :
        xLessThanY.append(item)
print(f"c. Where x < y : {xLessThanY}")

xEqualY = []
for i in range(len(points)) :
    item = points[i]
    if item[0] == item[1] :
        xEqualY.append(item)
print(f"d. Where x == y : {xEqualY}")

xPowerEqualY = []
for i in range(len(points)) :
    item = points[i]
    if item[0]**2 == item[1] :
        xPowerEqualY.append(item)
print(f"e. Where x^2 = y : {xPowerEqualY}")

yPowerEqualX = []
for i in range(len(points)) :
    item = points[i]
    if item[1]**2 == item[0] :
        yPowerEqualX.append(item)
print(f"f. Where y^2 = x : {yPowerEqualX}")