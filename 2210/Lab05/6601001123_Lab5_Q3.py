import math

def distance1(x1,y1,x2,y2) :
    return math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))

def distance2(p1,p2) :
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

def distance3(c1,c2) :
    distance = math.sqrt(math.pow(c1[0]-c2[0],2)+math.pow(c1[1]-c2[1],2))
    return distance , (c1[2]+c2[2]<distance)
        
def perimeter(points) :
    total_dist = 0
    n = len(points)
    for i in range(n):
        total_dist += distance2(points[i], points[(i + 1) % n])
    return total_dist

print(distance1(0,0,3,4))
print(distance2([0,0],[3,4]))
a,b = distance3([0,0,1],[5,0,2])
print(a,b)
print(perimeter([[0,0],[0,2],[2,2],[2,0]]))