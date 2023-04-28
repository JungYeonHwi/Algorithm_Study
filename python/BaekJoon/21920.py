from sys import stdin
from collections import defaultdict
from math import gcd

dp = defaultdict(int)

n = int(stdin.readline().rstrip())
seq = list(map(int, stdin.readline().rstrip().split()))
x = int(stdin.readline().rstrip())

total, cnt = 0, 0
for num in seq:
    if not dp[num]:
        dp[num] = gcd(x, num)
    if dp[num] == 1:
        total += num
        cnt += 1

print(total / cnt)