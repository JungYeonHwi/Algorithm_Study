import sys
import heapq
t = int(sys.stdin.readline())
heap = []

for _ in range(t) : 
    n = int(sys.stdin.readline())
    
    if n : heapq.heappush(heap, (-n, n))
    else : 
        if len(heap) >= 1 : print(heapq.heappop(heap)[1])
        else : print(0)