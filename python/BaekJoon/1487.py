import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
costs.sort()

dp = [0] * N
maxProfit = 0
answers = []
for i in range(N):
    for j in range(i, N):
        tmp = costs[i][0] - costs[j][1]
        if tmp > 0:
            dp[i] += tmp
    if maxProfit <= dp[i]:
        if maxProfit < dp[i]:
            answers = []
        maxProfit = dp[i]
        answers.append(costs[i][0])
print(min(answers) if answers else 0)