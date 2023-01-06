import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(input().rstrip()))


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(x, y, cnt):
    value = -1
    q = deque()
    q.append((x,y,cnt))
    visited[x][y] = 1
    while q:
        x, y, curCnt = q.popleft()
        if value < curCnt:
            value = curCnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' and visited[nx][ny] == 0 :
                q.append((nx,ny,curCnt+1))
                visited[nx][ny] = 1
    return value

m = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[0] * (m) for _ in range(n)]
            m = m(m,BFS(i,j,0))
print(m)