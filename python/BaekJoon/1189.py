n, m, K = map(int, input().split())
graph = [list(input()) for _ in range(n)]
answer = 0

def fun(x, y, k):
    global answer
    if k == K:
        if (x, y) == (0, m - 1): answer += 1
    else:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'T':
                graph[nx][ny] = 'T'
                fun(nx, ny, k + 1)
                graph[nx][ny] = '.'

graph[n - 1][0] = 'T' 
fun(n - 1, 0, 1)
print(answer)