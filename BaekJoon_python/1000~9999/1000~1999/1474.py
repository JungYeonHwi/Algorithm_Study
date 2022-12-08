import sys

input = sys.stdin.readline
n, m = map(int, input().split())
data = [input().rstrip() for _ in range(n)]

basic, r = divmod(m - sum(map(len, data)), n - 1)

result = data[0]

for idx in range(1, n) :
    if data[idx][0].islower() and r != 0 :
        r -= 1
        result += '_' * (basic + 1) + data[idx]
    elif idx + r == n :
        r -= 1
        result += '_' * (basic + 1) + data[idx]
    else :
        result += '_' * basic + data[idx]
print(result)