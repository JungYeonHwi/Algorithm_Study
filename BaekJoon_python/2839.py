import sys

num = int(sys.stdin.readline())
dp = [-1] * (num + 1)

if num >= 3 : dp[3] = 1
if num >= 5 : dp[5] = 1

for i in range(6, num + 1) : 
    if dp[i-3] < 0 and dp[i-5] < 0 : dp[i] = -1
    elif dp[i-3] > 0 and dp [i-5] > 0 : dp[i] = 1 + min(dp[i-3], dp[i-5])
    else : dp[i] = 1 + max(dp[i-3], dp[i-5])

for i in range(num+1) : 
    print(i, dp[i], end='\n')

print(dp[num])