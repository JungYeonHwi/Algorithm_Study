import sys

input = sys.stdin.readline
xArr = []
yArr = []
for _ in range(int(input())) :
    x, y = map(int, input().split())
    xArr.append(x)
    yArr.append(y)
print((max(xArr) - min(xArr)) * (max(yArr) - min(yArr)))