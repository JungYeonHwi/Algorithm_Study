s, k = map(int, input().split())
arr = [s//k for _ in range(k)]
for i in range(s % k) :  
    arr[i] += 1
res = 1
for n in arr :
    res *= n
print(res)