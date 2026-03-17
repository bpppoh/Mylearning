filename = input('Enter filename: ')

with open(filename,'r') as file :
    lines = file.readlines()
    sum = 0
    for line in lines :
        data = line.strip().split(',')
        high = int(data[0])
        low = int(data[1])
        sum = abs(high-low)
    print(f"Average temperature difference: {sum/len(lines)}")