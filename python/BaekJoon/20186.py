import sys

n, k = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
sum = 0
for i in range(1, k+1) : 
    sum += arr[-i] - i + 1
print(sum)