x, y = map(int, input().split())
xList = [0, x]
yList = [0, y]

n = int(input())

for _ in range(n) :
    xy, length = map(int, input().split())
    if xy == 0 :
        yList.append(length)
    else:
        xList.append(length)
        
xList.sort()
yList.sort()

maxSquare = 0
for i in range(1, len(xList)) :
    for j in range(1, len(yList)) :
        width = xList[i] - xList[i-1]
        height = yList[j] - yList[j-1]
        maxSquare = max(maxSquare, width * height)

print(maxSquare)