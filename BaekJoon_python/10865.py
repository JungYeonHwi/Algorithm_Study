import sys

n, m = map(int,sys.stdin.readline().split())

arr = [0 for _ in range(n+1)]

for _ in range(m) : 
    a, b=map(int,sys.stdin.readline().split())
    
    arr[a] += 1
    arr[b] += 1
    
for i in range(1, n+1) : 
    print(arr[i])