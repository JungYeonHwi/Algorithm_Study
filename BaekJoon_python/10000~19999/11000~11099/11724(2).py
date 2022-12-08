import sys
from collections import deque
sys.setrecursionlimit(10000)

def BFS(n) :
    visited[n] = True
    queue = deque([n])
    
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
            
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
count = 0
    
for k in range(1, n + 1) : 
    if not visited[k] : 
        BFS(k)
        count += 1
        
print(count)