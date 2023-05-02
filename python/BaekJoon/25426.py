import sys
input = sys.stdin.readline
t = int(input())
s = []
for _ in range(t):
    a, b = map(int, input().split())
    s.append([a, b])
s.sort()
re = 0
for i in range(t) :
    re += (s[i][0] * (i + 1) + s[i][1])
print(re)