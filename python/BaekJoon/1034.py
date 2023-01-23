n, m = tuple(map(int, input().split()))
arr = []

for _ in range(n):
    arr.append(input())
    
k = int(input())

cnt = 0

for col in range(n) :
    zero = 0
    for num in arr[col] :
        if num == '0' :
            zero += 1
        
    i = 0
    if zero <= k and zero%2 == k%2 : 
        for col2 in range(n) : 
            if arr[col] == arr[col2] : 
                i += 1 
                
    cnt = max(cnt, i)  
    
print(cnt)