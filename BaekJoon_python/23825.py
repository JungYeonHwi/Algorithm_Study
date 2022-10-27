import sys
input = sys.stdin.readline

n, m = map(int, input().split())

temp = min(n, m)

print(temp // 2)