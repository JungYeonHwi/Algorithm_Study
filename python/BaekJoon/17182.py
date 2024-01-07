import sys

def recursive(pos, cnt, cost):
    global result

    if cnt == N:
        result = min(result, cost)
        return

    for next in range(N):
        if not visit[next]:
            visit[next] = True
            recursive(next, cnt + 1, cost + graph[pos][next])
            visit[next] = False

N, K = map(int, sys.stdin.readline().split())
graph = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]

# 1. 플로이드 와샬. 모든 정점 최단 거리 구하기
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

visit = [False] * N
result = int(1e9)
visit[K] = True

# 2. 행성을 백트래킹으로 탐색하여 모든 행성 방문하여 최소 시간 구하기
recursive(K, 1, 0)
print(result)
