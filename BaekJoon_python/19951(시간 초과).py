import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m) : 
    a, b, k = map(int, input().split())
    for i in range(a-1, b) : 
        arr[i] += k
    
print(*arr)