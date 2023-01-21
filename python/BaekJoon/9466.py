def dfs(i):
    visited[i] = True
    team.append(i)
    x = arr[i]
    if visited[x]:
        if x in team:
            global cnt
            cnt += len(team[team.index(x):])
    else:
        dfs(x)

import sys
sys.setrecursionlimit(1000001)
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [True] + [False] * n

    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            team = []
            dfs(i)
    print(n - cnt)
