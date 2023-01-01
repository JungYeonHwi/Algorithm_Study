import sys
import math

t = int(sys.stdin.readline())
while t:
    t-=1
    n = int(sys.stdin.readline())
    lis = list(map(int, sys.stdin.readline().split()))
    pSum = []
    cnt = 0
    for item in lis :
        cnt += item
        pSum.append(cnt)
    maxValue =- math.inf
    for i in range(len(pSum)) :
        for j in range(i, len(pSum)) :
            maxValue = max(pSum[j] - pSum[i] + lis[i], maxValue)
    sys.stdout.write(str(maxValue)+'\n')