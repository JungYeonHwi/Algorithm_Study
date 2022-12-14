T = int(input())

for _ in range(T) :
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planet = 0
    
    for _ in range(n) :
        px, py, radius = map(int, input().split())
        start = (((x1 - px) ** 2) + ((y1 - py) ** 2)) ** 0.5
        end = (((px - x2) ** 2) + ((py - y2) ** 2)) ** 0.5
        
        if start < radius and end < radius : pass
        elif start < radius : planet += 1
        elif end < radius : planet += 1
    
    print(planet)