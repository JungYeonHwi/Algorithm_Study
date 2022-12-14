import sys
from collections import deque

def DFS(n) :
    print(n, end=' ')
    visited[n] = True
    for i in graph[n] :
        if not visited[i] :
            DFS(i)

def BFS(n) :
    visited[n] = True
    queue = deque([n])
    
    while queue :
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1) :
    graph[i].sort()

DFS(v)
visited = [False] * (n + 1)
print()
BFS(v)