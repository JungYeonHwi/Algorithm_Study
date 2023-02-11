import sys
input = sys.stdin.readline

N = int(input())
p = sorted([sorted(map(int, input().split())) for i in range(N)])
dp = [1 for i in range(N)]
for i in range(1, N):
    for j in range(i):
        if p[i][1] >= p[j][1]: dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
