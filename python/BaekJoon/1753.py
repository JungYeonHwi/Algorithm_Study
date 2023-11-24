import sys
import heapq
input = sys.stdin.readline
INF = 100000000

V,e = map(int, input().split())
start = int(input())
data = [[] for _ in range(V+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    data[u].append((v, w))

distance = [INF]*(V+1)

q = []
def dijkstra(start):
    distance[start] = 0 
    heapq.heappush(q,(0,start))
    while q:
        # print(q)
        # print(data)
        # print(distance)
        dist, now_node = heapq.heappop(q)
        for n_n, weight in data[now_node]:
            cost = dist + weight
            if cost < distance[n_n]:
                distance[n_n] = cost
                heapq.heappush(q,(cost,n_n))

dijkstra(start)
for i in distance[1:]:
    if i != INF:
        print(i)
    else:
        print("INF")
