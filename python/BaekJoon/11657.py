import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))

distance = [math.inf for _ in range(n)]
distance[0] = 0
notValid = False

for i in range(n):
    for vertex in range(n):
        for nextVertex, time in graph[vertex]:
            tempTime = distance[vertex] + time
           
            if tempTime < distance[nextVertex]:
                distance[nextVertex] = tempTime
    
                if i == n - 1:
                    notValid = True

if notValid:
    print(-1)
else:
    for i in range(1, n):
        print(distance[i] if distance[i] != math.inf else -1)
