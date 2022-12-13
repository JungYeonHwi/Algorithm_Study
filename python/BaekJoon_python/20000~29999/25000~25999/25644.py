import sys
input = sys.stdin.readline

N = int(input())
ANA = list(map(int, input().split()))
benefit, result = 0, 0

for i in range(N-1, -1, -1) :
    benefit = max(benefit, ANA[i])
    result = max(result, benefit - ANA[i])

print(result)