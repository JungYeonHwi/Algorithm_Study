import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N = int(input())
Q = []
for _ in range(N) :
    n = float(input())
    heappush(Q, n)

for _ in range(7) :
    n = heappop(Q)
    print(f'{n:.3f}')