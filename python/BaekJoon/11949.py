n, m = map(int, input().split(" "))
arr = []

for i in range(n) : 
    arr.append(int(input()))
    
for i in range(1, m+1) : 
    for j in range(1, len(arr)) : 
        if arr[j-1] % i > arr[j] % i : arr[j-1], arr[j] = arr[j], arr[j-1]
        
for i in arr : 
    print(i)