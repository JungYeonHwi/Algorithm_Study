n, m = map(int, input().split())

arr = []

for idx in range(1, m+1) : 
    arr.append([idx, 0])

for _ in range(n) : 
    value = list(map(int, input().split()))
    
    for i in range(m) : 
        if value[i] == 1 : arr[i][1] += 1
        
arr.sort(key = lambda x : -x[1])

answer = []

for a in arr : 
    answer.append(a[0])
    
print(*answer)