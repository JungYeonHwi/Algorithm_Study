def check(n) : 
    s = 0
    cnt = 0
    for i in range(n-1) : 
        for j in range(i+1, n) : 
            s += i * j
            cnt += 1
            
    return cnt

n = int(input())
print(check(n))
print(2)