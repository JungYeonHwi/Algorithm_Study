import sys

n, m=map(int, sys.stdin.readline().split())
tmp = [i+1 for i in range(n)]

for _ in range(m) :
    a, b=map(int,sys.stdin.readline().split())
    tmp[a-1:b] = tmp[a-1 : b][::-1]
    
print(*tmp)
