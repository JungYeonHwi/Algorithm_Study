n = int(input())
dp = [1]*117
for i in range(4, n+1) :
    dp[i] = dp[i-3] + dp[i-1]
print(dp[n])