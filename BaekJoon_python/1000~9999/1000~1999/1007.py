import sys
import math
import itertools

T = int(sys.stdin.readline())
results = []
 
for _ in range(T) :
    N = int(sys.stdin.readline())
    coords = []
    
    xTotal = 0
    yTotal = 0
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        xTotal += x
        yTotal += y
        coords.append([x, y])
    
    res = math.inf
    combinations = list(itertools.combinations(coords, int(N/2)))
    l = int(len(combinations) / 2)
    for s in combinations[:l] :
        s = list(s)
 
        x1Total = 0
        y1Total = 0
        for x1, y1 in s :
            x1Total += x1
            y1Total += y1
        
        x2Total = xTotal - x1Total
        y2Total = yTotal - y1Total
        
        res = min(res, math.sqrt((x1Total - x2Total) ** 2 + (y1Total - y2Total) ** 2))
 
    results.append(res)
 
for result in results :
    sys.stdout.write(str(result)+'\n')