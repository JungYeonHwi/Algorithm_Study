import sys
from itertools import accumulate

input=sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))

SumList=[0]+list(accumulate(A))

Max=0

for i in range(N):
    if i+K<=N:
        Max = max(Max, SumList[i + K] - SumList[i])
    else:
        Max = max(Max, SumList[N] - SumList[i] + SumList[(i + K) % N])

print(Max)
