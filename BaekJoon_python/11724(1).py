import sys
sys.setrecursionlimit(10000)

def DFS(n) :
    visited[n] = True
    for i in graph[n] :
        if not visited[i] :
            DFS(i)
            
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
        DFS(k)
        count += 1
        
print(count)