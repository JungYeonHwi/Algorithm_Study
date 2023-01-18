n, m = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n+1)]

dp[1][1] = 1
for y in range(1, n+1) :
    for x in range(1, m+1) :
        dx = x+1
        dy = y+1
        
        if 0 < dx <= m : dp[y][dx] += dp[y][x]
        if 0 < dy <= n : dp[dy][x] += dp[y][x]
        if 0 < dx <= m and 0 < dy <= n : dp[dy][dx] += dp[y][x]
            
print(dp[-1][-1]%1000000007)