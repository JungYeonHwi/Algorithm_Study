import sys

sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
lines = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    lines[a].append(b)
    lines[b].append(a)
dp = [[0, 0] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]


def dfs(r):
    visited[r] = 1
    dp[r][0] = 1
    for i in lines[r]:
        if not visited[i]:
            dfs(i)
            dp[r][0] += min(dp[i][0], dp[i][1])
            dp[r][1] += dp[i][0]


dfs(1)
print(min(dp[1][0], dp[1][1]))
