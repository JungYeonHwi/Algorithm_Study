from collections import deque

n = int(input())
m = int(input())

graph = [[]*n for _ in range(n+1)]
for _ in range(m) : 
    a, b = map(int,input().split())
    graph[a].append(b) 
    graph[b].append(a) 

cnt = 0
visited = [0]*(n+1) 

def BFS(n) :
    global cnt 
    visited[n] = 1
    queue = deque([n])
    
    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                cnt += 1
                
BFS(1)
print(cnt)