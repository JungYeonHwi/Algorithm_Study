import math

for _ in range(int(input())) : 
    a1, p1 = map(int, input().split(" "))
    r1, p2 = map(int, input().split(" "))
    
    if (a1 / p1) < (r1**2 * math.pi / p2) : print("Whole pizza")
    else : print("Slice of pizza")
    