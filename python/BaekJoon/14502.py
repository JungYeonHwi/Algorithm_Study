import sys
input = sys.stdin.readline

from collections import deque
import copy

def BFS() : 
    global answer
    queue = deque()
    graphCopy = copy.deepcopy(graph)
    
    for i in range(n) : 
        for j in range(m) : 
            if graphCopy[i][j] == 2 : 
                queue.append((i, j))
                
    while queue : 
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graphCopy[nx][ny] == 0 :
                graphCopy[nx][ny] = 2
                queue.append((nx, ny))
    
    cnt = 0
    
    for i in range(n) : 
        cnt += graphCopy[i].count(0)
    
    answer = max(answer, cnt)

def makeWall(cnt) : 
    if cnt == 3 : 
        BFS()
        return
    for i in range(n) : 
        for j in range(m) : 
            if graph[i][j] == 0 : 
                graph[i][j] = 1
                makeWall(cnt + 1)
                graph[i][j] = 0

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n) : 
    graph.append(list(map(int, input().split())))

answer = 0
makeWall(0)
print(answer)