n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

for _ in range(m) : 
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
    
print(*arr)