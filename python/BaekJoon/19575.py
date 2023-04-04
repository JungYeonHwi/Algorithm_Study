import sys

cnt = 0
n, x = map(int, sys.stdin.readline().split())
index = [0] * (n+1)
for i in range(n+1) :
    a, ai = map(int, sys.stdin.readline().split())
    index[ai] = a
index = index[::-1]
start = index[0] * x + index[1]
 
for i in range(2, n+1) :
    start = start * x + index[i]
    start %= (10 ** 9 + 7)
    
print(start)
