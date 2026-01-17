filePath = input("Choose your movefile: ")

with open(filePath,'r',encoding='utf-8') as file :
    coordinate = input("Initial position: ")
    x,y = coordinate.split(',')
    x = int(x)
    y = int(y)
    for line in file.readlines() :
        line = line.strip()
        if line == "L" :
            x -= 1
        elif line == "R" :
            x += 1
        elif line == "U" :
            y += 1
        elif line == "D" :
            y -= 1
    print(f"Robot stop at {x},{y}")