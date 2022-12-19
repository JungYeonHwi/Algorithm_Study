from sys import stdin
input = stdin.readline

dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

def DFS(depth, r, c, char, gr, gc) :
    if (r, c) == (gr, gc) and depth >= 4:
        print("Yes")
        exit()

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < R and 0 <= nc < C) or board[nr][nc] != char:
            continue
        if not check[nr][nc] :
            check[nr][nc] = 1
            DFS(depth+1, nr, nc, board[nr][nc], gr, gc)
            check[nr][nc] = 0

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
check = [[0] * C for _ in range(R)]
for sr in range(R) :
    for sc in range(C):
        DFS(0, sr, sc, board[sr][sc], sr, sc)
print("No")