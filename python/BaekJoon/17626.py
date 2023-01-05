N = int(input())
dp = [0,1]

for i in range(2, N+1):
    value = 1e9
    j = 1

    while (j**2) <= i :
        value = min(value, dp[i - (j**2)])
        j += 1

    dp.append(value + 1)
print(dp[N])