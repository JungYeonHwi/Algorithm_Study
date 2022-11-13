n = int(input())

for _ in range(n) : 
    m = int(input())
    karr = []
    darr = []
    aarr = []
    answer = 0
    
    for i in range(m) : 
        K, D, A = map(int, input().split())
        karr.append(K)
        darr.append(D)
        aarr.append(A)    
    k, d, a = map(int, input().split())
    
    for aa, bb, cc in zip(karr, darr, aarr) : 
        value = aa * k - bb * d + cc * a
        
        if value <= 0 : answer += 0
        else : answer += value
    
    print(answer)