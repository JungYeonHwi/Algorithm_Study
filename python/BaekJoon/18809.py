from sys import stdin
from collections import deque
from itertools import combinations

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = 9876543210

n,m,g,r = map(int, input().split())
board = []
candidate = []
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y] == 2:
            candidate.append((x,y))

answer = 0
def solv():
    select = [0]*(g+r)
    for pos in combinations(candidate,g+r):
        select_color(select,0,pos,[g,r])
    print(answer)
def select_color(select,now,pos,cnt):
    global answer
    if now == g+r:
        answer = max(answer, simul(pos, select))
        return

    if cnt[0] > 0:
        cnt[0] -= 1
        select[now] = 1
        select_color(select,now+1,pos,cnt)
        cnt[0] += 1

    if cnt[1] > 0:
        cnt[1] -= 1
        select[now] = -1
        select_color(select,now+1,pos,cnt)
        cnt[1] += 1

def simul(pos, order):
    visited = [[0] * m for _ in range(n)]
    q = deque()

    for idx in range(g+r):
        x,y = pos[idx]
        color = order[idx]
        visited[x][y] = color
        q.appendleft((x, y, color))

    flower_count = 0
    while q:
        x,y,t = q.pop()

        if visited[x][y] == INF:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited):
                if visited[nx][ny] == 0:
                    if t < 0:
                        visited[nx][ny] = t-1
                        q.appendleft((nx,ny,t-1))
                    else:
                        visited[nx][ny] = t+1
                        q.appendleft((nx,ny,t+1))
                elif abs(visited[nx][ny]) == abs(t)+1 and ((visited[nx][ny] < 0 and t > 0) or (visited[nx][ny] > 0 and t < 0)):
                    flower_count += 1
                    visited[nx][ny] = INF
    return flower_count
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif visited[x][y] == INF:
        return False
    elif board[x][y] == 0:
        return False
    return True
solv()
