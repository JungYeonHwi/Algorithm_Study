n = int(input())
tList = []
pList = []
dp = []

for _ in range(n) : 
    a, b = map(int, input().split())
    
    tList.append(a)
    pList.append(b)
    dp.append(b)
dp.append(0)
    
for i in range(n - 1, -1, -1) :
    if tList[i] + i > n :
        dp[i] = dp[i + 1]
    else :
        dp[i] = max(dp[i + 1], pList[i] + dp[i + tList[i]])

print(dp[0])