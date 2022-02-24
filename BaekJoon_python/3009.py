xNums = []
yNums = []

for i in range(3):
    x, y = map(int, input().split())
    xNums.append(x)
    yNums.append(y)

for i in range(3):
    if xNums.count(xNums[i]) == 1:
        x4 = xNums[i]
    if yNums.count(yNums[i]) == 1:
        y4 = yNums[i]
print(x4, y4)