import sys

x, y = list(map(int, sys.stdin.readline().split()))

answer = (x + y) + y // 10 if x >= y else (x + y) + x // 10

print(answer)