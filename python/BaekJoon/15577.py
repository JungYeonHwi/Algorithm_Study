import heapq
n = int(input())
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))

for _ in range(n-1):
    x1 = heapq.heappop(h)
    x2 = heapq.heappop(h)
    heapq.heappush(h, (x1+x2) / 2)
print('{:.6f}'.format(h[0]))