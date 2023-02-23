N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dp = [[0] * N for _ in range(N)] 
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break
        cnt = field[i][j]

        if j + cnt < N : dp[i][j + cnt] += dp[i][j]

        if i + cnt < N : dp[i + cnt][j] += dp[i][j]
