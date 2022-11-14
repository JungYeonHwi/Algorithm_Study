import sys
input = sys.stdin.readline

n = int(input())

card = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n) :
    m = 0
    for j in range(i) :
        if card[j] < card[i] :
            m = max(m, dp[j])
        
    dp[i] = m + 1

print(max(dp))