n = int(input())
a, b = map(int, input().split())
if n < 3 : 
    print(0)
    exit()
minX, minY, maxX, maxY = a, b, a, b

for i in range(n-1) :
    a, b=map(int, input().split())
    minX = min(minX, a)
    minY = min(minY, b)
    maxX = max(maxX, a)
    maxY = max(maxY, b)
    
print((maxX-minX)*(maxY-minY))