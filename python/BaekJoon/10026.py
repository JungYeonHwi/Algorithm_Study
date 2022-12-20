from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y) : 
    
    q.append((x, y))
    visited[x][y] = 1
                
    while q : 
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and not visited[nx][ny] :
                visited[nx][ny] = 1
                q.append((nx,ny))

n = int(input())
graph = [list(input()) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
q = deque()

three = 0
two = 0
    
for i in range(n) : 
    for j in range(n) : 
        if not visited[i][j] : 
            BFS(i, j)
            three += 1

for i in range(n) : 
    for j in range(n) :
        if graph[i][j] == "G" : 
            graph[i][j] = "R"
            
visited = [[0] * n for _ in range(n)]
for i in range(n) : 
    for j in range(n) : 
        if not visited[i][j] : 
            BFS(i, j)
            two += 1
            
print(three, two)