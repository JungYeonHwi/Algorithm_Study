from collections import deque
import heapq
import sys
input = sys.stdin.readline

N = int(input())
queue = deque(list(map(int,input().split())))
curNum = 1
count = 0

while queue:
    x = queue.popleft()
    if x == curNum : curNum += 1
    else : count += 1

print(count)