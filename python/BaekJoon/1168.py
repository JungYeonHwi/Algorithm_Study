import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1, N+1)])
answer = []

while dq :
    dq.rotate(-K+1)
    answer.append(str(dq.popleft()))

sys.stdout.write("<"+", ".join(answer)+">")