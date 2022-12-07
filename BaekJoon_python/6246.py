n, q = map(int, input().split())
arr = [0 for _ in range(n)]

for _ in range(q) : 
    a, b = map(int, input().split())
    for i in range(a-1, len(arr), b) : 
        arr[i] = 1

print(arr.count(0))