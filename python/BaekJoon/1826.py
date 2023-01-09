import sys
import heapq

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
arrive, fuel = map(int, input().split())
ans = 0
info.append([arrive, 0])
info.sort()
heap = []

for i in range(len(info)):
    if fuel - info[i][0] < 0:
        while heap:
            fuel += -heapq.heappop(heap)
            ans += 1
            if fuel - info[i][0] >= 0:
                break
    if len(heap) == 0 and fuel - info[i][0] < 0:
        ans = -1
        break
    else:
        heapq.heappush(heap, -info[i][1])

print(ans)