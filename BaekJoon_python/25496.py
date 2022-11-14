p, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

i = 0

for _ in range(n) : 
    if p >= 200 : break

    p += arr[i]
    i += 1
    
print(i)