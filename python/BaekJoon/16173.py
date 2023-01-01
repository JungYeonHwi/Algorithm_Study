import sys

n = int(sys.stdin.readline())
square = []
for _ in range(n):
    square.append(list(map(int, sys.stdin.readline().split())))
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    if x >= n or y >= n:
        return False

    value = square[x][y]
    if value == -1:
        print("HaruHaru")
        exit(0)

    if not visited[x][y]:
        visited[x][y] = True
        dfs(x + value, y) 
        dfs(x, y + value) 

dfs(0, 0)
print("Hing")