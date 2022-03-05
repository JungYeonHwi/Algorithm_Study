arr = list(map(int, input().split()))

m = 1

while 1 : 
    cnt = 0
    
    for i in range(5) : 
        if m >= arr[i] and m % arr[i] == 0 : cnt += 1
    if cnt >= 3 : break
    
    m += 1
    
print(m)