import sys
input = sys.stdin.readline

n = int(input())

s = 0
for i in range(1, n+1) :
    s += (n//i)*i

print(s)