import sys
from collections import deque

visited = []
res = 0


def solution():
    global res, visited
    
    # 수영장이 될 수 있는지 확인하고 되면 물 양 더하기
    def bfs(x, y, h):
        global res, visited

        que = deque([x, y])
        
        flag = True  # 수영장이 될 수 있는지 체크하는 변수

        visited[x][y] = True
        cnt = 1
        while que:
            x, y = que.popleft()

            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]
                # 수영장 밖으로 물이 넘치면 flag False로 하고 연결된 나머지 전부 체크(수영장이 안되는 위치 전부)
                if nx == -1 or nx == N or ny == -1 or ny == M:
                    flag = False
                    continue
                
                if board[nx][ny] <= h and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append([nx, ny])
                    cnt += 1
        if flag:
            res += cnt

    N, M = map(int, input().split())
    board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    
    # 수면을 1부터 8까지 올리면서 확인
    for num in range(1, 9):
        visited = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                # 현재 수면보다 낮고 아직 체크 안한 곳
                if board[i][j] <= num and not visited[i][j]:
                    bfs(i, j, num)
    print(res)


solution()
