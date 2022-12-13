def DFS(node) :
    for n in graph[node] :
        if visited[n] == 0 : 
            visited[n] = visited[node] + 1
            DFS(n)
        
            
n = int(input())
s, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

m = int(input())

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1) :
    graph[i].sort()
    
DFS(s)

print(visited[e] if visited[e] > 0 else -1)